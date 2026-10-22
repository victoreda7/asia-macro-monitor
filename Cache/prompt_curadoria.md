atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-22T01:22:46.126221+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1005
  🇨🇳 China          853
  🇹🇼 Taiwan         358
  🇰🇷 Coreia do Sul  784

## O que já está no feed (não repita)

  - [japan] Japan MOF To Auction Y3.3T Of TD-Bills Oct 29
  - [korea] Bank of Korea holds rates after back-to-back hikes
  - [korea] Vice budget minister calls Future Fund 'fiscal innovation' for future growth
  - [korea] BOK holds key rate steady at 3% after 2 consecutive rate hikes
  - [korea] BOK pauses rate hikes as inflation, debt concerns linger
  - [korea] BOK holds key rate steady at 3 pct
  - [korea] Bank of Korea Holds Rate Steady After Back-to-Back Hikes
  - [korea] The Bank of Korea freezes the base interest rate by 3%... Avoid three consecutive raises
  - [korea] [Breaking News] Bank of Korea freezes base interest rate at 3.00% per annum... ‘Taking a breather’ after conse
  - [korea] [Breaking News] Bank of Korea base interest rate maintained at 3.00%… U.S. Federal Reserve action is also a va
  - [korea] BOK stands pat in October following back-to-back policy rate hikes
  - [korea] The Bank of Korea freezes the base interest rate at 3.00% per annum... Take a breath after two impressions
  - [korea] Bank of Korea freezes base interest rate at 3.00% per annum... ‘Taking a breath’ personality (step 1)
  - [korea] [Breaking News] Bank of Korea freezes base interest rate... Maintain 3% per year
  - [korea] Bank of Korea holds rates as expected after back-to-back hikes
  - [japan] Bank of Japan Accounts (October 20)
  - [korea] Bank of Korea Holds Rates as Expected
  - [korea] Bank of Korea freezes base interest rate at 3.00% per annum, paying attention to whether further increase in N
  - [japan] Cuts announced to Japan's eco-friendly car subsidies
  - [korea] [Breaking News] Bank of Korea freezes base interest rate at 3.00%
  - [korea] Bank of Korea freezes base interest rate at 3.00%... ‘Speed ​​adjustment’ after continuous impression
  - [korea] [Breaking News] Bank of Korea freezes base interest rate at 3.0%... Taking a breath after two impressions
  - [korea] Bank of Korea freezes base interest rate at 3.00% per annum (Breaking News)
  - [japan] Japan funding conditions still loose despite interest rate hikes, survey shows
  - [korea] [Breaking News] Bank of Korea freezes base interest rate at 3.00% per annum
  - [korea] [Breaking News] Bank of Korea freezes base interest rate... 3.00% per annum
  - [korea] [Breaking News] Bank of Korea, ‘taking a breather’ in base interest rate… Freeze 3.00% per annum
  - [japan] JGB Yield Curve Flattens Amid Continued AI-Related Credit Concerns — Market Talk
  - [korea] [Breaking News] Bank of Korea freezes base interest rate at 3.0% per annum
  - [korea] [Breaking News] Bank of Korea decides to take a breather and freezes base interest rate... 3.00% per annum
  - [korea] [Breaking News] Bank of Korea freezes base interest rate at 3.0% per annum - Money Today
  - [korea] [Breaking News] Bank of Korea freezes base interest rate... 3.0% per annum
  - [korea] [Breaking News] Bank of Korea base interest rate frozen at 3.00% per annum
  - [korea] [Breaking News] Bank of Korea base interest rate maintained at 3.00% per annum... Take a breath after two impr
  - [korea] [Breaking News] Bank of Korea freezes base interest rate at 3.0% per annum... ‘taking a breather’ after two hi
  - [korea] [Breaking News] Bank of Korea maintains base interest rate at 3% - Chosun Biz
  - [taiwan] Taiwan tech supply chain eyes Texas for first US industrial cluster
  - [japan] Now that we have entered the ``age of interest rates,'' should you really buy or rent a house? Hiroyuki's ``ex
  - [korea] Bank of Korea decides base interest rate today... Weight on ‘Maintain’
  - [korea] The Bank of Korea is likely to freeze its base interest rate... Pay attention to the possibility of additional

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
      "published_utc": "2026-10-22T01:22:46+00:00",
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

