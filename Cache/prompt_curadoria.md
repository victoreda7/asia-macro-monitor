atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-28T15:50:49.833225+00:00
Total: 420 manchetes

  🇯🇵 Japão          151
  🇨🇳 China          128
  🇹🇼 Taiwan          34
  🇰🇷 Coreia do Sul  107

## O que já está no feed (não repita)

  - [korea] Seoul stocks sink over 2.5% on chip losses
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
  - [korea] PAG Real Assets eyes $2 bn investment in S.Korean real estate
  - [taiwan] TSMC, others hold recruitment campaign in Silicon Valley
  - [china] Soybeans plummet more than 20 points in Chicago after China keeps American grain out of tariff cuts
  - [china] Russian oil supply to India tightens on reduced exports, strong Chinese demand
  - [japan] Citi sees Japan yen intervention likely near 160 per dollar By Investing.com
  - [japan] Citi sees Japan yen intervention likely near 160 per dollar
  - [china] China Auto Subsidy Scheme Unravels, Leaving Consumers and Banks Exposed
  - [taiwan] VIS-NXP JV chip fab enters initial production stage
  - [japan] Exclusive-Japan’s currency diplomat Mimura urges markets to heed ’very clear’ warning on yen By Reuters
  - [japan] EXCLUSIVE: Japan's currency diplomat Mimura urges markets to heed 'very clear' warning on yen
  - [japan] Yen Gains After Japan’s Currency Czar Warns Against Weakness
  - [korea] [Preview of National Assembly Inspection] Bank of Korea Governor Shin Hyun-song’s first National Assembly insp
  - [china] The central bank launched three-term reverse repos on September 28, with a net investment of 439.7 billion yua
  - [korea] This week, a window manufacturing company with annual sales of 20 billion won was registered as a sa..
  - [china] China e EUA concordam em reduzir tarifas sobre US$60 bi em mercadorias
  - [korea] [Palm Economy] Base interest rates in global financial markets
  - [japan] Bank of Japan releases summary of July decision-making meeting; multiple members call for acceleration of inte
  - [japan] BREAKING NEWS: Dollar plunges nearly 1 yen, falls below 157 line
  - [korea] As construction of industrial facilities, including private semiconductor production facilities, inc..
  - [japan] Asia stocks slip as oil, yields rise; chipmakers hit by OpenAI pause
  - [japan] Bank of Japan debated need for faster rate hikes, July minutes show By Reuters
  - [korea] Deputy Prime Minister and Minister of Finance and Economy Lee Hyung-il visits the Bank of Korea head..
  - [japan] Jobs Report and Inflation Reading to Gauge US Economic Strength This Week
  - [china] US, China slash tariffs on basic goods – but leave rare earths off the record
  - [japan] A very annoying "Christmas gift"...The Bank of Japan's proposal infuriated the Banking Bureau of the Ministry 
  - [korea] Will continuous increases in base interest rates put a burden on the profitability of savings banks?
  - [taiwan] TSMC affiliate already eyes expansion as first Singapore plant 'sells out'
  - [china] US and China list Christmas ornaments, lumber, camels for tariff cuts
  - [korea] Hyung-il Lee and Hyun-song Shin first meeting... Are fiscal-monetary policies in sync?

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
      "published_utc": "2026-09-28T15:50:49+00:00",
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

