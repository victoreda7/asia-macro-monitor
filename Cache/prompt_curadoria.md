atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-13T07:32:45.602102+00:00
Total: 2999 manchetes

  🇯🇵 Japão          1134
  🇨🇳 China          833
  🇹🇼 Taiwan         298
  🇰🇷 Coreia do Sul  734

## O que já está no feed (não repita)

  - [taiwan] TSMC, Intel supplier Qnity bets on local production to win business
  - [korea] South Korea's Kospi Slumps on Selloff in Chip Stocks — Update
  - [korea] Foreign selloff sends Kospi down 5.5% as chip giants tumble
  - [china] China’s exports seen growing at faster pace in September: Reuters Poll
  - [korea] Seoul shares dip over 5% on tech sell-off on renewed AI, inflation woes
  - [korea] South Korea shares tumble in chip selloff
  - [china] Key facts: NASDAQ:NVDA -1.6% on Microsoft Maia; China GPUs -44%; TSMC
  - [korea] (LEAD) Seoul shares dip over 5 pct on tech sell-off on renewed AI, inflation woes
  - [korea] Bae Jun-young: “Bonk Governor needs to ‘reexamine the starting point’ of raising base interest rate this month
  - [china] Asia stocks slide as chip rout deepens, Chinese automakers hit by EU trade curbs
  - [japan] Dollar Likely to Trade in 157.50-159.30 Yen Range This Week — Market Talk
  - [korea] Kospi Falls for Fifth Consecutive Session on Chip Selloff
  - [china] Why are Chinese car exports soaring? Europe is responding
  - [korea] Korean Chip Stocks' Retreat Partly Reflect Skepticism About Earnings Sustainability — Market Talk
  - [china] Tencent prepares $4.5B+ dollar and yuan bond offering for AI capex
  - [korea] Korea launches chip policy office to fast-track W800tr investments
  - [china] Nvidia AI chip share in China falls as Huawei catches up- Reuters
  - [korea] SK Hynix in extreme oversold freefall near KRW 1,439,000: Live
  - [japan] 88.6% of Japan households expect prices to rise a year from now, BOJ says By Reuters
  - [japan] Asian brands tighten grip on Tokyo's high-end shopping districts
  - [japan] 86.5% of households expect prices to rise five years from now; prices continue to rise and remain at high leve
  - [japan] 86.5% of households expect prices to rise five years from now, the highest level in nine years as prices rise 
  - [japan] It is now important to keep the underlying price level stable at around 2% - Bank of Japan Governor (Reuters)
  - [japan] Gold rebounds as dollar retreats, Middle East tensions sustain inflation concerns
  - [korea] SoftBank, SK Hynix lead Asian tech sell-off amid AI investment concerns
  - [china] China blue chips fall to 14-month low on tech selloff
  - [japan] BOJ Governor Ueda says important to anchor inflation around 2% now
  - [japan] 88.6% of Japan households expect prices to rise a year from now, BOJ says
  - [japan] Japan's producer price inflation slows to 6.8% in September, below market expectations
  - [taiwan] TSMC's Third-Quarter Net Profit Likely Jumped 62% as Revenue Tops Guidance — Earnings Preview
  - [china] China to Cut New Energy Vehicle Export Tax Rebate to 9% From April 2027
  - [taiwan] Taiwan Finance Minister to attend APEC meeting in Hong Kong next week (Reuters)
  - [china] Asian tech shares plunge after Chinese chipmaker reports key advance
  - [china] Xpeng Vice Chairman Welcomes EU-China Hybrid Import Cap Deal
  - [korea] South Korea's Kospi Slumps on Selloff in Chip Stocks
  - [taiwan] IMF sharply raises Taiwan's 2026 GDP growth forecast to 10.7%
  - [china] Yuan holds firm near 2023 highs despite dollar strength
  - [taiwan] TSMC Revenue Growth Upgrade a 'Live Possibility' — Market Talk
  - [taiwan] Taiwan finance minister to attend APEC meeting in Hong Kong
  - [taiwan] TSMC, ASML earnings on tap: Bull and bear cases for tech outlined

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
      "published_utc": "2026-10-13T07:32:45+00:00",
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

