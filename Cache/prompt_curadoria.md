atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-23T04:32:43.331264+00:00
Total: 3000 manchetes

  🇯🇵 Japão          991
  🇨🇳 China          840
  🇹🇼 Taiwan         367
  🇰🇷 Coreia do Sul  802

## O que já está no feed (não repita)

  - [japan] BOJ Likely to Hike Three More Times, Taking Policy Rate to 2% — Market Talk
  - [china] When Typhoon Qiangbi hit, the central bank continued to provide foreign currency funds of US$585 million | San
  - [china] China's yuan holds steady, set for fourth weekly rise
  - [korea] SK Hynix puts US IPO of chip unit Solidigm on hold after Seoul authorities raise concerns
  - [japan] Asia FX steadies as oil surge weighs on risk appetite, yen holds gains
  - [japan] September consumer prices +2.1% compared to the same month last year, the first time in nine months that the i
  - [japan] BOJ Likely to Declare It Achieved 2% Inflation Target in Upcoming Meeting — Market Talk
  - [japan] Yen rallies as global tech rout sparks flight to safety
  - [japan] Yen Strengthens on French Debt Woes, Hits One-Year High Against Euro
  - [japan] Japan considers ending gasoline subsidies in December- Reuters
  - [korea] Asia stocks fall as AI rout batters S.Korea; Japan spooked by strong CPI
  - [japan] Japan government, BOJ gap on inflation laid bare ahead of key policy meeting
  - [japan] BOJ Could Be in Tough Spot If Costs Curb Consumption — Market Talk
  - [korea] Krafton Target Price Cut to KRW210,000 From KRW 300,000 by Nomura>259960.SE
  - [korea] Chainlink partners with LG CNS to drive Korean won stablecoin expansion
  - [korea] Bank of Korea issues unprecedented warning against fiscal expansion: “If spending continues to increase, it wi
  - [korea] SK Hynix says Solidigm suspends review of US IPO, citing market volatility
  - [japan] Yen's Latest Rise Likely Driven by Safe-Haven Demand — Market Talk
  - [korea] South Korean won, Philippine peso rises the most among Asian FX
  - [japan] Japan futures slide as yen strengthens, on track for second weekly loss
  - [china] The central bank launches 258 billion yuan overnight reverse repurchase operation
  - [japan] Yen shines as AI jitters spur safe-haven rush
  - [japan] Bitcoin Faces 2 December Rate Hikes as Japan’s Inflation Clears the BOJ’s Target
  - [japan] The consumption tax reduction bill was questioned by the House Finance Committee on the 27th and jointly revie
  - [japan] Japan Consumer Inflation Uptick Offers Tailwind for BOJ Rate Hike — Update
  - [korea] SK Hynix Pulls Plug on Memory-Chip Unit U.S. IPO On Market Jitters —Update
  - [japan] Asian shares wobble as tech rout boosts bonds, dents rate hike bets
  - [china] CHINA PBOC CONDUCTS CNY258 BLN VIA O/N REVERSE REPO FRI
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7180 FRI VS 6.7195
  - [japan] Japan weighs phasing out gasoline subsidies from December as costs mount, officials say
  - [korea] South Korean Government and Central Bank Push to Regulate Stablecoins Through Foreign Exchange Law Revision
  - [china] The central bank launched a 258 billion yuan overnight reverse repurchase operation on October 23
  - [japan] Dollar Likely to Remain in 155-160 Yen Range in Near Term — Market Talk
  - [japan] Decided on amendments to digitize bill of lading, etc. to improve efficiency of trade procedures
  - [korea] SK Hynix abandons plan for US unit's IPO, citing market volatility
  - [korea] Kospi drops on AI funding worries, oil-driven inflation fears
  - [japan] Yen Rallies on Haven Buying, Strong Inflation
  - [japan] Japan Inflation Rises Above BOJ Target Level, Backing Rate Hikes
  - [japan] Japan Inflation Rises Above BOJ Target, Backing Rate Hikes
  - [korea] Why is SK Hynix stock sliding today?

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
      "published_utc": "2026-10-23T04:32:43+00:00",
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

