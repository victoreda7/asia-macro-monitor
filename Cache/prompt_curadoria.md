atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-11T02:32:42.823034+00:00
Total: 3000 manchetes

  🇯🇵 Japão          920
  🇨🇳 China          909
  🇹🇼 Taiwan         310
  🇰🇷 Coreia do Sul  861

## O que já está no feed (não repita)

  - [china] Russia retreats from China's yuan as U.S. sanctions bolster dollar
  - [japan] Japan futures gain for second session on tyre makers' dip-buying, weaker yen
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation today
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation in the open market today
  - [taiwan] Taiwan machinery exports rise for 21st month on AI demand, but US election adds uncertainty
  - [china] CHINA PBOC CONDUCTS CNY187 BLN VIA O/N REVERSE REPO WEDS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7191 WEDS VS 6.7167
  - [china] On November 11, the central bank launched a 187 billion yuan overnight reverse repurchase operation.
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation with an interest rate of 1
  - [japan] "Neocloud" Core Weave's final deficit 6 times due to interest payment
  - [japan] Japan MOF To Auction Y700.0B Of 20-Year Govt Bonds Nov 18
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation on November 11
  - [japan] Japan MOF To Auction Y1.9T Of TD-Bills Nov 18
  - [china] US lawmakers push China chip rules after Nvidia CEO allegations
  - [china] HEADS UP: US TSY'S BESSENT ABOUT TO SPEAK AT THE NATIONAL COMMITTEE ON US-CHINA RELATIONS GALA DINNER
  - [korea] Revised regional currency swap arrangement takes effect
  - [korea] South Korean shares slip as US inflation data boosts rate-hike bets
  - [japan] From AKB to the Bank of Japan, on-site financial classes are spreading, one step at a time to prevent fraud (A
  - [korea] Exports more than double in 1st 10 days of Nov.
  - [korea] Govt. to release growth forecasts 3 times per year: finance minister
  - [korea] South Korea's Tax Cuts for Gasoline, Diesel, Butane to Continue Until Jan. 31, Finance Ministry Says
  - [korea] South Korea to Extend Temporary Fuel Tax Cuts by Two Months, Finance Ministry Says
  - [korea] Seoul shares turn higher after weak start amid inflation woes
  - [korea] Even mention of the US ‘big step’… Will the Bank of Korea raise interest rates despite ‘AI risk’? [Money]
  - [korea] (LEAD) Seoul shares turn higher after weak start amid inflation woes
  - [korea] (LEAD) Exports more than double in 1st 10 days of Nov.
  - [taiwan] TSMC plans investments in Anthropic, OpenAI; sets up investment firm to expand semiconductor strategy
  - [korea] Seoul shares open lower on inflation woes
  - [korea] South Korea November 1-10 exports surge 111.9% year/year
  - [korea] S. Korea to extend fuel tax cuts through Jan. to ease price burdens
  - [china] Russian Push to Escape Dollar for Yuan Collapses Under Sanctions
  - [taiwan] LWLG: Foxconn system demo advances polymer optics; foundry delays move volume production to 2028
  - [japan] Considering registration system for business employing people with disabilities
  - [taiwan] TSMC, Microsoft executives debate AI's impact on Day 2 of Nikkei Dialogue
  - [china] At China’s Big Import Fair, Sellers Try to Crack a Tough Market
  - [japan] SoftBank Group Corp. Stock 12‑Month Price Target Cut to JPY 8677.28, Implies 155% Upside
  - [china] Still possible chipmaker Nexperia could reunite with Chinese operations, CEO says
  - [korea] Exicure, Inc. Announces Agreement to Sell GPC-100 Program Assets to GPCRT Inc. for KRW 6.5 Billion
  - [korea] Exicure, Inc. (XCUR) Agrees to Sell GPC-100 Assets for KRW 6.5B
  - [korea] Exicure (XCUR) Agrees to Sell GPC-100 Assets for KRW 6.5B

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
      "published_utc": "2026-11-11T02:32:42+00:00",
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

