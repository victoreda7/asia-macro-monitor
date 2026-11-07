atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-07T05:32:45.639471+00:00
Total: 3000 manchetes

  🇯🇵 Japão          913
  🇨🇳 China          895
  🇹🇼 Taiwan         327
  🇰🇷 Coreia do Sul  865

## O que já está no feed (não repita)

  - [china] China Forex Reserves Edged Up in October — WSJ
  - [taiwan] Foreign assets reached nearly 3 times the bottom of foreign exchange deposits. Taiwan stock market turbulence 
  - [japan] <Book Reviews> ``Added Value of Managers'' ``What is Foreign Exchange Intervention? The Mystery of the Birth o
  - [china] Beijing Vows to Hit Back Against US Sanctions on China Companies
  - [china] Bessent, Greer Raise Concerns on China Trade Deal Actions
  - [japan] Economic situation in November, “moderate recovery”, Bank of Japan Shimonoseki branch, 35th consecutive month 
  - [japan] Bank of Japan Governor Ueda wants to keep inflation at 2%, mentions upside risk (Jiji Press)
  - [taiwan] The Czech central bank raises interest rates by 1% to 4% to prevent rising inflation and slowing economic grow
  - [japan] Bank of Japan Governor warns of upward swing in prices, saying there are “many challenges” even after reaching
  - [japan] Treasury Secretary George Bessent and Vice Premier He discuss the status of the trade war ``truce''
  - [japan] PM Takaichi gave fewer Diet budget committee responses than 4 predecessors
  - [japan] Bank of Japan decides to speed up ETF sales (Hiroyuki Kubota) - Expert
  - [japan] Which is correct regarding the consumer price increase rate: ``3.2%'' by the Bank of Japan or ``2.1%'' by the 
  - [japan] Japan's new whisky breed chases export elixir
  - [japan] Consumption tax reduction bill passed by the House of Representatives; consensus building between ruling and o
  - [japan] BOJ chief Ueda sees ’some upside risks’ to inflation
  - [japan] [Asahi Shimbun answers 10,000 characters (part 3)] Supporting the digital deficit with real estate and stock d
  - [japan] Sony Group Stocks Slip 2.63% Despite Record 1.33 Trillion Yen Profit Forecast
  - [china] US, China trade chiefs hold call ahead of Trump-Xi summit in Shenzhen
  - [china] U.S. urges China to comply with Busan trade deal over rare earth shortfalls - report
  - [china] Nvidia's Quiet New Ultimatum to Stop China Chip Smuggling
  - [korea] BOK Financial Posts Investor Presentation Highlighting Q3 Loan Growth and 2026 Outlook
  - [china] US urges China to meet rare earths, agriculture commitments ahead of Trump-Xi meetings
  - [china] US urged Beijing to implement commitments of Busan trade deal, Treasury says
  - [china] Guangzhou Proposes Easing Developers’ Infrastructure Obligations
  - [japan] BOJ's Ueda says Japan could do well with AI replacing labor, given existing shortages
  - [taiwan] Taiwan Semiconductor Stocks Jump 7.45% as Taiwan Slashes Short Selling After Rout
  - [korea] SK hynix Stocks Plunge 10.44% as AI Memory Leader Leads Seoul Selloff
  - [china] Chinese premier chairs State Council executive meeting
  - [taiwan] TSMC considers making advanced memory chips, The Information reports
  - [taiwan] TSMC considera fabricar chips de memória avançados, segundo o Theme Information
  - [japan] U.S. employment increased by 165,000 in October, exceeding expectations
  - [china] Suzano's CFO Says Chinese Debt Market Now Looks More Attractive For Bond Issuance
  - [taiwan] TSMC Weighs Making Advanced Memory Chips To Capture More AI Spending - The Information
  - [japan] Food consumption tax reduction bill passes the House of Representatives and will be debated in the House of Co
  - [china] Table: Yuan Jen Enterprises Oct Rev NT$741.2M Vs NT$530.9M
  - [china] Could a paused US blacklist rule signal room for progress in China trade talks?
  - [china] China’s State Council Calls for Stronger Stock Market Stability
  - [china] Nexwise Intelligence China Signs 4.9 Billion Yuan Computing Power Service Contract
  - [japan] [America after the Trump administration] “Support won’t return even if the economy recovers” Supporters are de

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
      "published_utc": "2026-11-07T05:32:45+00:00",
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

