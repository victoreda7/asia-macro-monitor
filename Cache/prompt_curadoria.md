atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-19T17:42:44.129973+00:00
Total: 3000 manchetes

  🇯🇵 Japão          994
  🇨🇳 China          900
  🇹🇼 Taiwan         350
  🇰🇷 Coreia do Sul  756

## O que já está no feed (não repita)

  - [korea] Agriculture Ministry eyes legal action over egg import, farmland claims
  - [china] Goldman Sachs raises copper forecast as US-China competition tightens supply
  - [japan] Advantage Partners Readies Japan's First Big Forestry Investment Fund, Nikkei Reports
  - [japan] Advantage Partners readies Japan's first big forestry investment fund
  - [china] China Tightens Export Controls on Drone Parts, Eases Curbs on Farm Models
  - [korea] Samsung Makes Unusual Move for Nvidia Chips
  - [china] Yuan Ranks Third in Global Payments Under Broader Measure, PBOC Chief Says
  - [korea] SK hynix launches W2tr financing program to bolster chip suppliers
  - [japan] Preview: Forecasters See Japanese Exports, Imports Continuing to Surge in September Report as Tech Spending Ri
  - [china] Euro falls amid turmoil in France, Australian dollar appreciates as China grows
  - [china] China’s Second-Tier New-Home Prices Flatten as Property Slump Persists
  - [china] Micron Stock Rallies as China Memory Chip Rival Forecasts Revenue Boom — Barrons.com
  - [china] Pace of Chinese Yuan's Gains Vs Dollar Likely to Remain Gradual — Market Talk
  - [taiwan] Business groups back Taipower, CPC subsidies; scholars dissent
  - [japan] Consumption tax reduction bill: Ruling party: “Committee deliberation begins on 21st” Opposition: “Enhancement
  - [japan] Agriculture Minister Yan and Minister of Education, Culture, Sports, Science and Technology Seki pursue the fu
  - [korea] Samsung Is Turning to Rival TSMC for Nvidia's Next AI Memory
  - [korea] Kr Motors To Divest Real Estate Worth 47.5 Billion Won
  - [taiwan] AI chip startup Tenstorrent more than doubles its valuation to $6.2 billion in funding round
  - [china] XiAn Eswin Material Technology Q3 Net Profit At 440.7 Million Yuan
  - [china] The Chinese government announced on the 19th a plan to adjust export controls on drone-related produ..
  - [korea] AM Markets Need to Know: Musk plans SpaceX gift, Samsung taps TSMC, and more
  - [japan] Micronesian President visits Japan and holds summit meeting with Prime Minister Takaichi
  - [china] Shenzhen Investment Says In Q3, Real Estate Dev Business Unaudited Contracted Sales Of Rmb1.814 Bln
  - [japan] Liberal Democratic Party Ishin leadership seeks cooperation from opposition parties to pass consumption tax re
  - [china] China's economic growth gains strength with export boom
  - [china] China’s Retail Sales Growth Accelerates to 1.1%
  - [japan] Prime Minister Takaichi secures financial resources for consumption tax reduction “Proceed with review of expe
  - [china] China’s central bank studies making overnight rate its main policy rate
  - [china] United Nova Technology Q3 Net Profit At 411.7 Million Yuan
  - [china] China GDP Growth Beats Expectations
  - [china] China's Export Boom Masks Deep Economic Problems at Home — WSJ
  - [china] China’s Industrial Output Growth Picks Up
  - [japan] Yen price falls slightly against the dollar against the backdrop of rising crude oil futures prices
  - [china] LME owner HKEX eyes more yuan-denominated commodities contracts
  - [korea] Samsung said to use TSMC tech for Nvidia's next-generation memory chips
  - [china] China Slaps Export Curbs on More Drones and Industrial Machinery
  - [korea] Stocks are jumping around the earnings announcement... Why the impact of base interest rate changes is minimal
  - [taiwan] BREAKING NEWS: Mitsubishi Electric, Hon Hai subsidiary aim for FY 2030 1 tril. yen sales
  - [korea] Chip boom to continue through 2027, South Korea minister tells CNBC

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
      "published_utc": "2026-10-19T17:42:44+00:00",
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

