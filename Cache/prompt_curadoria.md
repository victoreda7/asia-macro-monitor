atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-28T12:32:46.524354+00:00
Total: 3000 manchetes

  🇯🇵 Japão          918
  🇨🇳 China          834
  🇹🇼 Taiwan         391
  🇰🇷 Coreia do Sul  857

## O que já está no feed (não repita)

  - [taiwan] Taiwan Semiconductor raising prices could mean less competition from Intel: Wedbush
  - [korea] Lynx sees SK Hynix results rekindling interest in this chip stock
  - [korea] SK hynix Is Maintained at Buy by Rosenblatt
  - [korea] SK Hynix vai retornar US$75 bi aos acionistas após lucro recorde
  - [korea] SK hynix Inc. reports results for the quarter ended September 30 - Earnings Summary
  - [korea] Rosenblatt maintains Buy rating on SK hynix, $400 price target
  - [china] China Nonferrous Metal Industry's Foreign Engineering And Construction's Q3 New Contracts Total 3.2 Billion Yu
  - [china] Changjiang Publishing & Media Q3 Net Profit At 317.4 Million Yuan
  - [china] Yunnan Coal & Energy Q3 Net Loss At 397.8 Million Yuan
  - [japan] Finance Minister: Consumption tax cut “Support measures for farmers will be materialized during the budget for
  - [japan] Japan-Germany Summit Meeting Prime Minister: “We want to deepen cooperation as premium partners”
  - [taiwan] Taiwan's UMC Q3 revenue rises on wafer shipments growth
  - [taiwan] BRIEF-United Microelectronics Q3 Revenue TWD 74,240 Million
  - [korea] Asia report: SK Hynix leads chip rally after record profits
  - [korea] Nasdaq Futures Rise as SK Hynix Boosts Chip Sector Ahead of Fed Decision, Earnings Release
  - [korea] Nasdaq futures gain as SK Hynix lifts chips ahead of Fed decision, earnings
  - [china] Zhejiang Zheneng Electric Power Q3 Net Loss At 56.8 Million Yuan
  - [korea] SK hynix Price Target Maintained With a $250.00/Share by Cantor Fitzgerald
  - [korea] Micron Stock Pops as Rival SK Hynix Fuels AI Frenzy With Two Bombshells — Barrons.com
  - [china] China's September net gold imports via Hong Kong hit five-month high in September
  - [korea] Cantor Fitzgerald reiterates Overweight rating on SK hynix, $250 price target
  - [china] Shenzhen Edadoc Technology's Unit Plans To Invest About 1 Billion Yuan In PCB Project
  - [korea] SK Hynix delivered on third-quarter results - but the outlook is what really mattered to Wall Street and the A
  - [korea] SK hynix Is Maintained at Buy by Needham
  - [korea] Needham maintains Buy rating on SK hynix, $235 price target
  - [japan] Sales of Leqembi® totaled 32.2 billion yen in the third quarter 2026
  - [china] Shandong Gold Mining Q3 Net Loss At 362.5 Million Yuan
  - [korea] AM Markets Need to Know: SK Hynix surges on record profit, U.S.-Russia weigh oil deals, and more
  - [korea] [Economic Odyssey] Bank of Korea freezes base interest rate...What will be your choice for November?
  - [korea] Alphabet, Microsoft, SK Hynix, Robinhood, and More Stocks That Explain Today's Market — Barrons.com
  - [china] Moore Threads Tech Q3 Net Profit At 49.3 Million Yuan
  - [china] China's September net gold imports via Hong Kong rise over 28% m/m
  - [korea] Nasdaq futures rise as SK Hynix boosts chips before Fed decision, earnings
  - [korea] AI memory, chip stocks gain after SK Hynix posts record profit
  - [china] China Hainan Rubber Industry Group: Rubber-price gains and cost cuts supported Q3, but 9M revenue fell 22.28%
  - [taiwan] Ex-TSMC CTO says Taiwan's research institutes get too much funding and train too little talent
  - [korea] NPS sets sights on Silicon Valley startups, tightens risk control on AI bets
  - [korea] Finance minister hopes for Bloomberg review of S. Korea's market status
  - [korea] SK Hynix announced its plan to return more than KRW 60 trillion to additional shareholders within th..
  - [korea] S. Korean won sharply weakens against US dollar

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
      "published_utc": "2026-10-28T12:32:46+00:00",
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

