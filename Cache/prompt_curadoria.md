atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-13T09:52:43.764550+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1134
  🇨🇳 China          835
  🇹🇼 Taiwan         297
  🇰🇷 Coreia do Sul  734

## O que já está no feed (não repita)

  - [korea] South Korea central bank to keep policy restrictive until inflation hits target, governor says
  - [china] IMF Cuts China Growth Forecasts for 2026 and 2027
  - [korea] KOSPI Slumps as U.S. AI Chip Panic Spreads — Barrons.com
  - [japan] Intervention Risk Limits Yen Falls Against Dollar — Market Talk
  - [japan] 88% of people expect prices to rise one year from now, Bank of Japan's September lifestyle awareness survey (K
  - [china] Chip selloff deepens amid AI trade fears, rising Chinese competition
  - [korea] The Ministry of Finance and Economy announced an administrative notice on the 13th to raise the pre
  - [japan] Former NHK Chairman Nobuo Inaba dies at age 75, former Bank of Japan board member (Jiji Press)
  - [korea] Commercial banks are offering non-face-to-face real estate mortgage loans for private businesses. Th..
  - [korea] [Photo] Export-import silver supports independence of isolated youth
  - [korea] Samsung Electronics chairman Lee to receive 2.6 trillion won worth of shares from mother, reports say
  - [japan] More than 80% predict that prices will rise in five years Bank of Japan's lifestyle awareness survey (TV Asahi
  - [china] Visa Wins Preliminary Approval for Yuan Card Clearing in China
  - [korea] Repeat & Correct: South Korea's Kospi Slumps on Selloff in Chip Stocks — Update
  - [china] Global chip selloff deepens as AI worries, China competition weigh
  - [japan] Former NHK chairman Nobuo Inaba dies at age 75, also serving as director of the Bank of Japan (Mainichi Shimbu
  - [taiwan] Taiwan panel makers enter semiconductor fight as structural challenges persist
  - [japan] Inflation expectations remain 86.5% higher in 5 years, highest level in 19 years due to Middle East impact, Ba
  - [taiwan] U.S. dollar closes sharply higher on Taipei forex market
  - [japan] Nobuo Inaba, former chairman of NHK and former director of the Bank of Japan, dies at age 75, announces lung c
  - [china] Cathie Wood warns of ‘vicious’ memory chip cycles as China adds capacity
  - [china] China's Export Rebate Cut to Cost NEV Makers 4,000-6,000 Yuan Per Vehicle — Market Talk
  - [korea] “We bought time by raising it before the US”... Bank of Korea plans to freeze base interest rate in October
  - [japan] Individuals' inflation expectations remain high: 86.5% that prices will rise in five years' time Bank of Japan
  - [korea] South Korea's Kospi Slumps on Selloff in Chip Stocks — Update
  - [japan] Stock prices have fallen significantly due to concerns about intensifying competition in the AI ​​and semicond
  - [korea] (2nd LD) Seoul shares dip over 5 pct on tech sell-off on renewed AI, inflation woes
  - [taiwan] TSMC, Intel supplier Qnity bets on local production to win business
  - [korea] Kospi tumbles as chip rout deepens, briefly breaking below 6,000
  - [china] South Africa Factories Crater as China Imports Stunt Revival
  - [korea] Foreign selloff sends Kospi down 5.5% as chip giants tumble
  - [china] China’s exports seen growing at faster pace in September: Reuters Poll
  - [korea] Seoul shares dip over 5% on tech sell-off on renewed AI, inflation woes
  - [korea] 'Brutal session' for chip stocks shows AI trade is turning
  - [korea] South Korea shares tumble in chip selloff
  - [korea] Korean Chip Stocks Sink on Chinese Rival Worry, Broadcom Remarks
  - [china] Key facts: NASDAQ:NVDA -1.6% on Microsoft Maia; China GPUs -44%; TSMC
  - [korea] (LEAD) Seoul shares dip over 5 pct on tech sell-off on renewed AI, inflation woes
  - [korea] Bae Jun-young: “Bonk Governor needs to ‘reexamine the starting point’ of raising base interest rate this month
  - [china] Asia stocks slide as chip rout deepens, Chinese automakers hit by EU trade curbs

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
      "published_utc": "2026-10-13T09:52:43+00:00",
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

