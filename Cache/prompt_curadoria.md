atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-27T03:02:43.170974+00:00
Total: 3000 manchetes

  🇯🇵 Japão          976
  🇨🇳 China          850
  🇹🇼 Taiwan         371
  🇰🇷 Coreia do Sul  803

## O que já está no feed (não repita)

  - [japan] Ex-BOJ chief Kuroda backs more rate hikes, his former deputy urges caution
  - [korea] Roundup: S. Korea's real GDP grows 1.0 pct on quarter in Q3
  - [china] The world's super central bank debuts this week, the United States, Europe and Japan are expected to remain on
  - [china] "Peak-cutting and valley-filling" precise adjustment, MLF volume reduction continuation in October
  - [korea] Bank of Korea warns country's chip exports could fall by up to $100 billion if AI spending slows
  - [korea] Rupiah, peso lead losses among Asian currencies; won bucks trend
  - [korea] South Korean shares surge on US rally, strong GDP
  - [korea] South Korea's Stronger 3Q Growth Bolsters Case for November Rate Hike — Market Talk
  - [japan] Yen slips ahead of central bank bonanza, dollar firms on tech rebound
  - [taiwan] Anthropic's IPO filing puts TSMC, HBM, direct leasing at the center of AI compute risk
  - [korea] The top 1% return on equity investment was found to have bought Samsung Electronics the most and sol..
  - [china] The central bank launched a 412 billion yuan reverse repurchase today
  - [korea] With semiconductor market leader Samsung Electronics and SK Hynix announcing their third-quarter ear..
  - [china] On October 27, the central bank launched a 412 billion yuan 7-day reverse repurchase operation.
  - [china] China Industrial Profits Rise 14.4%, Fastest Growth in Three Months
  - [china] CHINA PBOC CONDUCTS CNY412 BLN VIA 7-DAY REVERSE REPO TUES
  - [china] China Industrial Profits Grow 15.5% YoY in Jan-Sept
  - [china] China’s Industrial Profits Jump Most in Three Months on Oil, AI
  - [china] CHINA PBOC CONDUCTS CNY1000 BLN VIA O/N REVERSE REPO TUES
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7171 TUES VS 6.7162
  - [china] China's industrial profits rise 15.5% in January-September
  - [china] Yu Weining, chief statistician of the Industrial Department of the National Bureau of Statistics, interprets t
  - [china] From January to September 2026, profits of industrial enterprises above designated size nationwide increased b
  - [china] The central bank's reverse repurchase net investment today is 1.014 billion yuan
  - [korea] S.Korean shares rebound as Anthropic IPO plan drives Samsung, SK Hynix rally
  - [china] The central bank launched a 412 billion yuan 7-day reverse repurchase operation today
  - [korea] SK Hynix tests bearish resistance cluster at KRW 1,381,000: Live
  - [japan] BlackRock Joins SBI and Startale to Link Tokenized MMFs With Japanese Yen Stablecoins
  - [korea] South Korea's Corporate Bond Issuance Surges 77.5% in September
  - [japan] JGB Yields Higher as AI Bubble Concerns Ease — Market Talk
  - [korea] Why is SK Hynix stock surging today?
  - [japan] Major life insurance companies accelerate replacement of government bonds
  - [korea] South Korea’s economy grows 1% in Q3, beating BOK forecast
  - [korea] Foreigners have sold a large number of domestic stocks, but the won-dollar exchange rate is on the d..
  - [japan] JAPAN SEPT SERVICES PPI +0.3% M/M: AUG +0.1%
  - [korea] S. Korea's GDP expands 1% in Q3 on strong exports, investment: BOK
  - [korea] South Korea’s Economy Beats Forecasts on AI-Driven Chip Boom
  - [japan] MNI: JAPAN SEPT SERVICES PPI +3.7% Y/Y; AUG +3.5%
  - [japan] Japan Services Producer Inflation Highest Since June 2024
  - [china] Southeast Asia’s housing paradox: too many homes, too few buyers

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
      "published_utc": "2026-10-27T03:02:43+00:00",
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

