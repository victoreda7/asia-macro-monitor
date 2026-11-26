atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-26T04:12:49.464814+00:00
Total: 3000 manchetes

  🇯🇵 Japão          913
  🇨🇳 China          983
  🇹🇼 Taiwan         337
  🇰🇷 Coreia do Sul  767

## O que já está no feed (não repita)

  - [japan] BOJ’s Tamura flags faster pace of rate hikes amid inflation risk
  - [china] China Vanke Is Seeking Another Extension On A Yuan Bond Due Next Month - Bloomberg News
  - [china] China Braces for Tariff Hike After US Announcement
  - [korea] Some said that the nominal GDP, which was around 2,600 trillion won last year, will far exceed 3,000..
  - [korea] The Bank of Korea raises the base interest rate to 3.25%... Leave open the possibility of 3.75% next year
  - [korea] [Photo] Bank of Korea monetary policy direction press conference
  - [korea] BOK Gov: Chip Companies' Operating Profits Estimated at KRW700T This Year
  - [china] Nissan Motor Planning To Import And Sell Plug-In Hybrid Vehicles Produced By China JV In Japan Market, Nikkei 
  - [korea] The Bank of Korea raises the base interest rate to 3.25% per annum... Growth rate expected to be 4.1% next yea
  - [korea] BOK Gov: See Private Consumption Growing 2.4% in 2027, Faster Than in 2026
  - [korea] BOK Gov: IT Boom May Take Time to Translate Into Private Consumption
  - [korea] The Bank of Korea raises the base interest rate to 3.25%… “Next year’s growth rate will be 4.1%”
  - [korea] (URGENT) BOK chief sees improvement in S. Korea's potential growth rate
  - [japan] BOJ policymaker signals chance of faster-pace interest rate hikes
  - [japan] Japanese yield curve steepens as markets reprice BOJ rate outlook
  - [korea] U.S. expected to maintain agreed-upon 15 pct tariff rate for S. Korea, issues warning on chips
  - [china] Nvidia chips reach Chinese-owned U.S. firms despite export curbs, CBS reports
  - [korea] (URGENT) S. Korea's nominal GDP expected to top 3,000 tln won in 2026, 700 tln won from chip sector: BOK gov.
  - [japan] Bank of Japan council member Naoki Tamura ``responds quickly, including accelerating the pace of interest rate
  - [japan] Bank of Japan's Tamura, a member of the Bank of Japan's Council, wants to raise interest rates further towards
  - [japan] BOJ member Tamura wants to raise interest rates further towards neutral interest rates “as soon as possible” (
  - [china] China, Hong Kong shares shrug off tariff risk to edge up from multimonth lows
  - [korea] (URGENT) Recent stock market correction likely to affect private consumption: BOK gov.
  - [korea] (URGENT) Inflation expected to reach target inflation of 2 pct in 2028: BOK gov.
  - [korea] BOK Gov: To Take Action Until Inflation Converges Toward Target
  - [korea] BOK Gov: Expect Inflation to Approach Target in 2028
  - [korea] Bank of Korea raises interest rates amid AI chip boom
  - [korea] Bank of Korea Gov: Inflation to Remain Above Target Through 2027
  - [korea] South Korea’s central bank raises rates, upgrades 2027 growth outlook
  - [taiwan] Taiwan says it is confident of keeping previously agreed tariffs with US
  - [taiwan] Taiwan says it is confident it will maintain tariffs previously agreed with the US
  - [korea] The Bank of Korea raises the base interest rate by 3.25% per year... Next year’s growth rate increased signifi
  - [korea] (2nd LD) BOK raises key rate to 3.25 pct amid strong growth, inflation, revises up 2027 forecast to 4.1 pct
  - [korea] The Bank of Korea raises the base interest rate by 0.25%p... 3.25% per annum in 2 years
  - [china] CHINA PBOC CONDUCTS CNY571.5 BLN VIA O/N REVERSE REPO THURS
  - [korea] There are a series of experiences in the online real estate community that this year's comprehensive..
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7096 THURS VS 6.7088
  - [korea] Samsung Electronics, SK hynix rebound as U.S. chip stocks recover
  - [korea] [Full text] Bank of Korea Monetary Policy Committee’s monetary policy direction for November
  - [korea] [Breaking News] Bank of Korea raises base interest rate to 3.25% per annum... Next year’s growth rate is raise

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
      "published_utc": "2026-11-26T04:12:49+00:00",
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

