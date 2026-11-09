atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-09T01:42:43.901889+00:00
Total: 3000 manchetes

  🇯🇵 Japão          933
  🇨🇳 China          879
  🇹🇼 Taiwan         328
  🇰🇷 Coreia do Sul  860

## O que já está no feed (não repita)

  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7188 MON VS 6.7168
  - [china] China Oct Non-Food Prices +1.5% on Year
  - [china] China Oct Food Prices -2.9% On Year
  - [china] China Jan-Oct CPI +0.9% on Year
  - [china] China Oct CPI 0.0% on Month
  - [japan] Japan MOF To Auction Y250.0B Of 10-Year CPI-Indexed Bonds Nov 16
  - [china] China Oct CPI +0.7% on Year; Market Expected +0.8%
  - [korea] Citi: “Despite the decline in stock prices, we will raise the base interest rate this month… If the semiconduc
  - [china] Consumer prices in October 2026 increased by 0.7% year-on-year
  - [korea] What will the interest rates be next year? “If the semiconductor industry collapses, the Bank of Korea will al
  - [japan] Japan stepped in to buy one-day record 7.98 tril. yen in July: gov't data
  - [japan] Berkshire Hathaway Mandates Mizuho And Bank Of America Securities For Yen Denominated Unsecured Senior Bond, J
  - [japan] Japan's July yen-buying intervention sets fresh daily record
  - [japan] Record-breaking yen buying intervention of 7.9 trillion yen on July 30th
  - [korea] NH Investment & Securities expects base interest rate to increase by 25bp in November
  - [japan] Market intervention on July 30th: 7,975.6 billion yen, largest ever for yen buying intervention
  - [korea] South Korea's Economic Outlook Hinges on Chip Cycle — Market Talk
  - [japan] BREAKING NEWS: Japan spent record 7.98 tril. yen in yen-buying intervention on July 30
  - [japan] Japan FX intervention data underscores challenge of reversing weak yen
  - [japan] Monetary Base and the Bank of Japan's Transactions (Oct.)
  - [japan] Bank of Japan's Transactions with the Government (Oct.)
  - [japan] Market Operations by the Bank of Japan (Oct.)
  - [japan] Consumption tax reduction bill will be debated in the House of Councilors the next day, leading to debate betw
  - [korea] [Morning Report] “Despite the sharp decline in the stock market, the Bank of Korea is expected to raise intere
  - [japan] BOJ chief Ueda sees ’some upside risks’ to inflation
  - [japan] "AI that steals jobs" has not taken hold in Japan...The potential of "AI that enters between" has been seen at
  - [japan] Five general trading companies all increase profits and record high profits...Despite the tailwind from high r
  - [japan] Today's Japan-Vietnam summit meeting: Coordination of joint statement on important minerals, nuclear cooperati
  - [korea] Hana Bank, ranked first in interest reduction per interest rate reduction request in the first half of the yea
  - [china] The Chinese people are wiping out President Xi Jinping's ``misjudgment''...The tyranny of local governments th
  - [japan] Will the AI ​​bubble burst? & Thoughts on Trump's miscalculations etc. = Thoughts on the Bank of Japan's "lunc
  - [japan] ANA makes Air Do and Solaseed Air wholly owned subsidiaries... Each company complains of "real deficits on dom
  - [japan] A major blunder at DoCoMo, where a series of troubles occurred in less than a month... Just when the president
  - [taiwan] NSC tightens anti-infiltration measures
  - [korea] Korea’s budget coffee chain Mega MGC dwarfs legacy brands despite Starbucks’ recovery
  - [korea] Affiliated real estate trust companies have been in the red for the third consecutive year, with the..
  - [japan] Consumption tax reduction bill Liberal Democratic Party Policy Research Council Chairman Kobayashi “deliberate
  - [korea] With the stock market plummeting, the calculation of the Bank of Korea's interest rate hike is complicated... 
  - [japan] Piles of old rice in the warehouse, sold at a loss
  - [japan] Are prices in the area you live higher than the national average? Only nine prefectures have a higher rate, an

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
      "published_utc": "2026-11-09T01:42:44+00:00",
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

