atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-01T04:22:45.056645+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1290
  🇨🇳 China          765
  🇹🇼 Taiwan         258
  🇰🇷 Coreia do Sul  687

## O que já está no feed (não repita)

  - [japan] Government plans to submit 21 bills including consumption tax reduction bill in extraordinary Diet session
  - [china] China’s Tencent leases 100,000 chips from Oracle to accelerate AI push, FT reports
  - [japan] Sources of Changes in Current Account Balances and Market Operations (Sept.)
  - [japan] Asian currencies mixed as dollar holds highs, yen slips on BOJ signals
  - [japan] Bank of Japan Tankan Economic judgment of large companies in manufacturing industry improves for 6th consecuti
  - [japan] Japan’s patchy business mood takes pressure off BOJ for immediate hike
  - [japan] BoJ Policymakers See Scope for Faster Rate Hikes
  - [japan] Japanese Yen weakens as BOJ summary damps bets for back-to-back rate hike
  - [china] China’s Tencent Leases 100,000 Chips From Oracle To Accelerate AI Push - FT
  - [japan] Japan bond yields rise as US Treasury selloff persists, BOJ outlook in focus
  - [japan] Stock prices rise significantly Buy orders for AI/semiconductor related stocks
  - [china] Yuan Appreciation Intact but U.S.-China Rate Gap to Cap Pace — Market Talk
  - [japan] BOJ Likely to Remain on Guard Against Inflation — Market Talk
  - [china] Greer urges G20 to back Trump tariff agenda, takes aim at China
  - [japan] Tokyo Metro aims to ease rush by projecting vehicle congestion on the floor
  - [japan] [Today's Oha Biz October 1st (Thursday)] Nidek final deficit 564.6 billion yen
  - [japan] What is the NHK public opinion poll? Survey targets and methods
  - [japan] [New phase of the “Beer Wars”] What will happen to the beer industry with the liquor tax reform on October 1st
  - [china] China's PMI Improvement May Not Be Sign of Economic Recovery — Market Talk
  - [korea] Seoul shares narrow losses late Thurs. morning amid inflation woes
  - [japan] Japan 10-Year Yield Rises on Hawkish BOJ Outlook
  - [japan] Tankan Supports View for Faster-Than-Before BOJ Rate Hikes — Market Talk
  - [japan] Yen Falls After BOJ Summary Eases Rate-Hike Bets
  - [korea] Lotte expands financial, export support for partners
  - [japan] Japan's Nikkei hits six-week high as Micron forecast lifts chip stocks
  - [korea] South Korean won, Thai baht lead losses across Asian currencies
  - [japan] Yen Weakens as Dollar, Treasury Yields Weigh
  - [japan] Bank of Japan's short view on the 6th period of continuous improvements in the large enterprise manufacturing 
  - [japan] Bank of Japan Tankan: Large companies and non-manufacturing industries worsen for the first time in five quart
  - [japan] Bank of Japan's main opinions were less hawkish than expected (NRI researcher's commentary on current events)
  - [korea] Korea moves to cut bond issuance as high rates bite
  - [japan] Need to accelerate pace of interest rate hikes; strong economy, wary of upward movement in prices; Bank of Jap
  - [japan] BOJ Summary Points to Growing Risk of Inflation Overshooting Target
  - [korea] SK Hynix to review shareholder protection measures after reports of Solidigm's US IPO
  - [taiwan] TSMC weighs investment in Texas to expand U.S. chip production, Reuters reports
  - [korea] South Korea’s Export Growth Extends Rally as Chip Boom Rolls on
  - [korea] South Korea’s Monthly Exports Hit Record as Chip Boom Rolls on
  - [korea] S.Korea Sept exports hit record high as AI boom drives chip sales to all-time peak
  - [japan] Japan MOF To Auction Y600.0B Of 30-Year Govt Bonds Oct 8
  - [korea] AI Boom Powers South Korea's September Exports Past $120 Billion — Update

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
      "published_utc": "2026-10-01T04:22:45+00:00",
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

