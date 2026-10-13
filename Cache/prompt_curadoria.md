atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-13T03:22:45.865790+00:00
Total: 2966 manchetes

  🇯🇵 Japão          1131
  🇨🇳 China          824
  🇹🇼 Taiwan         290
  🇰🇷 Coreia do Sul  721

## O que já está no feed (não repita)

  - [korea] South Korean Won Retreats from 2-Year High
  - [korea] South Korea’s Lee says country cannot avoid raising interest rates
  - [japan] [Illustration] Corporate prices rise 6.8% in September = growth slows due to fall in rice prices - Bank of Jap
  - [korea] Samsung, SK Hynix shares plunge on China competition fears
  - [china] Offshore Yuan Steady Vs. Dollar Ahead of Major Chinese Economic Data — Market Talk
  - [japan] Mr. Sasaki appointed as Bank of Japan Shizuoka Branch Manager (Kyodo News)
  - [japan] Yen Gains in Post-Holiday Trading
  - [korea] Why is Samsung Electronics stock plunging today?
  - [korea] Why is SK Hynix stock plunging today?
  - [korea] IMF Chief Economist: Outlook for AI Supply Chain Econs Like South Korea, Singapore, Vietnam Raised Significant
  - [korea] South Korea shares tumble over 6% as chip selloff triggers trading curb
  - [korea] IMF raises S. Korea's growth forecast to 3.3% amid chip supercycle
  - [korea] IMF Raises 2026 South Korea Growth Forecast to 3.3% From 2.6%
  - [japan] IMF Raises 2026 Japan Growth Forecast to 0.7% From 0.6%
  - [china] IMF Lowers 2027 China Economic Growth Forecast to 4.0% From 4.1%
  - [china] IMF Lowers 2026 China Economic Growth Forecast to 4.5% From 4.6%
  - [china] IMF'S WORLD ECONOMIC OUTLOOK: CHINA '26 GROWTH SEEN +4.5%, -0.1; '27 +4.0%,-0.1
  - [japan] September corporate price index increased by 6.8% compared to the same month last year; rate of increase slows
  - [taiwan] Taiwan dollar, South Korean won lead Asian currencies lower
  - [china] The central bank launches 65 billion yuan 7-day reverse repurchase operation
  - [korea] Sebo Manufacturing Engineering Construction Wins 97 Billion Won Order
  - [japan] Bank of Japan to raise interest rates to neutral level in stages despite forecast of slowing growth = IMF (Reu
  - [japan] IMF expects gradual BOJ rate hike towards neutral setting
  - [taiwan] Hamada Labs targets Taiwan, Japan manufacturing with AI platform
  - [korea] IMF raises S. Korea's growth forecast to 3.3 pct amid chip supercycle
  - [japan] Japan bond yields diverge as investors weigh inflation, BOJ outlook
  - [china] CHINA PBOC CONDUCTS CNY65 BLN VIA 7-DAY REVERSE REPO TUES
  - [china] The central bank launched a 65 billion yuan 7-day reverse repurchase operation today
  - [china] SNDK, MU, INTC, AMD, SKHY: Chip Stocks Extend Slide As AI Funding Concerns, China Competition Weigh On Sector
  - [china] Goldman Says Markets Are Underestimating How Far Yuan Can Rise
  - [china] On October 13, the central bank launched a 65 billion yuan 7-day reverse repurchase operation.
  - [japan] Japan MOF To Auction Y700.0B Of 20-Year Govt Bonds Oct 20
  - [china] Exclusive | China’s finance minister to deliver opening speech at Apec meeting in Hong Kong
  - [korea] Foreign selling slams Kospi as China chip fears hit Samsung, SK Hynix
  - [japan] Japan’s wholesale inflation remains elevated, keeps alive BOJ rate-hike view
  - [korea] Seoul shares open sharply lower on U.S. losses, inflation concerns
  - [korea] Korean Chip Stocks Sink on Chinese Rival Worry, Broadcom Remarks
  - [korea] (LEAD) Seoul shares open sharply lower on U.S. losses, inflation concerns
  - [taiwan] Podcast highlights: Is Elon Musk using TSMC talks as leverage against Intel and Samsung?
  - [japan] Japan PPI unexpectedly eases in Sept on stronger yen, cooling oil By Investing.com

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
      "published_utc": "2026-10-13T03:22:46+00:00",
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

