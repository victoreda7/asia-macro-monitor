atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-05T07:02:46.887320+00:00
Total: 2888 manchetes

  🇯🇵 Japão          1231
  🇨🇳 China          762
  🇹🇼 Taiwan         245
  🇰🇷 Coreia do Sul  650

## O que já está no feed (não repita)

  - [china] India may be best placed to fill a China-sized hole in fuel exports: Maguire
  - [japan] Takaichi pledges fiscal discipline as Japan’s debt bill rises
  - [taiwan] Taiwan's September Inflation Likely Exceeded 2%, WSJ Poll Shows — Market Talk
  - [japan] Bank of Japan's output gap increases by 0.55% in April-June quarter, supporting continued interest rate hike (
  - [japan] Japan’s PMI data signals cooling momentum across manufacturing and services
  - [japan] Output Gap, Potential Growth Rate, and Labor Market Indicators
  - [china] Weekly Recap: ’26 9–10% currency-neutral guidance and China push
  - [taiwan] Global AI servers shift production nearshore, slowing direct Taiwan exports to US
  - [korea] South Korean Won Firms Near 2024 High
  - [taiwan] TSMC, Intel named as Musk's Terafab ambitions face reality check
  - [china] China-EU Trade Talks Unlikely to Result in Major Breakthroughs — Market Talk
  - [taiwan] Tesla Stock Rises Overnight After Musk Says ‘Something May Come Of’ TSMC Talks On Terafab
  - [china] Tata's Assam chip unit is almost ready, and a non-China supply chain is in place
  - [japan] BOJ says AI boom may have eased financial conditions, warns of market risks
  - [china] ZAWYA: Egypt’s food industry exports to China rise 21% YoY in 8 months
  - [japan] Extraordinary National Diet convenes to debate bills such as “Food consumption tax reduction” bill
  - [japan] Yen Holds Steady as Traders Await Economic Data
  - [korea] “The government bond interest rate is over 5%, so how much will the loan interest rate rise?” Increasing press
  - [japan] Prime Minister Takaichi will be forced to make a major decision at the end of the year, and with the rise of t
  - [taiwan] Taiwan dollar gains most among muted Asian currencies
  - [taiwan] TSMC emerges as potential Terafab partner as suppliers see over 80% chance of Musk deal
  - [taiwan] Shield AI expands Taiwan supply chain in sovereign AI push
  - [japan] BOJ’s Deputy Chief Flags AI’s Possible Impact on Neutral Rate
  - [taiwan] Weekly news roundup: Musk looms large as AI chip boom drives capacity expansion and geopolitical risks
  - [japan] Japan services PMI misses forecasts in September as private-sector growth slows By Investing.com
  - [japan] Japan services PMI misses forecasts in September as private-sector growth slows
  - [japan] Japan's Rapidus To Help 17 Companies Design Chips For Clients, Nikkei Says
  - [japan] Interview: The role of reflation policy has ended, and demand expansion from here is a "risk" - Former Bank of
  - [korea] If the loan interest rate rises, house prices fall after 6 months.
  - [japan] Japan service sector activity slows from 5-month high, PMI shows
  - [japan] BOJ's Uchida flags AI's mixed impacts on productivity
  - [japan] Opening Remarks by Deputy Governor UCHIDA at the ECONDAT 2026 Fall Meeting (AI, Big Data, and Monetary Policy)
  - [japan] Reflationist ex-BOJ policymaker calls end to low rates, big spending
  - [japan] JGBs Mixed Ahead of Expected Extraordinary Diet Session in Japan — Market Talk
  - [china] As US bears down, exporters China and Vietnam establish closer transport links
  - [japan] Sources of Changes in Current Account Balances (Projections for Oct.)
  - [korea] Mortgage interest rates are also ‘fluctuating’… Will interest rates rise further due to the additional hike by
  - [china] U.K. is said to plan tariffs on Chinese EVs under pressure from EU
  - [china] Britain set to levy tariffs on Chinese electric cars, The Times reports
  - [japan] Is a variable type home loan still more advantageous? Should I switch to a fixed rate due to concerns that wil

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
      "published_utc": "2026-10-05T07:02:47+00:00",
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

