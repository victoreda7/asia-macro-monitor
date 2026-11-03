atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-03T21:52:45.035271+00:00
Total: 2838 manchetes

  🇯🇵 Japão          821
  🇨🇳 China          838
  🇹🇼 Taiwan         302
  🇰🇷 Coreia do Sul  877

## O que já está no feed (não repita)

  - [china] China's Temu, JD.com revamp business models amid tariff headwinds
  - [china] China Steps in to Boost Stocks, Cool Off Yuan
  - [china] US China Export Controls Threaten SK Hynix's Multi-Billion-Dollar New York Chip Expansion Plan
  - [korea] Foreign reserves rebound in Oct. on foreign currency deposits
  - [japan] Problems that arise in the workplace due to the legal employment rate for people with disabilities increasing 
  - [japan] In France, where government income far exceeds that of Japan, why are the people dissatisfied? The limits of a
  - [japan] Coordination between ruling and opposition parties over voting timing for consumption tax reduction bill begin
  - [korea] SK Hynix in spotlight as Commerce Dept. holds up Chinese equipment plans: report
  - [korea] SK Hynix's plans to make chips in New York face obstacles due to US restrictions on China, sources say
  - [japan] USD/JPY Faces a 160 Ceiling as December Rate Hikes Threaten Yen Carry Trades
  - [korea] SK Hynix’s US expansion plans hit snag over China license delays - report
  - [korea] SK Hynix’s New York chip plans hit snag over US restrictions on China, sources say
  - [korea] Samsung Secures AMD, Nvidia Orders for New Texas Chip Plant
  - [china] COMMENTARY: China's steady thermal coal imports mask supply shifts amid El Nino
  - [china] Raising the foreign exchange deposit reserve ratio, why did the central bank take action to stabilize the exch
  - [china] The central bank raised the foreign exchange deposit reserve ratio by 2 percentage points
  - [korea] AMD Stock Jumps on Major Samsung Chip Manufacturing Breakthrough
  - [korea] Why did Micron, SK Hynix and SanDisk shares rise on Tuesday?
  - [korea] Why are Micron, SK Hynix, and SanDisk stocks rising on Tuesday?
  - [china] China's State Council announces removal of officials
  - [china] Global central banks purchased gold at the fastest pace in 2 years in the third quarter, China topped the list
  - [korea] Samsung to make chip parts for AMD, Nvidia at Texas plant: report
  - [korea] SK hynix Secures Board Nomination Rights at Penguin Solutions with 9.1% Stake
  - [china] Dollar drifts on Mideast, midterm risks; Aussie and yuan dip
  - [china] China's steady thermal coal imports mask supply shifts amid El Nino: Russell
  - [china] The central bank will raise the foreign exchange deposit reserve ratio of financial institutions. What signal 
  - [china] After raising the foreign exchange deposit reserve ratio, why did the central bank take action to stabilize th
  - [korea] AMD, Nvidia Could Join Tesla On Samsung’s Texas Chip Plant Customer List: Report
  - [japan] What midterms might mean for the yen
  - [china] The People's Bank of China decides to raise the foreign exchange deposit reserve ratio of financial institutio
  - [china] What does the central bank mean by raising the foreign exchange reserve requirement ratio for the first time i
  - [china] China, Oman sign currency swap agreement
  - [china] Jiemian Evening News | The central bank raised the foreign exchange deposit reserve ratio by 2 percentage poin
  - [china] Sales of Tesla electric vehicles made in China increase 10.3% in October year-on-year
  - [korea] Samsung will manufacture chip components from AMD and Nvidia at its second factory in Texas, according to a re
  - [korea] Samsung to make AMD, Nvidia chip parts at second Texas plant, Maeil Business reports
  - [china] Zhejiang Construction Investment Group Says Unit's Consortium Wins 1.5 Billion Yuan Bid
  - [china] First time in nearly five years! The central bank raised the foreign exchange deposit reserve ratio, and the o
  - [korea] HYBE Q3 2026 slides: record revenue hits KRW 1.5 trillion on BTS tour
  - [china] China-made Tesla electric vehicle sales rose 10.3% year-on-year in October

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
      "published_utc": "2026-11-03T21:52:45+00:00",
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

