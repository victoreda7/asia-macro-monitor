atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-10T06:12:45.666252+00:00
Total: 3000 manchetes

  🇯🇵 Japão          936
  🇨🇳 China          896
  🇹🇼 Taiwan         311
  🇰🇷 Coreia do Sul  857

## O que já está no feed (não repita)

  - [japan] The current account surplus in the first half of this fiscal year is the second largest on record.
  - [korea] How Posco fortifies Korea's energy, battery supply chains
  - [japan] President Keiko Fujimori of Peru, South America, to visit Japan; coordination of summit meeting on 20th
  - [taiwan] Table: Taiwan Semiconductor Mfg Oct Rev NT$586.89B Vs NT$367.47B
  - [japan] If rejected in the House of Councilors, will the consumption tax be dissolved? The reality of the scenario in 
  - [korea] Semiconductor exports influence the Bank of Korea’s interest rate… Expected to be lowered by 3.5% during a boo
  - [china] Shanghai Electric Integrates Industrial AI into Heavy-Duty Gas Turbine Manufacturing and Lifecycle Services
  - [china] China's exports in October increased by 35.2% year-on-year, beating expectations. The surplus in the previous 
  - [japan] JGB yields rise after 30-year auction draws weak demand
  - [china] Alice Huang, Chinese businesswoman tied to Nvidia CEO, went from finance to chips
  - [china] Yuan Rally Likely to Cool, Not Reverse — Market Talk
  - [japan] Main opinions from the October meeting of the Bank of Japan Pointed out that it is important to “stick” the in
  - [japan] BOJ October Summary: Rate hikes should continue as inflation reaches 2% target
  - [japan] Sumitomo Metal Mining - To Buy Back Up To 2.79% Own Shares Worth 30 Billion Yen
  - [china] China's October trade surplus reaches $105.3B as exports jump 35.2% and imports surge 41.6%
  - [japan] Bank of Japan ETF sales to bring in $6.3 bln annually, finmin Katayama says
  - [china] Chinese Chip Firms Have Mixed Debuts in Hong Kong
  - [china] Moonshot AI rents Nvidia’s top chips in China, Bloomberg reports
  - [china] China's crude oil imports recover, fuel exports not so much: Russell
  - [japan] Tokyo Ohka Kogyo: AI-led semiconductor demand lifted 9M results and drove higher FY26 guidance
  - [japan] Future interest rate hikes will be ``implemented when possible,'' and there is also mention of raising the rat
  - [taiwan] Machine Tool Association: Exports of complete machines remain flat and key components continue to grow | Indus
  - [china] Moonshot Rents Nvidia’s Top AI Chips in China, Documents Show
  - [taiwan] Demand for gold reserves increases as Singapore launches central bank custody service to tap international mar
  - [japan] Analysis-Market rout tests BOJ’s upbeat view of financial conditions
  - [japan] BOJ Opinion Summary Shows Board Remains in Favor of More Tightening
  - [china] The central bank launched a 190 billion yuan reverse repurchase program on November 10, with a net investment 
  - [china] China Unlikely to Lower Policy Rate in Near Term — Market Talk
  - [taiwan] Central Bank: The current situation of foreign capital remittances of tens of billions of dollars in non-suppo
  - [japan] MODEC: Higher FY26 guidance follows strong 3Q26 results and a JPY 10B buyback approval
  - [china] China's Trade Surplus Surged Past $1 Trillion in October — WSJ
  - [japan] Toray Industries - To Buy Back Up To 5.08% Own Shares Worth 70 Billion Yen
  - [japan] Toa Corp (Tokyo) - To Buy Back Up To 5.67% Of Own Shares Worth 8 Billion Yen
  - [china] China October soybean imports fall on high inventories, weak crush margins
  - [korea] Asia stocks rally as Korean chips surge and oil retreat lifts sentiment
  - [china] Developing | China’s imports outpace exports in October amid efforts to tackle record surplus
  - [china] Yuan steady after dollar softens, awaits US CPI
  - [china] China's copper concentrate imports slump 11% in October as smelter woes deepen
  - [japan] Modec Inc - To Buy Back Up To 2.9% Of Own Shares Worth 10 Billion Yen
  - [china] China's iron ore imports at five-month low as thin margins dent appetite

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
      "published_utc": "2026-11-10T06:12:45+00:00",
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

