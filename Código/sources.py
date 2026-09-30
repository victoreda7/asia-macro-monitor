"""
Coletores. Cada função devolve (itens_brutos, status) e nunca levanta exceção:
uma fonte fora do ar vira uma linha vermelha no painel de saúde, não um crash.

Item bruto = dict com title, url, published, source_name. A classificação
(região, tópicos, tradução) acontece depois, no pipeline.
"""

from __future__ import annotations

import base64
import html
import json
import re
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import quote_plus, urlsplit

import asia_config as cfg
from http_util import get_text


class SourceStatus:
    """Resultado de uma coleta, para o painel de saúde da UI.

    `newest` é o item mais recente que a fonte entregou. Existe porque
    responder 200 não significa estar viva: o RSS do Xinhua devolvia XML
    perfeito com notícias de 2018, e sem esse campo a fonte aparecia verde
    enquanto contribuía zero.
    """

    __slots__ = ("source_id", "name", "ok", "count", "error", "newest")

    def __init__(self, source_id: str, name: str, ok: bool, count: int,
                 error: str = "", newest: str = ""):
        self.source_id, self.name = source_id, name
        self.ok, self.count, self.error = ok, count, error
        self.newest = newest

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id, "name": self.name,
            "ok": self.ok, "count": self.count, "error": self.error,
            "newest": self.newest,
        }


# ---------------------------------------------------------------------------
# RSS
# ---------------------------------------------------------------------------

_TAG = re.compile(r"<[^>]+>")
_WS = re.compile(r"\s+")


def _clean(text: str | None) -> str:
    """Tira HTML, desescapa entidades e colapsa espaço.

    O html.unescape importa mais do que parece: sem ele, títulos com &#39;,
    &quot; e &amp;amp; chegam crus na tela — e RSS é cheio deles.
    """
    if not text:
        return ""
    return _WS.sub(" ", html.unescape(_TAG.sub("", text))).strip()


def _local(tag: str) -> str:
    """Nome da tag sem o namespace: '{http://...}item' -> 'item'."""
    return tag.rsplit("}", 1)[-1] if "}" in tag else tag


def normalize_url(url: str, base: str = "") -> str:
    """Resolve URL protocolo-relativa e caminho relativo."""
    url = (url or "").strip()
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/") and base:
        return base.rstrip("/") + url
    return url


def parse_rss(xml_text: str, limit: int, base: str = "") -> list[dict]:
    """Parser tolerante de RSS 2.0, RDF e Atom.

    Percorre a árvore inteira comparando o nome local da tag, então funciona
    igual com feed sem namespace, com namespace RSS 1.0 ou Atom. Fixar o nome
    exato da tag, como eu fazia, perde feeds namespaceados em silêncio.
    """
    if not xml_text:
        return []
    cleaned = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", xml_text)
    try:
        root = ET.fromstring(cleaned)
    except ET.ParseError:
        return []

    items: list[dict] = []
    for node in root.iter():
        if _local(node.tag) not in ("item", "entry"):
            continue

        title = link = pub = src_name = ""
        for child in node:
            loc = _local(child.tag)
            if loc == "title" and child.text and not title:
                title = _clean(child.text)
            elif loc == "link" and not link:
                # RSS põe a URL no texto; Atom põe no atributo href
                link = (child.text or "").strip() or (child.get("href") or "").strip()
            elif loc in ("pubDate", "published", "updated", "date") and child.text and not pub:
                pub = child.text.strip()
            elif loc == "source" and child.text and not src_name:
                src_name = _clean(child.text)

        if title and link:
            items.append({"title": title, "url": normalize_url(link, base),
                          "published": pub, "source_name": src_name})
        if len(items) >= limit:
            break

    return items


