atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-04T15:52:45.451110+00:00
Total: 2860 manchetes

  🇯🇵 Japão          1222
  🇨🇳 China          756
  🇹🇼 Taiwan         237
  🇰🇷 Coreia do Sul  645

## O que já está no feed (não repita)

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
  - [japan] This is the complete picture of Obata's theoretical system (21st century economic theory)...Entertainment, ecs
  - [japan] Trump warmly welcomes Xi Jinping at the U.S.-China summit meeting...Why Americans' "feelings toward China have
  - [taiwan] Musk confirms talks with TSMC over his Texas chip factory project
  - [china] How US-China tech ties are deepening as RISC-V chips go mainstream
  - [china] Why India’s Manufacturing Future Isn’t the China Model
  - [japan] Pros and cons of 1% food consumption tax What are the tax reduction effects?
  - [china] Can Britain really afford to diverge from EU tariffs on Chinese EVs?
  - [japan] OPINION: Japan must improve fiscal credibility as long-term rates rise
  - [korea] Trump Touts 'Better' South Korea Trade Deal With $8.4 Billion Oil Project, But Seoul Says It Wasn’t Part of th
  - [japan] What, wasn't it the Bank of Japan's fault? …Reiwa’s Black Monday is a bigger factor than the “Ueda shock”
  - [japan] Bank of Japan September Tankan Business conditions DI for manufacturing industry worsens Kagawa Prefecture (KS
  - [japan] The importance of the Bank of Japan's words "change in circumstances" (Hiroyuki Kubota) - Expert
  - [japan] U.S. employment statistics show a lower-than-expected 29,000 increase in September...unemployment rate rises f
  - [korea] "The Federal Reserve and the Bank of Korea will freeze interest rates in October... USD-KRW 1,345-1,370 expect
  - [korea] US firms add just 29,000 Jobs, unemployment rate ticks up
  - [korea] The Bank of Korea said, “Raising interest rates will help stabilize inflation and housing prices.”
  - [japan] What will happen to the relationship between Prime Minister Takaichi, who was supposed to be a ``reflationist,
  - [japan] One of the reasons why the yen continues to depreciate is the Bank of Japan's "fiscal subordination" issue, an
  - [japan] One of the reasons why the yen continues to depreciate is the Bank of Japan's "fiscal subordination" issue, an
  - [korea] Trump pushes South Korea on $54B Alaska LNG venture, warns of tariff hikes
  - [japan] IBM/GE → Unemployment, Entrepreneurship, Publishing, National University Professor's ``University Professor fr
  - [japan] Japan local governments step up Taiwan outreach for chip investment
  - [japan] Hedge Funds Are Rebuilding Short Bets Against Japan’s Yen
  - [japan] What's coming to the former Bank of Japan Kanazawa branch? The artworks on display will be... 21st century wil
  - [taiwan] TSMC Stocks Jump 3.1% as High-NA Road Map Targets 2030
  - [korea] ASML Stocks Surge 3.5% as Samsung Pulls High-NA Into DRAM
  - [japan] Dollar set for first 3-week win streak since January, euro rebounds and yen gains
  - [japan] Behind-the-scenes circumstances behind Indonesia's resumption of imports of "Japanese used trains" What happen
  - [taiwan] Taiwan Semiconductor Stock Rises on Broadcom's $60 Billion Chip Deal

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
      "published_utc": "2026-10-04T15:52:45+00:00",
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

