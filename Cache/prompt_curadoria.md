atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-05T07:32:44.038065+00:00
Total: 3000 manchetes

  🇯🇵 Japão          892
  🇨🇳 China          901
  🇹🇼 Taiwan         312
  🇰🇷 Coreia do Sul  895

## O que já está no feed (não repita)

  - [china] China says trade barriers block tech imports, fueling its surplus
  - [korea] KT&G: 2030 plans pair mid-to-high single-digit OP growth with KRW 5tn in regular returns
  - [korea] Samsung Electronics faces push for sixth labor union amid alleged internal rifts
  - [korea] PPP lawmakers oppose special counsel bill on 'fabricated indictments
  - [japan] Asian stocks diverge, BoJ signals further hikes and Australia's trade surplus surges
  - [japan] BREAKING NEWS: Sony Group July-Sept. net profit rises to 449.6 bil. yen
  - [japan] How long will interest rate hikes last? The Bank of Japan discusses the final goal; summary of September meeti
  - [japan] BREAKING NEWS: Sony Group April-Sept. net profit rises 38.8% to 791.76 bil. yen
  - [japan] BREAKING NEWS: Sony Group lifts FY 2026 net profit outlook to 1.33 tril. yen
  - [korea] Lee calls for virtuous cycle to translate exports growth into domestic demand recovery
  - [china] China's Inflation Likely Stable in October — Market Talk
  - [korea] BOK chief to attend BIS governors' meeting in Switzerland
  - [china] Asian FX rises as dollar slides on U.S. vote, kiwi leads gains; yuan steadies
  - [japan] BoJ Minutes signal more hikes ahead as central bank pauses at 1.25%
  - [china] China Mulls Dollar, Offshore Yuan Sovereign Bond Sale This Month
  - [japan] Toyota interim financial results: Sales and profits increase due to yen depreciation, annual forecast upwardly
  - [china] China's cleantech stocks jump as investors bet on US policy shift
  - [china] China Longyuan Power Poised for Growth in 2027 — Market Talk
  - [japan] Japan services PMI rises to 51.7 in October; composite growth slows to 5-month low
  - [china] China Longyuan Power Raised to Buy From Neutral by Citigroup >0916.HK
  - [korea] The Export-Import Bank of Korea has signed a $170 million foreign economic cooperation fund (EDCF) l..
  - [japan] Soda Nikka Co Ltd - To Buy Back Up To 4.37% Own Shares Worth 1.6 Billion Yen
  - [japan] Upward price fluctuation risk, interest rate hike appropriate, policy “change in phase” Bank of Japan Septembe
  - [korea] SK hynix puts Chey Tae-won at helm of $10b US AI investment arm
  - [japan] Japan bond yields fall as lower oil prices ease inflation concerns
  - [korea] South Korea finance minister vows to monitor AI policy changes after US midterm elections
  - [japan] Inabata & Co Ltd - To Buy Back Up To 1.86% Own Shares Worth 5.4 Billion Yen
  - [japan] BREAKING NEWS: Toyota lowers FY 2026 sales outlook to 53.5 tril. yen
  - [china] Copper Finds Support Amid Tightening Supply in China
  - [japan] Kh Neochem Co., Ltd. - To Buy Back Up To 10.52% Of Own Shares Worth 12 Billion Yen
  - [japan] BREAKING NEWS: Toyota raises FY 2026 net profit outlook to 3.57 tril. yen
  - [japan] Nof Corp - To Buy Back Up To 0.94% Of Own Shares Worth 5 Billion Yen
  - [japan] Toyota - To Buy Back Up To 5.18% Of Shares Worth 1.3 Trln Yen Versus Up To 1 Trln Yen Planned Previously
  - [china] Chipmaker YMTC's IPO on hold as China tightens share sale approvals, sources say
  - [korea] LG Chem: Q3 sales rose, but a KRW 600bn net loss reflected uneven segment performance
  - [korea] South Korean Won Weakens on Foreign Outflows
  - [japan] "Increasing the burden on aesthetic medical institutions to reduce 'naobi'", the Ministry of Finance proposes 
  - [japan] At the Bank of Japan's September interest rate hike meeting, there was an opinion that the pace should be acce
  - [japan] Sato Sho-Ji Corp - To Buy Back Up To 1.45% Of Own Shares Worth 900 Million Yen
  - [japan] Finance Directors’ Meeting leaves economic outlook unchanged as “moderate recovery”

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
      "published_utc": "2026-11-05T07:32:44+00:00",
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

