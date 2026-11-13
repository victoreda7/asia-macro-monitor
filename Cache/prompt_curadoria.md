atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-13T05:12:41.847485+00:00
Total: 3000 manchetes

  🇯🇵 Japão          989
  🇨🇳 China          865
  🇹🇼 Taiwan         308
  🇰🇷 Coreia do Sul  838

## O que já está no feed (não repita)

  - [japan] SMC Corp - Announces Maximum Buyback Value Of Jpy 50 Billion
  - [korea] SEMIFIVE Secures KRW 178.4 Billion in Q3 New Orders, Up 437% YoY, Driving Order Backlog to Record High
  - [korea] SEMIFIVE Q3 Orders Rise 437% YoY to KRW 178.4B
  - [japan] Presidents of Chile and Peru will visit Japan next week to hold summit meeting with Prime Minister Takaichi
  - [japan] Berkshire Hathaway aims to raise $1.1 billion in yen bond sale, term sheet shows
  - [china] Toyota rewires China supply chain to fight back in EV race
  - [japan] BOJ not planning further ETF sales review now, Himino says
  - [china] China's yuan inches higher as companies convert cash holdings
  - [korea] Import prices fall again in Oct. on stronger S. Korean won, lower oil prices
  - [china] The U.S. Congress plans to tighten the export of AI chips to China, making it more difficult for China to obta
  - [china] The central bank launched a 300 billion yuan 7-day reverse repurchase operation in the open market today
  - [korea] It was found that the top 1% of stock investment returns sold SK Hynix and Samsung Electronics in la..
  - [taiwan] Sheffield, Taiwan firms target aerospace, defense semiconductor opportunities
  - [china] Chinese shares lead Asia chip rally amid Jensen Huang turmoil
  - [china] PBOC Looks Focused on Directing Credit Toward Priority Sectors — Market Talk
  - [japan] Stock price rise Buy orders for AI/semiconductor related stocks
  - [japan] U.S. Treasury Department “purchased 79.4 billion yen worth of yen” during Japan-U.S. joint intervention, Fed r
  - [korea] S. Korean gov't sees solid economic growth trend amid surging exports, investment
  - [japan] Asia FX: yen intervention in focus as rate hike bets put dollar near 19-mth high
  - [china] Mike Johnson Sees Growing Support For China Chip Restrictions As Nvidia’s Jensen Huang Exit Rocks Washington: 
  - [taiwan] TSMC seeks to back next chip titan with new investment arm
  - [japan] Obayashi Corporation - To Buy Back Up To 2.9% Of Own Shares Worth 30 Billion Yen
  - [korea] Cloud: Upbit opens spot trading in KRW, BTC and USDT markets - 13 Nov 2026
  - [japan] Japanese yen tests 160 again, drawing intervention threats
  - [japan] Toda Corporation Says It Will Buy Back Up To 2.7% Of Own Shares Worth 10 Billion Yen
  - [china] The U.S. Congress has launched a bipartisan effort to regulate semiconductors...It will also affect Samsung El
  - [japan] Japan futures set for first weekly gain in five as yen weakens, oil jumps
  - [korea] South Korean won gains most among tepid Asian FX
  - [korea] i3system: Infrared-led growth lifted 9M revenue and operating income; orders reached KRW 151.82bn.
  - [china] Chinese e-commerce sellers brace for Thai duties. Will a 30% tariff hurt sales?
  - [japan] Japan’s finance minister vows action as yen breaches 160 threshold
  - [korea] On the 13th, KBI Metal, a wire material and automotive electronic parts manufacturer of KBI Group, s..
  - [china] China Chipmaker SigmaStar Said to Plan $300 Million HK Listing
  - [korea] Samsung, SK hynix gain over 2% despite Nvidia sell-off
  - [japan] Dollar near 19-month high on Fed hike bets, yen tests 160
  - [china] The central bank announced: Today it will launch a 364 billion yuan overnight reverse repurchase operation
  - [japan] Japan's Finance Minister Warns Against Rapid Yen Moves
  - [china] CHINA PBOC CONDUCTS CNY300 BLN VIA 7D REVERSE REPO FRI
  - [china] CHINA PBOC CONDUCTS CNY364 BLN VIA O/N REVERSE REPO FRI
  - [china] The central bank launched a 300 billion yuan 7-day reverse repurchase operation today - 36 Krypton

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
      "published_utc": "2026-11-13T05:12:42+00:00",
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

