atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-27T20:33:24.334175+00:00
Total: 3000 manchetes

  🇯🇵 Japão          953
  🇨🇳 China          854
  🇹🇼 Taiwan         382
  🇰🇷 Coreia do Sul  811

## O que já está no feed (não repita)

  - [japan] Today's Japan-German summit meeting to confirm supply chain strengthening, etc.
  - [china] WuXi AppTec Co., Ltd. Class A Stock 12‑Month Price Target Raised to CNY 202.63, Implies 39% Upside
  - [korea] SK Hynix Stock Jumps as Massive Payout Rumors Swirl
  - [taiwan] TSMC Gets Fresh Pricing Power From AI Chip Boom
  - [japan] Japan banks, fintech step up digital currency push for trade settlements
  - [korea] Samsung Electronics Stocks Gain 4.23% With Cash-Return Decisions Approaching
  - [china] China Claims Strong Economic Growth, but Skeptics Question Official Figures — WSJ
  - [korea] SK Hynix's Solidigm Reportedly In Talks Over $45B Investment In US Chip Plant
  - [korea] SK Hynix $155 call OI leads options chain as 6.7% Q3 swing looms
  - [japan] Japan's EV subsidies face uncertain future as country's 'DOGE' takes aim
  - [korea] SK hynix Stocks Gain 5.18% Before Its Payout Plan Faces Board Scrutiny
  - [china] Portuguese president condemns violence, calls for ending housing crisis
  - [china] Xinjiang Beixin Road & Bridge Q3 Net Loss At 163.1 Million Yuan
  - [japan] Dollar firms ahead of central bank meetings, steadier stocks stall safe haven play By Reuters
  - [china] Geovis Technology Q3 Net Loss At 171.9 Million Yuan
  - [china] WuXi AppTec Co., Ltd. Class A Stock 12‑Month Price Target Raised to CNY 200.32, Implies 37% Upside
  - [japan] Opinion of the expert panel regarding the three security documents, “Tax increases are not excluded as an opti
  - [korea] S.Korea’s 1% Q3 growth sets pace to beat BOK’s 3.3% annual forecast
  - [taiwan] Cathie Wood Trims AMD and TSMC, Adds Air Taxi Bets
  - [japan] Selling investment trusts as prices fall due to rising interest rates, JA Saga will be in the red this fiscal 
  - [china] Shenzhen Kingkey Smart Agriculture Times Q3 Net Loss At 193.6 Million Yuan
  - [japan] The reason why the report card for the first year of the Takaichi administration is ``barely passing in fiscal
  - [japan] Japan eyes 1 tril. yen private investment in Bangladesh over 5 yrs
  - [japan] Finance Minister Katayama refrains from purchasing and rushes for consumption tax cut, related ministries and 
  - [china] Shanghai V-Test Semiconductor Tech To Invest In Shanghai HQ Project
  - [china] Sinograin vende 172.240 t de soja importada pela China, aponta Mysteel
  - [taiwan] Taiwan's 2027 budget with NT$10,000 handouts heads to committee
  - [china] Gree Electric Appliances's Shareholder To Raise Stake By 600-1200 Million Yuan
  - [china] Hainan Airport Infrastructure Q3 Net Loss At 132.6 Million Yuan
  - [japan] Digital Core REIT Announces Pricing Of JPY 5 Bln 3.47% Fixed Rate Notes Due 2031
  - [china] WuXi AppTec Co., Ltd. Class A Stock 12‑Month Price Target Raised to CNY 199.71, Implies 37% Upside
  - [china] Sustained Recovery for China Equities May Require Stronger Stimulus — Market Talk
  - [japan] What role does the Bank of Japan branch play? "Bank of Japan Nagasaki Branch" Branch Manager talks about the c
  - [japan] Retail price of eggs reaches record high “Avian influenza continues to affect” Ministry of Agriculture, Forest
  - [japan] Mr. Hitoshi Sasaki is appointed as the new branch manager of the Bank of Japan's Shizuoka Branch, with the amb
  - [japan] Meiko Electronics - Announcement Of Execution Of A Basic Agreement Regarding Acquisition Of Shares Of Unimicro
  - [korea] Huons Global To Acquire Real Estate Worth 244.5 Billion Won
  - [china] Xinjiang Daqo New Energy Q3 Net Loss At 410.9 Million Yuan
  - [taiwan] Foreign fund outflows send Taiwan dollar sharply lower: Central bank
  - [china] China National Nuclear Power: Nine-month profit fell sharply amid tariff and cost pressures, despite stronger 

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
      "published_utc": "2026-10-27T20:33:24+00:00",
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

