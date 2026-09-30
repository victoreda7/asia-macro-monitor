atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-30T00:02:45.717397+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1270
  🇨🇳 China          760
  🇹🇼 Taiwan         254
  🇰🇷 Coreia do Sul  716

## O que já está no feed (não repita)

  - [japan] JAPAN AUG RETAIL SALES -1.2% M/M (JULY REVISED TO +2.1% FROM +2.4%); MEDIAN FORECAST -0.9% (RANGE: -1.6% TO -0
  - [korea] Hengan International Says Chair And Executive Director Sze Man Bok Passed Away On Sept 29
  - [japan] JAPAN AUG RETAIL SALES +2.7% Y/Y (JULY REVISED TO +3.7% FROM +4.0%); 6TH STRAIGHT RISE; MEDIAN FORECAST +2.7% 
  - [japan] JAPAN METI KEEPS VIEW: INDUSTRIAL OUTPUT TAKING ONE STEP FORWARD AND ONE STEP BACK
  - [japan] JAPAN AUG INDUSTRIAL OUTPUT +3.4% Y/Y (JULY REVISED TO +3.9% FROM +4.1%), 3RD STRAIGHT RISE; MEDIAN FORECAST +
  - [japan] JAPAN AUG INDUSTRIAL OUTPUT -1.7% M/M (JULY REVISED TO -0.2% FROM +0.1%); 2ND STRAIGHT FALL; MEDIAN FORECAST +
  - [japan] Japan Aug Inventory-Shipments Ratio +1.7% on Month
  - [japan] Japan Aug Shipments -2.5% on Month
  - [japan] Japan August factory output falls 1.7% month-on-month
  - [japan] Nikkei May Rise as Decline in Oil Prices Ease Inflation Fears — Market Talk
  - [china] China promete reagir caso UE adote medidas que visem comércio chinês
  - [korea] South Korea Retail Sales Fall Again in August
  - [china] China plans to strengthen surveillance on steel exports
  - [korea] South Korea Industrial Output Unexpectedly Falls
  - [korea] The annual interest burden of the Korea Land and Housing Corporation (LH), which supports the govern..
  - [japan] Tsuyoshi Morioka's reputation has changed from being the ``God of Marketing''...The true nature of his ``abili
  - [korea] Trump set to unveil $200B South Korean U.S. investment plan
  - [japan] Three banks in Chiba Prefecture raise interest rates to 0.5% for ordinary deposits in response to Bank of Japa
  - [japan] Nikkei average could reach 80,000 yen level due to six performance improvement drivers such as AI and semicond
  - [japan] <Liquor tax will be unified from October> Behind the scenes of dependence on champion Asahi's "Super Dry"... "
  - [japan] Roland revived from a large deficit through MBO...6 years after relisting, now that the fund that supported th
  - [korea] SK Hynix Stock Rises While Bernstein Cuts Target
  - [taiwan] Wells Fargo Spots Unexpected Winner in TSMC's 2nm Race
  - [korea] Appeals court declines to pause sanctions against Trump lawyers in IRS settlement
  - [japan] Japan to create state investment fund for defense startups, eyeing more drones
  - [taiwan] The Trump-Xi summit leaves Taiwan in limbo
  - [korea] Korea launches its own version of popular US fund Roundhill Memory ETF DRAM
  - [taiwan] TSMC Stock Moves Higher as AI Revival Meets Capacity Risk
  - [taiwan] TSMC's 2nm Push Could Create a New Winner in the AI Chip Boom
  - [korea] Samsung Electronics Stock Gains as Helix Draws $1 Billion
  - [japan] Prime Minister Takaichi held a summit meeting with Prime Minister of Mongolia Nyamuosor Otilal
  - [korea] Korea’s dollar store giant Daiso emerges as real estate player with $355 mn deals
  - [china] China Posts $378 Billion Current Account Surplus Driven by Strong Exports, AI
  - [china] The central bank uses multiple tools to protect liquidity, and funding is expected to be stable across quarter
  - [korea] Seoul stocks fall for 2nd day on inflation woes
  - [korea] Why did Micron, SK Hynix and SanDisk shares rise on Tuesday?
  - [korea] The Korean financial market is tense due to the sharp rise in US and Japanese government bond yields... Bank o
  - [japan] Wells Fargo revises dollar, yen, euro estimates amid rate hike outlook
  - [korea] K-defense: A textbook case of transforming weapons self-reliance into global exporter
  - [china] Four arrows fired in unison! After the National Standing Committee set the tone, the central bank launched a n

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
      "published_utc": "2026-09-30T00:02:45+00:00",
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

