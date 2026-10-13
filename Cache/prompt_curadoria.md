atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-13T21:02:43.701017+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1137
  🇨🇳 China          831
  🇹🇼 Taiwan         298
  🇰🇷 Coreia do Sul  734

## O que já está no feed (não repita)

  - [taiwan] TSMC Stocks Slip as Thursday's Earnings Put AI Margins Under Scrutiny
  - [japan] I gave up on curry, the salmon roe bowl was in the red, and I finally opened 30 stores nationwide with "Pork C
  - [japan] 77% feel anxious about leaking personal information NHK poll
  - [china] Micron Stock Is Falling. Elon Musk's Comments on Chinese Chips Aren't Helping. — Barrons.com
  - [china] China’s Growth Seen Edging Up to 4.4% as Exports Offset Weak Demand
  - [china] China’s Magnet Export Crackdown Is Putting Companies Like Evolution Metals in the Spotlight (NASDAQ: EMAT)
  - [korea] Chip Stocks Slide as South Korea's KOSPI Plunges, J&J Sinks 6%: Stock Market Today
  - [korea] 'Brutal session' for chip stocks shows AI trade is turning
  - [korea] Seoul shares dip over 5% on tech sell-off on renewed AI, inflation woes
  - [japan] Japan looks for off-ramp from Trump's ICC feud before US sanctions kick in
  - [korea] Korea launches chip policy office to fast-track W800tr investments
  - [china] Shares of U.S. chip companies extend decline as China memory report and concerns about AI spending hit the sec
  - [china] US chip stocks extend slide as China memory report, AI spending jitters hit sector
  - [china] 'If you can't beat them, join them': Uday Kotak backs China investment, manufacturing JVs in India
  - [japan] Yen Rises After BoJ Ueda Comments
  - [japan] Yen Rises Against Majors
  - [korea] Kospi tumbles as chip rout deepens, briefly breaking below 6,000
  - [korea] Roze AI Announces Approximately US$14.8 Million (KRW 19.88 Billion) in New Contracts for AI-Powered Fire Risk 
  - [korea] SK Hynix Stock Crashes 9% as AI Fears Trigger Asian Tech Sell-Off
  - [china] Nvidia Loses Ground in China as AI Chip Shipments Plunge 44%
  - [china] Long before his Nobel win, Michael Woodford was influencing China’s central bank
  - [taiwan] Qnity Bets On Local Production To Win More AI Chip Business From Nvidia, TSMC – CEO Touts ‘Local-For-Local’ St
  - [korea] Bank of Korea Gov. Shin Makes Case for Forward Guidance That Preserves Flexibility
  - [korea] IMF raises S. Korea's growth forecast to 3.3% amid chip supercycle
  - [korea] Bank of Korea chief says monetary policy to stay restrictive for now
  - [taiwan] Taiwan Semiconductor Manufacturing Company Limited expected to post earnings of $4.50 a share - Earnings Previ
  - [china] As import curbs loom, Chinese carmakers hard to miss at Paris Motor Show
  - [japan] Asia report: Nikkei, KOSPI post big losses as chipmakers drop
  - [korea] Hong Ra-hee to Gift 11.15 Million Samsung Electronics Shares to Lee Jae-yong
  - [china] E-House (China) Enterprise Says Grand Court Of Cayman Islands Sanctions Cayman Scheme
  - [china] ‘Easy money is past’: why investors are rethinking the AI memory-chip trade
  - [korea] Korean Won, New Taiwan Dollar Underperform Amid Chip-Stock Selloff — Market Talk
  - [korea] UnitedHealth, JPMorgan, Six Flags, SK Hynix, and More Stocks That Explain Today's Market — Barrons.com
  - [japan] "Cabinet approval rate" is also one of the indicators of government management
  - [japan] Support rate for each party: “Liberal Democratic Party” 35.3% “No support” 38.5% NHK public opinion poll
  - [japan] High approval rate for the city cabinet: 51%, 32% disapproval, NHK survey
  - [japan] Mapping the Market: 'Death cross' bodes more trouble for peso against resurgent yen
  - [japan] Rupee extends surge; Dollar consolidates near peaks ahead of inflation data
  - [korea] South Korea central bank to keep policy restrictive until inflation hits target, governor says
  - [china] IMF Cuts China Growth Forecasts for 2026 and 2027

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
      "published_utc": "2026-10-13T21:02:43+00:00",
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

