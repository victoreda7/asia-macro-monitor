atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-29T07:12:43.229118+00:00
Total: 3000 manchetes

  🇯🇵 Japão          895
  🇨🇳 China          838
  🇹🇼 Taiwan         382
  🇰🇷 Coreia do Sul  885

## O que já está no feed (não repita)

  - [korea] OCI Holdings swings to profit as revenue tops 1 trillion won, builds U.S.-bound supply chain linking Malaysia 
  - [japan] Nippon Shokubai Co - To Buy Back Up To 2.0% Own Shares Worth 6 Billion Yen
  - [korea] INTC, AMD, AVGO, MU Decline On Samsung’s Profit Miss, Lighter Capex From Microsoft, Alphabet
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Quarterly Dividend for Third Quarter 2026
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Announcement of Capex Plan for FY 2026
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - 2026 3Q Earnings Release
  - [japan] Yen strengthens against dollar following Warsh's remarks
  - [china] Volkswagen: U.S. Tariffs Weigh on Us, China Mkt is Shrinking, Europe Competitive Pressure Increasing Significa
  - [japan] Bank of Japan Monetary Policy Meeting: Will the inflation rate reach 2%? (ABEMA TIMES)
  - [korea] S. Korea eyes virtuous cycle via green economic growth
  - [korea] Korea's chip boom catches US Fed chair's eye
  - [korea] Exclusive-Bank of Korea board member says won moves faster than expected
  - [china] The central bank launches 1 trillion yuan in overnight reverse repurchases
  - [korea] Samsung sees memory supply tight through 2028 as 2027 HBM sells out
  - [japan] Japan bonds steady ahead of BOJ decision; strong auction lends support
  - [korea] BOK board member flags won volatility despite AI chip export boom - RTRS
  - [japan] Popular entertainer shocked by overseas prices. Snacks in LA cost 1,500 yen if they were in Japan...Studios ar
  - [korea] Samsung roars back in AI chip race with record W107tr profit
  - [japan] Tokyo Gas Co Ltd - To Buy Back Up To 3.6% Of Shares Worth 50 Billion Yen
  - [japan] [Today's Oha Biz October 29th (Thursday)] The point of the Fed leaving interest rates unchanged is
  - [korea] Samsung's Chip Profit Drives Another Record Quarter — Update
  - [korea] South Korean Won Recovers on Dollar Weakness
  - [japan] Why has the "long-term interest rate rise" temporarily stopped? Linkage with AI semiconductor stocks, "Don't l
  - [korea] Samsung Electronics: Record results led by Memory as AI demand surges and supply remains tight
  - [japan] Toyoda Gosei - To Buy Back Up To 6.1% Own Shares Worth 30 Billion Yen
  - [china] China stocks slip as tech weakness overshadows Fed rate decision
  - [japan] Advantest Corp. Stock 12‑Month Price Target Raised to JPY 45945.45, Implies 32% Upside
  - [japan] Japan 10Y Yield Steadies Ahead of BOJ Decision
  - [japan] BOJ preview October: hawkish hold expected as inflation remains sticky By Investing.com
  - [china] China's yuan hits 4-year high versus dollar after Fed decision
  - [japan] BOJ preview October: hawkish hold expected as inflation remains sticky
  - [korea] Samsung sees chip shortage worsening, but keeps investors in suspense on returns
  - [china] China Focus: China's sustained housing upgrades keep urban decay at bay
  - [japan] Bank of Japan holds monetary policy meeting from today, policy interest rate expected to remain unchanged
  - [japan] Bank of Japan expects to keep interest rates unchanged, determined to reach inflation rate target of 2% (TV As
  - [china] Beijing Branch of the Central Bank: Beijing’s social financing increase in the first three quarters was 1.1062
  - [korea] Banks' household mortgage lending rates up for 5th month in Sept.
  - [japan] Yen Steadies Ahead of BOJ Policy Decision
  - [japan] The Bank of Japan has determined that the inflation rate will reach 2%, and is expected to leave the policy ra
  - [japan] Is the inflation rate determined to reach 2%? The Bank of Japan is expected to leave the policy rate unchanged

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
      "published_utc": "2026-10-29T07:12:43+00:00",
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

