atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-04T12:42:43.592430+00:00
Total: 2935 manchetes

  🇯🇵 Japão          850
  🇨🇳 China          876
  🇹🇼 Taiwan         310
  🇰🇷 Coreia do Sul  899

## O que já está no feed (não repita)

  - [japan] House of Representatives Finance and Financial Affairs Committee Consumption tax reduction bill Ruling parties
  - [japan] ``You can just drop in and have a casual time'' at the former Bank of Japan Kanazawa branch, with many request
  - [china] Chinese chipmaker YMTC puts IPO on hold as weaker markets weigh, sources say
  - [japan] National Governors Association requests correction of uneven distribution of taxes, etc. ahead of tax reform d
  - [china] The central bank will launch a 300 billion yuan buyout reverse repurchase operation
  - [china] The central bank raised the foreign exchange deposit reserve ratio for the first time in the past five years
  - [japan] ``We should enter into a full-fledged discussion about the future image'' of the former Bank of Japan Kanazawa
  - [taiwan] Mediatek Shahriari to strengthen collaboration with key supply chain partners including TSMC
  - [taiwan] Exporters sell foreign exchange and foreign capital remittances compete, the New Taiwan dollar closes down 6.1
  - [china] Central Bank: It will launch a 300 billion yuan buyout reverse repurchase operation on November 5 with a perio
  - [china] Central Bank: From November 15, increase the reserve requirement ratio of foreign exchange deposits of financi
  - [japan] Department stores announce lucky bags in anticipation of rising prices and consumption tax cuts
  - [japan] The Bank of Japan's December interest rate hike is judged to be in flux ~ Between "reports" and "analysis" ~ (
  - [taiwan] Blue means Taiwan has fallen into structural inflation Green: Will ask the political Yuan to track food prices
  - [japan] Consumption tax reduction bill Liberal Democratic Party: “Vote on the 6th” Democratic Party: “Decision after l
  - [japan] New valuation method for unlisted company stocks “Ruling party tax investigation committee” Finance Minister K
  - [china] Central Bank: Will launch 300 billion yuan buyout reverse repurchase operation on November 5
  - [china] Chinese Vice Minister of Commerce Li Chenggang meets with KKR's Nuttall
  - [korea] Hanwha Co., Ltd. exceeded its net profit of KRW 1 trillion in the third quarter of this year alone.
  - [korea] Democratic US election sweep lifts Korean batteries but clouds chip outlook
  - [china] "China could erode 2.2 trillion won in South Korean EV exports in four years"
  - [korea] TCL Technology: Samsung Electronics to Become Direct Shareholder of TCL CSOT Following Transaction
  - [korea] Samsung Display to Transfer Its 10.16% Stake in TCL China Star Optoelectronics Technology to Samsung Electroni
  - [japan] BREAKING NEWS: JR Kyushu says Kumamoto quake losses total about 17 billion yen
  - [china] Hong Kong Shares Bounce Back to End Higher, Led by Semiconductor Stocks — Market Talk
  - [china] Hong Kong Stocks Bounce Back to End Higher, Led by Semiconductor Stocks — Market Talk
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Report on Share Disposition Results
  - [japan] Yen up, stocks down in Tokyo as Japan digests midterms
  - [china] Asian FX gains as dollar falls on U.S. midterm results, yuan weakens on PBOC move
  - [korea] Food Week Korea opens in Seoul with focus on exports, food technology
  - [japan] Collateral Accepted by the Bank of Japan (End of Oct.)
  - [japan] Japanese Government Bonds Held by the Bank of Japan
  - [japan] Mitsui & Co Ceo: Aim To Achieve Net Profit Of More Than 1.1 Trillion Yen And Roe Of Over 12% In Fy2028, Driven
  - [korea] A total of 10.894 billion won in monetary sanctions have been confirmed to six securities companies
  - [japan] The Ministry of Finance points out at the Fiscal Council that the cost of medical care for the elderly will be
  - [japan] Japan futures fall for 4th session as yen jumps, Tokyo equities drop
  - [china] Lowers stock repurchase and refinancing interest rates to 1% China's central bank: Provides adequate quota gua
  - [japan] TSE continues to fall, selling mainly in semiconductor-related stocks
  - [china] CNOOC Limited Class A Stock 12‑Month Price Target Raised to CNY 44.7, Implies 31% Upside
  - [korea] Imported vehicle sales jump 29.3% in Oct. on strong EV demand

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
      "published_utc": "2026-11-04T12:42:43+00:00",
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

