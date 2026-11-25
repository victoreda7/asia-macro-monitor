atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-25T06:03:08.732830+00:00
Total: 3000 manchetes

  🇯🇵 Japão          959
  🇨🇳 China          1001
  🇹🇼 Taiwan         337
  🇰🇷 Coreia do Sul  703

## O que já está no feed (não repita)

  - [korea] (LEAD) Hanwha Aerospace secures export rights for KM3 amphibious bridging vehicle
  - [japan] JGB yield curve steepens as market reassesses BOJ's rate hike path
  - [korea] Chuncheon City drew up a budget plan for next year worth 1.8554 trillion won and submitted it to the..
  - [korea] 54% of bond market workers say, “The Bank of Korea Monetary Policy Committee will raise the base interest rate
  - [taiwan] TSMC confirms Texas tax abatement filing, investment under review
  - [japan] Japan’s services PPI jumps 4.2% in October, hitting highest level since 1990
  - [japan] Indicators for Core CPI
  - [china] China's plastics export boom fades as stockpiles run down, feedstock costs climb
  - [korea] (LEAD) Banks' household mortgage lending rates hit over 14-yr high in Oct.
  - [korea] Bank of Korea May Opt for Hawkish Hold — Market Talk
  - [korea] Why is SK Hynix stock tumbling today?
  - [korea] Why is Samsung Electronics stock plunging today?
  - [taiwan] Deputy Minister of Agriculture Hu Zhongyi: Taiwan’s rice is very competitive and is estimated to export nearly
  - [china] MLF reverse repurchase portfolio operation, the central bank accurately regulates liquidity
  - [japan] Japan not considering issuing new deficit-financing bonds for extra budget, TBS says
  - [china] China Focus: China's manufacturing powerhouse deepens regional integration
  - [china] China's yuan touches 3-week high but trade tension worries cap gains
  - [china] The central bank launched a 516 billion yuan overnight reverse repurchase operation today
  - [china] Alibaba in Talks for Potential Yuan, Dollar Bond Sale Next Year
  - [japan] Auction Result of 40-Year JGBs on November 25, 2026
  - [korea] North Korea expels Swiss representative over sanctions related to children's camp
  - [taiwan] Taiwan Government: In Close Contact With US Ahead Of Expected Tariff Announcement
  - [japan] Japan’s key services inflation gauge hits 36-year high
  - [korea] Banks' household mortgage lending rates up for 6th month in Oct.
  - [japan] Judgment on the prefecture's economy remains unchanged Bank of Japan Kochi Branch [Kochi] (RKC Kochi Broadcast
  - [china] EU sets caps on Chinese, Korean hybrid car imports; impact on Hyundai, Kia seen limited
  - [japan] Nikkei average stock price drops by more than 2,100 yen at one point, selling mainly semiconductor-related sto
  - [japan] Which prefecture has the highest food prices? 1st place in 2025 is Okinawa prefecture with 106.6, Tokyo is 3rd
  - [china] Alibaba in talks for potential yuan, dollar bond sale next year- Bloomberg News
  - [china] Taxman can be China's next GDP growth engine
  - [japan] Rakuten Credit Risk Surges After Yen Bond Offering Scrapped
  - [taiwan] Taiwan dollar and South Korean won lead decline in Asian FX
  - [china] On November 25, the central bank launched a 617 billion yuan overnight reverse repurchase operation.
  - [japan] Long-Term JGB Yields Fall Amid Chip Stock Selloffs — Market Talk
  - [china] Important signal! 500 billion + 800 billion, the central bank takes action today
  - [china] CHINA PBOC CONDUCTS CNY617 BLN VIA O/N REVERSE REPO WEDS
  - [korea] AI Chip Boom to See Won Build on Best Year in Almost a Decade
  - [japan] "US Tariffs and Japan's Price Index" Today's Bonds by Cow and Bear (Column) November 25, 2026 (Hiroyuki Kubota
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7088 WEDS VS 6.7111
  - [china] The central bank launched a 617 billion yuan overnight reverse repurchase operation today

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
      "published_utc": "2026-11-25T06:03:08+00:00",
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

