atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-11T00:42:42.692107+00:00
Total: 3000 manchetes

  🇯🇵 Japão          920
  🇨🇳 China          897
  🇹🇼 Taiwan         318
  🇰🇷 Coreia do Sul  865

## O que já está no feed (não repita)

  - [korea] Seoul shares turn higher after weak start amid inflation woes
  - [korea] Even mention of the US ‘big step’… Will the Bank of Korea raise interest rates despite ‘AI risk’? [Money]
  - [korea] (LEAD) Seoul shares turn higher after weak start amid inflation woes
  - [korea] (LEAD) Exports more than double in 1st 10 days of Nov.
  - [korea] Seoul shares open lower on inflation woes
  - [korea] South Korea November 1-10 exports surge 111.9% year/year
  - [korea] S. Korea to extend fuel tax cuts through Jan. to ease price burdens
  - [china] Nvidia faces deepening scrutiny over China chip ties, CEO affair
  - [taiwan] LWLG: Foxconn system demo advances polymer optics; foundry delays move volume production to 2028
  - [japan] Considering registration system for business employing people with disabilities
  - [taiwan] TSMC, Microsoft executives debate AI's impact on Day 2 of Nikkei Dialogue
  - [china] US lawmakers push China chip rules after Nvidia CEO allegations
  - [japan] SoftBank Group Corp. Stock 12‑Month Price Target Cut to JPY 8677.28, Implies 155% Upside
  - [china] Still possible chipmaker Nexperia could reunite with Chinese operations, CEO says
  - [korea] Exicure, Inc. Announces Agreement to Sell GPC-100 Program Assets to GPCRT Inc. for KRW 6.5 Billion
  - [korea] Exicure, Inc. (XCUR) Agrees to Sell GPC-100 Assets for KRW 6.5B
  - [korea] Exicure (XCUR) Agrees to Sell GPC-100 Assets for KRW 6.5B
  - [japan] There is no need for a ``Declaration of Overcoming Deflation.'' We must not repeat the mistake of the Bank of 
  - [china] Alice Huang, Chinese businesswoman tied to Nvidia CEO, went from finance to chips
  - [japan] Consumption tax reduction bill will be debated in the House of Councilors today, leading to debate among the r
  - [japan] SoftBank Group Corp. Stock 12‑Month Price Target Cut to JPY 8810.23, Implies 159% Upside
  - [china] NVIDIA Stocks Slide 4.43% as Report Alleges $7.5 Billion in Chips Reached China
  - [korea] Samsung Electronics Stocks Climb 4.74% as Chip Rebound Pushes Shares Near 200,000 Won
  - [korea] SK hynix Stocks Jump 6.69% as Seoul Chip Rally Lifts KOSPI 4.39%
  - [taiwan] TSMC Just Delivered the AI Growth Shock Wall Street Was Waiting For
  - [china] COMMENTARY: China's crude oil imports recover, fuel exports not so much
  - [china] Xin Yuan Enterprises Says PLH Enters Additional Irrevocable Undertaking For PLH Second IU Shares
  - [china] Shanghai Electric integrates industrial artificial intelligence into high-power gas turbine manufacturing and 
  - [taiwan] TSMC's October Sales Climb 14.7% Sequentially
  - [china] Microsoft urges US to reconsider potential import ban on Chinese optical transceivers: report
  - [china] China Everbright Says Court Orders Release Of Asset Preservation Measures Over Chongqing Yingli Real Estate In
  - [china] How Nvidia CEO’s troubles, US midterms may tighten China chip curbs: ‘adding fuel to fire’
  - [taiwan] TSMC earmarks up to $1bn to buy Anthropic and OpenAI shares
  - [taiwan] TSMC investirá até US$ 1 bilhão na Anthropic e na OpenAI
  - [taiwan] TSMC to invest up to $1 billion in Anthropic, OpenAI
  - [taiwan] TSMC and SoftBank Reveal a Chasm Between AI Winners and Losers — Barrons.com
  - [taiwan] Taiwan Semiconductor's October sales offer up 'strong start' to quarter, Wedbush says
  - [korea] Louis Vuitton hit by stock slump, stronger won in South Korea
  - [china] China's crude oil imports recover, fuel exports not so much: Russell
  - [japan] Honda upwardly revised its earnings forecast for this fiscal year due to weaker yen and increased sales of HVs

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
      "published_utc": "2026-11-11T00:42:42+00:00",
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

