atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-30T16:02:43.159966+00:00
Total: 3000 manchetes

  🇯🇵 Japão          920
  🇨🇳 China          861
  🇹🇼 Taiwan         362
  🇰🇷 Coreia do Sul  857

## O que já está no feed (não repita)

  - [korea] Why are Micron, SK Hynix, and SanDisk stocks falling on Friday?
  - [japan] Bank of Japan judges that inflation rate will reach 2%; future focus will be on countering upside risks...Gove
  - [korea] Why is SK hynix stock sliding today?
  - [china] IR: Strong orders and higher guidance offset China pricing pressure and inflation headwinds
  - [china] Overnight reverse repurchase is "on the job", and the policy interest rate has officially changed its anchor
  - [taiwan] Belarusian potash exports blocked POLITICO: US pressures Lithuania to open transportation | International
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Announcement on behalf of subsidiary FII
  - [taiwan] Intel plunges 25%, triggers global chip rout on bleak outlook
  - [china] China Publishing & Media Q3 Net Loss At 1.0 Million Yuan
  - [china] Chongqing Afari Technology Q3 Net Loss At 1.8 Million Yuan
  - [korea] Hyundai Motor Company Stock 12‑Month Price Target Cut to KRW 552483.87, Implies 89% Upside
  - [japan] When will the Bank of Japan raise interest rates next? Will the policy interest rate exceed 2%? #Expert Topi (
  - [china] News Analysis: What China's new consumption trends say about its economy
  - [china] Central Bank: Conduct bidding for overnight reverse repurchase operations every working day
  - [china] Big announcement from the central bank! It will officially come into effect next Monday!
  - [taiwan] 113 port dockworkers around the world join anti-war strikes to protest shipping arms exports | International
  - [japan] BOJ says 2% inflation target generally achieved, maintains policy rate
  - [korea] Clues Point to Familiar Culprit in Massive Binance Crypto Heist: North Korea — WSJ
  - [japan] [Emin Yilmaz talks] What will happen? The future of Japanese stocks/Is it a waste to just rely on Orkan? / Cur
  - [japan] Japan govt. to spend another $7.3 bil. on fuel subsidy
  - [japan] Fixed mortgage interest rates to be lowered by four major banks starting in November
  - [taiwan] Taiwan Q3 GDP growth hits 14.36%, highest in 48 years
  - [japan] Bank of Japan Governor Ueda says price stability target “reached 2%” and leaves policy interest rate unchanged
  - [china] The central bank officially announced that the policy interest rate has officially "changed the anchor", and t
  - [japan] Chief Cabinet Secretary Kihara: “We hope for appropriate monetary policy management” Bank of Japan’s “2% price
  - [china] Central Bank: Starting from November 2, bidding for overnight reverse repurchase operations will be carried ou
  - [japan] September crude oil imports decreased for the first time in four months, possibly due to pipeline suspensions
  - [taiwan] Intel warning sparks chip rout as PC weakness clouds turnaround
  - [china] The central bank announced important adjustments, which will be implemented starting next week!
  - [japan] Asia report: Tech stocks tumble on AI fears as BoJ holds rates
  - [japan] Japanese Yen Gains Modest as BOJ Rate-Rise Prospects Well Priced — Market Talk
  - [japan] BOJ stays pat on rates, signals inflation target reached
  - [china] The central bank announced! Overnight reverse repurchase will be carried out every working day starting next w
  - [china] Central Asia’s Fastest Growing Economy Plans Yuan Bond in 2027
  - [china] Important adjustments from the central bank will be implemented starting next week
  - [japan] Angle: Bank of Japan continues to raise interest rates to keep the underlying price level at 2%. Is the “next 
  - [china] Memory Crunch Cements CXMT as China's Chip Champion — Update
  - [china] The central bank releases important information
  - [japan] Nxera Pharma: 9M profitability advances the JPY 50bn 2030 revenue ambition, with milestone timing a key variab
  - [taiwan] Tainan station tightens rules for popular public piano

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
      "published_utc": "2026-10-30T16:02:43+00:00",
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

