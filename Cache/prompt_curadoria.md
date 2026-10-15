atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-15T08:33:41.256999+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1118
  🇨🇳 China          840
  🇹🇼 Taiwan         311
  🇰🇷 Coreia do Sul  731

## O que já está no feed (não repita)

  - [china] China stocks close at 14-month low as US inflation stokes Fed fears
  - [taiwan] TSMC CEO says profitability has no ceiling, plans High-NA EUV adoption in 2030
  - [taiwan] TSMC beats forecasts as quarterly sales, profits soar
  - [korea] South Korea, Japan agree to extend $10 billion currency swap
  - [japan] Japan Industrial Output Falls More Than Estimated
  - [taiwan] TSMC breaks silence on Musk's Terafab: Talks underway, but fab control non-negotiable
  - [korea] Kospi slides over 7% as chip stocks sink
  - [taiwan] Earnings Snapshot: Taiwan Semiconductor Manufacturing tops Q3 estimates, gives Q4 revenue guidance above estim
  - [japan] Japan futures fall as Tokyo equities slump, China imports weaken
  - [taiwan] Earnings call transcript: TSMC beats Q3 2026 estimates as stock slips
  - [korea] Seoul shares crash over 7% on chip rout amid AI, inflation woes
  - [japan] ``Don't be overly cautious about raising interest rates'', Bank of Japan's Councilor Koeda gives speech (Asahi
  - [taiwan] Wall St futures drop as hot CPI revives Fed hike concerns; TSMC results in focus
  - [japan] TSE closing price 3318 yen lower, third largest decline
  - [china] China long-dated bond yields hit 15-month low as PBOC keeps cash flowing
  - [japan] Japan's Nikkei slumps 5% as tech stocks hammered by AI, rate hike worries
  - [japan] Japan finance minister: G20 concerned over yields, FX volatility
  - [korea] Kospi Falls for Seventh Straight Session as Chip Stocks Slump
  - [taiwan] Taiwan Semiconductor Manufacturing in charts: Advanced chips drive 79% of Q3 wafer revenue
  - [korea] SK hynix ties U.S. NAND factory to approval for more equipment at China fab - report
  - [taiwan] TSMC Chairman: No Ceiling for TSMC Profitability, But Dramatic Improvement Won't Happen Overnight
  - [china] China launches large-scale economic stimulus package, despite sluggish domestic demand, fiscal support is "lim
  - [taiwan] QCOM, AVGO, NVDA Stocks In Focus As ByteDance Reportedly Closes In On A MediaTek Pact For AI Data Center Chips
  - [taiwan] Taiwan Semiconductor ADR earnings beat by $0.18, revenue topped estimates
  - [taiwan] TSMC Raises 2026 Revenue Growth Forecast to Around 44%
  - [taiwan] TSMC profit soars 69% in another record quarter fueled by AI boom
  - [taiwan] Taiwan Dollar, Won Slump as Chip Stock Selloff Hurts Sentiment
  - [taiwan] TSMC Reiterates 2026 Capex Between US$60B-US$64B
  - [taiwan] TSMC Expects 4Q Revenue Between US$52.3B-US$54.3B
  - [taiwan] TSMC Expects 4Q Gross Margin Between 65%-67%
  - [taiwan] AI Demand Extends TSMC's Record Earnings Streak
  - [taiwan] TSMC profit beats estimates with 69% rise, but stock faces big test
  - [japan] Today's Oha Biz October 15th (Thursday) U.S. Consumer Price Index continues to grow rapidly
  - [japan] Japan August industrial production revised down to -2.4% M/M; core machine orders rise 5.2%
  - [japan] IMF: Japan to fall to 6th in 2027 global GDP rankings
  - [taiwan] TSMC Q3 profit surges more than expected to record high on AI-fueled demand
  - [korea] Asia markets in red: South Korea and Japan lead deep tech selloff; Japan industrial output revised down
  - [taiwan] TSMC Q3 profit jumps 69% to record, beating expectations
  - [japan] U.S. semiconductor company plans to build new factory for up to 3 trillion yen based on Japan-U.S. agreement
  - [taiwan] Lucro da TSMC no terceiro trimestre salta 69%, atingindo um recorde e superando as expectativas

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
      "published_utc": "2026-10-15T08:33:41+00:00",
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

