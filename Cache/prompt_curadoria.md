atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-05T02:22:44.332690+00:00
Total: 2864 manchetes

  🇯🇵 Japão          1225
  🇨🇳 China          758
  🇹🇼 Taiwan         238
  🇰🇷 Coreia do Sul  643

## O que já está no feed (não repita)

  - [taiwan] Taiwan dollar gains most among muted Asian currencies
  - [china] UK Expected to Follow EU With Tariffs on Chinese EVs, Times Says
  - [japan] Japan services PMI misses forecasts in September as private-sector growth slows By Investing.com
  - [japan] Japan services PMI misses forecasts in September as private-sector growth slows
  - [japan] Japan's Rapidus To Help 17 Companies Design Chips For Clients, Nikkei Says
  - [japan] Interview: The role of reflation policy has ended, and demand expansion from here is a "risk" - Former Bank of
  - [japan] Japan service sector activity slows from 5-month high, PMI shows
  - [japan] BOJ's Uchida flags AI's mixed impacts on productivity
  - [japan] Opening Remarks by Deputy Governor UCHIDA at the ECONDAT 2026 Fall Meeting (AI, Big Data, and Monetary Policy)
  - [japan] Reflationist ex-BOJ policymaker calls end to low rates, big spending
  - [japan] JGBs Mixed Ahead of Expected Extraordinary Diet Session in Japan — Market Talk
  - [japan] Sources of Changes in Current Account Balances (Projections for Oct.)
  - [japan] Extraordinary Diet convenes today to debate consumption tax reduction bill, etc.
  - [korea] Mortgage interest rates are also ‘fluctuating’… Will interest rates rise further due to the additional hike by
  - [china] U.K. is said to plan tariffs on Chinese EVs under pressure from EU
  - [china] Britain set to levy tariffs on Chinese electric cars, The Times reports
  - [japan] Is a variable type home loan still more advantageous? Should I switch to a fixed rate due to concerns that wil
  - [japan] Although he was almost seriously injured due to tiles falling off the exterior wall...the condominium manageme
  - [japan] The “biggest problem” of the Japanese economy is not “fiscal deficit” but “corporate surplus” (Diamond Online)
  - [china] Britain expected to impose tariffs on Chinese electric cars, The Times reports
  - [japan] It's not Prime Minister Takaichi's fault or the Bank of Japan's fault...The name of the politician pointed out
  - [japan] <Special Discussion> The US could impose up to 100% tariffs on countries that support Russia...If the Democrat
  - [japan] ``It is best for the petrochemical business to be independent,'' says Resonac CFO, who is in a hurry to focus 
  - [japan] Japan's Rapidus to help 17 companies design chips for clients
  - [korea] Trump threatens tariffs of up to 300% as Korea faces pressure over US investment
  - [korea] Foreign investors sell W20.3tr in Korean stocks, led by SK hynix and Samsung Electronics
  - [japan] Japan adds Garantex to list of Russia sanctions over Ukraine war
  - [china] Russian exporters fight to win back Chinese buyers amid fallout over fake goods
  - [korea] K consumer goods stocks, which had been spotlighted as "export stocks" due to the foreign consumptio..
  - [japan] Liberal Democratic Party Policy Research Council Chairman Kobayashi strengthens his approach to opposition par
  - [japan] Takaichi policy speech, Malaysia budget, Pacific islands climate summit
  - [japan] Is it no longer reliable? ...The Bank of Japan will also quietly make a decision in 2026. Why Hello Work's eff
  - [japan] Iran’s rial hits fresh low as $2 billion currency intervention fails to stem slide
  - [japan] Kringle Pharma, a drug discovery venture from Osaka University and Keio University, is expected to reduce its 
  - [korea] On September 15, the "2026 BOK Regional Economic Symposium" was held at the Lotte City Hotel in Daej..
  - [korea] The prolonged high interest rate has increased the interest expense on loans borne by households by
  - [japan] This is the complete picture of Obata's theoretical system (21st century economic theory)...Entertainment, ecs
  - [japan] Trump warmly welcomes Xi Jinping at the U.S.-China summit meeting...Why Americans' "feelings toward China have
  - [taiwan] Iranian rial at new low, as cenbank sells dollars to support currency
  - [taiwan] Musk confirms talks with TSMC over his Texas chip factory project

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
      "published_utc": "2026-10-05T02:22:44+00:00",
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

