atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-06T19:42:46.653584+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1285
  🇨🇳 China          778
  🇹🇼 Taiwan         256
  🇰🇷 Coreia do Sul  681

## O que já está no feed (não repita)

  - [korea] Samsung Biologics union seeks bargaining with Samsung Electronics
  - [taiwan] TSMC Stocks Drop as Musk Confirms Terafab Talks Without a Deal
  - [korea] South Korea exports eased Russia fuel crisis caused by drone strikes, Ukraine says
  - [taiwan] Taiwan's AUO, Innolux bet on glass as next-gen AI chip material
  - [japan] Bank of Japan member Sato favors continuing interest rate hikes without specifying timing, concerns about weak
  - [taiwan] Taiwan Semiconductor Price Target Raised to $665.00/Share From $650.00 by Barclays
  - [japan] "There are too many needs for semiconductors or GPUs"...Minister of Economy, Trade and Industry Akazawa says i
  - [japan] Japanese Yen Likely to Rise if Fed Lifts Rates Less Than Expected — Market Talk
  - [korea] NPS cuts Korean tech winners for insurers, defensive stocks as interest rates rise
  - [korea] Numeraire: Upbit opens KRW and USDT spot trading - 06 Oct 2026
  - [japan] Kawasaki Heavy to launch dog-shaped social robot by fiscal 2028
  - [japan] Finance Minister Katayama: ``This is not an election campaign'' according to some reports
  - [china] China turns on the export taps as LME zinc squeeze grinds on: Andy Home
  - [china] MORE U.S. AUGUST TRADE: CHINA DEFICIT UP TO $16.4 BILLION FROM $15.2 BILLION IN JULY
  - [korea] Roze AI Expands Disaster Prevention and Physical AI Business with Approximately US$12.2 Million (KRW 16.4 Bill
  - [korea] Roze AI Inc. (RZAI) Wins KRW 16.4B Disaster-Prevention Contracts in South Korea
  - [japan] JGB yield rises despite 30-year-high coupon
  - [japan] Yen market price decline; yen selling moves due to interest rate difference between Japan and the US
  - [japan] Bank of Japan Governor Ueda plans to continue raising interest rates while remaining cautious of upside risk t
  - [korea] Goldman sees Korean FX intervention risk if won strengthens sharply By Investing.com
  - [korea] Goldman sees Korean FX intervention risk if won strengthens sharply
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
      "published_utc": "2026-10-06T19:42:46+00:00",
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

