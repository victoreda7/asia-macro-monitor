atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-08T07:02:46.472765+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1237
  🇨🇳 China          784
  🇹🇼 Taiwan         268
  🇰🇷 Coreia do Sul  711

## O que já está no feed (não repita)

  - [korea] South Korea shares log second weekly decline as chipmakers drag
  - [taiwan] Table: Taiwan Semiconductor Mfg Sep Rev NT$511.86B Vs NT$330.98B
  - [japan] "With the weak yen and rising prices..." Family trip to Hawaii → Save money on food Cocorico Endo's wife confe
  - [china] Parties name 16 committee conveners for new Legislative Yuan session
  - [japan] Prime Minister: “Consumption tax cut will not affect social security revenue” Thoughts on Yano Farmer Inherita
  - [china] Table: Yuan Jen Enterprises Sep Rev NT$907.1M Vs NT$602.4M
  - [korea] Seoul stocks down for 3rd day amid inflation worries
  - [korea] (URGENT) Seoul stocks down for 3rd day amid inflation worries
  - [china] China's Semiconductor Self-Sufficiency Rate Could Reach 47% in 2030 — Market Talk
  - [korea] Kospi Falls for Third Consecutive Session; Chip Stocks Retreat
  - [japan] Bank of Japan Branch Managers Expect Price Pressures to Broaden
  - [korea] Samsung Stock Unimpressed Even After 783% Profit Growth Forecast
  - [taiwan] TSMC's third-quarter revenue surges 50%, rides on AI wave to beat market forecast
  - [taiwan] TSMC’s third-quarter revenue surges to record, beating market forecast
  - [taiwan] TSMC's Q3 Revenue Hits a Record, Beating Market Forecasts
  - [japan] Bank of Japan sees broadening inflationary pressure
  - [taiwan] TSMC's revenue in the third quarter grows 50% compared to the same period last year, exceeding market forecast
  - [japan] Increase in Tohoku, Shikoku Bank of Japan economic judgment, AI demand (Kyodo News)
  - [japan] Bank of Japan raises economic outlook for Tohoku and Shikoku, leaves unchanged for remaining 7 regions = Regio
  - [japan] BOJ: AI demand may push Japan’s inflation above 2% target, impact policy
  - [japan] Bank of Japan maintains economic outlook in 7 regions nationwide (Kyodo News)
  - [korea] Samsung Electronics Projects Surge In Q3 Operating Income, Sales On AI Demand
  - [japan] Bank of Japan upgrades economic view for 2 of 9 regions
  - [japan] Samsung operating profit approximately 8.8 times, new record high due to increased demand for semiconductors
  - [korea] South Korean Won Rises to 4-Week High
  - [korea] Pons: Spot trading opens on Upbit in KRW, BTC, and USDT markets - 08 Oct 2026
  - [korea] Why is SK Hynix stock falling today?
  - [korea] Why is Samsung Electronics stock falling today?
  - [korea] SK Hynix's Solidigm selects Goldman, Morgan Stanley to lead $100B US listing: report
  - [korea] Samsung Electronics Co., Ltd. Stock 12‑Month Price Target Cut to KRW 486160.09, Implies 81% Upside
  - [china] The first day after the holiday! The central bank took action and launched a 1.2 trillion yuan buyout reverse 
  - [japan] Asian currencies rangebound as dollar holds near 18-month high, yen slips
  - [taiwan] AUO subsidiary Darwin shifts toward high-end manufacturing, explores CPO and semiconductor opportunities
  - [china] Yuan steady despite dollar strength during China's Golden Week holiday
  - [korea] S. Korea says no confirmed fuel exports to Russia, vows strict enforcement of export controls
  - [japan] Stock prices fall, profit-taking selling in some semiconductor-related stocks
  - [china] As China and the EU begin crunch trade talks, optimism is in short supply
  - [japan] Yen Holds Steady After Strong Data
  - [taiwan] TSMC Could Deliver Over 40% Revenue Growth into 2027 — Market Talk
  - [korea] Seoul shares extend losses late Thurs. morning amid inflation worries

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
      "published_utc": "2026-10-08T07:02:46+00:00",
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

