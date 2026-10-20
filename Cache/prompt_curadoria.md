atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-20T06:12:43.376779+00:00
Total: 3000 manchetes

  🇯🇵 Japão          994
  🇨🇳 China          901
  🇹🇼 Taiwan         356
  🇰🇷 Coreia do Sul  749

## O que já está no feed (não repita)

  - [japan] Analysis-As Japan pursues a chip-industry reboot, it’s being pressed to build America’s
  - [japan] Bank of Japan may raise inflation forecast, stand pat on rates, sources say
  - [japan] Bank of Japan may raise price outlook for FY2027, policy interest rate likely to remain unchanged = source (Re
  - [korea] Hyundai Motor Group unites defense arms in global export push
  - [japan] ABB To Acquire 51% Stake In Mitsubishi Electric Joint Venture For JPY 82.4 Bln
  - [korea] SK Hynix Shares Appear Undervalued Amid AI Financing Concerns — Market Talk
  - [korea] 93% of bond market workers say, “The Bank of Korea Monetary Policy Committee will freeze the base interest rat
  - [korea] BYD surges to No. 4 in Korea's imported car market
  - [china] No more than 1 trillion per day! The central bank will carry out overnight reverse repos for nine consecutive 
  - [china] Asian currencies firm as dollar retreats; yuan hits four-year high
  - [china] The central bank will carry out overnight reverse repurchase operations for 9 consecutive working days, with a
  - [china] The central bank will launch overnight reverse repos with a daily limit of 1 trillion from tomorrow
  - [china] Chinese Consumption Likely Still Faces Challenges — Market Talk
  - [korea] The Jeonnam Gwangju Semiconductor Forum held its first board meeting and launched activities to crea..
  - [taiwan] TSMC plans 3nm semiconductor manufacturing at second Japan factory, investment to exceed USD 23 billion
  - [china] For 9 consecutive working days, the central bank has made major moves! No more than 1 trillion yuan per day
  - [china] China and Hong Kong shares weaken as stable growth eases stimulus bets
  - [china] The central bank’s latest announcement: It will carry out overnight reverse repurchase operations for 9 consec
  - [japan] JAPAN consumption tax cut bill on food goes to Lower House
  - [japan] Bill related to consumption tax reduction on food items to be debated in the House of Representatives this aft
  - [korea] Samgi America, the North American subsidiary of Samgi Energy Solutions, has won a contract to supply..
  - [china] Yuan hits fresh high since 2022 on export growth, stronger guidance
  - [china] The central bank has pushed a daily cap of 1 trillion yuan for overnight reverse repos and plans to gradually 
  - [china] The central bank has pushed a daily cap of 1 trillion yuan for overnight reverse repurchases and plans to grad
  - [korea] Asia stocks slump as AI jitters hammer Korean chipmakers ahead of tech earnings
  - [china] China's fuel oil exports for bunkering rebound in September while imports ease
  - [china] The daily operation volume does not exceed 1 trillion! The central bank will carry out overnight reverse repur
  - [japan] Is the sudden rise in interest rates in France only due to special factors? The sudden sell-off of government 
  - [japan] Citizens Submit a counterproposal to the consumption tax reduction bill, aiming to reduce the burden through r
  - [japan] Yen Weakens Despite Hawkish Ueda Remarks
  - [china] Central Bank: Conduct overnight reverse repurchase operations from October 21 to November 2, with a daily limi
  - [korea] Finance minister pledges support for global 'AI basic society'
  - [china] Offshore Yuan Extends Gains to Over 4-Year High
  - [taiwan] Taiwan industry seeks nuclear restart and utility relief amid energy costs boom
  - [japan] Japan's Nikkei falls as higher yields, inflation fears weigh
  - [china] China Likely on Track to Hit Annual Growth Target — Market Talk
  - [japan] Japan futures rise as rains squeeze Thai supply, yen slips
  - [taiwan] Taiwan dollar weakens most among muted Asian currencies
  - [korea] Samsung Electronics and SK Hynix, which had risen by recovering some of the recent declines the prev..
  - [china] China's September US soybean imports rebound from zero a year earlier, data shows

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
      "published_utc": "2026-10-20T06:12:43+00:00",
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

