atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-12T13:03:30.357079+00:00
Total: 2907 manchetes

  🇯🇵 Japão          1107
  🇨🇳 China          810
  🇹🇼 Taiwan         280
  🇰🇷 Coreia do Sul  710

## O que já está no feed (não repita)

  - [korea] ASML to raise prices of chipmaking parts for Samsung, SK Hynix by 10%: report
  - [china] EU eyes December trade initiatives after China car import deal
  - [korea] S.Korean stocks slide as chip selloff deepens, foreign selling persists
  - [taiwan] Taiwan condemns China over sanctions on ministers of diplomatic allies
  - [china] Chinese Policymakers Appear at Ease With Stronger Yuan — Market Talk
  - [taiwan] Hon Hai subsidiary sells stake in Zhen Ding for $3.2bn
  - [china] Leapmotor-Stellantis JV calls EU-China import cap deal 'interesting alternative'
  - [korea] Asia report: Stocks mixed but Seoul suffers steep chip sell-off
  - [china] Micron Stock Falls as China Memory Chip Threat Gets Serious — Barrons.com
  - [korea] Finance minister urges preemptive action for supply chain stability
  - [china] How China and the EU pressed pause on trade war – and what it took to get there
  - [korea] Sandisk, IREN, SK Hynix, Amazon, and More Stocks That Explain Today's Market — Barrons.com
  - [china] EU to Cap Chinese Hybrid-Vehicle Imports at 350,000 Units Annually, Official Says
  - [korea] FX at one-month high led by Indian rupee, Korean won; earnings, IMF in focus
  - [china] Commentary: Europe Can’t Tariff Away Its China Trade Deficit
  - [korea] Bank of Korea Expects 2027 Budget to Have Marginal Impact on Inflation
  - [korea] Suggesting further increase in base interest rate... Shin Hyun-song “Deciding the timing considering prices et
  - [korea] Seoul shares open lower on inflation, Mideast woes
  - [korea] Will the base interest rate be further increased due to rising prices?
  - [japan] Dollar firm near 18-month highs, as Gulf unrest, US inflation keep investors on edge By Reuters
  - [china] China's new car exports increased by 60% in September; high gasoline prices may also boost EV demand
  - [china] China to lower VAT export rebate on new energy vehicles
  - [china] China-EU car deal eases trade tensions for now at least
  - [korea] Exports double in first 10 days of Oct. on chip boom
  - [china] Micron Stock Slips as China Memory Chip Threat Ramps Up — Barrons.com
  - [china] IMF Urges China to Shift Growth Model Toward Consumption, Services
  - [korea] Governor of the Bank of Korea: “Next year’s budget will also stimulate prices”… Interest rate hike hints
  - [korea] Korean budget carriers shift to cargo to ease passenger, fuel pressures amid chip boom
  - [china] Table: Yuan Ding Investment Corp. Sep Rev NT$2.37B Vs NT$1.77B
  - [korea] [2026 National Assembly Audit] Shin Hyun-song “Buying time by preemptively raising interest rates”… Austerity 
  - [china] China’s CXMT makes ‘key progress’ on new chip structure: SCMP
  - [korea] As the won continued to strengthen, foreign currency tech groups, aiming to buy low foreign currency..
  - [korea] The value of the Korean won is on a high march. The won per dollar rose to its highest level in two
  - [korea] The government's tax reform is expected to significantly increase the burden of comprehensive real e..
  - [china] Copper Rises on China Stimulus Hopes, Mining Supply Risks — Market Talk
  - [korea] Governor of the Bank of Korea: “A 0.5% point increase in the base interest rate has the effect of reducing the
  - [taiwan] Taoyuan's Lala Mountain becomes Taiwan's first Urban Night Sky Place
  - [korea] Jungheung Construction Group will donate 10 billion won for the success of the "Honam Semiconductor
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Report on Share Repurchase Results
  - [korea] European Chip Stocks Mixed After Korean Tech Selloff — Market Talk

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
      "published_utc": "2026-10-12T13:03:30+00:00",
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

