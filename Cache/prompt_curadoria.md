atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-06T04:22:42.927663+00:00
Total: 3000 manchetes

  🇯🇵 Japão          890
  🇨🇳 China          900
  🇹🇼 Taiwan         325
  🇰🇷 Coreia do Sul  885

## O que já está no feed (não repita)

  - [korea] Korean stocks pare heavy losses as bargain hunters snap up blue chips; Kospi back above 5,000 mark
  - [japan] Asian FX mixed as yen gains on risk aversion, Taiwan dollar breaks 33 amid AI rout
  - [china] Exclusive-China’s top flash memory chipmaker targets more homegrown tools for new factory, sources say
  - [japan] Hanwa Co Ltd Says It Will Buy Back Up To 1.82% Of Own Shares Worth 5 Billion Yen
  - [korea] KOSPI crashes 8% to below 5,000, Nikkei plunges 5% as US elections trigger AI rout; Samsung, SK Hynix sink
  - [japan] BOJ eyes AI demand as inflation risk
  - [japan] Japan Q3 GDP growth seen slowing sharply as consumption, external demand drag: Reuters poll By Reuters
  - [china] China's yuan slips, looks set to snap five-week winning streak
  - [taiwan] Taiwan-UK tech ties could support Europe's chip autonomy drive
  - [taiwan] Taiwan Dollar Weakens on AI Selloff, Foreign Equity Outflows — Market Talk
  - [japan] Japan Q3 GDP growth seen slowing sharply as consumption, external demand drag: Reuters poll
  - [japan] Mr. Takaichi considers the proceeds from the sale of Bank of Japan ETFs as a source of funding for bridging go
  - [china] China Commerce Ministry: Held China-Netherlands Export Control Dialogue Mechanism Meeting In Shenzhen On Nov 5
  - [china] China to Cut Diesel Exports on Tight Stocks, Energy Aspects Says
  - [japan] Consumption tax reduction bill passed by the House of Representatives Finance Committee and will be passed by 
  - [japan] Prime Minister Takaichi's consumption tax reduction bill: “Support based on income for more than 30% of worker
  - [taiwan] Taiex plunges over 3,700 points in early trading as TSMC hits limit down
  - [korea] Mercedes-Benz overtakes BMW to rank second in imported car sales
  - [japan] Shimane Bank has fallen into a large deficit forecast and was forced to increase its capital by 10 billion yen
  - [japan] Proceeds from the sale of Bank of Japan ETFs will be used for growth investment as a source of funds for redem
  - [taiwan] Taiwan targets reusable rocket manufacturing in 2027 strategy to rival SpaceX
  - [korea] Why is SK Hynix stock crashing today?
  - [taiwan] Why is TSMC stock plunging today?
  - [taiwan] Taiwan dollar, Malaysian ringgit lead losses in Asian currencies
  - [taiwan] In line with international trade fishing and management, the Fisheries Department piloted the opening of expor
  - [china] Nvidia chips pile up in Hong Kong as China withholds import approval
  - [korea] Why is Samsung Electronics stock plunging today?
  - [china] CHINA PBOC CONDUCTS CNY226 BLN VIA O/N REVERSE REPO FRI
  - [japan] JGB Yields Fall as Stock Markets Drop Sharply — Market Talk
  - [china] On November 6, the central bank launched a 226 billion yuan overnight reverse repurchase operation.
  - [japan] Bank of Japan's additional ETF sales proceeds will lead to further growth through reinvestment - Prime Ministe
  - [japan] Japan to spend proceeds from BOJ’s ETF sales on growth areas, PM says
  - [taiwan] Taiwan's market fundamentals are good, deputy finance minister says
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7168 FRI VS 6.7156
  - [japan] Dollar holds, yen gains as equity rout saps risk appetite ahead of payrolls
  - [china] Chances are, US-China truce will be extended at Shenzhen Apec summit
  - [japan] Japan MOF To Auction Y3.1T Of TD-Bills Nov 13
  - [japan] BREAKING NEWS: Japan to use 10 bil. yen from reserve funds for cybersecurity measures
  - [taiwan] TSMC Plunges 9.8%; Foxconn Down 9.15%
  - [korea] Coway Co., Ltd. Overseas Revenue Rises 26.2% to KRW 591.8B

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
      "published_utc": "2026-11-06T04:22:43+00:00",
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

