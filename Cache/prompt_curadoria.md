atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-30T10:52:43.032436+00:00
Total: 3000 manchetes

  🇯🇵 Japão          922
  🇨🇳 China          852
  🇹🇼 Taiwan         363
  🇰🇷 Coreia do Sul  863

## O que já está no feed (não repita)

  - [china] Memory Crunch Cements CXMT as China's Chip Champion
  - [japan] Bank of Japan Governor focuses on fixing 2% inflation (Jiji Press)
  - [china] Yonghui Superstores Q3 Net Loss At 82.7 Million Yuan
  - [japan] Japan’s inflation rate reaches 2% target, Bank of Japan President: 13 years of hard work to meet important mil
  - [china] BYD Company Limited Class A Stock 12‑Month Price Target Cut to CNY 108.62, Implies 32% Upside
  - [taiwan] Export investment exceeded expectations. The economic growth rate in the third quarter was 14.36%, the highest
  - [china] ECB President Christine Lagarde doesn’t want to be neutral anymore and leaves office early
  - [japan] BREAKING NEWS: Kioxia expects 1.36 tril. yen net profit for Oct.-Dec. quarter
  - [china] The European Central Bank decides to keep interest rates unchanged at 2.5% | International
  - [china] Gansu Jiu Steel Group Hongxing Iron & Steel Q3 Net Loss At 813.7 Million Yuan
  - [japan] Japan's Katayama signals hope of bigger surplus from central bank's ETF sales
  - [china] China's central bank steps up shift toward overnight rate as policy anchor
  - [china] BAIC BluePark New Energy Technology Q3 Net Loss At 922.0 Million Yuan
  - [japan] BOJ stays pat on rates, signals inflation target reached
  - [china] Cinda Real Estate Q3 Net Loss At 1.2 Billion Yuan
  - [japan] Yen gains after BOJ; AI jitters dent dollar By Reuters
  - [china] JZJ Chain Drugstore Q3 Net Loss At 312.5 Million Yuan
  - [china] National Silicon Industry Group Q3 Net Profit At 236.7 Million Yuan
  - [japan] Yen Rises On BoJ's Hawkish Pause
  - [china] CRRC, Units Signs Major Contracts Totalling About 71.0 Billion Yuan
  - [japan] Yen market: Small price movements Limited impact of the Bank of Japan’s monetary policy meeting
  - [japan] BOJ declares victory in hitting price target, signals near-term hikes By Reuters
  - [japan] BOJ declares victory in hitting price target, signals near-term hikes
  - [taiwan] Taiwan's ICT export market ranked third in the world last year, and computers and peripheral equipment jumped 
  - [china] Anhui Jianghuai Automobile Group Q3 Net Loss At 391.8 Million Yuan
  - [taiwan] Rising inflation erodes purchasing power. The French lament the rising energy and food prices and tighten thei
  - [taiwan] Soaring inflation erodes purchasing power, and French people tighten their pants to survive
  - [japan] Bank of Japan ETF sale, Finance Minister Katayama ``Considering how to handle the increase'' (Reuters)
  - [china] Henan Dayou Energy Q3 Net Loss At 436.4 Million Yuan
  - [japan] [Illustration] Bank of Japan Governor says that the 2% target is “generally consistent” = key price inflation 
  - [china] Shanghai Electric Power: Q3 profit nearly vanished as lower tariffs and higher fuel costs pressured results
  - [japan] BOJ Says Japan’s Inflation Trend Hits 2% Target as it Holds Rates
  - [china] Next week, 1.749 billion yuan of reverse repos will mature in the central bank’s open market.
  - [china] Central Bank: Starting from November 2, 2026, bidding for overnight reverse repurchase operations will be laun
  - [china] China's central bank to conduct overnight reserve repos every working day from November 2, rate at 1.25%
  - [japan] Market moves ``as expected'' at Bank of Japan meeting, with limited movement even after announcement of accele
  - [china] Central Bank: Starting from November 2, bidding for overnight reverse repurchase operations will be launched e
  - [japan] Is achieving the 2% target with good price increases that was initially aimed at a dream that cannot be fulfil
  - [china] Central Bank: Conduct bidding for overnight reverse repurchase operations every working day
  - [japan] Why did the Bank of Japan aim for 2%? Adjust the economy and prices by moving interest rates

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
      "published_utc": "2026-10-30T10:52:43+00:00",
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

