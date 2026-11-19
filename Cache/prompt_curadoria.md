atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-19T11:33:11.150408+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1018
  🇨🇳 China          896
  🇹🇼 Taiwan         318
  🇰🇷 Coreia do Sul  768

## O que já está no feed (não repita)

  - [china] Trump suggests Nvidia's Blackwell chips could go to China later
  - [china] Indonesia defends a sinking rupiah as China reins in a rising yuan - IntelliNews Lambda
  - [china] China, Rússia e EUA planejam ampliar oferta de petróleo refinado e reafirmam importância de fluxos energéticos
  - [taiwan] Xi tells Trump to 'do right thing' on Taiwan as trade truce remains in flux
  - [china] Analysis: Nvidia CEO’s Exit, U.S. Chip Rules Leave China’s Tech Giants Reeling
  - [taiwan] TSMC And Samsung Suspend Some Chip Shipments To Chinese Customers - FT
  - [japan] Japan Tobacco to book 1.38 tril. yen loss over Russia asset seizure
  - [taiwan] Taiwan hopes to sign trade deal with Canada soon after Carney's remarks
  - [japan] In France, Le Pen's National Union unexpectedly emphasizes fiscal discipline...What will happen between the fa
  - [taiwan] Taiwan unlikely to be Trump-Xi-Putin topic 'from what we know': MAC
  - [china] Trump begins historic trilateral talks with Xi, Putin in China
  - [china] China's Moonshot AI Scraps $150 Million Deal To Access Nvidia Chips In Indonesia - The Information
  - [japan] Japan's Takaichi criticizes 'arbitrary' export curbs in brief China visit
  - [japan] Finance Minister Katayama lower income limit for support grants: “Consider annual income of around 560,000 yen
  - [korea] Inktec To Divest Real Estate Worth 63 Billion Won
  - [japan] Next fiscal year's tax reform: LDP tax review begins discussion; issues include correction of tax revenue disp
  - [china] Chinese Steel Imports Put Pressure On India’s Capacity Expansion
  - [korea] Prices and growth rise together... Will the Bank of Korea further increase the base interest rate on the 26th?
  - [korea] How semiconductors powered South Korea’s $1tr export milestone
  - [china] [Breaking News] Did they exchange opinions on trade, AI, etc. at the US-China summit meeting?
  - [taiwan] Nvidia doubles down on Taiwan supply chain as AI squeezes substrate and OSAT capacity
  - [korea] "Claude" developer Antropics broke through weak technology stocks to achieve the largest initial pub..
  - [china] HAUTO: Strong Chinese exports offset disruption as capacity tightened and Q4 EBITDA was expected to improve
  - [korea] One 10-Kilogram Box Worth 1 Billion Won ... Semiconductors Pack a 5,000-Pyeong Warehouse
  - [china] NVDA, INTC Stocks Ease Post 5-Day Rout: After Meeting Xi Jinping, Trump Says Nvidia Blackwell Chips Could Reac
  - [japan] Defense spending "isn't just about the amount" Funding sources "consider fiscal sustainability" Prime Minister
  - [korea] LG Display cancels 3 trillion won investment plan on OLED production facility
  - [korea] Boston Dynamics to test Atlas humanoid robots at GlobalFoundries chip plants
  - [korea] South Korea’s Exports Top $1 Trillion for First Time on AI Boom
  - [korea] ANT Stock’s Debut Could Be A Blockbuster – But SpaceX And SK Hynix History Shows Why The First-Day Pop Isn’t E
  - [taiwan] Taiwan Tightens Short Selling Curbs to Support Stock Market
  - [korea] AI boom boosts semiconductors, South Korea's exports exceed US$1 trillion for the first time, and is expected 
  - [korea] The last Bank of Korea Monetary Policy Committee D-7 of the year... Interest rate hike weighs on inflation and
  - [korea] Korean Drama Producers Likely to Benefit From China Trade Talks — Market Talk
  - [korea] South Korean shares end higher as country joins $1 trillion export club
  - [taiwan] Wave of sales in Taiwan leads Asian shares to the lowest price in seven months; forex market remains cautious 
  - [korea] [Kim Yong-hoon’s Column] The mismatch between Korea-US monetary policies
  - [korea] South Korea Is Fourth Country to Hit $1 Trillion in Annual Exports, Trade Ministry Says
  - [korea] South Korea rides AI boom to new height as exports hit $1 trillion
  - [japan] Tokio Marine Holdings, Inc. - To Buy Back Up To 9.6% Of Shares Worth 280 Billion Yen

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
      "published_utc": "2026-11-19T11:33:11+00:00",
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

