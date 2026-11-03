atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-03T09:12:43.573448+00:00
Total: 3000 manchetes

  🇯🇵 Japão          897
  🇨🇳 China          874
  🇹🇼 Taiwan         358
  🇰🇷 Coreia do Sul  871

## O que já está no feed (não repita)

  - [korea] D&D Pharmatech is pushing for technology export of "DD01," a treatment for hepatitis (MASH) rela..
  - [taiwan] TSMC Has Raised T$14.8 Billion Via Unsecured Bonds
  - [china] NVDA Shares Inch Higher Overnight After 4-Day Rout: Chipmaker Reportedly Tells Cloud Clients To Limit China Ex
  - [china] China XD Electric's Units Win 1.1 Billion Yuan Bids For State Grid Projects
  - [china] ZAWYA: Egypt explores solar cell manufacturing plant with China’s Boomy to boost local production
  - [china] Offshore Yuan Weakens After PBOC Moves to Cool Currency Rally
  - [korea] Kim, a representative K-food player, surpassed KRW 1 trillion in production for the first time in Gw..
  - [korea] The contract for rare obesity treatment, which LG Chem exported technology to U.S. bio companies, ha..
  - [china] China to Raise Forex Deposit Reserve Requirement to Curb Yuan’s Rally
  - [china] Key facts: NVIDIA China Rule; Melius Cuts Target; U.S. Chip Curbs
  - [china] PBOC Move Likely Aimed at Slowing Down, Not Reversing, Yuan's Appreciation — Market Talk
  - [china] Iron ore dips on higher shipments, sluggish China demand
  - [china] Asian currencies mixed as Aussie falls after RBA hike, yuan weakens
  - [china] Thailand to raise tax on imported EVs to 35% as Chinese brands gain ground
  - [china] The People's Bank of China decides to raise the foreign exchange deposit reserve ratio for financial instituti
  - [china] The war in the Middle East pushed up inflation and the Australian central bank raised interest rates by 1 poin
  - [korea] Korea Aerospace Industries: Export-led orders surged as revenue grew, but net income declined and KF-21 delive
  - [china] China's State Council removes Winnie Ho from HKSAR gov't post
  - [korea] Kospi Falls as Energy, Shipping, Chip Stocks Retreat
  - [china] The central bank stabilizes the exchange rate and then takes action to raise the foreign exchange deposit rese
  - [korea] Dawon Nexview To Acquire Real Estate Worth 17 Billion Won
  - [japan] Parkway Life Real Estate Investment Trust: Singapore rent growth lifted distributions as Japan FX pressure off
  - [china] Yuan Weakens as PBOC Signals Discomfort With Rapid Gains
  - [korea] Hanwha brings Korean defense, manufacturing ETFs to Abu Dhabi
  - [korea] Korea Inflation Could Gradually Return to BOK's Target Through 2027 — Market Talk
  - [china] China's steady thermal coal imports mask supply shifts amid El Nino: Russell
  - [china] The central bank decided to raise the foreign exchange deposit reserve ratio!
  - [china] The central bank raised the foreign exchange deposit reserve ratio for the first time in the past five years, 
  - [korea] US midterm elections·Household loan variables... Bank of Korea, final weighing of interest rate hike
  - [korea] Asia Paper Manufacturing Co Ltd To Cancel 7.4 Billion Won Worth Of Own Shares
  - [china] Chinese stocks drop as policy measures disappoint, but yuan rally halted
  - [china] The central bank steps to ease the pressure on RMB appreciation and raises the foreign exchange deposit reserv
  - [korea] SK Hynix tests SMA(50) cloud resistance after Double Bottom: Live
  - [korea] The Bank of Korea said, “Inflation in November is also in the upper 2% range”… Will there be a further increas
  - [china] China's central bank conducts 100 billion yuan of swap operations
  - [china] China Talks Up Market Openness While Steering Stocks and Yuan
  - [china] Why is the Chinese Yuan falling today?
  - [taiwan] TSMC's next US chip plant could land in Sherman
  - [korea] South Korean Won Recovers as Oil Prices Retreat
  - [china] Asian currencies mixed as yuan slides after PBOC move, won rebounds

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
      "published_utc": "2026-11-03T09:12:43+00:00",
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

