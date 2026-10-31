atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-31T10:32:52.674424+00:00
Total: 3000 manchetes

  🇯🇵 Japão          922
  🇨🇳 China          871
  🇹🇼 Taiwan         353
  🇰🇷 Coreia do Sul  854

## O que já está no feed (não repita)

  - [china] The central bank further optimizes the short-term interest rate control mechanism
  - [korea] Samsung hosts OpenAI’s Altman for talks on AI chips and infrastructure
  - [china] Swiss firms plan to expand China investments as trade deal deepens ties
  - [china] New signal! The central bank’s major adjustments will be implemented from the day after tomorrow——
  - [taiwan] Taiex to face heavy pressure after TSMC's ADRs plunge nearly 6%: Analyst
  - [korea] Siemens CEO outlines path to bring industrial AI to smaller manufacturers
  - [china] The operating interest rate is 1.25%! The anchor change of the policy interest rate will be officially impleme
  - [china] The People's Bank of China switches its policy interest rate and announces the overnight reverse repurchase ra
  - [china] CNOOC Limited Class A Stock 12‑Month Price Target Raised to CNY 42.52, Implies 18% Upside
  - [japan] Will it be a “buyer’s market” in 2-3 years? A former Bank of Japan economist predicts the future of a country 
  - [china] 3 agencies identified for procuring drones said to contain Chinese-made chips
  - [japan] BOJ speeds up ETF sales, potentially boosting funding for Takaichi’s plans By Investing.com
  - [japan] BOJ speeds up ETF sales, potentially boosting funding for Takaichi’s plans
  - [china] China's State Council appoints, removes officials
  - [japan] What was the ``role'' of the Bank of Japan governor during the deflationary recession? Read Haruhiko Kuroda's 
  - [china] The central bank switches its main policy interest rate from 1.4% to 1.25%
  - [japan] Japanese Listed Iole Plans to Sell All 151.21 Bitcoin, Expects 254 Million Yen Loss
  - [japan] BOJ ETF Sales Acceleration Could Support Takaichi’s Spending Agenda
  - [china] China willing to import more German goods, Premier Li says
  - [japan] Mushrooms, the savior of high prices, can be transformed into great things by changing the combination and how
  - [china] China’s October factory activity contracts at fastest pace in 3 months, PMI survey shows
  - [china] China Manufacturing Unexpectedly Weakens
  - [china] China Composite PMI Falls Back into Contraction
  - [japan] The government should carefully judge its declaration of overcoming deflation.
  - [china] Central Bank: Starting from November 2, bidding for overnight reverse repurchase operations will be launched e
  - [china] The policy interest rate "changes the anchor" and the central bank will conduct overnight reverse repurchase o
  - [taiwan] TSIA 30: The manpower problem behind Taiwan's semiconductor resilience
  - [korea] Despite the US freeze, the Bank of Korea 'nods down' on interest rate hike in November... Surprising growth an
  - [taiwan] TSIA 30: AI is breaking the sequential supply chain — Taiwan may be built for what comes next
  - [taiwan] Good Morning World》Taiwan’s export investment exceeded expectations. The economic growth rate in the third qua
  - [china] The central bank officially announced that the policy interest rate has officially "changed the anchor", exper
  - [japan] German Chancellor Merz worries about EV incentives to be considered at EU summit meeting
  - [japan] Tokyo Electron Ltd. Stock 12‑Month Price Target Raised to JPY 16138.18, Implies 61% Upside
  - [korea] Hyundai Motor Company Stock 12‑Month Price Target Cut to KRW 548612.9, Implies 88% Upside
  - [japan] Bank of Japan plans to raise interest rates in December, aims for neutral interest rate as inflation rises (Ji
  - [korea] North Korea says sanctions don't work to deny its status as nuclear weapons state
  - [japan] The Takaichi administration's theory of a ``bad yen depreciation'' due to fiscal expansion is wrong - Why we s
  - [japan] NY foreign exchange market = Yen rises for 3rd day, Bank of Japan leaves interest rates unchanged, emphasizes 
  - [taiwan] Intel on course for worst day ever, triggers global chip rout
  - [japan] Bank of Japan announces “underlying inflation rate” to reach 2%; ability to suppress upward swings in prices a

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
      "published_utc": "2026-10-31T10:32:52+00:00",
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

