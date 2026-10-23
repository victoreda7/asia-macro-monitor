atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-23T16:32:42.801904+00:00
Total: 3000 manchetes

  🇯🇵 Japão          984
  🇨🇳 China          848
  🇹🇼 Taiwan         375
  🇰🇷 Coreia do Sul  793

## O que já está no feed (não repita)

  - [korea] Micron, Sandisk gain as SK Hynix scraps Solidigm IPO, LYNX says
  - [japan] Japan weighs rebranding energy, AI as defense spending under Trump pressure
  - [korea] SK Hynix and Samsung likely to boost shareholder returns as demand stays strong: BofA
  - [china] China's MiniMax completes export registration for open-source, overseas AI model licensing
  - [korea] Woori Financial Group : Earnings topped KRW 1 trillion as stronger fees and lower credit costs supported retur
  - [china] China issues guidelines to promote employment amid AI advances
  - [korea] Apro: AT begins KRW spot trading on Bithumb - 23 Oct 2026
  - [korea] SK Hynix Just Sent Another Warning Signal to the AI Trade — Barrons.com
  - [china] BGI Genomics Q3 Net Profit At 2.9 Million Yuan
  - [japan] German Chancellor Merz will visit Japan next week to hold a summit meeting with Prime Minister Takaichi
  - [china] The central bank launches 700 billion yuan 1-year MLF operation
  - [china] Hang Zhou Iron & Steel Q3 Net Loss At 108.7 Million Yuan
  - [japan] Japan-Micronesia summit meeting confirms further strengthening of bilateral relations
  - [china] The central bank launched a 700 billion yuan medium-term lending facility (MLF) operation on October 26_Compan
  - [korea] Micron pivots from 4F² to 3D DRAM, differing from rivals Samsung, SK Hynix: Wedbush
  - [china] The central bank takes action! The 700 billion yuan MLF operation is coming
  - [korea] What's Going On With SK Hynix Stock Friday
  - [china] The People's Bank of China will launch a 700 billion yuan MLF operation
  - [korea] SK Hynix’s Solidigm Nasdaq IPO plans derailed by shareholder backlash, state scrutiny of dual listings; Shares
  - [japan] Bank of Japan's monetary policy meeting next week: Underlying inflation expected to reach 2%; interest rate hi
  - [china] Wuhan Tianyuan Group's Consortium Wins 3.6 Billion Yuan Bid For Project
  - [china] The central bank announced that it will carry out 700 billion yuan MLF operations
  - [japan] Euro set for weekly drop against dollar, yen as France concerns resurface
  - [china] Could Europe’s cost-of-living protests sharpen EU-China trade tensions?
  - [japan] September consumer prices +2.1% compared to the same month last year, the first time in nine months that the i
  - [taiwan] Taiwan's September jobless rate drops to 3.36%, lowest in 26 years
  - [china] Wingtech Says Q3 Net Loss At 216.6 Million Yuan
  - [korea] SK Hynix Scraps U.S. IPO of Memory-Chip Unit. Why the Stock Is Jumping. — Barrons.com
  - [china] Ziyuanyuan Holdings' Unit Enters Cooperation Framework Agreement With Shenzhen Shenshu
  - [china] The central bank will launch an MLF operation of 700 billion yuan on October 26, with a reduction of 200 billi
  - [korea] SK Hynix puts US IPO of chip unit Solidigm on hold after Seoul authorities raise concerns
  - [japan] Yen rallies, euro sags, dollar shrugs as AI worries drive haven bid
  - [china] HKEX launches AI and semiconductor indexes, licenses AI index in China
  - [korea] South Korea to amend forex law to regulate stablecoins as payment instruments: report
  - [china] Charts of the Day: Solar Exports Surge in September
  - [china] China sells offshore yuan bonds in Hong Kong at record-low yields
  - [china] EU Looks Beyond Cars for Next Round of China Trade Talks
  - [japan] Citi expects USD/JPY to remain range-bound amid BoJ’s rate decision By Investing.com
  - [japan] Bank of Japan: Inflation likely to reach 2% inflation
  - [japan] Bank of Japan is likely to judge that the inflation rate will reach 2%; further interest rate hikes may be pos

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
      "published_utc": "2026-10-23T16:32:42+00:00",
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

