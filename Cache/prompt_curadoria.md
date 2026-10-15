atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-15T09:22:45.813469+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1117
  🇨🇳 China          841
  🇹🇼 Taiwan         315
  🇰🇷 Coreia do Sul  727

## O que já está no feed (não repita)

  - [china] China Q3 growth set to pick up on stimulus, keeping 2026 goal within reach
  - [taiwan] TSMC Weighs Texas Expansion, Holds Talks on Musk's Terafab as AI Demand Outpaces Supply — Update
  - [japan] Japan economy minister says nation no longer in deflation, seeks investor rethink
  - [japan] What is the difference between Switzerland and America? “Japan’s price level” and the world’s real world (LIMO
  - [taiwan] After Elon Musk’s Invitation, TSMC CEO Reportedly Says Open To Working On Terafab But Must Run It
  - [taiwan] TSMC Stock Falls After Blowout Earnings. Musk Talks Could Offset AI Chip Fears. — Barrons.com
  - [taiwan] TSMC CEO sees no sign of a slowdown as chip foundry reports record profit
  - [taiwan] TSMC open to Terafab collaboration but insists on controlling its own plants
  - [japan] Bank of Japan Councilor Koeda: ``We won't be overly cautious about raising interest rates'' (TBS NEWS DIG Powe
  - [taiwan] TSMC is "prudent" for 2027 after recording sixth consecutive quarter of record profits
  - [china] China stocks close at 14-month low as US inflation stokes Fed fears
  - [japan] Bank of Japan Councilor Koeda says 2% underlying inflation rate is "taking hold": Rate hikes should be done in
  - [taiwan] TSMC CEO says profitability has no ceiling, plans High-NA EUV adoption in 2030
  - [taiwan] TSMC beats forecasts as quarterly sales, profits soar
  - [korea] South Korea, Japan agree to extend $10 billion currency swap
  - [taiwan] AI demand highlights Taiwan's semiconductor capabilities: Lai
  - [japan] Japan Industrial Output Falls More Than Estimated
  - [taiwan] TSMC breaks silence on Musk's Terafab: Talks underway, but fab control non-negotiable
  - [korea] Kospi slides over 7% as chip stocks sink
  - [taiwan] TSMC's Q3 net profit hits new quarterly high
  - [taiwan] Earnings Snapshot: Taiwan Semiconductor Manufacturing tops Q3 estimates, gives Q4 revenue guidance above estim
  - [japan] Japan futures fall as Tokyo equities slump, China imports weaken
  - [taiwan] Earnings call transcript: TSMC beats Q3 2026 estimates as stock slips
  - [korea] Seoul shares crash over 7% on chip rout amid AI, inflation woes
  - [japan] ``Don't be overly cautious about raising interest rates'', Bank of Japan's Councilor Koeda gives speech (Asahi
  - [taiwan] Wall St futures drop as hot CPI revives Fed hike concerns; TSMC results in focus
  - [japan] TSE closing price 3318 yen lower, third largest decline
  - [china] China long-dated bond yields hit 15-month low as PBOC keeps cash flowing
  - [korea] (LEAD) Seoul shares crash over 7 pct on chip rout amid AI, inflation woes
  - [japan] Japan's Nikkei slumps 5% as tech stocks hammered by AI, rate hike worries
  - [japan] Japan finance minister: G20 concerned over yields, FX volatility
  - [korea] Kospi Falls for Seventh Straight Session as Chip Stocks Slump
  - [taiwan] Taiwan Semiconductor Manufacturing in charts: Advanced chips drive 79% of Q3 wafer revenue
  - [korea] SK hynix ties U.S. NAND factory to approval for more equipment at China fab - report
  - [taiwan] TSMC Chairman: No Ceiling for TSMC Profitability, But Dramatic Improvement Won't Happen Overnight
  - [china] China launches large-scale economic stimulus package, despite sluggish domestic demand, fiscal support is "lim
  - [taiwan] QCOM, AVGO, NVDA Stocks In Focus As ByteDance Reportedly Closes In On A MediaTek Pact For AI Data Center Chips
  - [taiwan] Taiwan Semiconductor ADR earnings beat by $0.18, revenue topped estimates
  - [taiwan] TSMC Raises 2026 Revenue Growth Forecast to Around 44%
  - [taiwan] TSMC profit soars 69% in another record quarter fueled by AI boom

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
      "published_utc": "2026-10-15T09:22:46+00:00",
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

