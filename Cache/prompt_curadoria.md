atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-02T05:42:46.650144+00:00
Total: 3000 manchetes

  🇯🇵 Japão          930
  🇨🇳 China          863
  🇹🇼 Taiwan         355
  🇰🇷 Coreia do Sul  852

## O que já está no feed (não repita)

  - [japan] It also lost to the Social Democratic Party in terms of approval ratings, and its "former colleagues" dismisse
  - [japan] BOJ locks in December hike, but neutral-rate uncertainty muddies outlook
  - [korea] Tesla, Samsung flag manufacturing risks from Trump's Vietnam tariff push
  - [china] China's Weak Property Sector Remains Key Drag for Factory Activity — Market Talk
  - [korea] Tous les Jours taps US bakery network to boost Korean grape exports
  - [japan] Japan's real interest rates have risen recently, BOJ says
  - [china] Chinese EV Makers Lean on Exports as Home Market Sinks
  - [china] Surging costs and China trade war test US farmers' loyalty to Trump
  - [japan] Nippon Light Metal Holdings Co Ltd Says It Will Buy Back Up To 1.0% Of Own Shares Worth 1.5 Billion Yen
  - [japan] Outlook for Economic Activity and Prices (October 2026, full text)
  - [china] China's Property Sector May See Some Improvement in Next Few Months — Market Talk
  - [japan] Japan chip earnings roundup: AI a double-edged sword
  - [taiwan] Taiwan and Japan eye trade deal akin to Taipei-London pact, sources say
  - [china] Offshore Yuan Rallies to Over 4-Year High
  - [korea] South Korean Won Falls as Overseas Dollar Demand Persists
  - [korea] South Korea's Chip-Led Surplus Set to Drive Further Won Gains — Market Talk
  - [japan] Mabuchi Motor: Sales rose 14.2% as automotive orders, yen depreciation and M&A lifted results
  - [japan] Sources of Changes in Current Account Balances and Market Operations (Oct.)
  - [china] Dollar, low supply and exports to China place cattle in Brazil on the R$400/at route
  - [korea] Bank of Korea probes financial firms’ exposure to crypto risks
  - [taiwan] Lite-On boosts 2027 capex as AI race raises stakes for CSPs
  - [japan] Japan weighs $500 billion defence spending plan, sources say
  - [china] "Anchor replacement" was implemented, and the central bank launched a 541 billion yuan overnight reverse repur
  - [korea] South Korea PMI Shows Faltering Manufacturing Momentum — Market Talk
  - [japan] October 2026 Bank of Japan Policy Meeting Review - Summary of this meeting and future market outlook [Sumitomo
  - [china] China's Manufacturing Activity Faces Risk From Slow Fiscal Spending — Market Talk
  - [japan] Flat 35 Interest rate 3.81%, second highest ever
  - [china] Yuan hovers near 4-year high as US midterms, Chinese regulator meeting in focus
  - [china] Asian currencies mixed as yuan holds near four-year high, dollar steadies
  - [china] China’s shift to new policy rate signals easier funding conditions
  - [korea] South Korea’s manufacturing PMI slows to 8-month low in October
  - [china] China Longyuan Tariff Outlook Expected to Improve in 2027 — Market Talk
  - [japan] BREAKING NEWS: JAL's April-Sept. net profit drops 42.2% to 39.07 billion yen
  - [japan] Japan manufacturing PMI slows to seven-month low in October By Investing.com
  - [japan] Japan manufacturing PMI slows to seven-month low in October
  - [taiwan] Taiwan PMI Shows Goods Producers' Supply-Chain Struggles — Market Talk
  - [china] China Longyuan Power Target Price Cut to HK$6.70 From HK$7.00 by Deutsche Bank >0916.HK
  - [japan] Yen Weakens Despite Verbal Warning
  - [japan] Is “Japan’s bankruptcy due to long-term interest rates” a lie? Yoichi Takahashi reveals misconceptions about “
  - [japan] Japan Manufacturing PMI Signals Decent Growth, Continued Cost Pressure — Market Talk

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
      "published_utc": "2026-11-02T05:42:46+00:00",
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

