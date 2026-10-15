atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-15T14:52:47.966764+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1121
  🇨🇳 China          845
  🇹🇼 Taiwan         319
  🇰🇷 Coreia do Sul  715

## O que já está no feed (não repita)

  - [japan] Mazda brings part of its supply chain back to Japan with help from robots
  - [japan] Further Possible BOJ Tightening Could Lift Japanese Yen — Market Talk
  - [taiwan] TSMC Stock Falls After Blowout Earnings. Musk Talks Could Offset AI Chip Fears. — Barrons.com
  - [korea] Why is SK hynix ADR stock sliding today?
  - [china] France and Germany to allow UK in EU car policy if it aligns on China tariffs
  - [taiwan] CoreWeave, TSMC, FMC, Rocket Lab, Schwab, and More Stocks That Explain Today's Market — Barrons.com
  - [china] Blast simulation, university probes, robotics fine, AI spies: 7 US-China relations reads
  - [japan] Japan’s Katayama Renews FX Warnings After US CPI Heats Up
  - [japan] India to overtake Japan as 4th-largest economy in 2027 with $4.52 trillion GDP: IMF
  - [taiwan] Taiwan Semiconductor Posts Record Profit
  - [korea] Kospi crashes 8% as Samsung, SK hynix sink over 10%
  - [taiwan] TSMC's Q3 results, outlook pave path for 'banner year' in 2027: analysts
  - [japan] Japan tells G20 authorities must watch FX moves with high sense of urgency, finance minister says
  - [china] The central bank launched a 700 billion yuan buyout reverse repo to increase liquidity support in the fourth q
  - [taiwan] Taiwan Semiconductor Manufacturing Company Limited reports results for the quarter ended September 30 - Earnin
  - [china] China’s central bank chief urges ’comprehensive’ view on global imbalances
  - [taiwan] TSMC evaluating Texas production, cooperation with Terafab
  - [taiwan] Needham maintains Buy rating on Taiwan Semiconductor, $560 price target
  - [japan] Nikkei marks 3rd largest single-day point drop on AI, chip concerns
  - [china] China's yuan may appreciate further, but weak domestic demand and US yields pose risks: Report
  - [japan] Japan economy minister stresses BOJ independence, rejects reflationist label
  - [korea] Why a memory chip glut could be Korea's weapon against China
  - [japan] Komei compiles a proposal to provide approximately 80,000 yen per person for consumption tax reduction
  - [korea] South Korea, Japan extend $10 billion currency swap for three years
  - [japan] Tech sell-off gathers pace as chipmakers hammered By Reuters
  - [taiwan] TSMC eyes Texas and Musk Terafab project for US expansion
  - [japan] Bank of Japan member: ``We won't be overly cautious about raising interest rates,'' indicating a stance of mai
  - [japan] Bank of Japan member: ``We won't be overly cautious about raising interest rates.'' Indicates stance to mainta
  - [japan] Bank of Japan member: ``We won't be overly cautious about raising interest rates.'' Shows stance to maintain i
  - [taiwan] Intel, Marvell, CoreWeave, TSMC, Apple, and More Stocks That Explain Today's Market — Barrons.com
  - [taiwan] TSMC's net profit hits record in third quarter
  - [korea] Hyundai Motor Company Stock 12‑Month Price Target Cut to KRW 592032.26, Implies 89% Upside
  - [china] EU leaders to tackle China exports, energy prices, budget at summit
  - [china] China Resources Power Logs 9M Net Generation Of Subsidiary Power Plants Up 9.7%
  - [japan] Japan economy minister says deflation era is over, urges investor rethink
  - [japan] [Volatility of AI/semiconductor stocks will further increase] Japanese stocks are in turmoil after the US midt
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Subsidiary obtaining fShares
  - [taiwan] TSMC revenue rises 41% as AI chip demand drives growth
  - [japan] Policymaker: BOJ shouldn't be too cautious raising rates
  - [taiwan] Can TSMC earnings help settle AI jitters?

## O que fazer

1. Visite os portais do checklist abaixo, priorizando **oficial e estatal**
   antes de wire. Foque nas últimas 72 horas.
2. Selecione só o que for **macroeconômico**: política monetária, fiscal,
   câmbio, inflação, atividade, comércio, imobiliário, indústria e chips,
   ou sinalização de autoridade. Nada de tape de bolsa, corporativo isolado,
   esporte ou cultura.
3. Responda **só com o JSON** no formato abaixo, num bloco ```json.
   Ele vai ser colado no painel, então nada de texto fora do bloco.

## Checklist por país

**🇯🇵 Japão** (`region: "japan"`)
  - MOF Japan — mof.go.jp (orçamento, emissão de JGB, tributário)
  - Bank of Japan — boj.or.jp/en (statement, minuta, discursos do governador)
  - NHK World English — www3.nhk.or.jp/nhkworld (sem RSS público, precisa de olhada manual)
  - Kyodo News English, Reuters Japan, Nikkei Asia

**🇨🇳 China** (`region: "china"`)
  - PBoC — pbc.gov.cn (OMO, MLF, LPR, compulsório)
  - NBS — stats.gov.cn e Alfândega (GACC) para comércio
  - State Council / 国务院 e comunicados do Politburo
  - Xinhua English, Caixin, SCMP Economy, Yicai

**🇹🇼 Taiwan** (`region: "taiwan"`)
  - CBC — cbc.gov.tw (decisão de juros, gestão do TWD)
  - DGBAS — eng.stat.gov.tw (PIB, CPI) e MOF para comércio
  - Executive Yuan / 行政院 (pacotes fiscais)
  - Focus Taiwan (CNA), Taipei Times, DIGITIMES

**🇰🇷 Coreia do Sul** (`region: "korea"`)
  - Bank of Korea — bok.or.kr/eng (Base Rate, minuta, outlook)
  - KOSTAT e MOTIE (exportação dos 20 primeiros dias do mês)
  - Yonhap English, Korea Herald, KED Global
  - 한국경제 e 매일경제 para a leitura doméstica

## Regras rígidas

- **Nunca invente URL, título ou data.** Se não abriu a página, não inclua.
- `title_en` sempre em inglês. Se a fonte for JA/ZH/KO, traduza você e ponha
  o texto original em `title_original` com o `lang_original` correto.
- `region` é o país principal da notícia, um de: `japan`, `china`, `taiwan`, `korea`.
- `topics` é uma lista com um ou mais de: `monetary`, `fiscal`, `fx`, `inflation`, `activity`, `trade`, `property`, `industrial`, `signaling`.
- `published_utc` em ISO 8601 com offset. Se a fonte só der a data, use 12:00Z.
- Entre 8 e 25 itens. Qualidade acima de volume.

## Formato exato do arquivo

```json
{
  "items": [
    {
      "title_en": "Japan's MOF plans record JGB issuance for FY2027",
      "title_original": "財務省、2027年度の国債発行額を過去最大に",
      "url": "https://www.mof.go.jp/...",
      "region": "japan",
      "topics": ["fiscal"],
      "published_utc": "2026-10-15T14:52:48+00:00",
      "source_name": "MOF Japan",
      "lang_original": "ja"
    }
  ],
  "notes": "opcional — o que você checou e não rendeu nada"
}
```

`title_original`, `lang_original` e `notes` são opcionais. O resto é obrigatório.
Itens sem `title_en`, sem `url` ou com `region` inválida são descartados em
silêncio pelo pipeline.

## Depois de responder

A pessoa cola o JSON no campo **Resultado da IA** do painel e clica em
**Enviar**. O painel grava o arquivo no repositório e dispara uma coleta,
que funde o manual com o automático.

