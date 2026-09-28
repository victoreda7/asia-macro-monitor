#!/usr/bin/env python3
"""
Monta o prompt de curadoria por IA.

    python3 build_prompt.py            imprime o prompt
    python3 build_prompt.py --json     {"ok":true,"prompt":"..."} para o painel

O prompt é autocontido: leva as estatísticas do último feed, o checklist por
país, o schema exato do arquivo de saída e o caminho onde gravar. A IA que
recebe isso não precisa saber nada do projeto.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

import asia_config as cfg

ROOT = Path(__file__).resolve().parent.parent
FEED_PATH = ROOT / "Cache" / "feed.json"
MANUAL_PATH = ROOT / "Cache" / "manual_additions.json"

GATILHO = "atualizar noticias asia"

CHECKLIST = {
    "japan": [
        "MOF Japan — mof.go.jp (orçamento, emissão de JGB, tributário)",
        "Bank of Japan — boj.or.jp/en (statement, minuta, discursos do governador)",
        "NHK World English — www3.nhk.or.jp/nhkworld (sem RSS público, precisa de olhada manual)",
        "Kyodo News English, Reuters Japan, Nikkei Asia",
    ],
    "china": [
        "PBoC — pbc.gov.cn (OMO, MLF, LPR, compulsório)",
        "NBS — stats.gov.cn e Alfândega (GACC) para comércio",
        "State Council / 国务院 e comunicados do Politburo",
        "Xinhua English, Caixin, SCMP Economy, Yicai",
    ],
    "taiwan": [
        "CBC — cbc.gov.tw (decisão de juros, gestão do TWD)",
        "DGBAS — eng.stat.gov.tw (PIB, CPI) e MOF para comércio",
        "Executive Yuan / 行政院 (pacotes fiscais)",
        "Focus Taiwan (CNA), Taipei Times, DIGITIMES",
    ],
    "korea": [
        "Bank of Korea — bok.or.kr/eng (Base Rate, minuta, outlook)",
        "KOSTAT e MOTIE (exportação dos 20 primeiros dias do mês)",
        "Yonhap English, Korea Herald, KED Global",
        "한국경제 e 매일경제 para a leitura doméstica",
    ],
}


def load_feed() -> dict:
    if not FEED_PATH.exists():
        return {}
    try:
        return json.loads(FEED_PATH.read_text("utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def build(web: bool = False) -> str:
    """web=True: versão para o painel na Vercel — a IA devolve o JSON no chat
    e a pessoa cola no painel, em vez de gravar um arquivo no Mac."""
    feed = load_feed()
    items = feed.get("items", [])
    by_region = Counter(i.get("region") for i in items)
    gerado = feed.get("generated_at_utc", "nunca")

    # As manchetes recentes vão no prompt para a IA não repetir o que já temos.
    recentes = sorted(items, key=lambda i: i.get("published_utc", ""), reverse=True)[:40]
    ja_temos = "\n".join(
        f"  - [{i.get('region','?')}] {i.get('title_en','')[:110]}" for i in recentes
    ) or "  (feed vazio)"

    stats = "\n".join(
        f"  {cfg.REGION_FLAG[r]} {cfg.REGION_LABEL[r]:<14} {by_region.get(r, 0):>3}"
        for r in cfg.REGIONS
    )

    checklist = "\n".join(
        f"\n**{cfg.REGION_FLAG[r]} {cfg.REGION_LABEL[r]}** (`region: \"{r}\"`)\n"
        + "\n".join(f"  - {linha}" for linha in CHECKLIST[r])
        for r in cfg.REGIONS
    )

    topicos = ", ".join(f"`{t}`" for t in cfg.TOPIC_ORDER)
    agora = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")

    if web:
        destino = ("3. Responda **só com o JSON** no formato abaixo, num bloco ```json.\n"
                   "   Ele vai ser colado no painel, então nada de texto fora do bloco.")
        depois = ("## Depois de responder\n\n"
                  "A pessoa cola o JSON no campo **Resultado da IA** do painel e clica em\n"
                  "**Enviar**. O painel grava o arquivo no repositório e dispara uma coleta,\n"
                  "que funde o manual com o automático.\n")
    else:
        destino = f"3. Grave o resultado em:\n   `{MANUAL_PATH}`"
        depois = (
            "## Depois de gravar\n\n"
            "Rode a coleta de novo para fundir o manual com o automático:\n\n"
            "```\n"
            f"python3 \"{ROOT / 'Código' / 'fetch_asia_news.py'}\"\n"
            "```\n\n"
            "Ou clique em **Atualizar agora** no painel. O fetcher nunca apaga o\n"
            "manual_additions.json — ele só lê e mistura.\n"
        )

    return f"""{GATILHO}

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: {gerado}
Total: {len(items)} manchetes

{stats}

## O que já está no feed (não repita)

{ja_temos}

## O que fazer

1. Visite os portais do checklist abaixo, priorizando **oficial e estatal**
   antes de wire. Foque nas últimas 72 horas.
2. Selecione só o que for **macroeconômico**: política monetária, fiscal,
   câmbio, inflação, atividade, comércio, imobiliário, indústria e chips,
   ou sinalização de autoridade. Nada de tape de bolsa, corporativo isolado,
   esporte ou cultura.
{destino}

## Checklist por país
{checklist}

## Regras rígidas

- **Nunca invente URL, título ou data.** Se não abriu a página, não inclua.
- `title_en` sempre em inglês. Se a fonte for JA/ZH/KO, traduza você e ponha
  o texto original em `title_original` com o `lang_original` correto.
- `region` é o país principal da notícia, um de: {", ".join(f'`{r}`' for r in cfg.REGIONS)}.
- `topics` é uma lista com um ou mais de: {topicos}.
- `published_utc` em ISO 8601 com offset. Se a fonte só der a data, use 12:00Z.
- Entre 8 e 25 itens. Qualidade acima de volume.

## Formato exato do arquivo

```json
{{
  "items": [
    {{
      "title_en": "Japan's MOF plans record JGB issuance for FY2027",
      "title_original": "財務省、2027年度の国債発行額を過去最大に",
      "url": "https://www.mof.go.jp/...",
      "region": "japan",
      "topics": ["fiscal"],
      "published_utc": "{agora}",
      "source_name": "MOF Japan",
      "lang_original": "ja"
    }}
  ],
  "notes": "opcional — o que você checou e não rendeu nada"
}}
```

`title_original`, `lang_original` e `notes` são opcionais. O resto é obrigatório.
Itens sem `title_en`, sem `url` ou com `region` inválida são descartados em
silêncio pelo pipeline.

{depois}
"""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--json", action="store_true", help="saída JSON para o painel")
    p.add_argument("--web", action="store_true",
                   help="versão do painel web: a IA devolve o JSON em vez de gravar arquivo")
    p.add_argument("--saida", help="grava o prompt neste arquivo em vez de imprimir")
    args = p.parse_args()

    try:
        prompt = build(web=args.web)
    except Exception as exc:
        if args.json:
            print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}))
            return 1
        raise

    if args.json:
        print(json.dumps({"ok": True, "prompt": prompt,
                          "manual_path": str(MANUAL_PATH)}, ensure_ascii=False))
    elif args.saida:
        Path(args.saida).write_text(prompt, encoding="utf-8")
    else:
        print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
