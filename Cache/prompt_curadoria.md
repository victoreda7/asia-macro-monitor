atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-07T09:32:45.202540+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1276
  🇨🇳 China          775
  🇹🇼 Taiwan         263
  🇰🇷 Coreia do Sul  686

## O que já está no feed (não repita)

  - [japan] Prime Minister Takaichi: “The best way to reduce consumption tax” “Thorough appropriate allocation of road bud
  - [korea] AMD CEO says he continues to explore foundry partnership with Samsung Electronics
  - [taiwan] Musk says TSMC won’t run Terafab AI chip complex
  - [korea] AMD’s Lisa Su calls chips ‘team sport’ as Samsung, SK hynix ties deepen
  - [china] Visionox Technology To Raise Up To 3 Bln Yuan In Private Share Placement
  - [japan] Ruling party approves consumption tax reduction bill; government to submit to parliament as early as this week
  - [japan] Japanese Yen Faces Hit From Potential Supplementary Budget — Market Talk
  - [korea] "Annual Export of $1 Trillion…" "You have to start preparing for 'Post Semiconductor'."
  - [taiwan] Musk says we will “build and run” Terafab, TSMC may sublease space
  - [korea] Operating profit of KRW 4 trillion by Q3… LG Electronics' All-Time Performance 'Preview' This Year
  - [korea] Samsung Electronics DS employee earning 80 million won a year to receive 750 million won in performance bonuse
  - [korea] Deputy Prime Minister and Minister of Finance and Economy Lee Hyung-il met with the head of six econ..
  - [taiwan] Taiwan Inflation Hits 31-Month High
  - [taiwan] Taiwan's Inflation Hits Over Two-Year High
  - [japan] Asian currencies mixed as dollar firms, yen weakens near 158
  - [japan] Bank of Japan Tankan Steel business confidence turns positive, reflecting sales price transfer (Nikkan Sangyo 
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
      "published_utc": "2026-10-07T09:32:45+00:00",
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

