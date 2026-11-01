atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-01T22:32:43.896489+00:00
Total: 3000 manchetes

  🇯🇵 Japão          926
  🇨🇳 China          863
  🇹🇼 Taiwan         360
  🇰🇷 Coreia do Sul  851

## O que já está no feed (não repita)

  - [japan] Why did he accept the position of Governor of the Bank of Japan, something he once hesitated to do? Haruhiko K
  - [japan] Will the real estate myth end with the Bank of Japan interest rate hike? “Aggressive cash conversion” promoted
  - [korea] South Korea is on the verge of achieving a record $1 trillion in annual exports this month thanks to..
  - [taiwan] Bulgarian presidential runoff exit poll: Acting President Jotova wins | International
  - [japan] Debate continues over the abolition of Japan Post Bank's savings interest cap
  - [japan] Consumption tax reduction bill Ruling party: “Consults for vote” Opposition: “Prime Minister to attend”
  - [china] China's BYD Continues Massive EV Exports. It Isn't Helping. — Barrons.com
  - [korea] South Korea set to become world’s 4th country to hit $1 trillion in annual exports
  - [japan] Japan Weeks Ahead: BOJ Has Cleared First Major Goal of Lifting Near 2% But Still Needs to Anchor Price Rises a
  - [china] The People's Bank of China will conduct overnight reverse repurchases every working day starting from 11/2 to 
  - [korea] Top global stories this week: Shell, HSBC, SK Hynix among notable names
  - [taiwan] Benefitting from AI investment, South Korea's exports doubled in October, the largest increase in half a centu
  - [taiwan] South Korea's exports nearly doubled in October thanks to AI investment, the largest increase in half a centur
  - [china] China’s Communist Party demands loyalty, vows to tighten discipline
  - [korea] Samsung chief Lee visits Japan chip packaging lab
  - [taiwan] Nuit Blanche Taipei brings night of art, performances to Yuanshan
  - [china] China's BYD extends sales growth streak on strong exports
  - [japan] Bank of Japan Maebashi Branch September Tankan flat rate at +15 for third consecutive period (Gunma TV)
  - [japan] Bank of Japan Maebashi Branch September Tankan flat at +15 for third consecutive period (Gunma TV)
  - [china] Tomorrow, the central bank will make important adjustments! A look at next week’s major financial events
  - [japan] Liberal Democratic Party Policy Research Council Chairman Kobayashi “approaches opposition parties for passage
  - [korea] Korea Investment & SBI Holdings plan 10 tn yen fund to build AI data centers in Japan
  - [korea] Samsung Electronics and SK Hynix are sweeping the money. Thanks to the semiconductor supercycle. It
  - [china] PBOC and CSRC to Meet Tomorrow on Tools to Support Capital Markets
  - [japan] Unstoppable high prices: More than 1,400 food items will rise in price in November The policy management of th
  - [korea] [APK 2026] Korean PM urges deeper high-tech ties with Germany in AI, chips
  - [korea] [APK 2026] APK 2026 in Seoul sets stage for deeper AI, supply chain ties amid global turmoil
  - [japan] Former Liberal Democratic Party Chairman Miyazawa also supports the bill: “Given benefits rather than consumpt
  - [china] China’s ‘Upgraded’ Peru Trade Deal Takes Effect, Widening Ties
  - [korea] South Korea Exports Extend Robust Growth on AI-Fueled Chip Boom
  - [korea] As long as I have time... In October, the Monetary Policy Committee decided to ‘freeze’ the base interest rate
  - [taiwan] AI inflation sweeps through the mobile phone market. Industry players: Price pressure may persist until 2028
  - [japan] Semiconductor TSMC's sales exceed the upper limit of expectations, with double-digit sales growth for the Octo
  - [korea] SK hynix hosts first Partners Day in Japan to strengthen chip supply chain
  - [korea] South Korea exports surge 93.7% in October, fastest growth since 1974
  - [japan] Policies that the government should focus on: ``Price control measures'', the most popular policy for the four
  - [korea] South Korea exports nearly double in October on AI investment boom
  - [taiwan] Lifting Her Dreams: Bunun Teenager Wu Yu-Syuan Journey from Taoyuan
  - [korea] S. Korea's monthly exports hit $115.3b in Oct. on strong chip sales
  - [korea] South Korea's Chip-Led Exports Accelerate, Bringing $1 Trln Annual Target Closer — WSJ

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
      "published_utc": "2026-11-01T22:32:44+00:00",
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

