atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-27T07:32:47.927555+00:00
Total: 3000 manchetes

  🇯🇵 Japão          949
  🇨🇳 China          976
  🇹🇼 Taiwan         331
  🇰🇷 Coreia do Sul  744

## O que já está no feed (não repita)

  - [china] China's State Council appoints, removes officials
  - [china] New U.S. Tariffs Unlikely to Derail U.S.-China Economic Relations — Market Talk
  - [japan] School bullying in Japan hit record high in fiscal 2025
  - [korea] Huawei, Kioxia challenge Samsung, SK hynix’s HBM dominance
  - [china] China’s factory slump likely extends to November despite solid exports
  - [japan] Stock price rises due to buyback of AI/semiconductor related stocks, price rises by more than 1,200 yen
  - [china] Analysis-Trump’s new tariffs aim to prise global trade from China’s grip
  - [japan] Bank of Japan Warns Stablecoins and Tokenization Threaten Financial Stability
  - [china] China stocks, yuan rally after Beijing vows stronger market support
  - [china] Nvidia, neoclouds in focus as chip sellers rule out Chinese renters
  - [japan] USDJPY: Dollar Holds Above ¥159 as Tokyo Inflation Keeps BOJ Hike in Play
  - [china] China Industrial Profits Log Robust Growth
  - [china] China to strengthen defense against imported risks in capital markets
  - [japan] Today's Oha Biz 11/27 Bank of Japan councilor moves policy interest rate to “neutral level”
  - [korea] Sebo Manufacturing Engineering Construction Wins 72.4 Billion Won Order
  - [japan] Tokyo Core Inflation Strongest Since Mid 2025
  - [korea] Decision to Impose Anti-Dumping Duties on Bisphenol A Originating in the Republic of Korea and the Separate Cu
  - [japan] Former Bank of Japan Governor Haruhiko Kuroda hopes for skill in central bank coordination between Japan, the 
  - [china] Asian stocks jump on U.S. futures rally, China profit beats, shrugging off tariff risks
  - [china] 1st LD: Chinese premier chairs State Council executive meeting
  - [china] Chinese premier chairs State Council executive meeting
  - [korea] Korea’s future fund must not come at the cost of fiscal discipline
  - [korea] South Korea November exports seen posting fastest growth in over 50 years on AI chip surge: Reuters poll
  - [china] Commentary: Brazil’s Lesson for China — GDP Isn’t Everything
  - [japan] (BOJ Review) Developments in JGB Market-Making Business by Securities Companies
  - [china] China's industrial profits surge 20.1% in October as ten-month growth accelerates to 16%
  - [china] Emdoor Says To Buy Digital Solutions Firm For 715 Mln Yuan
  - [china] Neoclouds Told To Choose: Nvidia Chips Or Chinese Customers
  - [china] Yuan eases on tariff fears despite four-year fixing high
  - [japan] Japan Core Inflation Expected to Hover Near 2% in Early FY2027 — Market Talk
  - [japan] Japan Core Inflation Likely at 2.6% in November, Barclays Says — Market Talk
  - [japan] Consumer price index for Tokyo's 23 wards rose 2.9% in November, exceeding 2% for 3 consecutive months (TV Asa
  - [japan] Result of Liquidity Enhancement Auction on November 27, 2026(For JGB Market Special Participants)
  - [japan] Finance Minister Katayama plans to focus the supplementary budget on necessary measures
  - [china] The central bank's reverse repurchase operation net withdrawn 45.5 billion! Dividend low-volatility ETF Huatai
  - [korea] Korean Won Poised to Strengthen Against Dollar in 2027 — Market Talk
  - [japan] Consumer price index for November in Tokyo's 23 wards increased by 2.9% compared to the same month last year
  - [china] China warns of retaliation after Trump administration proposes new tariffs alleging overcapacity
  - [china] China warns of retaliation after Trump administration proposes new tariffs over overcapacity
  - [japan] Tokyo Core CPI Rises to 2.9% YoY; December BoJ Rate Hike Expected

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
      "published_utc": "2026-11-27T07:32:48+00:00",
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

