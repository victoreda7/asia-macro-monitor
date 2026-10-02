atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-02T10:03:03.884136+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1292
  🇨🇳 China          783
  🇹🇼 Taiwan         246
  🇰🇷 Coreia do Sul  679

## O que já está no feed (não repita)

  - [japan] Japan finance minister: Government united in view reflation is over
  - [japan] Prime Minister Takaichi “plans to leave monetary policy to the Bank of Japan,” Finance Minister Satsuki Kataya
  - [japan] Consumption tax reduction bill approved at Liberal Democratic Party joint meeting, with calls for clarificatio
  - [japan] Dollar flat ahead of payrolls as yen firms, hot euro inflation keeps ECB in focus
  - [korea] European Chip Stocks Rally after Report Samsung Ups Prices — Market Talk
  - [china] SK Innovation, Aramco-backed S-Oil rally as China export bans add to global fuel strain
  - [china] China fuel export suspension to choke supplies in Asia
  - [japan] BREAKING NEWS: Japan farm minister admits making "misleading" remarks on local budget cut
  - [korea] Art Group Buys 6.87% Equity Interests In Edgeon For Krw 585.75 Million
  - [china] China's Mortgage Subsidy Likely to Have Limited Impact — Market Talk
  - [japan] Collateral Accepted by the Bank of Japan (End of Sept.)
  - [japan] Japanese Government Bonds Held by the Bank of Japan
  - [korea] Ministry of Finance and Economy ◇Promotion of Deputy Director △Public relations Officer Kim Young-h..
  - [korea] SK hynix Inc. Stock 12‑Month Price Target Cut to KRW 3287582.16, Implies 79% Upside
  - [korea] Samsung Electronics' large-scale share buyback has entered the final stage. The event, which has sup..
  - [china] In Focus | How US sanctions forced Xinjiang’s cotton industry to build a survival model
  - [korea] South Korea’s Sept inflation cools to 2.9% on fuel caps, lower farm prices
  - [china] Everest Medicines Announces the Acceptance and Priority Review of VELSIPITY(R) Manufacturing Localization Appl
  - [japan] Why did National Democratic Party representative Tamaki suddenly distance himself from the government? The tru
  - [japan] Minister of Administrative Reform Nakajima Autumn Review “Keeping in mind the creation of financial resources 
  - [japan] Chief Cabinet Secretary Kihara informs governor of financial support for Kumamoto earthquake recovery fund
  - [china] China Chip Smuggling Cases Expose Nvidia’s Blind Spots
  - [china] Atlas Copco Buys Chinese Heating and Cooling Equipment Manufacturer Guangdong Euroklimat
  - [japan] House of Representatives Opposition Diet Committee Chairman and others call for careful deliberation of consum
  - [china] China's Policy Stimulus Package Still Positive Step Despite Limited Scale — Market Talk
  - [japan] Inflation increases in Tokyo's 23 wards by more than 2% for the first time in 8 months (ABEMA TIMES)
  - [japan] Long-term JGB yields rise toward multi-decade highs as inflation signs mount
  - [japan] Hankyu Hanshin Holdings, Inc. - To Expand The Limit For Its Share Buybacks Up To 5.16% Worth 50 Billion Yen Fr
  - [korea] South Korea's Strong Chip Exports Yet to Spill Over Into Broader Economy — Market Talk
  - [japan] Japan Stocks Look Attractive, Especially When Dollar-Yen Above 152 — Market Talk
  - [japan] Retail JGB sales surge more than 80% as rates rise
  - [japan] September consumer price index for Tokyo's 23 wards increased by 2.7% compared to the same month last year
  - [korea] South Korean Won Steady on Export Growth
  - [japan] Japan's unemployment rate rises to 2.5% in August, above expectations
  - [china] More aggressive China stimulus unlikely for now, BofA says
  - [japan] <Clearly emerging trends> In the past five years, when inflation has rapidly increased, what and how have hous
  - [japan] Japanese yen firms on strong inflation, dollar muted before payrolls test
  - [taiwan] TSMC reportedly weighs Texas expansion, but key US tax incentive could decide the move as Singapore enters the
  - [japan] Tokyo inflation accelerates in Sept, strengthening case for further BOJ hikes By Investing.com
  - [japan] Japan does not need excessively loose monetary policy, economy minister says

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
      "published_utc": "2026-10-02T10:03:04+00:00",
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

