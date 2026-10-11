atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-11T21:12:45.046062+00:00
Total: 2777 manchetes

  🇯🇵 Japão          1104
  🇨🇳 China          770
  🇹🇼 Taiwan         270
  🇰🇷 Coreia do Sul  633

## O que já está no feed (não repita)

  - [japan] Investors bet on Japan, Australia rental housing as rates, home prices rise
  - [japan] "European Debt Crisis 2.0" becomes a reality with the explosion in France...Can the ECB put out the fire as in
  - [japan] Former iPhone display plant in Japan to start new life in chip supply chain
  - [japan] Japan Week Ahead: BOJ Policymakers to Digest More Q3 Data Before Oct. 29-30 Meeting; Board Widely Expected Hol
  - [korea] Shin Hyun-song’s first National Assembly inspection… ‘A lot of issues’ in the controversy over interest rate h
  - [japan] Preview: Forecasters See Another High Reading for Japanese Producer Price Inflation in September Report
  - [japan] What the sell off in bonds means for monetary policy
  - [korea] Humanoids emerge as new growth engine for Samsung, SK Hynix
  - [china] EU plans yearly cap of 350,000 Chinese hybrid cars as trade tensions rise
  - [korea] Solidigm IPO sparks debate over SK hynix shareholder value
  - [korea] The Bank of Korea predicts a ‘hawkish freeze’ in its benchmark interest rate in October… Additional tightening
  - [korea] Hacking attempts on BOK, state lenders top 1 million
  - [china] China Moves to Stave Off Wider EU Trade War With Hybrid Deal
  - [japan] Japan weighs railway upgrades as part of defense spending push
  - [korea] Samsung to expand chip capacity in Vietnam, boost high-end production in Korea
  - [china] Renault CEO calls EU-China hybrid import deal a ’major milestone’ - Bloomberg
  - [japan] Cocorico Endo > Family trip to Hawaii - cup noodles due to the weak yen and rising prices (beautiful every day
  - [japan] Yen weakness since 2025 has been limited to offshore hours: analysis By Investing.com
  - [japan] Yen weakness since 2025 has been limited to offshore hours: analysis
  - [korea] Korea-US base interest rates expected to freeze in October... 'The austerity trend will continue'
  - [korea] As investment in industrial facilities such as semiconductor fabs and data centers has emerged as a
  - [korea] Food companies that were sanctioned for fixing food prices, such as sugar and flour, topped the Fair..
  - [korea] “Interest rates are soaring, what happens to interest?” 57.3% of household loans have variable interest rates
  - [taiwan] Taiwan’s Lai Urges Democracies to Unite After Trump-Xi Summit
  - [taiwan] Taiwan’s Lai Urges Democracies to Unite After Trump-Xi Talks
  - [korea] Floating rate loans increase despite consecutive increases in base interest rates... Household debt warning li
  - [japan] The Bank of Japan raises the policy interest rate from 1% to 1.25%, entering an era of interest rates. What wi
  - [japan] Kawasaki Heavy aims at 1 tril. yen in defense sales as Japan ups spending
  - [japan] Japanese giant expands China chip packaging materials output amid AI boom
  - [taiwan] Changs Ascending September revenue jumps 92% on semiconductor plant buildouts
  - [japan] Semiconductor memory giant Micron's financial results reflect "endless memory shortage" AI servers shipped wit
  - [korea] Concerns about an 'interest bomb' in household loans due to consecutive increases in base interest rates... Th
  - [japan] Minister Kihara "Carefully discuss with opposition parties to pass tax reduction bill, etc." NHK Sunday debate
  - [korea] South Korean Firms Diverge as Large-Company Exports Surge and Small-Business Output Falls
  - [japan] A 47-year-old single woman gave up her 80 square meter apartment and moved to a 1LDK/custom-built home as her 
  - [japan] Employment of 50 people with disabilities terminated after 9 months
  - [taiwan] Huge capital investment in Taiwan's semiconductor back-end process ``Packaging and testing are not supporting 
  - [japan] Everpure director Mallun Yen sells $1.75m in shares By Investing.com
  - [japan] Everpure director Mallun Yen sells $1.75m in shares
  - [china] In September, the central bank's various tools provided a net liquidity of 556.4 billion yuan. Experts: There 

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
      "published_utc": "2026-10-11T21:12:45+00:00",
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

