atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-24T21:42:42.796601+00:00
Total: 3000 manchetes

  🇯🇵 Japão          975
  🇨🇳 China          996
  🇹🇼 Taiwan         340
  🇰🇷 Coreia do Sul  689

## O que já está no feed (não repita)

  - [china] EU restricts Chinese-made hybrid cars due to rapid imports, including Japanese-made cars
  - [china] In 2027, the rules of the world will change significantly...The US-China-Russia summit meeting was not ``empty
  - [japan] Why do companies choose the "employment support business" despite constant criticism of "separation of people 
  - [china] US government restricts AI semiconductor exports to Southeast Asia and Brazil due to suspicions of Nvidia Huan
  - [japan] Corporate Japan logs record first-half profit on AI demand, soft yen
  - [japan] Prime Minister Takaichi intends to support Japan's future finances with the huge proceeds from the sale of Ban
  - [japan] Formulation of second supplementary budget plan expected to be limited to Kumamoto earthquake recovery, etc.
  - [korea] Credo Technology Group Holding, Navitas Semiconductor, SiTime, Rambus, and SK hynix stocks trade down, what yo
  - [japan] Prime Minister Takaichi instructs the formulation of the second supplementary budget for this fiscal year, "Li
  - [japan] Ibiden Stocks Soar 14.98% as AI Substrate Maker Leads Tokyo's Chip Rebound
  - [japan] Advantest Stocks Jump 12.45% as Tokyo Chip Testers Lead Huang Rebound
  - [china] Nvidia Faces Fresh China Chip Restrictions Despite Huang's Return
  - [china] US Readies Tariff Hike on China, EU Goods as Soon as Tuesday
  - [china] 800 billion yuan MLF + 500 billion yuan reverse repurchase, the central bank’s long-term “combination punch” w
  - [china] China probes Shanghai party boss Chen Jining, marking fourth Politburo member to fall since 2025
  - [china] China Probes Fourth Politburo Member in Major Leadership Shakeup
  - [china] China extends suspension of ban on US-bound gallium, germanium, antimony exports
  - [china] U.S. technology stocks have collectively pulled back; the central bank will launch an 800 billion yuan MLF ope
  - [japan] Japan Government Keeps Gradual Economic Recovery Outlook;Notes Sluggish Consumer Spending amid Rising Costs, W
  - [china] To prevent fluctuations and guarantee the monthly extension, the central bank will carry out a 7-day reverse r
  - [china] White House prepares sweeping new tariffs on China, EU, and dozens of nations
  - [japan] Prime Minister Takaichi instructs the formulation of the second supplementary budget bill for this fiscal year
  - [china] Country Garden Reports 136 Million Yuan in New Litigation and 1.686 Billion Yuan in Overdue Debt
  - [china] U.S. prepares to raise tariffs on China, EU, other nations - WSJ
  - [china] EU Restricts Import Quotas On Hybrid Cars To Curb Chinese Imports
  - [korea] Bank of Korea interest rate hike forecast, possibility and impact of base rate of 3.25% on November 26
  - [china] US Prepares To Raise Tariffs On China And Other Countries - WSJ
  - [china] U.S. Prepares to Raise Tariffs on China and Other Countries — WSJ
  - [china] China probes Shanghai party boss, Politburo's Chen Jining
  - [china] The latest announcement from the central bank: it will carry out 800 billion yuan MLF operations
  - [japan] Yen Falls Amid Global AI Sector Revival
  - [taiwan] The central bank announced new regulations on stable currency reserves, specifying deposit thresholds and rati
  - [china] 800 billion + 500 billion! The central bank's "combination punch" protects liquidity
  - [china] China's Alibaba Health interim profit falls on supply chain investments
  - [china] China investigates Politburo member Chen Jining, Xinhua says
  - [japan] Japanese Yen Could Stay Weak Through Most of 2027 — Market Talk
  - [china] Chinese cobalt firms race to beat DR Congo’s export ban on key battery material
  - [china] The central bank recently announced that it will carry out 800 billion yuan of MLF operations
  - [china] The People's Bank of China will launch MLF and 7-day reverse repurchase operations on the same day
  - [japan] Yen Falls Against Majors

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
      "published_utc": "2026-11-24T21:42:43+00:00",
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

