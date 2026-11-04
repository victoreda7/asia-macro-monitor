atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-04T22:52:43.008837+00:00
Total: 2960 manchetes

  🇯🇵 Japão          855
  🇨🇳 China          892
  🇹🇼 Taiwan         312
  🇰🇷 Coreia do Sul  901

## O que já está no feed (não repita)

  - [china] Fortescue to Swap Bond Issue Proceeds Into Offshore Yuan
  - [japan] Consumption tax reduction bill will be passed by the ruling party in the House of Representatives tomorrow, wh
  - [japan] There is a blind spot in the argument that the yen appreciates due to speculative yen buying...Which is more v
  - [japan] Franc, Yen Emerge as FX Winners as US Midterms Weaken Dollar
  - [china] Europe to invest €525 million in chip startups to catch up with US and China
  - [china] Canada, China Extend Tariff Deal, Aim to Boost Canadian Exports
  - [china] Nvidia's China Customers Face a Stunning 99% Chip Shortfall
  - [taiwan] Taiwan Weighs Tighter Controls on Chip Exports to Chinese Mainland
  - [korea] Micron, SK Hynix e SanDisk caem: por que vitória democrata no Texas assusta investidores
  - [china] China pledges to reduce trade tensions with Canada
  - [china] Shanghai Fosun Pharma Subsidiary Initiates Phase Iii Trial Of Fxs6837 Capsules For Pnh
  - [china] The central bank will carry out 300 billion yuan of buyout reverse repurchase, shrinking the amount by 200 bil
  - [japan] IHI: Record Q2 profit drives higher FY2026 guidance and a JPY 25 dividend forecast
  - [japan] Cabbage retail price approximately 70% higher than normal
  - [china] The central bank will launch a 300 billion yuan buyout reverse repurchase operation
  - [china] MORE U.S. SEPT TRADE: CHINA DEFICIT $17.9 BILLION VS $16.4 BILLION IN AUGUST
  - [china] Regarding the U.S.-China-Russia summit meeting, China's Ministry of Foreign Affairs "communicates with relevan
  - [japan] Ministry of Finance ``In principle, raise the burden of medical expenses for people over 70 to 30%'' at the Fi
  - [china] The People's Bank of China will scale back its volume and carry out a 300 billion yuan buyout reverse repurcha
  - [china] Central Bank: Launch a 300 billion yuan buyout reverse repurchase operation on November 5, with a period of 3 
  - [china] The foreign exchange reserve ratio was raised for the first time in the past five years! The central bank rare
  - [china] The central bank announced that it will carry out a 300 billion yuan buyout reverse repurchase operation
  - [japan] House of Representatives Finance and Financial Affairs Committee Consumption tax reduction bill Ruling parties
  - [china] The central bank will launch a 300 billion yuan buyout reverse repurchase operation - China Daily
  - [japan] Yen up, stocks down in Tokyo as Japan digests midterms | NHK WORLD-JAPAN News
  - [japan] Yen up, stocks down in Tokyo as Japan digests midterms
  - [china] Chinese exporters see respite as Beijing curbs yuan rise amid looming record surplus
  - [china] Chinese exporters see respite as Beijing curbs yuan rise amid record surplus
  - [japan] ``You can just drop in and have a casual time'' at the former Bank of Japan Kanazawa branch, with many request
  - [china] Chinese chipmaker YMTC puts IPO on hold as weaker markets weigh, sources say
  - [japan] National Governors Association requests correction of uneven distribution of taxes, etc. ahead of tax reform d
  - [china] What signal does the central bank send out by reducing supply and continuing to buy out reverse repurchases?
  - [taiwan] Exporters | Keyword News
  - [china] The central bank raised the foreign exchange deposit reserve ratio for the first time in the past five years
  - [japan] ``We should enter into a full-fledged discussion about the future image'' of the former Bank of Japan Kanazawa
  - [taiwan] Mediatek Shahriari to strengthen collaboration with key supply chain partners including TSMC
  - [taiwan] Exporters sell foreign exchange and foreign capital remittances compete, the New Taiwan dollar closes down 6.1
  - [china] Central Bank: It will launch a 300 billion yuan buyout reverse repurchase operation on November 5 with a perio
  - [china] Central Bank: From November 15, increase the reserve requirement ratio of foreign exchange deposits of financi
  - [japan] Department stores announce lucky bags in anticipation of rising prices and consumption tax cuts

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
      "published_utc": "2026-11-04T22:52:43+00:00",
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

