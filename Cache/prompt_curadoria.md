atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-01T01:12:42.967890+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1288
  🇨🇳 China          762
  🇹🇼 Taiwan         255
  🇰🇷 Coreia do Sul  695

## O que já está no feed (não repita)

  - [japan] Japan Manufacturing Sector Ebbs In September - S&P Global
  - [japan] Bank of Japan summary affirms priority is avoiding inflation overshoot
  - [taiwan] Key facts: TSMC (2330) $265B U.S. investment; $60–$64B capex outlook; Q3 results Oct. 15
  - [japan] Some say there is no choice but to accelerate interest rate hikes if there are signs of an upward trend in pri
  - [taiwan] Taiwan Manufacturing Expands Most Since 2021
  - [japan] Japan September factory growth slows to 6-month low, PMI shows
  - [taiwan] TSMC evaluates potential Texas investment, sources say
  - [korea] South Korea factory growth hits 4-month high as export orders boom, PMI shows
  - [korea] South Korea Manufacturing Growth Accelerates in September
  - [taiwan] TSMC avalia possível investimento no Texas, segundo fontes
  - [japan] Japan Big Manufacturers More Optimistic Despite Headwinds
  - [japan] Japan Manufacturing Growth at 6-Month Low, Confirmed
  - [japan] [Japanese Market Conditions] Yen falls to 157 yen-lower level following Bank of Japan's ``main opinion'' - bon
  - [japan] [Breaking News] Bank of Japan September Tankan Business Confidence Improving in Large Companies and Manufactur
  - [japan] BREAKING NEWS: Gov't urged BOJ to act proactively vs. excessive market moves: summary
  - [japan] JGBs Fall on Prospects for Quicker Pace of BOJ Rate Hikes — Market Talk
  - [korea] AI Boom Powers South Korea's September Exports Past $120 Billion
  - [korea] South Korea September exports rise 83.5% y/y to monthly record
  - [japan] Japan business mood improves, tankan survey shows
  - [japan] BOJ debated need for more rate hikes at September meeting, summary shows
  - [japan] Bank of Japan Tankan in September improves for 6th consecutive quarter, large companies/manufacturing industry
  - [korea] South Korea exports surge past expectations in Sept, trade surplus grows
  - [japan] [Breaking News] Bank of Japan Tankan: Large corporate manufacturing industry improves for 6th consecutive quar
  - [japan] Bank of Japan September meeting should be managed appropriately to prevent prices from continuing to rise exce
  - [japan] BoJ Tankan: Large Manufacturing Index Improves In Q3
  - [japan] BOJ SEPT TANKAN SMALLER MANUFACTURER SENTIMENT’S LARGER-THAN-EXPECTED RISE DRIVEN BY AUTOS, NON-FERROUS METALS
  - [taiwan] Lip-Bu Tan calls TSMC a partner rather than a rival
  - [korea] South Korea Exports Hit Fresh Record High
  - [taiwan] How a TSMC veteran is steering Singapore's lab-to-fab chip strategy
  - [japan] BOJ SEPT TANKAN: SMALL MFG INDEX 14; JUNE 9; MEDIAN 11
  - [japan] BOJ TANKAN: SMALL NON-MFG INDEX 15; JUNE 15; MEDIAN 16
  - [japan] BOJ TANKAN LARGE NON-MFG INDEX 35; JUNE 37; MEDIAN 37
  - [japan] MNI BOJ SEPT TANKAN LARGE MFG DI 24; JUNE 22; MEDIAN 26
  - [korea] South Korea Posts Record Trade Surplus
  - [japan] BOJ SEPT TANKAN SHOWS LARGE MFG SENTIMENT RISE LED BY OIL/COAL, STEEL, NON-FERROUS, WHILE OFFSET BY FOOD, LUMB
  - [korea] South Korea Import Growth Tops Estimates
  - [japan] BOJ SEPT TANKAN: MAJOR MANUFACTURERS SEE INFLATION AT 2.2% IN 5 YEARS FROM NOW VS. 2.2% FORECAST IN JUNE SURVE
  - [japan] BOJ SEPT TANKAN: MAJOR MANUFACTURERS SEE INFLATION AT 2.3% IN 3 YEARS FROM NOW VS. 2.2% FORECAST IN JUNE SURVE
  - [japan] BOJ SEPT TANKAN: MAJOR MANUFACTURERS SEE INFLATION AT 2.3% A YEAR FROM NOW VS. 2.3% FORECAST IN JUNE SURVEY
  - [japan] BOJ SEPT TANKAN: ALL FIRMS ASSUME FISCAL 2026 USD/JPY FX RATE TO AVERAGE Y154.23 (JUNEY152.57)

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
      "published_utc": "2026-10-01T01:12:43+00:00",
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

