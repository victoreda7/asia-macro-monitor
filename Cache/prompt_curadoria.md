atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-02T10:02:45.913583+00:00
Total: 3000 manchetes

  🇯🇵 Japão          924
  🇨🇳 China          871
  🇹🇼 Taiwan         355
  🇰🇷 Coreia do Sul  850

## O que já está no feed (não repita)

  - [china] ZAWYA: Ten projects signal broader Oman-China manufacturing ties
  - [japan] Yomiuri: Fujifilm Bets 10 Billion Yen on Magnetic Data Storage Resurgence
  - [china] Far East Smarter Energy's Units Win Bids, Sign Contracts Worth 1.5 Billion Yuan
  - [china] PBOC: 31 Securities, Fund Companies Have Applied for Quotas Exceeding CNY100B
  - [china] PBOC: Move Is to Support Healthy, Stable Development of Capital Market
  - [china] China Central Bank to Conduct Swap Facility Operations With Financial Institutions on Tuesday
  - [china] People's Bank of China: Swap Term Is One Year, Can Be Extended
  - [japan] Yen Falls After Japan Katayama's Intervention Warning
  - [china] China's central bank taps liquidity tool to fund share purchases
  - [taiwan] AI-Led Export Boom Likely to Continue Feeding Into Taiwan Domestic Demand — Market Talk
  - [korea] With President Lee Jae Myung's speech to the National Assembly on the 2nd, the 2027 budget political..
  - [korea] S. Korean won sharply weakens against US dollar
  - [taiwan] U.S. dollar closes sharply higher on Taipei forex market
  - [korea] Samsung Electronics and SK Hynix announced a policy to return shareholders based on their all-time p..
  - [china] China's manufacturing sector remains on front foot - RatingDog
  - [japan] Yen Falls Against Majors
  - [china] China Shifts Main Policy Rate to Overnight Reverse Repo Rate
  - [china] Xiaomi Diversifies Battery Supply Chain With Sunwoda Deal
  - [china] China's Central Bank Likely to Keep Policy Rate Unchanged Through 2027 — Market Talk
  - [china] CNOOC Limited Class A Stock 12‑Month Price Target Raised to CNY 42.52, Implies 18% Upside
  - [korea] “Domestic and export sales both slump”: Renault Korea Co., Ltd. sells 5,503 vehicles in October, down 23.6% ye
  - [taiwan] BenQ Materials targets premium displays and medical growth, seeks semiconductor materials breakthrough
  - [korea] South Korea urges cryptocurrency exchanges to tighten security
  - [china] Asian currencies mixed as yuan holds near four-year high, dollar steadies
  - [china] Asian stocks diverge following Wall Street tech sell-off; PBoC shifts policy anchor to overnight rate
  - [china] China’s Manufacturing Activity Returns to Contraction
  - [china] China’s shift to new policy rate signals easier funding conditions
  - [china] China’s soaring chemical exports threaten new trade war front
  - [korea] Kospi Snaps Two-Session Losing Streak; Chip, Energy Stocks Advance
  - [china] "Anchor exchange" comes into effect, the central bank launches 541 billion yuan overnight reverse repurchase o
  - [japan] Mitsubishi Corp Says It Will Sell Stake In LNG Canada Project To Blackstone Credit For About 250 Billion Yen
  - [japan] S&P Global Japan Manufacturing PMI slows to 7-month low of 53.3
  - [japan] BOJ flags progress in anchoring inflation around target
  - [korea] Finance minister discusses economic ties, cooperation with US ambassador
  - [korea] Household loans again rise in Oct. despite tightened rules, higher rates
  - [china] PBoC shifts primary policy anchor to overnight rate with daily 1.25% reverse repos
  - [china] The central bank’s interest rate regulation is facing major changes, and the asset pricing coordinates need to
  - [japan] Interest-Rate Hikes to Come in December, Highest Certainty in Japan — Market Talk
  - [japan] JGB yields edge up ahead of series of auctions
  - [japan] Macnica Holdings Inc - To Buy Back Up To 0.89% Of Own Shares Worth 5 Billion Yen

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
      "published_utc": "2026-11-02T10:02:46+00:00",
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

