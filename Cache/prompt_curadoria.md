atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-30T04:52:42.900154+00:00
Total: 3000 manchetes

  🇯🇵 Japão          941
  🇨🇳 China          825
  🇹🇼 Taiwan         363
  🇰🇷 Coreia do Sul  871

## O que já está no feed (não repita)

  - [japan] Daiwa Securities Group Backed Fund To Acquire Part Of Tokyo Garden Terrace Kioicho For Over 300 Billion Yen, N
  - [taiwan] Foxconn unveils three new EV models as it expands contract manufacturing push
  - [japan] Key points from the Bank of Japan governor's conference: Policy significance of reaching the 2% target, next i
  - [japan] Although the Bank of Japan judges that the underlying price level has reached the 2% target, good price increa
  - [japan] The Bank of Japan announced that the inflation rate has reached the 2% target and kept interest rates unchange
  - [japan] Analysts consider the Bank of Japan meeting to be hawkish even if it remains unchanged; focus on announcement 
  - [japan] Bank of Japan's underlying price increase rate “effectively reached 2% target”; policy interest rate unchanged
  - [china] BYD Company Limited Class A Stock 12‑Month Price Target Cut to CNY 111.26, Implies 35% Upside
  - [japan] BOJ keeps rates steady, declares victory in hitting price target
  - [japan] Analysts react to BOJ decision to keep rates steady
  - [japan] Bank of Japan believes that the inflation rate will reach 2% for the first time since the target was introduce
  - [taiwan] Intel tells Taiwan's chip suppliers to build service capacity early
  - [japan] Japan GDP Data Key to Timing Next BOJ Hike — Market Talk
  - [japan] 2% inflation target reached: Bank of Japan opinion
  - [japan] Janome Corp - To Buy Back Up To 5.98% Of Shares Worth 1 Billion Yen
  - [japan] Outlook for Economic Activity and Prices (October 2026, The Bank's View)
  - [japan] Statement on Monetary Policy
  - [japan] BOJ Hold Comes With Critical Shift in Inflation View — Market Talk
  - [china] The central bank launched a 7-day reverse repurchase of 15 billion yuan on October 30, with a net investment o
  - [china] The central bank launched a 15 billion yuan 7-day reverse repo on October 30, with a net investment of 15 bill
  - [japan] Yen gains after BOJ, AI jitters drive Treasury rally, weigh on dollar By Reuters
  - [japan] BREAKING NEWS: BOJ pledges to continue adjusting monetary accommodation
  - [japan] BOJ keeps interest rates steady, signals further rate hikes
  - [japan] Bank of Japan ETF sales pace doubles, completion time shortened from 112 years to 43 years (Mainichi Shimbun)
  - [japan] [Breaking News] Bank of Japan has determined that the ``underlying inflation rate'' target of 2% has been virt
  - [japan] Nikkei Extends Losses, Yen Strengthens After BOJ Decisions — Market Talk
  - [japan] Bank of Japan Holds Fire While Signaling Rate Hikes Ahead
  - [japan] BOJ SEES FY28 CORE CPI +2.0% VS. JULY 2.0%
  - [japan] BOJ SEES FY27 CORE CPI +2.6% VS. JULY +2.4%
  - [japan] BOJ SEES FY26 CORE CPI +2.5% VS. JULY 2.5%
  - [japan] Bank of Japan holds rates, says inflation trend hits target for first time
  - [japan] BOJ TO ADJUST POLICY TO ANCHOR UNDERLYING INFLATION
  - [japan] BOJ KEEPS VIEW: UPSIDE RISK TO PRICES
  - [japan] BOJ: AIMS TO STABILIZE UNDERLYING INFLATION AROUND 2%
  - [china] China's yuan hits over 4-year high, set for fourth monthly gain
  - [japan] Bank of Japan leaves policy rate unchanged at 1.25%
  - [japan] Bank of Japan decides to keep policy rate unchanged at 1.25% Monetary Policy Meeting
  - [japan] Bank of Japan Likely Declaring Win in Deflation Battle — Market Talk
  - [japan] Asia stocks tumble as AI spending concerns deepen; BOJ holds rates
  - [japan] BOJ: UNDERLYING INFLATION CONSISTENT WITH 2% TARGET

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
      "published_utc": "2026-10-30T04:52:43+00:00",
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

