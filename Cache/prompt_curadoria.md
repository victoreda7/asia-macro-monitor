atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-05T04:42:43.656595+00:00
Total: 3000 manchetes

  🇯🇵 Japão          880
  🇨🇳 China          894
  🇹🇼 Taiwan         318
  🇰🇷 Coreia do Sul  908

## O que já está no feed (não repita)

  - [japan] At the Bank of Japan's September interest rate hike meeting, there was an opinion that the pace should be acce
  - [japan] Sato Sho-Ji Corp - To Buy Back Up To 1.45% Of Own Shares Worth 900 Million Yen
  - [japan] Finance Directors’ Meeting leaves economic outlook unchanged as “moderate recovery”
  - [japan] Daicel Corporation - To Buy Back Up To 2.19% Of Own Shares Worth 8 Billion Yen
  - [china] China's yuan rebounds as PBOC lifts midpoint, dollar falls after Democrats take Congress
  - [japan] BOJ policymaker urged rate hike size debate: Sept. minutes
  - [japan] Tosoh Corp - To Buy Back Up To 3.9% Of Own Shares Worth 25 Billion Yen
  - [japan] Summary of the Bank of Japan's September meeting ``Policy rates should get closer to the goal as soon as possi
  - [china] Asian FX rises as dollar slides on U.S. vote, kiwi leads gains; yuan steadies
  - [japan] Japan’s large-cap exporters: Will the U.S. midterm sweep bring tariff relief?
  - [china] China indicts ex-Politburo member Ma Xingrui for bribery
  - [taiwan] Ukraine's top unmanned fleet developer looks to Taiwan for critical components
  - [china] China Banking Corp Reports Net Income Of 22.6 Billion Pesos In 9M2026
  - [china] China's largest import expo opens in Shanghai amid record trade imbalances
  - [japan] Stock values ​​fall, sell orders for AI semiconductor stocks following the results of the US midterm elections
  - [korea] Why is SK Hynix stock sliding today?
  - [taiwan] ELAN, Thunder Tiger, Gallopwave team up on 11 chips for all-domestic AI drones
  - [taiwan] The Central Bank’s Aboriginal Series Coin Set La’aruwa Tribe is on sale to the public on 11/12 | Sankei
  - [japan] Yen Strengthens on Hawkish BOJ Minutes
  - [korea] BOK chief to attend BIS governors' meeting in Switzerland
  - [korea] Why is Samsung Electronics stock plunging today?
  - [japan] Japan services PMI grows for fifth straight month in October By Investing.com
  - [japan] Japan services PMI grows for fifth straight month in October
  - [taiwan] Taiwan Inflation Likely Eased But Stayed High, WSJ Poll Shows — Market Talk
  - [china] China's curbs on tungsten used in drill bits squeeze AI supply chain
  - [korea] Samsung, SK hynix emerge as major bond investors amid chip boom
  - [japan] Tokyo's budget for next year's total requested amount exceeds 10 trillion yen for the first time, due to soari
  - [taiwan] Indonesian rupiah leads gains in Asian currencies; Taiwan dollar underperforms
  - [japan] BOJ debated need for more rate hikes, scope for faster moves, September minutes show
  - [japan] Mitsui Chemicals reportedly plans US$8.2B acquisition of JSR in Japan chip materials push
  - [korea] S.Korea’s current account surplus hits record $61 bn; Global IBs hike GDP growth forecasts
  - [china] China indicts ex-Politburo member Ma for bribery
  - [korea] S. Korea posts record high current account surplus of over $60b in Sept. on chip supercycle
  - [korea] Shares of Samsung Electronics and SK Hynix fell more than 40 to 50% from their high points, but the
  - [korea] Freeze the base interest rate... Adjusting the pace, not ending austerity
  - [korea] SK Hynix was counted as the largest net purchase by high-yield investors of Mirae Asset Securities u..
  - [japan] Upward price fluctuation risk, interest rate hike appropriate, policy “change in phase” Bank of Japan Septembe
  - [china] CHINA PBOC CONDUCTS CNY263 BLN VIA O/N REVERSE REPO THURS
  - [japan] BOJ Board Sees Little Capex Impact From Higher Rates, Minutes Show — Market Talk
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7156 THURS VS 6.7180

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
      "published_utc": "2026-11-05T04:42:43+00:00",
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

