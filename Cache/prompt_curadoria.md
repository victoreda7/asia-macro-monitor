atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-27T17:52:58.996907+00:00
Total: 3000 manchetes

  🇯🇵 Japão          945
  🇨🇳 China          972
  🇹🇼 Taiwan         340
  🇰🇷 Coreia do Sul  743

## O que já está no feed (não repita)

  - [china] Nvidia, CoreWeave Face New U.S. Restrictions on China AI Chip Access
  - [china] The Week Ahead (Nov. 30-Dec. 6): Nasdaq Extends Trading, EU Caps Chinese Hybrid Imports
  - [china] 800 billion MLF + 500 billion reverse repurchase, the central bank's "combination punch" accurately protects l
  - [korea] Midday Need to Know: Brazil stocks surge, SK Hynix boosts buybacks & more
  - [japan] Japan's data center subsidies to weigh local impact as backlash grows
  - [china] German Companies in China Adapt to Persistent Price Pressure
  - [korea] SK Hynix increases buybacks following recent share skid: report
  - [korea] Micron, SK Hynix and SanDisk Stocks Rise — What's the Verdict on Demand?
  - [china] Nvidia Blackwell Chips Turn Up at China Site Tied to Alice Huang
  - [japan] Liberal Democratic Party Vice President Aso, Foreign Minister Motegi and others meet to pass consumption tax r
  - [china] Aluminum Corporation Of China Says Guinea Subsidiary Signs EPC Contract With China Aluminum International Engi
  - [japan] School bullying in Japan hit record high in fiscal 2025
  - [china] EU weighs tighter export controls to prevent battery waste going to China
  - [korea] Samsung revamps chip division to sharpen its AI edge
  - [china] China's central bank promises flexible and effective use of monetary policy tools
  - [korea] Daesang Corporation Seaweed Sales Rose ~30% to KRW 200.0B
  - [korea] Micron, SK Hynix, Samsung in focus as GF cuts DRAM prices for 2027
  - [china] Nvidia Blackwell chips found at China data center linked to Alice Huang: report
  - [korea] SK hynix doubles daily buyback orders as shares slide
  - [china] Nvidia Blackwell chips found in Shanghai data center tied to Alice Huang
  - [china] China's central bank pledges flexible and effective use of monetary policy tools
  - [china] NVIDIA Blackwell chips surface at China site tied to Megaspeed - Bloomberg
  - [china] EU launches anti-dumping probe into China, Singapore sustainable aviation fuel imports
  - [japan] Electricity charges for December usage drop at 10 major companies due to resumption of government subsidies
  - [taiwan] Taiwan's 2026 GDP growth forecast raised to 13.28%, highest since 1978
  - [china] CMST Development Plans To Register 4 Billion Yuan Debt Financing Instruments
  - [korea] Why South Korea’s chip boom is now a US tariff trap as a US$350b pledge looms
  - [china] Zhifei Biological Products Says Manufacturing Registration Application For Semaglutide Injection For Weight Ma
  - [japan] Bank of Japan official says stablecoins need reserve rules to preserve ‘singleness of money’
  - [japan] House of Councilors consumption tax reduction bill ruling and opposition parties agree to hold question and an
  - [china] China State Construction Engineering Corp Secures Projects Totalling 14.6 Billion Yuan
  - [china] China's major stock indexes surge, chip shares rally
  - [china] Xiaocaiyuan International Holding Says It Resolved To Pay A Special Dividend Of RMB 0.4292 Per Share
  - [china] China central bank cuts subscription thresholds for big-denomination deposit products from March
  - [china] U.S. Tech Restrictions More Pressing Challenge to China Than Tariffs — Market Talk
  - [china] DSC partners with JAPANCARS to expand China’s used car exports
  - [taiwan] AI is still in short supply. The General Accounting Office estimates that exports will hit a new high of US$1 
  - [china] Kweichow Moutai To Distribute Cash Dividend Of 25.6 Yuan Per Share
  - [taiwan] Taiwan Lifts 2027 Growth Outlook Despite Mounting AI Concern
  - [china] Guangdong Songfa Ceramics' Subsidiary To Invest About 17 Billion Yuan In Project

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
      "published_utc": "2026-11-27T17:52:59+00:00",
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

