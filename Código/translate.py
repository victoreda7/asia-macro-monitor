"""
Detecção de idioma e tradução de títulos para inglês, com cache em disco.

A tradução é o gargalo do pipeline, então três coisas importam aqui:
o cache (chave SHA256 de "idioma|texto"), o paralelismo modesto, e nunca
deixar uma falha de tradução derrubar o item — se não der para traduzir,
o título original segue em frente.

A API translate.googleapis.com/translate_a/single é não oficial. Use com
parcimônia: sem loop agressivo, sem lote gigante.
"""

from __future__ import annotations

import hashlib
import json
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote

import asia_config as cfg
from http_util import get_text


# ---------------------------------------------------------------------------
# Detecção de idioma por faixa Unicode
# ---------------------------------------------------------------------------

def _ranges(text: str) -> tuple[bool, bool, bool]:
    hangul = kana = han = False
    for ch in text:
        if "가" <= ch <= "힯" or "ᄀ" <= ch <= "ᇿ":
            hangul = True
        elif "぀" <= ch <= "ヿ":
            kana = True
        elif "一" <= ch <= "鿿" or "㐀" <= ch <= "䶿":
            han = True
    return hangul, kana, han


_PT_HINTS = (
    " de ", " da ", " do ", " para ", " com ", " não ", " está ", " são ",
    "ções", "ação", "mercado", "juros", "bolsa", "após", "governo", "câmbio",
)


def detect_lang(text: str) -> str:
    """Devolve 'ko' | 'ja' | 'zh-CN' | 'pt' | 'en'."""
    if not text:
        return "en"
    hangul, kana, han = _ranges(text)
    if hangul:
        return "ko"
    if kana:
        return "ja"
    if han:
        return "zh-CN"

    low = f" {text.lower()} "
    if sum(h in low for h in _PT_HINTS) >= 2:
        return "pt"
    return "en"


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

class TranslationCache:
    def __init__(self, path: Path):
        self.path = path
        self._lock = threading.Lock()
        self._data: dict[str, str] = {}
        self._dirty = False
        if path.exists():
            try:
                self._data = json.loads(path.read_text("utf-8"))
            except (json.JSONDecodeError, OSError):
                self._data = {}

    @staticmethod
    def key(lang: str, text: str) -> str:
        return hashlib.sha256(f"{lang}|{text}".encode("utf-8")).hexdigest()

    def get(self, lang: str, text: str) -> str | None:
        with self._lock:
            return self._data.get(self.key(lang, text))

    def put(self, lang: str, text: str, value: str) -> None:
        with self._lock:
            self._data[self.key(lang, text)] = value
            self._dirty = True

    def save(self) -> None:
        with self._lock:
            if not self._dirty:
                return
            self.path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(self._data, ensure_ascii=False), "utf-8")
            tmp.replace(self.path)
            self._dirty = False

    def __len__(self) -> int:
        return len(self._data)


# ---------------------------------------------------------------------------
# Tradução
# ---------------------------------------------------------------------------

_ENDPOINT = "https://translate.googleapis.com/translate_a/single"

# Calendários de era. O tradutor não converte 令和８年 (8º ano da era Reiwa =
# 2026) e às vezes inventa o ano: saiu "Meeting in 2020" em 30/09. Trocar a era
# pelo ano gregoriano ANTES de traduzir resolve, e de quebra muda a chave do
# cache, então traduções antigas erradas são refeitas sozinhas.
_ERAS = {"令和": 2018, "平成": 1988, "昭和": 1925, "民國": 1911, "民国": 1911}
# "中華民國115年" vira só "2026年": se sobrar o "中華", o tradutor lê "China".
_ERA_RE = re.compile(r"(?:中[華华](?=民))?(令和|平成|昭和|民國|民国)\s*([0-9０-９]+|元)\s*年")
_FULLWIDTH = str.maketrans("０１２３４５６７８９", "0123456789")


def normalizar_eras(text: str) -> str:
    def troca(m: re.Match) -> str:
        n = m.group(2)
        ano = 1 if n == "元" else int(n.translate(_FULLWIDTH))
        return f"{_ERAS[m.group(1)] + ano}年"
    return _ERA_RE.sub(troca, text or "")


