atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-19T08:22:43.250520+00:00
Total: 3000 manchetes

  🇯🇵 Japão          997
  🇨🇳 China          900
  🇹🇼 Taiwan         345
  🇰🇷 Coreia do Sul  758

## O que já está no feed (não repita)

  - [china] Economic growth picks up in China on robust export demand
  - [korea] Samsung, SK Hynix Slide Causes $137 Billion Hit to Korea Pension
  - [japan] Sell orders centered on semiconductor-related stocks with a decline in the Nikkei Stock Average
  - [taiwan] Foxconn To Acquire 50% Stake In Mitsubishi Electric Mobility For 115 Bln Yen
  - [china] Chip Investors, Watch Out: China’s CXMT Plunges Despite Record Forecast After Samsung’s Post-Outlook Slide
  - [china] China commerce ministry announces export controls for tunnel boring machines
  - [china] Volcano Engine Launches Seedance AI Drama Incentive Program, Offering Up to 200,000 Yuan per Series
  - [china] Iron ore rises as China's economic growth accelerates, steel output climbs
  - [japan] Japan PM says won’t rule out debt issuance to fund tax cut
  - [japan] Japan futures rise as tyre manufacturing resumes in China
  - [china] China stocks end higher as strong GDP outweighs AI jitters
  - [korea] SK Hynix’s potential Solidigm IPO reignites debate over multiple listings
  - [china] China commerce ministry announces new export control measures for drone-related items, dredgers
  - [korea] Key facts: Samsung accepts NVDA HBM terms; Banco Santander AI pact
  - [japan] Liberal Democratic Party Ishin leadership seeks cooperation from opposition parties to pass consumption tax re
  - [china] China GDP growth ticks up to 4.5% in Jul.-Sep. period
  - [korea] SK hynix launches W2tr financing program to bolster chip suppliers
  - [japan] Fiscal Concerns May Weigh on 20-Year JGB Auction Demand — Market Talk
  - [korea] S.Korea says SK Hynix’s Solidigm listing could violate rules- reports
  - [china] China Q3 GDP Growth Improves
  - [korea] Although Korea Western Power Co. has invested more than 630 billion won in safety-related budgets an..
  - [japan] Rice Prices Key to Japan Inflation Expectations — Market Talk
  - [japan] House of Councilors, Liberal Democratic Party, Ritsumeikan Committee on National Affairs meeting, discussion o
  - [korea] South Korean Won Extends Gains Near 2-Year High
  - [taiwan] Central bank mulls forex intervention after Taiwan dollar losses
  - [korea] SK Hynix bounces from extreme oversold-bear risk stays: Live levels
  - [japan] Nikkei 225 in strong downtrend at JPY 65,000: Live levels
  - [china] China’s CXMT shares slide despite ninefold revenue growth forecast
  - [japan] USD/JPY Seen Range-Bound Ahead of Central Bank Meetings — Market Talk
  - [japan] Japan Power Price at Four-Year High With Rising Coal, LNG Costs
  - [china] China Fangda Unit's IKK Fangda JV Signs 2.05 Bln Yuan Curtain Wall Works For Stadium In Saudi Arabia
  - [korea] The Bank of Korea is expected to freeze its base interest rate on the 22nd... Weighted at maintaining 3.00% pe
  - [korea] Morning Bid: Markets left to figure out sanctions
  - [china] China's GDP Growth Accelerates, but Underlying Momentum Remains Weak — Market Talk
  - [china] Asia FX ticks higher; yuan hits 4-yr high after China Q3 GDP beat
  - [china] China stocks inch higher as strong GDP offsets weak AI mood
  - [china] China's Economy Expanded 4.5% in Third Quarter, Powered by Exports — WSJ
  - [korea] Samsung Electronics, SK Hynix Slide as Korea Pension Fund Takes $137 Billion Hit
  - [korea] Samsung and SK Hynix stocks slide; is there a reversal in sight?
  - [korea] Bitcoin, Korea’s Kospi and Nasdaq Futures Rally as China GDP Beats Estimates

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
      "published_utc": "2026-10-19T08:22:43+00:00",
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

