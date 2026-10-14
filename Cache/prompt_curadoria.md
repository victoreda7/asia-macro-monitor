atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-14T02:22:42.206290+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1134
  🇨🇳 China          843
  🇹🇼 Taiwan         296
  🇰🇷 Coreia do Sul  727

## O que já está no feed (não repita)

  - [korea] Most Asian currencies on backfoot; South Korean won strengthens
  - [china] Announcement from the Central Bank: Launching a 56 billion yuan 7-day reverse repurchase operation. On October
  - [china] Tencent to Raise Around $5.7 Billion From Dollar, Yuan Bonds
  - [china] China producer inflation beats forecasts as commodity costs rise, CPI lags
  - [china] China Sep Exports +29.6% on Year in Yuan Terms
  - [china] China Sep Imports +24.6% on Year in Yuan Terms
  - [china] The central bank launched a 56 billion yuan 7-day reverse repurchase operation with an interest rate unchanged
  - [china] China's yuan-denominated September exports rose 29.6%, imports 24.6%
  - [china] CHINA SEP NON-FOOD PRICES +1.5% Y/Y VS +1.2% Y/Y AUG
  - [china] CHINA SEP FOOD PRICES -1.7% Y/Y VS -1.4% Y/Y AUG
  - [china] CHINA SEP PPI +1.2% M/M VS +0.4% M/M AUG
  - [china] CHINA SEP CPI +0.2% M/M VS +0.4% M/M AUG
  - [china] China's Consumer, Producer Prices Accelerated in September
  - [china] China Food Prices Fall for 6th Month
  - [china] China CPI inflation grows less than expected in Sept; PPI hits 4-yr high
  - [china] CHINA PBOC CONDUCTS CNY56 BLN VIA 7-DAY REVERSE REPO WEDS
  - [china] China's consumer prices rose 0.9% in September (Kyodo News)
  - [china] China Producer Inflation Highest Since 2022
  - [china] China Inflation Rate Slightly Below Estimates
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7249 WEDS VS 6.7298
  - [china] China Sep Non-Food Prices +1.5% on Year
  - [china] China Sep Food Prices -1.7% On Year
  - [china] China Jan-Sep CPI +0.9% on Year
  - [china] China Sep CPI +0.2% on Month
  - [china] China Sep CPI +0.9% on Year; Market Expected +1.0%
  - [japan] Hitoshi Sasaki, former Matsuyama branch manager, will be the new manager of the Bank of Japan Shizuoka branch.
  - [china] The central bank launched a 56 billion yuan 7-day reverse repurchase operation today
  - [china] The central bank launches 56 billion yuan 7-day reverse repurchase operation
  - [korea] Rep. Yoon Hu-deok, Bank of Korea's National Audit Office intensively inspects the effects of interest rate hik
  - [korea] SK Hynix bounces in downtrend after support breach: Live levels
  - [japan] Bank of Japan Accounts (October 10)
  - [taiwan] TSMC-GF interposer deal reshapes US AI supply chain, from CoWoS to HBM
  - [china] China's wafer-scale graphene breakthrough brings quantum rectifiers closer to semiconductor integration
  - [japan] Nikkei Rises 0.3% on Possible Position Adjustments Before U.S. CPI Data — Market Talk
  - [china] Nantong Lianya To Sell 133.7 Mln Shares At 7 Yuan apiece in Shenzhen Listing
  - [korea] Key facts: Samsung Electronics (005930) 55% margin; Goldman Buy; fell
  - [japan] September money stock M2 increased 2.0% year-on-year = Bank of Japan (Reuters)
  - [china] Tencent prices $1.8 billion, 26 billion yuan notes under MTN programme
  - [china] China Inflation, Trade Data Due On Wednesday
  - [taiwan] TSMC Stocks Slip as Thursday's Earnings Put AI Margins Under Scrutiny

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
      "published_utc": "2026-10-14T02:22:42+00:00",
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

