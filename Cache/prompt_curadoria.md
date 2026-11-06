atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-06T16:02:45.683748+00:00
Total: 3000 manchetes

  🇯🇵 Japão          906
  🇨🇳 China          896
  🇹🇼 Taiwan         329
  🇰🇷 Coreia do Sul  869

## O que já está no feed (não repita)

  - [taiwan] TSMC considers making advanced memory chips, The Information reports
  - [taiwan] TSMC considera fabricar chips de memória avançados, segundo o Theme Information
  - [japan] U.S. employment increased by 165,000 in October, exceeding expectations
  - [china] Suzano's CFO Says Chinese Debt Market Now Looks More Attractive For Bond Issuance
  - [taiwan] TSMC Weighs Making Advanced Memory Chips To Capture More AI Spending - The Information
  - [japan] Food consumption tax reduction bill passes the House of Representatives and will be debated in the House of Co
  - [china] Table: Yuan Jen Enterprises Oct Rev NT$741.2M Vs NT$530.9M
  - [china] China’s State Council Calls for Stronger Stock Market Stability
  - [china] Nexwise Intelligence China Signs 4.9 Billion Yuan Computing Power Service Contract
  - [japan] [America after the Trump administration] “Support won’t return even if the economy recovers” Supporters are de
  - [taiwan] Stabilization fund ready for market intervention after Taiex's plunge
  - [japan] Invesco CurrencyShares Japanese Yen Trust 3Q 2026: EPS ($0.04) — 10-Q Summary
  - [china] Soybean imports by China in 2026/27 estimated at 110 million tons, says USDA attaché
  - [japan] Consumption tax cut bill passes Japan's lower house in fast-tracked vote
  - [china] China formally removes Li Lecheng as industry minister after Anhui party appointment
  - [china] Analysis-China’s yuan dilemma: too weak abroad and too strong at home
  - [taiwan] The central bank strengthened its defense and exporters assisted. The Taiwan dollar depreciated and rose to cl
  - [japan] Prime Minister Takaichi intends to allocate the proceeds from additional sales of BOJ ETFs to “new investment 
  - [china] Ex-Everbright Executive and Wife Took 4.29 Million Yuan in Salary Bribes
  - [china] Subaru China recalls 196,494 imported cars in China, China's market regulator says
  - [korea] Citi presents two scenarios for Bank of Korea base rate hike
  - [korea] Citi sees two rate hike scenarios for South Korea’s BoK
  - [japan] Consumption tax reduction bill to be debated in the House of Councilors on the 11th
  - [korea] Domestic financial experts raised a series of concerns over the government's budget plan for next ye..
  - [japan] Bill on food tax cut clears Lower House | NHK WORLD-JAPAN News
  - [japan] Bill on food tax cut clears Lower House
  - [japan] Proceeds from the sale of Bank of Japan ETFs will be placed in a new special account, Chief Cabinet Secretary 
  - [korea] Was this the reason why the Governor of the Bank of Korea said, “Semiconductor prices are important”?
  - [japan] Prime Minister Takaichi Proceeds from additional sales of Bank of Japan ETFs will be used as a source of new i
  - [korea] NPS tightens stewardship rules on treasury shares, $157 bn Korean equity mandates
  - [japan] GPIF investment performance July-September deficit of over 5.25 trillion yen, impact of low foreign bonds
  - [korea] Korean sweet persimmons will be exported to China for the first time. This is the first achievement
  - [taiwan] Taiwan's October Exports Likely Rose 52.8%, WSJ Poll Shows — Market Talk
  - [china] China's Consumer Price Pressure Likely Remained Subdued — Market Talk
  - [korea] Amid the growing burden of taxes and financial costs in the housing market in the Gangnam area of Se..
  - [taiwan] Taiwan’s Currency Weakens Past 33 Per US Dollar on AI Jitters
  - [taiwan] U.S. dollar closes sharply lower on Taipei forex market
  - [japan] Asian FX mixed as yen pares gains, Aussie hits 18-week low ahead of U.S. payrolls By Investing.com
  - [japan] Prime Minister Takaichi: “Proceeds from additional sales of Bank of Japan ETFs will be used as a source of fun
  - [japan] Mortgage Service Japan 1H Net Y608.00M Vs Net Y513.00M

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
      "published_utc": "2026-11-06T16:02:45+00:00",
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

