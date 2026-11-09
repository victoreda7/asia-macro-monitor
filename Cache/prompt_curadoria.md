atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-09T06:32:44.041400+00:00
Total: 3000 manchetes

  🇯🇵 Japão          931
  🇨🇳 China          874
  🇹🇼 Taiwan         330
  🇰🇷 Coreia do Sul  865

## O que já está no feed (não repita)

  - [japan] Pola Orbis Holdings: Operating profit rose 21.3%; yen-driven FX gains lifted the FY outlook
  - [korea] Nvidia scandal raises export risks for Korean chipmakers
  - [china] China's October car exports stay resilient
  - [china] China Passenger-Car Sales Slump in October Despite Export Boom
  - [japan] Juroku Financial Group Inc - To Buy Back Up To 1.129% Own Shares Worth 5 Billion Yen
  - [japan] Mirait One Corp Says It Will Buy Back Up To 0.91% Of Own Shares Worth 2 Billion Yen
  - [japan] Mr. Ishiba and four others respond to the consumption tax reduction bill by giving their reasons for leaving t
  - [china] Exclusive-Chinese banks boost dollar deposit rates, sources say, as Beijing seeks to smooth yuan rally
  - [china] China extends suspensions of 24% tariff on US goods, port fees on US ships for two months
  - [japan] Record retail JGB demand signals bets Japan yields are peaking
  - [china] China Faces Deflationary Risks in 2027 Even if Oil Prices Normalize — Market Talk
  - [korea] Korean food exporters sign $15 million in preliminary deals at Melbourne fair
  - [korea] Woori Financial Group: "The direct impact of the U.S. midterm elections is limited... The Bank of Korea will r
  - [korea] Nvidia, SK Telecom, Rebellions forge AI chip alliance
  - [japan] Berkshire plans second yen-denominated bond offering of 2026
  - [china] China extends suspension of 24 pct additional tariff on U.S. goods for two months
  - [china] China's October car exports stay resilient, falling domestic sales yet to hit bottom
  - [japan] Consumption Activity Index
  - [china] China's Inflation Likely to Remain Low Next Year — Market Talk
  - [china] The central bank launched a 182 billion yuan reverse repurchase operation on November 9, with a net withdrawal
  - [japan] Japan bought yen at record pace in July
  - [china] China Extends Pause on 24% US Tariffs to January, Keeps 10% Rate
  - [china] Asia FX gains as dollar steadies after strong U.S. jobs data; China CPI in focus
  - [china] China, Hong Kong stocks edge up as State Council vows to stabilise market
  - [korea] Citibank, 'Early interest rate cut when semiconductor exports slow'...suggesting policy changes in the second 
  - [china] China's CPI Data Shows Domestic Demand Remains Weak — Market Talk
  - [china] China’s factory-gate inflation at fastest in nearly 4-1/2 years in October, while CPI rise moderates
  - [china] China Producer Inflation Accelerates to Over Four-Year High — Update
  - [china] China's yuan holds steady as seasonal FX sales offset dollar strength
  - [taiwan] UKSC highlights three UK semiconductor strengths for Taiwan
  - [china] China October consumer price index +0.7% 1% lower for 4th consecutive month
  - [japan] Mitsui O.S.K Q2 profit flat as higher shipping rates, weak yen boost revenue
  - [taiwan] Malaysia-Taiwan fraying ties threaten future chip investments
  - [japan] Mitsui Chemicals to Acquire JSR With Development Bank of Japan for $8.8 Billion
  - [japan] Japan Spent Record $50 Billion in Single Day to Bolster Yen
  - [china] Decision Effective 1:01 p.m. Local Time Tuesday, Customs Tariff Commission of the State Council Says
  - [china] China to Continue to Suspend 24% Additional Tariff on U.S. Goods for Two Months
  - [china] China to Retain 10% Additional Tariff Rate on U.S. Goods for Two Months
  - [china] Chinese consumer prices rise 0.7%, domestic demand slumps, below 1% for 4 consecutive months October (Jiji Pre
  - [china] China's October price rise of 0.7%, growth rate slowing (Kyodo News)

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
      "published_utc": "2026-11-09T06:32:44+00:00",
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

