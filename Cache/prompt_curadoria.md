atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-06T07:32:48.666576+00:00
Total: 2966 manchetes

  🇯🇵 Japão          1271
  🇨🇳 China          774
  🇹🇼 Taiwan         250
  🇰🇷 Coreia do Sul  671

## O que já está no feed (não repita)

  - [japan] 10-year government bond interest rate set at 3.1% per year
  - [japan] BOJ chief calls for more focus on anchoring inflation around target
  - [japan] Liberal Democratic Party/Ishin “Efforts to pass food consumption tax reduction bill in the current Diet sessio
  - [korea] Samsung Biologics union seeks bargaining with Samsung Electronics
  - [japan] Japan's Nikkei climbs 1% on dip in crude oil, smooth JGB auction
  - [japan] BREAKING NEWS: BOJ to raise rates as needed to stabilize inflation: governor
  - [korea] Kospi Snaps Two-Session Winning Streak; Defense, Chip Stocks Retreat
  - [japan] BOJ Ueda says financial conditions remain loose
  - [korea] The amount of finance supported by the Export-Import Bank of Korea to smoothly secure "seven key min..
  - [japan] Japan's Iwatani, Cosmo to develop hydrogen supply chain at Chiba refinery
  - [china] China turns on the export taps as LME zinc squeeze grinds on: Andy Home
  - [japan] Prime Minister Takaichi asks US President Trump to approach Japan-North Korea summit meeting
  - [korea] Samsung Biologics union seeks direct talks with Samsung Electronics
  - [korea] Vice Minister of Finance and Economy Kwon Dae-young said on the 6th that the Financial Services Comm..
  - [japan] 10-year JGB coupon hits 30-year high as rising rates add to fiscal fears
  - [japan] Food consumption tax reduction bill approved by the Liberal Democratic Party's Board of Governors and to be su
  - [china] AI street surveillance system China's exports are increasing
  - [korea] SK Hynix compresses at KRW 1,776,000 Fibonacci support: Live
  - [japan] [Today's Oha Biz October 6th (Tuesday)] Major housing manufacturer's strategy review
  - [japan] Jefferies Names Top Japan Semiconductor Equipment Stocks to Buy By Investing.com
  - [japan] Jefferies Names Top Japan Semiconductor Equipment Stocks to Buy
  - [japan] Bank of Japan may decide to reach 2% underlying inflation at October meeting - source (Reuters)
  - [japan] BOJ may signal underlying inflation has hit 2% goal, sources say
  - [korea] Samsung steps up HBM cooling as TSMC expands CoWoS
  - [japan] Japan bonds pare losses after strong auction, but fiscal worries weigh
  - [japan] Kawasaki Heavy: Aims For Revenue Of More Than 3.3 Trln Yen And Business Profit Of More Than 330 Billion Yen By
  - [japan] Asian currencies mixed as dollar climbs, euro nears 17-month low
  - [taiwan] Solidigm expands Taiwan SSD production base to tap AI server supply chain
  - [korea] Bank of Korea ahead of the Monetary Policy Committee in October… The variables that determine the base interes
  - [japan] World map made of glass beads in the Bank of Japan underground vault unveiled at Kanazawa Machinaka Arts Festi
  - [japan] Citi Strategist Sees JGB Yields Nearing Peak
  - [japan] Japan Yield Gains as Takaichi Vows Fiscal Expansion
  - [korea] Most Asian FX steady; Philippine peso, South Korean won weaken
  - [japan] Yen Steady as Takaichi Vows Fiscal Expansion
  - [japan] It is reported that the Bank of Japan has determined that the underlying inflation rate has reached 2% (curren
  - [japan] Japan bonds slide before 10-year auction amid fiscal worries at home and abroad
  - [korea] Finance minister vows efforts to tame inflation, boost growth
  - [korea] South Korea finance minister sees economic growth in 3% range this year
  - [korea] Samsung Electro-Mechanics Gains After Chip-Packaging Equipment Purchase Deal
  - [korea] Hanmi to Build Packaging Equipment for Samsung's AI-Chip Substrates

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
      "published_utc": "2026-10-06T07:32:48+00:00",
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

