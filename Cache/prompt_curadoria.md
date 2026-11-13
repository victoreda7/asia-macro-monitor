atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-13T17:02:47.473651+00:00
Total: 3000 manchetes

  🇯🇵 Japão          994
  🇨🇳 China          868
  🇹🇼 Taiwan         308
  🇰🇷 Coreia do Sul  830

## O que já está no feed (não repita)

  - [japan] GlobalFoundries breaks ground on first new semiconductor fab under landmark U.S.-Japan initiative
  - [korea] Applied Materials, Diodes, Marvell Technology, Applied Optoelectronics, and SK hynix stocks trade down, what y
  - [china] Update: China's yuan loans grow 11.42 trln yuan in first 10 months
  - [china] 1st LD-Writethru: China's yuan loans grow 11.42 trln yuan in first 10 months
  - [korea] Modine Manufacturing jumps 30% on reports of acquisition talks with Samsung
  - [china] China's yuan loans grow 11.42 trln yuan in first 10 months
  - [china] China’s access to some Nvidia chips in doubt as curbs gain traction in US Congress
  - [korea] Polen Global Growth adds Seagate, AMD And SK Hynix, trims Nvidia and Broadcom among Q3 moves
  - [china] The central bank will carry out a 200 billion yuan buyout reverse repurchase operation to stabilize market exp
  - [china] The People's Bank of China will scale back its operations and carry out a 200 billion yuan six-month buyout re
  - [china] Alice Huang-Linked Firm Procured Banned Nvidia Chips in China
  - [japan] Food consumption tax reduction bill: Subsidy “Consideration for more than 50% of workers”
  - [china] China could cap rare earths sales if US expands chip curbs over Nvidia: analysts
  - [japan] Dollar set for best week in two months, weak yen captures Tokyo’s attention
  - [china] 664 billion! After the anchor change, the central bank’s first “overnight + 7 days” matching operation will re
  - [china] The central bank takes action! 200 billion yuan buyout reverse repurchase is coming
  - [japan] Interim results for three megabanks record high profits due to rising interest rates
  - [japan] Analyst sees 4 straight quarters of GDP growth
  - [korea] DeepX bets $100M on new AI chip using Samsung technology
  - [taiwan] TSMC Faces Major Security Scare as Hackers Demand Bitcoin
  - [japan] BREAKING NEWS: Japan eyes 60 tril. yen for 5-yr defense buildup without major tax hike
  - [korea] Bitcoin slides below $70,000 as inflation concerns hurt crypto
  - [japan] Interim financial results of 3 megabanks show record high profits again due to Bank of Japan's interest rate h
  - [china] Nvidia scandal deepens as banned chips traced to China
  - [japan] Dollar set for best week in two months, yen tests 160 By Reuters
  - [china] How a slowdown in US AI capex might impact China's economy
  - [china] Central Bank: Will carry out 200 billion yuan buyout reverse repurchase operation
  - [china] Scaled-down sequel! The central bank will launch a 200 billion yuan buyout reverse repurchase operation next w
  - [china] Central Bank: Launch 200 billion yuan buyout reverse repurchase operation on November 16
  - [japan] 3 mega banks G's interim results show record high profits, boosted by Bank of Japan interest rate hike, full-y
  - [korea] GRAVITY Co., Ltd. (GRVY) Q3 Net Profit Rose 7.7% YoY to KRW 21.4B
  - [japan] Three mega bank groups achieve record high profits in interim results, boosted by Bank of Japan's interest rat
  - [japan] Adjustment by postponing government bond NISA for individuals
  - [japan] Rakuten's 3rd quarter financial results record high sales but end up in the red due to strong finance and trav
  - [china] China's New Yuan Loans Contracted in October
  - [korea] VKAISS 2026 Strengthens Vietnam and South Korea Cooperation in AI and Semiconductors
  - [japan] Prime Minister Takaichi says consumption tax reduction bill support funds will be considered for 50% or more o
  - [japan] Profit of 5 major banks approaches 4 trillion yen; interest income increases due to Bank of Japan interest rat
  - [china] Metro Holdings: Indonesian property sales and improved China results drove a return to pre-tax profit
  - [china] Metallurgical Corporation Of China's January-October New Contracts Totalled 548.8 Billion Yuan

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
      "published_utc": "2026-11-13T17:02:47+00:00",
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

