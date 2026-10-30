atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-30T08:42:44.022203+00:00
Total: 3000 manchetes

  🇯🇵 Japão          924
  🇨🇳 China          838
  🇹🇼 Taiwan         366
  🇰🇷 Coreia do Sul  872

## O que já está no feed (não repita)

  - [china] China Life Insurance Q3 Net Loss At 45.1 Billion Yuan
  - [japan] BOJ's Ueda Hails Inflation Progress But Says Battle Isn't Over
  - [china] Trump’s days of running US-China relations on personal ties are numbered
  - [japan] BOJ's Decision to Hold Likely to Have Limited Impact on Yen — Market Talk
  - [taiwan] Chip design company MediaTek says growth in demand for AI will "absolutely" continue
  - [china] Flat Glass Q3 Net Loss At 472.7 Million Yuan
  - [japan] [Key points explained] Reading Bank of Japan Governor Ueda's press conference & economists' predictions for in
  - [china] New Hope Liuhe Q3 Net Loss At 865.8 Million Yuan
  - [china] China set to lose LNG import crown to Japan on weak demand
  - [taiwan] Taiwan Q3 GDP Growth Beats Expectations
  - [japan] Yen Rises Against Majors
  - [taiwan] Chip designer MediaTek says AI demand growth will continue 'for sure'
  - [japan] BOJ May Move Away From Predictable Hiking Cadence Beyond March 2027 — Market Talk
  - [china] BBMG Q3 Net Loss At 1.5 Billion Yuan
  - [japan] BOJ chief Ueda says 2% inflation goal not yet sustainably achieved
  - [taiwan] Taiwan Q3 preliminary GDP beats forecasts on solid AI demand
  - [japan] Today's Oha Biz October 30th (Friday) What is the terminal rate (achieved interest rate)?
  - [japan] Bank of Japan Likely to Wait Before Further Tightening — Market Talk
  - [china] Qi An Xin Tech Q3 Net Loss At 757.5 Million Yuan
  - [china] Audi cuts 2026 outlook on China weakness, price pressure
  - [china] New China Life Insurance Q3 Net Loss At 511 Million Yuan
  - [taiwan] Taiwan 3Q GDP +3.21% From 2Q
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Transaction with Affiliate Company
  - [taiwan] Taiwan 3Q GDP +14.36% On Year; Market Expected +12.0%
  - [china] Advanced Micro-Fabrication Equipment Inc China Q3 Net Profit Up 159.0% Y/Y
  - [japan] ``Underlying price increase rate'' reached 2% target; Bank of Japan Governor Ueda says ``The outlook will rema
  - [korea] ADX Says Units Of PLUS Korea Manufacturing Core Alliance Index ETF Will Be Listed On ADX On Nov 02
  - [taiwan] Taiwan's Inflation Likely to Remain Elevated — Market Talk
  - [taiwan] Taiwan Q3 preliminary GDP +14.36%, better than forecast
  - [china] Key facts: Haleon (HLN) Q3 +2.6%; China import pause; £500m buyback
  - [japan] Japan's anime market tops 4 tril. yen for 1st time
  - [japan] BOJ declares victory in hitting price target, signals near-term hikes
  - [japan] Bank of Japan Governor says that the 2% target is "generally consistent" with the underlying price index still
  - [japan] BREAKING NEWS: BOJ's plan to step up ETF selling will have limited market impact: Ueda
  - [korea] Samsung Electronics to buy 1.27 trillion won worth of shares in TCL China from Samsung Display
  - [japan] Bank of Japan Governor Ueda says, ``It is important to achieve a sustained and stable inflation rate of 2%, an
  - [japan] Yen Extends Gains Against Dollar After BOJ Keeps Rates Steady
  - [japan] Bank of Japan cuts, ETF trading accelerates "limited impact" (Joint Communications)
  - [china] UNIQLO Shanghai Flagship Store Renovation Japanese Retailer in China Moves to Review Stores
  - [japan] Inflation rate is "mostly consistent", says Bank of Japan governor, 14 years on from deflation (Kyodo News)

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
      "published_utc": "2026-10-30T08:42:44+00:00",
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

