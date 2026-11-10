atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-10T04:12:44.038541+00:00
Total: 3000 manchetes

  🇯🇵 Japão          931
  🇨🇳 China          896
  🇹🇼 Taiwan         316
  🇰🇷 Coreia do Sul  857

## O que já está no feed (não repita)

  - [china] China's Trade Surplus Surged Past $1 Trillion in October — WSJ
  - [japan] Toray Industries - To Buy Back Up To 5.08% Own Shares Worth 70 Billion Yen
  - [japan] Toa Corp (Tokyo) - To Buy Back Up To 5.67% Of Own Shares Worth 8 Billion Yen
  - [china] China October soybean imports fall on high inventories, weak crush margins
  - [korea] Asia stocks rally as Korean chips surge and oil retreat lifts sentiment
  - [china] Yuan steady after dollar softens, awaits US CPI
  - [china] China’s October crude oil imports rise to highest level since March amid Middle East war
  - [china] China October rare earth exports jump 2.7% from prior month
  - [china] China's copper concentrate imports slump 11% in October as smelter woes deepen
  - [japan] Modec Inc - To Buy Back Up To 2.9% Of Own Shares Worth 10 Billion Yen
  - [china] China's iron ore imports at five-month low as thin margins dent appetite
  - [china] The Trump-Xi APEC summit paved the way for China to extend its suspension of rare earth and other export contr
  - [japan] In Japan chip deal, everyone wins except the buyer
  - [korea] Korean stocks rebound as chip giants lead recovery
  - [china] CXMT chairman's reported DeepSeek investment spotlights China's semiconductor capital network
  - [china] China exports stay resilient as trade surplus tops $1tn
  - [china] CHINA JAN-OCT IMPORTS +23.6% Y/Y IN YUAN TERM: CUSTOMS
  - [china] China trade balance shrinks more than expected in Oct; imports surge
  - [japan] Additional proceeds from the sale of Bank of Japan ETFs “Used as a financial source for the Special Account fo
  - [china] China Export Growth Eases in October as Imports Surge
  - [china] China’s trade surplus soars past $1 trillion, October exports jump 35.2% y/y
  - [china] China's October coal imports fall 6% year-on-year
  - [china] China Chipmakers to Debut in HK in Test of Tech Stock Demand
  - [china] China Oct Exports +28.7% on Year in Yuan Terms
  - [china] China Oct Imports +34.7% on Year in Yuan Terms
  - [china] China Oct Trade Surplus CNY712.78B
  - [china] China Oct Trade Surplus $105.28B; Expected Surplus $126.9B
  - [china] China Oct Exports +35.2% on Year; Expected +36.1%
  - [china] China Oct Imports +41.6% on Year; Expected +34.0%
  - [japan] BOJ estimates $6 billion annual gain from faster ETF sales, finance minister says
  - [taiwan] Mitsui Chemicals to acquire JSR for US$11.6 billion, targeting semiconductor materials growth
  - [china] The central bank launched a 190 billion yuan overnight reverse repurchase operation in the open market today
  - [japan] Monetary policy method ``Everything is decided by the Bank of Japan'', no effect on ETF sales = Finance Minist
  - [korea] South Korea’s defense export boom exposes cockpit display vulnerability
  - [taiwan] IEAT and the Export-Import Bank of China signed an MOU to join forces to help enterprises expand into internat
  - [japan] ``I ate 180,000 yen sushi with my wife'' and ``Prices are rising.'' Pros and cons of Shinjuku ward councilor's
  - [china] On November 10, the central bank launched a 190 billion yuan overnight reverse repurchase operation.
  - [korea] Will the Bank of Korea put a brake on interest rate hikes as stock prices plummet?
  - [china] Chinese chip firms Denglin, Xinde open mixed in Hong Kong debuts
  - [japan] At the October meeting of the Bank of Japan, many voices called for interest rate hike “quickly”; it is import

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
      "published_utc": "2026-11-10T04:12:44+00:00",
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