def fetch_rss(source: dict) -> tuple[list[dict], SourceStatus]:
    body = get_text(source["url"])
    if body is None:
        err = getattr(__import__("http_util").get_bytes, "last_error", "sem resposta")
        return [], SourceStatus(source["id"], source["name"], False, 0, str(err))
    items = parse_rss(body, cfg.RSS_PER_SOURCE_LIMIT)
    shift = source.get("pub_shift_hours")
    if shift:
        # fonte com relógio errado conhecido (ver asia_config); import local
        # para não criar dependência circular com filters
        from datetime import timedelta
        from filters import parse_dt
        for it in items:
            dt = parse_dt(it.get("published"))
            if dt:
                it["published"] = (dt + timedelta(hours=shift)).isoformat()
    for it in items:
        it["source_name"] = source["name"]
    ok = bool(items)
    return items, SourceStatus(source["id"], source["name"], ok, len(items),
                               "" if ok else "feed vazio ou ilegível")


# ---------------------------------------------------------------------------
# Google News
# ---------------------------------------------------------------------------

GN_TEMPLATE = "https://news.google.com/rss/search?q={q}&hl={hl}&gl={gl}&ceid={ceid}"
GN_DEFAULT_LOCALE = ("en-US", "US", "US:en")

_URL_IN_BLOB = re.compile(rb"https?://[\w\-./%?=&#:+~,]{12,}")


def decode_google_news_url(url: str) -> str:
    """Tenta recuperar a URL canônica de um link do Google News.

    O link vem como /rss/articles/<base64 de um blob protobuf>. Dentro do blob
    a URL do publisher aparece em texto claro. Não é contrato público, então
    é best-effort: se qualquer coisa falhar, devolve o link original, que
    continua funcionando no browser.
    """
    if "news.google.com" not in url:
        return url
    try:
        path = urlsplit(url).path
        marker = "/articles/"
        if marker not in path:
            return url
        token = path.split(marker, 1)[1].split("/")[0].split("?")[0]
        token = token.replace("-", "+").replace("_", "/")
        token += "=" * (-len(token) % 4)
        blob = base64.b64decode(token, validate=False)

        # O blob é protobuf: cada string vem precedida de um varint com o
        # comprimento. Ler esse byte é o que evita arrastar o campo seguinte
        # junto — sem ele a URL sai com um "0" ou "\x01" colado no fim.
        best = b""
        for m in _URL_IN_BLOB.finditer(blob):
            start = m.start()
            cand = m.group(0)
            if start > 0:
                length = blob[start - 1]
                if 20 <= length < 128 and start + length <= len(blob):
                    cand = blob[start:start + length]
            if len(cand) > len(best):
                best = cand
        if not best:
            return url

        out = re.split(r"[\x00-\x20]", best.decode("utf-8", errors="ignore"))[0]
        out = out.rstrip("\\")
        return out if out.startswith("http") and "google.com" not in out else url
    except Exception:
        return url


def _strip_source_suffix(title: str, source_name: str) -> str:
    """Tira o ' - <veículo>' que o Google News cola no fim do título.

    Sem isso a mesma nota que sai nos espelhos regionais do Investing.com
    (Investing.com / Investing.com UK / Investing.com South Africa) chega
    como três títulos "diferentes" só porque o sufixo muda, e sobrevive ao
    dedupe por título — foi assim que a manchete do JV TSMC/Sony se repetiu
    três vezes em 15 minutos no feed. O <source> do GN e o sufixo do título
    vêm do mesmo rótulo, então cortar por match exato é seguro.
    """
    if not title or not source_name:
        return title
    suffix = f" - {source_name}"
    if title.lower().endswith(suffix.lower()):
        return title[: -len(suffix)].rstrip()
    return title


