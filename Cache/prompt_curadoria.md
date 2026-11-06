atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-06T02:52:45.668547+00:00
Total: 3000 manchetes

  🇯🇵 Japão          893
  🇨🇳 China          896
  🇹🇼 Taiwan         325
  🇰🇷 Coreia do Sul  886

## O que já está no feed (não repita)

  - [japan] Consumption tax reduction bill passed by the House of Representatives Finance Committee and will be passed by 
  - [japan] Prime Minister Takaichi's consumption tax reduction bill: “Support based on income for more than 30% of worker
  - [korea] Mercedes-Benz overtakes BMW to rank second in imported car sales
  - [japan] Shimane Bank has fallen into a large deficit forecast and was forced to increase its capital by 10 billion yen
  - [japan] Proceeds from the sale of Bank of Japan ETFs will be used for growth investment as a source of funds for redem
  - [korea] Why is SK Hynix stock crashing today?
  - [taiwan] Why is TSMC stock plunging today?
  - [taiwan] Taiwan dollar, Malaysian ringgit lead losses in Asian currencies
  - [taiwan] In line with international trade fishing and management, the Fisheries Department piloted the opening of expor
  - [china] Nvidia chips pile up in Hong Kong as China withholds import approval
  - [korea] Why is Samsung Electronics stock plunging today?
  - [china] CHINA PBOC CONDUCTS CNY226 BLN VIA O/N REVERSE REPO FRI
  - [japan] JGB Yields Fall as Stock Markets Drop Sharply — Market Talk
  - [japan] Bank of Japan's additional ETF sales proceeds will lead to further growth through reinvestment - Prime Ministe
  - [japan] Japan to spend proceeds from BOJ’s ETF sales on growth areas, PM says
  - [taiwan] Taiwan's market fundamentals are good, deputy finance minister says
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7168 FRI VS 6.7156
  - [japan] Dollar holds, yen gains as equity rout saps risk appetite ahead of payrolls
  - [china] Chances are, US-China truce will be extended at Shenzhen Apec summit
  - [japan] Japan MOF To Auction Y3.1T Of TD-Bills Nov 13
  - [japan] BREAKING NEWS: Japan to use 10 bil. yen from reserve funds for cybersecurity measures
  - [taiwan] TSMC Plunges 9.8%; Foxconn Down 9.15%
  - [korea] Coway Co., Ltd. Overseas Revenue Rises 26.2% to KRW 591.8B
  - [japan] Bank of Japan ETF sales increase, not used to finance consumption tax cut (Kyodo News)
  - [korea] South Korea stocks plunge 8%, circuit breaker triggered as chip shares tumble
  - [korea] Samsung, SK hynix slide 10% as AI data center fears spread
  - [korea] Finance minister vows timely actions to ease stock market volatility
  - [china] Analysis-China’s yuan dilemma: too weak abroad and too strong at home
  - [china] Dongguan Mentech Plans To Raise Up To 1.28 Bln Yuan In Share Placement
  - [korea] South Korea finance minister vows to curb excessive stock market volatility
  - [japan] Japan’s real wages rise for ninth month in September, backing BOJ rate hike
  - [japan] Yen Rises on Haven Demand as CIBC, Nomura See Room for More Gain
  - [china] US extends suspension of export restrictions on Chinese firms
  - [korea] [Blue tsunami emergency diagnosis] Bond market: “If it reaches 4,000 pi, it will be impossible to raise the ba
  - [korea] Filibuster over bill on alleged fabricated indictments
  - [taiwan] Foxtron aims to turn Taiwan's automotive supply chain into a global net-zero force
  - [china] Oversea-Chinese Banking: Global Conditions Remain Uncertain Amid Geopolitical Tensions, Inflation Risks >O39.S
  - [japan] Upward price fluctuation risk, interest rate hike appropriate, policy “change in phase” Bank of Japan Septembe
  - [korea] “Will it go up again?”... November 26, the base interest rate is 3.25%. If the mortgage is 300 million won, yo
  - [japan] Analysis-Japanese savers have rediscovered interest rates and banks are feeling it

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
      "published_utc": "2026-11-06T02:52:45+00:00",
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

