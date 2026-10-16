atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-16T07:22:44.520918+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1109
  🇨🇳 China          854
  🇹🇼 Taiwan         326
  🇰🇷 Coreia do Sul  711

## O que já está no feed (não repita)

  - [korea] Seoul stocks rebound over 2% on eased chip rout, Fed bets
  - [japan] Stock price rise Repurchase movement centered on AI/semiconductor related products
  - [japan] Brokerages expect next BOJ rate hike in Dec, further tightening in 2027
  - [korea] Samsung, SK Hynix power S.Korean stock rebound amid extended foreign selling
  - [japan] BOJ's Ueda says anchoring inflation around 2% target becoming more important
  - [japan] Brokerages see next BOJ rate hike in December
  - [japan] Tokyo Century Corporation - Consolidated Subsidiary Aviation Capital Group To Order 75 Airbus Aircraft
  - [korea] Kospi Snaps Seven-Session Losing Streak; Chip, Auto Stocks Advance
  - [china] China central bank chief touted yuan assets to investors, Bloomberg News reports
  - [korea] High interest rates expected due to US price shock... October interest rates remain 'hawkish'
  - [taiwan] Taiwan reportedly plans $4B Texas complex for Nvidia AI supply chain; tightens China AI chip exports
  - [china] Stocktwits AI Roundup: AI Chip Selloff Deepens, CoreWeave Debt Concerns And Apple’s China AI Launch
  - [japan] Japanese Government Bond (JGB) Yields Recover as Risk Aversion Mood Eases
  - [japan] JGB yields rebound as risk-off mode eases
  - [taiwan] Taiwan to curb AI chip sales to China for more U.S. alignment- Bloomberg
  - [china] China's Piecemeal Stimulus Still Insufficient to Boost Domestic Demand — Market Talk
  - [taiwan] Taiwan to Curb AI Chip Exports to China as Part of US Trade Deal
  - [taiwan] Taiwan economic growth in 2026 to be highest in 39 years: CIER
  - [japan] Consumption tax reduction bill agreed to be discussed on 20th; Liberal Democratic Party and Democratic Party o
  - [korea] South Korean Won Extends Losses on Capital Outflows
  - [korea] Korea's manufacturing jobs rise for first time in 27 months
  - [korea] Raising interest rates is necessary to keep prices down, but South Korea and the US central banks are in deep 
  - [korea] Interest rates raised twice, will they stop in October? Bank of Korea considers ‘additional hike’
  - [china] Tardy China Stimulus Sets Up Second Quarter of Sub-Target Growth
  - [korea] People's Power selected candidate Yoon Jae-bok without a second vote in the race for chairman of the..
  - [japan] US Treasury says Japan no longer faces deflationary environment, yen level must change
  - [japan] 95.5% of people feel that prices have “increased”, 88.6% predict one year from now, Bank of Japan announced on
  - [japan] Economic and Fiscal Affairs Minister Jonai denies some reports saying there was no mention of requesting a pos
  - [taiwan] Analysis: TSMC-GF deal moves mature nodes into AI packaging: What it means for China
  - [china] China's yuan poised to strengthen for a third week in a row on strong exports
  - [taiwan] Taiwan's Chun Yuan Steel sees 4Q26 auto surge, expands into AI robotics
  - [taiwan] TSMC's Capex Likely to Surge to US$83 Billion in 2027 — Market Talk
  - [taiwan] TSMC eyes adding facilities in Texas
  - [japan] Japan core inflation likely exceeded BOJ target for first time since December
  - [china] PBOC’s Pan Touts Yuan Assets to Investors at Deutsche Bank Event
  - [japan] Japan 10-Year Yield Rises as BOJ Outlook Mulled
  - [taiwan] TSMC Still Best-Placed in AI Boom — Market Talk
  - [china] The central bank launched a 700 billion yuan buyout reverse repo on October 15, with an additional 6-month ext
  - [japan] [Latest Saizeriya financial results] Prices of Milanese-style Doria increased for the first time in 6 years! 3
  - [taiwan] Taiwan plans $4 bln Texas park to support Nvidia’s AI supply chain - Bloomberg

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
      "published_utc": "2026-10-16T07:22:44+00:00",
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

