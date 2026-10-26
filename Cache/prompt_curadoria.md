atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-26T13:33:46.142343+00:00
Total: 3000 manchetes

  🇯🇵 Japão          981
  🇨🇳 China          853
  🇹🇼 Taiwan         373
  🇰🇷 Coreia do Sul  793

## O que já está no feed (não repita)

  - [korea] Micron, SanDisk and SK Hynix Stocks Climb as AI Memory Demand Takes Center Stage
  - [taiwan] Goldman Sachs revise up Taiwan's GDP growth forecast for this year and next, predicting the start of an intere
  - [china] China plans to strengthen the protection of trade secrets and ban foreign investment in the import and export 
  - [china] On October 26, the central bank launched a 56 billion yuan 7-day reverse repurchase operation.
  - [japan] Euro firms against yen, flat vs dollar ahead of central bank meetings
  - [china] China XLX Fertiliser nine-month profit rises on export growth
  - [china] Zhejiang Jiemei Electronic and Technology Plans To Invest 2.7 Billion Yuan In Project
  - [korea] SK hynix Inc. expected to post earnings of $6.00 a share - Earnings Preview
  - [korea] SK hynix Price Target Cut to $250.00/Share From $300.00 by Cantor Fitzgerald
  - [china] Dosilicon Q3 Net Profit At 830.1 Million Yuan
  - [china] SPIC Industry Finance Q3 Net Profit At 903.3 Million Yuan
  - [china] EU Plans to Hit China With More Import Curbs in Early 2027
  - [japan] Japan's largest machine tool trade show Introducing technologies using AI
  - [japan] Currencies idle ahead of five-bank gauntlet; euro gains on Moody’s reprieve
  - [china] China's central bank launches swap facility to offer emergency liquidity to asset managers
  - [korea] SK Hynix Plans $12 Billion Dividend From Kioxia Gains: Report
  - [japan] Euro firms against dollar, yen ahead of central bank meetings
  - [korea] Vt Co Ltd To Acquire Real Estate Worth 79 Billion Won
  - [china] Beijing Wantai Biological Pharmacy Q3 Net Loss At 102.5 Million Yuan
  - [china] Asian stocks closed with mixed trends as the market awaits technology industry earnings reports and central ba
  - [china] China's central bank sets up non-bank financial institution bond market swap facility
  - [japan] Japan auto union group looks beyond inflation-linked pay hikes for 2027 talks
  - [taiwan] Taiwan Industrial Output Growth Eases to 4-Month Low
  - [china] China stocks end flat as investors turn cautious before key central bank meetings
  - [korea] Industrial Bank of Korea: SME growth and higher interest income offset rising credit costs and weaker subsidia
  - [korea] The Bank of Korea warned that if U.S. big tech companies' investment in artificial intelligence (AI)..
  - [korea] Due to the boom in artificial intelligence (AI) semiconductors, the Korean economy's external report..
  - [korea] The difference in housing prices owned by the top 20% of Korea's national assets and the bottom 20%
  - [korea] AI chip surge lifts South Korea to record surplus, behind only China
  - [korea] Director Choi Chang-ho appointed as Bank of Korea's new Assistant Vice President for Monetary Policy and Marke
  - [china] XTC New Energy Materials Xiamen's Unit Plans To Invest 722.5 Million Yuan In Project
  - [korea] Korea's export front is on alert as the European Union (EU) raises trade barriers with carbon neutra..
  - [korea] Amid the strong won (the weak dollar), the investment strategy of an opportunity to buy dollar-denom..
  - [korea] Shipbuilders’ earnings rise and fall with their ‘currency-hedging strategies’
  - [china] Shenzhen Envicool Technology: Strong revenue growth was offset by lower 9M earnings and shipment timing delays
  - [korea] Another major concern for domestic artificial intelligence (AI) semiconductor companies is when they..
  - [korea] Kukdo Chemical Co To Buy Lg Chem's Bpa Manufacturing Facility And Business Unit For 78.4 Billion Won
  - [taiwan] Taiwan Retail Sales Hit Over 2-Year High
  - [korea] Industrial Bank Of Korea Earnings Up In Q3
  - [japan] Sumitomo Life to remain cautious on JGB yields, keep investment pace unchanged from H1

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
      "published_utc": "2026-10-26T13:33:46+00:00",
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

