atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-29T01:12:24.787802+00:00
Total: 420 manchetes

  🇯🇵 Japão          151
  🇨🇳 China          121
  🇹🇼 Taiwan          35
  🇰🇷 Coreia do Sul  113

## O que já está no feed (não repita)

  - [korea] Seoul stocks open lower on inflation woes
  - [korea] Samsung Electronics: HBM will account for nearly 30% of industry DRAM capacity next year
  - [china] Soybeans near one-month low on exclusion from China's proposed tariff cuts
  - [korea] Samsung Electronics says HBM to account for nearly 30% of industry DRAM capacity next year
  - [korea] While the Seoul apartment sales price index, which compared January to August this year, rose 6.4%
  - [korea] (LEAD) Seoul stocks open lower on inflation woes
  - [korea] Hanmi Semiconductor Wins 8 Billion Won Order
  - [korea] (URGENT) Seoul stocks open lower on inflation woes
  - [korea] Samsung Electronics allocates US$1 billion to expand Helix Digital AI, a company backed by KKR
  - [korea] Samsung Electronics commits $1 billion to KKR-backed Helix Digital AI buildout
  - [japan] Japan's currency diplomat Mimura urges markets to heed 'very clear' warning on yen
  - [korea] Samsung Electro-Mechanics' Vietnam Affiliate to Spend KRW2.510T to Expand Chip-Substrate Production
  - [korea] Samsung Electro-Mechanics to Spend KRW4.270T to Expand Chip-Substrate Production in Sejong
  - [taiwan] Behind CoWoS (part 2): How TSMC turned a niche packaging experiment into an industry standard
  - [taiwan] Behind CoWoS (part 1)—How a 0% yield crisis led to TSMC's first advanced packaging win
  - [japan] Business confidence improves due to AI demand, but rising prices are a headwind for personal consumption (Sept
  - [japan] Should I sell the “New NISA” due to the Bank of Japan interest rate hike? Misconception that “interest rate hi
  - [japan] It's a miracle that ``Japanese gin'' sells ``430,000 bottles a year'' in its home country of England...The tru
  - [japan] Japan's Resonac develops large wafers that can yield 4 times as many chips
  - [japan] Used condominium market plunges into “inventory hell” due to Bank of Japan interest rate hike (Bunshun Online)
  - [korea] Biz sentiment falls in September on rising costs: BOK
  - [japan] A direct interview with the CEO of heating type king “IQOS”! The existence of competitors such as JT is "welco
  - [china] The need for a "New Plaza Accord" increases as China's trade surplus increases dramatically... A huge trade im
  - [japan] Will the price advantage of heating type disappear? How will JT and BAT challenge the champion "ICOS" with a 7
  - [korea] SK Hynix Stock Falls 5.1% as Rubin Memory Moves Into View
  - [japan] Yen Gains After Japan’s Currency Czar Warns Against Weakness
  - [korea] PAG Real Assets eyes $2 bn investment in S.Korean real estate
  - [china] The 14-day reverse repurchase restarted, and the central bank’s open market operations invested a total of 1.1
  - [korea] Seoul stocks sink over 2.5% on chip losses
  - [china] CBOT soybean futures plunge as China tariff cuts exclude soybeans
  - [japan] Preview: Forecasters See Japan September Tankan Showing Large Manufacturers’ Sentiment at +25, Highest Since 2
  - [china] China tightens humanoid patent grip with 60% share
  - [taiwan] TSMC increases 2nm wafer production outlook by 20%: report
  - [korea] What's next for Intel after the SK Hynix partnership rumors?
  - [china] Chinese premier chairs State Council executive meeting on macro policies, investment
  - [china] China Studies Policies to Boost Economy, Stabilize Housing Market
  - [japan] U.S. debt sell-off extends on $106 crude oil and hawkish central bank outlooks
  - [china] Brazil signs an agreement with China to export pork offal; ABPA sees more than US$100 million in revenue
  - [japan] The Bank of Japan releases the minutes of its July monetary policy meeting, with several members giving positi
  - [china] US, China Release Product Lists for $30 Billion Tariff Deal

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
      "published_utc": "2026-09-29T01:12:24+00:00",
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

