atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-20T07:04:34.715973+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1043
  🇨🇳 China          908
  🇹🇼 Taiwan         320
  🇰🇷 Coreia do Sul  729

## O que já está no feed (não repita)

  - [china] China's October coal imports from Australia hit six-year high
  - [korea] South Korean shares hit 10-month low as chipmakers slump on US tech selloff
  - [taiwan] Foxconn Technology: Global manufacturing capabilities support gaming, casing and thermal products, alongside E
  - [japan] Nikkei average closing price drops by 3007 yen Confusion over AI
  - [korea] SK Hynix weighs converting Kioxia bonds to shares, report says
  - [korea] The top 1% return on stock investment, which sold the largest amount of Samsung Electronics' common
  - [korea] JPMorgan initiates BOK Financial stock coverage with neutral rating
  - [taiwan] Selling wave in chip stocks leads Taiwan to worst week since 1990; Asian stock markets fall
  - [china] Asian stocks slump on Wall Street decline, PBoC rate hold, hotter Japan inflation, and muted Xi-Trump-Putin su
  - [korea] Samsung Electronics Appoints New Memory-Chip Business Head
  - [japan] JGB yields track US peers lower; data signals foreign investors lead yield moves
  - [taiwan] TSMC tightens China AI chip curbs as new US rules close manufacturing loophole, sources say
  - [japan] Why is the Japanese yen rising today?
  - [japan] Why is the Japanese yen rising today? By Investing.com
  - [japan] Meiji Restoration “Abolition of tax system to promote wage increases for small and medium-sized enterprises” t
  - [china] Cathie Wood’s ARK Invest Loads Up $90M In Anthropic Shares, Dumps Nvidia As China Chip Sale Woes Deepen
  - [korea] The attention of the Bank of Korea’s Monetary Policy Committee in November… Weighing down on interest rate hik
  - [japan] Japan's October core CPI rises to 2.2%, misses estimates, and headline inflation hits 11-month high
  - [china] China's October soybean imports fall 23% as Brazil shipments decline
  - [korea] SK Hynix's single-stock leverage product, which had raised expectations that it could double profits..
  - [japan] Balance of the Fiscal Loan Fund (End of October 2026)
  - [china] China's refined copper imports set to jump in 2027, traders and analysts say
  - [china] China Has Capacity, But Maybe Not the Will to Boost Fuel Exports
  - [china] PBOC Anchors Yuan With Stable Fix as Volatility Jumps After APEC
  - [korea] Samsung Management Shuffle Aimed at Strengthening Competitiveness of Semiconductor Business
  - [china] China home prices seen falling again in 2027, Reuters poll shows
  - [taiwan] Why is TSMC stock sliding today?
  - [korea] Samsung Electronics: Hwang Previously Led Development of Memory Products Including DRAM, HBM
  - [china] Preços dos imóveis na China devem cair novamente em 2027, aponta pesquisa da Reuters
  - [korea] Samsung Electronics Names Sang Joon Hwang as Head of Memory Business
  - [korea] Samsung Electronics Appoints New Memory Business Chief
  - [china] China yuan recovers from one-month low on exporter demand, strong dollar caps gain
  - [china] Alibaba puts quixotic faith in made-in-China chips
  - [china] China Solar Cell Exports Rise for Second Month on Tariff Rush
  - [china] China's fuel oil exports for bunkering ease in October while imports rebound
  - [japan] Result of Liquidity Enhancement Auction on November 20, 2026(For JGB Market Special Participants)
  - [japan] Japan Core CPI Likely to Accelerate to 2.7% in November — Market Talk
  - [japan] Finance Minister Katayama: JT’s huge loss “will not affect growth investment”
  - [japan] The consumer price index rose 2.2% in October, exceeding the Bank of Japan's 2% target for the second consecut
  - [china] The unexpired balance of the central bank's MLF remains unchanged at 7.4 trillion yuan, with 1 trillion yuan d

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
      "published_utc": "2026-11-20T07:04:34+00:00",
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

