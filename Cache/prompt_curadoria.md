atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-04T07:52:43.788517+00:00
Total: 2906 manchetes

  🇯🇵 Japão          839
  🇨🇳 China          871
  🇹🇼 Taiwan         306
  🇰🇷 Coreia do Sul  890

## O que já está no feed (não repita)

  - [japan] Japan futures fall for 4th session as yen jumps, Tokyo equities drop
  - [japan] TSE continues to fall, selling mainly in semiconductor-related stocks
  - [china] CNOOC Limited Class A Stock 12‑Month Price Target Raised to CNY 44.7, Implies 31% Upside
  - [korea] Imported vehicle sales jump 29.3% in Oct. on strong EV demand
  - [china] China's slumping state airlines pin hopes on overseas demand like exporters
  - [korea] The International Atomic Energy Export Event held at the end of last month was successfully complete..
  - [korea] Democratic gains unlikely to derail Korea-US investment deal
  - [taiwan] Taiwan firm signs MOU with Ukrainian drone company on supply chains
  - [japan] Tokyo Seimitsu: AI-driven semiconductor demand lifted H1 results and prompted higher FY2027 guidance
  - [japan] House of Representatives Finance and Financial Affairs Committee Consumption tax reduction bill Ruling parties
  - [japan] Chiyoda: Golden Pass LNG started production as orders target JPY 300bn and share redemption advances
  - [japan] Mitsubishi raises FY profit forecast, announces 1 trillion yen buyback
  - [japan] Mitsubishi raises FY profit forecast, announces 1 trillion yen buyback By Investing.com
  - [china] Estee Lauder sets growth targets through 2030 amid China recovery
  - [korea] Hugel Inc. Q1-Q3 Sales Rise 15% to KRW 352.1B
  - [china] China’s services PMI misses expectations at 50.8 in October, composite PMI drops to 52.0
  - [china] Concerns about trade imbalance continue, Shanghai International Import Expo will launch "Export to China Repor
  - [taiwan] TSMC scheduled to list NT$14.8 billion green bonds on Nov. 12
  - [japan] Mitsubishi Corporation - To Buy Back Up To About 6% Of Own Shares Worth 1 Trillion Yen
  - [china] Nvidia China clients to get 1% of $70 bln RTX chips ordered- Bloomberg
  - [china] The Estée Lauder Companies Announces Fiscal 2030 Ambition at Its Capital Markets Experience: China Ecosystem I
  - [japan] Franc, Yen Emerge as FX Winners as US Midterms Weaken Dollar
  - [china] Offshore Yuan Remains Under Pressure
  - [japan] Mitsui Chemicals to buy Japan chip material maker JSR for over $8.2bn
  - [japan] Chief Cabinet Secretary: Support for the International Criminal Court (ICC) Considering financial measures, et
  - [japan] Nikkei Drops 4.2% to Five-Month Low, Dragged by Chip Stocks — Market Talk
  - [china] China's yuan hits 2-week low as investors weigh PBOC foreign exchange reserve hike
  - [china] Asian FX gains as dollar falls on U.S. midterm results, yuan weakens on PBOC move
  - [japan] Consumption tax reduction bill Liberal Democratic Party: “Vote on the 6th” Democratic Party: “Decision after l
  - [japan] Consumption tax reduction bill House of Councilors establishes special committee, chaired by Liberal Democrati
  - [china] Nvidia China Clients Expected to Get 1% of $70 Billion in RTX Chip Orders
  - [china] Nvidia China clients to get 1% of $70 billion RTX chips ordered- Bloomberg News
  - [china] China Steps in to Boost Stocks, Cool Off Yuan
  - [japan] Swiss Franc, Yen Jump as US Midterms Push Dollar to Worst Day in a Month
  - [korea] Kospi Slumps as Democrats’ US Election Lead Spurs Chip Selloff
  - [china] Nvidia China Clients to Get 1% of $70 Billion RTX Chips Ordered
  - [japan] Yen Strengthens as US Dollar Weakens
  - [china] The central bank launched a 257.5 billion yuan overnight reverse repurchase operation on November 4, with a ne
  - [korea] BOK Financial raises quarterly dividend by 23.8% to $0.78/share
  - [china] China's PMI Data Show Economic Activity Lost Momentum in Oct — Market Talk

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
      "published_utc": "2026-11-04T07:52:44+00:00",
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

