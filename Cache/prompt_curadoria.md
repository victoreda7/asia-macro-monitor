atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-10T12:32:42.782624+00:00
Total: 3000 manchetes

  🇯🇵 Japão          926
  🇨🇳 China          903
  🇹🇼 Taiwan         311
  🇰🇷 Coreia do Sul  860

## O que já está no feed (não repita)

  - [japan] Honda upwardly revised its earnings forecast for this fiscal year due to weaker yen and increased sales of HVs
  - [taiwan] TSMC Board Approves Investment of Up to $500 Million in Each of Anthropic and OpenAI
  - [china] Puya Semiconductor (Shanghai) Plans To Seek Hong Kong Listing
  - [china] How does China get Nvidia chips despite restrictions?
  - [taiwan] Anthropic Private Placement With Google, Advanced Micro Devices, Broadcom, Micron Tech, Microsoft, Nvidia, TSM
  - [china] Nvidia CEO's alleged affair helped facilitate $7.5B in chip shipments to China: report
  - [china] Case involving Nvidia CEO and alleged spy favored US$7.5 billion in chips for China, says Information
  - [china] Nvidia CEO's affair with an alleged spy contributed to $7.5 billion worth of chip shipments to China, accordin
  - [china] China's iron ore imports hit lowest level in five months
  - [taiwan] TSMC Sales Jump Again -- Nvidia and Apple Orders Keep the AI Chip Boom Going
  - [japan] SoftBank Group interim financial results: 768 billion yen deficit due to change in DC plan
  - [china] The love affair of Nvidia's chief executive contributed to the shipment of chips worth US$7.5 billion to China
  - [china] Nvidia CEO's alleged affair aided $7.5 billion in chip shipments to China, Information reports
  - [china] China's soybean imports fall in October amid high stocks, weak crushing margins
  - [china] China's trade surplus surpasses $1trn as exports soar
  - [china] China's trade surplus exceeds $1 trillion, causing trade friction
  - [taiwan] The pressure on foreign capital's remittances has not subsided. The New Taiwan dollar nearly broke through 33 
  - [japan] Economy Watcher Survey: Decline for the first time in 6 months, impact on consumption due to rising prices
  - [china] Aluminium falls on higher Chinese exports and hopes for Middle East de-escalation
  - [china] China Logs Strong Export Growth In October
  - [korea] BOK chief becomes first Asian to chair BIS committee
  - [korea] BOK chief Shin Hyun-song tapped to lead BIS committee on payment systems
  - [china] China's Exports Could Face Headwinds in 2027 — Market Talk
  - [japan] SBG has a deficit of 768 billion yen in interim results
  - [japan] Yen Falls Amid Risk-On Mood
  - [china] China Chipmakers to Debut in HK in Test of Tech Stock Demand
  - [china] Stocks in China and Hong Kong close higher, supported by the appreciation of the technology sector
  - [japan] Softbank G falls into interim deficit
  - [china] Table: Yuan Ding Investment Corp. Oct Rev NT$1.99B Vs NT$1.78B
  - [korea] KRAFTON: 9M results set records as PUBG expansion and KRW 917.2bn in returns shape the outlook
  - [china] Alice Huang, Chinese businesswoman tied to Nvidia CEO, went from finance to chips
  - [china] China supera a marca de US$ 1 trilhão de superávit comercial em 10 meses
  - [taiwan] UK space firms eye Taiwan's chip and hardware ecosystem, global satellite production scales up
  - [korea] October Monetary Policy Committee unanimously freezes... Additional tightening is weighed against price pressu
  - [korea] [Exclusive] LG Chem has amassed 2.5 trillion won ... to build a semiconductor materials plant on a petrochemic
  - [china] China's Hesai Q3 revenue rises 34% as lidar shipments grow
  - [korea] Nexon axes eight projects in restructuring as S.Korean game sector tightens belt amid downturn
  - [china] ZAWYA: Can China’s zero-tariff programme offset the loss of Agoa for South African agriculture?
  - [china] Chinese investment in African manufacturing could change the world
  - [korea] Exports to large companies more than doubled in the third quarter of this year due to the semiconduc..

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
      "published_utc": "2026-11-10T12:32:42+00:00",
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

