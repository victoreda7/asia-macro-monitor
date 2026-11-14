atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-14T08:25:28.539348+00:00
Total: 3000 manchetes

  🇯🇵 Japão          998
  🇨🇳 China          867
  🇹🇼 Taiwan         312
  🇰🇷 Coreia do Sul  823

## O que já está no feed (não repita)

  - [china] China, US discuss tariffs, farm trade at first trade council meeting
  - [china] Blacklisted Chinese university reportedly purchased Nvidia H200s despite export restrictions
  - [japan] National Secretary-General Shinba Consumption tax reduction bill Request acceptance of resident tax reduction
  - [japan] JAPAN MATERIAL: Q2 sales rose 20.4%, while operating profit grew 41.0% on semiconductor-fab demand
  - [china] The central bank takes action! 200 billion yuan buyout reverse repurchase is coming
  - [taiwan] TSMC gets record NT$167.6 billion in aid from U.S., Japan, Germany, China
  - [china] China's BYD clears import hurdle, looks to accelerate India push
  - [korea] The banking sector is resuming a series of mortgage insurance subscriptions, which have been restric..
  - [china] The central bank reduced its supply and continued the 6-month buyout reverse repurchase agency: curbing the do
  - [china] Indian solar manufacturers look to Germany as China proposes curbs on technology exports
  - [japan] Shock of consideration of ``1.5 trillion yen'' compassionate budget》 60 trillion yen defense budget proposal i
  - [japan] “Gindako” turns the corner: Why does it fall into the red?
  - [china] A-share headlines: Financial data released in October, the central bank's reverse repurchase volume is reduced
  - [japan] What I found interesting about the main opinions from the Bank of Japan's monetary policy meeting (Hiroyuki Ku
  - [china] The central bank will launch a 200 billion yuan buyout reverse repurchase operation
  - [japan] Defense budget, 60 trillion yen target, 5-year total, finance, defense offensive and defense Prime Minister Ta
  - [china] Trump to hold summit with Xi, Putin in Shenzhen on Thursday, NY Post reports
  - [japan] US Treasury bought nearly $500mn in yen during joint July forex intervention
  - [china] EU’s fixation on Chinese subsidies masks its own structural stagnation
  - [japan] "Anthropic's malicious IPO" + "NVIDIA CEO Jensen Huang scandal"...The collapse of the AI/semiconductor bubble 
  - [japan] Commerce Secretary Lutnick's responsibility for export of Nvidia's advanced semiconductors emerges
  - [japan] Questioning the pros and cons of the Takaichi administration's huge fiscal spending...A former general contrac
  - [china] US-China truce masks rising tensions ahead of Xi-Trump redux at APEC
  - [taiwan] What is the impact of the downfall of Nvidia's CEO, a "Taiwanese hero"? What is the reality of the "de-fan dep
  - [japan] U.S. wholesale inflation hits 4-year high in October, market bets on Fed rate hike in December | International
  - [china] Nvidia scandal sparks Washington blame game over China chip exports
  - [korea] Samsung Electronics Stocks Move Lower as Nvidia CEO Exit Tests AI Memory Rally
  - [china] Nvidia faces new $3.2 billion China chip problem
  - [korea] Why did Micron, SK Hynix and SanDisk shares fall on Friday?
  - [japan] GlobalFoundries breaks ground on first new semiconductor fab under landmark U.S.-Japan initiative
  - [korea] Applied Materials, Diodes, Marvell Technology, Applied Optoelectronics, and SK hynix stocks trade down, what y
  - [china] Update: China's yuan loans grow 11.42 trln yuan in first 10 months
  - [taiwan] Align director, wife charged over suspicious chips
  - [china] 1st LD-Writethru: China's yuan loans grow 11.42 trln yuan in first 10 months
  - [korea] Modine Manufacturing jumps 30% on reports of acquisition talks with Samsung
  - [china] China's yuan loans grow 11.42 trln yuan in first 10 months
  - [china] China’s access to some Nvidia chips in doubt as curbs gain traction in US Congress
  - [korea] Polen Global Growth adds Seagate, AMD And SK Hynix, trims Nvidia and Broadcom among Q3 moves
  - [china] The People's Bank of China will scale back its operations and carry out a 200 billion yuan six-month buyout re
  - [china] Alice Huang-Linked Firm Procured Banned Nvidia Chips in China

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
      "published_utc": "2026-11-14T08:25:28+00:00",
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

