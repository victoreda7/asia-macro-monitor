atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-15T05:22:43.529087+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1002
  🇨🇳 China          863
  🇹🇼 Taiwan         309
  🇰🇷 Coreia do Sul  826

## O que já está no feed (não repita)

  - [korea] South Korea's October ICT Exports Hit $70.35 Billion as Chip Exports Jump 259.4%
  - [china] Effective from today! The central bank raised the foreign exchange deposit reserve ratio for the first time in
  - [china] The central bank’s major adjustment is happening today
  - [china] Effective from today! The foreign exchange deposit reserve ratio of financial institutions increased to 6%
  - [japan] Japan faces currency hell as yen plunges and bond yields explode
  - [korea] The possibility of a big step by the U.S. Federal Reserve increases pressure on the Bank of Korea to raise int
  - [china] Increase to 6%! The central bank’s major adjustments officially take effect today
  - [japan] 20% say they have seen or heard slander against the Ainu people, Cabinet Office poll
  - [china] Central Bank: Starting today, the foreign exchange deposit reserve ratio of financial institutions will be inc
  - [japan] Redevelopment is in the red now in Abeno, Osaka
  - [japan] Good Morning World》U.S. wholesale inflation in October hit a four-year high, and the market is betting on the 
  - [japan] De-stimulation & exposure? A successful advance on the opposite path to "Love Jotou"...Why Netflix "Ai no Sato
  - [korea] “Interest rates are going to rise, so we should be short”… Bank short-term deposits exceed KRW 470 trillion, ‘
  - [japan] Why was the 29-story building standing alone in front of the station in the suburbs sold for over 100 million 
  - [korea] The US Federal Reserve is even discussed as a ‘big step’… Will the Bank of Korea raise interest rates next wee
  - [japan] Abeno, Osaka: Voices of ``I want my hometown back''...Behind the scenes of ``revitalization due to inbound tou
  - [china] China e EUA discutem tarifas e comércio agrícola antes de encontro entre Xi e Trump
  - [china] GEOPOLITICS | Bessent and Lutnick Reportedly Differ on Nvidia Chip Curbs for China
  - [japan] Liberal Democratic Party House of Councilors Chairman Matsuyama consumption tax reduction bill “People and Kom
  - [japan] National Secretary-General Shinba Consumption tax reduction bill Request acceptance of resident tax reduction
  - [china] China, U.S. discuss tariff cuts ahead of Trump-Xi meeting next week
  - [china] China, US Discuss Tariffs in First Meeting of Trade Council
  - [china] China, US discuss tariffs, farm trade at first trade council meeting
  - [china] China, US discuss tariffs, farm trade ahead of Xi-Trump meeting
  - [china] Blacklisted Chinese university reportedly purchased Nvidia H200s despite export restrictions
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
      "published_utc": "2026-11-15T05:22:43+00:00",
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

