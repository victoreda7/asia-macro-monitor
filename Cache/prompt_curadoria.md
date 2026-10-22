atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-22T07:52:42.965090+00:00
Total: 3000 manchetes

  🇯🇵 Japão          965
  🇨🇳 China          861
  🇹🇼 Taiwan         354
  🇰🇷 Coreia do Sul  820

## O que já está no feed (não repita)

  - [japan] Japan's Daiichi Life keeps focus on yen bond swaps, expects cuts in overseas debt
  - [korea] Samsung Electro-Mechanics gets $2.8 billion chip investment from Tesla, Nvidia, report says
  - [japan] Japan's Top Labor Union Targets Big Pay Bump, in Line With BOJ Aims
  - [japan] Yen rallies as dollar slips to 3-wk low; traders eye central bank meetings
  - [japan] Yen Rises Against Majors
  - [korea] Samsung Electro-Mechanics receives investment of US$2.8 billion for the production of chips from Tesla and Nvi
  - [korea] BOK pauses in its tightening campaign with policy rates at 3%; November hike on the table
  - [japan] Developments in Real Exports and Real Imports
  - [japan] In absence of sovereign buyers, Indian chip firms find clients in Japan, EU
  - [japan] Japan's Nikkei slides as AI capex caution weighs on chip shares
  - [korea] South Korean shares log 6-month closing low as chipmakers fall on profit-taking
  - [china] Receivers to sell Shimao’s 2 Hong Kong hotels to Malaysian developer
  - [japan] Yen rallies as dollar wobbles toward Fed meeting
  - [korea] [Exclusive] Samsung Electro-Mechanics to receive 3.7 trillion won from Tesla and NVIDIA to build AI chip subst
  - [korea] BOK pauses rate hikes, but signals more may come
  - [japan] Six opposition parties in the House of Councilors consumption tax reduction bill “call for establishment of a 
  - [korea] Strong chip exports expected to spill over into private consumption from next year: BOK report
  - [japan] Singapore Dollar Gains on Yen as Carry Funder, Analysts Say
  - [china] COMMENTARY: China uses crude stockpiles, but rising oil imports may curtail draws
  - [korea] K-beauty stocks stumble as strong won squeezes profits
  - [korea] K-beauty firms to seek export deals at Cheongju expo
  - [china] The central bank launched a 173 billion yuan overnight reverse repurchase operation today, and the latest net 
  - [korea] Base interest rate frozen at 3%... Bank of Korea governor raises concerns about fiscal sustainability
  - [japan] Japan's trade deficit nearly doubles in Apr.-Sep.
  - [korea] Bank of Korea freezes base interest rate at 3.00%... Will interest rates rise again in November?
  - [korea] Kbi Dongkook Ind To Acquire Real Estate Worth 27.5 Billion Won
  - [korea] The Bank of Korea has stopped raising interest rates... Base interest rate frozen at 3% (comprehensive) - Mone
  - [korea] BOK's Hawkish Hold Leaves Door Open to Rate Hikes — Market Talk
  - [japan] October 2026 Bank of Japan Policy Meeting Preview - Organizing the highlights of this meeting [Sumitomo Mitsui
  - [korea] Nvidia taps Korean component makers for AI chips, robots
  - [korea] The Bank of Korea's Monetary Policy Committee freezes the base interest rate at 3%... Take a breath after 2 co
  - [china] China's yuan climbs to fresh 4-year high, global central bank meetings in focus
  - [korea] Bank of Korea Holds Steady After Back-to-Back Hikes — Update
  - [korea] Bank of Korea holds rates, upbeat outlook points to future hikes
  - [korea] Bank of Korea stops raising interest rates... Tightening speed control
  - [korea] (3rd LD) BOK holds rate at 3 pct after 2 straight hikes, signals continued tightening
  - [china] China snaps up Australian canola as improved ties, lower tariffs fuel demand
  - [china] The central bank plans to switch to overnight reverse repos! Dividend low-volatility ETF Huatai-PineBridge (51
  - [japan] JGB yields touch multi-week lows as traders weigh geopolitics, BOJ policy outlook
  - [china] China bets on manufactured water, and wants to sell it to the world

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
      "published_utc": "2026-10-22T07:52:43+00:00",
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

