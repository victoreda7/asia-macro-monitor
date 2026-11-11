atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-11T22:52:46.566621+00:00
Total: 3000 manchetes

  🇯🇵 Japão          930
  🇨🇳 China          894
  🇹🇼 Taiwan         309
  🇰🇷 Coreia do Sul  867

## O que já está no feed (não repita)

  - [japan] Japan Producer Price Data Due On Thursday
  - [japan] Nissan Motor Co., Ltd. Stock 12‑Month Price Target Cut to JPY 370.31, Implies 31% Upside
  - [korea] NC: Three growth pillars lifted Q3 results and underpin 2027 revenue guidance of KRW 3.2t–3.4t
  - [japan] Consumption tax reduction bill begins deliberation in the House of Councilors and will be questioned by a spec
  - [china] Lutnick stalled Trump crackdown on diversion of Nvidia chips to China, Axios reports
  - [japan] Worst ranking of credit unions and credit unions in terms of net profit...While they continue to post deficits
  - [japan] Risks posed by Russia's takeover of JT: "Are foreign assets safe?"... Huge foreign net worth = yen appreciatio
  - [china] Como o presidente-executivo da Nvidia, Jensen Huang, se viu envolvido em um escândalo envolvendo chips e espio
  - [china] US container imports set all-time volume record in October as Chinese imports spike, Descartes says
  - [japan] Nissan Motor Co., Ltd. Stock 12‑Month Price Target Cut to JPY 373.44, Implies 32% Upside
  - [korea] SK hynix Stocks Climb 5.36% as Foreign Investors Pile Back Into AI Memory
  - [korea] NC: Three growth pillars lifted Q3 operating profit and 2026 revenue expectations to ~KRW 2.8T
  - [taiwan] TSMC Stocks Climb 3.37% After Record NT$586.9 Billion October Revenue
  - [japan] Nissan Motor Co., Ltd. Stock 12‑Month Price Target Cut to JPY 377.81, Implies 34% Upside
  - [japan] Odisha, Japan's Tottori Prefecture sign agreement to boost investment, startups and overseas employment
  - [china] China's central bank vows to step up counter-cyclical adjustment, boost domestic demand
  - [china] Chinese university on US blacklist bought Nvidia H200 AI chips: report
  - [china] Amended: China Consumer Prices Flat In October
  - [japan] BofA: Retail yen selling rises but offset by foreign inflows
  - [china] Commentary: China’s AI Export Boom May Reach Beyond Chips
  - [japan] Food consumption tax reduction bill enters deliberation in the House of Councilors, ruling party is in minorit
  - [china] Lots of money, lots of discussion | The foreign exchange deposit reserve ratio is raised, why does the central
  - [china] Military-linked Chinese university bought Nvidia H200 chips despite US blacklist, records show
  - [korea] AI hard to value, interest rates moderate by historical standards: Howard Marks
  - [taiwan] Taiwan's Jan.-Sept. regular wage growth hits 2nd highest in 26 years: DGBAS
  - [japan] Asia report: AI and chip stocks provide a boost in Tokyo, Seoul, Taipei
  - [japan] Japan advisers urge focus on sustaining growth after inflation hits BOJ goal
  - [japan] Yen Slumps as Fed Rate-Hike Bets Boost Dollar — Update
  - [china] China’s central bank vows to step up policy support for the economy
  - [japan] Food Tax Cut Bill Faces Upper House Debate
  - [japan] Citi sees yen strengthening risk if Japanese stocks correct further By Investing.com
  - [japan] Citi sees yen strengthening risk if Japanese stocks correct further
  - [japan] Prime Minister Takaichi "Strengthens growth potential through highly predictable fiscal management" Collaborat
  - [japan] Yen Could Turn Stronger Over Medium Term — Market Talk
  - [japan] Japan automakers post strong sales on weaker yen | NHK WORLD-JAPAN News
  - [japan] Dollar holds gains as Fed hike bets rise after hot U.S. CPI; yen near 6-wk low
  - [japan] SoftBank Group Corp. Stock 12‑Month Price Target Cut to JPY 8611.49, Implies 122% Upside
  - [japan] [Strategic way to buy government bonds, a powerful asset in an era of interest rates] No loss of principal! Th
  - [china] China says offshore trust tax declarations top 160 billion yuan
  - [china] China to issue US dollar-denominated sovereign bonds in Hong Kong next week

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
      "published_utc": "2026-11-11T22:52:46+00:00",
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

