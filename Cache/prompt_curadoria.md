atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-27T00:22:41.714607+00:00
Total: 3000 manchetes

  🇯🇵 Japão          983
  🇨🇳 China          846
  🇹🇼 Taiwan         375
  🇰🇷 Coreia do Sul  796

## O que já está no feed (não repita)

  - [japan] JAPAN SEPT SERVICES PPI +0.3% M/M: AUG +0.1%
  - [korea] S. Korea's GDP expands 1% in Q3 on strong exports, investment: BOK
  - [japan] MNI: JAPAN SEPT SERVICES PPI +3.7% Y/Y; AUG +3.5%
  - [japan] Japan Services Producer Inflation Highest Since June 2024
  - [japan] Services Producer Price Index (Sept.)
  - [korea] South Korea GDP grows more than expected in Q3 on AI boost
  - [korea] (LEAD) S. Korea's GDP expands 1 pct in Q3 on strong exports, investment: BOK
  - [korea] South Korea Q3 GDP Growth Tops Forecasts
  - [china] Analysis-China’s lab-grown diamond makers target AI, chip sectors for next wave of growth
  - [korea] South Korea's economy grows 1.0% in 3rd quarter on chip boom
  - [korea] South Korea Q3 GDP +1.0% q/q, stronger than expected
  - [korea] South Korea GDP Data Due On Tuesday
  - [korea] Samsung Electronics and SK Hynix, which are set to announce their earnings this week, are expected t..
  - [japan] Preview: Forecasters See Japanese Retail Sales Up Again in September with Boost from Autos, Department Store S
  - [japan] Preview: Forecasters See Japan Industrial Production Lifted Again By AI Buildout in September
  - [japan] Preview: Forecasters See Japan Jobless Rate Flat in September as Employment Remains Buoyant
  - [korea] Samsung's Exynos 2700 outperforms Qualcomm's flagship chip by nearly 20 pc
  - [china] Chinese automakers expand manufacturing in Europe to avoid EU tariffs amid rising domestic competition: Report
  - [japan] [France at a dead end] If spending is suppressed, the people will protest, and if the financial situation wors
  - [china] MBRF meatpacking plant in Promissão has exports suspended by China
  - [china] China halts beef imports from MBRF plant in Brazil
  - [taiwan] AI and oil worries rattle Asian currencies from Taiwan to Philippines
  - [korea] Samsung Electronics Stocks Decline Before 107.4 Trillion Won Profit Test
  - [japan] U.S. IT giant Meta raises up to 15 trillion yen through stock issuance, plans for huge capital investment in A
  - [china] WuXi AppTec Co., Ltd. Class A Stock 12‑Month Price Target Raised to CNY 196.86, Implies 36% Upside
  - [japan] Japan life insurers eye purchases of higher-yielding JGBs
  - [china] MBRF meatpacking plant in Promissão has exports suspended by China, says CNN
  - [china] China halts beef imports from MBRF plant in Brazil, CNN reports
  - [korea] Samsung Life lança emissão de títulos de US$ 1,5 bilhão, segundo mostra a ficha de termos
  - [korea] SK Hynix Q3 earnings on deck: What to expect
  - [japan] Preview: Forecasters See Tokyo CPI Staying Well above BOJ’s 2% Target in October
  - [china] WuXi AppTec Co., Ltd. Class A Stock 12‑Month Price Target Raised to CNY 195.93, Implies 35% Upside
  - [japan] Dollar rebounds as euro slips ahead of key central bank decisions
  - [china] Properties Pass Down China’s Construction Supply Chain in a ‘Debt Relay’
  - [taiwan] Anthropic Highlights Disruptions to TSMC Operations as a Risk
  - [japan] Japan to back perovskite solar cell mass production with $640m in subsidies
  - [china] Shanghai Iluvatar Corex Semiconductor Granted Aggregate Banking Facilities Of Over Rmb12 Billion, As At Oct 26
  - [china] EU Plans to Hit China With More Import Curbs in Early 2027
  - [korea] Micron, SanDisk and SK Hynix Stocks Climb as AI Memory Demand Takes Center Stage
  - [taiwan] Goldman Sachs has revised up its forecast for Taiwan’s GDP growth this year to 11.7% and expects to start an i

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
      "published_utc": "2026-10-27T00:22:41+00:00",
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

