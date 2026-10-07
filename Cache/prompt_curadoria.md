atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-07T05:52:44.417664+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1289
  🇨🇳 China          776
  🇹🇼 Taiwan         257
  🇰🇷 Coreia do Sul  678

## O que já está no feed (não repita)

  - [korea] Global banks lift Korea growth outlook to 3.5% on chip boom
  - [japan] Consumption Activity Index
  - [japan] Australian Dollar-Yen May Have Reached Long-Term Ceiling — Market Talk
  - [korea] South Korean Won Tests 2024 High
  - [china] India's central bank's reverse repurchase rate is 3.35% as of October 7, compared with the previous value of 3
  - [china] As of October 7, the central bank's deposit reserve ratio is 3%, expected to be 3%, and the previous value was
  - [japan] Japan 10Y Yield Eases as BOJ Rate Outlook in Focus
  - [japan] Asian currencies mixed as dollar holds gains, yen weakens near 158
  - [china] Chinese Yuan May Be Undervalued — Market Talk
  - [korea] AMD's Su to Meet with Samsung's Chip Division Chief as Memory Shortage Persists — Bloomberg News
  - [korea] AMD’s Su to meet Samsung’s chip head as memory crunch persists- Bloomberg News
  - [korea] Korean Retail Investors Lose $1.7 Billion on Leveraged Chip ETFs
  - [china] Chinese EV Market Is Shifting to Serve Primarily as Hub for EV Exports — Market Talk
  - [korea] Samsung Electronics Set to Post Record Third-Quarter Operating Profit — Earnings Preview
  - [taiwan] Hwacom shifts semiconductor business to SureWin, targets post-quantum security
  - [korea] Samsung Electronics, SK hynix rebound from early losses
  - [japan] Yen Weakens on Yield Differential
  - [korea] Samsung's Q3 profit seen jumping nine-fold, but chip margins may be flat
  - [japan] Yomiuri: Mizuho Bank to Offer 2 Trillion Yen in Startup Support
  - [china] China's forex reserves fall more than expected in September
  - [korea] Korea to strengthen food safety ties, support exports to Latin America
  - [japan] Japan futures rise as weather disruptions, port delays tighten supply
  - [korea] Finance minister pledges to create favorable biz environment amid challenges
  - [japan] Will the Bank of Japan's decision to reach 2% assist the Takaichi administration's move away from its reflatio
  - [japan] JGB yields track global bond rally; dovish BOJ member signals support for hikes
  - [taiwan] AI supercycle, pricing, and Terafab top the agenda ahead of TSMC's earnings call
  - [china] China Golden Week Offers Limited Boost to Consumption — Market Talk
  - [korea] South Korean Shares Extend Decline on Chip Outlook
  - [korea] Samsung takes Vietnam up semiconductor value chain with $5bn expansion
  - [japan] Japan MOF To Auction Y2.5T Of 5-Year Govt Bonds Oct 14
  - [japan] Towa Plans Chipmaking Tool Plant For Japanese Supply Chain: CEO, Nikkei Says
  - [korea] SK Hynix bounces at Fibonacci support, cloud traps price: Live
  - [japan] Bank of Japan Accounts (September 30)
  - [taiwan] Rapidus adds Malaysian chip designers to its semiconductor network
  - [taiwan] Nan Pao pitches water-based resins as Taiwan textile shipments surge
  - [japan] JGB Futures Edge Higher, Tracking Gains in U.S. Treasury Market — Market Talk
  - [japan] Analysis-Japan’s $15 billion Rapidus chip bet hinges on winning customers
  - [japan] Analysis-Japan’s $15 billion Rapidus chip bet hinges on winning customers By Reuters
  - [japan] Japan Forex Reserves Fall Further in September
  - [korea] Samsung Electronics poised to top $74bn in Q3 OP

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
      "published_utc": "2026-10-07T05:52:44+00:00",
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

