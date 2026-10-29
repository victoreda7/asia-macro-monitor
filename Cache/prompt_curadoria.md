atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-29T03:52:45.414215+00:00
Total: 3000 manchetes

  🇯🇵 Japão          895
  🇨🇳 China          840
  🇹🇼 Taiwan         385
  🇰🇷 Coreia do Sul  880

## O que já está no feed (não repita)

  - [korea] Samsung sees chip shortage worsening, but keeps investors in suspense on returns
  - [china] China Focus: China's sustained housing upgrades keep urban decay at bay
  - [japan] Bank of Japan holds monetary policy meeting from today, policy interest rate expected to remain unchanged
  - [japan] Bank of Japan expects to keep interest rates unchanged, determined to reach inflation rate target of 2% (TV As
  - [china] Beijing Branch of the Central Bank: Beijing’s social financing increase in the first three quarters was 1.1062
  - [korea] Banks' household mortgage lending rates up for 5th month in Sept.
  - [japan] Yen Steadies Ahead of BOJ Policy Decision
  - [japan] Will the inflation rate reach 2%? The Bank of Japan is expected to leave the policy rate unchanged (TV Asahi (
  - [taiwan] Taiwan central bank head deems AI bubble crash scenario extreme
  - [china] The central bank launched a 115 billion yuan 7-day reverse repurchase operation, with a net investment of 115 
  - [taiwan] AI, semiconductors drive foreign investor gains, weakening Taiwan dollar
  - [japan] Bank of Japan outlook for keeping policy interest rate unchanged Monetary policy meeting from today (NTV NEWS 
  - [china] AgiBot Reports Nearly 2 Billion Yuan in H1 2026 Revenue, 20,000 Robots Produced
  - [japan] Toho Gas Co., Ltd. - To Buy Back Up To 5.7% Own Shares Worth 17 Billion Yen
  - [china] China clean tech exports to cut global emissions by Brazil-sized amount in 2026
  - [japan] Mito Securities Co Ltd - To Buy Back Up To 1.68% Own Shares Worth 800 Million Yen
  - [taiwan] Cathie Wood Piles Into Archer, Joby for Third Straight Day as Ark Dumps AMD, TSMC Shares
  - [korea] Earnings call transcript: Samsung Electronics posts record Q3 2026 profit
  - [korea] South Korean won, Indonesian rupiah lead Asian currencies higher
  - [japan] Denso Corporation - To Buy Back Up To 3.99% Own Shares Worth 200 Billion Yen
  - [korea] Why is Samsung Electronics stock sliding today?
  - [korea] Samsung Electronics posts record profit in Q3 on AI chip supercycle
  - [korea] Samsung posts record profit in Q3 on AI chip boom
  - [korea] Samsung Expects Chip Supply Shortages to Persist Through 2028
  - [china] The central bank launched a 115 billion yuan 7-day reverse repurchase operation today
  - [china] CHINA PBOC CONDUCTS CNY115 BLN VIA 7-DAY REVERSE REPO THURS
  - [china] CHINA PBOC CONDUCTS CNY1 TRLN VIA O/N REVERSE REPO THURS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7147 THURS VS 6.7165
  - [japan] Japan MOF To Auction Y2.6T Of 10-year Govt Bonds Nov 5
  - [korea] Sk Hynix Considering Various Ways To Increase Competitiveness Of Solidigm
  - [korea] S. Korea to conditionally ease diesel export restrictions amid stable crude supplies
  - [korea] Correct: Samsung Electronics: Chip Business Posted Record Profit of KRW106.5T in 3Q, Not KRW106.5
  - [korea] Samsung posts record quarterly profit as AI-driven chip demand surges
  - [korea] Samsung Electronics: Chip Business Posted Record Profit of KRW106.5T in 3Q
  - [korea] Samsung Electronics approves W30tr dividend on record Q3 profit
  - [korea] Samsung prevê que a escassez de chips se agrave, mas mantém os investidores em suspense quanto aos retornos
  - [japan] JGB Yields Rise Amid Caution Ahead of BOJ Decision — Market Talk
  - [korea] Samsung Electronics Q3 2026 Earnings Call Is Live
  - [korea] Samsung Electronics 3Q Net Profit Below FactSet-Compiled Consensus
  - [china] China's New Export Restrictions Protect Its AI Crown Jewels

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
      "published_utc": "2026-10-29T03:52:45+00:00",
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

