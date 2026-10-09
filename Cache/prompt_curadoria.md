atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-09T10:22:43.236064+00:00
Total: 2966 manchetes

  🇯🇵 Japão          1204
  🇨🇳 China          796
  🇹🇼 Taiwan         278
  🇰🇷 Coreia do Sul  688

## O que já está no feed (não repita)

  - [japan] Government Cabinet approves bill related to food consumption tax reduction
  - [japan] Japan Machine Tool Orders Surge 60.4% In September
  - [china] Sales of Chinese-made Tesla electric vehicles accelerate in September
  - [china] China's third batch of 2026 fuel export quotas down from year ago, sources say
  - [china] How China’s Stimulus May Shore Up GDP While Reinforcing Imbalances
  - [china] China's central bank buys net 100 billion yuan of sovereign bonds in September
  - [china] EU and China face crunch time in effort to avoid trade war
  - [china] China ramps up fiscal push to meet growth target
  - [china] The central bank invested a net 100 billion yuan in open market government bond sales in September
  - [china] Central Bank: Net investment in open market government bond sales in September was 100 billion yuan
  - [japan] Buy it in a hurry? Or wait and see? ...The Bank of Japan's interest rate hike will increase the burden of home
  - [korea] Just as important as preventing hacking is protecting the user's assets in the event of an accident...
  - [china] China Says It Has No Intention of Depreciating Yuan to Boost Exports
  - [japan] Stock price decline narrows in the afternoon, buyback movement in semiconductor-related stocks
  - [china] China to support expansion of domestic demand, deepen fiscal reform
  - [china] Uzum Says U.S. Investors Remain Interested Despite China Trade Tensions
  - [japan] Dollar Likely to Stay in 155-160 Yen Range — Market Talk
  - [korea] SK chief eyes Gwangju chip fabs alongside Yongin cluster
  - [china] China's tax crackdown increases pressure on luxury brands as US spending weakens
  - [japan] Prime Minister Takaichi: “Consumption tax reduction: reduced burden per person of approximately 36,000 yen”
  - [japan] Iseki&Co Ltd - To Buy Back Up To 1.46% Of Own Shares Worth 500 Million Yen
  - [korea] It was found that the budget of 16 million won was used by the chairman of the Korea Education Facil..
  - [korea] Bank of Korea predicts ‘hawkish freeze’ in base interest rate in October… Additional U.S. tightening is a vari
  - [japan] Osg Corp - To Buy Back Up To 1.8% Of Own Shares Worth 5 Billion Yen
  - [japan] Citi sees limited upside for EUR/JPY amid intervention expectations
  - [japan] Japan Machine Tool Orders Notch Fresh High
  - [china] Broker Sucden Financial wants to clear LME metals trades in offshore yuan
  - [china] China Central Bank Defends Currency Policy Before EU Trade Talks
  - [japan] Is Kyushu experiencing a “warm and rainy winter”? Concerns about rising prices due to crop failures and poor c
  - [korea] South Korean Won Eases
  - [china] Ecobank Taps Yuan Payments, Eyes Africa’s Trade With China
  - [china] The central bank uses multiple tools to protect liquidity, and funding is expected to remain stable in October
  - [china] China's blue-chip stocks hit over one-year low on AI-linked supply chain selloff
  - [china] China to resume fuel exports in Oct after holiday pause, Reuters reports
  - [japan] Asia stocks mixed; chipmakers slide on OpenAI revenue concerns
  - [japan] Issues with food consumption tax reduction: securing financial resources and impact on consumers
  - [china] China to resume October fuel exports after a brief halt, four trade sources say
  - [china] China to resume October fuel exports after holiday pause, sources say
  - [japan] Japan PM vows to keep watching yen, inflation moves carefully
  - [taiwan] TSMC Revenue Likely to Be Driven by Continued Growth in AI Demand — Market Talk

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
      "published_utc": "2026-10-09T10:22:43+00:00",
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

