#!/usr/bin/env python3
"""
Asia Macro News Monitor — pipeline principal.

    python3 fetch_asia_news.py             coleta uma vez
    python3 fetch_asia_news.py --watch     loop a cada 300s
    python3 fetch_asia_news.py --no-live   pula Investing e TradingView
    python3 fetch_asia_news.py --explain   mostra por que cada manchete caiu
    python3 fetch_asia_news.py --check     testa as fontes, não grava nada

Ordem: coleta em paralelo → filtro macro → tradução → dedupe → grava
Cache/feed.json e regenera "Monitor de Notícias Macro.html".
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import asia_config as cfg
import filters
import render_html
import sources
from filters import NewsItem
from translate import TranslationCache, translate_items

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "Cache"
FEED_PATH = CACHE / "feed.json"
TRANSLATION_CACHE = CACHE / "translation_cache.json"
SEEN_CACHE = CACHE / "first_seen_cache.json"
MANUAL_PATH = CACHE / "manual_additions.json"
HTML_PATH = ROOT / "Monitor de Notícias Macro.html"


# ---------------------------------------------------------------------------
# Data de primeira vista — para fontes sem pubDate
# ---------------------------------------------------------------------------

class SeenCache:
    """Trava a data de um item sem pubDate confiável no primeiro encontro.

    O RSS 1.0 do Nikkei Asia (e qualquer fonte parecida) não traz data
    nenhuma no item — só title e link. Sem isso, `to_iso(None)` caía para
    "agora", e a mesma matéria de duas semanas atrás voltava com "1 min"
    a cada coleta, para sempre: o item nunca envelhecia porque o próprio
    pipeline reescrevia a data dele em todo run. Este cache resolve isso
    lembrando quando a gente viu o item pela primeira vez e reusando essa
    data nas coletas seguintes, em vez de gerar uma nova a cada vez.
    """

    def __init__(self, path: Path):
        self.path = path
        self._data: dict[str, str] = {}
        self._dirty = False
        if path.exists():
            try:
                self._data = json.loads(path.read_text("utf-8"))
            except (json.JSONDecodeError, OSError):
                self._data = {}

    def get_or_set(self, key: str, now: datetime) -> datetime:
        cached = self._data.get(key)
        if cached:
            dt = filters.parse_dt(cached)
            if dt:
                return dt
        self._data[key] = now.isoformat()
        self._dirty = True
        return now

    def save(self) -> None:
        if not self._dirty:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self._data, ensure_ascii=False), "utf-8")
        tmp.replace(self.path)
        self._dirty = False


# ---------------------------------------------------------------------------
# Curadoria manual
# ---------------------------------------------------------------------------

def load_manual() -> tuple[list[NewsItem], list[str]]:
    """Lê Cache/manual_additions.json. Nunca apaga o arquivo — só lê e mistura.

    Devolve (itens, avisos). Entradas inválidas são puladas com aviso, não
    derrubam a carga: uma vírgula errada do curador não pode custar a coleta.
    """
    if not MANUAL_PATH.exists():
        return [], []
    try:
        data = json.loads(MANUAL_PATH.read_text("utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        return [], [f"manual_additions.json ilegível: {exc}"]

    rows = data.get("items", data) if isinstance(data, dict) else data
    if not isinstance(rows, list):
        return [], ["manual_additions.json: esperava uma lista em 'items'"]

    out, warns = [], []
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            warns.append(f"item {i}: não é objeto")
            continue
        title = (row.get("title_en") or "").strip()
        url = (row.get("url") or "").strip()
        region = (row.get("region") or "").strip().lower()
        if not title or not url:
            warns.append(f"item {i}: sem title_en ou url")
            continue
        if region not in cfg.REGIONS:
            warns.append(f"item {i}: region '{region}' inválida")
            continue
        topics = row.get("topics") or ["signaling"]
        topics = [t for t in topics if t in cfg.TOPIC_PATTERNS] or ["signaling"]
        out.append(NewsItem(
            source_id="manual_ia",
            source_name=row.get("source_name") or "Curadoria IA",
            title_en=title,
            title_original=row.get("title_original") or title,
            url=url,
            published_utc=filters.to_iso(filters.parse_dt(row.get("published_utc"))),
            region=region,
            topics=topics,
            lang_original=row.get("lang_original") or "en",
            translated=bool(row.get("title_original")
                            and row.get("title_original") != title),
            manual=True,
        ))
    return out, warns


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def aplicar_tetos(itens: list[NewsItem]) -> list[NewsItem]:
    """Corta o feed no tamanho final, com duas proteções.

    Item curado à mão nunca é cortado: alguém escolheu ele de propósito, e o
    corte por data eliminava justamente os mais valiosos — comunicado oficial
    de ministério é publicado uma vez por trimestre e fica velho rápido, mas
    não deixa de importar.

    E nenhuma fonte pode ocupar mais que PER_SOURCE_CAP, para que um wire
    tagarela não empurre para fora as fontes que publicam pouco e bem.
    """
    curados = [i for i in itens if i.manual]
    espaco = max(cfg.FEED_ITEM_CAP - len(curados), 0)

    por_fonte: Counter = Counter()
    automaticos: list[NewsItem] = []
    for it in itens:
        if it.manual:
            continue
        if por_fonte[it.source_id] >= cfg.PER_SOURCE_CAP:
            continue
        por_fonte[it.source_id] += 1
        automaticos.append(it)
        if len(automaticos) >= espaco:
            break

    juntos = curados + automaticos
    juntos.sort(
        key=lambda i: filters.parse_dt(i.published_utc)
        or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return juntos


def run_once(include_live: bool = True, explain: bool = False, write: bool = True) -> dict:
    started = time.time()
    print("→ coletando fontes…", flush=True)
    raw, statuses = sources.collect_all(include_live=include_live)
    print(f"  {len(raw)} itens brutos de {len(statuses)} fontes "
          f"({sum(1 for s in statuses if not s.ok)} com problema)", flush=True)

    kept: list[NewsItem] = []
    rejected = Counter()
    examples: dict[str, str] = {}
    newest_by_source: dict[str, datetime] = {}
    seen = SeenCache(SEEN_CACHE)
    now = datetime.now(timezone.utc)

    for row, meta in raw:
        title = row.get("title", "")
        pub = filters.parse_dt(row.get("published"))
        if pub:
            sid = meta["source_id"]
            if sid not in newest_by_source or pub > newest_by_source[sid]:
                newest_by_source[sid] = pub
        extra = row.get("extra", "")
        reason = filters.reject_reason(
            title,
            scope=meta["scope"],
            fixed_region=meta["fixed_region"],
            domestic_jp=meta["domestic_jp"],
            extra=extra,
        )
        if reason:
            rejected[reason] += 1
            examples.setdefault(reason, title[:90])
            continue

        region, topics = filters.classify(
            title, scope=meta["scope"], fixed_region=meta["fixed_region"],
            domestic_jp=meta["domestic_jp"], extra=extra)
        if region not in cfg.REGIONS:
            rejected["sem-regiao"] += 1
            continue

        pub_dt = filters.parse_dt(row.get("published"))
        if pub_dt is None:
            # Sem data na fonte (RSS 1.0 do Nikkei e afins): trava no
            # primeiro encontro em vez de gerar "agora" de novo a cada run.
            seen_key = f"{meta['source_id']}|{filters.dedupe_key(title)}"
            pub_dt = seen.get_or_set(seen_key, now)
        published = filters.to_iso(pub_dt)
        if filters.is_too_old(published):
            rejected["antigo"] += 1
            continue

        kept.append(NewsItem(
            source_id=meta["source_id"],
            source_name=row.get("source_name") or meta["source_name"],
            title_en=title,
            title_original=title,
            url=row.get("url", ""),
            published_utc=published,
            region=region,
            topics=topics,
            live_wire=meta["live_wire"],
        ))

    print(f"→ filtro: {len(kept)} passaram, {sum(rejected.values())} descartados",
          flush=True)
    if explain:
        for reason, n in rejected.most_common():
            print(f"    {reason:<16} {n:>5}   ex.: {examples.get(reason,'')}")

    # Fonte pode responder 200 e ainda assim estar parada. Marca as travadas
    # para elas aparecerem em vermelho no painel em vez de passarem por vivas.
    limite = datetime.now(timezone.utc) - timedelta(days=cfg.STALE_SOURCE_DAYS)
    paradas = 0
    for st in statuses:
        novo = newest_by_source.get(st.source_id)
        if novo:
            st.newest = novo.isoformat()
            if novo < limite and st.ok:
                st.ok = False
                st.error = f"parada desde {novo:%d/%m/%Y}"
                paradas += 1
    if paradas:
        print(f"  ! {paradas} fonte(s) respondem mas estão desatualizadas", flush=True)

    seen.save()

    manual, warns = load_manual()
    for w in warns:
        print(f"  ! {w}", flush=True)
    if manual:
        print(f"→ curadoria: +{len(manual)} itens manuais", flush=True)

    print("→ traduzindo títulos…", flush=True)
    cache = TranslationCache(TRANSLATION_CACHE)
    before = len(cache)
    translate_items(kept, cache)
    print(f"  {len(cache) - before} traduções novas, {len(cache)} em cache", flush=True)

    # Reclassifica tópicos com o título em inglês: um título japonês que só
    # entrou por 'signaling' pode revelar 'fiscal' depois de traduzido.
    for it in kept:
        if it.translated:
            richer = cfg.topics_of_title(it.title_en)
            if richer:
                it.topics = sorted(set(it.topics) | set(richer),
                                   key=cfg.TOPIC_ORDER.index)

    merged = aplicar_tetos(filters.dedupe(kept + manual))
    by_region = Counter(i.region for i in merged)

    feed = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "count": len(merged),
        "by_region": {r: by_region.get(r, 0) for r in cfg.REGIONS},
        "elapsed_s": round(time.time() - started, 1),
        "sources": [s.to_dict() for s in statuses],
        "items": [i.to_dict() for i in merged],
    }

    if write:
        CACHE.mkdir(parents=True, exist_ok=True)
        tmp = FEED_PATH.with_suffix(".tmp")
        tmp.write_text(json.dumps(feed, ensure_ascii=False, indent=1), "utf-8")
        tmp.replace(FEED_PATH)
        render_html.render(feed, HTML_PATH)
        print(f"→ gravado: {FEED_PATH.name} e {HTML_PATH.name}", flush=True)

    resumo = "  ".join(f"{cfg.REGION_FLAG[r]} {by_region.get(r,0)}" for r in cfg.REGIONS)
    print(f"✓ {len(merged)} manchetes em {feed['elapsed_s']}s   {resumo}", flush=True)
    return feed


def check_sources() -> int:
    """Testa cada fonte e imprime um relatório. Não grava nada."""
    _, statuses = sources.collect_all(include_live=True)
    bad = [s for s in statuses if not s.ok]
    for s in sorted(statuses, key=lambda x: (x.ok, x.name)):
        mark = "ok  " if s.ok else "FALHA"
        print(f"{mark} {s.name:<26} {s.count:>4}  {s.error}")
    print(f"\n{len(statuses) - len(bad)}/{len(statuses)} fontes respondendo.")
    return 1 if len(bad) > len(statuses) // 2 else 0


def main() -> int:
    p = argparse.ArgumentParser(description="Asia Macro News Monitor")
    p.add_argument("--watch", action="store_true", help="loop contínuo")
    p.add_argument("--interval", type=int, default=300, help="segundos entre coletas")
    p.add_argument("--no-live", action="store_true", help="pula Investing e TradingView")
    p.add_argument("--explain", action="store_true", help="mostra os motivos de descarte")
    p.add_argument("--check", action="store_true", help="só testa as fontes")
    args = p.parse_args()

    if args.check:
        return check_sources()

    if not args.watch:
        run_once(include_live=not args.no_live, explain=args.explain)
        return 0

    print(f"modo watch: a cada {args.interval}s. Ctrl+C para sair.\n", flush=True)
    while True:
        try:
            run_once(include_live=not args.no_live, explain=args.explain)
        except KeyboardInterrupt:
            print("\nencerrado.")
            return 0
        except Exception as exc:
            print(f"! erro na coleta: {type(exc).__name__}: {exc}", flush=True)
        try:
            time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\nencerrado.")
            return 0


if __name__ == "__main__":
    raise SystemExit(main())
