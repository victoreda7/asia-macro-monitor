atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-09T09:12:44.950172+00:00
Total: 3000 manchetes

  🇯🇵 Japão          929
  🇨🇳 China          870
  🇹🇼 Taiwan         329
  🇰🇷 Coreia do Sul  872

## O que já está no feed (não repita)

  - [china] China Will Extend U.S. Tariff Suspensions for Two Months as Trump Visit Looms — Update
  - [japan] ``Party support rate'' for about 30 years The key to elections revealed by NHK opinion poll
  - [korea] Lam Research, Comet bid for S.Korean chip equipment maker Dawon Powertron
  - [korea] Foreign currency raised by the Export-Import Bank of Korea is expected to exceed $17 billion (about
  - [taiwan] Taiwan's October exports surge again on strong AI demand
  - [korea] As international energy prices soar, concerns are growing over the financial deterioration of state
  - [korea] As financial authorities regulate Samsung Electronics and SK Hynix's single-stock leveraged exchange..
  - [china] China Will Extend U.S. Tariff Suspensions for Two Months as Trump Visit Looms
  - [china] CNH/USD: Cross-Border Yuan Flows on China’s Network Head for Record Year
  - [taiwan] AI chip testing demands lift Taiwan's wafer testing specialist HTSI as October revenue surges 62%
  - [china] Xinhua News | China extends suspension of 24 pct additional tariff on U.S. goods for two months
  - [japan] September economic trend index increased by 0.7 points from the previous month, the first increase in 2 months
  - [taiwan] Taiwan's Export Growth Stays Robust Despite AI Selloff
  - [korea] The government has set aside 1.4 trillion won in budget to supply 10,000 public rental homes for you..
  - [china] China Passenger-Car Sales Slump in October Despite Export Boom — Update
  - [china] Exclusive-Chinese banks boost dollar deposit rates, sources say, as Beijing seeks to smooth yuan rally
  - [china] Key facts: NVIDIA China curbs; chip-demand view; Nov. 17/18 events
  - [china] Opinion: Building a Virtuous Cycle Between Consumption and Investment
  - [japan] Mr. Ishiba and four others respond to the consumption tax reduction bill by giving their reasons for leaving t
  - [china] Wholesale prices of manufactured goods in China and the Middle East rise to the highest level in 4 years and 4
  - [china] China inflation misses estimates as food prices extend decline
  - [japan] SoftBank: AI-led growth targets FY2030 revenue of JPY 9.0 tn and operating income of JPY 1.7 tn
  - [taiwan] Exclusive: Gallium oxide prepares to tackle power semiconductor market with 6-inch mass production and 8-inch 
  - [china] China’s export growth expected to have remained strong in October: Reuters poll
  - [japan] The Liberal Democratic Party and the Meiji Restoration work closely together in the House of Councilors delibe
  - [japan] Chuo Warehouse Co Ltd - To Buy Back Up To 4.3% Of Own Shares Worth 1 Billion Yen
  - [japan] Six opposition parties in the House of Councilors urge the prime minister to attend consumption tax reduction 
  - [japan] Japan stepped in to buy one-day record 7.98 tril. yen in July: gov't data
  - [taiwan] TIER raises Taiwan's 2026 growth forecast to 12.34% on AI demand
  - [japan] Government/BOJ yen buying intervention hits record high of approximately 8 trillion yen on July 30th (ABEMA TI
  - [japan] The Chiba Bank, Ltd. - To Buy Back Up To 1.09% Own Shares Worth 15 Billion Yen
  - [japan] Pola Orbis Holdings: Operating profit rose 21.3%; yen-driven FX gains lifted the FY outlook
  - [korea] A total of 8.354 billion won in monetary sanctions and measures against 23 executives and employees
  - [taiwan] Zhang Jianyi: CPI may exceed 3% if CNPC and Taipower fail to allocate subsidies, forcing the central bank to r
  - [korea] Nvidia scandal raises export risks for Korean chipmakers
  - [china] China's October car exports stay resilient
  - [china] China Passenger-Car Sales Slump in October Despite Export Boom
  - [korea] Bank of Korea predicts interest rate hike in November... Market interest rate direction and banking calculatio
  - [japan] Juroku Financial Group Inc - To Buy Back Up To 1.129% Own Shares Worth 5 Billion Yen
  - [japan] Mirait One Corp Says It Will Buy Back Up To 0.91% Of Own Shares Worth 2 Billion Yen

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
      "published_utc": "2026-11-09T09:12:45+00:00",
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

