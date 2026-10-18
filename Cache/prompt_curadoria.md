atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-18T13:08:31.944613+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1033
  🇨🇳 China          885
  🇹🇼 Taiwan         342
  🇰🇷 Coreia do Sul  740

## O que já está no feed (não repita)

  - [korea] Samsung will use TSMC technology for Nvidia's next-generation memory chips, according to Seoul newspaper
  - [korea] Samsung to use TSMC technology for Nvidia's next-generation memory chips, Seoul newspaper reports
  - [taiwan] Health minister decries bill subsidizing NHI premiums for most seniors
  - [japan] Yokohama mayoral election exit poll results
  - [china] TSLA, CSIQ Stocks In Focus As China Tightens Solar Manufacturing Technology Exports
  - [japan] Yokohama mayoral election vote counting and exit poll election information is here [Breaking news]
  - [korea] Bank of Korea decides base interest rate this week...market expected to freeze
  - [china] Huizhou China Eagle To Issue 47.01 Mln Shares At 14.89 Yuan Apiece In Share Placement
  - [korea] Samsung Electronics to Use TSMC 3nm Process for NVHBM Base Dies at Nvidia's Request
  - [china] Explosive Says Units' Jan-Sept New Blasting Services Contracts At 12 Bln Yuan
  - [china] This Week’s Key Economic and Crypto Events: US Initial Jobless Claims, China GDP
  - [korea] BOK to pause before November hike, rates to peak at 3.50%, survey shows
  - [korea] Controversy over the semiconductor supercycle "peakout" is heating up ahead of the Bank of Korea's M..
  - [korea] “The Bank of Korea will freeze the base interest rate in October…likely to raise it in November.”
  - [china] Hygon Information Plans To Buy Back Shares For Up To 800 Mln Yuan
  - [korea] The balance of group loans increased while jeonse loans decreased amid the government's tightening o..
  - [korea] [Photo] Strengthening global financial supply chains
  - [china] Wuxi Hyatech To Issue Convertible Bond Raising 600 Mln Yuan For Projects
  - [china] China proposes export curbs on 12 key solar manufacturing technologies
  - [japan] BREAKING NEWS: 65.1% concerned about consumption tax cut's fiscal impact: Kyodo poll
  - [china] Shengyi Technology Plans To Buy Back Shares For Up To 300 Mln Yuan
  - [china] Montage Technology Plans To Buy Back Shares For Up To 500 Mln Yuan
  - [china] Galaxycore Plans To Buy Back Shares For 150-300 Mln Yuan
  - [korea] Foreign exchange prices are displayed at a currency exchange in Myeong-dong, Jung-gu, Seoul on the 1..
  - [china] China's solar panel exports extend slump in September
  - [japan] This is the V-shaped recovery! The last trump card "Night Ticket Strategy" is the savior of Jangria Okinawa, w
  - [china] China proposes export controls on solar-manufacturing technologies
  - [korea] The base interest rate has risen repeatedly... Expected to take a breather in October
  - [korea] Samsung, SK hynix suffer worst weekly stock rout since 2008
  - [china] PBOC Deputy Calls for Greater Private Involvement in Sovereign Debt Restructuring
  - [korea] Samsung invests $22.8m in Texas workforce as TSMC eyes entry
  - [korea] The Bank of Korea forecasts to freeze the base interest rate by 3% on the 22nd... Possibility of further incre
  - [china] PBOC Deputy Urges Private Role in Sovereign Debt Restructuring
  - [china] China's September refined fuel exports surge amid Iran war, diesel exports more than triple
  - [korea] The Monetary Policy Committee has raised the base interest rate in succession, with a freeze expected this mon
  - [china] China's September grain, sugar and pork imports
  - [japan] Ruling and opposition party leaders discuss consumption tax reduction bill NHK Sunday debate
  - [korea] What To Expect From BOK Financial’s (BOKF) Q3 Earnings
  - [korea] [Preview of the Monetary Policy Committee] Bank of Korea freezes this month... November's raise card remains
  - [korea] [Preview] Bank of Korea freezes this month... November's raise card remains

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
      "published_utc": "2026-10-18T13:08:32+00:00",
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

