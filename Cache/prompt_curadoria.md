atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-30T06:22:46.174515+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1260
  🇨🇳 China          777
  🇹🇼 Taiwan         247
  🇰🇷 Coreia do Sul  716

## O que já está no feed (não repita)

  - [taiwan] Why TSMC’s capacity crunch opens the door for Samsung’s foundry
  - [korea] Korea lifts tax revenue forecast to record W478.6tr on chip boom
  - [korea] Industrial output, retail sales, facility investment down in Aug.
  - [japan] Regarding the government's denial of reflation and the Bank of Japan's acceleration of the pace of interest ra
  - [china] China adds 55% tariff to Brazil beef as imports hit quota
  - [japan] Japan Housing Starts Rise Less than Estimated
  - [japan] Japan Production Likely Supported by AI-Related Capex — Market Talk
  - [china] China’s ‘Mini Stimulus’ Seen Securing GDP Target, Not Much More
  - [korea] South Korea's Headline Inflation Likely Eased in September, Poll Shows — Market Talk
  - [china] China factory activity grows at fastest pace in 5 months in Sept: RatingDog PMI
  - [china] China stocks flat, limp to quarterly drop, as stimulus falls short
  - [japan] Japan's industrial output drops 1.7% M/M in August; retail sales rise 2.7% Y/Y
  - [japan] Asian currencies mixed as yen rebounds, dollar stays near two-month high
  - [japan] Asia stocks mixed ahead of U.S. PCE inflation; regional data in focus
  - [china] Standard Chartered does not rule out the possibility of central bank cutting RRR
  - [japan] Yen Strengthens Past 157 Per Dollar, Outperforming G-10 Peers: JPY/USD
  - [japan] Yen's Long-Term Trend Has Likely Turned to Appreciation — Market Talk
  - [china] China’s weak soybean demand dims prospects for US cargoes after tariff snub
  - [taiwan] Foundry 2.0 revenue hits record as growth spreads beyond TSMC
  - [china] Yuan set for 7th straight quarterly gain as exporters sell dollars before holiday
  - [china] China stimulus picks: tech and consumer names tied to new credit flows
  - [korea] Korea’s Aug factory output, consumption, investment tumble on Hyundai strike; bond yields fall
  - [china] DeepSeek partners with Huawei to develop chip programming tools, reducing reliance on Nvidia
  - [china] Offshore Yuan Holds Gains
  - [china] China’s Two-Speed Economy Spurs Yawning Gap Between Stocks, Yuan
  - [china] China's DeepSeek says it used open-source tools based on Huawei ascend chips
  - [china] China Warns Broad EU Tariffs Could Disrupt Trade Negotiations
  - [korea] Rupiah gains; Korean won, Philippine peso weaken among mixed Asian FX
  - [china] China's New Mortgage Subsidy Falls Short of Expectations — Market Talk
  - [china] Trade Talks, Rare-Earth Exports Key Near-Term Gauges of U.S.-China Ties — Market Talk
  - [taiwan] TSMC reportedly evaluates Texas fabs as US regional competition intensifies
  - [japan] Yen Set for Monthly Advance
  - [china] Chinese stocks inch up after Beijing's fresh stimulus but property stocks slide
  - [china] CHINA PBOC CONDUCTS CNY833.5 BLN VIA O/N REVERSE REPO WEDS
  - [china] China services growth hits three-month high, private PMI shows
  - [china] China Manufacturing Growth Hits 5-Month High
  - [china] China factory activity hits five-month high in September, private PMI shows
  - [china] China NBS General PMI Rises to 9-Month High
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7351 WEDS VS 6.7411
  - [korea] Samsung Electronics, SK hynix rise as U.S. chip stocks rally

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
      "published_utc": "2026-09-30T06:22:46+00:00",
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