# Três caminhos, na ordem. O translate_a/single (client=gtx) é o melhor, mas
# o Google bloqueia por IP com 429 ("Sorry...") de tempos em tempos — em
# 10–11/10/2026 bloqueou tanto o Mac quanto o GitHub Actions e toda manchete
# nova saiu sem tradução. O endpoint da extensão do Chrome (clients5) é outro
# limite, e o MyMemory é a rede de segurança (cota anônima ~5 mil caracteres
# por dia, suficiente para os furos de um dia ruim).
_CLIENTS5 = "https://clients5.google.com/translate_a/t"
_MYMEMORY = "https://api.mymemory.translated.net/get"

# Backend que falhou nesta execução não é tentado de novo: um 429 do gtx
# custaria retries e backoff em cada uma das dezenas de manchetes.
_desligados: set[str] = set()
_falhas: dict[str, int] = {}
uso: dict[str, int] = {}
_estado_lock = threading.Lock()
_MAX_FALHAS = 3


def _json_ou_none(url: str):
    body = get_text(url, retries=1, timeout=15)
    if not body or body.lstrip().startswith("<"):
        return None
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return None


def _via_gtx(text: str, lang: str) -> str | None:
    data = _json_ou_none(f"{_ENDPOINT}?client=gtx&sl={lang}&tl=en&dt=t&q={quote(text)}")
    try:
        # formato: [[["traduzido","original",...], ...], ...]
        return "".join(seg[0] for seg in data[0] if seg and seg[0]).strip() or None
    except (IndexError, TypeError, KeyError):
        return None


def _via_clients5(text: str, lang: str) -> str | None:
    data = _json_ou_none(f"{_CLIENTS5}?client=dict-chrome-ex&sl={lang}&tl=en&q={quote(text)}")
    try:
        # ["traduzido"] ou [["traduzido","ja"]]
        out = data[0]
        if isinstance(out, list):
            out = out[0]
        return out.strip() if isinstance(out, str) and out.strip() else None
    except (IndexError, TypeError, KeyError):
        return None


def _via_mymemory(text: str, lang: str) -> str | None:
    data = _json_ou_none(f"{_MYMEMORY}?q={quote(text)}&langpair={quote(lang + '|en')}")
    try:
        if int(data.get("responseStatus", 0)) != 200 or data.get("quotaFinished"):
            return None
        out = (data["responseData"]["translatedText"] or "").strip()
    except (AttributeError, KeyError, TypeError, ValueError):
        return None
    # Cota estourada às vezes vem como texto "traduzido" com status 200.
    if not out or "MYMEMORY WARNING" in out.upper() or out == text:
        return None
    return out


_BACKENDS = (("google", _via_gtx), ("google-ext", _via_clients5), ("mymemory", _via_mymemory))


def _translate_once(text: str, lang: str) -> str | None:
    for nome, fn in _BACKENDS:
        with _estado_lock:
            if nome in _desligados:
                continue
        out = fn(text, lang)
        with _estado_lock:
            if out:
                _falhas[nome] = 0
                uso[nome] = uso.get(nome, 0) + 1
                return out
            _falhas[nome] = _falhas.get(nome, 0) + 1
            if _falhas[nome] >= _MAX_FALHAS:
                _desligados.add(nome)
    return None


def resumo_uso() -> str:
    partes = [f"{k} {v}" for k, v in uso.items()]
    if _desligados:
        partes.append("bloqueados: " + ", ".join(sorted(_desligados)))
    return "; ".join(partes) or "nenhuma chamada"


def translate_items(items, cache: TranslationCache) -> None:
    """Preenche title_en/lang_original/translated in place.

    Só chama a rede para o que não estiver em cache e não for inglês.
    """
    pending = []
    for it in items:
        lang = detect_lang(it.title_original)
        it.lang_original = lang
        if lang == "en":
            it.title_en = it.title_original
            it.translated = False
            continue
        cached = cache.get(lang, normalizar_eras(it.title_original))
        if cached:
            it.title_en = cached
            it.translated = True
        else:
            pending.append((it, lang))

    if not pending:
        return

    lock = threading.Lock()

    def work(job):
        it, lang = job
        with lock:
            time.sleep(cfg.TRANSLATE_PAUSE / max(cfg.TRANSLATE_WORKERS, 1))
        fonte = normalizar_eras(it.title_original)
        out = _translate_once(fonte, lang)
        if out:
            cache.put(lang, fonte, out)
            it.title_en = out
            it.translated = True
        else:
            # falhou: mantém o original, marca como não traduzido.
            it.title_en = it.title_original
            it.translated = False

    with ThreadPoolExecutor(max_workers=cfg.TRANSLATE_WORKERS) as pool:
        list(pool.map(work, pending))

    cache.save()
