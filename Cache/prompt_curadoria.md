atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-28T05:09:24.435065+00:00
Total: 3000 manchetes

  🇯🇵 Japão          930
  🇨🇳 China          833
  🇹🇼 Taiwan         387
  🇰🇷 Coreia do Sul  850

## O que já está no feed (não repita)

  - [korea] Kospi hits two-week high on tech rally as SK Hynix plans $75 bn payout on record profit
  - [taiwan] AI-Driven Tech Rise Lifts Taiwan, South Korea Stocks; Asian currencies fall
  - [china] Is Israel afraid of change? The first wave of exit polls exposed! ｜Bosonaro is said to have fled to the United
  - [japan] BOJ Gov. Ueda's Remarks to Be Under Scrutiny for Rate-Hike Hints — Market Talk
  - [japan] BOJ Rate Hold Seen as Done Deal, Putting Focus on Guidance
  - [japan] Presentation of materials on the government's consumption tax reduction bill support funding concept
  - [japan] Bank of Japan decision meeting emphasizes that achieving the price target is still the “gateway” (TBS CROSS DI
  - [taiwan] Taiwan central bank says it will hike interest rate if inflation too hot next year
  - [korea] SK Hynix profit beat fuels $45 billion of dividends, buyback
  - [korea] South Korean Won Retreats from Over 2-Year High
  - [china] China's yuan hovers near 4-year high ahead of Fed decision
  - [korea] SK hynix: Record Q3 earnings, tight AI-memory supply and ~KRW 100tn in planned shareholder returns
  - [japan] Stock price rise Buy orders for stocks such as semiconductors
  - [japan] Yurtec Corp - To Buy Back Up To 2.47% Of Shares Worth 5.5 Billion Yen
  - [japan] The Japanese economy is now an AI-powered economy, with capital investment in exports, stock prices, and even 
  - [korea] Asia stocks rally as SK Hynix earnings boost AI trade; Fed decision ahead
  - [korea] South Korean Stocks Rally as SK Hynix Payout and AI Optimism Boost Markets
  - [korea] Why is Samsung Electronics stock surging today?
  - [korea] Foreign currency deposits rise to fresh record high in Sept.
  - [japan] Yen Weakens as Safe-Haven Appeal Diminishes
  - [china] Is the stock market falsely decoupled from the typhoon? Yang Jinlong: Depending on the attitude of the Financi
  - [korea] NPS sets sights on Silicon Valley startups, tightens risk control on AI bets
  - [korea] Why is SK Hynix stock surging today?
  - [korea] South Korean won, Philippine peso lead declines among Asian currencies
  - [japan] What's New October, 2026 : Ministry of Finance
  - [korea] Micron recruits in South Korea for Taiwan roles as Taoyuan strike dispute persists
  - [taiwan] Cathie Wood Extends Archer, Joby Buying Spree; Ark Sells More AMD, Taiwan Semiconductor Shares
  - [korea] SK hynix’s $45bn shareholder return plan lifts chip stocks
  - [korea] SK Hynix Plans $75 Billion in Shareholder Returns After Blockbuster Earnings — Update
  - [china] CHINA PBOC CONDUCTS CNY151 BLN VIA 7-DAY REVERSE REPO WEDS
  - [china] CHINA PBOC CONDUCTS CNY1 TRLN VIA O/N REVERSE REPO WEDS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7165 WEDS VS 6.7171
  - [japan] Japan bond yields rise as haven demand recedes, BOJ meeting looms
  - [taiwan] Taiwan Central Bank Chief: Never Said CPI Cannot Remain Above +2%
  - [korea] South Korean shares rally 6% as SK Hynix beats forecasts
  - [korea] SK hynix Q3 2026 slides: revenue tops 100T, 80% margin on AI boom
  - [korea] SK Hynix Profit Jumps Seven-Fold to Soothe Doubts Over AI Rush
  - [korea] Choi Won-tae (Samsung Lions) will take the mound at an important moment.Samsung, led by head coach P..
  - [korea] Kospi jumps as chipmakers rally on SK Hynix’s record profit, shareholder returns
  - [korea] Kospi rises 4% after SK Hynix results; Asian stocks gain on AI optimism ahead of US Fed decision

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
      "published_utc": "2026-10-28T05:09:24+00:00",
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

