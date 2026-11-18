atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-18T04:42:50.509393+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1035
  🇨🇳 China          909
  🇹🇼 Taiwan         303
  🇰🇷 Coreia do Sul  753

## O que já está no feed (não repita)

  - [china] China's AI Chip Vendors to Gain From U.S. Chip Curbs — Market Talk
  - [japan] [Topical topics on Yahoo! Comments] ``Doubts about the effectiveness of active fiscal policy and consumption t
  - [china] Yuan dips, holds bullish outlook on bigger role in regional trade
  - [japan] Bank of Japan governor says central bank should keep raising rates
  - [china] PBOC Sets Strongest Yuan Fix Since 2022 to Allow Further Gains
  - [china] China's October fuel exports slowed on month but still topped last year's monthly average
  - [china] China's September grain, sugar and pork imports
  - [japan] Auction Result of 20-Year JGBs on November 18, 2026
  - [japan] Japan's Orix To Acquire Recruit Holdings' Online Learning Business For About 60 Billion Yen, Nikkei Says
  - [japan] Japan's Underlying Economic Growth Likely Resilient, Unlikely to Alter BOJ's Policy Outlook — Market Talk
  - [korea] South Korean State Think Tank Raises Growth Forecasts
  - [japan] Stock prices fall, sell orders related to AI and semiconductors
  - [korea] South Korean State Think-Tank KDI Raises GDP Forecasts
  - [china] Asia tech shares turn mixed after Nvidia beat as China chip curbs cloud optimism
  - [japan] BOJ’s Ueda Says Planned Food Tax Cut Likely to Aid Growth
  - [china] U.S. Chip Curbs to Leave U.S.-China Relationship More Fragile — Market Talk
  - [japan] BOJ's Ueda Sees Sales Tax Cut Boosting Growth, But Impact Uncertain
  - [japan] Trade balance deficit of 476.5 billion yen in October, 6th consecutive month of deficit
  - [china] China’s Recombinant Collagen Technology Wins the INPD Innovative Manufacturing Process Award
  - [korea] South Korean won gains most among mixed Asian currencies
  - [china] Central Bank: Launches 700.2 billion yuan overnight reverse repurchase operation with an operating interest ra
  - [korea] The Bank of Korea is highly likely to raise its benchmark interest rate by 25bp in November amid the strong wo
  - [japan] It is appropriate to raise policy interest rates and adjust the degree of easing according to economic, price 
  - [china] On November 18, the central bank launched a 700.2 billion yuan overnight reverse repurchase operation.
  - [korea] Boston Dynamics to deploy robots at GlobalFoundries' chip plants
  - [china] PBOC Raises Yuan Reference Rate to Strongest Since 2022
  - [china] CHINA PBOC CONDUCTS CNY700.2 BLN VIA O/N REVERSE REPO WEDS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7118 WEDS VS 6.7132
  - [japan] Announcement of 40-year JGBs to Be Issued in November 2026
  - [japan] Japan MOF To Auction Y300.0B Of 40-Year Govt Bonds Nov 25
  - [japan] Ueda says BOJ will weigh if underlying inflation becomes anchored
  - [korea] Citigroup predicts that the Bank of Korea will raise interest rates in both November and February, with rising
  - [korea] Samsung Electro-Mechanics, Nvidia to expand cooperation on AI chip components
  - [china] China warns US of retaliation over new AI chip restrictions
  - [japan] The whole family is working together to endure the rise in prices...The reason why Japanese households cannot 
  - [korea] S. Korea moves to simplify rules of origin verification for used car exports
  - [china] Nvidia no longer selling US-approved Hopper chips to China, Interim CEO Kress says
  - [japan] Japan's Export Growth Expected to Moderate Gradually — Market Talk
  - [china] Banks Pause $480 Million Chip Loan Tied to China’s ByteDance
  - [japan] Bank of Japan Governor Ueda will attend a special committee meeting of the House of Councilors from 10:00 a.m.

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
      "published_utc": "2026-11-18T04:42:50+00:00",
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

