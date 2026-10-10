atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-10T01:12:42.950812+00:00
Total: 2987 manchetes

  🇯🇵 Japão          1204
  🇨🇳 China          818
  🇹🇼 Taiwan         277
  🇰🇷 Coreia do Sul  688

## O que já está no feed (não repita)

  - [china] Stocktwits Zero To Sixty — Tesla Shanghai Exports Shine, Texas Cybercab Fleet Scales, And Lucid Built Fewer Ca
  - [japan] Why are bankruptcies at record high due to high prices?
  - [korea] The execution rate of the information protection budget of 20 financial companies with many computer..
  - [japan] Did the Bank of Japan achieve its price target? (Hiroyuki Kubota) - Expert
  - [japan] Nakayama Kinni-kun conducts a “real” price survey at an American supermarket.Although he is surprised by the 5
  - [china] Super Micro contractor pleads guilty in scheme to divert AI servers with Nvidia chips to China
  - [korea] Prices that cannot be determined... Will the Bank of Korea and the US Federal Reserve raise the base interest 
  - [japan] Japan food tax cut gets cabinet approval with key questions unanswered
  - [china] Super Micro Contractor Pleads Guilty In Scheme To Divert Computer Servers Built With Nvidia AI Chips To China
  - [china] China and EU discuss trade conflict EU "to curb exports from China"
  - [china] The central bank uses multiple tools to protect liquidity and funds are expected to remain stable in October |
  - [japan] Japan machine tool order backlog hits all-time high on AI demand
  - [korea] BOK Financial Price Target Cut to $146.00/Share From $149.00 by RBC Capital
  - [china] China, EU strike deal to halve Chinese hybrid exports
  - [china] EU Says it Reached Understanding with China to Cut Back Hybrid Vehicle Exports — Update
  - [china] Tariffs targeting China's Temu, Shein shrink US small parcel deliveries
  - [korea] SK chief eyes Gwangju chip fabs alongside Yongin cluster
  - [china] EU-China understanding could halve Chinese hybrid car exports
  - [china] China’s Oil Imports Look Set to Rise as Supertanker Fleet Swells
  - [japan] Japan's DOGE to 'step up' spending review, eyeing EV subsidies, health checks
  - [china] China-EU trade talks yield prospect of Chinese hybrid exports halving
  - [china] Mercedes welcomes EU-China import deal for offering more predictability
  - [china] China Longyuan Power Posts Sept 2026 Power Generation Up 7.08% To 5.7 Million Mwh
  - [taiwan] OPPO To Launch Find X10 Pro Max With MediaTek 2nm Chip Globally
  - [china] China, EU strike deal to cut Chinese hybrid vehicle exports by over half
  - [china] Beijing Lets Local Governments Tap 550 Billion Yuan in Unused Debt Quotas
  - [china] EU says it agrees with China to halve hybrid vehicle exports to EU
  - [china] Developer of One Stanley pledges 6-year warranty and checks amid steel bar probe
  - [china] EU Says Accord With China Could Cut Hybrid Car Exports by Half
  - [china] EU Says China Accord Could Cut Hybrid Car Exports by Half
  - [japan] Food consumption tax reduction bill submitted to the Diet, Agriculture Minister Yan says, investigation contin
  - [taiwan] Taiwan Semiconductor's strong Q3 sales a positive sign for Q4, Wedbush says
  - [japan] Potential Tax-Free Incentive For Holding Japanese Bonds Could Help Yen — Market Talk
  - [china] China AI developers publish safety tests for just 3.6% of model releases, report finds
  - [china] China Says It Has ‘Understanding’ With EU on Hybrid Car Exports
  - [china] Ecobank to join China's CIPS payments platform for yuan settlement
  - [china] China agrees to slash EU hybrid car exports in half, putting brake on trade war
  - [china] Developing | China and EU reach ‘understanding’ on hybrid vehicles after crunch trade talks
  - [china] Breaking | China and EU reach ‘understanding’ on hybrid vehicles after crunch trade talks
  - [japan] Govt. submits bill for consumption tax cut | NHK WORLD-JAPAN News

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
      "published_utc": "2026-10-10T01:12:43+00:00",
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

