atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-03T14:52:46.576526+00:00
Total: 2816 manchetes

  🇯🇵 Japão          814
  🇨🇳 China          833
  🇹🇼 Taiwan         302
  🇰🇷 Coreia do Sul  867

## O que já está no feed (não repita)

  - [china] Global central banks purchased gold at the fastest pace in 2 years in the third quarter, China topped the list
  - [korea] Samsung to make chip parts for AMD, Nvidia at Texas plant: report
  - [china] Raising the foreign exchange deposit reserve ratio, why did the central bank take action to stabilize the exch
  - [korea] SK hynix Secures Board Nomination Rights at Penguin Solutions with 9.1% Stake
  - [china] Dollar drifts on Mideast, midterm risks; Aussie and yuan dip
  - [china] China's steady thermal coal imports mask supply shifts amid El Nino: Russell
  - [china] The central bank will raise the foreign exchange deposit reserve ratio of financial institutions. What signal 
  - [china] After raising the foreign exchange deposit reserve ratio, why did the central bank take action to stabilize th
  - [korea] AMD, Nvidia Could Join Tesla On Samsung’s Texas Chip Plant Customer List: Report
  - [japan] What midterms might mean for the yen
  - [china] The People's Bank of China decides to raise the foreign exchange deposit reserve ratio of financial institutio
  - [china] China, Oman sign currency swap agreement
  - [china] Sales of Tesla electric vehicles made in China increase 10.3% in October year-on-year
  - [korea] Samsung will manufacture chip components from AMD and Nvidia at its second factory in Texas, according to a re
  - [korea] Samsung to make AMD, Nvidia chip parts at second Texas plant, Maeil Business reports
  - [china] Zhejiang Construction Investment Group Says Unit's Consortium Wins 1.5 Billion Yuan Bid
  - [china] First time in nearly five years! The central bank raised the foreign exchange deposit reserve ratio, and the o
  - [korea] HYBE Q3 2026 slides: record revenue hits KRW 1.5 trillion on BTS tour
  - [china] China-made Tesla electric vehicle sales rose 10.3% year-on-year in October
  - [china] Central Bank: Net investment in open market government bond sales in October was 150 billion yuan
  - [korea] NPS sacks real estate head, stalling $900 mn in 2026 fund commitments
  - [taiwan] Foxconn's EV strategy opens new export routes for Taiwan
  - [korea] Korean beauty exports extend growth streak despite strong won
  - [korea] D&D Pharmatech is pushing for technology export of "DD01," a treatment for hepatitis (MASH) rela..
  - [taiwan] TSMC Has Raised T$14.8 Billion Via Unsecured Bonds
  - [china] NVDA Shares Inch Higher Overnight After 4-Day Rout: Chipmaker Reportedly Tells Cloud Clients To Limit China Ex
  - [china] China XD Electric's Units Win 1.1 Billion Yuan Bids For State Grid Projects
  - [china] ZAWYA: Egypt explores solar cell manufacturing plant with China’s Boomy to boost local production
  - [china] Offshore Yuan Weakens After PBOC Moves to Cool Currency Rally
  - [korea] Kim, a representative K-food player, surpassed KRW 1 trillion in production for the first time in Gw..
  - [korea] The contract for rare obesity treatment, which LG Chem exported technology to U.S. bio companies, ha..
  - [taiwan] Student skygazer in Taoyuan captures rare images of red sprites
  - [taiwan] U.S. dollar closes sharply higher on Taipei forex market
  - [china] China to Raise Forex Deposit Reserve Requirement to Curb Yuan’s Rally
  - [china] Key facts: NVIDIA China Rule; Melius Cuts Target; U.S. Chip Curbs
  - [korea] The base interest rate has risen... NIM of the four major banks falls simultaneously
  - [china] PBOC Move Likely Aimed at Slowing Down, Not Reversing, Yuan's Appreciation — Market Talk
  - [china] Iron ore dips on higher shipments, sluggish China demand
  - [china] Asian currencies mixed as Aussie falls after RBA hike, yuan weakens
  - [china] Thailand to raise tax on imported EVs to 35% as Chinese brands gain ground

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
      "published_utc": "2026-11-03T14:52:46+00:00",
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

