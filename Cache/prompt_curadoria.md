atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-12T07:22:43.167719+00:00
Total: 3000 manchetes

  🇯🇵 Japão          961
  🇨🇳 China          888
  🇹🇼 Taiwan         313
  🇰🇷 Coreia do Sul  838

## O que já está no feed (não repita)

  - [japan] Dollar rises to 19-month high as Fed hike bets grow, yen wobbles
  - [japan] Meiji: Pharmaceutical strength offsets Food pressure; FY operating profit guidance holds at JPY 100.0bn
  - [china] Global EV sales bounce back in October on European gains and Chinese exports
  - [japan] Sumitomo Mitsui Trust Group, Inc. - To Buy Back Up To 1.6% Of Shares Worth 50 Billion Yen
  - [korea] Hanwha Life Insurance: 9M earnings and CSM grew, while Q3 volatility drove KRW 431bn in investment losses
  - [japan] JAPAN MATERIAL: Semiconductor demand drove H1 sales up 20.4% and operating profit up 41.0% YoY
  - [japan] Tokyo Tatemono: Investor property sales lifted 9M profit, putting FY2026 targets ahead of schedule
  - [korea] How bad is the memory crunch? New phones now use secondhand chips
  - [japan] Nikkei leads Asian sell-off after reports of Nvidia shake-up weigh on U.S. futures; Japan PPI beats forecasts
  - [taiwan] Foxconn: Expect 2027 AI Rack Shipment to Post High Double-Digit Growth >2317.TW
  - [taiwan] Foxconn: Expect 4Q AI Server Rack Shipments to Post High Double-Digit Growth on Quarter >2317.TW
  - [japan] BOJ's Asada says role of reflationist policies may be over
  - [china] China chip stocks rally as U.S. weighs curbs on remote AI access
  - [japan] BOJ Board Member Asada Could Dissent Again in December — Market Talk
  - [china] China’s central bank vows ample liquidity and yuan stability in Q3 monetary policy report
  - [japan] Beer sales increase by 20% in October thanks to tax cut
  - [japan] Japan's producer inflation accelerates to 7.1% in October; BoJ urges caution on rate hikes
  - [japan] Crude Oil Could Keep Pressure on Japan Import Costs — Market Talk
  - [korea] The Korea Land and Housing Corporation (LH) has decided to invest a total of 2 trillion won this yea..
  - [japan] Tsurumi Manufacturing Co Ltd - To Buy Back Up To 2.51% Of Own Shares Worth 2.6 Billion Yen
  - [taiwan] Ministry of Economic Affairs assists industrial upgrading, AI demand drives exports | Financial Management
  - [japan] Macroscope: Corporate prices accelerate in October, Bank of Japan assesses future direction of AI investment, 
  - [japan] Consumption tax reduction bill Prime Minister Takaichi to attend House of Councilors special committee meeting
  - [china] Hartalega: Higher U.S. Tariffs on China-Origin Gloves Improve Price Competitiveness of Malaysia Producers
  - [china] Semiconductors lift China stocks; Hong Kong falls as Alibaba weighs
  - [china] China's Central Bank Signals Easing Restraint as Growth Holds Up
  - [japan] ``We need to pay close attention to the pace'' of future interest rate hikes, says Bank of Japan Councilor Asa
  - [korea] South Korea’s HBM demand drives 54% surge in Taiwan glass fiber exports
  - [japan] Nissan Motor Co., Ltd. Stock 12‑Month Price Target Cut to JPY 372.31, Implies 34% Upside
  - [japan] JGB Yields Fall as Hopes for Accelerated BOJ Tightening Eases — Market Talk
  - [japan] Asia FX holds losses as dollar hits 19-mth high; yen nears 160
  - [china] China’s Loan Interest Rates Are Already Low, Central Bank Says
  - [china] U.S. finalizing rule to block China’s remote AI chip access- The Information
  - [china] China's yuan inches higher as PBOC sets firmer guidance
  - [china] Senior US Democratic senators urge administration to preserve Nvidia export records amid China security concer
  - [taiwan] AUO and Innolux target 2028 commercial breakthrough in semiconductor packaging
  - [japan] Bank of Japan member Asada talks with the business community in Nagasaki to pay attention to the impact of int
  - [japan] Corporate prices rose 7.1% in October; growth accelerated due to high crude oil prices and AI demand; Bank of 
  - [china] The central bank launched a 384 billion yuan overnight reverse repurchase operation on November 12, with a net
  - [japan] Stock prices fall Sell orders for AI/semiconductor related stocks

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
      "published_utc": "2026-11-12T07:22:43+00:00",
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

