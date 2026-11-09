atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-09T14:42:45.104099+00:00
Total: 3000 manchetes

  🇯🇵 Japão          927
  🇨🇳 China          874
  🇹🇼 Taiwan         333
  🇰🇷 Coreia do Sul  866

## O que já está no feed (não repita)

  - [japan] IBM Announces Offering Of Multiple Series Of Yen-Denominated Notes - SEC Filing
  - [japan] Japan-Vietnam summit meeting agrees on promoting security, collaboration on important minerals and nuclear pow
  - [japan] Japanese Yen Likely to Gain on BOJ Rate-Rise Prospects — Market Talk
  - [china] Beijing Orient EcoEnergy's LP Vehicle Signs 912.5 Million Yuan GPU Card Purchase Contract
  - [japan] Government/Bank of Japan foreign exchange intervention of 7.9 trillion yen, record high on July 30th, structur
  - [china] China extends US trade truce by two months
  - [china] China's export controls to the United States and unreliable entity list will continue to be suspended for 2 mo
  - [japan] J-Star to host Japan manufacturer for Texas facility review By Investing.com
  - [japan] Berkshire Hathaway To Offer Three Series Of Yen-Denominated Senior Notes
  - [taiwan] Taiwan's October exports hit high, jump nearly 60% on AI demand
  - [japan] Six opposition parties in the House of Councilors urge the prime minister to attend consumption tax reduction 
  - [japan] The Liberal Democratic Party and the Meiji Restoration work closely together in the House of Councilors delibe
  - [taiwan] Ministry of Finance: Taiwan’s export scale will surpass Japan’s this year, ranking “8th and 7th” in the world
  - [china] China producer inflation hits four-year high as energy costs surge
  - [japan] Support rate for each party: “Liberal Democratic Party” 35.9% “No support” 37.1% NHK public opinion poll
  - [japan] The approval rate for the high city cabinet is 53%, while 32% do not support it
  - [taiwan] Ministry of Finance: Exports to the United States accounted for 31.7% in the first 10 months, setting a new hi
  - [taiwan] October's export record hit 5 major highlights, with 36 hits in a row, the longest growth cycle in history | S
  - [korea] The Trade Remedy Review Committee of the Ministry of Economic Affairs made a positive determination of industr
  - [taiwan] Taiwan President taps chip strengths for self-reliant space push
  - [china] Table: King Yuan Electronics 3Q Net Profit NT$2.64B Vs NT$2.30B
  - [china] China Will Extend U.S. Tariff Suspensions for Two Months as Trump Visit Looms — Update
  - [china] China extends suspensions of 24% tariff on US goods, port fees on US ships for two months
  - [china] Shenzhen Qingyi Photomask's Unit To Invest In Semiconductor Photomask Production Base Project
  - [china] Chinese Producer Inflation Hits 5.7% for Post-Covid Era High
  - [taiwan] KYEC warns AI demand is amplifying semiconductor supply-chain risks
  - [japan] ``Party support rate'' for about 30 years The key to elections revealed by NHK opinion poll
  - [korea] Lam Research, Comet bid for S.Korean chip equipment maker Dawon Powertron
  - [taiwan] Taiex posts 2nd-largest daily point gain on intervention pledge
  - [china] China Extends Pause on US Tariffs and Trade Curbs for Two Months
  - [china] China's consumer price index rose 0.7% in October, positive for 13 consecutive months, affected by rising fuel
  - [china] China Consumer Price Index rose 0.7% in October, positive for 13 consecutive months, affected by rising fuel p
  - [korea] Foreign currency raised by the Export-Import Bank of Korea is expected to exceed $17 billion (about
  - [taiwan] Taiwan's October exports surge again on strong AI demand
  - [korea] As international energy prices soar, concerns are growing over the financial deterioration of state
  - [korea] As financial authorities regulate Samsung Electronics and SK Hynix's single-stock leveraged exchange..
  - [korea] Woori Financial Group: “The Bank of Korea is expected to raise the base interest rate to 3.25% at the November
  - [china] China Will Extend U.S. Tariff Suspensions for Two Months as Trump Visit Looms
  - [china] China Car Exports Forecast to Slow From ‘Supercharged’ Pace
  - [china] CNH/USD: Cross-Border Yuan Flows on China’s Network Head for Record Year

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
      "published_utc": "2026-11-09T14:42:45+00:00",
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

