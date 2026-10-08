atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-08T13:12:43.351732+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1233
  🇨🇳 China          788
  🇹🇼 Taiwan         275
  🇰🇷 Coreia do Sul  704

## O que já está no feed (não repita)

  - [taiwan] GlobalFoundries will manufacture essential component for AI chips for TSMC in US$2 billion deal
  - [taiwan] GlobalFoundries to make key AI chip component for TSMC in $2 billion deal
  - [taiwan] TSMC Stocks Drop 2% Despite Citi's NT$4,000 Target
  - [taiwan] GlobalFoundries will manufacture a key AI chip component for TSMC
  - [taiwan] GlobalFoundries to make key AI chip component for TSMC
  - [taiwan] GlobalFoundries partners with TSMC to establish US-based production of silicon interposers
  - [korea] New Silkroad Says Unit To Buy 2.67% Stake In I-Aurora For KRW 1,999.99 Million
  - [china] China has no need or intention to weaken yuan for trade edge, central bank says
  - [taiwan] Taiwan Trade Surplus Grows In September
  - [china] China's Central Bank Rejects Claims Yuan Is Undervalued
  - [korea] Samsung, SK hynix face investor test as buybacks wind down
  - [japan] Bank of Japan’s regional economic report “AI-related demand expands and production increases in many regions”
  - [korea] Budget minister calls for 'virtuous cycle' of spending, growth and tax revenue
  - [japan] PM Takaichi rejects "reflationary" label for her economic policies
  - [japan] Prime Minister: “Funding sources for consumption tax reduction will be considered throughout budget formulatio
  - [china] China Central Bank Defends Currency Policy Before EU Trade Talks
  - [china] EU trade chief in talks with China to rebalance 'unsustainable' deficit
  - [china] China PBOC: Daily Yuan FX Turnover Too Big to Manipulate
  - [china] China PBOC: Yuan Undervaluation Claims Are Misconceived
  - [china] China PBOC Says It Doesn't See Yuan as Undervalued
  - [china] China PBOC Says It Never Engaged in Competitive Devaluation to Boost Exports
  - [china] People's Bank of China Says It Doesn't Need to Devalue Yuan to Gain Trade Advantage
  - [china] China PBOC: Yuan Devaluation Didn't Accelerate Export Share Growth
  - [china] China PBOC: Past Yuan Appreciation Did Not Hurt Trade
  - [china] India launches subsidy probe on Chinese insoluble sulphur imports
  - [taiwan] TSMC Sales Are a Big Win for the AI Trade. Why AMD and Other Chip Stocks Are Falling Anyway. — Barrons.com
  - [korea] Seoul shares turn lower after opening up amid inflation worries
  - [taiwan] TSMC Sales Are a Good Sign for the AI Trade. Tech Stocks Are Falling Anyway. — Barrons.com
  - [taiwan] Taiwan September exports hit fresh monthly record on AI demand, US leads
  - [china] Far East Smarter Energy's Units Win Bids, Sign Contracts Worth 1.4 Billion Yuan
  - [korea] S. Korea extends current account surplus in Aug. amid solid exports
  - [taiwan] TSMC achieves record revenue in the 3rd quarter and exceeds market forecasts
  - [japan] BREAKING NEWS: BOJ upgrades economic view of 2 regions on strong AI demand
  - [japan] Yen market price falls slightly; yen sells due to inflation concerns
  - [china] Table: Chun Yuan Steel Industry Sep Rev NT$1.99B Vs NT$1.99B
  - [japan] BofA sees downside risks for USD/JPY
  - [japan] More than 5,000 bankruptcies in the first half of this fiscal year for the second consecutive year, due to the
  - [taiwan] Taiwan Imports Hit New Record
  - [japan] Street economy in September rises for 5 consecutive months Consumption is strong due to holidays
  - [taiwan] Taiwan Exports Hit Record High

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
      "published_utc": "2026-10-08T13:12:43+00:00",
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