def fetch_google_news(query: dict) -> tuple[list[dict], SourceStatus]:
    # Busca em CJK com o locale en-US/US volta vazia ou quase vazia — o Google
    # News decide o que indexar (e devolve) por edição/idioma da consulta, não
    # só pelo texto. Uma query em coreano ou chinês precisa do locale nativo
    # (ko/KR, zh-CN/CN) pra achar o que existe; foi assim que gn_kr_bok voltava
    # "sem resultados" e gn_cn_pboc voltava só 1 item mesmo com a query certa.
    hl, gl, ceid = query.get("locale", GN_DEFAULT_LOCALE)
    url = GN_TEMPLATE.format(q=quote_plus(query["q"]), hl=hl, gl=gl, ceid=ceid)
    body = get_text(url)
    if body is None:
        return [], SourceStatus(query["id"], query["name"], False, 0, "sem resposta")

    items = parse_rss(body, cfg.GN_PER_QUERY_LIMIT)
    for it in items:
        it["url"] = decode_google_news_url(it["url"])
        # o <source> do GN traz o veículo real; é melhor rótulo que o nome da query
        it["source_name"] = it.get("source_name") or query["name"]
        it["title"] = _strip_source_suffix(it["title"], it["source_name"])
    ok = bool(items)
    return items, SourceStatus(query["id"], query["name"], ok, len(items),
                               "" if ok else "sem resultados")


# ---------------------------------------------------------------------------
# Investing.com
# ---------------------------------------------------------------------------

