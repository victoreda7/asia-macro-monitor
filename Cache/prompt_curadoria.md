atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-09T02:02:44.619370+00:00
Total: 2989 manchetes

  🇯🇵 Japão          1222
  🇨🇳 China          791
  🇹🇼 Taiwan         279
  🇰🇷 Coreia do Sul  697

## O que já está no feed (não repita)

  - [china] How China’s Stimulus May Shore Up GDP While Reinforcing Imbalances
  - [china] Chinese developer makes ARTEX AI agent closed-source after Korean bank hack
  - [japan] JGB Yields Lower Across Curve After U.S. Treasury Yield Declines — Market Talk
  - [china] The central bank launched a 2 billion yuan 7-day reverse repurchase operation today
  - [china] The Central Bank of China: Today it launched a 2 billion yuan 7-day reverse repurchase operation, with a biddi
  - [japan] Japan MOF To Auction Y2.2T Of TD-Bills Oct 19
  - [japan] Japan MOF To Auction Y3.3T Of TD-Bills Oct 16
  - [japan] Government Cabinet approves bill related to food consumption tax reduction
  - [korea] Key facts: Samsung Electronics (005930) Q3 Profit Jumps; Q4 Phone Cuts
  - [japan] Nikkei May Decline Amid Concerns About Energy Costs — Market Talk
  - [japan] JAPAN AUG HOUSEHOLD SPENDING Y/Y FALL LED BY LOWER PRIVATE UNIVERSITY TUITION, DOMESTIC PACKAGE TOUR COST, SUB
  - [japan] JAPAN AUG REAL CORE HOUSEHOLD SPENDING (EX-HOUSING, VEHICLES, GIFT MONEY) -4.2% Y/Y VS. -1.4% IN JULY WHEN OVE
  - [japan] IMF invites BOJ chief Ueda to speak on November 6
  - [japan] Japan's EV subsidies benefit Tesla more than Honda, Nissan
  - [china] Synopsys Looks To Work With Chinese AI Labs To Speed Up Chip Design, Nikkei Says
  - [china] CXMT, the semiconductor giant with the top Chinese market capitalization, begins mass production of next-gener
  - [taiwan] TSMC's AI Boom Just Got Bigger
  - [china] Sumitomo Bakelite to boost chip encapsulant output in China, Singapore
  - [china] Synopsys plans to explore working with Chinese AI labs on chip design tech: report
  - [china] Synopsys looks to work with Chinese AI labs to speed up chip design
  - [korea] Samsung, SK Hynix record earnings fuel South Korea spending on AI, youth
  - [china] China defends yuan policy as Europe steps up pressure over trade surplus
  - [korea] Cash Cat: CASHCAT begins KRW spot trading on Bithumb - 08 Oct 2026
  - [korea] October “Korea-US base interest rate ‘freezes’, stock market range strengthens”
  - [korea] Seoul shares down for 3rd day amid inflation worries
  - [korea] Samsung Electronics guides to huge surge in Q3 profits
  - [china] China Central Bank Defends Currency Policy Before EU Trade Talks
  - [china] Xin Yuan Enterprises Says Ocean Vivo To Make Pre-Conditional Voluntary Cash Offer
  - [taiwan] TSMC Taps GlobalFoundries In $2B AI Chip Deal, Putting GFS Stock On Track To Hit Over 1-Month High
  - [taiwan] Taiwan Semiconductor’s Sales Surged In September
  - [china] China defende política do iuan enquanto Europa intensifica pressão sobre superávit comercial
  - [taiwan] TSMC Sales Soar 50%. The Stock Is Falling Anyway
  - [taiwan] GlobalFoundries will manufacture essential component for AI chips for TSMC in US$2 billion deal
  - [taiwan] GlobalFoundries to make key AI chip component for TSMC in $2 billion deal
  - [taiwan] TSMC Stocks Drop 2% Despite Citi's NT$4,000 Target
  - [taiwan] September exports hit record monthly high, extend growth to 35 months
  - [taiwan] GlobalFoundries will manufacture a key AI chip component for TSMC
  - [taiwan] GlobalFoundries to make key AI chip component for TSMC
  - [japan] Prudential's Japanese unit involved in 5.2 bil. yen fraud
  - [taiwan] GlobalFoundries partners with TSMC to establish US-based production of silicon interposers

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
      "published_utc": "2026-10-09T02:02:44+00:00",
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

