atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-25T19:12:43.315286+00:00
Total: 3000 manchetes

  🇯🇵 Japão          986
  🇨🇳 China          856
  🇹🇼 Taiwan         375
  🇰🇷 Coreia do Sul  783

## O que já está no feed (não repita)

  - [japan] Japan Week Ahead: BOJ Set to Leave Rate at 1.25% as Mission Shifts from Normalizing Super-Low Rates to Keeping
  - [korea] Osong beauty expo draws nearly $100m in export deals
  - [korea] AI money shifts from chips to software, exposing Korea’s lack of alternatives
  - [japan] [Breaking news] Fukushima prefecture gubernatorial election exit poll results
  - [china] China’s export controls around PV cells could slow India’s upstream solar push
  - [china] Govt needs to incentivise domestic solar production as China eyes curbs on tech exports: Solex Chairman
  - [japan] Fukushima prefecture gubernatorial election vote counting and exit poll election information is here [Breaking
  - [china] The Egyptian pound continues to depreciate and reaches a record low. The president of the Egyptian Central Ban
  - [china] Daan Gene Q3 Net Loss At 19.7 Million Yuan
  - [china] Hengyi Petrochemical Says Q3 Net Profit At 2.1 Billion Yuan
  - [china] DeepSeek and others complete overseas export registration amid China’s AI export controls | Cross-Strait
  - [china] China's fifth plenum, Jio listing on Indian bourses, BOJ meeting
  - [korea] Osong beauty expo draws nearly US$100 mln in export deals
  - [korea] Why Kospi and Korean won have parted ways
  - [china] China’s tech giants are paying 1 million yuan for a new kind of AI engineer
  - [japan] ``Japan's first full-fledged suburban luxury residential area'' ``Eiichi Shibusawa is also involved in the dev
  - [japan] "A garden city before Denenchofu" and "favored by the elites of the Taisho era"...The background of the "hidde
  - [japan] Will the October FOMC leave interest rates unchanged? Focus
  - [japan] Chairman of the ruling and opposition party committees discuss consumption tax reduction bill NHK Sunday debat
  - [korea] SK Hynix, a Korean semiconductor company that has transformed from the verge of selling itself, ignites demand
  - [korea] S. Korea's Q2 current account surplus ranks 2nd on robust chip exports
  - [korea] Samsung's Exynos 2700 outscores Qualcomm's top chip by nearly 20%
  - [china] Despite a large surplus in health insurance finances for foreign members, ``Chinese nationals are once again i
  - [japan] Fiscal soundness begins with "procedures" - Institutionalization of independent verification indicated by the 
  - [china] Sri Lanka’s property boom gives Chinese developers hope. But old risks linger
  - [taiwan] Magnate Technology sees aerospace, semiconductor growth opportunities
  - [japan] Amazing Venture [17] LENZO / Taking on the challenge of next-generation AI semiconductors from Japan | Busines
  - [japan] Amazing Venture [19] EmotionX/Secret Computing Semiconductor & Cloud | Business | Toyo Keizai Online
  - [china] China Hits Back at US Proposal to Tighten Investment Limits
  - [taiwan] Lin urges Taiwan-Europe cooperation on trusted AI, drone supply chains
  - [taiwan] Diplomatic discord over haze issue erupts, Indonesia cuts natural gas exports to Singapore | International
  - [japan] Liberal Democratic Party Policy Research Council Chairman Kobayashi on consumption tax reduction related bill 
  - [korea] Bubblemaps: BMT opens spot trading on Upbit's KRW market - 24 Oct 2026
  - [taiwan] Atypical employment ratio dips to 14-year low: DGBAS
  - [korea] Samsung Electronics and SK hynix bonuses: 700 million won vs. 150 million won at Micron in Taiwan—why the huge
  - [taiwan] Taiwan Semiconductor Manufacturing Company Ltd. Stock 12‑Month Price Target Cut to $553.18, Implies 32% Upside
  - [china] The central bank will carry out 700 billion yuan of MLF operations to reduce volume and continue operations
  - [japan] What's New October, 2026 : Ministry of Finance
  - [korea] With the won-yen exchange rate moving around 840 won per 100 yen, the Bank of Japan's expectation of..
  - [korea] Bank of Korea maintains base interest rate at 3%... Leave room for price increases due to price instability

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
      "published_utc": "2026-10-25T19:12:43+00:00",
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

