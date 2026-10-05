atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-05T22:22:47.286801+00:00
Total: 2922 manchetes

  🇯🇵 Japão          1247
  🇨🇳 China          771
  🇹🇼 Taiwan         250
  🇰🇷 Coreia do Sul  654

## O que já está no feed (não repita)

  - [japan] <Machine tool orders> The summer decline continues to be strong, with August orders reaching 197.8 billion yen
  - [japan] Threatening complaints were made, but an "unexpected savior" appeared during the "litigation trouble" with a b
  - [taiwan] SPCX Stock Ends Higher On Starship Fuel Plans, Analyst Optimism And TSMC Talks
  - [korea] South Korea FX Reserves End Three-Month Rising Streak
  - [japan] Nasdaq hits new high; buy tech stocks even as long-term interest rates rise
  - [china] Behind Germany's far-right AfD's rise is the "China Shock"...China's industrial competitiveness is exporting t
  - [japan] Prime Minister Takaichi seeks understanding on consumption tax cut, opposition parties plan to provide financi
  - [taiwan] Intel stock slides as TSMC explores Terafab tie-up, analyst flags share losses
  - [taiwan] Tesla Stock Rises After Musk Confirms TSMC Talks
  - [china] Takaichi's ``aggressive fiscal policy'' is state capitalism that imitates China while viewing it as an enemy. 
  - [china] UK considering tariffs on Chinese car imports
  - [taiwan] Intel Stock Tumbles -- TSMC Eyes Elon Musk's Terafab Project
  - [japan] Focus is on “reduction of consumption tax on food products” Extraordinary Diet session convened
  - [korea] Korean shipbuilders, refiners see Q3 estimates upgraded; chipmakers face cuts
  - [china] P2P stablecoin wallets in China grew 43x despite restrictions on cryptocurrencies, according to Chainalysis
  - [china] Antimony Market Faces a Nov. 27 Export-Control Deadline from China
  - [japan] Japan and Australia finance ministers meet to launch new dialogue framework
  - [taiwan] Musk hints TSMC may join his mega chip venture, and Intel's stock is taking a hit
  - [china] India may be best placed to fill a China-sized hole in fuel exports: Maguire
  - [japan] Euro falls to 17-month low on Paris fiscal worries
  - [japan] Bank of Japan Deputy Governor Uchida AI “moves the financial environment more accommodatively” (TBS NEWS DIG P
  - [japan] After making an internal report about deficiencies in the remittance system at the Bank of Japan, she was bann
  - [japan] Asian currencies weaken as dollar gains, euro hits 17-month low
  - [taiwan] Taiwan Forex Reserves Edge Lower
  - [japan] Rapidus collaborates with 17 semiconductor design companies to attract attention for mass production
  - [japan] Japan farm minister retracts controversial budget remarks, makes apology
  - [taiwan] AMD's Lisa Su back in Taiwan as AI capacity crunch spreads beyond TSMC
  - [korea] Should I sell stocks and deposit money? Bankers’ deposit interest rate ‘increase rally’
  - [taiwan] Taiwan teams accelerate 2D semiconductor transfer with published research in Nature
  - [china] QCOM Gains Overnight After Patent Deal With China’s Huawei Covering AI Chip Tech
  - [japan] Japan service sector growth slows in September, PMI shows By Investing.com
  - [japan] Takaichi pledges fiscal discipline as Japan’s debt bill rises
  - [japan] Nikkei stock index retakes 70,000, 1st time since July, as Fed rate hike prospects dim
  - [japan] BREAKING NEWS: Japan farm minister retracts controversial budget remarks, makes apology
  - [japan] Bank of Japan New Building Blocks "Shogun's Road", Great Proposal from Tanzan to Pope...Road Replacement Opera
  - [japan] Japan services PMI misses forecasts in September as private-sector growth slows By Investing.com
  - [japan] Takaichi Faces Test of Economic Agenda as Japan Parliament Opens
  - [china] COMMENTARY: India may be best placed to fill a China-sized hole in fuel exports
  - [taiwan] Taiwan's September Inflation Likely Exceeded 2%, WSJ Poll Shows — Market Talk
  - [korea] Mortgage interest rates around 7%... Additional increases add to the burden

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
      "published_utc": "2026-10-05T22:22:47+00:00",
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

