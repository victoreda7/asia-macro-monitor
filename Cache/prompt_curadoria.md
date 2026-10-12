atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-12T04:52:43.883160+00:00
Total: 2844 manchetes

  🇯🇵 Japão          1108
  🇨🇳 China          785
  🇹🇼 Taiwan         276
  🇰🇷 Coreia do Sul  675

## O que já está no feed (não repita)

  - [china] China Plays Critical Role in Global AI Supply Chain, Domestic AI Ecosystem — Market Talk
  - [korea] CXMT: How big is its market threat to Samsung, SK Hynix and Micron?
  - [korea] The Bank of Korea repeatedly hinted at the possibility of further interest rate hikes... Market outlook “withi
  - [korea] Why is Samsung Electronics stock sliding today?
  - [korea] Why is SK Hynix stock sliding today?
  - [china] Yuan holds near 3-1/2-year high against dollar as rate bets ease
  - [japan] Nikkei average growth is sluggish, focus on TSMC performance and price index (TV Asahi (ANN))
  - [taiwan] Elon Musk Wants Tesla, SpaceX To Test 10 Chip Designs A Year At Terafab As TSMC Reportedly Eyes Texas
  - [china] EU-China Deal Could Halve Chinese Hybrid Car Exports
  - [china] China Moves to Stave Off Wider EU Trade War With Hybrid Deal
  - [china] PBOC Expected to Tolerate Further Gradual Yuan Appreciation — Market Talk
  - [korea] South Korean Won Hits 2-Year High
  - [korea] Bank of Korea Governor Shin Hyun-song: “Monetary policy independence is firm”… Leveraged ETF admits lack of ri
  - [korea] South Korean Won Hits 24-month High
  - [taiwan] Gold gains on weaker oil, dollar; US inflation data in focus
  - [japan] Yen Holds Steady in Thin Holiday Trade
  - [taiwan] TSMC, ASML eye 12-inch photomasks to unlock High-NA EUV's full-field potential
  - [korea] Bank of Korea Governor Shin Hyun-song attends G20/IMF annual general meeting... Global economic and monetary p
  - [korea] South Korean Won's Gains Underpinned by Robust Exports, Current Account Surplus — Market Talk
  - [china] China sanctions Paraguay, Belize ministers over Taiwan ties
  - [korea] Governor of the Bank of Korea: “Reduces ultimate costs by raising base interest rates in consecutive months in
  - [korea] Governor of the Bank of Korea: “Buying time by preemptively raising interest rates… ultimately reducing costs.
  - [korea] The role of the Bank of Korea in expansionary finances is highlighted... Shin Hyun-song “I will protect my ind
  - [korea] [Photo] National Assembly Finance and Economy Committee conducts audit of the Bank of Korea’s government affai
  - [korea] [2026 National Assembly Audit] Shin Hyun-song “We will carry out independent monetary policy without hesitatio
  - [korea] Most Asian currencies muted; South Korean won hits two-year high
  - [korea] S.Korean stocks slide as chip selloff deepens, foreign selling persists
  - [taiwan] TSMC expected to report sixth straight quarter of record profit thanks to AI boom
  - [korea] Governor of the Bank of Korea: “Carry out independent monetary policy without hesitation”
  - [china] China-EU Deal Likely Averts Trade War, But Impact Limited — Market Talk
  - [korea] Finance minister urges preemptive action for supply chain stability
  - [taiwan] MediaTek flagship AP share to surpass Samsung as TSMC boosts Dimensity
  - [korea] After the tax reform plan, high-priced apartments in Gangnam, Seoul, have turned weak, but the upwar..
  - [korea] [Issue Inspection] Bank of Korea raises base interest rate to 3.0%...maintains ‘austerity stance’
  - [korea] Governor of the Bank of Korea: “Inflation is expected to remain above the target level for a considerable peri
  - [korea] Bank of Korea Governor: Chip Industry Supports Faster Economic Growth
  - [korea] [2026 National Assembly Audit] Bank of Korea Governor's inflation rate exceeds target for a considerable perio
  - [china] CHINA PBOC CONDUCTS CNY50 BLN VIA 7-DAY REVERSE REPO MON
  - [korea] S. Korea likely to continue solid growth driven by robust chip exports
  - [china] The central bank launched a 50 billion yuan 7-day reverse repurchase operation today

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
      "published_utc": "2026-10-12T04:52:44+00:00",
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

