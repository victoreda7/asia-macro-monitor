atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-29T10:02:43.324610+00:00
Total: 3000 manchetes

  🇯🇵 Japão          892
  🇨🇳 China          841
  🇹🇼 Taiwan         383
  🇰🇷 Coreia do Sul  884

## O que já está no feed (não repita)

  - [taiwan] Taiwan central bank board members flag inflation woes, minutes show
  - [japan] Volkswagen's July-September fiscal year results in a large deficit of over 800 billion yen
  - [china] RemeGen Q3 Net Profit At 610.9 Million Yuan
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Charitable Contribution
  - [china] Governor of the Central Bank: Tightening again if necessary will maintain the housing market in a situation of
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Decision on Share Disposition
  - [japan] Yomiuri: Sumitomo Mitsui Trust Bank to Launch 10 Billion Yen Anime Fund
  - [japan] Yomiuri: Ward in Central Tokyo Calls on Condominium Developers to Prohibit Resale Within 5 Years
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Transactions with Affiliate Company
  - [china] The minutes of the central bank's proceedings reveal that 2 board members opposed the 10th consecutive freeze 
  - [china] Beijing Capital Development Q3 Net Loss At 1.1 Billion Yuan
  - [china] Alphabet spells out more AI capex, China+1 doesn't add up
  - [korea] Samsung Electronics earned nearly as much as Microsoft and Alphabet combined. What the Korean giant is now say
  - [china] CanSemi Tech Q3 Net Loss At 349.1 Million Yuan
  - [china] Shanxi Taigang Stainless Steel Q3 Net Loss At 355.1 Million Yuan
  - [china] Beijing Compass Technology Development Q3 Net Loss At 91.1 Million Yuan
  - [korea] Samsung Electronics' Investment in Facility Investment at Article 85...Responding to semiconductor boom with l
  - [korea] Samsung Electronics Co. Investments in Facilities Investment at Article 85
  - [japan] Kddi: To Expand London Data Centre With 47 Billion Yen Land Acquisition
  - [korea] The Seoul Metropolitan Government has set aside 55.7445 trillion won for next year's budget. It is t..
  - [korea] Federal Reserve freezes base interest rate, ‘taking a breather’… Bank of Korea weighs ‘November hike’
  - [china] China stocks slip as tech gauges hit over one-year lows, overshadowing Fed rate decision
  - [china] Loongson Technology Q3 Net Loss At 188.6 Million Yuan
  - [china] Muyuan Foods Q3 Net Loss At 3.2 Billion Yuan
  - [china] CNSIG Inner Mongolia Chemical Industry Q3 Net Loss At 302.5 Million Yuan
  - [taiwan] Foxconn Industrial Internet: AI-driven demand powered strong revenue and profit growth, alongside rising serve
  - [japan] Markets Shouldn't Take BOJ Rate Hikes for Granted — Market Talk
  - [japan] Shinya Ueda despairs over prices in the U.S. ``Japan doesn't cost 1,500 yen'' Taiyo Sugiura is also shocked by
  - [japan] Fed Tightening Bias Gives BOJ More Room for Hawkish Signaling — Market Talk
  - [taiwan] Taiwan semiconductor industry group backs government review of nuclear power restart
  - [japan] House of Representatives Finance and Financial Affairs Committee: Consumption tax reduction bill: Ruling and o
  - [japan] Dollar pulls back as Warsh leaves tightening path murky; Euro tread water
  - [china] Sensodyne maker Haleon cuts revenue growth forecast due to weak flu season and disruptions in China
  - [china] Sensodyne maker Haleon cuts revenue growth forecast on weak flu season, China disruption
  - [korea] Puriosa AI, a domestic artificial intelligence (AI) semiconductor start-up, attracted an investment
  - [japan] Financial Partners Group - To Buy Back Up To 1.2 Million Shares For 2 Billion Yen
  - [japan] House of Councilors Liberal Democratic Party consumption tax reduction bill “If a special committee is establi
  - [japan] Bank of Japan decides to reach 2% price target, policy interest rate will be maintained (Kyodo News)
  - [japan] Bank of Japan decides to reach 2% inflation, policy interest rate will be maintained (Kyodo News)
  - [japan] Japan's Nikkei rises on Advantest profit outlook as BOJ looms

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
      "published_utc": "2026-10-29T10:02:43+00:00",
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

