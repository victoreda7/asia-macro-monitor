atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-10T19:32:44.408849+00:00
Total: 3000 manchetes

  🇯🇵 Japão          922
  🇨🇳 China          903
  🇹🇼 Taiwan         318
  🇰🇷 Coreia do Sul  857

## O que já está no feed (não repita)

  - [japan] SoftBank Group Corp. Stock 12‑Month Price Target Cut to JPY 8810.23, Implies 159% Upside
  - [china] NVIDIA Stocks Slide 4.43% as Report Alleges $7.5 Billion in Chips Reached China
  - [korea] Samsung Electronics Stocks Climb 4.74% as Chip Rebound Pushes Shares Near 200,000 Won
  - [korea] SK hynix Stocks Jump 6.69% as Seoul Chip Rally Lifts KOSPI 4.39%
  - [taiwan] TSMC Just Delivered the AI Growth Shock Wall Street Was Waiting For
  - [china] COMMENTARY: China's crude oil imports recover, fuel exports not so much
  - [china] Xin Yuan Enterprises Says PLH Enters Additional Irrevocable Undertaking For PLH Second IU Shares
  - [china] Shanghai Electric integrates industrial artificial intelligence into high-power gas turbine manufacturing and 
  - [taiwan] TSMC's October Sales Climb 14.7% Sequentially
  - [china] Microsoft urges US to reconsider potential import ban on Chinese optical transceivers: report
  - [china] China Everbright Says Court Orders Release Of Asset Preservation Measures Over Chongqing Yingli Real Estate In
  - [china] How Nvidia CEO’s troubles, US midterms may tighten China chip curbs: ‘adding fuel to fire’
  - [taiwan] TSMC earmarks up to $1bn to buy Anthropic and OpenAI shares
  - [taiwan] TSMC investirá até US$ 1 bilhão na Anthropic e na OpenAI
  - [taiwan] TSMC to invest up to $1 billion in Anthropic, OpenAI
  - [taiwan] TSMC and SoftBank Reveal a Chasm Between AI Winners and Losers — Barrons.com
  - [taiwan] Taiwan Semiconductor's October sales offer up 'strong start' to quarter, Wedbush says
  - [korea] Louis Vuitton hit by stock slump, stronger won in South Korea
  - [china] China's crude oil imports recover, fuel exports not so much: Russell
  - [japan] Honda upwardly revised its earnings forecast for this fiscal year due to weaker yen and increased sales of HVs
  - [taiwan] TSMC Board Approves Investment of Up to $500 Million in Each of Anthropic and OpenAI
  - [china] Puya Semiconductor (Shanghai) Plans To Seek Hong Kong Listing
  - [china] How does China get Nvidia chips despite restrictions?
  - [taiwan] Anthropic Private Placement With Google, Advanced Micro Devices, Broadcom, Micron Tech, Microsoft, Nvidia, TSM
  - [china] Nvidia CEO's alleged affair helped facilitate $7.5B in chip shipments to China: report
  - [china] Case involving Nvidia CEO and alleged spy favored US$7.5 billion in chips for China, says Information
  - [korea] 'Interest Rate Freeze' October Monetary Policy Committee Member "Adjusting the timing and speed of additional 
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
      "published_utc": "2026-11-10T19:32:44+00:00",
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

