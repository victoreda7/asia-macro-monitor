atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-05T02:22:45.253309+00:00
Total: 3000 manchetes

  🇯🇵 Japão          872
  🇨🇳 China          895
  🇹🇼 Taiwan         318
  🇰🇷 Coreia do Sul  915

## O que já está no feed (não repita)

  - [taiwan] Indonesian rupiah leads gains in Asian currencies; Taiwan dollar underperforms
  - [japan] BOJ debated need for more rate hikes, scope for faster moves, September minutes show
  - [korea] S.Korea’s current account surplus hits record $61 bn; Global IBs hike GDP growth forecasts
  - [china] China indicts ex-Politburo member Ma for bribery
  - [korea] S. Korea posts record high current account surplus of over $60b in Sept. on chip supercycle
  - [korea] SK Hynix was counted as the largest net purchase by high-yield investors of Mirae Asset Securities u..
  - [japan] Upward price fluctuation risk, interest rate hike appropriate, policy “change in phase” Bank of Japan Septembe
  - [china] CHINA PBOC CONDUCTS CNY263 BLN VIA O/N REVERSE REPO THURS
  - [japan] BOJ Board Sees Little Capex Impact From Higher Rates, Minutes Show — Market Talk
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7156 THURS VS 6.7180
  - [korea] (LEAD) S. Korea posts record high current account surplus of over US$60 bln in Sept. on chip supercycle
  - [korea] Bank of Korea expects interest rate hike in November despite removal of interest rate differential and exchang
  - [japan] BoJ Sees Case for Further Rate Hikes: September Minutes
  - [japan] Japan MOF To Auction Y2.5T Of 5-Year Govt Bonds Nov 12
  - [taiwan] TSMC Slips 0.2%; UniMicron Technology Falls 8.6%
  - [taiwan] Taiwan's Chip-Related Stocks Broadly Lower
  - [japan] Japan Services PMI Improves To 51.7 In October - S&P Global
  - [japan] Japan Composite PMI Revised Lower
  - [japan] BOJ Minutes Flag Price Risks, Backing Rate Hike Bets — Market Talk
  - [japan] Bank of Japan members need to discuss the “range” of interest rate hikes, summary of September meeting (Kyodo 
  - [japan] Several opinions stated that interest rates would continue to rise at a rapid pace = Summary of the September 
  - [japan] BREAKING NEWS: BOJ has entered phase to discuss rate hike size: policymaker in minutes
  - [china] Canada, China Extend Tariff Deal, Aim to Boost Canadian Exports
  - [japan] Japan services activity expands for fifth month, PMI shows
  - [japan] ``This is a situation where we need to discuss the extent of interest rate hikes,'' says a Bank of Japan membe
  - [china] Early participation in the bond market, November 5 | The central bank reduced its volume today and continued t
  - [korea] [Reorganization of U.S. power ⑩] Will the method of calculating interest rates and exchange rates change? Bank
  - [korea] South Korea’s Current Account Surplus Hits Record on Chip Boom
  - [japan] Long-Term JGB Yields Fall After Oil Price Drops — Market Talk
  - [japan] [Editorial] Prices reach 2%; Bank of Japan implements policy to curb price increases (Nishinippon Shimbun me)
  - [korea] S. Korea's current account surplus tops $60b for 1st time on chip boom
  - [korea] Korea Zinc : Q3 revenue grew YoY, but profit fell sharply QoQ amid cost and metal-price pressure
  - [japan] Sources of Changes in Current Account Balances (Projections for Nov.)
  - [japan] Minutes of the Monetary Policy Meeting on September 17 and 18, 2026
  - [korea] Hanwha : A KRW 1,083bn spin-off gain lifted earnings as quarterly revenue and operating profit fell
  - [taiwan] DIGITIMES Insight: TSMC, ASML's 2031 photomask target puts High NA EUV suppliers on the clock
  - [taiwan] Subsidies pave the way as cheap cells squeeze Taiwan's energy storage players into a profit battle
  - [korea] S. Korea posts record high current account surplus of over US$60 bln in Sept. on chip supercycle
  - [china] Fortescue to Swap Bond Issue Proceeds Into Offshore Yuan
  - [japan] Franc, Yen Emerge as FX Winners as US Midterms Weaken Dollar

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
      "published_utc": "2026-11-05T02:22:45+00:00",
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