_NEXT_DATA = re.compile(
    r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', re.S)


def _walk_for_news(node, out: list[dict], depth: int = 0) -> None:
    """Varre o __NEXT_DATA__ procurando qualquer dict que pareça uma notícia.

    O shape da página muda com frequência; procurar pela forma do objeto é
    mais durável do que fixar um caminho de chaves.
    """
    if depth > 12 or len(out) > 200:
        return
    if isinstance(node, dict):
        title = node.get("title") or node.get("headline")
        href = node.get("href") or node.get("url") or node.get("link")
        if isinstance(title, str) and isinstance(href, str) and len(title) > 15:
            if href.startswith("/"):
                href = "https://www.investing.com" + href
            if href.startswith("http"):
                ts = (node.get("publishedAt") or node.get("date")
                      or node.get("publishDate") or "")
                out.append({"title": title.strip(), "url": href,
                            "published": str(ts), "source_name": "Investing.com"})
        for v in node.values():
            _walk_for_news(v, out, depth + 1)
    elif isinstance(node, list):
        for v in node:
            _walk_for_news(v, out, depth + 1)


def fetch_investing() -> tuple[list[dict], SourceStatus]:
    items: list[dict] = []

    rss = get_text(cfg.INVESTING_RSS_URL,
                   headers={"Accept": "application/rss+xml, application/xml, text/xml, */*",
                            "Referer": cfg.INVESTING_HEADLINES_URL})
    if rss:
        for it in parse_rss(rss, 60, base="https://www.investing.com"):
            it["source_name"] = "Investing.com"
            items.append(it)

    page = get_text(cfg.INVESTING_HEADLINES_URL,
                    headers={"Referer": "https://www.investing.com/",
                             "Cache-Control": "no-cache"})
    if page:
        m = _NEXT_DATA.search(page)
        if m:
            try:
                _walk_for_news(json.loads(m.group(1)), items)
            except json.JSONDecodeError:
                pass

    ok = bool(items)
    return items, SourceStatus("investing_live", "Investing (ao vivo)", ok,
                               len(items), "" if ok else "403 ou layout mudou")


# ---------------------------------------------------------------------------
# TradingView News Flow
# ---------------------------------------------------------------------------

def fetch_tradingview() -> tuple[list[dict], SourceStatus]:
    from datetime import datetime, timezone

    items: list[dict] = []
    errors: list[str] = []

    for lang in cfg.TRADINGVIEW_LANGS:
        body = get_text(
            cfg.TRADINGVIEW_NEWS_URL.format(lang=lang),
            headers={"Origin": cfg.TRADINGVIEW_ORIGIN,
                     "Referer": cfg.TRADINGVIEW_ORIGIN + "/news-flow/",
                     "Accept": "application/json"},
        )
        if not body:
            errors.append(f"{lang}: sem resposta")
            continue
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            errors.append(f"{lang}: json inválido")
            continue

        rows = payload.get("items") if isinstance(payload, dict) else payload
        if not isinstance(rows, list):
            errors.append(f"{lang}: shape inesperado")
            continue

        for row in rows:
            if not isinstance(row, dict):
                continue
            title = (row.get("title") or "").strip()
            story = row.get("storyPath") or ""
            if not title or not story:
                continue
            url = story if story.startswith("http") else "https://www.tradingview.com" + story
            ts = row.get("published")
            published = ""
            if isinstance(ts, (int, float)):
                published = datetime.fromtimestamp(ts, timezone.utc).isoformat()
            provider = ((row.get("provider") or {}).get("name")
                        if isinstance(row.get("provider"), dict) else None)
            # Os tickers relacionados ajudam a classificar o tópico (7203 =
            # Toyota sugere indústria), mas NUNCA a região: um item sobre o
            # Fed pode carregar USDJPY e viraria "Japão" por engano.
            simbolos = " ".join(
                str(s.get("symbol") or "")
                for s in (row.get("relatedSymbols") or [])
                if isinstance(s, dict)
            )
            items.append({"title": title, "url": url, "published": published,
                          "source_name": provider or "TradingView",
                          "extra": simbolos})

    ok = bool(items)
    return items, SourceStatus("tradingview_live", "TradingView (ao vivo)", ok,
                               len(items), "; ".join(errors) if not ok else "")


# ---------------------------------------------------------------------------
# Coleta paralela
# ---------------------------------------------------------------------------

def collect_all(include_live: bool = True) -> tuple[list[tuple[dict, dict]], list[SourceStatus]]:
    """Baixa tudo em paralelo.

    Devolve [(item_bruto, meta_da_fonte), ...] e a lista de status. O meta
    carrega scope/fixed_region/domestic_jp, que o filtro precisa depois.
    """
    jobs = []

    for src in cfg.RSS_SOURCES:
        meta = {"source_id": src["id"], "source_name": src["name"],
                "scope": src.get("scope", "global"), "fixed_region": None,
                "domestic_jp": src.get("domestic_jp", False), "live_wire": False}
        jobs.append((lambda s=src: fetch_rss(s), meta))

    for q in cfg.GOOGLE_NEWS_QUERIES:
        meta = {"source_id": q["id"], "source_name": q["name"],
                "scope": "global", "fixed_region": q.get("region"),
                "domestic_jp": False, "live_wire": False}
        jobs.append((lambda x=q: fetch_google_news(x), meta))

    if include_live:
        jobs.append((fetch_investing, {
            "source_id": "investing_live", "source_name": "Investing.com",
            "scope": "global", "fixed_region": None,
            "domestic_jp": False, "live_wire": True}))
        jobs.append((fetch_tradingview, {
            "source_id": "tradingview_live", "source_name": "TradingView",
            "scope": "global", "fixed_region": None,
            "domestic_jp": False, "live_wire": True}))

    raw: list[tuple[dict, dict]] = []
    statuses: list[SourceStatus] = []

    with ThreadPoolExecutor(max_workers=cfg.FETCH_WORKERS) as pool:
        futures = {pool.submit(fn): meta for fn, meta in jobs}
        for fut in as_completed(futures):
            meta = futures[fut]
            try:
                items, status = fut.result()
            except Exception as exc:  # rede é imprevisível; nada derruba a coleta
                items, status = [], SourceStatus(
                    meta["source_id"], meta["source_name"], False, 0,
                    f"{type(exc).__name__}: {exc}"[:100])
            statuses.append(status)
            raw.extend((it, meta) for it in items)

    statuses.sort(key=lambda s: (s.ok, s.name))
    return raw, statuses
