atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-26T02:02:41.739635+00:00
Total: 3000 manchetes

  🇯🇵 Japão          917
  🇨🇳 China          980
  🇹🇼 Taiwan         339
  🇰🇷 Coreia do Sul  764

## O que já está no feed (não repita)

  - [japan] BOJ's Tamura Urges Timely Rate Hikes, Bolstering Case for December Move
  - [korea] BOK: All Board Members Leave Door Open to More Rate Increases Over Next Six Months
  - [korea] BOK: Sees Core Inflation Averaging 2.6% in 2026 and 2027, Up From 2.5% for Both Years
  - [korea] BOK raises rates as expected, lifts growth outlook on AI-driven chip boom
  - [korea] BOK: Two Board Members Favored Holding Rates, While Five Supported Hike
  - [korea] Bank of Korea: Rate Decision Wasn't Unanimous
  - [japan] Long-Term JGB Yields Rise as Chip Stocks Rebound — Market Talk
  - [japan] BOJ’s Tamura signals chance of faster-pace interest rate hikes
  - [korea] [Full text] Bank of Korea Monetary Policy Committee resolution on monetary policy direction for November
  - [korea] Full text of BOK statement on monetary policy decision in Nov.
  - [korea] (URGENT) Rate hike decision in Nov. was not unanimous; 2 dissenting members: BOK
  - [korea] Base interest rate increase: It has risen to 3.25%. How much will my loan interest rate rise?
  - [japan] Announcement of 10-year JGBs to Be Issued in December 2026
  - [japan] Japan MOF To Auction Y2.6T Of 10-year Govt Bonds Dec 3
  - [korea] Bank of Korea raises base interest rate by 0.25% point... 3.25% per annum
  - [korea] Bank of Korea hikes rate to 3.25% against backdrop of strong economy
  - [korea] South Korean shares rise over 2% as central bank raises growth forecasts
  - [korea] Bank of Korea Delivers What May Be Its Last Hike of This Cycle — Market Talk
  - [korea] BOK revises up S. Korea's 2026 growth outlook to 3.9%, 4.1% for 2027
  - [korea] Bank of Korea Resumes Rate Hikes as AI Boom Fuels Growth
  - [japan] Bank of Japan councilor says interest rate hike will be slow and hasty (Kyodo News)
  - [korea] Bank of Korea raises base interest rate from 3.00% to 3.25%... last hike of the year
  - [korea] Bank of Korea hikes interest rates to 2-yr high
  - [korea] Bank of Korea raises interest rate to highest level in two years
  - [korea] (LEAD) BOK raises key rate to 3.25 pct to curb inflationary pressure
  - [korea] BOK raises rate to 3.25% in final hike of year
  - [korea] Bank of Korea raises base interest rate to 3.25%... Increase resumes after one month
  - [korea] [Breaking News] Bank of Korea lowers base interest rate to 3.25% per annum... Third raise this year
  - [korea] BOK raises key rate to 3.25 pct
  - [korea] Bank of Korea raises base interest rate by 0.25%p... At 3.25% per year (1 step)
  - [japan] Speech by Board Member TAMURA in Yamanashi (Economic Activity, Prices, and Monetary Policy in Japan)
  - [korea] Bank of Korea raises base interest rate to 3.25%... Third austerity this year alone
  - [korea] [Breaking News] Bank of Korea raises base interest rate by 0.25% point to 3.25% per annum
  - [korea] South Korea's central bank raises rates, upgrades 2027 growth outlook
  - [korea] South Korea's central bank resumes tightening with quarter-point hike
  - [korea] The Bank of Korea raises the base interest rate to 3.25%... austerity again
  - [korea] Bank of Korea raises base interest rate to 3.25% per annum... Economic growth rate expected to be 3.9% this ye
  - [korea] [Breaking News] The Bank of Korea raises its base interest rate by 0.25%p... 3.25% per annum in 2 years
  - [korea] [Breaking News] Bank of Korea raises base interest rate by 0.25% to 3.25% per annum
  - [korea] BOK revises up S. Korea's 2026 growth outlook to 3.9 pct, 4.1 pct for 2027

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
      "published_utc": "2026-11-26T02:02:41+00:00",
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

