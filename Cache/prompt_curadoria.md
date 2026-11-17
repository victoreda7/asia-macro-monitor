atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-17T00:55:35.106159+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1035
  🇨🇳 China          874
  🇹🇼 Taiwan         304
  🇰🇷 Coreia do Sul  787

## O que já está no feed (não repita)

  - [japan] Interest Rate (November 16 2026)
  - [korea] Bank of Korea Could Raise Inflation Forecasts at Coming Policy Meeting — Market Talk
  - [taiwan] UK sovereign AI push needs Taiwan's chip manufacturing and OSAT partners
  - [japan] A weak yen causes prices to rise and consumption to shrink...Japanese economy has negative growth for the firs
  - [japan] Dollar's Bias Vs. Yen Looks Increasingly Bullish, Charts Show — Market Talk
  - [japan] The trick of a subscription service that tricks your brain into thinking "If it's less than 10,000 yen per mon
  - [china] China resumes storing crude oil, giving it fuel export options: Russell
  - [china] U.S. Department of Commerce launches new rules to prevent detouring of advanced semiconductors to China and ot
  - [korea] The possibility of the Bank of Korea's base interest rate increasing from 3.00 to 3.25% this month increases.
  - [korea] The Bank of Korea is likely to raise its benchmark interest rate by 0.25%p this month.
  - [japan] SoftBank, Rakuten push Japan retail bond issuance to record high
  - [taiwan] 3G Capital starts position Nu, adds to Taiwan Semiconductor, cuts stake in Intel among Q3 moves
  - [japan] Japan's economy unexpectedly shrinks as inflation squeezes households
  - [china] US to curb China’s access to AI chips as Trump heads to Asia
  - [china] US issues new chip rule as China's AI companies fear Nvidia scandal fallout
  - [taiwan] Lone Pine Capital Reports Stake in Intel, Amazon; Raises Stakes in Alphabet, TSMC
  - [japan] The famous soba, which has been priced at 555 yen for 40 years, is suddenly priced at 1,110 yen...The reason w
  - [japan] Will the "smart cash register special demand" return due to food tax cuts? Reasons why smart cash registers an
  - [korea] A $1 Billion Reason SK Hynix Stock Is Falling Today
  - [china] China developer Huafa's debt woes show resurgence of credit risk
  - [china] Nvidia China Trouble Could Spill Over to These AI Chip Stocks
  - [taiwan] Tiger Global Management Cuts Share Stake In Meta, TSMC, GE Vernova
  - [japan] Advantest Stocks Tumble 11.12% as Tokyo Chip Selloff Drags Nikkei Below 60,00
  - [korea] SK hynix Stocks Sink 7.89% Despite 80% Margin and 100 Trillion Won Payout
  - [taiwan] TSMC Stocks Slide 5.7% Despite October Sales Jumping 59.7% to a 2026 High
  - [japan] US voice AI developer ElevenLabs to buy Japanese-focused peer Kotoba
  - [china] Nvidia scandal, AI anger, Beijing’s mockery: 7 US-China relations reads
  - [japan] Teradyne Stocks Drop 6.14% as Advantest's 11% Tokyo Plunge Hits Chip Testers
  - [japan] Japan eyes two-pronged approach to cover tax cut, growth investments
  - [japan] EU sets tariffs on steel from India, Japan, Taiwan, Turkey, Vietnam
  - [china] US blocks China's indirect access to American AI chips
  - [china] No chips for you: US issues rule to stymie China's access to AI GPUs via data centers
  - [japan] Nomura Real Estate to acquire 8 MW of energy storage in Japan
  - [korea] Micron, SK hynix, and Sandisk shares plummet, what you need to know
  - [korea] Why is SK hynix stock sliding today?
  - [japan] Yen Could Strengthen Versus Dollar by Year-End — Market Talk
  - [korea] Samsung plans to build satellite chips at Texas fab for SpaceX: report
  - [china] China Resources Power Posts October Net Generation Of Subsidiary Power Plants Up 20.9% To 20.1 MLN MWh
  - [japan] Japanese Yen Offers Best Risk-Reward — Market Talk
  - [japan] Yomiuri: JIC Expects Capital Gain of Over 900 Billion Yen from Sale of JSR Shares to Mitsui Chemicals

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
      "published_utc": "2026-11-17T00:55:35+00:00",
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

