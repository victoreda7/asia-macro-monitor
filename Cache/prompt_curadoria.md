atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-03T03:02:44.099200+00:00
Total: 3000 manchetes

  🇯🇵 Japão          913
  🇨🇳 China          848
  🇹🇼 Taiwan         359
  🇰🇷 Coreia do Sul  880

## O que já está no feed (não repita)

  - [china] The central bank takes action! The foreign exchange reserve ratio was raised by 2 percentage points, and the o
  - [china] Offshore Yuan Weakens After PBOC Moves to Cool Currency Rally
  - [japan] Aeon subsidiary Ministop suddenly goes into the red...The biggest factor behind the expected surplus of 1.5 bi
  - [china] PBOC to raise banks’ forex reserve requirements amid yuan appreciation pressure
  - [korea] Youngwoo DSP, a company specializing in semiconductor and display equipment, recorded a good perform..
  - [china] Offshore Yuan Slides as PBOC Acts to Curb Rally
  - [korea] “So you’ve been waiting only for shareholder returns from Samsung Electronics and SK Hynix?” ... A policy that
  - [korea] Asian currencies mostly lower; South Korean won bucks trend
  - [korea] Consumer price inflation rate 2.8% in October Processed food and eating out costs rise = South Korea
  - [china] Iron ore dips on higher shipments, sluggish China demand
  - [china] The central bank suddenly took action: the foreign exchange reserve ratio was raised to 6%
  - [china] The first increase in the past 5 years! After the RMB rose above 6.65, the central bank raised the foreign exc
  - [korea] LG Energy Solution Q3 Revenue Rose 27.6% QoQ to KRW 9.6T
  - [china] China's Central Bank Tweaks Forex Reserve Rules to Steady Yuan
  - [japan] Japan petrol subsidy cut could mark fiscal limit
  - [china] CHINA PBOC CONDUCTS CNY621 BLN VIA O/N REVERSE REPO TUES
  - [korea] Samsung's Young Hyun Jun urges humility, customer trust amid semiconductor profit boom
  - [china] The central bank took action to cool down the RMB and raised the foreign exchange deposit reserve ratio to 6%.
  - [china] On November 3, the central bank launched a 621 billion yuan overnight reverse repurchase operation.
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7150 TUES VS 6.7146
  - [china] Soy barge bids firm as exports to China continue
  - [china] China hikes forex deposit reserve ratio to 6%
  - [korea] BOK sees consumer inflation remaining near 3% in Nov.
  - [china] As the RMB continues to appreciate, the People's Bank of China raises the foreign exchange deposit reserve rat
  - [china] Hong Kong to drive global yuan use, PBOC official says
  - [japan] The Bank of Japan left interest rates unchanged, and the yield on five-year government bonds fell to 2.237% in
  - [taiwan] High inventories threaten Taiwan manufacturing PMI expansion
  - [korea] BOK sees consumer inflation remaining near 3 pct in Nov.
  - [china] Central Bank: From November 15, increase the reserve requirement ratio of foreign exchange deposits of financi
  - [china] China to raise forex deposit reserve ratio to 6% starting November 15
  - [china] China Central Bank: Aim Is to Better Manage Foreign Exchange Liquidity in Financial Institutions
  - [china] China to Raise Foreign Exchange Reserve Requirement Ratio by 2 Percentage Points
  - [china] China Central Bank: Decision Takes Effect Nov. 15
  - [china] Central Bank: Starting from November 15, it will increase the foreign exchange deposit reserve ratio of financ
  - [china] The central bank decided to raise the foreign exchange deposit reserve ratio of financial institutions
  - [korea] LG Energy Solution: ESS-led shipments lifted Q3 revenue 28% QoQ and operating profit to KRW 756bn
  - [korea] South Korea Inflation Holds Firm, Bolstering Case for More Hikes
  - [korea] US trade commission terminates Samsung chip patent probe following settlement with Netlist
  - [korea] Consumer prices up 2.8% in Oct., remain in 2% for 2nd month
  - [korea] Consumer price inflation rate in October 2.8%, in the low 2% range for 2 consecutive months = South Korea

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
      "published_utc": "2026-11-03T03:02:44+00:00",
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

