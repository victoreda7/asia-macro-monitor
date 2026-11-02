atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-02T18:42:45.142941+00:00
Total: 3000 manchetes

  🇯🇵 Japão          919
  🇨🇳 China          857
  🇹🇼 Taiwan         362
  🇰🇷 Coreia do Sul  862

## O que já está no feed (não repita)

  - [korea] North Korea leans on China and Russia to drive 3% economic growth
  - [china] Walnut Capital Says China Lead Enters Block Trade Agreement For Sale Of Shares
  - [china] Central Bank to Conduct Third Swap Facility Operation
  - [china] Shanghai Iluvatar Corex Semiconductor Says Cumulative Chip Shipments Exceeded 80,000 Units For Ten Months
  - [china] China's exports of chemical products surge, U.S. think tank: May trigger new trade conflict | Cross-Strait
  - [china] ‘Queen of the Chinese’, drone war fears, cancer drug on sale: 7 US-China relations reads
  - [korea] North Korea's Lazarus Group has stolen $11.87 billion in crypto, equal to 45% of the country's GDP
  - [japan] Tokyo Electron Ltd. Stock 12‑Month Price Target Cut to JPY 15959.09, Implies 68% Upside
  - [taiwan] Taiwan's October manufacturing activity in expansion but momentum eases
  - [china] Update: Chinese central bank shifts policy rate anchor to overnight
  - [japan] Is the Bank of Japan's ``2% price increase'' target out of sync with how people feel about their daily lives?F
  - [japan] If gold breaks lower, investors may look at these safe haven currencies: analyst By Investing.com
  - [china] China's central bank launched policy tools on the 3rd to boost the stock market | Cross-Strait
  - [taiwan] Manufacturing solid but strain of energy costs, supply disruptions starts to show
  - [japan] The BOJ accidentally made $440 billion in stocks
  - [china] China’s CXMT defends push into new DRAM architecture as US chip curbs bite
  - [china] Economic Watch: Chinese central bank shifts policy rate anchor to overnight
  - [china] The main policy interest rate "changes anchor", why does the overnight reverse repurchase rate bear such a hea
  - [china] China unearths new critical mineral deposit, bolstering supply chain security
  - [taiwan] A major breakthrough! Japanese media revealed that Taiwan and Japan could sign a "comprehensive trade agreemen
  - [japan] SBI Holdings Inc - To Establish Merged Company With Capital Of 100 Million Yen Equally Split Between SBI Group
  - [taiwan] The New Taiwan dollar fell by more than 2 cents during the session. The central bank and exporters joined forc
  - [korea] South Korean president plans to expand fiscal spending in 2027 budget bill, perhaps due to declining approval 
  - [china] China's central bank taps liquidity tool to aid struggling stocks
  - [japan] Still-negative Japanese real rates should continue to support USD/JPY: UBS
  - [korea] Finance minister, Hyundai Motor chief discuss EV policies: sources
  - [china] ZAWYA: Ten projects signal broader Oman-China manufacturing ties
  - [china] The switching of major policy interest rates has started, and the People's Bank of China has launched a 541 bi
  - [japan] Yomiuri: Fujifilm Bets 10 Billion Yen on Magnetic Data Storage Resurgence
  - [china] Far East Smarter Energy's Units Win Bids, Sign Contracts Worth 1.5 Billion Yuan
  - [china] PBOC: 31 Securities, Fund Companies Have Applied for Quotas Exceeding CNY100B
  - [china] PBOC: Move Is to Support Healthy, Stable Development of Capital Market
  - [china] China Central Bank to Conduct Swap Facility Operations With Financial Institutions on Tuesday
  - [china] People's Bank of China: Swap Term Is One Year, Can Be Extended
  - [japan] Yen Falls After Japan Katayama's Intervention Warning
  - [china] China's central bank taps liquidity tool to fund share purchases
  - [china] Jiemian Evening News | The draft amendment to the Criminal Procedure Law is submitted for review; the central 
  - [taiwan] AI-Led Export Boom Likely to Continue Feeding Into Taiwan Domestic Demand — Market Talk
  - [korea] With President Lee Jae Myung's speech to the National Assembly on the 2nd, the 2027 budget political..
  - [korea] S. Korean won sharply weakens against US dollar

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
      "published_utc": "2026-11-02T18:42:45+00:00",
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

