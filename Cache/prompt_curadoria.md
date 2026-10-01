atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-01T21:02:44.998354+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1284
  🇨🇳 China          789
  🇹🇼 Taiwan         249
  🇰🇷 Coreia do Sul  678

## O que já está no feed (não repita)

  - [china] China shortens leash on property developers
  - [korea] Samsung Electronics Stocks Gain 2.8% as Micron Reinforces Memory Scarcity
  - [japan] BOJ debated more rate hikes to adjust 'accommodative' conditions: opinion summary
  - [china] Exclusive-US slows aircraft-part exports to China as Trump seeks leverage in trade negotiations, sources say
  - [china] 45% YTD rally! Experts see up to 56% upside in these 3 stocks on China's export shift | Target, rationale
  - [korea] Samsung raises Galaxy S26 prices by $100 amid chip shortage
  - [china] DGTR recommends anti-dumping duty on tuberculosis drug ingredient imports from China, Thailand
  - [china] IMF says extension of tariff truce between US and China increases trade predictability
  - [china] IMF says US-China tariff truce extension enhances trade predictability
  - [china] In Depth: What’s in the China-U.S. Tariff Truce, and What’s Left Unsettled
  - [china] Xi-Trump meeting’s takeaways, successes and fallout: 7 US-China relations reads
  - [korea] S.Korea Sept exports hit record high as AI boom drives chip sales to all-time peak
  - [china] EU sees worrying rise in imports from China, official says
  - [china] China driving worrying rise in EU imports, Commission official says
  - [taiwan] Taiwan's manufacturing activity expands at fastest pace in five years
  - [china] US reduces exports of aircraft parts to China as Trump seeks advantage in trade talks: sources
  - [china] Russia will increase exports of sunflower oil to China, war affects sales to India
  - [china] Brazil Steelmakers See New Import Threats as China Share Falls
  - [korea] SK hynix reiterates no decision made on Solidigm financing despite dual-listing reports
  - [korea] Lotte expands financial, export support for partners
  - [japan] Kumamoto Earthquake: National government takes financial measures for prefecture reconstruction fund Fujii, Mi
  - [china] China's BYD sales rise in September as export boom sustains momentum
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
  - [china] Oil price rises 4% after news that China has suspended fuel exports and that American troops are on their way 
  - [japan] Japan to Map Out First Five Years of Takaichi’s Investment Plan
  - [japan] Japan to Detail First Five Years of Takaichi Investment Plan
  - [china] China's Latest Stimulus Package Could Be Beginning of New Policy Support Round — Market Talk
  - [china] Chinese refiners suspend October fuel exports, sources say

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
      "published_utc": "2026-10-01T21:02:45+00:00",
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

