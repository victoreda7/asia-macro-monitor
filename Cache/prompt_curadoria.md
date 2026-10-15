atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-15T06:12:42.450440+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1121
  🇨🇳 China          844
  🇹🇼 Taiwan         300
  🇰🇷 Coreia do Sul  735

## O que já está no feed (não repita)

  - [taiwan] TSMC profit soars 69% in another record quarter fueled by AI boom
  - [taiwan] TSMC Reiterates 2026 Capex Between US$60B-US$64B
  - [taiwan] TSMC Expects 4Q Revenue Between US$52.3B-US$54.3B
  - [taiwan] TSMC Expects 4Q Gross Margin Between 65%-67%
  - [taiwan] AI Demand Extends TSMC's Record Earnings Streak
  - [japan] Today's Oha Biz October 15th (Thursday) U.S. Consumer Price Index continues to grow rapidly
  - [japan] Japan August industrial production revised down to -2.4% M/M; core machine orders rise 5.2%
  - [japan] IMF: Japan to fall to 6th in 2027 global GDP rankings
  - [taiwan] TSMC Q3 profit surges more than expected to record high on AI-fueled demand
  - [korea] Asia markets in red: South Korea and Japan lead deep tech selloff; Japan industrial output revised down
  - [taiwan] TSMC Q3 profit jumps 69% to record, beating expectations
  - [japan] U.S. semiconductor company plans to build new factory for up to 3 trillion yen based on Japan-U.S. agreement
  - [taiwan] Lucro da TSMC no terceiro trimestre salta 69%, atingindo um recorde e superando as expectativas
  - [taiwan] TSMC 3Q Revenue From Internet of Things Rose 5% on Quarter >2330.TW
  - [korea] Samsung's top brass converge in Tokyo as Japan chip ties deepen
  - [taiwan] TSMC 3Q Revenue From High Performance Computing Up 22% on Quarter >2330.TW
  - [taiwan] TSMC 3Q Gross Margin 66.4%, Up 6.9 Pct Pt on Year >2330.TW
  - [taiwan] Taiwan Semiconductor Manufacturing Co. 3Q Net Profit Beat TWD731.77B Expected in a FactSet Poll >2330.TW
  - [taiwan] Taiwan Semiconductor Manufacturing Co. 3Q Rev TWD1.494T Vs. TWD989.92B >2330.TW
  - [taiwan] Taiwan Semiconductor Manufacturing Co. 3Q Net TWD763.1B >2330.TW
  - [china] EU leaders to tackle China exports, energy prices, budget at summit
  - [china] This Chinese export boom really has legs – and wings
  - [japan] Bank of Japan member Koeda: ``We won't be overly cautious about raising interest rates.''
  - [japan] Japan to invest up to $21 billion in two GlobalFoundries chip factories in New York By Reuters
  - [korea] SK Hynix, Samsung fall as market fears higher rates could curb AI expansion
  - [japan] BOJ Member Koeda's Speech Reinforces Scope for Further Rate Hikes — Market Talk
  - [japan] Asian stocks sell off as AI trades crumble after hot US inflation data By Reuters
  - [taiwan] ByteDance taps MediaTek for custom data center chips - report
  - [korea] South Korean Won Falls Further on Tech Rout
  - [japan] Japan Industrial Output Falls More than Initially Anticipated
  - [korea] Kospi crashes 8% as Samsung, SK hynix sink over 10%
  - [korea] Stock Crash: SK Hynix plunges 57% from peak in four months, loses nearly $700 billion in value
  - [china] China's yuan gains as Fed rate caution knocks dollar from 18-month high
  - [japan] Asia FX mixed, dollar slips after hot U.S. CPI; yen firms on intervention warnings
  - [korea] Hot US inflation hammers Kospi nearly 6% lower as chips buckle
  - [china] China stocks fall, led by tech, as US inflation stokes Fed fears
  - [korea] Hyundai Motor Company Stock 12‑Month Price Target Cut to KRW 592032.26, Implies 89% Upside
  - [china] China's Export Surge Creates Winners as Well as Losers in Asia — Market Talk
  - [korea] Won-Yen Divergence May Likely Be Due to Chip Demand Boom — Market Talk
  - [japan] Japan, U.S. reach first chip deal under $550 bln investment plan By Investing.com

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
      "published_utc": "2026-10-15T06:12:42+00:00",
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

