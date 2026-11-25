atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-25T18:12:42.668731+00:00
Total: 3000 manchetes

  🇯🇵 Japão          932
  🇨🇳 China          1011
  🇹🇼 Taiwan         343
  🇰🇷 Coreia do Sul  714

## O que já está no feed (não repita)

  - [china] U.S. Proposes Additional 20% Tariff on China Ahead of Trade Truce Deadline
  - [china] BIO: Local manufacturing, China expansion and H2 FY27 innovation lead the update
  - [china] Trump rebuilds tariff wall with new duties on China, Japan and others
  - [china] Nvidia Sellers Seek New Buyers As US Curbs China AI Chip Access - CNBC
  - [china] Trump administration proposes new tariffs on 14 economies, including EU and China
  - [korea] SK hynix Stocks Sink 11.05% Despite 80% Operating Margin
  - [china] China Wan Tong Yuan (Holdings) Says No Progress On Construction Approvals For Cemetery JV Project
  - [japan] Japan Seeks Supply Chain Mandate For Chips, Other Critical Goods, Nikkei Reports
  - [japan] Japan seeks supply chain mandate for chips, other critical goods
  - [taiwan] Nvidia Chipmaker TSMC Sends $22.6 Billion AI Signal
  - [japan] Additional tariffs imposed on Japan and other countries due to rice overproduction, up to 15% in Japan includi
  - [korea] SK hynix stock trades down, here is why
  - [china] US Targets China, EU With New Tariffs Citing Overcapacity
  - [japan] Bitcoin investors urged to watch Japan's monetary policy as the BOJ tightens
  - [korea] The Bank of Korea decides the base interest rate today (26th)... Should I raise it to 3.25% per year?
  - [taiwan] Business sentiment cautious: TIER
  - [taiwan] Why is Taiwan Semiconductor Manufacturing stock plunging today?
  - [taiwan] TSMC Stocks Slide 6.65% as Taiwan Lands on US Tariff List
  - [korea] Samsung Electronics Stocks Plunge 9.87%, Market Value Drops Below 1,000 Trillion Won
  - [china] EU sets caps on Chinese, Korean hybrid car imports; impact on Hyundai, Kia seen limited
  - [china] Trump propõe novas tarifas contra China, UE e outros 12 parceiros
  - [china] US Targets China, EU, India With New Tariff Proposal — Greer Says China's 20% Rate To Be Added To Older Duties
  - [korea] LG Electronics Inc to divest 2% stake in Indian subsidiary
  - [korea] Korea to retain 15% tariff cap under new US tariff proposal
  - [china] Chinese AI firms face growing pressure from US chip rules - Information
  - [korea] Seoul Semiconductor Enables Beyond-OLED Picture Quality with LCD
  - [korea] Seoul Semiconductor Begins WICOP Pixel Mass Production
  - [china] Trump's China tariff math: 20%, times two if talks go sour
  - [china] USTR GREER Q&A/CNBC: USA OPPOSED TO CANADA'S PROPOSED TARIFF EXEMPTIONS FOR CHINA STEEL, ALUMINUM; BALANCING N
  - [china] USTR says latest US tariffs mostly align with trade deals with China, others
  - [china] USTR GREER Q&A/CNBC: PROPOSED SECTION 301 TARIFF RATE FOR CHINA SOMEWHAT ADDITIVE BUT PAIRED WITH PROPOSED EXE
  - [china] Could potential US tariffs put the US-China trade truce at risk?
  - [china] U.S. Set to Raise Tariffs on China, EU and Others — WSJ
  - [china] China Southern Airlines Subsidiary Orders 50 Boeing Aircraft For $7.4 Bln
  - [china] Trump admin proposes new tariffs on 14 trading partners, 20% on China - report
  - [china] US Targets China, EU With New Tariffs After Overcapacity Probe
  - [taiwan] TSMC asking for tax incentives at Texas fab suggests no AI slowdown: Wedbush
  - [china] Taxman can be China's next GDP growth engine
  - [china] The Logistics Report: China and Other Countries Face Higher U.S. Tariffs Over Industrial Subsidies — WSJ Newsl
  - [china] 800 billion + 500 billion! The central bank's "combination punch" protects liquidity

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
      "published_utc": "2026-11-25T18:12:42+00:00",
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

