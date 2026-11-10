atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-10T08:52:43.234663+00:00
Total: 3000 manchetes

  🇯🇵 Japão          932
  🇨🇳 China          893
  🇹🇼 Taiwan         314
  🇰🇷 Coreia do Sul  861

## O que já está no feed (não repita)

  - [china] China's Hesai Q3 revenue rises 34% as lidar shipments grow
  - [korea] Nexon axes eight projects in restructuring as S.Korean game sector tightens belt amid downturn
  - [china] ZAWYA: Can China’s zero-tariff programme offset the loss of Agoa for South African agriculture?
  - [china] Chinese investment in African manufacturing could change the world
  - [korea] Exports to large companies more than doubled in the third quarter of this year due to the semiconduc..
  - [china] Aluminium falls as surging China exports revive supply worries
  - [korea] KT received a disappointing report card. The progress of artificial intelligence (AI), real estate
  - [korea] Kospi posts biggest gain in two weeks as chips rebound, oil falls
  - [china] China’s Moonshot AI rents advanced Nvidia chips: Bloomberg
  - [japan] Yen Falls Against Majors
  - [korea] Monetary Policy Committee members who froze interest rates "check the effect of consecutive interest rate incr
  - [japan] BOJ's October meeting calls for ``raise interest rates when possible'' to reach 2% price
  - [japan] Consumption tax reduction bill to be debated in the House of Councilors tomorrow; ruling and opposition partie
  - [taiwan] TSMC's October sales soar almost 60% year-on-year to hit high
  - [taiwan] Taiwan sees US$10 billion in capital outflows in November
  - [korea] Louis Vuitton hit by stock slump, stronger won in South Korea
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
      "published_utc": "2026-11-10T08:52:43+00:00",
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

