atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-07T21:12:46.302004+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1263
  🇨🇳 China          782
  🇹🇼 Taiwan         273
  🇰🇷 Coreia do Sul  682

## O que já está no feed (não repita)

  - [china] Zoom CEO Eric Yuan sells $2.27 million in NASDAQ:ZM stock
  - [japan] NGK President Kobayashi ``Concentrates investment in the semiconductor manufacturing field''...Withdrawal from
  - [taiwan] Caterpillar, Intel, TSMC, Micron, SpaceX, HPE, and More Stocks That Explain Today's Market — Barrons.com
  - [japan] Representative question from today in the House of Councilors, debate over consumption tax cut, investigation 
  - [japan] <Our original business is pumps> Ebara's entry into semiconductor equipment was a "historical necessity"; the 
  - [korea] Samsung Electronics to pay chip division special bonus in spring 2027
  - [korea] AMD’s Lisa Su Visits South Korea, Reportedly Discusses AI Collaboration With Samsung, SK Hynix
  - [japan] Australia will buy Japan frigates despite budget cuts: finance chief
  - [japan] Fed Used Treasury Funds to Support Yen in Joint Intervention
  - [japan] Japan bank to connect small businesses with US AI developers
  - [taiwan] Taiwan's US envoy says ties robust after Trump-Xi summit
  - [korea] SK Hynix Stocks Drop 2.8% Despite AMD's Multi-Generation HBM Plan
  - [china] The Fed's overnight reverse repurchase agreement (RRP) usage on Wednesday was $2.338 billion
  - [china] China rejects EU request for voluntary hybrid car export curbs, FT reports
  - [china] China slaps down EU request for voluntary curbs on hybrid car exports
  - [japan] Japan Pushes Local 5G Manufacturing, Digital Infrastructure In India
  - [korea] Samsung’s HBM prices tipped to more than double in 2027
  - [japan] Central Bank of India raises interest rates for the first time in 3 years and 8 months against the backdrop of
  - [taiwan] Intel stays in Musk's Terafab plan as TSMC joins the mix
  - [korea] Lotte Biologics expands US manufacturing partnership with Alvotech
  - [taiwan] Micron Tech chipmaker union in Taiwan gets OK to strike
  - [korea] AMD’s Lisa Su calls chips ‘team sport’ as Samsung, SK hynix ties deepen
  - [taiwan] SpaceX, Intel, TSMC, Webull, Fair Isaac, and More Stocks That Explain Today's Market — Barrons.com
  - [china] Why China’s export engine may hit a ceiling as trading partners face limits
  - [korea] The number of hacking attempts targeting the Export-Import Bank of Korea this year was nearly eight
  - [china] EU seeks to cut trade deficit with China in talks with Beijing
  - [japan] Yen Rises After BoJ Sato's Hawkish Remarks
  - [china] Tozed Kangwei To Issue 36.45 Mln Shares, Raising 979.8 Mln Yuan In Shenzhen Listing
  - [taiwan] TSMC earnings could cause another round of consensus upgrades
  - [japan] Yen Rises Against Majors
  - [taiwan] Intel Stock Is Defying the Chip Slump as Musk Explains TSMC Role in AI Project — Barrons.com
  - [china] UK proposes duty on imports of Chinese rutile titanium dioxide
  - [china] China Warns EU It Has Tools Ready If Trade Tensions Escalate
  - [japan] Ritsumeikan summarizes the concept of "immediate payment within this fiscal year" regarding consumption tax re
  - [korea] Samsung's Q3 profit seen jumping nine-fold, but chip margins may be flat
  - [korea] Korea to strengthen food safety ties, support exports to Latin America
  - [japan] BREAKING NEWS: Takaichi vows proper budget distribution amid farm minister controversy
  - [korea] Finance minister pledges to create favorable biz environment amid challenges
  - [taiwan] Micron Taoyuan union secures strike authorization, weighs 'surprise strike'
  - [taiwan] SpaceX, TSMC, Constellation Brands, FICO, and More Stocks That Explain Today's Market — Barrons.com

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
      "published_utc": "2026-10-07T21:12:46+00:00",
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

