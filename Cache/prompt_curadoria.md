atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-13T01:22:43.516597+00:00
Total: 2932 manchetes

  🇯🇵 Japão          1121
  🇨🇳 China          812
  🇹🇼 Taiwan         288
  🇰🇷 Coreia do Sul  711

## O que já está no feed (não repita)

  - [japan] Japan’s wholesale inflation remains elevated, keeps alive BOJ rate-hike view
  - [korea] Seoul shares open sharply lower on U.S. losses, inflation concerns
  - [korea] (LEAD) Seoul shares open sharply lower on U.S. losses, inflation concerns
  - [taiwan] Podcast highlights: Is Elon Musk using TSMC talks as leverage against Intel and Samsung?
  - [japan] Japan PPI unexpectedly eases in Sept on stronger yen, cooling oil By Investing.com
  - [japan] JAPAN SEPT CORP GOODS PRICE INDEX -0.3% M/M; AUG -0.3%
  - [japan] September corporate price index increased by 6.8% compared to the same month last year
  - [japan] JAPAN SEPT CGPI IMPORT INDEX +24.5% Y/Y IN YEN TERMS FOR 10TH STRAIGHT RISE VS. AUG REVISED UP TO +25.1% FROM+
  - [japan] September corporate price index rose 6.8% to 135.7...Bank of Japan announced (Yomiuri Shimbun Online)
  - [japan] Japan PPI unexpectedly eases in Sept on stronger yen, cooling oil
  - [japan] JAPAN SEPT CGPI: KEY ENERGY PRICES; CRUDE OIL/COAL PRODUCTS +11.5% Y/Y VS. AUG +14.7%
  - [japan] Domestic corporate goods prices rose 6.8% year-on-year in September, growth rate slowed from the previous mont
  - [taiwan] Geothermal power too costly for chipmakers? Taiwan's semiconductor industry sees value beyond electricity pric
  - [korea] (URGENT) Seoul shares open sharply lower on U.S. losses, inflation concerns
  - [japan] Corporate prices rise 6.8% in September Bank of Japan (Jiji Press)
  - [japan] Japan Producer Prices Rise the Least in 4 Months
  - [japan] JAPAN SEPT PRODUCER PRICES -0.3% M/M (AUG REVISED TO -0.3% FROM -0.2%); 2ND STRAIGHT DROP; MEDIAN FORECAST +0.
  - [japan] Corporate Goods Price Index (Sept.)
  - [japan] Japan finance minister named as next chair of World Bank-IMF joint development committee
  - [china] Exclusive | China finance minister to deliver opening speech at Apec meeting in Hong Kong
  - [korea] The Bank of Korea repeatedly hinted at the possibility of further interest rate hikes... Market outlook “withi
  - [taiwan] Weekly Recap: Moody's affirms A2, outlook positive and TSMC tie-up boosts chips
  - [japan] Weekly Recap: TSE:8604 Macquarie-unit buy and JGB global marketing
  - [korea] Concerns are growing that the impact of a rate hike could have a greater impact on the elderly in th..
  - [japan] [Direct hit] “The era of reflationary policy is over” The core of Sanaenomics as told by Minister of Economy a
  - [korea] “We bought time by raising it before the US”... Bank of Korea plans to freeze base interest rate in October
  - [korea] Onto Innovation wins SK hynix award for HBM defect technology
  - [japan] FX weekly: Greenback climbs, Yen slides for fourth consecutive week
  - [china] Dow Rises 200 Points, Nasdaq Wavers: China Chip Competition Hits Tech Stocks, Oil Climbs
  - [china] China to Cut Export Tax Rebate for New-Energy Vehicles
  - [taiwan] Interview: Microsoft's Maia GM on Maia 300, Taiwan and HBM supply
  - [korea] Seoul shares plunge over 3 pct on tech sell-off amid Mideast, inflation woes
  - [china] Micron Stock Falls on China Chip Threat
  - [japan] Finance Minister Katayama becomes the next chairman of the World Bank/IMF Joint Development Committee Prime Mi
  - [china] EU limits Chinese hybrid shipments at 350,000 annually
  - [korea] S.Korean stocks slide as chip selloff deepens, foreign selling persists
  - [china] EU Aims to Put Brakes on Chinese Hybrid-Vehicle Market Share With Import Cap — Update
  - [japan] Japanese Yen Could Trade Sideways Vs Dollar in Near-Term — Market Talk
  - [china] Copper climbs on China stimulus hopes, Chile mine supply risks
  - [china] BYD sees tariff pressure linked to EU-China deal as short term

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
      "published_utc": "2026-10-13T01:22:43+00:00",
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

