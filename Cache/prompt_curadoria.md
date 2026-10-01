atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-01T02:52:45.612774+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1286
  🇨🇳 China          759
  🇹🇼 Taiwan         258
  🇰🇷 Coreia do Sul  697

## O que já está no feed (não repita)

  - [japan] [Today's Oha Biz October 1st (Thursday)] Nidek final deficit 564.6 billion yen
  - [japan] What is the NHK public opinion poll? Survey targets and methods
  - [china] China's PMI Improvement May Not Be Sign of Economic Recovery — Market Talk
  - [japan] Japan 10-Year Yield Rises on Hawkish BOJ Outlook
  - [japan] Tankan Supports View for Faster-Than-Before BOJ Rate Hikes — Market Talk
  - [korea] Lotte expands financial, export support for partners
  - [japan] Japan business mood reaches 8-year high, bolsters case for BOJ hikes
  - [japan] Japan's Nikkei hits six-week high as Micron forecast lifts chip stocks
  - [korea] South Korean won, Thai baht lead losses across Asian currencies
  - [japan] Yen Weakens as Dollar, Treasury Yields Weigh
  - [japan] Bank of Japan's short view on the 6th period of continuous improvements in the large enterprise manufacturing 
  - [japan] Bank of Japan Tankan: Large companies and non-manufacturing industries worsen for the first time in five quart
  - [japan] Bank of Japan's main opinions were less hawkish than expected (NRI researcher's commentary on current events)
  - [korea] Korea moves to cut bond issuance as high rates bite
  - [japan] Need to accelerate pace of interest rate hikes; strong economy, wary of upward movement in prices; Bank of Jap
  - [japan] BOJ Summary Points to Growing Risk of Inflation Overshooting Target
  - [korea] SK Hynix to review shareholder protection measures after reports of Solidigm's US IPO
  - [taiwan] TSMC weighs investment in Texas to expand U.S. chip production, Reuters reports
  - [korea] South Korea’s Export Growth Extends Rally as Chip Boom Rolls on
  - [korea] S.Korea Sept exports hit record high as AI boom drives chip sales to all-time peak
  - [japan] Japan MOF To Auction Y600.0B Of 30-Year Govt Bonds Oct 8
  - [korea] AI Boom Powers South Korea's September Exports Past $120 Billion — Update
  - [korea] South Korea stocks slip despite stellar exports as oil worries weigh
  - [japan] Japan MOF To Auction Y3.0T Of TD-Bills Oct 8
  - [taiwan] AI chip packaging demand meets labor pushback: ASE's NT$5.6B Taiwan snack factory deal sparks strike vote
  - [japan] Japan Manufacturing Sector Ebbs In September - S&P Global
  - [korea] SK Hynix trapped in no-trade zone at ₩1,778,000: Live levels
  - [taiwan] SG Semiconductor builds brand and talent for Singapore chip industry
  - [japan] Bank of Japan summary affirms priority is avoiding inflation overshoot
  - [taiwan] Key facts: TSMC (2330) $265B U.S. investment; $60–$64B capex outlook; Q3 results Oct. 15
  - [japan] Some say there is no choice but to accelerate interest rate hikes if there are signs of an upward trend in pri
  - [taiwan] Taiwan Manufacturing Expands Most Since 2021
  - [korea] South Korea Manufacturing Growth Accelerates in September
  - [taiwan] TSMC avalia possível investimento no Texas, segundo fontes
  - [taiwan] TSMC evaluates potential Texas investment, sources say
  - [japan] Japan Big Manufacturers More Optimistic Despite Headwinds
  - [japan] Japan Manufacturing Growth at 6-Month Low, Confirmed
  - [korea] South Korea factory growth hits 4-month high as export orders boom, PMI shows
  - [japan] [Japanese Market Conditions] Yen falls to 157 yen-lower level following Bank of Japan's ``main opinion'' - bon
  - [japan] Japan September factory growth slows to 6-month low, PMI shows

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
      "published_utc": "2026-10-01T02:52:45+00:00",
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

