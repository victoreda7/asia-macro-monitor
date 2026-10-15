atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-15T00:52:44.736812+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1123
  🇨🇳 China          851
  🇹🇼 Taiwan         293
  🇰🇷 Coreia do Sul  733

## O que já está no feed (não repita)

  - [korea] Seoul stocks open sharply lower on lingering concerns over AI, US inflation
  - [korea] Kospi plunges nearly 6% as foreigners dump chip stocks
  - [japan] Japan's Nikkei tumbles as tech stocks hammered on US rate hike worries
  - [korea] (LEAD) Seoul stocks open sharply lower on lingering concerns over AI, U.S. inflation
  - [japan] How can eel pie companies eliminate departmental deficits?
  - [taiwan] Fujifilm to expand Arizona semiconductor materials output
  - [china] The central bank will launch a 700 billion yuan buyout reverse repurchase operation. In September, imports and
  - [korea] Samsung Semiconductor Highlights 400+ Layer Flash Powering Agentic AI
  - [china] The central bank will launch a 700 billion yuan buyout reverse repurchase operation
  - [taiwan] TSMC Set to Post Sixth Consecutive Quarter of Record Profit Thanks to AI Boom
  - [taiwan] TSMC expected to report sixth straight quarter of record profit thanks to AI boom
  - [china] The Times said the central bank will launch a 700 billion yuan buyout reverse repurchase operation
  - [japan] US-listed semiconductor stocks continue to fall
  - [japan] U.S. semiconductor company plans to build new factory for up to 3 trillion yen based on Japan-U.S. agreement
  - [japan] G20 Finance Ministers and Central Bank Governors Meeting to begin on the 15th
  - [japan] Fed economic report “Price growth pace is accelerating in some areas” Focus on timing for additional interest 
  - [japan] <Competitors are withdrawing or making losses> A new frontier for Uber Eats, which has been in the black for t
  - [japan] JR Hokkaido's "Yellow Line Area" fundamental improvement plan is in chaos, financial support of 380 billion ye
  - [japan] Japan to invest $21 billion in up to two GlobalFoundries chip factories in New York By Reuters
  - [japan] "Eel pie" is doing well, but the division is in the red for 400 million yen...The "amazing comeback" of Hamama
  - [taiwan] TSMC options chain shows big call wall at $500 strike ahead of earnings
  - [japan] Japan to invest $21 billion in up to two GlobalFoundries chip factories in New York
  - [china] Times data said | The central bank will launch a 700 billion yuan buyout reverse repurchase operation
  - [japan] GlobalFoundries options surge on $21B U.S.-Japan chip deal
  - [china] China’s Sept. Exports Surge 36.3% Amid AI Boom, Auto Export Rush
  - [china] China’s Sept. Exports Surge 36% Amid AI Boom, Auto Export Rush
  - [korea] South Korean minister rejects claim of W80b wasted on Brazilian egg imports
  - [japan] PRES TRUMP POSTS: 'MASSIVE; $21 BLN INVESTMENT FINANCED BY JAPAN, SKOREA, TAIWAN TO BUILD TWO SEMICONDUCTOR FA
  - [taiwan] TSMC Earnings Will Surge but Terafab and Texas Talks Are in Focus — Barrons.com
  - [taiwan] Thursday preview: TSMC results, UK GDP in focus
  - [china] Micron Takes Another Hit as China Chip Fears Flare
  - [korea] ASML's Next Big Chipmaking Cycle Has a Timeline—Intel, Samsung and TSMC Set It
  - [korea] Seoul shares fall for 6th day on renewed AI concerns ahead of US inflation data
  - [japan] Japan to invest up to $21 billion in two US chip factories to be run by GlobalFoundries By Reuters
  - [china] Commentary: Why Gradual Yuan Appreciation Remains the Baseline
  - [japan] US consumer prices rise 3.7% in September; expectations for early interest rate hike rise somewhat
  - [japan] US Consumer Price Index rises 3.7%; growth rate expands for the first time in 4 months; yen weakens due to exp
  - [taiwan] US cuts Obamacare subsidies for 189,000 with duplicate coverage
  - [korea] Korea's GDP per capita to top $40,000 this year, IMF says
  - [china] IMF calls for US to cut deficits amid bond woes, urges China to shift away from exports

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
      "published_utc": "2026-10-15T00:52:44+00:00",
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

