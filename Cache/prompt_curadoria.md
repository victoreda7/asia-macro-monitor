atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-30T12:22:42.978010+00:00
Total: 3000 manchetes

  🇯🇵 Japão          926
  🇨🇳 China          852
  🇹🇼 Taiwan         363
  🇰🇷 Coreia do Sul  859

## O que já está no feed (não repita)

  - [japan] BOJ says 2% inflation target generally achieved, maintains policy rate
  - [korea] Clues Point to Familiar Culprit in Massive Binance Crypto Heist: North Korea — WSJ
  - [japan] Japan govt. to spend another $7.3 bil. on fuel subsidy
  - [japan] Fixed mortgage interest rates to be lowered by four major banks starting in November
  - [taiwan] Taiwan Q3 GDP growth hits 14.36%, highest in 48 years
  - [japan] Bank of Japan Governor Ueda says price stability target “reached 2%” and leaves policy interest rate unchanged
  - [japan] Chief Cabinet Secretary Kihara: “We hope for appropriate monetary policy management” Bank of Japan’s “2% price
  - [japan] September crude oil imports decreased for the first time in four months, possibly due to pipeline suspensions
  - [taiwan] Intel warning sparks chip rout as PC weakness clouds turnaround
  - [japan] Asia report: Tech stocks tumble on AI fears as BoJ holds rates
  - [china] The central bank officially announced that the policy interest rate has officially "changed the anchor", and t
  - [japan] Japanese Yen Gains Modest as BOJ Rate-Rise Prospects Well Priced — Market Talk
  - [china] The central bank announced! Overnight reverse repurchase will be carried out every working day starting next w
  - [china] Important adjustments from the central bank will be implemented starting next week
  - [japan] Angle: Bank of Japan continues to raise interest rates to keep the underlying price level at 2%. Is the “next 
  - [china] Memory Crunch Cements CXMT as China's Chip Champion — Update
  - [china] The central bank releases important information
  - [japan] Nxera Pharma: 9M profitability advances the JPY 50bn 2030 revenue ambition, with milestone timing a key variab
  - [taiwan] Tainan station tightens rules for popular public piano
  - [japan] Bank of Japan judges that the underlying inflation rate has reached 2%, and postpones raising interest rates a
  - [japan] Finance Minister Katayama understands the Bank of Japan's judgment is "consistent with the 2% target" (Jiji Pr
  - [japan] “Achieving 2% is symbolic” “Two more rate hikes” Statement from Bank of Japan experts (Jiji Press)
  - [china] Memory Crunch Cements CXMT as China's Chip Champion
  - [japan] Bank of Japan Governor focuses on fixing 2% inflation (Jiji Press)
  - [china] Yonghui Superstores Q3 Net Loss At 82.7 Million Yuan
  - [japan] Japan’s inflation rate reaches 2% target, Bank of Japan President: 13 years of hard work to meet important mil
  - [japan] Bank of Japan determines that 2% inflation target has been achieved (Jiji Press)
  - [china] BYD Company Limited Class A Stock 12‑Month Price Target Cut to CNY 108.62, Implies 32% Upside
  - [taiwan] Export investment exceeded expectations. The economic growth rate in the third quarter was 14.36%, the highest
  - [china] ECB President Christine Lagarde doesn’t want to be neutral anymore and leaves office early
  - [japan] BREAKING NEWS: Kioxia expects 1.36 tril. yen net profit for Oct.-Dec. quarter
  - [japan] BREAKING NEWS: Japan chipmaker Kioxia posts 2.2 tril. yen net profit in April-Sept.
  - [china] The European Central Bank decides to keep interest rates unchanged at 2.5% | International
  - [china] Gansu Jiu Steel Group Hongxing Iron & Steel Q3 Net Loss At 813.7 Million Yuan
  - [japan] Japan's Katayama signals hope of bigger surplus from central bank's ETF sales
  - [china] China's central bank steps up shift toward overnight rate as policy anchor
  - [japan] Chief Cabinet Secretary Kihara maintains “responsible and active fiscal policy”; Bank of Japan effectively rea
  - [japan] Bank of Japan Governor Ueda holds press conference, reaching 2% price target: Experts say this (Reuters)
  - [china] BAIC BluePark New Energy Technology Q3 Net Loss At 922.0 Million Yuan
  - [japan] BOJ stays pat on rates, signals inflation target reached

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
      "published_utc": "2026-10-30T12:22:43+00:00",
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

