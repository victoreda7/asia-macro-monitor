atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-08T04:42:45.922403+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1241
  🇨🇳 China          784
  🇹🇼 Taiwan         268
  🇰🇷 Coreia do Sul  707

## O que já está no feed (não repita)

  - [korea] Samsung Electronics Co., Ltd. Stock 12‑Month Price Target Cut to KRW 486160.09, Implies 81% Upside
  - [china] The first day after the holiday! The central bank took action and launched a 1.2 trillion yuan buyout reverse 
  - [korea] Why is SK Hynix stock gaining today?
  - [japan] Asian currencies rangebound as dollar holds near 18-month high, yen slips
  - [taiwan] AUO subsidiary Darwin shifts toward high-end manufacturing, explores CPO and semiconductor opportunities
  - [japan] Prime Minister: “Consumption tax cut will not affect social security revenue” Thoughts on Yano Farmer Inherita
  - [china] Yuan steady despite dollar strength during China's Golden Week holiday
  - [korea] S. Korea says no confirmed fuel exports to Russia, vows strict enforcement of export controls
  - [japan] Stock prices fall, profit-taking selling in some semiconductor-related stocks
  - [china] As China and the EU begin crunch trade talks, optimism is in short supply
  - [japan] Yen Holds Steady After Strong Data
  - [china] The central bank’s 7-day reverse repurchase operation volume on October 8 was zero
  - [taiwan] TSMC Could Deliver Over 40% Revenue Growth into 2027 — Market Talk
  - [korea] Seoul shares extend losses late Thurs. morning amid inflation worries
  - [japan] PGIM: French Bond Selloff Could Bring Japanese Money Home and Support the Yen
  - [japan] "A tremendous shock and blow"...The risk of Trump's "diesel oil export ban" smoldering ahead of the midterm el
  - [korea] ‘Three major conditions’ for preemptive interest rate increase proposed by the Bank of Korea
  - [china] The central bank will launch a 1.2 trillion yuan buyout reverse repurchase operation
  - [korea] Samsung, SK hynix face investor test as buybacks wind down
  - [china] Nissan Says It Will Start Sales Of China-Made Frontier Pro Pickup Truck In Mexico In October, Highlighting Chi
  - [korea] Budget minister calls for 'virtuous cycle' of spending, growth and tax revenue
  - [japan] Japan futures fall as yen firms, Tokyo equities slip
  - [china] Yuan Consolidates as Market Participants Assess PBOC's Yuan Fixing Vs. Dollar — Market Talk
  - [china] The central bank will launch a 1.2 trillion yuan buyout reverse repurchase operation - News
  - [japan] Tokyo Financial Exchange launches new BOJ rate futures as policy shifts accelerate
  - [japan] Tokyo Gas acquires Indonesian LNG developer for island network
  - [china] CHINA PBOC CONDUCTS CNY606 BLN VIA O/N REVERSE REPO THURS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7367 THURS VS 6.7351
  - [china] The central bank will launch a 1.2 trillion yuan buyout reverse repurchase operation-News Center
  - [china] Central Bank: Launching 606 billion overnight reverse repos on October 8
  - [japan] Asian stocks slip as oil, inflation worries and tech selloff weigh heavy; Nikkei down 700 points
  - [china] [The Central Bank will launch a 1.2 trillion yuan buyout reverse repurchase operation] In order to maintain su
  - [china] The central bank will carry out a 1.2 trillion yuan buyout reverse repurchase operation_7x24 news_Sina Finance
  - [china] Central Bank: The volume of 7-day reverse repurchase operations on October 8, 2026 was zero
  - [china] Central Bank: The volume of 7-day reverse repurchase operations on October 8 was zero
  - [china] The central bank launched a 606 billion yuan overnight reverse repurchase operation today
  - [korea] South Korea's August Current Account Surplus Hits Second-Highest Level
  - [china] The central bank's reverse repurchase is net withdrawn today..._7x24 News_Sina Finance
  - [china] The central bank's reverse repurchases net withdrawn 608.5 billion yuan today.
  - [china] Central Bank of China: Based on the needs of primary dealers in open market business, the volume of 7-day reve

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
      "published_utc": "2026-10-08T04:42:46+00:00",
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

