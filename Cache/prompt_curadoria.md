atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-20T09:52:43.761396+00:00
Total: 3000 manchetes

  🇯🇵 Japão          999
  🇨🇳 China          902
  🇹🇼 Taiwan         356
  🇰🇷 Coreia do Sul  743

## O que já está no feed (não repita)

  - [japan] Dollar surrenders gains as record Japanese bond auction sparks Yen rally
  - [china] China and Hong Kong stocks fall; stable growth dampens stimulus expectations
  - [china] Chinese Hybrid Import Cap Offers Relief to European Carmakers — Market Talk
  - [china] Cssc Offshore & Marine Engineering Says 9-Month New Orders Totalled 35.8 Billion Yuan
  - [china] EXCLUSIVE: ByteDance, Alibaba, Tencent place over $35 billion worth of Nvidia chip orders
  - [china] China's Strong 3Q Growth Rules out Additional Stimulus — Market Talk
  - [china] China solar exports to Middle East, Southeast Asia surge in September but Europe, Asia weigh on total
  - [china] China's Central Bank Likely to Hold Policy Rate Steady for Rest of 2026 — Market Talk
  - [china] Foreign holdings of China's onshore yuan bonds unchanged at end-September
  - [korea] Bank of Korea raises interest rates twice in a row... Focus on “Will we upload it again” vs. “Will we freeze i
  - [japan] Food consumption tax reduction bill: Prime Minister aims to enact the bill as soon as possible
  - [taiwan] BASF Signs Semiconductor Agreement With Taiwan to Expand Materials Site
  - [taiwan] Taiwan September export orders hit record value on solid AI demand
  - [taiwan] U.S. dollar closes sharply higher on Taipei forex market
  - [china] China, Hong Kong shares weaken as stable growth eases stimulus bets
  - [korea] The import concentration is intensifying from the single-person media industry such as YouTubers to
  - [korea] [Photo] Deputy Finance Minister Hearing On-Site Opinion on 'Coin Taxation'
  - [korea] New bank accounts created following preferential interest rates and stock accounts increased along w..
  - [china] The People's Bank of China will carry out overnight reverse repurchase operations for 9 consecutive working da
  - [japan] Japan MOF To Auction Y3.3T Of TD-Bills Oct 23
  - [taiwan] Taiwan Export Orders Hit New Record High
  - [china] China keeps yttrium exports to Japan restricted in September
  - [korea] South Korea to consider cutting bond issuance if needed to stabilise market
  - [taiwan] BASF Signs Letter Of Intent With Taiwan To Advance Semiconductor Manufacturing
  - [korea] Government R&D budget at 40 trillion won ... 80% of equipment is foreign-made
  - [china] The People's Bank of China will withdraw a net 65 billion yuan from the market on October 20 and will carry ou
  - [taiwan] Indonesian shares recover after hitting six-year low; Taiwan dollar depreciates
  - [china] The People's Bank of China will withdraw a net 65 billion yuan on October 20 and will carry out overnight reve
  - [china] China's Australian coal imports surge to six-year high
  - [china] PBOC Faces Multi-Month Road to New Rate Anchor, Analysts Say
  - [japan] Stock price temporarily fell by more than 1,100 yen due to rise in crude oil futures prices
  - [china] US Sanctions China’s Y Combinator in Google AI Secrets Case
  - [taiwan] Taiwan anchors US chip revival, SEMICON West spotlights trusted partners
  - [korea] Will the base interest rate increase take a break in October? Monetary Policy Committee predicts 3% annual fre
  - [japan] Japan's Nikkei ends lower as higher yields, inflation fears weigh
  - [japan] Yomiuri: Japan Eyes 250 Billion Yen in Additional Funding for Rapidus
  - [taiwan] Key facts: NVIDIA Sees $108B Q3 Sales; 104‑Qubit Sim; TSMC 3nm NVHBM
  - [japan] The prefecture's economy is on a "moderate recovery trend", Bank of Japan's Councilor Koeda gives a speech in 
  - [korea] South Korean shares post more than 6-month closing low as chipmakers fall on AI concerns
  - [china] China resumes sulphuric acid exports to copper king Chile after three-month halt

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
      "published_utc": "2026-10-20T09:52:44+00:00",
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

