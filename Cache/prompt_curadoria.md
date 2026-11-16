atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-16T08:32:41.168497+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1007
  🇨🇳 China          872
  🇹🇼 Taiwan         304
  🇰🇷 Coreia do Sul  817

## O que já está no feed (não repita)

  - [japan] BOJ chief Ueda tells government panel wage growth 'quite strong'
  - [china] China-ASEAN Summit China calls for promotion of cooperation in economic and trade fields
  - [japan] Highlights of the Outlook for Economic Activity and Prices (October 2026)
  - [japan] BOJ Current Account Balances by Sector (Oct.)
  - [japan] Japan's GDP growth rate in the third quarter was 0%. High inflation suppressed consumption and led to economic
  - [japan] Japan Real Estate Investment: Rent growth lifts NOI and distributions as annual growth targets rise
  - [korea] HD Hyundai Marine Engine: Engine demand drove 62% revenue growth and a KRW 1,731bn order backlog
  - [korea] Kospi sees worst day in over a week as Nvidia woes, Anthropic IPO drain hit chipmakers
  - [japan] Stock price: Closing price below 60,000 yen; sell orders spread mainly among semiconductor-related stocks
  - [taiwan] Fitch Says US Rate Hikes Have Modest Impact On Taiwan Bills Finance Companies
  - [japan] Wages are quite strongly consistent with 2% inflation - Bank of Japan Governor = Economic and Fiscal Policy Co
  - [japan] Aisan Industry Co., Ltd. - To Buy Back Up To 4.7% Of Shares Worth 7 Billion Yen
  - [china] China’s Economy Disappoints With New Stimulus Yet to Kick In
  - [taiwan] Taiwan, South Korea Tech Stocks Plunge Ahead of Key AI Trials
  - [korea] SK hynix commits $1.05B to strengthen semiconductor supply chain
  - [japan] Japan rubber futures trade in tight range as weaker yen counters lower oil
  - [china] Nissan Turns China Into Export Hub as Sales There Slump
  - [japan] Additional interest rate hikes at fixed intervals and widths Bank of Japan member Takada (Jiji Press)
  - [japan] Japan Industrial Output Recovers Less Than Estimated
  - [japan] Resurgent Inflation to Drive More BOJ Rate Hikes — Market Talk
  - [korea] SK Square: SK Hynix equity earnings drove 9M profit as shareholder returns and AI-led growth advanced
  - [china] Nvidia’s All-Important Q3 Report, China Tech Results, Anthropic IPO And Microsoft Ignite To Keep Investors Hoo
  - [korea] Samsung, SK hynix-linked ELS raises fear of further market volatility
  - [korea] Kospi Falls for Third Straight Session; Chip Stocks Retreat
  - [korea] The top 1% of stock investment returns bought SK Hynix, Samsung Electronics and Doosan the most in e..
  - [korea] It was found that the top 1% of stock investment returns bought the most semiconductor small-cap sto..
  - [japan] Net Protections Holdings, Inc. - To Buy Back Up To 3.5% Of Shares Worth 1.2 Billion Yen
  - [korea] Benchmark rate for banks' mortgage loans continues to rise
  - [japan] Asian markets mostly lower as weak Japan GDP, soft China data, and Nvidia caution weigh
  - [china] Asia stocks tumble as chipmakers slide and weak China data adds pressure
  - [korea] Hyundai Green Food: 9M earnings improved, while working-capital outflows and buybacks shaped cash deployment
  - [japan] Hawkish BOJ policymaker Takata calls for swift hike in rates to ’good’ position
  - [china] China's October retail sales ease to 0.4%, factory output slows to 4.8%, while jobless rate dips to 5.1%
  - [taiwan] Qisda affiliate Ace Pillar deepens semiconductor and AI automation push, expanding into wafer regeneration and
  - [china] China’s Economy Weakens More Than Forecast Despite Stimulus Push
  - [japan] Japan’s economy contracts 0.1% annualized in Q3; September industrial output rebounds 2.0%
  - [taiwan] Interest rate hike in December? Yang Jinlong: Three key points need to be considered: inflation and lending po
  - [korea] Korea's wage, productivity gaps widen amid chip-led growth: KDI
  - [japan] Weak Consumption Likely to Keep Japan's Economy in Low Gear — Market Talk
  - [japan] Weak Japan Consumption Could Deepen BOJ Board Divisions — Market Talk

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
      "published_utc": "2026-11-16T08:32:41+00:00",
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

