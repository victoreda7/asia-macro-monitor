atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-24T05:42:51.662046+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1022
  🇨🇳 China          956
  🇹🇼 Taiwan         336
  🇰🇷 Coreia do Sul  686

## O que já está no feed (não repita)

  - [japan] Concerning the consumption tax reduction bill, citizens submit a counterproposal to the Diet, including a maxi
  - [korea] 54% of bond market workers say, “The Bank of Korea Monetary Policy Committee will raise the base interest rate
  - [korea] Why are Samsung and SK Hynix shares soaring after Nvidia's turnaround?
  - [china] Chinese Automakers Book Strong European Growth Ahead of Import Cap
  - [korea] KB, Hana and Woori banks step up for smaller defense suppliers as exports rise
  - [china] China's yuan hits three-week high as firm fixing offsets dollar strength
  - [korea] [Issue] The four major banks ‘take a step back’ in NIM even if the base interest rate rises… All decline in th
  - [korea] Will Korea tighten its belt again? 54% of bond market experts say “base rate hike in November” By EBN
  - [taiwan] Micron steps up HBM investment in Taiwan, Singapore
  - [taiwan] TSMC, SK Hynix, and Asian tech surge after Jensen Huang's return as Nvidia CEO
  - [korea] Índice Kospi: Por que Samsung, SK Hynix e SK Square lideram as altas hoje
  - [japan] Dependency deduction for relatives living overseas: Requirements to be tightened in next year's tax reform
  - [china] China cobalt prices surge to three-month high as Congo bans exports
  - [taiwan] Why is TSMC stock surging today?
  - [china] US chip curbs won’t impact Malaysia’s China ties, PM says
  - [japan] Bank of Japan Kagoshima Branch holds press conference that the prefecture's economy is "moderately recovering"
  - [korea] 54 pct of bond experts eye rate hike this week: poll
  - [korea] 54% of bond market participants “expect an interest rate hike at the Monetary Policy Committee in November”
  - [korea] 54% of bond market experts say, “The Bank of Korea will raise the base interest rate”… Investor sentiment cool
  - [korea] Economists agree on Bank of Korea interest rate hike in November, Reuters: “One hike next year is likely”
  - [korea] 54% of bond market experts say, “The Bank of Korea will raise the base interest rate”… Investor sentiment cool
  - [japan] Japanese bond yields fall as lower oil prices ease inflation concerns
  - [japan] Nikkei Asia Forum 'The Global Chip Game: Our predictions for 2027'
  - [taiwan] Analysis: Taiwan's automakers break into overseas markets, but can exports sustain their momentum?
  - [china] The central bank launched a 516 billion yuan overnight reverse repurchase operation today
  - [china] On November 24, the central bank launched a 516 billion yuan overnight reverse repurchase operation.
  - [china] CHINA PBOC CONDUCTS CNY516 BLN VIA O/N REVERSE REPO TUES
  - [china] The central bank launched a 516 billion yuan overnight reverse repurchase operation with an interest rate of 1
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7111 TUES VS 6.7120
  - [korea] [Economy Focus] Will the Bank of Korea Monetary Policy Committee raise the base interest rate on the 26th?
  - [taiwan] TSMC Rises 9.85%; Foxconn Technology Gains 9.95%
  - [korea] Will the base interest rate rise? Interested in whether bank term deposits will be available at 4% per annum
  - [japan] Number of people in Japan making 100 mil. yen or more doubles over decade
  - [korea] SK hynix's US-traded shares surge 20% after Huang's reinstatement as Nvidia CEO
  - [korea] South Korea’s central bank seen raising rates on Thursday, once more next quarter - Reuters poll
  - [korea] Bank of Korea Set to Raise Rate This Week, Poll Says — Market Talk
  - [japan] Japan's factory activity expands in November, PMI shows
  - [japan] Interest Rate (November 20 2026)
  - [japan] JGB Futures Rise, Buoyed by Decline in Crude Oil Prices — Market Talk
  - [japan] Nikkei Asia webinar 'The Global Chip Game: Our predictions for 2027'

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
      "published_utc": "2026-11-24T05:42:51+00:00",
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

