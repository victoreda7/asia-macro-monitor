atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-17T08:33:07.934591+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1037
  🇨🇳 China          894
  🇹🇼 Taiwan         302
  🇰🇷 Coreia do Sul  767

## O que já está no feed (não repita)

  - [china] New wave of insolvency in China's real estate sector causes credit risk to resurface
  - [korea] South Korea tightens university exam checks to screen for hidden cameras
  - [china] Before the Trump-Xi meeting, the US strictly controlled the export of advanced AI chips and Beijing approved e
  - [china] Key facts: Apollo Go; Kunlunxin Listing; Cloud Cash Flow 2.8B Yuan
  - [japan] Understanding the loans of the government, the Bank of Japan, and credit unions; analyzing the soundness of ma
  - [china] U.S. Chip Curbs Pose Double-Edged Sword for China AI Industry — Market Talk
  - [china] Nvidia to halt chip sales to data centers renting over half to China - report
  - [china] Nvidia warns chip buyers of legal risks tied to China AI access, CNBC reports
  - [korea] Higher interest rates, sluggish consumer spending take toll on Korea’s credit card firms
  - [china] Nvidia warns chip buyers about legal risks related to access to AI in China, according to CNBC report
  - [korea] “Key Players in Accelerating the $1 Trillion Export Milestone”... World Class Products Expand to 1,100 Compani
  - [japan] Stock prices fall Sell orders centered on AI and semiconductor related stocks
  - [china] JSW Steel CEO flags Chinese exports, trade barriers as key challenges
  - [china] Secondhand Home Prices Rise in Fewer Major Chinese Cities
  - [korea] Kospi Falls for Fourth Straight Session; Chip, Defense Stocks Retreat
  - [korea] S. Korea set to achieve US$1 trillion export milestone for 1st time
  - [taiwan] Taiwan to subsidize employers who let parents work fewer hours
  - [china] How far will nuclear weapons reduction go at the US-China-Russia summit meeting? The twists and turns of the "
  - [korea] Anthropic IPO tests next leg of rally in Samsung, SK hynix
  - [taiwan] Candidates address Taoyuan's bus woes at TV policy presentation
  - [taiwan] The United States strictly controls the export supply chain of advanced AI chips: the manufacturing flow has a
  - [china] U.S. Chip Export Curbs a Mixed Bag for Chinese AI — Update
  - [korea] Even during rising interest rates, the four major banks take a step back in NIM... pressure on financing costs
  - [korea] Citi: “The Bank of Korea will further increase the base interest rate this month... The downside risk is priva
  - [china] Exclusive-China taps US AI models to train homegrown rivals as chip curbs bite
  - [china] U.S. Chip Export Curbs Have Mixed Implications for China's AI Industry
  - [china] China and Canada Expand Tariff Relief as Xi Meets Carney
  - [korea] IMF raises Korea's 2026 growth forecast to 3.9% on AI chip boom
  - [china] China stocks flat as chip curbs lift local tech, hit internet giants
  - [china] U.S. tightens rules to restrict China’s access to advanced AI chips overseas
  - [china] New rules for beauty festival before Sichuan-Xi meeting! Restricting the export of chips to overseas data cent
  - [china] Chinese firms turn to US AI models for training as export restrictions tighten: Reuters
  - [taiwan] Daxin aims for semiconductor materials to exceed half of revenue by 2030
  - [japan] Liberal Democratic Party Policy Research Council Chairman Kobayashi ``negotiates to gain understanding'' of co
  - [japan] Europe and Japan deepen semiconductor ties as imec expands in Hokkaido and JASMINE mobilizes
  - [japan] Government, Bank of Japan to grasp loan information of Shinkin Banks (Kyodo News)
  - [china] AMD, MU, SKHY, AVGO: Chip Stocks Ease Overnight After Selloff On New US Chip Restrictions Targeting China
  - [china] China AI Highflier Crashes 85% as Chip Fears Hit Model Makers
  - [china] Yuan steady despite firm dollar as PBOC strengthens fixing ahead of APEC
  - [china] China, Canada Expand Tariff Relief in Deepening Trade Thaw

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
      "published_utc": "2026-11-17T08:33:08+00:00",
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

