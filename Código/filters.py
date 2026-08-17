"""
O núcleo do produto: decidir se uma manchete é macro asiática, de qual país
é, sobre o que fala, e se já vimos ela antes.

Este módulo é puro — não faz rede, não escreve disco. É o que os testes em
test_filters.py cobrem, e é onde vale gastar atenção quando o feed vier sujo.
"""

from __future__ import annotations

import hashlib
import html
import re
import unicodedata
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone, timedelta
from urllib.parse import urlsplit

import asia_config as cfg


# ---------------------------------------------------------------------------
# Modelo
# ---------------------------------------------------------------------------

_TAGS = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")


def _norm_title(s: str) -> str:
    """Tira HTML, desescapa entidades e colapsa espaço."""
    if not s:
        return ""
    return _WS.sub(" ", html.unescape(_TAGS.sub("", s))).strip()


@dataclass
class NewsItem:
    source_id: str
    source_name: str
    title_en: str
    url: str
    published_utc: str                     # ISO 8601 com offset
    title_original: str = ""
    region: str | None = None
    topics: list[str] = field(default_factory=list)
    lang_original: str = "en"
    translated: bool = False
    live_wire: bool = False
    manual: bool = False
    id: str = ""

    def __post_init__(self) -> None:
        # Normaliza aqui, e não em cada coletor: RSS passa pelo parser, mas
        # TradingView e Investing chegam por JSON e escapariam da limpeza.
        self.title_en = _norm_title(self.title_en)
        self.title_original = _norm_title(self.title_original)
        if not self.title_original:
            self.title_original = self.title_en
        if not self.id:
            raw = f"{self.source_id}|{self.url}|{self.title_original}"
            self.id = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> dict:
        return asdict(self)


# ---------------------------------------------------------------------------
# Motivos de descarte — expostos para diagnóstico, não só para o filtro
# ---------------------------------------------------------------------------

KEEP = None  # passes_filter devolve None quando o item fica


def reject_reason(
    title: str,
    scope: str = "global",
    fixed_region: str | None = None,
    domestic_jp: bool = False,
    extra: str = "",
) -> str | None:
    """Devolve o motivo do descarte, ou None se o item deve ficar.

    Devolver o motivo em vez de um booleano é o que permite o modo --explain
    da CLI: quando uma manchete importante some, dá para saber qual regra
    comeu ela em vez de sair mexendo em regex no escuro.
    """
    t = (title or "").strip()

    # Comprimento mínimo depende do script: "日銀、追加利上げを検討" tem 11
    # caracteres e é uma manchete completa, enquanto 11 caracteres em inglês
    # são um fragmento. CJK carrega muito mais informação por caractere.
    if len(t) < (7 if _is_cjk(t) else 14):
        return "titulo-curto"

    has_macro_hint = bool(cfg.MACRO_HINT.search(t))

    # 1. Tape de bolsa sem nada de macro.
    if cfg.STOCK_TAPE_NOISE.search(t) and not has_macro_hint:
        return "tape-de-bolsa"

    # 2. Assunto fora do escopo mesmo com país no título.
    if cfg.NON_ASIA_HEADLINE.search(t):
        return "fora-de-escopo"

    # 3. Lede de outro mercado sem âncora Ásia.
    if cfg.US_LEDE_NO_ASIA.search(t) and not cfg.ASIA_ANCHOR.search(t):
        return "lede-nao-asia"

    # 3b. Outro mercado citado e nenhum dos quatro países no título.
    if cfg.OUTRO_MERCADO.search(t) and cfg.region_of_title(t) is None:
        return "outro-mercado"

    # 4. Precisa casar pelo menos um tópico.
    # O `extra` (tickers do TradingView) conta para tópico, nunca para região.
    topics = cfg.topics_of_title(f"{t} {extra}".strip() if extra else t)
    if not topics:
        # Exceção: RSS doméstico japonês em japonês costuma ser telegráfico
        # ("首相、補正予算を指示") e escapa dos regex em inglês. Se tem kana e
        # tem dica macro, entra como sinalização.
        if domestic_jp and _has_kana(t) and has_macro_hint:
            topics = ["signaling"]
        else:
            return "sem-topico"

    # 5. Precisa ter região.
    if fixed_region:
        return None
    if scope in cfg.REGIONS:
        return None
    if cfg.region_of_title(t) is None:
        return "sem-regiao"

    return None


