atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-18T05:32:43.039416+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1053
  🇨🇳 China          876
  🇹🇼 Taiwan         341
  🇰🇷 Coreia do Sul  730

## O que já está no feed (não repita)

  - [korea] Samsung invests $22.8m in Texas workforce as TSMC eyes entry
  - [china] China's September refined fuel exports surge amid Iran war, diesel exports more than triple
  - [korea] The Monetary Policy Committee has raised the base interest rate in succession, with a freeze expected this mon
  - [china] China's September grain, sugar and pork imports
  - [japan] Ruling and opposition party leaders discuss consumption tax reduction bill NHK Sunday debate
  - [korea] What To Expect From BOK Financial’s (BOKF) Q3 Earnings
  - [korea] [Preview] Bank of Korea freezes this month... November's raise card remains
  - [china] China's CXMT pushes into next-gen DRAM, but can it compete on cost?
  - [korea] The base interest rate has been raised repeatedly... A decision by the Monetary Policy Committee is expected t
  - [korea] Analysts forecast BOK to hold benchmark rate unchanged at upcoming meeting: poll
  - [korea] "We will expand the export volume of Jeju Samdasoo to 100,000 tons within three years."Kim Do-young
  - [korea] [This week's economy] Will the Bank of Korea continue to raise its base interest rate? Pay attention to produc
  - [japan] The US budget deficit approaches $2 trillion...the largest since the coronavirus pandemic (JoongAng Ilbo Japan
  - [korea] As the NPU market, a low-power artificial intelligence (AI) semiconductor, grows, leading Korean con..
  - [korea] [Base interest rate decision] “Should I raise it three times in a row or hide?”… The Bank of Korea determines 
  - [korea] The base interest rate has been raised continuously, will it take a break this time? October Monetary Policy C
  - [china] In 2027, China's economy will be in a state of "4% growth and defense"...US City predicts, headwinds of export
  - [korea] The Bank of Korea has repeatedly raised interest rates... The outlook for this week's Monetary Policy Committe
  - [korea] Will the Bank of Korea be open to raising interest rates? Treasury bond rebound alert
  - [korea] “In October and November” … Experts predict interest rate hike to 'hide and hold'
  - [japan] Japan to prohibit untraced gold exports, clamping down on tax evasion
  - [taiwan] Exclusive: EnterpriseSG positions Singapore's semiconductor SMEs for bigger roles in global chip supply chains
  - [taiwan] Mortgage numbers for seniors surge to historic peak
  - [taiwan] Notable tech headlines for the week: CoreWeave, TSMC, Anthropic in focus
  - [china] China central bank chief supports closer IMF surveillance of fiscal, spillover risks
  - [taiwan] Fees proposed for new Qilai Mountain Cabin, Paiyun Lodge rate hike
  - [japan] The Bank of Japan's Kochi branch maintained its judgment from the previous month that the prefecture's economy
  - [taiwan] TSMC’s 3nm Kumamoto plan wins Japan’s approval, qualifying for up to $4.1 billion in aid
  - [japan] Liberal Democratic Party Policy Research Chairman Kobayashi urges many opposition parties to pass consumption 
  - [japan] What’s the likelihood of Yen carry trade reversing? By Investing.com
  - [japan] What’s the likelihood of Yen carry trade reversing?
  - [japan] IMF senior official evaluation: Japan's consumption tax reduction bill
  - [japan] What you can do now about rising mortgage rates
  - [japan] BOJ may need to tighten faster if inflation beats forecast, IMF says
  - [korea] SK hynix Inc. Stock 12‑Month Price Target Cut to KRW 3243355.6, Implies 155% Upside
  - [japan] BREAKING NEWS: Economic, fiscal policy minister Kiuchi visits war-linked Yasukuni shrine
  - [korea] Trump touts Hyundai's US$560-mln Georgia investment pledge at campaign rally
  - [china] Philippines’ ‘China-free’ manufacturing strategy is a high-risk bet
  - [china] Opinion | Philippines’ ‘China-free’ manufacturing strategy is a high-risk bet
  - [china] Europe-China Trade Truce Helps Auto Makers — Barron's

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
      "published_utc": "2026-10-18T05:32:43+00:00",
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

