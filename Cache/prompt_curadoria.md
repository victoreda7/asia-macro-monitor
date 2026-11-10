atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-10T03:02:43.042633+00:00
Total: 3000 manchetes

  🇯🇵 Japão          934
  🇨🇳 China          887
  🇹🇼 Taiwan         321
  🇰🇷 Coreia do Sul  858

## O que já está no feed (não repita)

  - [china] China exports stay resilient as trade surplus tops $1tn
  - [china] China’s trade surplus soars past $1 trillion, October exports jump 35.2% y/y
  - [china] China's October coal imports fall 6% year-on-year
  - [china] China Oct Exports +28.7% on Year in Yuan Terms
  - [china] China Oct Imports +34.7% on Year in Yuan Terms
  - [china] China Oct Trade Surplus CNY712.78B
  - [china] China Oct Trade Surplus $105.28B; Expected Surplus $126.9B
  - [china] China Oct Exports +35.2% on Year; Expected +36.1%
  - [china] China Oct Imports +41.6% on Year; Expected +34.0%
  - [japan] BOJ estimates $6 billion annual gain from faster ETF sales, finance minister says
  - [china] The central bank launched a 190 billion yuan overnight reverse repurchase operation in the open market today
  - [japan] Monetary policy method ``Everything is decided by the Bank of Japan'', no effect on ETF sales = Finance Minist
  - [korea] South Korea’s defense export boom exposes cockpit display vulnerability
  - [taiwan] IEAT and the Export-Import Bank of China signed an MOU to join forces to help enterprises expand into internat
  - [korea] Korean stocks rebound as chip giants lead recovery
  - [japan] ``I ate 180,000 yen sushi with my wife'' and ``Prices are rising.'' Pros and cons of Shinjuku ward councilor's
  - [china] On November 10, the central bank launched a 190 billion yuan overnight reverse repurchase operation.
  - [korea] Will the Bank of Korea put a brake on interest rate hikes as stock prices plummet?
  - [china] Chinese chip firms Denglin, Xinde open mixed in Hong Kong debuts
  - [japan] At the October meeting of the Bank of Japan, many voices called for interest rate hike “quickly”; it is import
  - [japan] Bank of Japan debated need for faster rate hikes, October summary shows
  - [japan] Consumption tax reduction bill to be debated in the House of Councilors tomorrow; ruling and opposition partie
  - [korea] “$40,000 export contract”... KOMIPO supports overseas expansion of AI and robotics SMEs at Robotworld
  - [japan] Japan has agreed to provide 4.3 billion yen (about 36.6 billion won) worth of defense equipment to t..
  - [china] China busca obter vantagem em alta tecnologia em um setor que responde por 80% do comércio mundial
  - [korea] With Samsung Electronics and SK Hynix set to return 200 trillion won to shareholders this year...“For share pr
  - [korea] A company that imported tens of billions of won worth of magnesium alloys, mixed them with its own p..
  - [china] CHINA PBOC CONDUCTS CNY190 BLN VIA O/N REVERSE REPO TUES
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7167 TUES VS 6.7188
  - [china] The "anchor change" of the central bank's policy interest rate has been implemented smoothly, and the precisio
  - [korea] Louis Vuitton hit by stock slump, stronger won in South Korea
  - [taiwan] Semiconductor test-interface supplier WinWay revenue falls 11.51% MoM, rises 62.62% YoY
  - [taiwan] ePaper manufacturer E Ink to buy manufacturing plant in Taiwan for NT$2.78 billion, teams with Taiflex on AI m
  - [japan] Japanese chipmaker Rapidus targets Taiwan’s chip cluster model, plans 3 more Hokkaido plants
  - [taiwan] Exclusive: Quantum beyond quantum—Photarix bets on a new era of semiconductor photonics
  - [japan] Next interest rate hike: ``Implement when possible'': Bank of Japan members' opinions at the October decision 
  - [japan] As underlying inflation reaches 2%, multiple opinions say it is necessary to raise interest rates to a neutral
  - [japan] Nikkei Stock Average temporarily recovers to 60,000 yen level, buy orders centered on semiconductor-related st
  - [taiwan] Systex hits record October revenue on overseas semiconductor expansion
  - [japan] Bank of Japan member says rate hike should be done when possible (Kyodo News)

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
      "published_utc": "2026-11-10T03:02:43+00:00",
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

