atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-15T03:42:42.550547+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1123
  🇨🇳 China          847
  🇹🇼 Taiwan         291
  🇰🇷 Coreia do Sul  739

## O que já está no feed (não repita)

  - [korea] SKHY Tracks Worst Month Since Nasdaq Debut: SK Hynix Reportedly Wants To Ship More Chip Tools To China Before 
  - [japan] Japan's Nikkei plunges as tech stocks hammered by AI, rate hike worries
  - [japan] Don't be overly cautious about interest rate hikes: ``The risk of price rises is commensurate with the risks.'
  - [china] Offshore Yuan Lingers Near 2022 High
  - [taiwan] ByteDance nears chip supply deal with MediaTek for data centres, Bloomberg News reports
  - [china] The central bank launched a 45 billion yuan seven-day reverse repurchase operation with an interest rate of 1.
  - [china] Hong Kong's sole yuan clearing bank plans mainland NCD issuance
  - [japan] Yen Gains Amid Fresh Verbal Warning
  - [japan] Asia stocks slump as chip rout deepens after hotter U.S. inflation
  - [korea] Asia stocks tumble, S.Korea’s KOSPI slumps 7% on chip rout, Fed rate fears
  - [taiwan] Bytedance In Talks To Secure Mediatek AI Chips For Data Centers - Bloomberg News
  - [japan] What's behind the sudden turnaround and being fired in 4 weeks? Prime Minister Takaichi's "Chiebukuro" Ministe
  - [japan] G20 Finance Ministers and Central Bank Governors Meeting begins, discussing responses to the global economy an
  - [japan] ``There is a fair amount'' of price rise risk, and there is no need to be overly cautious about raising intere
  - [china] IMF urges China to deploy bigger fiscal stimulus
  - [japan] BOJ Board Member Indicates Further Room for Rate Hikes
  - [korea] Why a memory chip glut could be Korea's weapon against China
  - [japan] BoJ Koeda Urges Timely Rate Hikes Amid Inflation Risks
  - [korea] Exclusive-SK Hynix conditions new US factory on more US chip equipment exports to China, sources say
  - [korea] Why is SK Hynix stock plunging today?
  - [japan] BOJ should not be overly cautious in raising rates, board member Koeda says
  - [japan] BOJ policymaker warns against being overly cautious on rate hikes
  - [korea] Why is Samsung Electronics stock plunging today?
  - [china] On October 15, the central bank launched a 45 billion yuan 7-day reverse repurchase operation.
  - [japan] Bank of Japan council member emphasizes continuing interest rate hikes: ``There is no need to be cautious'' (K
  - [taiwan] TSMC Set to Post Sixth Consecutive Quarter of Record Profit, Thanks to AI Boom
  - [taiwan] TSMC expected to report sixth straight quarter of record profit thanks to AI boom
  - [china] China stocks fall, led by tech, as US inflation stokes Fed fears
  - [china] "Three polarizations" are occurring in the Chinese economy, where domestic demand has fallen sharply...The rea
  - [japan] Stock prices temporarily fell by more than 3,000 yen against the backdrop of expectations for a US interest ra
  - [korea] The cancellation of land supply contracts by the Korea Land and Housing Corporation (LH) increased a..
  - [japan] Bank of Japan member says there is "no need to be cautious" in raising interest rates (Kyodo News)
  - [japan] BOJ should not be overly cautious raising rates, board member Koeda says
  - [china] CHINA PBOC CONDUCTS CNY45 BLN VIA 7-DAY REVERSE REPO THURS
  - [korea] Korean memory makers accept ASML parts price hike, leaving TSMC as the open question
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7253 THURS VS 6.7249
  - [korea] Samsung Electronics Co. was counted as the largest net purchase by high-yield investors of Mirae Ass..
  - [japan] Speech by Board Member KOEDA in Kumamoto (Economic Activity, Prices, and Monetary Policy in Japan)
  - [japan] Japan futures fall as Tokyo equities slump, China imports weaken
  - [korea] Hot US inflation hammers Kospi nearly 6% lower as chips buckle

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
      "published_utc": "2026-10-15T03:42:42+00:00",
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

