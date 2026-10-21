atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-21T07:52:44.658856+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1034
  🇨🇳 China          871
  🇹🇼 Taiwan         351
  🇰🇷 Coreia do Sul  744

## O que já está no feed (não repita)

  - [japan] BREAKING NEWS: Foreign spending in Japan hits record 7 tril. yen in Jan.-Sept.
  - [japan] Japan futures slip as yen jumps, cost support seen easing
  - [japan] The Takaichi administration should present a "Plan B" for fiscal policy...A plan that says "achieving high gro
  - [korea] Samsung Biologics Co., Ltd. Q3 Rev KRW 1.49T; Lifts 2026 Growth Guide to 20%
  - [korea] South Korean shares post biggest gain in 6 weeks as chipmakers rebound
  - [japan] Will the Bank of Japan decide to reach the 2% price level? (NRI researcher's commentary on current events)
  - [korea] Ryukil C&S To Acquire Real Estate Worth 25 Billion Won
  - [korea] Kospi Regains Ground as Chip Stocks Recoup Most of Prior Session's Losses
  - [japan] Don't you feel safe even if you keep the approval rating at 50%? Yokohama, Chiyoda... The footsteps of "distur
  - [japan] One year since the Takauchi Cabinet was established, it is putting all its effort into enacting the consumptio
  - [korea] Nomura, JPMorgan bullish on Korean chips despite Kospi swings
  - [china] America, China Remain 'Fundamental' for European Spirits, Despite Tariff Turmoil — Interview
  - [korea] Samsung, SK Hynix upgrade China plants to make advanced memory chips - Reuters
  - [korea] Exclusive-Samsung, SK Hynix upgrading China plants to make more advanced chips, people say
  - [japan] Achieving the price target through appropriate monetary policy and contributing to sustainable growth - Bank o
  - [china] From now on, the central bank continues to "strengthen"
  - [korea] Capybobo: PYBOBO begins KRW trading on Bithumb - 21 Oct 2026
  - [japan] BOJ’s Himino signals readiness to raise borrowing costs
  - [japan] Japan’s trade gap widens despite 13-month export growth streak
  - [japan] Japan to consider fuel subsidies during winter, Kyodo reports
  - [japan] Bank of Japan decides to reach 2% price increase rate at October meeting, will it take 14 years to reach 2% (K
  - [japan] Japan's financial conditions loose even after rate hike, BOJ's Himino says
  - [japan] Meiji Yasuda may buy as much as 1 trillion yen worth of yen bonds this year
  - [korea] SK hynix Inc. Stock 12‑Month Price Target Cut to KRW 3203919.5, Implies 162% Upside
  - [japan] BREAKING NEWS: BOJ to decide in next meeting whether 2% inflation rate reached
  - [taiwan] TSMC Pauses Some Taiwan Construction After Mishap Kills Four
  - [korea] Korea's Core Inflation Acceleration Unlikely to Prompt Aggressive Rate Hike — Market Talk
  - [japan] Bank of Japan decides to reach 2% price level (Kyodo News)
  - [korea] Why is SK Hynix stock surging today?
  - [japan] Yomiuri: Japan's Carbon Fiber Manufacturers Expand to Robotaxis, Space
  - [japan] Asia stocks rebound as SpaceX, Super Micro results lift chipmakers
  - [taiwan] TSMC and others turn LCD plants into AI assets as LG Innotek weighs acquisition
  - [china] Trump Open to Summit With Xi and Putin in China to Discuss Ukraine
  - [korea] Samsung, SK Hynix Shares Soar 7%: Korea Chip Recovery Driven by 222% Surprise
  - [japan] Finance Minister Katayama: “The consumption tax cut is a measure against high prices that will allow you to fe
  - [korea] Axcelis plans US$35 million semiconductor facility in South Korea
  - [korea] South Korea to ease fuel supply rules, let refiners boost exports, Lee says
  - [taiwan] Micron faces potential Taiwan strike, union cites Samsung, SK Hynix profit-sharing benchmark
  - [japan] Stock prices rise due to fall in crude oil futures prices
  - [korea] Why is Samsung Electronics stock surging today?

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
      "published_utc": "2026-10-21T07:52:44+00:00",
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

