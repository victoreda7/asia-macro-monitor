atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-19T02:32:44.778456+00:00
Total: 3000 manchetes

  🇯🇵 Japão          997
  🇨🇳 China          914
  🇹🇼 Taiwan         341
  🇰🇷 Coreia do Sul  748

## O que já está no feed (não repita)

  - [china] China's Economy Expanded 4.5% in Third Quarter, Powered by Exports — WSJ
  - [china] China's daily crude steel output jumps in September on robust exports
  - [china] China's 3Q GDP Growth Tops Expectations
  - [china] CHINA YTD INDUSTRIAL OUTPUT +5.3% Y/Y VS JAN-AUG +5.3% Y/Y
  - [china] CHINA YTD RETAIL SALES +1.1% Y/Y VS JAN-AUG +1.1% Y/Y
  - [china] China's economic growth picks up in third quarter, beating expectations
  - [china] China's Q3 GDP narrowly beats forecasts as strong exports buoy growth
  - [china] China’s Q3 GDP growth accelerates to 4.5%, beating forecast
  - [china] China Retail Sales Strongest in 6 Months
  - [china] China's Home Price Decline Eased Slightly in September
  - [china] China Jobless Rate Edges Lower
  - [china] China Industrial Output Growth Hits 6-Month High
  - [china] China Q3 GDP Growth Beats Estimates
  - [china] BREAKING NEWS: China's GDP grows 4.5% in 3rd qtr, accelerating from 2nd qtr
  - [china] China's factory output growth picks up pace in September, retail sales also
  - [china] China Sep Industrial Output +5.5% On Year; Market Expected +5.5%
  - [china] China's Q3 GDP growth accelerates to 4.5%, beating f'cast
  - [china] China 3Q GDP +4.5% on Year; Market Expected +4.4%
  - [china] China Sep Industrial Output +0.61% On Month
  - [china] China Jan-Sep GDP +4.6% on Year
  - [china] China 3Q GDP +1.2% on Quarter
  - [china] In the third quarter of 2026, the national industrial capacity utilization rate above designated size was 73.1
  - [china] The added value of industrial enterprises above designated size increased by 5.5% in September 2026
  - [china] Total retail sales of consumer goods increased by 1.1% from January to September 2026
  - [china] Basic situation of national fixed asset investment from January to September 2026
  - [china] Basic situation of the national real estate market from January to September 2026
  - [china] The central bank launches 80 billion yuan 7-day reverse repurchase operation today
  - [china] China’s EV Exports Double in September Ahead of Tax Rebate Cut
  - [korea] NPS’s stock holdings lose $136bn in Q3 amid Samsung, SK hynix slump
  - [japan] Japan PM Pledges to Rein in Debt Issuance
  - [china] Yuan Steady Ahead of Major Chinese Economic Data — Market Talk
  - [china] China's new home prices fall in September as recovery remains elusive
  - [china] CHINA PBOC CONDUCTS CNY80 BLN VIA 7-DAY REVERSE REPO MON
  - [japan] Japan's 10-year yield falls on risk aversion, debt issuance pledge
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7208 MON VS 6.7220
  - [china] China New Home Prices Drop the Least in 9 Months
  - [china] Yang Caifang, senior statistician of the Urban Department of the National Bureau of Statistics, interprets the
  - [china] Changes in sales prices of commercial housing in 70 large and medium-sized cities in September 2026
  - [japan] BOJ may need to tighten faster if inflation beats forecast, IMF says
  - [china] The central bank launches 80 billion yuan 7-day reverse repurchase operation

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
      "published_utc": "2026-10-19T02:32:45+00:00",
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

