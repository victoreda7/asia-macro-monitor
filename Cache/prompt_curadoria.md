atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-29T07:25:21.073157+00:00
Total: 420 manchetes

  🇯🇵 Japão          155
  🇨🇳 China          113
  🇹🇼 Taiwan          34
  🇰🇷 Coreia do Sul  118

## O que já está no feed (não repita)

  - [korea] Seoul stocks fall for 2nd day on inflation woes
  - [korea] Seoul stocks open lower on inflation woes
  - [japan] EQt Raises Tender Offer Price For Kakaku.Com To 3,681 Yen From 3,680 Yen, Filing Shows
  - [japan] Asia stocks subdued as rising yields, oil weigh; RBA hikes rates as expected
  - [korea] The Bank of Korea approves a monetary and credit policy report containing the background for raising the base 
  - [japan] Japanese Shares Fall on Inflation Worries
  - [taiwan] Singapore's chip progress
  - [korea] Korea launches its own version of popular US fund Roundhill Memory ETF DRAM
  - [japan] The Bank of Japan and the Federal Reserve have no choice but to worry about stock prices -- The focus of monet
  - [china] Stifel upgrades STAAR Surgical stock rating on China growth outlook
  - [korea] SK Hynix Could Post Lower-Than-Expected But Still Record 3Q Operating Profit — Market Talk
  - [korea] (LEAD) Seoul stocks fall for 2nd day on inflation woes
  - [taiwan] Column: Why Micron's US$250M venture fund is about more than HBM margins—Taiwan has a stake in it
  - [korea] (URGENT) Seoul stocks fall for 2nd day on inflation woes
  - [china] China Signals Economic Stimulus to Counter Worsening Slowdown
  - [japan] Nikkei 225 drops 1.2% as US interest rates hit 19-year high: Why KOSPI barely moves
  - [korea] Korea’s dollar store giant Daiso emerges as real estate player with $355 mn deals
  - [korea] Samsung shares rise after 5% drop as Nvidia bets on AI beyond chips
  - [taiwan] Advanced packaging shifts toward system integration as AI renews semiconductor talent appeal
  - [taiwan] GlobalFoundries eyes GaN expansion to challenge TSMC in AI
  - [korea] SK Hynix tests HBM5 with TSMC as HBM4 enters Nvidia's next platform
  - [japan] [By prefecture] The prefecture with the highest prices is Tokyo, and the second is Kanagawa Prefecture...A ran
  - [china] China’s LNG Imports to Fall for Second Month Due to High Prices
  - [japan] The prefecture's economy is left unchanged as a "moderate recovery." Prices continue to be under upward pressu
  - [korea] Samsung Electronics, SK hynix rebound on bargain-hunting
  - [korea] CPTPP membership could lift Korea GDP by $6.5bn over decade: Gov’t
  - [china] The central bank launched a 90.5 billion yuan 7-day reverse repurchase operation in the open market
  - [korea] The contraction of transactions in the housing market in the three Gangnam districts (Gangnam, Seoch..
  - [korea] Following the Deputy Prime Minister, Shin Hyun-song met with 16 bank presidents and also listened to opinions 
  - [korea] South Korean exports seen rising for 16th month on solid AI chip demand
  - [korea] Samsung Electronics: HBM will account for nearly 30% of industry DRAM capacity next year
  - [china] Soybeans near one-month low on exclusion from China's proposed tariff cuts
  - [korea] Samsung Electronics says HBM to account for nearly 30% of industry DRAM capacity next year
  - [korea] While the Seoul apartment sales price index, which compared January to August this year, rose 6.4%
  - [korea] (LEAD) Seoul stocks open lower on inflation woes
  - [korea] Hanmi Semiconductor Wins 8 Billion Won Order
  - [korea] (URGENT) Seoul stocks open lower on inflation woes
  - [korea] Samsung Electronics allocates US$1 billion to expand Helix Digital AI, a company backed by KKR
  - [korea] Samsung Electronics commits $1 billion to KKR-backed Helix Digital AI buildout
  - [japan] EXCLUSIVE Japan's currency diplomat Mimura urges markets to heed 'very clear' warning on yen

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
      "published_utc": "2026-09-29T07:25:21+00:00",
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

