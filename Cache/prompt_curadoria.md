atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-24T10:32:45.399545+00:00
Total: 3000 manchetes

  🇯🇵 Japão          982
  🇨🇳 China          852
  🇹🇼 Taiwan         379
  🇰🇷 Coreia do Sul  787

## O que já está no feed (não repita)

  - [taiwan] Diplomatic discord over haze issue erupts, Indonesia cuts natural gas exports to Singapore | International
  - [japan] Liberal Democratic Party Policy Research Council Chairman Kobayashi on consumption tax reduction related bill 
  - [korea] Bubblemaps: BMT opens spot trading on Upbit's KRW market - 24 Oct 2026
  - [taiwan] Atypical employment ratio dips to 14-year low: DGBAS
  - [korea] Samsung Electronics and SK hynix bonuses: 700 million won vs. 150 million won at Micron in Taiwan—why the huge
  - [taiwan] Taiwan Semiconductor Manufacturing Company Ltd. Stock 12‑Month Price Target Cut to $553.18, Implies 32% Upside
  - [china] The central bank will carry out 700 billion yuan of MLF operations to reduce volume and continue operations
  - [japan] What's New October, 2026 : Ministry of Finance
  - [korea] Bank of Korea maintains base interest rate at 3%... Leave room for price increases due to price instability
  - [china] China Barely Eased Austerity Just Before Shift to Stimulus Mode
  - [taiwan] Key facts: TSMC (2330) Q3 net +69%; tests rare‑earth‑free motors
  - [japan] CFTC: Hedge Funds Cut Yen Shorts and Increase Australian Dollar Longs
  - [japan] Demonstrations in France reflect the "spark of Europe", which country will sell government bonds next, and the
  - [japan] Bank of Japan Monetary Policy Meeting from the 29th It is likely that the underlying inflation rate will reach
  - [china] The central bank will launch a 700 billion yuan MLF operation on October 26, with a reduction of 200 billion y
  - [korea] SK Hynix Stocks Gain 4.42% as Solidigm Ends IPO Review
  - [china] The central bank will carry out 700 billion yuan of MLF operations to maintain sufficient liquidity in the ban
  - [korea] Why did Micron, SK Hynix and SanDisk shares rise on Friday?
  - [japan] Japan banks prepared to weather AI crash, global rate spike: BOJ stress test
  - [japan] Consumption tax reduction bill enters substantive deliberation; debate continues over support payments, etc.
  - [china] China’s Fiscal Revenue Slips as Land-Sale Slump Deepens
  - [china] EU Looks Beyond Cars for Next Round of China Trade Talks
  - [korea] Micron, Sandisk gain as SK Hynix scraps Solidigm IPO, LYNX says
  - [japan] Japan weighs rebranding energy, AI as defense spending under Trump pressure
  - [korea] SK Hynix and Samsung likely to boost shareholder returns as demand stays strong: BofA
  - [china] China's MiniMax completes export registration for open-source, overseas AI model licensing
  - [korea] Woori Financial Group : Earnings topped KRW 1 trillion as stronger fees and lower credit costs supported retur
  - [china] China issues guidelines to promote employment amid AI advances
  - [china] The central bank launches 700 billion yuan 1-year MLF operation
  - [korea] Apro: AT begins KRW spot trading on Bithumb - 23 Oct 2026
  - [korea] SK Hynix Just Sent Another Warning Signal to the AI Trade — Barrons.com
  - [china] BGI Genomics Q3 Net Profit At 2.9 Million Yuan
  - [japan] German Chancellor Merz will visit Japan next week to hold a summit meeting with Prime Minister Takaichi
  - [china] Hang Zhou Iron & Steel Q3 Net Loss At 108.7 Million Yuan
  - [japan] Japan-Micronesia summit meeting confirms further strengthening of bilateral relations
  - [china] Chinese premier chairs State Council executive meeting
  - [china] The central bank launched a 700 billion yuan medium-term lending facility (MLF) operation on October 26
  - [china] The central bank launched a 700 billion yuan medium-term lending facility (MLF) operation on October 26_Compan
  - [korea] Micron pivots from 4F² to 3D DRAM, differing from rivals Samsung, SK Hynix: Wedbush
  - [korea] What's Going On With SK Hynix Stock Friday

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
      "published_utc": "2026-10-24T10:32:45+00:00",
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

