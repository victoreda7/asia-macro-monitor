atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-17T02:52:43.196780+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1080
  🇨🇳 China          874
  🇹🇼 Taiwan         335
  🇰🇷 Coreia do Sul  711

## O que já está no feed (não repita)

  - [korea] Trump touts Hyundai's US$560-mln Georgia investment pledge at campaign rally
  - [china] Philippines’ ‘China-free’ manufacturing strategy is a high-risk bet
  - [china] Europe-China Trade Truce Helps Auto Makers — Barron's
  - [japan] The Russo-Japanese War that Ryotaro Shiba did not depict in ``Clouds on the Slope''...Tax increase, Hibiya bur
  - [taiwan] Key facts: TSMC (2330) Q3 record profit; $98B capex to 2028
  - [china] Chinese premier chairs State Council executive meeting
  - [korea] [Next week's economy] Will the base interest rate be raised for the third consecutive time? Producer prices an
  - [japan] The US budget deficit is 314 trillion yen, the third highest on record due to increased interest payments, etc
  - [taiwan] Taiwan Semiconductor Posts Record Q3 Results: Time to Buy the Dip?
  - [china] China Proposes Export Controls On 23 AI Technologies Amid U.S. Tech Rivalry
  - [china] Paraguay’s tech minister defies Beijing sanctions, says Taiwan ties ‘not up for negotiation’
  - [japan] USD/JPY Near 158 as Yield Gap Support Collides With Japan’s Intervention Risk
  - [japan] Consumption tax reduction bill to be debated next week, ruling party aims to establish, opposition party clear
  - [japan] Consumption tax cut: consideration of benefits of around 5% of sales to farmers, etc.
  - [japan] US has full confidence in Takaichi's fiscal discipline: Treasury official
  - [japan] Bank of Japan Governor Ueda “will not tolerate price increases exceeding 2%” and will continue to raise intere
  - [china] Beijing seeks tighter grip on AI exports amid US rivalry
  - [china] EU to propose import curbs on other Chinese sectors, says EU chief
  - [taiwan] DA Davidson maintains Buy rating on Taiwan Semiconductor, $500 price target
  - [japan] US import prices increase; post largest annual gain in more than four years By Reuters
  - [china] European Commission to propose additional China import curbs
  - [china] China Moves to Control AI Tech Exports While Taiwan Cracks Down on Smuggling — Barrons.com
  - [japan] Bank of Japan Governor Ueda will continue to raise interest rates, 2% price stability is more important
  - [japan] TSMC's 3-nanometer semiconductor production plan in Kumamoto approved by the government
  - [korea] Seoul stocks rebound over 2% on eased chip rout, Fed bets
  - [taiwan] Legislature passes NHI senior subsidies
  - [china] China's central bank to further open its financial markets to foreigners, chief says
  - [china] China seeks tighter controls on AI-related exports amid rivalry with US
  - [japan] The underlying price increase rate is “approaching 2%”; Bank of Japan Governor Ueda says, “We cannot tolerate 
  - [china] EU urges safeguards against Chinese chemicals, machinery imports
  - [china] China’s CXMT Swings to Profit After Memory Chip Prices Surge
  - [japan] Fiscal System Council proposes use of imported rice for stockpiled rice
  - [japan] BOJ's Ueda says inflation can't be allowed to rise further
  - [japan] Bank of Japan Governor maintains interest rate hike stance, keeping a close eye on energy prices and AI demand
  - [japan] BOJ chief vows to keep raising rates, anchor inflation around target
  - [japan] Bank of Japan Governor Ueda emphasizes stance on continuing interest rate hikes: ``We cannot accept any furthe
  - [japan] Bank of Japan Governor Ueda calls upward movement in prices ``unacceptable'', approaches 2% target, continues 
  - [japan] Bank of Japan Governor Ueda calls upward price hike ``unacceptable'', approaches 2% target, continues rate hik
  - [japan] Decision on 2% underlying inflation rate will be thoroughly discussed at October meeting; economy is in line w
  - [japan] BOJ Must Ensure Underlying Inflation Doesn't Go Above 2%, Ueda Says

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
      "published_utc": "2026-10-17T02:52:43+00:00",
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

