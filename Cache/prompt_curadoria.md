atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-28T06:22:41.000755+00:00
Total: 3000 manchetes

  🇯🇵 Japão          958
  🇨🇳 China          969
  🇹🇼 Taiwan         337
  🇰🇷 Coreia do Sul  736

## O que já está no feed (não repita)

  - [china] China’s import logistics demand falls 0.6% in January-October
  - [china] China Import Logistics Fell 0.6% in January-October, Xinhua Says
  - [japan] Bank of Japan will postpone interest rate hike in December due to falling stock prices Focus on Governor Ueda'
  - [japan] 2026 Japanese Stock Summary and 2027 Outlook: Next steps influenced by “Bank of Japan interest rate hike” and 
  - [japan] Japan to scrutinize anime, game funding as budget requests surge
  - [japan] What is the "unexpected asset" that a former Bank of Japan investment professional is currently paying attenti
  - [japan] Why did “Kappa Sushi” fall into the red?
  - [korea] Samsung revamps chip division to sharpen its AI edge
  - [japan] Tokyo leads world in office rent, price growth as employers vie for prime space
  - [taiwan] Semiconductor competition between Taiwan and South Korea extends to the advanced packaging field! Samsung, TSM
  - [japan] Behind the Tamahome fraudulent billing issue is a "blind spot" in insurance industry regulation, and there is 
  - [japan] 505 yen lunch box excluding tax: ``505 yen if you take it home, 550 yen if you eat it inside'' Unable to shake
  - [japan] The consumer price index (excluding fresh food) in Tokyo's wards increased by 2.9%, expanding due to the end o
  - [china] Lithium Price Outlook as Sellers Target 80,000 Yuan After Failed Recovery
  - [japan] The cost was surprisingly high... The true nature of the "ominous dissonance" between the Liberal Democratic P
  - [taiwan] TSMC Stocks Climb 1.84% as U.S. Tariff Proposal Leaves Chips Off the List
  - [korea] SK hynix Stocks Jump 5.41% as 100 Trillion Won Payout Plan Sinks In
  - [korea] Samsung Electronics Stocks Jump 4.55% as Seoul Rallies on Stabilization Hopes
  - [japan] NIPPON STEEL CORP. Stock 12‑Month Price Target Raised to JPY 753.33, Implies 11% Upside
  - [china] Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang
  - [china] China's auto exports to rise 50% amid intensifying competition at home
  - [japan] Japan Week Ahead: October Factory Output, Retail Sales Likely to Show Solid Start to Final Quarter of 2026
  - [china] Nvidia, CoreWeave Face New U.S. Restrictions on China AI Chip Access
  - [china] The Week Ahead (Nov. 30-Dec. 6): Nasdaq Extends Trading, EU Caps Chinese Hybrid Imports
  - [korea] Bank of Korea raises base interest rate to 3.25%... Next year's growth rate in Korea is expected to be unprece
  - [china] 800 billion MLF + 500 billion reverse repurchase, the central bank's "combination punch" accurately protects l
  - [korea] Midday Need to Know: Brazil stocks surge, SK Hynix boosts buybacks & more
  - [japan] Japan's data center subsidies to weigh local impact as backlash grows
  - [china] German Companies in China Adapt to Persistent Price Pressure
  - [china] EU to Probe China and Singapore Sustainable Aviation Fuel Imports
  - [korea] SK Hynix increases buybacks following recent share skid: report
  - [korea] Micron, SK Hynix and SanDisk Stocks Rise — What's the Verdict on Demand?
  - [japan] Liberal Democratic Party Vice President Aso, Foreign Minister Motegi and others meet to pass consumption tax r
  - [china] Aluminum Corporation Of China Says Guinea Subsidiary Signs EPC Contract With China Aluminum International Engi
  - [japan] School bullying in Japan hit record high in fiscal 2025
  - [china] EU weighs tighter export controls to prevent battery waste going to China
  - [china] China's central bank promises flexible and effective use of monetary policy tools
  - [korea] Daesang Corporation Seaweed Sales Rose ~30% to KRW 200.0B
  - [korea] Micron, SK Hynix, Samsung in focus as GF cuts DRAM prices for 2027
  - [china] Nvidia Blackwell chips found at China data center linked to Alice Huang: report

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
      "published_utc": "2026-11-28T06:22:41+00:00",
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

