atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-23T10:12:43.965329+00:00
Total: 3000 manchetes

  🇯🇵 Japão          991
  🇨🇳 China          840
  🇹🇼 Taiwan         375
  🇰🇷 Coreia do Sul  794

## O que já está no feed (não repita)

  - [china] HKEX launches AI and semiconductor indexes, licenses AI index in China
  - [korea] South Korea to amend forex law to regulate stablecoins as payment instruments: report
  - [china] China sells offshore yuan bonds in Hong Kong at record-low yields
  - [japan] Bank of Japan: Inflation likely to reach 2% inflation
  - [japan] Bank of Japan is likely to judge that the inflation rate will reach 2%; further interest rate hikes may be pos
  - [china] HKMA names Deutsche Bank offshore yuan primary liquidity provider
  - [japan] Citi expects USD/JPY to remain range-bound amid BoJ’s rate decision By Investing.com
  - [japan] Citi expects USD/JPY to remain range-bound amid BoJ’s rate decision
  - [taiwan] Taiwan industrial production up for 31st straight month in September
  - [china] The central bank will carry out 700 billion yuan MLF operation!
  - [china] Central Bank: 700 billion yuan MLF operation will be carried out on October 26
  - [china] China's Hisense Home Appliances nine-month revenue falls on forex impact
  - [korea] SK Hynix Pauses IPO of Memory-Chip Unit as AI Valuation Fears Mount— WSJ
  - [japan] Bank of Japan warns of risks from AI market shock, cyberattacks
  - [taiwan] Taiwan's inaugural semiconductor strike pauses as nearly 70% of Micron Taoyuan Union rejects new bonus offer
  - [china] China’s January-September fiscal revenue up 5.1% y/y
  - [taiwan] Taiwan Jobless Rate at 3.33% in September
  - [korea] Chip-Price Inflation Serves as Growth Driver for South Korea, Taiwan — Market Talk
  - [japan] Japan weighs phasing out gasoline subsidies from December as costs mount, officials say
  - [china] Hong Kong Monetary Authority designates 12 banks as primary liquidity providers for offshore yuan market
  - [japan] Japan's Nippon Life plans cuts to JGB holdings for 2nd straight year, will hang on to OATs
  - [japan] Euro set for weekly drop, yen eyes biggest gain since early September
  - [japan] Rising Wages Help Japanese Households Absorb Higher Rates, BOJ Says — Market Talk
  - [china] China Likely Exception to Hawkish Asian Central Banks View — Market Talk
  - [japan] BoJ Likely to Keep Policy Rate Unchanged Next Week — Market Talk
  - [japan] BOJ Sees Limited Risk to Japanese Companies From Oil Shock — Market Talk
  - [japan] Bank of Japan decides to reach 2% inflation target, postpones interest rate hike after 14 years, October meeti
  - [china] China Barely Eased Austerity Just Before Shift to Stimulus Mode
  - [japan] Consumption tax reduction bill begins substantive deliberation in the House of Representatives Finance and Fin
  - [japan] Japan futures slide as yen strengthens, logs weekly gain
  - [korea] BOK chief signals hawkish stance amid outlook for higher growth, rates
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Obtaining Shares in Subsidiaries
  - [korea] SK Hynix shares soar 4.4% after Solidigm IPO cancellation
  - [japan] Japan's Nikkei Falls, JGBs Soar as AI Jitters Spur Demand for Safe Assets
  - [korea] Kospi drops on AI funding worries, oil-driven inflation fears
  - [taiwan] Taiwan manufacturers' business sentiment hits 54-month high
  - [japan] Bank of Japan is likely to judge that the inflation rate will reach 2%, but may postpone further interest rate
  - [china] China's Chery expects overseas-manufactured vehicles to top 50% of exports, exec says
  - [japan] Foreign Minister Motegi holds U.S.-China-Russia summit meeting, communicates closely with U.S.
  - [japan] Fanuc Corp Says It Will Buy Back Up To 1.08% Of Own Shares Worth 500 Billion Yen

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
      "published_utc": "2026-10-23T10:12:44+00:00",
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

