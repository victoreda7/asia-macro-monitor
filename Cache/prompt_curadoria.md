atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-22T03:12:44.472464+00:00
Total: 3000 manchetes

  🇯🇵 Japão          974
  🇨🇳 China          858
  🇹🇼 Taiwan         357
  🇰🇷 Coreia do Sul  811

## O que já está no feed (não repita)

  - [korea] BOK Gov: Stronger Won Helps Curb Import Prices, Boost Household Purchasing Power
  - [korea] BOK Gov: Core Inflation Could Near 2% Target in 2028
  - [china] The central bank's 7-day reverse repurchase operation volume was zero on October 22, and it carried out 173 bi
  - [korea] (URGENT) Investment-focused fiscal spending compatible with monetary tightening: BOK Gov. Shin
  - [korea] BOK Gov: Preemptive Move in August Gives Policymakers More Room to Maneuver
  - [korea] BOK Gov: Timing of Further Rate Increases Will Depend on Assessment of Incoming Data
  - [korea] Samsung E&A recorded an operating profit of KRW 5006 billion in the third quarter of this year.
  - [korea] Bank of Korea Gov: Will Maintain Tight Policy Stance Until Inflation Converges Toward Target
  - [korea] (URGENT) Strengthening won likely helps boost consumption in S. Korea: BOK Gov. Shin
  - [china] China buys nearly 1 million tons of Australian canola for 2027 shipment, traders say
  - [korea] Bank of Korea base interest rate frozen at 3.00% per annum... Speed ​​adjustment after 2 consecutive raises
  - [japan] Japan's Nikkei slips as chip stocks come under pressure due to wariness over AI investment
  - [japan] Japan's Nikkei slips as chip shares pressured by AI capex caution
  - [korea] Bank of Korea holds rates, upbeat outlook points to future hikes
  - [korea] Bank of Korea freezes base interest rate at 3.0% per annum... Will it be raised in November after taking a bre
  - [korea] South Korean won strengthens most among Asian currencies
  - [korea] BOK holds rate at 3%, leaves door open to November hike
  - [korea] [Full text] Bank of Korea Monetary Policy Committee October monetary policy direction
  - [korea] [Full text] Bank of Korea Monetary Policy Committee October monetary policy direction decision statement
  - [japan] Japan's strong-armed $21 bln chip bet is low risk
  - [korea] The Bank of Korea has stopped raising interest rates... Base interest rate frozen at 3% (comprehensive) - Mone
  - [korea] Bank of Korea freezes base interest rate at 3.00% per annum [Newsis Pic]
  - [korea] ‘Stop continuous increases and check the effect of austerity’... Bank of Korea freezes base interest rate at 3
  - [korea] BOK: Headline, Core Inflation Expected to Exceed August Forecasts Next Year
  - [korea] BOK: Headline, Core Inflation Expected to Match August Forecasts This Year
  - [korea] South Korean shares fall on profit taking; BOK in focus
  - [korea] BOK: 2026, 2027 Economic Growth Expected to Be Well Above August Forecasts
  - [korea] Bank of Korea: Decision to Hold Rates Steady Was Unanimous
  - [china] The central bank launched a 173 billion yuan overnight reverse repurchase operation
  - [china] CHINA PBOC CONDUCTS CNY173 BLN VIA O/N REVERSE REPO THURS
  - [korea] Full text of BOK statement on monetary policy decision in Oct.
  - [china] The central bank launched continuous overnight reverse repurchase operations, with an operation volume of 80 b
  - [korea] Bank of Korea freezes base interest rate at ‘3.00%’
  - [korea] Merck opens Korean chip materials plant to meet advanced memory demand
  - [taiwan] Taiwan's first-ever chip workers strike begins at Micron plant
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7195 THURS VS 6.7192
  - [korea] Bank of Korea freezes base interest rate at 3.00% per annum...adjusts pace of tightening
  - [japan] Japan MOF To Auction Y2.8T Of 2-Year Govt Bonds Oct 29
  - [korea] The Bank of Korea freezes the base interest rate at 3% per annum... ‘Taking a breather’ after two consecutive 
  - [korea] Bank of Korea holds rates at 3% after back-to-back hikes

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
      "published_utc": "2026-10-22T03:12:44+00:00",
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

