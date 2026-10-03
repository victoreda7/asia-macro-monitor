atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-03T03:42:45.410483+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1287
  🇨🇳 China          790
  🇹🇼 Taiwan         249
  🇰🇷 Coreia do Sul  674

## O que já está no feed (não repita)

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
  - [china] Soybeans slump on dimming hope of Chinese tariff cuts
  - [china] Man Charged by US With Illegally Shipping Nvidia Chips to China
  - [japan] Japan hits Russia 'shadow fleet' in 1st sanctions since Putin trip to disputed isle
  - [japan] Number of U.S. employed workers falls significantly below market expectations Expectations of Fed interest rat
  - [china] China Aoyuan Announces Disposal Of Assets By Receivers
  - [japan] Eurozone consumer prices rose 3.8% in September, the highest level in three years
  - [japan] Former Liberal Democratic Party Chairman Miyazawa: “It is better not to reduce the consumption tax”
  - [korea] Trump says South Korea trade deal adds $8.4B oil project
  - [china] China’s C919 jet faces further delivery delays amid US export chill: analysts
  - [japan] Yen market price rises, dollar sold due to fall in crude oil futures prices
  - [japan] Mitsubishi Heavy to invest 100 bil. yen to ramp up shipbuilding capacity
  - [japan] Dollar flat ahead of payrolls as yen firms, hot euro inflation keeps ECB in focus
  - [japan] Japan finance minister: Government united in view reflation is over
  - [japan] Prime Minister Takaichi “plans to leave monetary policy to the Bank of Japan,” Finance Minister Satsuki Kataya
  - [japan] Consumption tax reduction bill approved at Liberal Democratic Party joint meeting, with calls for clarificatio
  - [korea] South Korea’s Sept inflation cools to 2.9% on fuel caps, lower farm prices
  - [korea] European Chip Stocks Rally after Report Samsung Ups Prices — Market Talk
  - [china] SK Innovation, Aramco-backed S-Oil rally as China export bans add to global fuel strain
  - [taiwan] Manufacturing sector flashes 'green' light in August
  - [china] China seen doing ‘just enough’ with targeted fiscal support to defend GDP growth
  - [china] China fuel export suspension to choke supplies in Asia

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
      "published_utc": "2026-10-03T03:42:45+00:00",
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

