atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-03T06:42:43.577823+00:00
Total: 3000 manchetes

  🇯🇵 Japão          898
  🇨🇳 China          867
  🇹🇼 Taiwan         357
  🇰🇷 Coreia do Sul  878

## O que já está no feed (não repita)

  - [china] China's State Council removes Winnie Ho from HKSAR gov't post
  - [korea] Kospi Falls as Energy, Shipping, Chip Stocks Retreat
  - [china] The central bank stabilizes the exchange rate and then takes action to raise the foreign exchange deposit rese
  - [korea] Dawon Nexview To Acquire Real Estate Worth 17 Billion Won
  - [japan] Parkway Life Real Estate Investment Trust: Singapore rent growth lifted distributions as Japan FX pressure off
  - [china] Yuan Weakens as PBOC Signals Discomfort With Rapid Gains
  - [korea] Hanwha brings Korean defense, manufacturing ETFs to Abu Dhabi
  - [korea] Korea Inflation Could Gradually Return to BOK's Target Through 2027 — Market Talk
  - [china] China's steady thermal coal imports mask supply shifts amid El Nino: Russell
  - [korea] US midterm elections·Household loan variables... Bank of Korea, final weighing of interest rate hike
  - [korea] Asia Paper Manufacturing Co Ltd To Cancel 7.4 Billion Won Worth Of Own Shares
  - [china] Chinese stocks drop as policy measures disappoint, but yuan rally halted
  - [china] The central bank steps to ease the pressure on RMB appreciation and raises the foreign exchange deposit reserv
  - [china] Offshore Yuan Weakens After PBOC Moves to Cool Currency Rally
  - [korea] SK Hynix tests SMA(50) cloud resistance after Double Bottom: Live
  - [korea] The Bank of Korea said, “Inflation in November is also in the upper 2% range”… Will there be a further increas
  - [china] China's central bank conducts 100 billion yuan of swap operations
  - [china] China Talks Up Market Openness While Steering Stocks and Yuan
  - [china] Why is the Chinese Yuan falling today?
  - [taiwan] TSMC's next US chip plant could land in Sherman
  - [korea] South Korean Won Recovers as Oil Prices Retreat
  - [china] Asian currencies mixed as yuan slides after PBOC move, won rebounds
  - [china] PBOC's Forex Deposit Move Underscores Focus on Controlled Yuan Appreciation — Market Talk
  - [china] Meituan Unveils New AI Model Trained on Homegrown Chips
  - [china] Yuan set for biggest daily drop in 6 months after PBOC raises FX RRR
  - [china] China's Consumer Inflation Likely Eased in October — Market Talk
  - [china] The central bank launched 621 billion yuan in overnight reverse repos on November 3, with a net withdrawal of 
  - [china] China's top trade negotiator meets with US agricultural trade delegation
  - [china] For the first time in nearly five years! The central bank raised the foreign exchange deposit reserve ratio by
  - [china] After the RMB rose above 6.65, the central bank raised the foreign exchange deposit reserve ratio to 6% for th
  - [china] China's central bank raises foreign exchange reserve ratio to ease pressure on RMB appreciation | Cross-Strait
  - [china] PBoC to Raise FX Reserve Requirement to 6%
  - [china] The central bank takes action! The foreign exchange reserve ratio was raised by 2 percentage points, and the o
  - [japan] Aeon subsidiary Ministop suddenly goes into the red...The biggest factor behind the expected surplus of 1.5 bi
  - [korea] Youngwoo DSP, a company specializing in semiconductor and display equipment, recorded a good perform..
  - [china] Offshore Yuan Slides as PBOC Acts to Curb Rally
  - [korea] “So you’ve been waiting only for shareholder returns from Samsung Electronics and SK Hynix?” ... A policy that
  - [korea] Asian currencies mostly lower; South Korean won bucks trend
  - [korea] Consumer price inflation rate 2.8% in October Processed food and eating out costs rise = South Korea
  - [china] Iron ore dips on higher shipments, sluggish China demand

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
      "published_utc": "2026-11-03T06:42:43+00:00",
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

