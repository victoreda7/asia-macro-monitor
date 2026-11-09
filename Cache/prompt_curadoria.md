atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-09T22:22:42.616832+00:00
Total: 3000 manchetes

  🇯🇵 Japão          926
  🇨🇳 China          875
  🇹🇼 Taiwan         332
  🇰🇷 Coreia do Sul  867

## O que já está no feed (não repita)

  - [korea] SK hynix Inc. Stock 12‑Month Price Target Cut to KRW 3161025.43, Implies 179% Upside
  - [japan] Threat of trade curbs pushes Japan steel exports to three-decade low
  - [japan] Worst ranking of credit unions and credit unions for "deposit outflow"... 1st place decreased by 30%, more tha
  - [china] House Democratic leader says lawmakers need answers about Nvidia and wants restrictions on chip sales to China
  - [china] House Democratic leader says lawmakers needs answers on Nvidia, wants China chip restrictions
  - [china] Taiyuan Investigates Deadly Fire at Mixed-Use High-Rise
  - [japan] Japan's Mitsui Chemicals to buy chip materials maker JSR for $11.6bn
  - [japan] Dollar weakens against euro, yen as Iran talks lift risk appetite
  - [japan] Toyota Set To Bring Camry Back To Japan With Reverse Imports From US, Nikkei Says
  - [japan] Toyota set to bring Camry back to Japan with reverse imports from US
  - [korea] NAVER D2SF-backed MOVIN Raises KRW 10 Bln Series A Led By IMM Investment
  - [china] MP Stock Rises as China Extends Rare-Earth Reprieve Ahead of Trump-Xi Meeting — Barrons.com
  - [korea] NAVER D2SF-backed MOVIN Raises KRW 10 Billion Series A to Expand from Motion Capture to Motion Data Infrastruc
  - [china] U.S. Extends Tariff Exclusions for 178 Chinese Product Categories
  - [china] China Longyuan Power Posts October 2026 Power Generation Up 22.64% To 6.9 Million Mwh
  - [korea] On the 26th, the Monetary Policy Committee raised the base interest rate by 0.25%… ‘3.25% expected’
  - [japan] IBM Announces Offering Of Multiple Series Of Yen-Denominated Notes - SEC Filing
  - [japan] Japan-Vietnam summit meeting agrees on promoting security, collaboration on important minerals and nuclear pow
  - [japan] Japanese Yen Likely to Gain on BOJ Rate-Rise Prospects — Market Talk
  - [china] Beijing Orient EcoEnergy's LP Vehicle Signs 912.5 Million Yuan GPU Card Purchase Contract
  - [japan] Government/Bank of Japan foreign exchange intervention of 7.9 trillion yen, record high on July 30th, structur
  - [china] China's export controls to the United States and unreliable entity list will continue to be suspended for 2 mo
  - [japan] J-Star to host Japan manufacturer for Texas facility review By Investing.com
  - [japan] Berkshire Hathaway To Offer Three Series Of Yen-Denominated Senior Notes
  - [taiwan] Taiwan's October exports hit high, jump nearly 60% on AI demand
  - [japan] Six opposition parties in the House of Councilors urge the prime minister to attend consumption tax reduction 
  - [japan] The Liberal Democratic Party and the Meiji Restoration work closely together in the House of Councilors delibe
  - [china] China plans to boost yuan use in shipping risk-pricing, reduce reliance on West
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
      "published_utc": "2026-11-09T22:22:42+00:00",
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

