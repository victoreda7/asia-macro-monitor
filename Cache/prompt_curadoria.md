atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-02T03:32:42.458399+00:00
Total: 3000 manchetes

  🇯🇵 Japão          928
  🇨🇳 China          867
  🇹🇼 Taiwan         354
  🇰🇷 Coreia do Sul  851

## O que já está no feed (não repita)

  - [korea] South Korea’s manufacturing PMI slows to 8-month low in October
  - [china] China’s shift to new policy rate signals easier funding conditions
  - [china] China Longyuan Tariff Outlook Expected to Improve in 2027 — Market Talk
  - [china] The central bank launches 541 billion yuan overnight reverse repurchase operation
  - [japan] Japan manufacturing PMI slows to seven-month low in October By Investing.com
  - [japan] Japan manufacturing PMI slows to seven-month low in October
  - [taiwan] Taiwan PMI Shows Goods Producers' Supply-Chain Struggles — Market Talk
  - [china] China Longyuan Power Target Price Cut to HK$6.70 From HK$7.00 by Deutsche Bank >0916.HK
  - [japan] Yen Weakens Despite Verbal Warning
  - [japan] Is “Japan’s bankruptcy due to long-term interest rates” a lie? Yoichi Takahashi reveals misconceptions about “
  - [japan] Japan Manufacturing PMI Signals Decent Growth, Continued Cost Pressure — Market Talk
  - [korea] South Korea's Lee vows to make bold AI investment in record budget push
  - [china] PBoC Moves Toward Overnight Rate as Main Policy Anchor
  - [china] China Private Manufacturing Gauge Shows Steady Expansion in October — Update
  - [china] On November 2, the central bank launched a 541 billion yuan overnight reverse repurchase operation.
  - [taiwan] Rebuilding the American edge: How TSMC is driving US manufacturing and economic opportunity
  - [china] China lowers funding costs with shift to overnight policy rate
  - [korea] South Korean won, Taiwan dollar lead declines among Asian currencies
  - [korea] SK Square eyes record W4.3tr payout from SK hynix dividends
  - [korea] South Korean shares turn higher on dip buying after strong exports
  - [china] The central bank adjusts the reverse repurchase mechanism and carries out overnight operations with an interes
  - [china] The central bank adjusts the reverse repurchase mechanism to conduct overnight operations at an interest rate 
  - [china] China factory output grows at fastest pace in 6 months: RatingDog PMI
  - [taiwan] SPCX Stock Jumps Overnight: Musk Reportedly Revives TSMC Terafab Talks — Says Capex Efficiency Is ‘Greatly Und
  - [japan] MU, SNDK, DRAM Inch Higher Overnight After Mixed Week: Japan’s Kioxia Plunges After Cautious Memory Outlook
  - [china] China's Private Manufacturing Gauge Shows Steady Expansion in October
  - [china] China Manufacturing PMI Eases In September - S&P Global
  - [korea] DHL CEO sees Korea as winner in global supply chain shake-up
  - [china] China’s 5,000-Ton Digging Machines Are a Trade War Risk to India
  - [china] CHINA PBOC CONDUCTS CNY541 BLN VIA O/N REVERSE REPO MON
  - [japan] Mr. Shirouchi makes a cautious decision on overcoming deflation, with the Bank of Japan deciding to reach 2% i
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7146 MON VS 6.7138
  - [china] China Manufacturing PMI Beats Estimates
  - [china] China factory growth slows in October as export orders ease, private PMI shows
  - [japan] Japan Manufacturing Growth Confirmed at 7-Month Low
  - [japan] Bank of Japan says it's "generally consistent with 2%," and the hurdle to halting interest rate hikes has lowe
  - [korea] South Korean Shares Rebound on Record Exports
  - [japan] Japan MOF To Auction Y600.0B Of 30-Year Govt Bonds Nov 10
  - [japan] "The Bank of Japan has decided to maintain the status quo of monetary policy" Today's Bonds of the Cow and Bea
  - [china] The central bank launched a 541 billion yuan overnight reverse repurchase operation today

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
      "published_utc": "2026-11-02T03:32:42+00:00",
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

