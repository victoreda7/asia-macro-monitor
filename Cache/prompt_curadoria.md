atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-26T20:52:41.992614+00:00
Total: 3000 manchetes

  🇯🇵 Japão          925
  🇨🇳 China          978
  🇹🇼 Taiwan         338
  🇰🇷 Coreia do Sul  759

## O que já está no feed (não repita)

  - [china] 800 billion MLF + 500 billion reverse repurchase, the central bank's "combination punch" accurately protects l
  - [china] Trump-Xi summits unlikely to solve China's rare-earth licensing maze
  - [japan] Condominium prices continue to decline...still clear evidence that the "real estate bubble" is not over | Life
  - [taiwan] Taiwan Semiconductor Stocks Slip 1.96% as Taiwan's Market Sinks 4.8% in Chip Rout
  - [korea] White House's Coupang broadside alarms Seoul as US weighs 25% tariffs
  - [china] Nissan poised to import cars from China to Japan for first time
  - [china] China Rejects U.S. Proposal for Additional 20% Tariff
  - [korea] Nvidia, Kioxia team on AI server memory as alternative to South Korean chips
  - [japan] Japan Data Preview: Forecasters See Stable Jobless Rate in October Report as Job Market Holds Firm
  - [japan] Japan Data Preview: Solid Department Store Sales to Propel Retail Sales in October Report
  - [japan] Japan Data Forecast: Exports, AI Buildout to Lift Industrial Output in October Report
  - [china] Chip Sellers Have Told Neoclouds They Won’t Supply Nvidia Chips If Any Of The Computing Capacity Will Be Rente
  - [korea] Bank of Korea raises base interest rate to 3.25%... Third time in the second half of the year
  - [japan] Japanese Yen Lifted by Safe-Haven Demand — Market Talk
  - [japan] Japan-Marshal summit meeting confirms expansion of cooperation in security field, etc.
  - [japan] BOJ policymaker calls for faster rate hikes | NHK WORLD-JAPAN News
  - [taiwan] What to know about the latest U.S. tariff proposals for Taiwan
  - [china] China’s low interest rate comes with high stakes
  - [china] Bayer to Invest Up to $549 Million in China Drug Manufacturing Site
  - [china] The central bank's reverse repurchase operation net withdrawn 45.5 billion! Dividend low-volatility ETF Huatai
  - [japan] Personal information of 3.11 million people leaked due to unauthorized access to Mitsui Fudosan app
  - [china] Barclays downgrades European forklift makers as Chinese imports jump 51% in Q3
  - [japan] BOJ policymaker calls for faster rate hikes
  - [japan] Yomiuri: Toyota to Sell U.S.-Built Camry in Japan to Ease Trade Tensions
  - [japan] Bank of Japan Councilor Tamura: ``Toward a neutral level'' Appeals for the need for additional interest rate h
  - [china] Why Russia’s farm exports to China are booming despite US trade thaw
  - [japan] Bank of Japan council members are positive about raising interest rates (ABEMA TIMES)
  - [korea] The Bank of Korea raises the base interest rate to 3.25%... Third raise this year
  - [korea] The Bank of Korea raises its base interest rate and significantly raises its growth forecast. “Focus on price 
  - [korea] Bank of Korea raises base interest rate by 0.25% to 3.25%
  - [japan] Bank of Japan Councilor Tamura: ``There are cases where a judgment on the financial environment can be made in
  - [japan] Candriam Stays Long Yen, Returns to Neutral in Euro — Market Talk
  - [china] Could EU delisting of Chinese firm pave way for wider sanctions relief?
  - [china] China shares steady as markets seek to overcome tariff pessimism
  - [korea] SK Hynix seeks TSMC 3nm expertise as Micron steps up hiring
  - [japan] Bank of Japan, unrealized ETF gain of 76 trillion yen, record high, September interim results (Kyodo News)
  - [china] DPC Dash - Domino's Pizza China Scales Supply Chain Network to Drive Disciplined Store Expansion and Nationwid
  - [korea] There are concerns about a contraction in real estate market transactions due to the Bank of Korea’s interest 
  - [korea] Huawei eyes AI memory market dominated by Samsung, SK Hynix, Micron - report
  - [korea] Huawei eyes AI memory market dominated by Samsung, SK Hynix, Micron

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
      "published_utc": "2026-11-26T20:52:42+00:00",
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

