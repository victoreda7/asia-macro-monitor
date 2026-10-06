atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-06T10:32:45.361295+00:00
Total: 2990 manchetes

  🇯🇵 Japão          1283
  🇨🇳 China          775
  🇹🇼 Taiwan         254
  🇰🇷 Coreia do Sul  678

## O que já está no feed (não repita)

  - [japan] Yomiuri: Japan's House Foods Group to Absorb Subsidiaries in Restructuring Gambit
  - [japan] Bank of Japan Governor Ueda warns against upward trend in prices: ``Stability at 2% is more important'' (Asahi
  - [japan] Japan's Sumitomo Mitsui DS Asset swaps some French bonds for German, yen debt
  - [taiwan] TSMC Texas-Terafab buzz drives Taiwan contractors to move fast
  - [taiwan] TSMC evaluates potential Texas investment, sources say
  - [korea] Ministry of Planning and Budget ◇ Promotion of Deputy Director △ Director of Budget Park Jung-min
  - [korea] Amid growing fiscal instability in Europe, including Spain and France, the Korean national debt situ..
  - [japan] Bank of Japan Governor Ueda ``adjusts the degree of monetary easing'' and continues to raise interest rates Gr
  - [korea] Hanmi Semiconductor has won a 24.5 billion won order for semiconductor post-processing equipment fro..
  - [japan] Interest rates on 10-year government bonds rise to 3.1%, the highest level in about 30 years Ministry of Finan
  - [korea] First Vice Minister of Finance and Economy Kwon Dae-young apologized for increasing investor losses
  - [korea] Samsung Electronics is expected to open the era of "quarter operating profit of KRW 100 trillion" fo..
  - [japan] Japan should significantly expand JGB sales to retail investors, lawmaker says
  - [china] Chinese LCD panel makers tighten supply to lift prices — Taiwan suppliers eye order shifts
  - [taiwan] AMD CEO Lisa Su sees 'very high' chip demand continuing for years, praises TSMC expansion
  - [japan] JGB yield rises despite 30-year-high coupon as rates add to fiscal fears
  - [china] China's GDP Growth Likely Edged Up to 4.5% in 3Q, Citi Says — Market Talk
  - [japan] Underlying inflation stabilizes at around 2% target, ``more important'' Bank of Japan Governor Ueda (Jiji Pres
  - [japan] AI Inflation Impact on Japan CPI Likely Limited — Market Talk
  - [japan] BOJ chief calls for more focus on anchoring inflation around target
  - [japan] Asian currencies rangebound as dollar, euro hold near multi-month extremes
  - [taiwan] Taiwan's September Exports Likely Rose 46.5%, WSJ Poll Shows — Market Talk
  - [japan] 10-year government bond interest rate set at 3.1% per year
  - [japan] Liberal Democratic Party/Ishin “Efforts to pass food consumption tax reduction bill in the current Diet sessio
  - [japan] TV personality Dewi ordered to pay 200,000 yen fine over assaults
  - [korea] Samsung Biologics union seeks bargaining with Samsung Electronics
  - [taiwan] TSMC tops global FDI ranking as AI infrastructure redraws overseas investment
  - [japan] Japan's Nikkei climbs 1% on dip in crude oil, smooth JGB auction
  - [taiwan] AMD to expand Taiwan supply chain investment as chip demand grows: Lisa Su
  - [japan] BREAKING NEWS: BOJ to raise rates as needed to stabilize inflation: governor
  - [korea] Kospi Snaps Two-Session Winning Streak; Defense, Chip Stocks Retreat
  - [japan] BOJ Ueda says financial conditions remain loose
  - [korea] The amount of finance supported by the Export-Import Bank of Korea to smoothly secure "seven key min..
  - [japan] Japan's Iwatani, Cosmo to develop hydrogen supply chain at Chiba refinery
  - [china] China turns on the export taps as LME zinc squeeze grinds on: Andy Home
  - [japan] Prime Minister Takaichi asks US President Trump to approach Japan-North Korea summit meeting
  - [korea] Samsung Biologics union seeks direct talks with Samsung Electronics
  - [korea] Vice Minister of Finance and Economy Kwon Dae-young said on the 6th that the Financial Services Comm..
  - [japan] 10-year JGB coupon hits 30-year high as rising rates add to fiscal fears
  - [japan] Food consumption tax reduction bill approved by the Liberal Democratic Party's Board of Governors and to be su

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
      "published_utc": "2026-10-06T10:32:45+00:00",
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

