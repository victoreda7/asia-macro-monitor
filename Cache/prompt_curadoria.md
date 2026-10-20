atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-20T19:57:04.625635+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1007
  🇨🇳 China          900
  🇹🇼 Taiwan         354
  🇰🇷 Coreia do Sul  739

## O que já está no feed (não repita)

  - [japan] One year since the Takauchi Cabinet was established, it is putting all its effort into enacting the consumptio
  - [japan] Japan budget hotels ramp up overseas push with public baths, free breakfast
  - [japan] Dollar falls as record Japanese bond auction lifts yen, pound surges on jobs data
  - [korea] BOK Financial Q3 2026 slides: margin expansion offsets fee pressure
  - [korea] BOK Financial Corp reports results for the quarter ended September 30 - Earnings Summary
  - [korea] BOK Financial Q3 2026 Earnings Call Is Live
  - [korea] Injective, BDACS plan Korean won stablecoin settlement for tokenized assets
  - [japan] Japan PM's party pushes to fast-track debate on food tax cut
  - [china] EXCLUSIVE: ByteDance, Alibaba, Tencent place over $35 billion worth of Nvidia chip orders
  - [korea] Interest rates likely to rise further after being frozen tomorrow
  - [japan] Preview: Forecasters See Japanese Inflation Picking Up Steam amid Rising Energy Costs, Weak Yen
  - [japan] More than 23,000 cases of information may be leaked in the country's energy-saving housing project
  - [korea] BYD surges to No. 4 in Korea's imported car market
  - [korea] What's the future of AI stock? SK Hynix shares crash to lowest level since Apr as sell-off deepens; down 31% i
  - [china] Nvidia secures $35B in orders for new export-compliant GPU from Chinese tech giants: report
  - [china] BofA Prefers These Semicap Top Picks on Mix, Pricing, NAND, China Upside
  - [china] The central bank will carry out overnight reverse repurchase operations
  - [china] China’s hybrid car exports to EU surge by more than 200% as import cap looms
  - [japan] Food consumption tax reduction bill to be debated in the House of Representatives What financial resources and
  - [china] Micron Invests In US Indium Processing Amid China Export Restrictions – MU Stock Still Dips
  - [taiwan] Starlux expands routes amid AI, chip industry demand
  - [taiwan] 2 workers found without vital signs at Kaohsiung TSMC fab site
  - [korea] Axcelis To Begin Construction Of New Manufacturing Facility In Pyeongtaek, Korea
  - [taiwan] Apple commits up to $100 million for US titanium in domestic manufacturing push
  - [china] China’s rare earth magnet exports to EU and US rebound in September
  - [china] Hormuz Disruption, Chinese Export Curbs Keep Fertilizer Supplies Tight, S&P Says — Market Talk
  - [korea] Finance minister pledges support for global 'AI basic society'
  - [japan] Civil Reform Concerning consumption tax reduction related bill “40,000 yen per person benefit”
  - [china] China's US soybean imports rebounded in September, data shows
  - [japan] Prime Minister Takaichi “works to minimize burden on local governments” in consumption tax reduction bill
  - [taiwan] Micron Taoyuan union announces Oct. 22 solidarity strike
  - [china] London Metal Exchange CEO affirms support for use of yuan
  - [china] Soybeans open Tuesday higher in Chicago with new import data from China on radar
  - [korea] BOK Financial Corporation Stock 12‑Month Price Target Cut to $145.56, Implies 18% Upside
  - [taiwan] September exports smash previous monthly records, up over 60%
  - [china] China and Hong Kong stocks fall; stable growth dampens stimulus expectations
  - [japan] Dollar surrenders gains as record Japanese bond auction sparks Yen rally
  - [china] Chinese Hybrid Import Cap Offers Relief to European Carmakers — Market Talk
  - [china] Cssc Offshore & Marine Engineering Says 9-Month New Orders Totalled 35.8 Billion Yuan
  - [china] China's Strong 3Q Growth Rules out Additional Stimulus — Market Talk

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
      "published_utc": "2026-10-20T19:57:04+00:00",
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

