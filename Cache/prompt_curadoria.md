atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-02T03:52:46.069058+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1298
  🇨🇳 China          780
  🇹🇼 Taiwan         248
  🇰🇷 Coreia do Sul  674

## O que já está no feed (não repita)

  - [japan] Japanese yen firms on strong inflation, dollar muted before payrolls test
  - [japan] Japan does not need excessively loose monetary policy, economy minister says
  - [taiwan] DIGITIMES Insight: Intel, TSMC, Samsung converge on backside power — packaging becomes the next divide
  - [china] China's PMI Recovery Encouraging Despite Fragile Domestic Demand — Market Talk
  - [japan] September consumer price index for Tokyo's 23 wards, total excluding fresh food, rose by 2.7% Autumn delicacy 
  - [japan] Yen Steadies After Hot Tokyo Inflation Data
  - [taiwan] TSMC, NTU deepen R&D ties through nearly 50 projects a year
  - [taiwan] Taiwan dollar weakens, Philippine peso gains among largely muted Asian FX
  - [japan] Tokyo core inflation rate jumps in September, bolsters case for more BOJ hikes
  - [china] Asia's gasoline margin skyrockets on outages, China export halt, traders say
  - [korea] Samsung Electronics, SK hynix trade near flat after trimming losses
  - [japan] Toho, the largest commercial food wholesaler, has revised its sales forecast upward, but profits remain unchan
  - [japan] Japan power semiconductor deal stalls as Rohm, Toshiba, Mitsubishi haggle
  - [japan] September consumer price index for Tokyo's 23 wards increased by 2.7% compared to the same month last year
  - [japan] Tokyo prices rose 2.7% in September, reaching the 2% level for the first time in eight months (Kyodo News)
  - [china] Hangzhou Great Star 3Q Earnings Likely Weighed by Yuan Strength — Market Talk
  - [korea] South Korean Shares Edge Lower on Inflation Concerns
  - [korea] South Korean policymakers ramp up warnings amid bond sell-off
  - [japan] Why is Russia's finances in the biggest deficit even though crude oil prices have soared? The US's strong sanc
  - [korea] SSBT "The Bank of Korea freezes in October... If core prices rise, it will rise in November."
  - [japan] Japan MOF To Auction Y3.3T Of TD-Bills Oct 9
  - [japan] September consumer prices in Tokyo's 23 wards increased by 2.7% compared to the same month last year.Over 2% f
  - [japan] September consumer price index for Tokyo's 23 wards (excluding fresh food) 2.7% compared to the same month las
  - [japan] Opposition to the Bank of Japan's interest rate hike decision (Hiroyuki Kubota) - Expert
  - [korea] South Korea’s Sept inflation cools to 2.9% on fuel caps, lower farm prices
  - [taiwan] Key facts: TSMC (2330) Leads AI Foundry, Tops $2T Market Cap
  - [japan] Pickup in Tokyo Inflation Likely to Fuel Rate-Hike Views
  - [china] US Charges California Man Over $300 Million Nvidia Chip Shipments to China
  - [japan] [Tokyo Foreign Exchange] Dollar, low 157 yen level = softening due to strong Tokyo prices (9:00 am on the 2nd)
  - [japan] Tokyo inflation accelerates in Sept, strengthening case for further BOJ hikes By Investing.com
  - [japan] Tokyo inflation accelerates in Sept, strengthening case for further BOJ hikes
  - [korea] SK Hynix Stocks Gain 3.2% as Supply Contracts Reprice Memory Scarcity
  - [china] Man Charged by US With Illegally Shipping Nvidia Chips to China
  - [korea] Key facts: Samsung Electronics (005930) Q2 memory record; HBM4E samples
  - [japan] JAPAN SEPT TOKYO CORE-CORE CPI +3.0% Y/Y; AUG +2.0%
  - [japan] MNI JAPAN SEPT TOKYO CORE CPI +2.7% Y/Y; AUG +1.8%
  - [japan] Japan Jobless Rate Climbs To 2.5%
  - [japan] Tokyo Inflation Jumps To 2.7% Annually In September
  - [japan] Tokyo prices rose 2.7% in September (Kyodo News)
  - [japan] Average Contract Interest Rates on Loans and Discounts (Aug.)

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
      "published_utc": "2026-10-02T03:52:46+00:00",
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

