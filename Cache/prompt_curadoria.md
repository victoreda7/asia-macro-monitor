atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-24T12:12:44.774935+00:00
Total: 3000 manchetes

  🇯🇵 Japão          991
  🇨🇳 China          976
  🇹🇼 Taiwan         341
  🇰🇷 Coreia do Sul  692

## O que já está no feed (não repita)

  - [china] China's Alibaba Health interim profit falls on supply chain investments
  - [china] China investigates Politburo member Chen Jining, Xinhua says
  - [japan] Japanese Yen Could Stay Weak Through Most of 2027 — Market Talk
  - [china] Chinese cobalt firms race to beat DR Congo’s export ban on key battery material
  - [china] The central bank recently announced that it will carry out 800 billion yuan of MLF operations
  - [china] The People's Bank of China will launch MLF and 7-day reverse repurchase operations on the same day
  - [japan] Yen Falls Against Majors
  - [china] The central bank will carry out 800 billion yuan of MLF operations, and the total amount of liquidity operatio
  - [taiwan] Industrial production up 32nd straight month on strong AI demand
  - [japan] Proposal to tighten identity verification to combat gold smuggling approved by LDP executive committee
  - [china] China's Huawei says it has homegrown answer to US chip design tool curbs
  - [taiwan] Why Taiwan’s chip industry welcomes Jensen Huang’s Nvidia comeback
  - [china] After the three meetings between Sichuan and Xi, Beijing extended the suspension of the ban on exports of gall
  - [china] The central bank launched an 800 billion yuan MLF operation on November 25 for a period of one year
  - [korea] Will Korea tighten its belt again? 54% of bond market experts say “base rate hike in November” By EBN
  - [china] Chinese automakers gain ground in Europe as EU car sales rise 5.4% YTD
  - [japan] Budget formulation basic policy proposal “Aiming for both a strong economy and fiscal sustainability”
  - [japan] Prime Minister Takaichi instructs the formulation of the second supplementary budget for this fiscal year, "Li
  - [china] China to Suspend Some Critical-Material Export Curbs to U.S. Until January
  - [japan] Japanese prime minister orders extra budget, economy minister says
  - [china] China Vanke To Hold Bondholder Meeting On December 8 For Yuan Notes Due December 15
  - [china] China, India set for record Russian oil imports in 2026, but demand seen peaking
  - [japan] Prime Minister Takaichi instructs the formulation of the second supplementary budget bill for this fiscal year
  - [japan] Prime Minister Takaichi instructs Finance Minister Katayama to formulate the second supplementary budget for F
  - [japan] Opinions regarding the effects of consumption tax reduction, etc. Central public hearing of the House of Counc
  - [japan] UBS sees USD/JPY at 158 through 2027 on rate differentials
  - [china] Central Bank: Launch 800 billion yuan MLF operation on November 25, with a term of 1 year
  - [china] Bond market closes | The central bank will launch a 500 billion seven-day reverse repurchase operation tomorro
  - [taiwan] TSMC eyes US$22.6 billion Texas campus for 2nm chips
  - [china] The central bank will launch a 500 billion yuan 7-day reverse repurchase operation
  - [china] Central Bank: 800 billion yuan MLF operation will be carried out on November 25
  - [japan] Interview: Whether the Bank of Japan will raise interest rates to 2% next year, difficult to judge due to econ
  - [china] EU sets limits on hybrid vehicle imports from China and other countries
  - [china] The central bank will carry out 800 billion yuan MLF operation
  - [china] Extended Chinese Suspension of Export Curbs Covers Items Including Critical Minerals, Superhard Materials
  - [china] Central Bank: Will launch 500 billion yuan 7-day reverse repurchase operation on November 25
  - [china] Analysis: Trade Surplus, Capital Inflows Drive Yuan’s Rise
  - [japan] Japan vows sustainable finances and BOJ independence in budget guideline
  - [china] China Extends Suspension of Export Restrictions on Some Dual-Use Materials to U.S.
  - [china] EU Adopts Cap on Hybrid Cars to Help Curb Chinese Imports

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
      "published_utc": "2026-11-24T12:12:45+00:00",
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

