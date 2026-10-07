atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-07T00:22:46.776557+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1289
  🇨🇳 China          778
  🇹🇼 Taiwan         258
  🇰🇷 Coreia do Sul  675

## O que já está no feed (não repita)

  - [japan] JGB Futures Edge Higher, Tracking Gains in U.S. Treasury Market — Market Talk
  - [japan] Analysis-Japan’s $15 billion Rapidus chip bet hinges on winning customers
  - [japan] Japan Forex Reserves Fall Further in September
  - [korea] Samsung Electronics poised to top $74bn in Q3 OP
  - [japan] Monetary Base and the Bank of Japan's Transactions (Sept.)
  - [japan] Bank of Japan's Transactions with the Government (Sept.)
  - [japan] Market Operations by the Bank of Japan (Sept.)
  - [japan] Japan considers another extra budget for disaster relief, Yomiuri says
  - [japan] Japan manufacturers’ mood hits near 5-year high, service-sector sentiment slumps: Reuters poll
  - [korea] Samsung’s Q3 profit seen jumping nine-fold, but chip margins may be flat
  - [japan] Japan Manufacturers' Confidence Highest Since 2021
  - [japan] Bank of Japan interest rate hike "at a time that doesn't kill the economy," Councilor Sato says in a media int
  - [japan] BOJ's dovish dissenter signals support for future rate hikes
  - [japan] BOJ's Sato signals support for future rate hikes, Kyodo reports
  - [japan] Is it wrong to say that "Japanese houses are high-performance"? "The weakest function in developed countries" 
  - [korea] NLST Stock Jumps 18% After Micron’s $600M License Deal — Retail Now Awaits SK Hynix
  - [taiwan] TSMC boosts US investments to $265B on AI boom: report
  - [china] Uncertainty mounts in Singapore after China tightens offshore trust rules
  - [japan] Will the "$30 billion result" won by Trump at the US-China summit help the Republican Party in dire straits? "
  - [japan] Ebara challenges champion AMAT with semiconductor CMP equipment, "three weapons" unleashed by generation AI bo
  - [china] Wabash Welcomes Final U.S. Ruling on Unfairly Traded Chinese Trailer Imports; Canada and Mexico Investigations
  - [china] Wabash (WNC) Says U.S. Finalizes China Trailer AD/CVD; 232 Tariffs Stack
  - [taiwan] TSMC and other Taiwan players boost AI spending in US, Southeast Asia
  - [japan] Towa plans chipmaking tool plant for Japanese supply chain: CEO
  - [taiwan] Intel Stock Slips as TSMC Talks Complicate TeraFab's 14A Bet
  - [korea] Samsung Biologics union seeks bargaining with Samsung Electronics
  - [taiwan] TSMC Stocks Drop as Musk Confirms Terafab Talks Without a Deal
  - [korea] South Korea exports eased Russia fuel crisis caused by drone strikes, Ukraine says
  - [japan] Bank of Japan member Sato favors continuing interest rate hikes without specifying timing, concerns about weak
  - [taiwan] Taiwan's AUO, Innolux bet on glass as next-gen AI chip material
  - [taiwan] Taiwan Semiconductor Price Target Raised to $665.00/Share From $650.00 by Barclays
  - [japan] "There are too many needs for semiconductors or GPUs"...Minister of Economy, Trade and Industry Akazawa says i
  - [japan] Japanese Yen Likely to Rise if Fed Lifts Rates Less Than Expected — Market Talk
  - [korea] NPS cuts Korean tech winners for insurers, defensive stocks as interest rates rise
  - [korea] Numeraire: Upbit opens KRW and USDT spot trading - 06 Oct 2026
  - [japan] Kawasaki Heavy to launch dog-shaped social robot by fiscal 2028
  - [japan] Finance Minister Katayama: ``This is not an election campaign'' according to some reports
  - [china] China turns on the export taps as LME zinc squeeze grinds on: Andy Home
  - [china] MORE U.S. AUGUST TRADE: CHINA DEFICIT UP TO $16.4 BILLION FROM $15.2 BILLION IN JULY
  - [korea] Roze AI Expands Disaster Prevention and Physical AI Business with Approximately US$12.2 Million (KRW 16.4 Bill

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
      "published_utc": "2026-10-07T00:22:46+00:00",
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

