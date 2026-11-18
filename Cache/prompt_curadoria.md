atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-18T07:12:51.884906+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1025
  🇨🇳 China          910
  🇹🇼 Taiwan         304
  🇰🇷 Coreia do Sul  761

## O que já está no feed (não repita)

  - [japan] Finance Minister Katayama: “A flat tax cut is not appropriate as it could affect social security.”
  - [china] Table: King Yuan Electronics 3Q Net Profit NT$2.64B Vs NT$2.30B
  - [korea] S.Korean pension funds dump SK Hynix, rotate into Samsung and defensive plays
  - [china] Chinese steel imports remain a threat to Indian industry, Tata Steel CEO says
  - [korea] S. Korea's state-run think tank raises growth outlook to 3.8 pct for 2026
  - [korea] "Fill in all the gaps in the sky"... Hanwha Systems Exports Short-Sleeve AESA Radar to U.S. for the First Time
  - [korea] Kospi Snaps Four-Session Losing Streak; Chip Stocks Rebound
  - [japan] 10-Year JGB Yield Projected Around 2.9% in Three Months — Market Talk
  - [china] Clampdown on China Chip Loophole Puts Billions in Loans at Risk
  - [japan] Yen Likely to Strengthen Next Year as Fed Hike Bets Ease — Market Talk
  - [japan] Auction Result of 20-Year JGBs on November 18, 2026 (For JGB Market Special Participants)
  - [korea] South Korea’s chip boom bypasses retail investors as stock rout hits spending
  - [korea] Asian markets trade mixed as Nvidia earnings lift Kospi and Nikkei; Hong Kong slips on US chip curbs
  - [taiwan] Profet AI sees AI agents easing Taiwan manufacturers' talent bottleneck
  - [japan] Yen Intervention Likely Still Some Way Off — Market Talk
  - [china] China's October youth jobless rate falls to 17.2%
  - [japan] Japan posts smaller-than-expected JPY 476.5B trade deficit in October as exports hit record high
  - [japan] Japan Likely to Remain in Trade Deficit Amid Mideast Uncertainty — Market Talk
  - [china] U.S. Chip Curbs Could Accelerate China Advanced Memory Investment Cycle — Market Talk
  - [china] Tata Steel CEO Says Chinese Imports Always A Threat; Steel Body In Ongoing Talks With Government
  - [korea] Samsung Electronics executive says more to consider on shareholder return
  - [china] On November 18, the central bank launched 700.2 billion yuan in overnight reverse repos, with a net withdrawal
  - [china] China's AI Chip Vendors to Gain From U.S. Chip Curbs — Market Talk
  - [japan] [Topical topics on Yahoo! Comments] ``Doubts about the effectiveness of active fiscal policy and consumption t
  - [china] Yuan dips, holds bullish outlook on bigger role in regional trade
  - [japan] Bank of Japan governor says central bank should keep raising rates
  - [china] Interim Nvidia CEO Says It’s No Longer Sending AI Chips to China
  - [china] UBS Group Sees Yuan Rising to 6.25 in Most Bullish Market Call
  - [china] PBOC Sets Strongest Yuan Fix Since 2022 to Allow Further Gains
  - [china] China's October fuel exports slowed on month but still topped last year's monthly average
  - [china] China's September grain, sugar and pork imports
  - [taiwan] Taiwan Semiconductor (TSM) Stock Trending After Nvidia Posts Strong Q3 Results: What You Should Know
  - [japan] Auction Result of 20-Year JGBs on November 18, 2026
  - [japan] Japan's Orix To Acquire Recruit Holdings' Online Learning Business For About 60 Billion Yen, Nikkei Says
  - [china] Xi and Putin blast sanctions before meeting Trump in China
  - [japan] Japan's Underlying Economic Growth Likely Resilient, Unlikely to Alter BOJ's Policy Outlook — Market Talk
  - [korea] South Korean State Think Tank Raises Growth Forecasts
  - [japan] Stock prices fall, sell orders related to AI and semiconductors
  - [korea] South Korean State Think-Tank KDI Raises GDP Forecasts
  - [korea] Household debt in the third quarter surpassed KRW 2030 trillion, a new record. However, the increase..

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
      "published_utc": "2026-11-18T07:12:52+00:00",
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

