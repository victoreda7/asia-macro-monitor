atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-12T02:32:43.097725+00:00
Total: 2817 manchetes

  🇯🇵 Japão          1108
  🇨🇳 China          776
  🇹🇼 Taiwan         273
  🇰🇷 Coreia do Sul  660

## O que já está no feed (não repita)

  - [korea] [Photo] National Assembly Finance and Economy Committee conducts audit of the Bank of Korea’s government affai
  - [korea] [2026 National Assembly Audit] Shin Hyun-song “We will carry out independent monetary policy without hesitatio
  - [korea] Most Asian currencies muted; South Korean won hits two-year high
  - [korea] S.Korean stocks slide as chip selloff deepens, foreign selling persists
  - [taiwan] TSMC expected to report sixth straight quarter of record profit thanks to AI boom
  - [korea] The Bank of Korea repeatedly hinted at the possibility of further interest rate hikes... Market outlook “withi
  - [china] China-EU Deal Likely Averts Trade War, But Impact Limited — Market Talk
  - [korea] Finance minister urges preemptive action for supply chain stability
  - [taiwan] MediaTek flagship AP share to surpass Samsung as TSMC boosts Dimensity
  - [korea] After the tax reform plan, high-priced apartments in Gangnam, Seoul, have turned weak, but the upwar..
  - [korea] Governor of the Bank of Korea: “Inflation is expected to remain above the target level for a considerable peri
  - [china] CHINA PBOC CONDUCTS CNY50 BLN VIA 7-DAY REVERSE REPO MON
  - [korea] S. Korea likely to continue solid growth driven by robust chip exports
  - [china] The central bank launched a 50 billion yuan 7-day reverse repurchase operation today
  - [korea] President Shin Hyun-song “Solid growth continues…inflation has exceeded target for a considerable period of ti
  - [korea] The Bank of Korea raised interest rates for the second time in a row... Shin Hyun-song “Possibility of insolve
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7313 MON VS 6.7330
  - [korea] Deputy Prime Minister and Minister of Finance and Economy Lee Hyung-il announced on the 12th that he..
  - [china] Tencent plans dollar, offshore yuan bond sale under note programme
  - [china] Chinese Yuan Hits 4-year High
  - [china] This Chinese memory chip maker has global potential and is poised to outperform
  - [korea] South Korean bond rally seen faltering as traders brace for rate hikes
  - [korea] SK Hynix oversold near support after 15% slide: Live levels
  - [korea] The Bank of Korea repeatedly indicates its intention to “further increase the base interest rate”
  - [china] CX Daily: Yuan’s Global Role Is Expanding Beyond Trade, StanChart Execs Say
  - [china] Tencent proposes dollar, offshore yuan note offering
  - [china] The central bank's 302 billion yuan reverse repo expires this week, and the 500 billion yuan buyout expires on
  - [korea] Exports double in first 10 days of Oct. on chip boom
  - [japan] Nikkei average growth is sluggish, focus on TSMC performance and price index (TV Asahi (ANN))
  - [korea] Seoul shares open lower on inflation, Mideast woes
  - [korea] (LEAD) Seoul shares open lower on inflation, Mideast woes
  - [korea] (LEAD) Exports double in first 10 days of October on chips
  - [korea] BOK forms 11-member advisory committee on digital currency
  - [korea] 57.3% of bank household loans have variable interest rates... Will the interest burden increase due to further
  - [korea] (URGENT) Seoul shares open lower on inflation, Midest woes
  - [korea] Spread of interest rate hikes by central banks around the world... Bank of Korea also forecasts 3.5%
  - [korea] South Korea to deploy market stabilising measures if needed, finance minister says
  - [korea] Last year, the amount of counterfeit and falsified bills that the Bank of Korea took over from the i..
  - [korea] The base interest rate rose twice... 57% of bank household loans have variable interest rates
  - [japan] "A corner of Ota Ward's three major luxury residential areas" "Ikegami Line to be detoured due to residents' o

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
      "published_utc": "2026-10-12T02:32:43+00:00",
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

