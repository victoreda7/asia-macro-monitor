atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-21T10:22:44.673682+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1032
  🇨🇳 China          869
  🇹🇼 Taiwan         355
  🇰🇷 Coreia do Sul  744

## O que já está no feed (não repita)

  - [china] Esteve More Than $80 Million Invested To Expand And Strengthen Esteve Cdmo's Manufacturing Capabilities In Chi
  - [china] PBOC's Potential Shift to Overnight Policy Rate Appears Supportive for China Bonds — Market Talk
  - [china] Wens Foodstuff Says Q3 Net Loss At 595.5 Million Yuan
  - [korea] Producer prices up for 2nd month in Sept. on higher prices of agricultural goods
  - [china] China’s Youth Unemployment Rate Eases to 18%
  - [china] China's blue-chip index hits 14-month low as CATL tumbles, stimulus hopes fade
  - [china] China's solar curbs may accelerate India's push for domestic wafer and cell manufacturing: Report
  - [korea] Samsung, SK Hynix upgrading China fabs to make advanced NAND chips - report
  - [japan] Goldman Sachs bets on these 8 Japanese chip stocks as earnings upgrades loom
  - [taiwan] Cloud AI to drive chip growth in 2027 as Taiwan suppliers seek opportunities beyond weak consumer edge AI
  - [korea] Semiconductor stocks in South Korea and the United States are fluctuating, reacting sensitively to s..
  - [japan] Japan open to winter fuel subsidies to soften heating bill blow
  - [japan] Foreign visitors' spending in Japan hits record 7 tril. yen in Jan.-Sept.
  - [china] Indonesia's central bank kept its benchmark interest rate unchanged at 5.75% and announced it would lower bank
  - [korea] The average annual interest rate of illegal loan contracts issued by the Financial Supervisory Servi..
  - [china] Indonesia's central bank keeps its benchmark interest rate unchanged and lowers bank deposit reserve ratios
  - [taiwan] Rising Risk of Taiwan Central Bank Rate Hike — Market Talk
  - [japan] BOJ to decide at next week's meeting whether 2% inflation target reached: sources
  - [taiwan] TSMC Pauses Some Taiwan Construction After Mishap Kills Four
  - [japan] BREAKING NEWS: Foreign spending in Japan hits record 7 tril. yen in Jan.-Sept.
  - [japan] Japan futures slip as yen jumps, cost support seen easing
  - [taiwan] Taiwan semiconductor electricity use hits record high in Sept.
  - [japan] The Takaichi administration should present a "Plan B" for fiscal policy...A plan that says "achieving high gro
  - [korea] Samsung Biologics Co., Ltd. Q3 Rev KRW 1.49T; Lifts 2026 Growth Guide to 20%
  - [taiwan] Death toll in TSMC Kaohsiung construction accident rises to 4
  - [korea] South Korean shares post biggest gain in 6 weeks as chipmakers rebound
  - [japan] Will the Bank of Japan decide to reach the 2% price level? (NRI researcher's commentary on current events)
  - [korea] Ryukil C&S To Acquire Real Estate Worth 25 Billion Won
  - [korea] Kospi Regains Ground as Chip Stocks Recoup Most of Prior Session's Losses
  - [japan] Don't you feel safe even if you keep the approval rating at 50%? Yokohama, Chiyoda... The footsteps of "distur
  - [japan] One year since the Takauchi Cabinet was established, it is putting all its effort into enacting the consumptio
  - [korea] Nomura, JPMorgan bullish on Korean chips despite Kospi swings
  - [china] America, China Remain 'Fundamental' for European Spirits, Despite Tariff Turmoil — Interview
  - [korea] Samsung, SK Hynix upgrade China plants to make advanced memory chips - Reuters
  - [korea] Exclusive-Samsung, SK Hynix upgrading China plants to make more advanced chips, people say
  - [japan] Achieving the price target through appropriate monetary policy and contributing to sustainable growth - Bank o
  - [china] From now on, the central bank continues to "strengthen"
  - [korea] Capybobo: PYBOBO begins KRW trading on Bithumb - 21 Oct 2026
  - [china] China signals intent to push back against cleantech tariffs at COP31
  - [japan] BOJ’s Himino signals readiness to raise borrowing costs

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
      "published_utc": "2026-10-21T10:22:44+00:00",
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