def classify(
    title: str,
    scope: str = "global",
    fixed_region: str | None = None,
    domestic_jp: bool = False,
    extra: str = "",
) -> tuple[str | None, list[str]]:
    """(região, tópicos) para um título que já passou pelo filtro.

    A região sai do título sempre que ele der um sinal claro — a fonte
    (scope/fixed_region) é só um chute de fallback. Sem isso, uma notícia
    sobre a China que entra pela query "site:reuters.com China" ou pelo RSS
    doméstico japonês fica etiquetada no país da fonte mesmo quando o título
    diz outra coisa (ex.: "Taiwan's 2027 defence spending..." vindo da query
    de China, ou "China exports increased..." vindo do RSS econômico da NHK).
    O `extra` entra apenas na classificação de tópico — ticker relacionado
    não define de que país é a notícia.
    """
    t = (title or "").strip()
    region = cfg.region_of_title(t)
    if region is None:
        region = fixed_region or (scope if scope in cfg.REGIONS else None)

    topics = cfg.topics_of_title(f"{t} {extra}".strip() if extra else t)
    if not topics and domestic_jp and _has_kana(t):
        topics = ["signaling"]
    return region, topics


def _has_kana(s: str) -> bool:
    return any("぀" <= ch <= "ヿ" for ch in s)


def _is_cjk(s: str) -> bool:
    """True se a maior parte do texto for ideograma, kana ou hangul."""
    if not s:
        return False
    dense = sum(
        1 for ch in s
        if "぀" <= ch <= "ヿ" or "一" <= ch <= "鿿" or "가" <= ch <= "힯"
    )
    return dense >= max(4, len(s) * 0.3)


# ---------------------------------------------------------------------------
# Idade e datas
# ---------------------------------------------------------------------------

def is_too_old(published_utc: str, max_days: int = cfg.MAX_ITEM_AGE_DAYS) -> bool:
    dt = parse_dt(published_utc)
    if dt is None:
        return False
    return dt < datetime.now(timezone.utc) - timedelta(days=max_days)


def parse_dt(value: str | None) -> datetime | None:
    """Aceita ISO 8601 e RFC 822 (o formato do pubDate de RSS)."""
    if not value:
        return None
    v = value.strip()
    try:
        dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except ValueError:
        pass
    from email.utils import parsedate_to_datetime
    try:
        dt = parsedate_to_datetime(v)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return None


def to_iso(dt: datetime | None) -> str:
    dt = dt or datetime.now(timezone.utc)
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Deduplicação
# ---------------------------------------------------------------------------

_PUNCT = re.compile(r"[^\w\s]", re.UNICODE)
_SPACE = re.compile(r"\s+")

# Prefixos que os agregadores colam no título e que atrapalham o dedupe.
_PREFIX = re.compile(
    r"^\s*(update \d+[-:]|exclusive[-:]|breaking[-:]|analysis[-:]|"
    r"factbox[-:]|explainer[-:]|corrected[-:]|refile[-:])\s*",
    re.IGNORECASE,
)


def dedupe_key(title_en: str) -> str:
    """Chave de título: sem acento, sem pontuação, sem prefixo de wire."""
    t = _PREFIX.sub("", title_en or "")
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = _PUNCT.sub(" ", t.lower())
    return _SPACE.sub(" ", t).strip()[:120]


def url_key(url: str) -> str | None:
    """Chave de URL: host + path, sem querystring nem barra final.

    Links do Google News não servem como chave (cada query gera um redirect
    diferente para a mesma matéria), então devolvemos None para eles.
    """
    if not url:
        return None
    try:
        parts = urlsplit(url)
    except ValueError:
        return None
    host = parts.netloc.lower().removeprefix("www.")
    if not host or "news.google.com" in host:
        return None
    return f"{host}{parts.path.rstrip('/').lower()}"


def dedupe(items: list[NewsItem]) -> list[NewsItem]:
    """Remove repetidos por URL canônica e por título normalizado.

    Em empate, fica quem tem a melhor procedência: item curado à mão vence
    wire ao vivo, que vence agregador. Isso evita que o TradingView sobrescreva
    a versão da Reuters da mesma notícia.
    """
    def rank(it: NewsItem) -> tuple:
        return (
            0 if it.manual else 1,
            0 if "news.google.com" not in (it.url or "") else 1,
            1 if it.live_wire else 0,
            -len(it.title_en or ""),
        )

    best: dict[str, NewsItem] = {}
    order: list[str] = []

    for it in sorted(items, key=rank):
        keys = [f"t:{dedupe_key(it.title_en)}"]
        uk = url_key(it.url)
        if uk:
            keys.append(f"u:{uk}")

        hit = next((k for k in keys if k in best), None)
        if hit:
            # já temos uma versão melhor; só propaga as chaves novas
            for k in keys:
                best.setdefault(k, best[hit])
            continue

        for k in keys:
            best[k] = it
        order.append(it.id)

    seen, out = set(), []
    for it in best.values():
        if it.id not in seen:
            seen.add(it.id)
            out.append(it)

    out.sort(key=lambda i: parse_dt(i.published_utc) or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    return out
