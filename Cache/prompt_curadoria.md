atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-17T14:12:41.979900+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1027
  🇨🇳 China          901
  🇹🇼 Taiwan         310
  🇰🇷 Coreia do Sul  762

## O que já está no feed (não repita)

  - [japan] Yen Rises Amid Fx Intervention Risks
  - [china] China's Ministry of Foreign Affairs opposes new U.S. rules for exporting advanced semiconductors
  - [korea] Higher interest rates, sluggish consumer spending take toll on Korea’s credit card firms
  - [china] Central Bank Announcement: Launching 714 billion yuan overnight reverse repurchase operation on November 17
  - [korea] South Korean grape exports jump 85% as Taiwan leads sales
  - [japan] Will the US-North Korea summit happen? NW9 Hirouchi caster asks experts
  - [china] China resumes storing crude oil, giving it fuel export options: Russell
  - [china] Chinese copper import premium jumps 21% to record peak amid low stocks
  - [korea] Apple nears a rare long-term DRAM supply deal with Samsung Electronics: report
  - [korea] Micron, Sandisk, SK Hynix in focus as GF Securities cuts NAND price forecast, sees glut
  - [china] Nvidia sets up board committee to oversee national security, export control risks amid China scrutiny
  - [china] Forvia Hella Wins Three Series-Production Radar Orders From Leading Chinese Car Manufacturers
  - [japan] Yen Expected to Outperform in 2027, BofA Survey Says — Market Talk
  - [china] Hella - Forvia Hella Wins Series Production Orders For Radar From Leading Chinese Automotive Manufacturer
  - [taiwan] Foxconn plans to acquire Sony Semiconductor Solutions' automotive camera module business
  - [china] Walt Disney: Expect Growth in Global Guests to Continue in 1Q of Fiscal 2027, Despite Consumer Softness in Hon
  - [china] Walt Disney: Attendance at Hong Kong and Shanghai Parks Worsened During 4Q, and Expect This Pressure to Contin
  - [china] Nvidia Sends Stark Warning to Customers Over Chinese Access to Its AI Chips
  - [taiwan] Yushan Gold: Taiwan’s central bank has the conditions to raise interest rates by the end of the year and estim
  - [japan] Yen Rises Against Majors
  - [china] Canada, China extend tariff relief measures through 2028
  - [japan] Mapping the Market: Yen could weaken into danger zone for intervention
  - [korea] Citi expects South Korea rate hikes despite stock market decline
  - [china] US to curb China’s access to AI chips as Trump heads to Asia
  - [japan] Yomiuri: Effissimo Purchasing More Shares of Japanese Semiconductor-Related Stocks
  - [japan] Dollar scales new 19-month peak on hawkish Fed bets; Yen hemmed near 160
  - [taiwan] Foreign capital remittances and exporters' foreign exchange sales clashed. The New Taiwan dollar depreciated b
  - [china] APEC summit tomorrow, focus on US-China-Russia summit and Japan-China contacts
  - [taiwan] Foxconn says it will acquire Sony Semiconductor Solutions' automotive camera module business
  - [china] JSW Steel CEO flags Chinese exports, trade barriers as key challenges
  - [taiwan] The United States strictly controls the export of advanced AI chips: some orders may be delayed | Sankei
  - [taiwan] Taiex plunges amid AI concerns, suspected gov't intervention
  - [korea] Samsung and Apple near long-term DRAM supply agreement
  - [china] Shanghai Runda Medical Technology Plans Bond Issuance
  - [japan] House of Councilors Special Committee Confirms Second Question Asked for Prime Minister Takaichi's Attendance 
  - [japan] Yomiuri: Asics Aims for 1.5 Trillion Yen in Net Sales for 2029
  - [korea] [Counterattack of digital dollar hegemony] Strengthening dollar hegemony through financial innovation... Bank 
  - [japan] Local Finance Council “Take concrete steps through tax reform to correct uneven distribution of taxes”
  - [taiwan] New rules for US exports of AI chips to prevent transshipment Quanta and Wistron’s assessment will not be affe
  - [korea] Who sets the base interest rate and how?: A summary of the Monetary Policy Committee

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
      "published_utc": "2026-11-17T14:12:42+00:00",
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

