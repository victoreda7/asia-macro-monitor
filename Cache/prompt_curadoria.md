atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-20T02:52:40.545435+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1048
  🇨🇳 China          902
  🇹🇼 Taiwan         320
  🇰🇷 Coreia do Sul  730

## O que já está no feed (não repita)

  - [japan] [Today's Oha Biz Friday, November 20th] Full-scale discussion on tax reform begins
  - [japan] BOJ Likely to Raise Rate in December or January Amid Persistent Inflation — Market Talk
  - [japan] Japan Inflation Accelerates on Surging Cost of Daily Necessities — Market Talk
  - [japan] October consumer price index +2.2% compared to the same month last year Index excluding fresh food
  - [japan] Japan Consumer Inflation Reinforces Rate-Hike Expectations — Update
  - [korea] Samsung Electronics appoints new director for its memory chip division
  - [japan] Is the ``Mongol Empire that shocked the world'' an unexpected measure against unemployment? ...The unexpected 
  - [japan] Japan core inflation picks up, makes case for BoJ rate hike stronger
  - [taiwan] TSMC tightens China AI chip curbs as new US rules close manufacturing loophole, sources say
  - [japan] Rising Goods Prices Likely to Keep Driving Japan Inflation — Market Talk
  - [korea] Samsung Electronics, SK hynix slide on Wall Street tech selloff
  - [korea] SK Hynix was the largest net buyer of the top 1% return on stock investment in early trading on the
  - [china] The central bank launched 379.5 billion yuan in overnight reverse repos, with a net withdrawal of 688 billion 
  - [japan] BOJ December Rate Hike Looks Likely After CPI Results — Market Talk
  - [japan] Japan's core inflation rose to 2.2% in October, strengthening the Bank of Japan's expectations for a rate hike
  - [china] CHINA PBOC CONDUCTS CNY379.5 BLN VIA O/N REVERSE REPO FRI
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7131 FRI VS 6.7128
  - [korea] Samsung names new memory, mobile chiefs as chips sweep promotions
  - [china] The central bank launched a 379.5 billion yuan overnight reverse repurchase operation today
  - [japan] Announcement of 2-year JGBs to Be Issued in December 2026
  - [japan] Japan MOF To Auction Y2.8T Of 2-Year Govt Bonds Nov 30
  - [korea] South Korean shares hit 10-month low as chipmakers track US tech selloff
  - [japan] Stock price temporarily fell by more than 2,800 yen due to concerns about the future of the AI ​​and semicondu
  - [japan] Japan MOF To Auction Y3.1T Of TD-Bills Nov 27
  - [japan] Japan's Inflation Likely to Rise Much More Next Year — Market Talk
  - [japan] Consumer price index rose 2.2% in October
  - [korea] Protec Co Wins 23.4 Billion Won Order From Samsung Electronics
  - [japan] Analysis-BOJ’s ambiguity on rate hike path could tempt yen bears
  - [japan] Japan CPI Rises to Fastest This Year, Backing BOJ Hike Case
  - [korea] Samsung Electronics appoints new head for its memory chip business
  - [japan] Interest Rate (November 19 2026)
  - [japan] Bank of Japan: Reconsidering the logic of interest rate hikes (current events commentary by NRI researchers)
  - [japan] Japan's finance minister says JT dividend cut will not affect state budget plan
  - [korea] Producer prices drop in Oct. on lower food prices
  - [korea] “The Bank of Korea’s base interest rate is expected to reach 3.5% in February next year.”
  - [japan] Japan Consumer Prices Jump 0.8% In October
  - [korea] Key facts: SK hynix Raises $26.5B; Reaffirms 100 Trillion Won Returns
  - [japan] Japan CPI inflation rises in Oct, core print slightly misses estimates By Investing.com
  - [japan] JAPAN OCT CPI: SERVICES PRICES CATCHING UP WITH GOODS INFLATION AMID CONTINUED WAGE HIKES IN FISCAL 2026 BUT R
  - [japan] Japan’s core inflation accelerates in October, cementing rate hike expectations

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
      "published_utc": "2026-11-20T02:52:40+00:00",
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

