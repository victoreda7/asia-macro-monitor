atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-31T01:22:42.242791+00:00
Total: 3000 manchetes

  🇯🇵 Japão          923
  🇨🇳 China          867
  🇹🇼 Taiwan         359
  🇰🇷 Coreia do Sul  851

## O que já está no feed (não repita)

  - [china] The policy interest rate "changes the anchor" and the central bank will conduct overnight reverse repurchase o
  - [taiwan] TSIA 30: The manpower problem behind Taiwan's semiconductor resilience
  - [taiwan] TSIA 30: AI is breaking the sequential supply chain — Taiwan may be built for what comes next
  - [taiwan] Good Morning World》Taiwan’s export investment exceeded expectations. The economic growth rate in the third qua
  - [china] The central bank officially announced that the policy interest rate has officially "changed the anchor", exper
  - [japan] German Chancellor Merz worries about EV incentives to be considered at EU summit meeting
  - [japan] Tokyo Electron Ltd. Stock 12‑Month Price Target Raised to JPY 16138.18, Implies 61% Upside
  - [korea] Hyundai Motor Company Stock 12‑Month Price Target Cut to KRW 548612.9, Implies 88% Upside
  - [japan] Bank of Japan plans to raise interest rates in December, aims for neutral interest rate as inflation rises (Ji
  - [korea] North Korea says sanctions don't work to deny its status as nuclear weapons state
  - [japan] The Takaichi administration's theory of a ``bad yen depreciation'' due to fiscal expansion is wrong - Why we s
  - [japan] NY foreign exchange market = Yen rises for 3rd day, Bank of Japan leaves interest rates unchanged, emphasizes 
  - [taiwan] Intel on course for worst day ever, triggers global chip rout
  - [japan] Bank of Japan announces “underlying inflation rate” to reach 2%; ability to suppress upward swings in prices a
  - [japan] Interest rates rise due to coreweave shock... What will happen to the Nikkei Stock Average, which fell sharply
  - [japan] Dollar rises for October as rate hike bets remain elevated, euro and yen slip
  - [japan] Yen set for third straight daily gain against dollar after BOJ holds rates
  - [taiwan] Foxconn unveils 3 EVs to grow contract manufacturing business
  - [japan] Ruling party looks for voting schedule on consumption tax reduction bill Opposition party urges Prime Minister
  - [japan] Bank of Japan will shift focus to fixation once prices reach 2%; focus on how to proceed with interest rate hi
  - [korea] Samsung Stocks Decline 3% With Semiconductor Profit Concentration in Focus
  - [korea] SK Hynix Stocks Decline 7.1% With Long-Term Memory Contracts in Focus
  - [korea] Hyundai Motor Company Stock 12‑Month Price Target Cut to KRW 549580.65, Implies 88% Upside
  - [china] The central bank optimizes the short-end interest rate control mechanism and will carry out overnight reverse 
  - [china] Chinese Inverter Makers Reassess U.S. Business as Restrictions Tighten
  - [japan] Japan's Omron eyes India as export base for blood pressure monitors
  - [japan] Bank of Japan's price increase rate reaches 2% for the first time in 14 years 1,500 food items will have price
  - [japan] Japan's Sojitz to import rare earth yttrium from Malaysia
  - [china] Focus Observation | Why can the 1.25% overnight reverse repurchase rate be understood as an interest rate cut?
  - [china] China's State Council studies guiding principles of key Party plenum
  - [china] Weyerhaeuser expects to triple China log shipments in fourth quarter
  - [china] BYD Company Limited Class A Stock 12‑Month Price Target Cut to CNY 107.97, Implies 31% Upside
  - [japan] Panasonic: AI demand lifts FY 2027 AOP forecast to JPY 780 billion as all segments post record Q2 profit
  - [china] China's State Council appoints, removes officials
  - [korea] Why did Micron, SK Hynix and SanDisk shares fall on Friday?
  - [korea] Why are Micron, SK Hynix, and SanDisk stocks falling on Friday?
  - [japan] Bank of Japan judges that inflation rate will reach 2%; future focus will be on countering upside risks...Gove
  - [korea] Why is SK hynix stock sliding today?
  - [china] IR: Strong orders and higher guidance offset China pricing pressure and inflation headwinds
  - [china] Overnight reverse repurchase is "on the job", and the policy interest rate has officially changed its anchor

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
      "published_utc": "2026-10-31T01:22:42+00:00",
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

