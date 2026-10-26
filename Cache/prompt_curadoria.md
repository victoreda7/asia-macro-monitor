atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-26T06:42:45.563390+00:00
Total: 3000 manchetes

  🇯🇵 Japão          981
  🇨🇳 China          855
  🇹🇼 Taiwan         372
  🇰🇷 Coreia do Sul  792

## O que já está no feed (não repita)

  - [japan] Shin-Etsu Polymer Co Ltd - To Buy Back Up To 0.56% Of Own Shares Worth 1.25 Billion Yen
  - [korea] Inside Henkel's Korean factory making adhesives for AI chips
  - [korea] Samsung may have overtaken SK hynix in HBM revenue, analysis suggests
  - [china] Beyond exports: China's automakers dig deeper into Europe
  - [korea] South Korea's Lee says unlikely to join Pacific trade pact within his term
  - [korea] Hyundai Glovis partners with Shopee to boost K-beauty exports
  - [korea] Korea Investment Management enters Hong Kong ETF market with chip fund
  - [japan] Prime Minister Takaichi seeks cooperation from ruling party for early passage of consumption tax reduction bil
  - [japan] BOJ, Fed expected to leave rates unchanged this week
  - [japan] Why is Japan tightening its immigration rules?
  - [korea] SK Hynix tests Bear Flag resistance near KRW 1,320,000: Live
  - [korea] South Korean Won Hits 24-month High
  - [china] Asia FX muted, yuan at 4-yr high; dollar drifts lower ahead of c.bank-packed week
  - [china] The central bank launched a 700 billion yuan MLF operation on October 26 with a term of one year
  - [korea] SK Hynix Plans $12 Billion Dividend From Kioxia Gains: Report
  - [china] China stocks slip as tech shares lead declines, before key central bank meetings
  - [japan] Future “Regulatory reform for AI utilization and countermeasures against “AI unemployment”” Recommendations to
  - [china] China's Humanoid Shipment Volumes Likely to Remain Modest — Market Talk
  - [china] China National Team ETFs Draw Most Inflows Since Trade War Rout
  - [japan] Bank of Japan’s hawkish pause to leave scope for December hike
  - [china] China’s yuan climbs to fresh 4-year high ahead of key policy meetings
  - [japan] Stock prices fall Sell orders centered on semiconductor-related stocks
  - [taiwan] New Taiwan Dollar Likely to Rebound After Recent Slump — Market Talk
  - [korea] South Korea 3Q GDP Growth Likely Accelerated Sequentially, Poll Shows — Market Talk
  - [japan] Yen Holds Steady Ahead of BOJ Policy Meeting
  - [korea] Banks expected to maintain tight lending standards in Q4: BOK survey
  - [china] The central bank launched a 56 billion yuan 7-day reverse repurchase operation, with a net investment of 116 b
  - [taiwan] Taiwan wafer-testing supplier Hermes Testing Solutions commits more than US$215 million to advanced chip testi
  - [taiwan] Podcast highlights: TSMC's 3nm demand story, Samsung HBM shift, and A14 ramp
  - [china] This week, the central bank's open market reverse repurchase expires with 338 billion yuan. On Tuesday, 900 bi
  - [korea] SK Hynix Stock Rises: Korean Memory Giant Reportedly Weighs $12B Special Dividend From Kioxia Gains
  - [korea] A SK Hynix anunciará, nesta quarta-feira, medidas para aumentar o retorno aos acionistas
  - [korea] SK Hynix to announce steps to boost shareholder returns on Wednesday
  - [japan] Amazing Venture [39] Patentix/Next Generation Power Semiconductor with Energy Saving | Business | Toyo Keizai 
  - [korea] The U.S. Dairy Export Council (USDEC) participated in the session under the theme of "The Future of
  - [china] The central bank launched a 700 billion yuan medium-term lending facility operation today
  - [korea] Noeul, a manufacturer of artificial intelligence (AI)-based blood and cell analysis diagnostic equip..
  - [korea] Major banks have increased their information protection budgets for next year significantly since th..
  - [china] The central bank launched a 56 billion yuan 7-day reverse repurchase operation today
  - [japan] Currency markets subdued ahead of pivotal central bank week

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
      "published_utc": "2026-10-26T06:42:45+00:00",
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

