atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-30T03:02:44.140497+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1275
  🇨🇳 China          766
  🇹🇼 Taiwan         247
  🇰🇷 Coreia do Sul  712

## O que já está no feed (não repita)

  - [korea] Industrial output, retail sales, facility investment down in Aug.
  - [china] China's DeepSeek says it used open-source tools based on Huawei ascend chips
  - [korea] Rupiah gains; Korean won, Philippine peso weaken among mixed Asian FX
  - [china] China's New Mortgage Subsidy Falls Short of Expectations — Market Talk
  - [china] Trade Talks, Rare-Earth Exports Key Near-Term Gauges of U.S.-China Ties — Market Talk
  - [japan] Yen Set for Monthly Advance
  - [china] Chinese stocks inch up after Beijing's fresh stimulus but property stocks slide
  - [china] CHINA PBOC CONDUCTS CNY833.5 BLN VIA O/N REVERSE REPO WEDS
  - [china] China factory activity grows at fastest pace in 5 months in Sept: RatingDog PMI
  - [china] China services growth hits three-month high, private PMI shows
  - [china] China Manufacturing Growth Hits 5-Month High
  - [china] China factory activity hits five-month high in September, private PMI shows
  - [china] China NBS General PMI Rises to 9-Month High
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7351 WEDS VS 6.7411
  - [korea] Samsung Electronics, SK hynix rise as U.S. chip stocks rally
  - [china] China’s next big export could be $1.5 trln of debt
  - [taiwan] Grand Pacific Petrochemical, Air Water join forces to expand Taiwan semiconductor materials business
  - [china] The central bank launches 833.5 billion yuan overnight reverse repurchase operation
  - [china] The central bank's 7-day reverse repurchase operation volume was zero on September 30, and it also carried out
  - [korea] SK Hynix stuck in cloud consolidation below 50% Fib: Live
  - [japan] Industrial production index for August was 1.7% lower than the previous month
  - [japan] "Yinkya" or "Yinkya"? Which one will be happier: the "introvert" who seeks stability or the "extrovert" who se
  - [korea] South Korea finance minister vows to stabilise bond market
  - [japan] Japan Industrial Output Declines Again as Middle East Conflict Drags On
  - [japan] Japan Retail Sales Gain 2.7% On Year In August
  - [japan] Japan August factory output unexpectedly falls
  - [japan] JAPAN AUG RETAIL SALES Y/Y RISE SLOWS FROM JULY AS STORMY WEATHER DAMPENS SEASONAL DEMAND FOR CLOTHING, ELECTR
  - [china] China Stimulus Seen Supporting Growth Target, Not Broader Recovery
  - [japan] Japan Industrial Output Sinks 1.7% In August
  - [japan] Japan industrial production unexpectedly falls in August, retail sales slow
  - [japan] JAPAN AUG RETAIL SALES Y/Y RISE LED BY AUTOS, DEPARTMENT STORES, FOOD/BEVERAGES
  - [japan] JAPAN METI DOWNGRADES ITS VIEW ON RETAIL SALES FOR 1ST TIME SINCE SEPT 2025 REPORT, NOTING S/A 3-MONTH MOVING 
  - [japan] JAPAN AUG RETAIL SALES -1.2% M/M; JULY +2.1%
  - [japan] JAPAN METI DOWNGRADES VIEW: RETAIL SALES TAKING ONE STEP FORWARD AND ONE STEP BACK FROM RETAIL SALES ON UPTREN
  - [japan] MNI JAPAN AUG RETAIL SALES +2.7% Y/Y; JULY +3.7%
  - [japan] JAPAN AUG FACTORY OUTPUT POSTS 2ND STRAIGHT M/M DROP
  - [japan] MNI JAPAN AUG FACTORY OUTPUT -1.7% M/M; JULY -0.2%
  - [japan] Japan's Industrial Production Fell in August But Expected to Rebound
  - [japan] ASIA NIGHT SESSION | Nikkei, TAIEX Futures Rebound Overnight on Chip Strength as US Yields Hit 2007 High
  - [china] China’s ‘Mini Stimulus’ Seen Securing GDP Target, Not Much More

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
      "published_utc": "2026-09-30T03:02:44+00:00",
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

