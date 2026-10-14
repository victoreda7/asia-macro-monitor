atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-14T16:42:42.564183+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1132
  🇨🇳 China          849
  🇹🇼 Taiwan         290
  🇰🇷 Coreia do Sul  729

## O que já está no feed (não repita)

  - [china] Micron Takes Another Hit as China Chip Fears Flare
  - [korea] Seoul shares fall for 6th day on renewed AI concerns ahead of US inflation data
  - [china] Commentary: Why Gradual Yuan Appreciation Remains the Baseline
  - [japan] US consumer prices rise 3.7% in September; expectations for early interest rate hike rise somewhat
  - [japan] US Consumer Price Index rises 3.7%; growth rate expands for the first time in 4 months; yen weakens due to exp
  - [korea] Korea's GDP per capita to top $40,000 this year, IMF says
  - [china] IMF calls for US to cut deficits amid bond woes, urges China to shift away from exports
  - [china] On October 15, 2026, the central bank increased the amount of 6-month buyout reverse repurchase with an additi
  - [china] Central Bank, latest release! The increase in social financing in the first three quarters exceeded 27 trillio
  - [japan] GlobalFoundries to Build 2 Chip Plants With $21 Billion Backing Under U.S.-Japan Deal — Update
  - [japan] GlobalFoundries to Build 2 Chip Plants With $21B Backing Under U.S.-Japan Deal — Update
  - [japan] GlobalFoundries to Build 2 Chip Fabs in NY With Up to $21 Billion in Funding From U.S.-Japan Initiative
  - [japan] GlobalFoundries to Build 2 Chip Fabs in NY With Up to $21B in Funding From U.S.-Japan Initiative
  - [japan] GlobalFoundries stock rises on U.S.-Japan semiconductor deal By Investing.com
  - [japan] Possibility of Bank of Japan interest rate hike exceeding 2%
  - [china] French cosmetics facing delays clearing China customs, says industry association
  - [taiwan] Belize PM vows stronger support for Taiwan after China sanctions
  - [japan] Japan to invest up to $21 billion in two US chip factories to be run by GlobalFoundries
  - [japan] GlobalFoundries selected to operate two new semiconductor fabs in New York under landmark U.S.-Japan initiativ
  - [taiwan] Musk's Terafab plan poses no short-term threat to TSMC: Analyst
  - [china] The central bank will launch a 700 billion yuan buyout reverse repurchase operation
  - [china] China Inflation Rises Marginally; PPI Inflation Strongest Since 2022
  - [japan] Yomiuri: Japan Publishes English-Language Booklet on PM Takaichi's Economic Policies
  - [japan] Euro/yen shorts on Japan investors' OAT sales overdone, say UBS
  - [china] MAC accuses Beijing of election interference over Puma Shen family firm sanctions
  - [taiwan] What analysts are watching with key semiconductor maker TSMC set to report results
  - [china] India’s Russian crude imports fall 29% from July peak as China boosts buying
  - [taiwan] Lai calls for progress on unsigned Taiwan-Canada trade framework
  - [china] China buys 8-10 cargoes of US soybeans after Trump-Xi summit: sources
  - [korea] BOK chief meets Chinese, Japanese counterparts in Bangkok for economic talks
  - [china] China's soybean imports fall 7.7% in September compared to the previous year
  - [china] The Fifteenth Tripartite Governors' Meeting among PBOC, BOJ, and BOK
  - [japan] The Bank of Japan's interest rate hike is ``0.5%,'' but the online bank is raising it ``0.6%!'' My husband get
  - [china] Central Bank, latest release! In the first three quarters, the increase in social financing exceeded 27 trilli
  - [china] EU to Lift Sanction on Chinese Firm to Save an ASML Supplier
  - [china] Commentary: Why Consumption Stimulus Won’t Close China’s Demand Gap
  - [china] IMF calls for deficit reduction in the US and for China to reduce dependence on exports
  - [china] China resumes U.S. soybean buying with 8-10 cargoes after Trump-Xi summit - report
  - [china] The central bank is about to launch a 700 billion yuan buyout reverse repo
  - [japan] [Win against inflation! Fun shareholder benefits] My head is full of benefits! Investor Akiyo Fujii / Benefits

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
      "published_utc": "2026-10-14T16:42:42+00:00",
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

