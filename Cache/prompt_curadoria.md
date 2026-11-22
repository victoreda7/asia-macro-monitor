atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-22T21:32:41.438499+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1032
  🇨🇳 China          930
  🇹🇼 Taiwan         322
  🇰🇷 Coreia do Sul  716

## O que já está no feed (não repita)

  - [china] US seeks answers on Nvidia’s sale of chips to China, Bessent says
  - [china] US seeks answers on sale of Nvidia chips to China, says Treasury secretary
  - [korea] The last Monetary Policy Committee meeting of the year on the 26th... Interest rate expected to rise to 3.25%
  - [china] One Stanley developer reports alleged extortion bid involving ‘tens of millions’
  - [china] The associate of Alice Huang who funneled Nvidia chips to China - WSJ
  - [korea] The Bank of Korea is likely to raise interest rates this week... tighten the reins
  - [japan] Corporate Japan races to revive rare-earth supply chain amid China curbs
  - [china] Chinese-made cars take 34% of S.Korea's EV market, driving record auto trade deficit
  - [korea] All Hankyung economists said, “The base interest rate will be increased by 0.25% this month.”
  - [korea] All Hankyung economists say, “Interest rate will be increased by 0.25% this month”
  - [china] The founder of China's CATL, the world's largest battery company, donated more than 2.5 billion yuan..
  - [korea] “Further tightening is likely due to high inflation… base interest rate 0.25%P ↑ on the 26th”
  - [korea] [Weekly Economic, Crypto Calendar] FSC to Unveil Government Draft of Digital Asset Law; BOK Rate Decision Due
  - [japan] FOCUS: AI boom fuels corporate investment as Japan consumers tighten purse strings
  - [korea] Inflation and growth rate upward adjustment... Will the Bank of Korea raise the base interest rate to 3.25%?
  - [korea] BOK likely to hike interest rate on resilient growth, inflation
  - [korea] BOK likely to lift rate on resilient growth, inflation
  - [korea] Although Korea recorded the world's highest export growth this year, surpassing $1 trillion in annua..
  - [korea] Samsung, LG face risk of higher costs as EU appliance makers seek carbon levies on imports
  - [japan] Consumer price index in Sendai City increased by 1.9% compared to the same period last year (KHB East Japan Br
  - [korea] S. Korea expected to become world's 4th-largest exporter this year
  - [korea] Korean ramen exports surpassed last year's annual performance for the first time in 10 months this y..
  - [china] The Alice Huang Associate Accused of Funneling Nvidia Chips to China — WSJ
  - [korea] At the last Monetary Policy Committee meeting of the year, the Bank of Korea is likely to raise interest rates
  - [korea] Both prices and growth rise… Even though the market is difficult, “the Bank of Korea’s interest rate rises”
  - [korea] With the burden of growth and prices increasing, will the Bank of Korea raise interest rates at the last Monet
  - [japan] There are no ``main disagreements'' with the BOJ's ``main opinions''; cautious arguments by members Asada and 
  - [japan] What will happen to Japan's "salaries" and "prices" if Trump loses... Experts warn of double punch to househol
  - [korea] [Global economic indicators] New York stock market likely to be quiet on ‘Thanksgiving’… Pay attention to the 
  - [korea] “The Bank of Korea will raise the base interest rate on the 26th” in one voice… 9 out of 10 “3.50% next year” 
  - [korea] Pay attention to PCE in October in the US... Korean bank reveals revised growth rate for this year [Han Dong-h
  - [korea] Will the Bank of Korea resume raising interest rates? Interest in US PCE and growth rate [Han Dong-hoon's Week
  - [korea] Rapid growth rate, unpredictable prices... Bank of Korea expected to raise interest rates this week
  - [korea] The Bank of Korea expects to resume raising interest rates for the first time in three months... “Austerity un
  - [korea] [This week's Monetary Policy Committee] Bank of Korea tightens again due to high inflation and high growth... 
  - [china] Canada deepens trade relations with China, Chen Mingqi warns of risks of economic coercion from Beijing | Poli
  - [china] Treasury secretary rules out further restrictions on Nvidia chip sales to China
  - [china] Treasury secretary rules out further curbs on Nvidia chip sales to China
  - [china] Elon Musk revisits Tesla Shanghai factory after 3 years, praises China manufacturing
  - [china] Goldman upgrades China H-shares on faster earnings growth outlook

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
      "published_utc": "2026-11-22T21:32:41+00:00",
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

