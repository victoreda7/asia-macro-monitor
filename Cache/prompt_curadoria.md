atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-26T06:32:43.951914+00:00
Total: 3000 manchetes

  🇯🇵 Japão          912
  🇨🇳 China          981
  🇹🇼 Taiwan         335
  🇰🇷 Coreia do Sul  772

## O que já está no feed (não repita)

  - [japan] Short-dated JGB yields rise as equity rebound revives BOJ hike bets
  - [korea] The Bank of Korea raised interest rates by 1 percentage point to 3.25%, a two-year high, and raised its GDP fo
  - [korea] BOK raises rate to 3.25% as chip boom fuels inflation concerns
  - [taiwan] Taiwan confident of keeping 15% tariffs under Trump's new proposal
  - [korea] Bank of Korea lifts base rate by 25 bps to 3.25% and upgrades GDP outlook
  - [korea] Bank of Korea Resumes Rate Hikes as AI Boom Fuels Growth — Update
  - [japan] The ASEAN+3 Finance and Central Bank Deputies’ Meeting, November 25–26, 2026
  - [japan] Bank of Japan's Tamura, a member of the Bank of Japan's Council, wants to raise interest rates further towards
  - [korea] Xiaomi shipments plunge 29% as Samsung holds lead amid memory crunch
  - [japan] In the US, there are ``three signs'' of monetary tightening due to rising prices, steady growth and employment
  - [china] China Braces for Tariff Hike After US Announcement
  - [china] Yuan holds steady near three-week high despite tariff risk
  - [china] China shares flat as markets struggle to shake off tariff risks
  - [korea] The Bank of Korea raises the base interest rate by 0.25%p... 3.25% per annum in 2 years
  - [korea] Asia FX: won muted after BOK hikes rates, dollar steady
  - [korea] South Korea's central bank raises interest rates for the third time this year, aiming to curb price rises
  - [korea] Bank of Korea Hikes Rate as AI Boom Powers Growth, Inflation
  - [korea] Bank of Korea raises interest rates to 2-year high, AI exports drive upward revision of economic forecasts | I
  - [korea] [Video] Gangwon Boosts Agri-Food Export Cooperation
  - [japan] Honda re-imported Acura to be released next month
  - [japan] Japan Protests New US Tariff Rate, Allegation of Excess Capacity
  - [korea] South Korea’s central bank raises rates, upgrades 2027 growth outlook
  - [korea] (3rd LD) BOK raises key rate to 3.25 pct amid strong growth, inflation, revises up 2027 forecast to 4.1 pct
  - [japan] BOJ’s Tamura flags faster pace of rate hikes amid inflation risk
  - [china] China Vanke Is Seeking Another Extension On A Yuan Bond Due Next Month - Bloomberg News
  - [china] Trump Aims to Keep Leverage Over Xi With 40% China Tariff Threat
  - [china] Trump’s China Tariffs Raise Threat of New Test for Trade Truce
  - [korea] Some said that the nominal GDP, which was around 2,600 trillion won last year, will far exceed 3,000..
  - [korea] The Bank of Korea raises the base interest rate to 3.25%... Leave open the possibility of 3.75% next year
  - [korea] [Photo] Bank of Korea monetary policy direction press conference
  - [korea] The Bank of Korea raised its base interest rate to 3.25%. Why did it choose to raise it this time?
  - [korea] BOK Gov: Chip Companies' Operating Profits Estimated at KRW700T This Year
  - [china] Nissan Motor Planning To Import And Sell Plug-In Hybrid Vehicles Produced By China JV In Japan Market, Nikkei 
  - [korea] The Bank of Korea raises the base interest rate to 3.25% per annum... Growth rate expected to be 4.1% next yea
  - [korea] BOK Gov: See Private Consumption Growing 2.4% in 2027, Faster Than in 2026
  - [korea] BOK Gov: IT Boom May Take Time to Translate Into Private Consumption
  - [korea] The Bank of Korea raises the base interest rate to 3.25%… “Next year’s growth rate will be 4.1%”
  - [korea] (URGENT) BOK chief sees improvement in S. Korea's potential growth rate
  - [japan] BOJ policymaker signals chance of faster-pace interest rate hikes
  - [japan] Japanese yield curve steepens as markets reprice BOJ rate outlook

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
      "published_utc": "2026-11-26T06:32:44+00:00",
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

