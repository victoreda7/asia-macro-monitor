atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-07T08:22:46.462576+00:00
Total: 2999 manchetes

  🇯🇵 Japão          1279
  🇨🇳 China          772
  🇹🇼 Taiwan         263
  🇰🇷 Coreia do Sul  685

## O que já está no feed (não repita)

  - [taiwan] Taiwan's Inflation Hits Over Two-Year High
  - [japan] Sumitomo Mitsui Trust Group Plans Approximately 350 Billion Yen Japan Infrastructure Fund As Early As In 2028,
  - [korea] Itcenentec Acquiring Real Estate Worth 74 Billion Won
  - [japan] Okura Industrial Co Ltd - Determined Selling Price For Secondary Share Offering At 5,315 Yen
  - [korea] Monetary Policy Committee member Jang Yong-seong "It is difficult to predict the future of the semiconductor i
  - [taiwan] Micron union in Taoyuan, Taiwan gets authorization to go on strike
  - [taiwan] Micron's Taoyuan union in Taiwan secures authorisation to strike
  - [china] Guangxi Wuzhou's Key Shareholder Plans To Buy Shares For Up To 178.09 Mln Yuan
  - [korea] AMD CEO says she continues to explore foundry partnership with Samsung Electronics
  - [korea] AMD CEO says continues to explore foundry partnership with Samsung Electronics
  - [taiwan] INTC Stock Jumps Overnight: CEO Says Intel Will Keep Working With Musk's Terafab Amid TSMC Partnership Buzz
  - [korea] Monetary Policy Committee member Jang Yong-seong “Employment must increase to improve domestic demand… Semicon
  - [taiwan] Musk says TSMC will not manage Terafab AI chip complex
  - [taiwan] Musk says TSMC won't run Terafab AI chip complex
  - [japan] August economic trend index decreased by 1.9 points from the previous month, the first decrease in 6 months
  - [korea] Samsung Electronics semiconductor manager to receive 750 million won in performance bonuses next year
  - [korea] What if you put 5 million won into a product with a deposit interest rate of 4%?
  - [taiwan] Musk Says Maybe TSMC Subleases Part Of The Terafab If They Want, But Nothing More Than That
  - [japan] Japan futures rise as weather disruptions, port delays tighten supply
  - [japan] BOJ Has Favorable Window to Hike Rates Through Next Spring — Market Talk
  - [japan] Ckd Corp - To Buy Back Up To 1.94% Of Own Shares Worth 5 Billion Yen
  - [japan] Komei's new representative Okamoto has dismissed the consumption tax cut as "inefficient," but rumors of a "re
  - [china] Table: King Yuan Electronics Sep Rev NT$4.07B Vs NT$3.27B
  - [korea] Samsung’s Q3 profit seen hitting 105T won on AI-driven chip demand - report
  - [japan] Asia stocks slip as rising oil, yields weigh; RBI hikes rates as expected
  - [japan] Japan’s Rapidus faces uphill battle to fill its $15B chip factory
  - [taiwan] Micron Union in Taoyuan, Taiwan Gets Strike Clearance
  - [japan] Analysis-Japan’s $15 billion Rapidus chip bet hinges on winning customers
  - [japan] BREAKING NEWS: Japan gov't mulling FY 2026 extra budget for disaster reconstruction
  - [korea] Samsung’s HBM prices tipped to more than double in 2027
  - [korea] Lotte Biologics expands US manufacturing partnership with Alvotech
  - [korea] AMD's Lisa Su courts Korean AI chipmakers as it takes on Nvidia
  - [china] Asia markets slip amid softening Chinese reserves and persistent energy cost pressures
  - [taiwan] Intel to continue working on Musk’s Terafab despite TSMC talks - Bloomberg
  - [korea] Global banks lift Korea growth outlook to 3.5% on chip boom
  - [japan] Consumption Activity Index
  - [japan] Australian Dollar-Yen May Have Reached Long-Term Ceiling — Market Talk
  - [korea] South Korean Won Tests 2024 High
  - [china] India's central bank's reverse repurchase rate is 3.35% as of October 7, compared with the previous value of 3
  - [china] As of October 7, the central bank's deposit reserve ratio is 3%, expected to be 3%, and the previous value was

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
      "published_utc": "2026-10-07T08:22:46+00:00",
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

