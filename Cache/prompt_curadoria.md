atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-12T07:12:43.895672+00:00
Total: 2870 manchetes

  🇯🇵 Japão          1108
  🇨🇳 China          790
  🇹🇼 Taiwan         278
  🇰🇷 Coreia do Sul  694

## O que já está no feed (não repita)

  - [korea] Seoul shares plunge over 3 pct on tech sell-off amid Mideast, inflation woes
  - [korea] Micron, SK Hynix Stocks Slip Overnight: China’s CXMT Advances Next-Gen DRAM Technology
  - [korea] (LEAD) Seoul shares plunge over 3 pct on tech sell-off amid Mideast, inflation woes
  - [korea] Asia stocks mixed as Korean chipmakers slide on CXMT threat
  - [korea] The Bank of Korea repeatedly hinted at the possibility of further interest rate hikes... Market outlook “withi
  - [korea] Bank of Korea Governor Shin Hyun-song “When deciding on interest rates, price trends are the top priority… Red
  - [korea] Kospi Falls for Fourth Straight Session; Chip Stocks Retreat
  - [korea] Bank of Korea Governor Shin Hyun-song: “Further interest rate hikes, price trends are the most important”
  - [china] China home car sales downturn continues, exports retain momentum
  - [china] China Says EU Must Ensure Non-Discriminatory Treatment of Hybrid-Car Exports
  - [korea] Shin Hyun-song “Always check the adaptability of economic entities when carrying out monetary policy” (compreh
  - [korea] [Planning] Amid expectations of October freeze, there are still calls for further interest rate hikes
  - [korea] In response to the question, “Will the base interest rate be raised again in October?” The answer given by the
  - [korea] Shin Hyun-song "Monetary policy is having an effect... Policy stance is more important than interest rate hike
  - [korea] S.Korean stocks slide as chip selloff deepens, foreign selling persists
  - [japan] Dollar steady near 18-month high as Mideast conflict, US inflation in focus By Reuters
  - [korea] The annual income standard for young people who can sign up for the Youth Housing Dream subscription..
  - [korea] Bank of Korea Governor Shin Hyun-song attends the G20 and IMF general meetings... Monetary policy and internat
  - [korea] SK Hynix tests KRW 1,633,000 support after H&S breakdown: Live
  - [taiwan] Stocktwits Tech Watch: ASML, TSMC Earnings This Week And Apple’s Next Home Play
  - [china] China sanctions Paraguay, Belize ministers over Taiwan ties
  - [china] Offshore Yuan Strongest Since 2022
  - [korea] Will the Bank of Korea raise the base interest rate further within the year? Shin Hyun-song: “Preemptive respo
  - [korea] [National Assembly Inspection 2026] Shin Hyun-song “We gained time by raising interest rates… We reduced costs
  - [china] China Plays Critical Role in Global AI Supply Chain, Domestic AI Ecosystem — Market Talk
  - [taiwan] Taiwan semiconductor industry eyes landmark geothermal power deal exceeding 20MW
  - [korea] CXMT: How big is its market threat to Samsung, SK Hynix and Micron?
  - [korea] Why is Samsung Electronics stock sliding today?
  - [korea] Why is SK Hynix stock sliding today?
  - [china] Yuan holds near 3-1/2-year high against dollar as rate bets ease
  - [japan] Nikkei average growth is sluggish, focus on TSMC performance and price index (TV Asahi (ANN))
  - [taiwan] Elon Musk Wants Tesla, SpaceX To Test 10 Chip Designs A Year At Terafab As TSMC Reportedly Eyes Texas
  - [china] EU-China Deal Could Halve Chinese Hybrid Car Exports
  - [china] China Moves to Stave Off Wider EU Trade War With Hybrid Deal
  - [china] PBOC Expected to Tolerate Further Gradual Yuan Appreciation — Market Talk
  - [korea] South Korean Won Hits 2-Year High
  - [korea] Bank of Korea Governor Shin Hyun-song: “Monetary policy independence is firm”… Leveraged ETF admits lack of ri
  - [china] China Sanctions Officials of Taiwan’s Allies for the First Time
  - [korea] South Korean Won Hits 24-month High
  - [taiwan] Gold gains on weaker oil, dollar; US inflation data in focus

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
      "published_utc": "2026-10-12T07:12:44+00:00",
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

