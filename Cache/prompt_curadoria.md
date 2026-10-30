atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-30T08:22:45.102112+00:00
Total: 3000 manchetes

  🇯🇵 Japão          931
  🇨🇳 China          834
  🇹🇼 Taiwan         363
  🇰🇷 Coreia do Sul  872

## O que já está no feed (não repita)

  - [japan] BOJ chief Ueda says 2% inflation goal not yet sustainably achieved
  - [taiwan] Taiwan Q3 preliminary GDP beats forecasts on solid AI demand
  - [japan] BOJ's Ueda Hails Inflation Progress But Says Battle Isn't Over
  - [japan] Today's Oha Biz October 30th (Friday) What is the terminal rate (achieved interest rate)?
  - [japan] Bank of Japan Likely to Wait Before Further Tightening — Market Talk
  - [china] Qi An Xin Tech Q3 Net Loss At 757.5 Million Yuan
  - [china] Audi cuts 2026 outlook on China weakness, price pressure
  - [china] New China Life Insurance Q3 Net Loss At 511 Million Yuan
  - [taiwan] Taiwan 3Q GDP +3.21% From 2Q
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Transaction with Affiliate Company
  - [taiwan] Taiwan 3Q GDP +14.36% On Year; Market Expected +12.0%
  - [china] Advanced Micro-Fabrication Equipment Inc China Q3 Net Profit Up 159.0% Y/Y
  - [korea] ADX Says Units Of PLUS Korea Manufacturing Core Alliance Index ETF Will Be Listed On ADX On Nov 02
  - [taiwan] Taiwan's Inflation Likely to Remain Elevated — Market Talk
  - [taiwan] Taiwan Q3 preliminary GDP +14.36%, better than forecast
  - [china] Key facts: Haleon (HLN) Q3 +2.6%; China import pause; £500m buyback
  - [japan] BOJ declares victory in hitting price target, signals near-term hikes
  - [japan] Bank of Japan Governor says that the 2% target is "generally consistent" with the underlying price index still
  - [japan] BREAKING NEWS: BOJ's plan to step up ETF selling will have limited market impact: Ueda
  - [korea] Samsung Electronics to buy 1.27 trillion won worth of shares in TCL China from Samsung Display
  - [japan] Bank of Japan Governor Ueda says, ``It is important to achieve a sustained and stable inflation rate of 2%, an
  - [japan] Yen Extends Gains Against Dollar After BOJ Keeps Rates Steady
  - [japan] Bank of Japan cuts, ETF trading accelerates "limited impact" (Joint Communications)
  - [china] UNIQLO Shanghai Flagship Store Renovation Japanese Retailer in China Moves to Review Stores
  - [japan] Inflation rate is "mostly consistent", says Bank of Japan governor, 14 years on from deflation (Kyodo News)
  - [japan] Bank of Japan decides to keep policy interest rate unchanged at 1.25%; underlying price increase rate is ``gen
  - [china] BYD Company Limited Class A Stock 12‑Month Price Target Cut to CNY 110.56, Implies 34% Upside
  - [korea] Hyundai Motor Company Stock 12‑Month Price Target Cut to KRW 554096.77, Implies 89% Upside
  - [japan] BOJ to accelerate ETF sales, more than doubling pace from January
  - [japan] Japan Housing Starts Fall 2.7% In September
  - [japan] Bank of Japan Governor says interest rate hike will be decided including next meeting (Kyodo News)
  - [japan] BREAKING NEWS: All BOJ board members agree inflation consistent with 2% goal: Ueda
  - [japan] BREAKING NEWS: BOJ chief declines to comment on reviewing accord with gov't on deflation
  - [japan] Bank of Japan Governor reviews joint statement and makes no comment (Kyodo News)
  - [japan] BREAKING NEWS: BOJ monetary policy focus more on anchoring inflation to target: Ueda
  - [japan] BOJ Governor Ueda’s comments at news conference
  - [japan] BREAKING NEWS: BOJ to continue raising rates looking at inflation, other factors: Ueda
  - [japan] Bank Of Japan Holds Key Rate As Expected
  - [japan] BREAKING NEWS: BOJ chief Ueda stresses need to stabilize inflation at around 2%
  - [japan] Makita Corporation - To Buy Back Up To 3.9% Own Shares Worth 40 Billion Yen

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
      "published_utc": "2026-10-30T08:22:45+00:00",
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

