atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-22T10:22:44.947619+00:00
Total: 3000 manchetes

  🇯🇵 Japão          967
  🇨🇳 China          852
  🇹🇼 Taiwan         356
  🇰🇷 Coreia do Sul  825

## O que já está no feed (não repita)

  - [korea] Merck opens Korean chip materials plant to meet advanced memory demand
  - [china] Chow Tai Fook Jewellery Logs Q2 Chinese Mainland Retail Sales Value Down 5.3%
  - [korea] BOK pauses rate hikes as inflation, debt concerns linger
  - [korea] Vice budget minister calls Future Fund 'fiscal innovation' for future growth
  - [korea] BOK holds key rate steady at 3% after 2 consecutive rate hikes
  - [japan] Yen Rises Amid Risk-off Mood
  - [korea] Bernstein says Samsung overtook SK hynix in HBM revenue in 3Q26
  - [taiwan] Taiwan's first-ever chip workers strike hits Micron plant
  - [japan] Lower House committee to debate consumption tax cut
  - [china] China blue-chip index confirms bear market as AI stocks slump
  - [taiwan] TSMC seeks factory-equipment alternatives to thwart China's rare earths grip, sources say
  - [korea] Power generators fume over push to cut regional electricity rates: “We’re being saddled with 650 billion won i
  - [japan] Yen set for biggest rally in a month; risk-averse investors shun dollar
  - [korea] After Pause, End of BOK Tightening Cycle Now in Sight — Market Talk
  - [china] Zhejiang Wazam New Materials Q3 Net Profit At 627.0 Million Yuan
  - [japan] Japan to consider re-introducing gas and electricity subsidies, sources say
  - [japan] BOJ to hold rate at 1.25% at meeting next week
  - [japan] Japanese Government Bonds Held by the Bank of Japan
  - [japan] Japan's 2027 Wage Talks Could Shape BOJ Rate Hikes — Market Talk
  - [korea] Financial Services Commission Chairman Lee Eok-won said on the 22nd that SK Hynix's push to list its..
  - [korea] [Issue & People] Bank of Korea base interest rate freeze… What is the meaning of President Shin Hyun-song’s re
  - [japan] Japan's Daiichi Life keeps focus on yen bond swaps, expects cuts in overseas debt
  - [korea] Samsung Electro-Mechanics gets $2.8 billion chip investment from Tesla, Nvidia, report says
  - [japan] Japan's Top Labor Union Targets Big Pay Bump, in Line With BOJ Aims
  - [japan] Yen rallies as dollar slips to 3-wk low; traders eye central bank meetings
  - [korea] S. Korean won strengthens against U.S. dollar after BOK holds key rate
  - [japan] Yen Rises Against Majors
  - [korea] Samsung Electro-Mechanics receives investment of US$2.8 billion for the production of chips from Tesla and Nvi
  - [korea] BOK pauses in its tightening campaign with policy rates at 3%; November hike on the table
  - [japan] Developments in Real Exports and Real Imports
  - [japan] In absence of sovereign buyers, Indian chip firms find clients in Japan, EU
  - [japan] Japan's Nikkei slides as AI capex caution weighs on chip shares
  - [korea] South Korean shares log 6-month closing low as chipmakers fall on profit-taking
  - [japan] Yen rallies as dollar wobbles toward Fed meeting By Reuters
  - [korea] [Exclusive] Samsung Electro-Mechanics to receive 3.7 trillion won from Tesla and NVIDIA to build AI chip subst
  - [korea] BOK pauses rate hikes, but signals more may come
  - [japan] Six opposition parties in the House of Councilors consumption tax reduction bill “call for establishment of a 
  - [korea] Strong chip exports expected to spill over into private consumption from next year: BOK report
  - [japan] Singapore Dollar Gains on Yen as Carry Funder, Analysts Say
  - [china] COMMENTARY: China uses crude stockpiles, but rising oil imports may curtail draws

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
      "published_utc": "2026-10-22T10:22:45+00:00",
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

