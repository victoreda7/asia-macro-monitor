atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-09T03:22:43.992209+00:00
Total: 3000 manchetes

  🇯🇵 Japão          936
  🇨🇳 China          871
  🇹🇼 Taiwan         331
  🇰🇷 Coreia do Sul  862

## O que já está no feed (não repita)

  - [taiwan] Malaysia-Taiwan fraying ties threaten future chip investments
  - [japan] Mitsui Chemicals to Acquire JSR With Development Bank of Japan for $8.8 Billion
  - [japan] Japan Spent Record $50 Billion in Single Day to Bolster Yen
  - [china] China extends suspension of 24% tariff on US imports for two months
  - [china] Decision Effective 1:01 p.m. Local Time Tuesday, Customs Tariff Commission of the State Council Says
  - [china] China to Continue to Suspend 24% Additional Tariff on U.S. Goods for Two Months
  - [china] China to Retain 10% Additional Tariff Rate on U.S. Goods for Two Months
  - [japan] BREAKING NEWS: Mitsui Chemicals to buy chip material supplier JSR for 1.84 tril. yen
  - [japan] Foreign exchange intervention revealed to be “largest ever” at 8 trillion yen The government and the Bank of J
  - [taiwan] Taiwan chipmaker CEO warns memory price rises are unsustainable
  - [korea] Samsung Electronics, SK hynix trade mixed after two-day plunge last week
  - [china] China CPI inflation misses forecasts in Oct; factory-gate prices accelerate
  - [japan] Mitsui Chemicals: Development Bank of Japan to Jointly Invest in JSR
  - [korea] South Korean won gains most among subdued Asian FX
  - [china] China Producer Inflation Accelerates to Over Four-Year High
  - [china] China’s factory-gate inflation gains momentum in October, consumer price pressures stay muted
  - [japan] Mitsui Chemical Says It Will Sell Shares Worth Up To 150 Billion Yen To Help Finance Jsr Acquisition
  - [korea] Citi: "If semiconductor exports are sluggish, the Bank of Korea is likely to cut its base interest rate in the
  - [korea] Citi: "If the semiconductor industry declines, interest rates will be cut in the second half of next year... I
  - [china] China Consumer Prices Flat In September
  - [china] CHINA OCT NON-FOOD PRICES +1.5% Y/Y VS +1.5% Y/Y SEP
  - [china] CHINA OCT FOOD PRICES -2.9% Y/Y VS -1.7% Y/Y SEP
  - [china] CHINA OCT CPI +0.0% M/M VS +0.2% M/M SEP
  - [china] CHINA OCT PPI +0.7% M/M VS +1.2% M/M SEP
  - [china] China's consumer price index rose 0.7% in October (Kyodo News)
  - [taiwan] Nittobo's T-Glass supply crunch deepens despite 3.6-fold capacity expansion plan for AI chips
  - [taiwan] Weekly news roundup: AI compute race intensifies as DRAM rivals diverge and chipmakers expand investments
  - [china] CHINA PBOC CONDUCTS CNY182 BLN VIA O/N REVERSE REPO MON
  - [china] On November 9, the central bank launched a 182 billion yuan overnight reverse repurchase operation.
  - [china] China's October producer inflation quickens further, consumer prices edge down
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7188 MON VS 6.7168
  - [china] China Oct Non-Food Prices +1.5% on Year
  - [china] China Oct Food Prices -2.9% On Year
  - [china] China Jan-Oct CPI +0.9% on Year
  - [china] China Oct CPI 0.0% on Month
  - [japan] Japan MOF To Auction Y250.0B Of 10-Year CPI-Indexed Bonds Nov 16
  - [china] China Oct CPI +0.7% on Year; Market Expected +0.8%
  - [korea] Citi: “Despite the decline in stock prices, we will raise the base interest rate this month… If the semiconduc
  - [china] Consumer prices in October 2026 increased by 0.7% year-on-year
  - [korea] What will the interest rates be next year? “If the semiconductor industry collapses, the Bank of Korea will al

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
      "published_utc": "2026-11-09T03:22:44+00:00",
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

