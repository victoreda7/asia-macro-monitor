atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-13T11:52:43.924648+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1141
  🇨🇳 China          829
  🇹🇼 Taiwan         297
  🇰🇷 Coreia do Sul  733

## O que já está no feed (não repita)

  - [korea] Bank of Korea Gov. Shin Makes Case for Forward Guidance That Preserves Flexibility
  - [korea] IMF raises S. Korea's growth forecast to 3.3% amid chip supercycle
  - [korea] Bank of Korea chief says monetary policy to stay restrictive for now
  - [taiwan] Taiwan Semiconductor Manufacturing Company Limited expected to post earnings of $4.50 a share - Earnings Previ
  - [japan] Asia report: Nikkei, KOSPI post big losses as chipmakers drop
  - [korea] Hong Ra-hee to Gift 11.15 Million Samsung Electronics Shares to Lee Jae-yong
  - [china] E-House (China) Enterprise Says Grand Court Of Cayman Islands Sanctions Cayman Scheme
  - [korea] Kospi tumbles as chip rout deepens, briefly breaking below 6,000
  - [korea] Korean Won, New Taiwan Dollar Underperform Amid Chip-Stock Selloff — Market Talk
  - [korea] UnitedHealth, JPMorgan, Six Flags, SK Hynix, and More Stocks That Explain Today's Market — Barrons.com
  - [japan] "Cabinet approval rate" is also one of the indicators of government management
  - [japan] Support rate for each party: “Liberal Democratic Party” 35.3% “No support” 38.5% NHK public opinion poll
  - [japan] High approval rate for the city cabinet: 51%, 32% disapproval, NHK survey
  - [japan] Mapping the Market: 'Death cross' bodes more trouble for peso against resurgent yen
  - [japan] Rupee extends surge; Dollar consolidates near peaks ahead of inflation data
  - [korea] South Korea central bank to keep policy restrictive until inflation hits target, governor says
  - [china] IMF Cuts China Growth Forecasts for 2026 and 2027
  - [korea] KOSPI Slumps as U.S. AI Chip Panic Spreads — Barrons.com
  - [japan] Intervention Risk Limits Yen Falls Against Dollar — Market Talk
  - [japan] 88% of people expect prices to rise one year from now, Bank of Japan's September lifestyle awareness survey (K
  - [china] Chip selloff deepens amid AI trade fears, rising Chinese competition
  - [korea] The Ministry of Finance and Economy announced an administrative notice on the 13th to raise the pre
  - [japan] Former NHK Chairman Nobuo Inaba dies at age 75, former Bank of Japan board member (Jiji Press)
  - [japan] More than 80% expect prices to rise in five years' time Bank of Japan survey on lifestyle awareness (TV Asahi 
  - [korea] Commercial banks are offering non-face-to-face real estate mortgage loans for private businesses. Th..
  - [korea] [Photo] Export-import silver supports independence of isolated youth
  - [korea] Samsung Electronics chairman Lee to receive 2.6 trillion won worth of shares from mother, reports say
  - [japan] More than 80% predict that prices will rise in five years Bank of Japan's lifestyle awareness survey (TV Asahi
  - [china] Visa Wins Preliminary Approval for Yuan Card Clearing in China
  - [korea] Repeat & Correct: South Korea's Kospi Slumps on Selloff in Chip Stocks — Update
  - [china] Global chip selloff deepens as AI worries, China competition weigh
  - [japan] Former NHK chairman Nobuo Inaba dies at age 75, also serving as director of the Bank of Japan (Mainichi Shimbu
  - [taiwan] Taiwan panel makers enter semiconductor fight as structural challenges persist
  - [japan] Inflation expectations remain 86.5% higher in 5 years, highest level in 19 years due to Middle East impact, Ba
  - [japan] Inflation expectations remain 86.5% higher in 5 years; Middle East impact, highest level in 19 years; Bank of 
  - [taiwan] U.S. dollar closes sharply higher on Taipei forex market
  - [japan] Nobuo Inaba, former chairman of NHK and former director of the Bank of Japan, dies at age 75, announces lung c
  - [china] Cathie Wood warns of ‘vicious’ memory chip cycles as China adds capacity
  - [china] China's Export Rebate Cut to Cost NEV Makers 4,000-6,000 Yuan Per Vehicle — Market Talk
  - [korea] “We bought time by raising it before the US”... Bank of Korea plans to freeze base interest rate in October

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
      "published_utc": "2026-10-13T11:52:44+00:00",
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

