atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-11T04:42:43.398110+00:00
Total: 3000 manchetes

  🇯🇵 Japão          922
  🇨🇳 China          911
  🇹🇼 Taiwan         310
  🇰🇷 Coreia do Sul  857

## O que já está no feed (não repita)

  - [japan] Taisei Corporation - To Buy Back Up To 1.41% Of Shares Worth 20 Billion Yen
  - [taiwan] Changs Ascending rides semiconductor expansion into AI data-center power
  - [japan] Asia FX steadies after falling on hot U.S. inflation; yen near 6-wk low
  - [china] Yuan holds steady as PBOC eases guidance, dollar firms
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase on November 11, with a net withdrawa
  - [japan] Hibiya Engineering - To Buy Back Up To 0.72% of Own Shares Worth 1.1 Billion Yen
  - [korea] South Korea Jobless Rate Reaches More Than Three-Year Low as Hiring Slows
  - [taiwan] TSMC is seeing 'insatiable' demand for chips, executive tells Nikkei Forum
  - [china] Shanghai aluminium hits 11-month low on firmer dollar, higher China exports
  - [japan] Nikkei average stock price rise Movement to buy back AI and semiconductor related stocks
  - [japan] Mebuki Financial Group Inc - To Buy Back Up To 0.95% Of Own Shares Worth 10 Billion Yen
  - [korea] Household loans again rise in Oct. to record high despite tightened rules, higher rates
  - [japan] Macroscope: High city fiscal policy shows no signs of change even after the US mid-term elections, with stakeh
  - [japan] Consumption tax reduction bill goes to the House of Councilors, Prime Minister Takaichi says, “Support money f
  - [japan] Bank of Japan expects continued appropriate policy management to achieve sustainable and stable 2% target - Pr
  - [korea] “Could I also get an 800 million won performance bonus?” ... SK hynix hires production workers with no educati
  - [china] Russia retreats from China's yuan as U.S. sanctions bolster dollar
  - [japan] Japan futures gain for second session on tyre makers' dip-buying, weaker yen
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation today
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation in the open market today
  - [taiwan] Taiwan machinery exports rise for 21st month on AI demand, but US election adds uncertainty
  - [china] CHINA PBOC CONDUCTS CNY187 BLN VIA O/N REVERSE REPO WEDS
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7191 WEDS VS 6.7167
  - [china] On November 11, the central bank launched a 187 billion yuan overnight reverse repurchase operation.
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation with an interest rate of 1
  - [japan] "Neocloud" Core Weave's final deficit 6 times due to interest payment
  - [japan] Japan MOF To Auction Y700.0B Of 20-Year Govt Bonds Nov 18
  - [china] The central bank launched a 187 billion yuan overnight reverse repurchase operation on November 11
  - [japan] Japan MOF To Auction Y1.9T Of TD-Bills Nov 18
  - [china] US lawmakers push China chip rules after Nvidia CEO allegations
  - [china] HEADS UP: US TSY'S BESSENT ABOUT TO SPEAK AT THE NATIONAL COMMITTEE ON US-CHINA RELATIONS GALA DINNER
  - [korea] Revised regional currency swap arrangement takes effect
  - [korea] South Korean shares slip as US inflation data boosts rate-hike bets
  - [japan] From AKB to the Bank of Japan, on-site financial classes are spreading, one step at a time to prevent fraud (A
  - [korea] Exports more than double in 1st 10 days of Nov.
  - [korea] Govt. to release growth forecasts 3 times per year: finance minister
  - [korea] South Korea's Tax Cuts for Gasoline, Diesel, Butane to Continue Until Jan. 31, Finance Ministry Says
  - [korea] South Korea to Extend Temporary Fuel Tax Cuts by Two Months, Finance Ministry Says
  - [korea] Seoul shares turn higher after weak start amid inflation woes
  - [korea] Even mention of the US ‘big step’… Will the Bank of Korea raise interest rates despite ‘AI risk’? [Money]

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
      "published_utc": "2026-11-11T04:42:43+00:00",
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

