atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-19T06:02:43.922719+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1025
  🇨🇳 China          908
  🇹🇼 Taiwan         312
  🇰🇷 Coreia do Sul  755

## O que já está no feed (não repita)

  - [korea] South Korea's exports top $1 trillion for first time on chip boom
  - [japan] Prime Minister Takaichi attends the APEC Summit and holds a press conference after the meeting
  - [china] Bernstein names top China semiconductor equipment stocks
  - [korea] S. Korea's exports top US$1 tln for 1st time on strong chip demand
  - [korea] South Korea is the fourth country in the world to join the $1 trillion export club.According to the
  - [korea] South Korea 2026 exports hit $1 trillion milestone, Yonhap citing trade ministry
  - [china] Musk promete aumentar a produção da Tesla na fábrica da China, segundo a mídia estatal chinesa
  - [korea] South Korean entertainment stocks surge up to 30% on China trade deal
  - [japan] Japan auto industry targets common standards to strengthen supply chain
  - [japan] Japan AI selloff: These chips and electronics stocks were the worst hit
  - [korea] Although the amount of foreign real estate alternative investment by domestic financial companies ha..
  - [taiwan] Taiwan Stocks Plunge, Asian Currencies Stay Cautious as APEC Summit Highlights
  - [taiwan] UBright eyes semiconductor, passive components and smart acoustics growth
  - [china] [Local footage scheduled to be distributed] High-profile US-China summit meeting to be held later
  - [japan] BOJ's Ueda Vows to Keep Careful Eye on Fed Moves — Update
  - [china] Trump Suggests US Can Sell Blackwell Chips to China in Future
  - [japan] Finance Minister Katayama plans to leave stock valuation of unlisted companies to tax authorities
  - [china] China's yuan steady as Trump-Xi meeting in focus
  - [korea] Apple seeks to lock in memory supply as Samsung, SK hynix gain leverage
  - [korea] A 10% increase in the value of the won will reduce the cost of living per household by more than 160..
  - [japan] BOJ's Ueda Reaffirms Readiness to Keep Raising Rates
  - [korea] [Reporter Ki's Money Story⑪] Why is the loan interest rate rising even though the base interest rate remains t
  - [taiwan] Lam Research's Taiwan R&D expansion targets faster chip development with TSMC
  - [japan] Japan’s Datasection slumps on big guidance cut amid U.S.-China chip access row By Investing.com
  - [japan] BOJ chief plays down soft consumption data, signals near-term rate hike
  - [japan] BOJ chief offers upbeat view on consumption despite recent weakness
  - [taiwan] Taiwan dollar weakens as Asian currencies largely muted
  - [korea] Household debt of 2,030 trillion, home loan interest rate highest in 14 years... Vulnerable borrowers face dif
  - [japan] BOJ chief rules out further tweaks to pace of ETF sales
  - [japan] Japan’s Datasection slumps on big guidance cut amid U.S.-China chip access row
  - [china] On November 19, the central bank launched a 767.5 billion yuan overnight reverse repurchase operation.
  - [china] CHINA PBOC CONDUCTS CNY767.5 BLN VIA O/N REVERSE REPO THURS
  - [japan] BOJ Governor Ueda says financial conditions loose despite rate hikes
  - [korea] Samsung Electronics plays down concerns about neocloud companies and AI bubble
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7128 THURS VS 6.7118
  - [korea] Samsung Electronics downplays concerns about neocloud firms and AI bubble
  - [japan] Financial environment is accommodative, interest rates will continue to rise depending on economic, price and 
  - [china] The central bank launched a 767.5 billion yuan overnight reverse repurchase operation today
  - [china] To protect money withdrawals during tax period, the central bank launches 700.2 billion yuan overnight reverse
  - [taiwan] Microsoft’s chip packaging deal hands Intel credibility more than revenue

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
      "published_utc": "2026-11-19T06:02:44+00:00",
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

