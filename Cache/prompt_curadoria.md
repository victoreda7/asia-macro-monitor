atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-14T05:42:44.034531+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1134
  🇨🇳 China          845
  🇹🇼 Taiwan         296
  🇰🇷 Coreia do Sul  725

## O que já está no feed (não repita)

  - [japan] BOJ May Need to Accelerate Hikes to Reach Neutral Rate — Market Talk
  - [china] Asian equities stabilize following Wall Street tech selloff; oil nears $95, China trade data beats
  - [japan] Japan Bank Lending Remains Robust Despite BOJ Rate Hikes — Market Talk
  - [china] China’s Factory-Gate Inflation Hits Four-Year High as Consumer Prices Lag
  - [korea] SK hynix looks beyond HBM to tackle AI memory bottlenecks
  - [china] China's crude stocks slump despite slight rise in September import rate
  - [japan] How far will the Bank of Japan's interest rate hike be likely to exceed 2%? #Expert Topi (Koichi Fujishiro) - 
  - [korea] South Korean Won Rises Near 2-Year High
  - [china] China's September CPI rises 0.9% Y/Y, PPI accelerates to 5.0% above expectations
  - [japan] Five-Year JGB Yield Pares Gains After Five-Year Auction Draws Solid Demand — Market Talk
  - [china] China's September trade surplus widens to $133.53B; exports up 36.3%, imports up 31.0%
  - [china] Chinese Exports Accelerated in September — Update
  - [china] Imported Inflation to Continue Shaping China's Headline Inflation — Market Talk
  - [china] China Inflation At 0.9%; PPI Inflation Highest Since 2022
  - [china] China's consumer prices rose 0.9% in September, a slight increase from the previous month, affected by persist
  - [china] Asia FX subdued ahead of U.S. CPI; China data, Singapore GDP in focus
  - [china] China Consumer Price Index rose 0.9% in September, positive for 12 consecutive months; transportation fuel and
  - [china] Yuan gains as markets weigh China inflation, await US CPI
  - [korea] Bank of Korea Likely to Hold Rates Steady This Month — Market Talk
  - [taiwan] TSMC and MediaTek alumni lead Taiwan's new wave of deep tech startups
  - [china] China September iron ore imports rise on pre-holiday restocking
  - [korea] Shin Hyun-song's first National Assembly inspection, "Monetary policy unwavering"... Base interest rate 3.0%, 
  - [japan] Japan 10Y Yield Steadies on Cautious BOJ Outlook
  - [china] China's soybean imports fall 7.7% in September from a year earlier
  - [china] China's September exports blow past forecasts, imports accelerate
  - [china] Offshore Yuan Trades Near Multi-Year High
  - [taiwan] ASML, TSMC Report This Week: What Traders Are Watching After A 6-Day Chip Stock Slide
  - [china] China's export engine hits fastest pace since February with 36% growth
  - [china] China's September coal imports fall 6%
  - [china] The central bank launched a 56 billion yuan 7-day reverse repurchase on October 14
  - [china] China's export engine steams ahead with September shipments up 36%
  - [korea] Gold prices hold firm ahead of US inflation data
  - [china] China September rare earth exports rise 6.7% from a year earlier
  - [china] China hold 2027 fertiliser import tariff quota unchanged at 13.65 million tons
  - [china] China's wholesale prices rise 5%, the highest level in 4 years and 3 months due to high crude oil prices, Sept
  - [china] China factory-gate inflation heats up as commodity costs rise, CPI lags forecasts
  - [china] China Imports Hit Record High
  - [china] Chinese Exports Accelerate in September
  - [china] China’s exports surge 36.3% y/y in September, imports up 31%
  - [china] China’s Trade Surplus Nears $940 Billion as Export Growth Surges

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
      "published_utc": "2026-10-14T05:42:44+00:00",
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

