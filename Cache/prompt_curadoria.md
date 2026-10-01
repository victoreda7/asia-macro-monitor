atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-01T13:12:49.152009+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1291
  🇨🇳 China          779
  🇹🇼 Taiwan         250
  🇰🇷 Coreia do Sul  680

## O que já está no feed (não repita)

  - [china] US reduces exports of aircraft parts to China as Trump seeks advantage in trade talks: sources
  - [china] US slows aircraft-part exports to China as Trump seeks leverage in trade negotiations, sources say
  - [china] Russia will increase exports of sunflower oil to China, war affects sales to India
  - [korea] SK hynix reiterates no decision made on Solidigm financing despite dual-listing reports
  - [korea] Lotte expands financial, export support for partners
  - [japan] Kumamoto Earthquake: National government takes financial measures for prefecture reconstruction fund Fujii, Mi
  - [china] China's BYD sales rise in September as export boom sustains momentum
  - [japan] Euro slides to 17-month low, hit by rates and inflation mix By Reuters
  - [japan] Euro slides to 17-month low, hit by rates and inflation cocktail By Reuters
  - [japan] Globaltec Formation Says GOH Min Yen Appointed As Executive Director
  - [china] Oil prices rise 2% as China suspends fuel exports
  - [japan] Yen market price falls by more than 1 yen due to rise in long-term interest rates in the United States
  - [china] VIEW Chinese refiners suspend October fuel exports, sources say
  - [japan] [Approaching the 160 yen level again] Reasons why the trend of ``returning to a weak yen'' remains unchanged d
  - [japan] Dollar holds as elevated U.S. yields overshadow cooling inflation data
  - [japan] Bank of Japan Tankan Large Enterprises/Non-Manufacturing Index worsens for the first time in five quarters (AB
  - [japan] Nikkei closes at highest level in six weeks; Micron predictions boost semiconductor stocks
  - [japan] Main opinions expressed at the Bank of Japan's September meeting: ``I will refrain from commenting beyond publ
  - [japan] Bank of Japan Tankan Economic judgment of large companies in manufacturing industry improves for 6th consecuti
  - [japan] Bank of Japan releases “main opinions” from September meeting, also points out the possibility of accelerating
  - [korea] Bank of Korea plans gold purchase from domestic producers in December
  - [japan] Japan to Detail First Five Years of Takaichi Investment Plan
  - [china] China's Latest Stimulus Package Could Be Beginning of New Policy Support Round — Market Talk
  - [china] Chinese refiners suspend October fuel exports, sources say
  - [japan] Flat 35 interest rate is the highest ever at 3.830%
  - [japan] Yen Falls After Japan Q3 Tankan Survey Data
  - [japan] Japan PM vows to underpin yen by boosting economic competitiveness
  - [korea] While U.S. Micron, the third-largest memory chipmaker, was the first to start its earnings season sm..
  - [korea] The appointments of Deputy Prime Minister and Minister of Finance and Economy Lee Hyung-il and Minis..
  - [japan] ``Main opinions'' announced at Bank of Japan's September meeting; no comments on continuous interest rate hike
  - [taiwan] Taiwan extends fuel freeze, seeks extra subsidies for CPC, Taipower
  - [china] Guangzhou Caps Deposits, Tightens Oversight in Housing-Sales Overhaul
  - [china] China Cancels Some Fuel Shipments to Support Domestic Supply
  - [china] ZAWYA: Why East African banks are joining yuan payment system ?
  - [korea] ZAWYA: How Kenya won back Rwanda’s oil cargo imports ?
  - [japan] Japan PM says govermentt steps will strengthen market confidence in yen
  - [korea] S.Korea Sept exports hit record high as AI boom drives chip sales to all-time peak
  - [japan] Stock price rises by 2,200 yen Buy orders spread to AI/semiconductor related stocks
  - [japan] Main opinions from the September meeting of the Bank of Japan: If there are signs of upward movement in prices
  - [japan] Nikkei logs six-week closing high as Micron forecast lifts chip stocks

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
      "published_utc": "2026-10-01T13:12:49+00:00",
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

