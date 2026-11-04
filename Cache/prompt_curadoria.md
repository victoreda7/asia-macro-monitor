atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-04T04:52:44.625896+00:00
Total: 2884 manchetes

  🇯🇵 Japão          834
  🇨🇳 China          861
  🇹🇼 Taiwan         304
  🇰🇷 Coreia do Sul  885

## O que já está no feed (não repita)

  - [japan] Mitsui Chemicals to buy Japan chip material maker JSR for over $8.2bn
  - [japan] Chief Cabinet Secretary: Support for the International Criminal Court (ICC) Considering financial measures, et
  - [japan] Nikkei Drops 4.2% to Five-Month Low, Dragged by Chip Stocks — Market Talk
  - [china] China's yuan hits 2-week low as investors weigh PBOC foreign exchange reserve hike
  - [china] Asian FX gains as dollar falls on U.S. midterm results, yuan weakens on PBOC move
  - [japan] Consumption tax reduction bill Liberal Democratic Party: “Vote on the 6th” Democratic Party: “Decision after l
  - [japan] Consumption tax reduction bill House of Councilors establishes special committee, chaired by Liberal Democrati
  - [china] Nvidia China Clients Expected to Get 1% of $70 Billion in RTX Chip Orders
  - [china] Nvidia China clients to get 1% of $70 billion RTX chips ordered- Bloomberg News
  - [china] China Steps in to Boost Stocks, Cool Off Yuan
  - [japan] Swiss Franc, Yen Jump as US Midterms Push Dollar to Worst Day in a Month
  - [korea] Kospi Slumps as Democrats’ US Election Lead Spurs Chip Selloff
  - [japan] House of Representatives Finance and Financial Affairs Committee Consumption tax reduction bill Ruling parties
  - [china] Nvidia China Clients to Get 1% of $70 Billion RTX Chips Ordered
  - [japan] Yen Strengthens as US Dollar Weakens
  - [china] The central bank launched a 257.5 billion yuan overnight reverse repurchase operation on November 4, with a ne
  - [korea] BOK Financial raises quarterly dividend by 23.8% to $0.78/share
  - [china] China's PMI Data Show Economic Activity Lost Momentum in Oct — Market Talk
  - [taiwan] TSMC's acquisition of AUO plant reshapes panel supply chain
  - [korea] Growth and prices pointed out by Shin Hyun-song came out... Should we raise interest rates further?
  - [china] China's PBOC Lowers Relending Rate for Stock Buybacks
  - [korea] South Korean won climbs, Taiwan dollar lags among mixed Asian FX
  - [china] China Services PMI Ebbs In October - Caixin
  - [china] CHINA PBOC CONDUCTS CNY257.5 BLN VIA O/N REVERSE REPO WEDS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7180 WEDS VS 6.7150
  - [korea] Samsung Electronics, SK hynix rally on Wall Street chip rebound
  - [japan] Stock prices drop by more than 2,000 yen at one point; sell orders spread for stocks such as semiconductors
  - [china] How to understand the central bank’s increase in the foreign exchange deposit reserve ratio?
  - [china] On November 4, the central bank launched a 257.5 billion yuan overnight reverse repurchase operation.
  - [china] The central bank launched a 257.5 billion yuan overnight reverse repurchase operation today
  - [china] China PBOC Pledges to Fully Meet Future Re-Lending Demand
  - [china] China PBOC: Banks Have Applied for Relending Quotas Exceeding 200 Billion Yuan
  - [china] China PBOC: The 1-Year Relending Facility Supports 26 Major Banks
  - [china] China PBOC: It's Ramping Up Relending Policy for Stock Buybacks
  - [china] What are the implications of the central bank raising the foreign exchange deposit reserve ratio for the first
  - [china] China PBOC Says It Cuts Relending Rate for Stock Buybacks to 1%
  - [japan] The fiscal burden is almost the same as "zero consumption tax," but the Ministry of Finance's "sneaky true int
  - [japan] Monetary base fell 13.6% year-on-year in October, rate of decline slowing - Bank of Japan (Reuters)
  - [japan] The Bank of Japan decides to maintain the status quo of monetary policy (Hiroyuki Kubota) - Expert
  - [korea] [Analysis] Despite the slowdown in prices in October, interest rates are expected to increase in November

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
      "published_utc": "2026-11-04T04:52:44+00:00",
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

