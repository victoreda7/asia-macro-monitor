atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-08T09:02:46.367928+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1232
  🇨🇳 China          782
  🇹🇼 Taiwan         273
  🇰🇷 Coreia do Sul  713

## O que já está no feed (não repita)

  - [japan] More than 5,000 bankruptcies in the first half of this fiscal year for the second consecutive year, due to the
  - [japan] Street economy in September rises for 5 consecutive months Consumption is strong due to holidays
  - [taiwan] Taiwan Exports Hit Record High
  - [taiwan] Taiwan Posts Largest Trade Surplus on Record
  - [china] A sequel with more volume! The central bank will launch a 1.2 trillion yuan buyout reverse repo
  - [korea] Samsung Q3 profit seen surging nearly nine-fold as AI chip demand soars
  - [japan] Prime Minister: “Consumption tax cut will not affect social security revenue” Thoughts on Yano Farmer Inherita
  - [taiwan] Taiwan's Exports Gained Momentum in September
  - [china] China issues third batch of 2026 export quotas for low-sulfur fuel oil, sources say
  - [taiwan] TSMC's Q3 revenue jumps 50% Y/Y to record NT$1.49T, beating market forecast
  - [taiwan] TSMC's Q3 revenue jumps 50% Y/Y to record NT$1.49T, beating estimates
  - [china] China Banking Corp Says Gilbert U. Dee Resigns As Vice Chairman
  - [taiwan] TSMC posts record quarterly revenue, highest-ever September sales
  - [korea] (2nd LD) Seoul shares down for 3rd day amid inflation worries
  - [korea] Seoul shares down for 3rd day amid inflation worries
  - [japan] Consumption tax cut to compensate small and medium-sized farmers
  - [china] Occl Says Government Initiates Countervailing Duty Investigation On Insoluble Sulphur Imports From China Pr
  - [korea] Protec Mems Technology Wins 7.29 Billion Won Order From Samsung Electronics
  - [korea] South Korea shares log second weekly decline as chipmakers drag
  - [taiwan] Table: Taiwan Semiconductor Mfg Sep Rev NT$511.86B Vs NT$330.98B
  - [japan] "With the weak yen and rising prices..." Family trip to Hawaii → Save money on food Cocorico Endo's wife confe
  - [china] Parties name 16 committee conveners for new Legislative Yuan session
  - [japan] Bank of Japan Sakura Report raises economic outlook for Tohoku and Shikoku; companies also believe that AI-rel
  - [china] Table: Yuan Jen Enterprises Sep Rev NT$907.1M Vs NT$602.4M
  - [korea] Seoul stocks down for 3rd day amid inflation worries
  - [japan] BREAKING NEWS: Fast Retailing forecasts 560 bil. yen net profit for year ending next Aug.
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
      "published_utc": "2026-10-08T09:02:46+00:00",
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

