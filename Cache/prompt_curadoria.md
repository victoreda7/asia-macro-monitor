atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-15T18:45:23.303107+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1003
  🇨🇳 China          867
  🇹🇼 Taiwan         309
  🇰🇷 Coreia do Sul  821

## O que já está no feed (não repita)

  - [taiwan] Nvidia defends employee in Taiwan AI chip smuggling case
  - [taiwan] Nvidia Sought Taipei’s Help Over Employee’s Chip Smuggling Case
  - [japan] Over 63% skeptical about PM's tax cut to help fight inflation
  - [china] Nvidia Partner Megaspeed Breaks Silence on Alice Huang, Launches Probe Into China Chip Supply Links
  - [japan] [Breaking news] Ehime prefecture gubernatorial election exit poll results
  - [japan] Matsuyama mayoral election vote counting and exit poll election information is here [Breaking news]
  - [japan] [Breaking news] Matsuyama mayoral election exit poll results
  - [korea] Will the Bank of Korea raise its base interest rate on the 26th? Tensions rise over the possibility of a ‘big 
  - [china] APEC summit in Shenzhen, Indonesia monetary policy, ASEAN diplomacy
  - [japan] [Breaking news] Fukuoka mayoral election exit poll results
  - [china] Increase to 6%! The central bank’s major adjustments officially take effect today
  - [china] The central bank's "lock-up and release of short-term measures" stabilized funding expectations, with a net wi
  - [japan] Fukuoka mayoral election vote counting and exit poll election information is here [Breaking news]
  - [japan] Ehime Prefecture gubernatorial election vote counting and exit poll election information is here [Breaking new
  - [china] China’s auto export boom lifts Hyundai Glovis to record profit
  - [china] The central bank will raise the foreign exchange deposit reserve ratio by 2 percentage points from November 15
  - [japan] BREAKING NEWS: 68.6% worried about Japan's fiscal health due to consumption tax cut
  - [china] Central Bank: The foreign exchange deposit reserve ratio of financial institutions will be increased to 6% sta
  - [china] The central bank’s major adjustments are implemented! RMB, new signal
  - [china] After the Huang Renxun scandal, the United States may tighten chip exports. Chinese official media is worried 
  - [china] Novelis to sell two China subsidiaries for $265 million
  - [china] Hindalco Says Novelis Enters Agreement To Sell China Aluminum Subsidiaries
  - [china] Novelis Agrees to Sell Two China Subsidiaries for About $265 Million
  - [korea] Samsung conquered AI chips. Now it wants to build data centres
  - [korea] South Korea's October ICT Exports Hit $70.35 Billion as Chip Exports Jump 259.4%
  - [china] Effective from today! The central bank raised the foreign exchange deposit reserve ratio for the first time in
  - [china] The central bank’s major adjustment is happening today
  - [china] Effective from today! The foreign exchange deposit reserve ratio of financial institutions increased to 6%
  - [japan] Japan faces currency hell as yen plunges and bond yields explode
  - [korea] The possibility of a big step by the U.S. Federal Reserve increases pressure on the Bank of Korea to raise int
  - [japan] 20% say they have seen or heard slander against the Ainu people, Cabinet Office poll
  - [china] Central Bank: Starting today, the foreign exchange deposit reserve ratio of financial institutions will be inc
  - [japan] Redevelopment is in the red now in Abeno, Osaka
  - [japan] Good Morning World》U.S. wholesale inflation in October hit a four-year high, and the market is betting on the 
  - [japan] De-stimulation & exposure? A successful advance on the opposite path to "Love Jotou"...Why Netflix "Ai no Sato
  - [korea] “Interest rates are going to rise, so we should be short”… Bank short-term deposits exceed KRW 470 trillion, ‘
  - [japan] Why was the 29-story building standing alone in front of the station in the suburbs sold for over 100 million 
  - [korea] The US Federal Reserve is even discussed as a ‘big step’… Will the Bank of Korea raise interest rates next wee
  - [japan] Abeno, Osaka: Voices of ``I want my hometown back''...Behind the scenes of ``revitalization due to inbound tou
  - [korea] 85% chance of interest rate hike in September... The burden on the Bank of Korea increased due to rising oil p

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
      "published_utc": "2026-11-15T18:45:23+00:00",
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

