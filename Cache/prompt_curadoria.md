atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-01T08:22:46.303925+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1294
  🇨🇳 China          771
  🇹🇼 Taiwan         253
  🇰🇷 Coreia do Sul  682

## O que já está no feed (não repita)

  - [china] Guangzhou Caps Deposits, Tightens Oversight in Housing-Sales Overhaul
  - [japan] Japan PM vows to underpin yen by boosting economic competitiveness
  - [china] ZAWYA: Why East African banks are joining yuan payment system ?
  - [korea] ZAWYA: How Kenya won back Rwanda’s oil cargo imports ?
  - [japan] Japan PM says govermentt steps will strengthen market confidence in yen
  - [korea] S.Korea Sept exports hit record high as AI boom drives chip sales to all-time peak
  - [japan] Stock price rises by 2,200 yen Buy orders spread to AI/semiconductor related stocks
  - [japan] Main opinions from the September meeting of the Bank of Japan: If there are signs of upward movement in prices
  - [japan] Nikkei logs six-week closing high as Micron forecast lifts chip stocks
  - [japan] BOJ Summary Suggests Low Chance of Back-To-Back Rate Hike — Market Talk
  - [japan] Japanese Shares Climb on Chip Rally
  - [japan] BOJ Summary Shows Government Unconcerned About Price Overshoot Risks — Market Talk
  - [japan] Government plans to submit 21 bills including consumption tax reduction bill in extraordinary Diet session
  - [japan] Yen Falls After Japan Q3 Tankan Survey Data
  - [japan] Asian currencies rangebound as dollar holds near two-month high, yen slips
  - [japan] Yen Weakens as BOJ Summary Disappoints
  - [china] China's Tencent taps Oracle for 100,000 AI chips in $7B lease deal - report
  - [korea] Kospi Snaps Three-Session Losing Streak; Chip Stocks Advance
  - [japan] Ceres Inc - To Buy Back Up To 10.83% Of Shares Worth 2.5 Billion Yen
  - [japan] Japan manufacturing growth slows to six-month low in September By Investing.com
  - [japan] At 3:00 p.m., the dollar rose to the low 158 yen range, as expectations for continuous interest rate hikes by 
  - [japan] Japan manufacturing growth slows to six-month low in September
  - [japan] Asia stocks rise on chipmaker gains, soft U.S. inflation; Nikkei outperforms
  - [japan] Yen Falls Against Majors
  - [korea] Korea’s real wages fall for 4th straight month as inflation outpaces pay gains
  - [korea] Korea kicks off US investment plan with $22.3b Texas power project
  - [china] Chinese refiners suspend October fuel exports, one cancels cargoes, sources say
  - [taiwan] Four glass makers converge on 510x515mm substrate, hinting at TSMC's next move
  - [japan] Bank of Japan releases main opinions at September meeting, maintains interest rate hike stance, with some poin
  - [japan] Takashi Sasano mentions the ``deterioration of cockroaches'' in the Bank of Japan Tankan News: ``If you listen
  - [korea] Memory shortage deepens, extending boom for Korean chipmakers
  - [japan] Macroscope: Bank of Japan Tankan, support for interest rate hike, October forecast setback slightly (Reuters)
  - [japan] BOJ signals accelerated rate tightening amid persistent inflation risks
  - [korea] SK hynix says no decision on Solidigm amid IPO concerns
  - [china] Commentary: A $30 Billion Opening Beneath a Still-High U.S. Tariff Wall
  - [japan] Bank of Japan September meeting: Opinions on the need to raise interest rates at a rapid pace one after anothe
  - [japan] Japan's manufacturing PMI moderates to 54.1 in September; BOJ signals quicker hikes
  - [china] Russia steps up sunflower oil exports to China as war disrupts India trade
  - [china] Chinese refiners suspend Oct fuel exports, PetroChina cancels cargoes, sources say
  - [japan] Japan inflation wave lifts prices on 3,000 food and drink items

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
      "published_utc": "2026-10-01T08:22:46+00:00",
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

