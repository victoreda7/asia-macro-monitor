atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-25T13:32:57.632051+00:00
Total: 3000 manchetes

  🇯🇵 Japão          942
  🇨🇳 China          1006
  🇹🇼 Taiwan         344
  🇰🇷 Coreia do Sul  708

## O que já está no feed (não repita)

  - [china] China Southern Airlines Subsidiary Orders 50 Boeing Aircraft For $7.4 Bln
  - [china] Trump admin proposes new tariffs on 14 trading partners, 20% on China - report
  - [taiwan] TSMC asking for tax incentives at Texas fab suggests no AI slowdown: Wedbush
  - [japan] Japan to draft 2nd supplementary budget for urgent needs
  - [china] Taxman can be China's next GDP growth engine
  - [china] The Logistics Report: China and Other Countries Face Higher U.S. Tariffs Over Industrial Subsidies — WSJ Newsl
  - [china] 800 billion + 500 billion! The central bank's "combination punch" protects liquidity
  - [japan] $1.6bn real estate development in Tokyo's Shibuya wins key approval
  - [china] Central Bank: Will launch 500 billion yuan 7-day reverse repurchase operation on November 25
  - [taiwan] TIER expects U.S. tariffs on Taiwan goods not to top 15%
  - [china] Analysis-Jensen Huang’s return to Nvidia fuels Washington fight over China’s chip access
  - [korea] 54% of bond market workers say, “The Bank of Korea Monetary Policy Committee will raise the base interest rate
  - [china] China Merchants China Direct Investments Says Tian Zheng Agreed To Contribute Capital Of Rmb30 Million To Yuan
  - [japan] My home loan interest rate is a concern due to the Bank of Japan's interest rate hike. ``My repayments haven't
  - [japan] [There are also benefits that NISA does not have! iDeCo Complete Guide] Who will benefit from the revision? / 
  - [japan] Advance utilization of the former Bank of Japan Kanazawa branch site "Machinowa Korinbo" will begin use from M
  - [china] USAR, CRML, UAMY, MP Stocks Drop Premarket: China Extends Mineral Export Pause Amid Looming US Tariff Hikes
  - [taiwan] Texas comptroller backs US$354 million tax break for TSMC
  - [japan] The site of the former Bank of Japan Kanazawa branch will be opened to the public from May 22, 2027 Collection
  - [korea] AI Chip Boom to See Won Build on Best Year in Almost a Decade
  - [china] China’s Surprise Soyoil Export Boom Cools as India Turns to Palm
  - [china] EU sets caps on Chinese, Korean hybrid car imports; impact on Hyundai, Kia seen limited
  - [korea] Clash over end to AI memory boom heats up, roiling Korean chip stocks
  - [korea] The National Assembly will review next year's "Future Response Fund" budget, which amounts to around..
  - [taiwan] Zhang Jianyi: It is estimated that the central bank will consider raising interest rates by half a point in De
  - [korea] Clash over end of AI memory boom heats up, roiling Korean chip stocks
  - [china] China, US Set for ‘New Chapter’ of Trade Talks, Ex-Official Says
  - [china] China's PVC exports face anti-dumping investigations in many places. China's utilization rate is expected to r
  - [taiwan] U.S. dollar closes sharply higher on Taipei forex market
  - [japan] Japanese Government Bonds Held by the Bank of Japan
  - [china] China Dismisses US Tariff Prospect as ‘Political Maneuvering’
  - [taiwan] NTU team develops energy-efficient chips for on-device generative AI
  - [taiwan] Analysis: Nvidia leadership settled, but US export rules still cloud outlook for Taiwan server makers
  - [china] Chinese Stock Losses Widen as Semiconductor Stocks Weigh — Market Talk
  - [taiwan] Manufacturers' business sentiment weakens amid AI concerns
  - [korea] Kospi Falls to 10-Month Low as Chip Stock Selloff Resumes — Market Talk
  - [taiwan] Maintenance and component demand lift profits across Taiwan's aerospace supply chain
  - [china] China's Politburo shrinks as graft crackdown spreads
  - [china] MLF's continuous net withdrawals, what kind of signal does the 7-day reverse repo release at the end of the mo
  - [japan] Jtekt Corporation - To Launch Tender Offer For Own Shares Prices At 1,733 Yen Per Share

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
      "published_utc": "2026-11-25T13:32:57+00:00",
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

