atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-05T12:22:43.044868+00:00
Total: 3000 manchetes

  🇯🇵 Japão          891
  🇨🇳 China          901
  🇹🇼 Taiwan         323
  🇰🇷 Coreia do Sul  885

## O que já está no feed (não repita)

  - [japan] Fiscal System Council: Securing stable financial resources to strengthen defense capabilities
  - [korea] LG Electronics India Enters Automotive Tech, Plans Manufacturing In Andhra
  - [china] China ready to expand US agricultural imports if Board of Trade tariff cuts take effect
  - [japan] Citi sees dollar weakening against yen after U.S. midterms By Investing.com
  - [china] China controls rare earth exports to Japan, yttrium oxide plummets by 98% from January to September
  - [japan] Citi sees dollar weakening against yen after U.S. midterms
  - [china] KMB: China disruption constrained sales as Kenvue integration reshapes the growth outlook
  - [korea] Rupee gains nearly 1% in October, second-best performer in Asia after Korean won
  - [china] Nvidia chips pile up in Hong Kong as China withholds import approval
  - [taiwan] Import price increase in October hits the largest increase in the past 50 years. General Accounting Office: No
  - [taiwan] The central bank adjusted to prevent depreciation and foreign exchange deposits fell by US$4.308 billion at th
  - [china] Sichuan Qiaoyuan Gas Plans To Invest 3.2 Billion Yuan In Project Via New Unit
  - [taiwan] Micron retreats in premarket after suspension of $4.5B Taiwan factory plan
  - [china] SHL: Core growth was strong, while FY27 guidance reflects China, inflation and separation headwinds
  - [korea] KT&G: Compound 2030 pairs global growth with KRW 5tn in regular returns over four years
  - [taiwan] Hot money fled and the New Taiwan dollar nearly broke 33 yuan. Exporters actively sold foreign exchange and re
  - [china] Advanced Micro-Fabrication Equipment Inc China Plans A-Share Worth Buyback
  - [china] China Overseas Land & Investment Logs October Contracted Property Sales RMB 17.805 Billion
  - [japan] The condominium market changes due to the Bank of Japan's interest rate hike; it is the transaction price rang
  - [japan] Toyota Motor: FY operating-income guidance rose to JPY 3.9tn as investment and shareholder returns advanced
  - [taiwan] The New Taiwan Dollar depreciates heavily and the central bank calls out to exporters: Don’t expect excessive 
  - [japan] “A peacetime financial base in preparation for emergencies” Ministry of Finance insists on strengthening defen
  - [japan] Prepare for emergency financial expenditures: Ministry of Finance recommendation to strengthen defense capabil
  - [china] China to keep anti-dumping, anti-subsidy tariffs on US n-Propanol imports for five more years
  - [china] China Import Expo Selling content-related products from Japan
  - [korea] Coway To Acquire Real Estate Worth 365 Billion Won For Establishing New Research And Development Centre
  - [taiwan] Taiwan Semiconductor Price Target Raised to $600.00/Share From $554.00 by Bernstein
  - [china] China to issue yuan-denominated green sovereign bonds in Canada next week
  - [taiwan] Micron suspends work on US$4.5 billion factory in Taiwan, according to Bloomberg News report
  - [china] China's Worsening Economic Outlook May Lead to Aggressive Stimulus Next Year — Market Talk
  - [china] Commentary: After the Midterms, a Case for Realism in U.S.-China Relations
  - [japan] BOJ minutes: Inflation could prompt faster rate hikes
  - [taiwan] Taiwan's chipmakers shine brightest in living memory
  - [taiwan] Taiwan Forex Reserves at 3-Month Low
  - [korea] Real estate directly donated by grandparents to underage grandchildren has reached nearly 1.4 trilli..
  - [china] China Merchants Shekou Industrial Zone October Contract Sales At 18.7 Billion Yuan
  - [china] China's November diesel exports to ease amid thin domestic stocks, sources say
  - [korea] KT&G Posts Record Quarterly Revenue and Operating Profit in Q3, Unveils Four-Year KRW 5 Trillion Shareholder R
  - [korea] [Maeil Business TV] Semiconductors Lift the Won; What Lies Ahead?
  - [china] Table: Chun Yuan Steel Industry 3Q Net Profit NT$484.2M Vs NT$376.8M

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
      "published_utc": "2026-11-05T12:22:43+00:00",
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

