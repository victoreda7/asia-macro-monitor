atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-04T03:02:44.218982+00:00
Total: 2867 manchetes

  🇯🇵 Japão          827
  🇨🇳 China          854
  🇹🇼 Taiwan         303
  🇰🇷 Coreia do Sul  883

## O que já está no feed (não repita)

  - [korea] BOK Financial raises quarterly dividend by 23.8% to $0.78/share
  - [china] China's PMI Data Show Economic Activity Lost Momentum in Oct — Market Talk
  - [china] China's PBOC Lowers Relending Rate for Stock Buybacks
  - [japan] House of Representatives Finance and Financial Affairs Committee Consumption tax reduction bill Ruling parties
  - [korea] South Korean won climbs, Taiwan dollar lags among mixed Asian FX
  - [china] China Services PMI Ebbs In October - Caixin
  - [china] CHINA PBOC CONDUCTS CNY257.5 BLN VIA O/N REVERSE REPO WEDS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7180 WEDS VS 6.7150
  - [china] China Steps in to Boost Stocks, Cool Off Yuan
  - [korea] Samsung Electronics, SK hynix rally on Wall Street chip rebound
  - [japan] Stock prices drop by more than 2,000 yen at one point; sell orders spread for stocks such as semiconductors
  - [china] How to understand the central bank’s increase in the foreign exchange deposit reserve ratio?
  - [china] The central bank launched a 257.5 billion yuan overnight reverse repurchase operation today
  - [china] China PBOC Pledges to Fully Meet Future Re-Lending Demand
  - [china] China PBOC: Banks Have Applied for Relending Quotas Exceeding 200 Billion Yuan
  - [china] China PBOC: The 1-Year Relending Facility Supports 26 Major Banks
  - [china] China PBOC: It's Ramping Up Relending Policy for Stock Buybacks
  - [china] What are the implications of the central bank raising the foreign exchange deposit reserve ratio for the first
  - [china] China PBOC Says It Cuts Relending Rate for Stock Buybacks to 1%
  - [japan] The fiscal burden is almost the same as "zero consumption tax," but the Ministry of Finance's "sneaky true int
  - [japan] Monetary base fell 13.6% year-on-year in October, rate of decline slowing - Bank of Japan (Reuters)
  - [japan] The Bank of Japan decides to maintain the status quo of monetary policy (Hiroyuki Kubota) - Expert
  - [korea] [Analysis] Despite the slowdown in prices in October, interest rates are expected to increase in November
  - [japan] Bank of Japan Accounts (October 31)
  - [korea] Price 2.8%, growth rate 1.0%... Bank of Korea, base interest rate could be raised to 3.25% in November
  - [taiwan] Bosch creates semiconductor division to expand in robotics, external chipmaking
  - [china] CXMT Plans To Buy Back Company Shares Worth 2.5-5 Bln Yuan
  - [china] Changgao Electric's Units Win Bids In Equipment Projects Worth 230.4 Mln Yuan
  - [korea] South Korea FX Reserves Hit 4-Year High in October
  - [china] Financial News | The central bank raised the foreign exchange reserve ratio, and the RMB depreciated by more t
  - [korea] SK Hynix's New York chip plans face obstacles due to US restrictions on China, sources say
  - [china] China's Temu, JD.com revamp business models amid tariff headwinds
  - [china] US China Export Controls Threaten SK Hynix's Multi-Billion-Dollar New York Chip Expansion Plan
  - [korea] Foreign reserves rebound in Oct. on foreign currency deposits
  - [japan] Problems that arise in the workplace due to the legal employment rate for people with disabilities increasing 
  - [japan] In France, where government income far exceeds that of Japan, why are the people dissatisfied? The limits of a
  - [japan] Coordination between ruling and opposition parties over voting timing for consumption tax reduction bill begin
  - [korea] SK Hynix in spotlight as Commerce Dept. holds up Chinese equipment plans: report
  - [japan] USD/JPY Faces a 160 Ceiling as December Rate Hikes Threaten Yen Carry Trades
  - [korea] SK Hynix's plans to make chips in New York face obstacles due to US restrictions on China, sources say

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
      "published_utc": "2026-11-04T03:02:44+00:00",
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

