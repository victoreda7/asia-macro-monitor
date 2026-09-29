atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-29T18:55:00.909712+00:00
Total: 420 manchetes

  🇯🇵 Japão          152
  🇨🇳 China          119
  🇹🇼 Taiwan          34
  🇰🇷 Coreia do Sul  115

## O que já está no feed (não repita)

  - [taiwan] TSMC Stock Moves Higher as AI Revival Meets Capacity Risk
  - [taiwan] TSMC's 2nm Push Could Create a New Winner in the AI Chip Boom
  - [korea] Samsung Electronics Stock Gains as Helix Draws $1 Billion
  - [korea] Korea’s dollar store giant Daiso emerges as real estate player with $355 mn deals
  - [china] The central bank uses multiple tools to protect liquidity, and funding is expected to be stable across quarter
  - [korea] Seoul stocks fall for 2nd day on inflation woes
  - [korea] Why did Micron, SK Hynix and SanDisk shares rise on Tuesday?
  - [japan] Wells Fargo revises dollar, yen, euro estimates amid rate hike outlook
  - [china] Four arrows fired in unison! After the National Standing Committee set the tone, the central bank launched a n
  - [china] China launches 'mini stimulus' targeting affordable homes, infrastructure
  - [china] China announces interest rate cuts and mortgage subsidies to boost growth
  - [china] Libya's High State Council rejects changes to presidential election law as "unconstitutional"-Xinhua
  - [korea] Korea launches its own version of popular US fund Roundhill Memory ETF DRAM
  - [china] China unveils rate cut, mortgage subsidies to spur growth
  - [china] China espera que comércio cresça apesar dos desafios externos
  - [china] KMT, TPP legislators reject all 27 of Lai's Control Yuan nominees
  - [china] China Offers Mortgage Subsidies to Boost Ailing Property Sector
  - [china] China to subsidize mortgage interest for first-time home buyers
  - [china] China cuts key interest rate, offers mortgage subsidy to boost economy
  - [japan] Supplementary budget proposal of 14.9 billion yen TEPCO's contribution to snow removal support: Prefectural as
  - [korea] The annual interest burden of the Korea Land and Housing Corporation (LH), which supports the govern..
  - [korea] Seoul stocks open lower on inflation woes
  - [taiwan] In global semiconductor race, Singapore bets on critical, mature technologies
  - [japan] 2-year interest rate approaches 2%, Bank of Japan's intention to change stance Assessing the Tankan (Reuters)
  - [japan] 2-year interest rate approaches 2%, Bank of Japan's stance is changing - Assessing the Tankan (Reuters)
  - [korea] Issues that affect the decision to increase interest rates... Look at the remarks of the Monetary Policy Commi
  - [japan] Asia stocks subdued as rising yields, oil weigh; RBA hikes rates as expected
  - [china] Demand Boost for US Crops Still Unclear After China Tariff Cuts
  - [japan] EQt Raises Tender Offer Price For Kakaku.Com To 3,681 Yen From 3,680 Yen, Filing Shows
  - [korea] The Bank of Korea approves a monetary and credit policy report containing the background for raising the base 
  - [japan] Japanese Shares Fall on Inflation Worries
  - [taiwan] Singapore's chip progress
  - [japan] The Bank of Japan and the Federal Reserve have no choice but to worry about stock prices -- The focus of monet
  - [china] Stifel upgrades STAAR Surgical stock rating on China growth outlook
  - [korea] SK Hynix Could Post Lower-Than-Expected But Still Record 3Q Operating Profit — Market Talk
  - [korea] (LEAD) Seoul stocks fall for 2nd day on inflation woes
  - [taiwan] Column: Why Micron's US$250M venture fund is about more than HBM margins—Taiwan has a stake in it
  - [korea] (URGENT) Seoul stocks fall for 2nd day on inflation woes
  - [china] China Signals Economic Stimulus to Counter Worsening Slowdown
  - [china] ‘Important and consequential’: Jensen Huang on US-China AI race, risk management

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
      "published_utc": "2026-09-29T18:55:01+00:00",
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

