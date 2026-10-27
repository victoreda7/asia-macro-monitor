atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-27T08:32:43.130795+00:00
Total: 3000 manchetes

  🇯🇵 Japão          964
  🇨🇳 China          846
  🇹🇼 Taiwan         380
  🇰🇷 Coreia do Sul  810

## O que já está no feed (não repita)

  - [japan] Japan Government Keeps Gradual Economic Recovery Outlook, Continues to Warn about Inflationary Impact of Linge
  - [china] China Railway Construction Heavy Industry January-September New Contracts, Bids Totalled 10.5 Billion Yuan
  - [china] BofA: China core semiconductor sales rise 24% in June-August
  - [japan] JAPAN’S GOVERNMENT UPGRADES ITS VIEW ON BUSINESS SENTIMENT AFTER UPBEAT Q3 TANKAN SURVEY, DOWNGRADES ASSESSMEN
  - [japan] JAPAN KEEPS GRADUAL ECONOMIC RECOVERY OUTLOOK IN MONTHLY REPORT, REPEATS ITS WARNING ABOUT IMPACT OF MIDEAST C
  - [china] China Industrial Profits Increase Notably
  - [taiwan] JIMTOF 2026 draws 94 Taiwan machine tool exhibitors
  - [korea] Kospi jumps as Samsung, SK Hynix rally on Anthropic IPO plan, payout hopes
  - [japan] Japan Vows to Fortify Cyber Defenses as GMO Hack Hits Forex Brokers
  - [japan] Top Japanese Chip Stocks to Watch Going Into Q3 Earnings, According to Bernstein
  - [taiwan] COST OF LIVING Taiwan's consumer confidence weakens in October
  - [japan] Japan life insurers offer mixed view of JGBs as foreign bond selling persists
  - [korea] The Export-Import Bank of Korea announced on the 27th that it has signed a business agreement with t..
  - [korea] South Korean shares end over 3% higher on US rally, strong GDP
  - [china] AI investment expansion encounters bottlenecks, the central bank is worried about financing risks and amplifie
  - [japan] Japan’s trend inflation index hits 3-year high, cements case for BOJ rate hike
  - [japan] Japan eyes 1 tril. yen private investment into Bangladesh over 5 yrs
  - [korea] Kospi Gains as Chip, Battery Stocks Advance
  - [korea] S.Korea’s 1% Q3 growth sets pace to beat BOK’s 3.3% annual forecast
  - [japan] CPI excluding special factors accelerates sharply in September, perhaps supporting Bank of Japan's 2% trend (R
  - [korea] Four years on, Lee Jae-yong steers Samsung from chip slump to AI boom
  - [korea] Chip boom drives Korea's surprise 1% GDP growth in Q3
  - [korea] While the Korean economy grew by surprise in the third quarter of this year on the back of semicondu..
  - [taiwan] PSMC capacity crunch holds back Jeju Semiconductor's growth
  - [korea] Korea should save chip boom windfall for downturns: IDB economist
  - [japan] Mr. Kuroda supports interest rate hike policy, Mr. Wakatabe is cautious. Former Bank of Japan leaders write on
  - [china] The central bank's reverse repurchase net investment today was 1.014 billion yuan, and the China Development B
  - [korea] SK Hynix Set for Record Revenue, Operating Profit in Third Quarter — Earnings Preview
  - [japan] Japan stands ready to take decisive action in currency market, finance minister says
  - [china] The central bank revealed that foreign capital, which was the key to the depreciation of the Taiwan dollar, ha
  - [japan] CPI excluding special factors accelerates rapidly in September, perhaps supporting Bank of Japan's 2% trend (R
  - [china] UK’s tariffs on Chinese diggers challenged by Caterpillar
  - [taiwan] Taiwan central bank sees strong tech demand driving exports into 2027
  - [china] China 5-Year Yield Hits Record Low on PBOC’s Cash Injection
  - [japan] Yen eases on risk-on mood ahead of central bank bonanza
  - [taiwan] Nvidia, Chipmakers Face Higher Costs? TSMC Reportedly Plans Up To 20% Price Hike For Advanced Chip Packaging
  - [japan] Indicators for Core CPI
  - [japan] Yen eases on risk-on mood ahead of central bank bonanza By Reuters
  - [japan] Cybersecurity - Rising risks, ``threat to the financial system'' - Bank of Japan board member (Reuters)
  - [japan] Rising cybersecurity risks, ``a threat to the financial system'' - Bank of Japan board member (Reuters)

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
      "published_utc": "2026-10-27T08:32:43+00:00",
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

