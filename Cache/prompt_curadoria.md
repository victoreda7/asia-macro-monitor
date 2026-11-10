atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-10T07:52:44.191112+00:00
Total: 3000 manchetes

  🇯🇵 Japão          936
  🇨🇳 China          894
  🇹🇼 Taiwan         313
  🇰🇷 Coreia do Sul  857

## O que já está no feed (não repita)

  - [japan] BOJ's October meeting calls for ``raise interest rates when possible'' to reach 2% price
  - [japan] Consumption tax reduction bill to be debated in the House of Councilors tomorrow; ruling and opposition partie
  - [korea] Louis Vuitton hit by stock slump, stronger won in South Korea
  - [china] China's trade surplus soars past $1 trillion as AI boom powers exports
  - [china] Table: Chun Yuan Steel Industry Oct Rev NT$2.02B Vs NT$2.01B
  - [japan] SoftBank Group interim financial results final deficit of 768 billion yen
  - [korea] South Korean shares rebound as chipmaker track US peers
  - [japan] Aichi Financial Group Inc - To Buy Back Up To 0.9% Of Own Shares Worth 3 Billion Yen
  - [taiwan] TSMC October Revenue Jumps 60% Y-o-Y
  - [taiwan] Zhongke's exports in the first nine months exceeded 758.5 ​​billion, and its annual revenue is expected to exc
  - [taiwan] REG - Nexteq PLC - Taiwan property sale and trading update
  - [china] Fund sellers, China buyers squeeze copper's tariff trade: Andy Home
  - [china] Huang Jen-Hsun’s extramarital affair raises national security concerns Chinese scholar: U.S. exports of AI chi
  - [china] In Depth: CEO’s Affair Pulls Nvidia Deeper Into the U.S.-China Chip Fight
  - [japan] Honda raises full-year profit forecast as weak yen trumps costly EV retreat
  - [china] China Opens Onshore Forex Market to Overseas Yuan Clearing Banks
  - [korea] Asia stocks rally as Korean chips surge and oil retreat lifts sentiment
  - [japan] BREAKING NEWS: SoftBank Group logs net loss of 768 bil. yen in April-Sept.
  - [korea] Kospi Snaps Three-Session Losing Streak; Chip, Airline Stocks Advance
  - [taiwan] TSMC October revenue jumps nearly 60% on strong AI chip demand
  - [taiwan] TSMC October 2026 revenue surges 59.7% on strong AI chip demand
  - [china] China exports stay brisk as annual trade surplus tops $1tn
  - [china] China puts yuan within easier reach of Africa, but adoption faces major hurdles: report
  - [taiwan] TSMC Oct revenue jumps 60% as AI-fueled demand remains strong
  - [taiwan] TSMC: Revenue for January-October Totaled NT$4.485T, Up 43% on Year >2330.TW
  - [taiwan] TSMC: Revenue for October Totaled NT$586.89B, Up 15% From September >2330.TW
  - [taiwan] TSMC Revenue Rose 60% on Year in October >2330.TW
  - [japan] The current account surplus in the first half of this fiscal year is the second largest on record.
  - [japan] TOMY Company: Japan and Asia growth lifted Q1 profit; Americas shipments were hit by ERP delays
  - [korea] How Posco fortifies Korea's energy, battery supply chains
  - [china] Asian stocks rally on US tech rebound; China trade surplus hits $105B in October
  - [korea] Semiconductor exports influence the Bank of Korea’s interest rate… Expected to be lowered by 3.5% during a boo
  - [japan] The Hyakujushi Bank - To Buy Back Up To 1.76% Own Shares Worth 3 Bln Yen
  - [japan] President Keiko Fujimori of Peru, South America, to visit Japan; coordination of summit meeting on 20th
  - [taiwan] Table: Taiwan Semiconductor Mfg Oct Rev NT$586.89B Vs NT$367.47B
  - [japan] If rejected in the House of Councilors, will the consumption tax be dissolved? The reality of the scenario in 
  - [china] Shanghai Electric Integrates Industrial AI into Heavy-Duty Gas Turbine Manufacturing and Lifecycle Services
  - [china] China's exports in October increased by 35.2% year-on-year, beating expectations. The surplus in the previous 
  - [japan] JGB yields rise after 30-year auction draws weak demand
  - [china] Alice Huang, Chinese businesswoman tied to Nvidia CEO, went from finance to chips

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
      "published_utc": "2026-11-10T07:52:44+00:00",
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

