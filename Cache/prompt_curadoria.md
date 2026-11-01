atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-01T03:42:43.575419+00:00
Total: 3000 manchetes

  🇯🇵 Japão          926
  🇨🇳 China          864
  🇹🇼 Taiwan         357
  🇰🇷 Coreia do Sul  853

## O que já está no feed (não repita)

  - [taiwan] AI inflation sweeps through the mobile phone market. Industry players: Price pressure may persist until 2028
  - [japan] Semiconductor TSMC's sales exceed the upper limit of expectations, with double-digit sales growth for the Octo
  - [korea] SK hynix hosts first Partners Day in Japan to strengthen chip supply chain
  - [korea] South Korea Exports Extend Robust Growth on AI-Fueled Chip Boom
  - [korea] South Korea exports surge 93.7% in October, fastest growth since 1974
  - [japan] Policies that the government should focus on: ``Price control measures'', the most popular policy for the four
  - [korea] South Korea exports nearly double in October on AI investment boom
  - [taiwan] Lifting Her Dreams: Bunun Teenager Wu Yu-Syuan Journey from Taoyuan
  - [korea] S. Korea's monthly exports hit $115.3b in Oct. on strong chip sales
  - [korea] South Korea's Chip-Led Exports Accelerate, Bringing $1 Trln Annual Target Closer — WSJ
  - [korea] (LEAD) S. Korea's monthly exports hit US$115.3 bln in Oct. on strong chip sales
  - [korea] South Korea exports nearly double in October, strongest growth since 1974
  - [korea] South Korea Import Growth Below Forecasts
  - [korea] South Korea Exports Exports Hit New High in October
  - [korea] South Korea Trade Surplus Beats Estimates
  - [japan] Large-scale easing, "miscalculation" and "hardship" 2% inflation, reached after 14 years, Bank of Japan contin
  - [japan] [Key points explained] Reading Bank of Japan Governor Ueda's press conference & economists' predictions for in
  - [japan] "A dream town filled with children raising children" → "A town with an aging rate of 45% in 40 years"... Proba
  - [japan] A "town where 20,000 people can live" was built on the steep slope of a mountain at a cost of 23 billion yen..
  - [japan] Yen bond offerings hit record $16bn as AI funding race reaches Japan
  - [japan] Indo-Pacific Quad ministers work on supply chains, denounce arbitrary export restrictions
  - [china] Quad not ‘anti-China’, says Rubio as first summit in two years set before Trump-Xi talks
  - [japan] Japan weighs taxing real estate rental operators living overseas
  - [taiwan] Sunset Wins Golden Sound Award for Best Album, Drifting Exit and Takes Back the Band Award | Entertainment
  - [china] The central bank further optimizes the short-term interest rate control mechanism
  - [japan] BOJ sees 2% inflation target generally hit, holds policy rate steady
  - [korea] Samsung hosts OpenAI’s Altman for talks on AI chips and infrastructure
  - [china] Swiss firms plan to expand China investments as trade deal deepens ties
  - [china] The People's Bank of China switches its policy interest rate and announces the overnight reverse repurchase ra
  - [china] New signal! The central bank’s major adjustments will be implemented from the day after tomorrow——
  - [korea] "Samsung Electronics!" "Tesla!" "Monthly rent!"Maekyung Children's Economy Class held at COEX Magok
  - [taiwan] Taiex to face heavy pressure after TSMC's ADRs plunge nearly 6%: Analyst
  - [korea] Siemens CEO outlines path to bring industrial AI to smaller manufacturers
  - [china] The operating interest rate is 1.25%! The anchor change of the policy interest rate will be officially impleme
  - [china] CNOOC Limited Class A Stock 12‑Month Price Target Raised to CNY 42.52, Implies 18% Upside
  - [japan] Will it be a “buyer’s market” in 2-3 years? A former Bank of Japan economist predicts the future of a country 
  - [korea] OpenAI’s Altman Meets Samsung Executives as Chip Crunch Deepens
  - [china] 3 agencies identified for procuring drones said to contain Chinese-made chips
  - [japan] BOJ speeds up ETF sales, potentially boosting funding for Takaichi’s plans By Investing.com
  - [japan] BOJ speeds up ETF sales, potentially boosting funding for Takaichi’s plans

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
      "published_utc": "2026-11-01T03:42:43+00:00",
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

