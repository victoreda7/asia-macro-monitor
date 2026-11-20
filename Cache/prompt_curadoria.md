atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-20T09:42:42.032891+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1036
  🇨🇳 China          912
  🇹🇼 Taiwan         317
  🇰🇷 Coreia do Sul  735

## O que já está no feed (não repita)

  - [korea] SK Hynix to become top shareholder in rival Kioxia after bond conversion
  - [japan] Yen market price rise, US dollar selling movement due to fall in long-term interest rates
  - [korea] S.Korea to offer $1,870 tax credit per locally made EV to counter Chinese imports
  - [japan] High prices, ice cream prices going up, pizza shops selling low-priced products, farmers screaming
  - [korea] From robot pets to virtual livers: Apple Developer Academy showcases projects at Postech
  - [china] China's January-October fiscal revenues up 4.9% y/y
  - [taiwan] TSMC says it will comply with new US rule that strips Chinese chip designers of a key exemption
  - [china] Exclusive-Beijing to bar young ’red-chip’ firms from listing outside mainland China, sources say
  - [china] China's January-October government land sales revenue down 25.8% Y/Y
  - [taiwan] Taiwan October export orders surge by fastest clip on record thanks to AI demand
  - [china] Pequim deve proibir que jovens empresas “red-chip” sejam listadas fora da China continental, segundo fontes
  - [korea] The Korean won is expected to strengthen as demand to convert the dollar earned during the semicondu..
  - [china] US AI chip curbs hit China tech stocks, spur self-sufficiency push
  - [korea] Shim Jae-bok passed away, Sung Won-won's husband, Shim Won-bo (team leader of Geumho Construction'..
  - [japan] Yomiuri: Japan's MS&AD to Merge Life Insurance Subsidiaries
  - [korea] Kospi tanks to 10-month low on China chip fears; Investors hunt for bottom
  - [china] Factbox-Global investment banks see Chinese yuan’s gradual appreciation extending into 2027
  - [japan] House of Councilors Special Committee Local Hearing: Consumption tax reduction “Support for local governments,
  - [china] The first U.S.-China-Russia summit meeting is not the "New Yalta Conference" but a modern version of "Entente.
  - [japan] Prime Minister Takaichi's "diplomatic defeat" was exposed at the US-China-Russia summit meeting, and how will 
  - [china] Key facts: NVIDIA Q3 Revenue $115.8B; CEO Resigns; China Chip Probe
  - [korea] SK Hynix: To Hold 14.1% Stake in Kioxia Through SPC After CB Conversion
  - [korea] SK Hynix: SPC-Invested CBs to Convert Into 129,000 Kioxia Shares
  - [korea] SK Hynix: Hold Kioxia Stake Through Special Purpose Company
  - [korea] SK Hynix to Convert Convertible Bonds Into Kioxia Holdings Shares
  - [korea] Asia tech stocks reel from Anthropic IPO as SoftBank, Samsung, and TSMC slide
  - [korea] SK Hynix: to exercise convertible bond option for stake in Kioxia
  - [china] China's yttrium exports to US hit seven-month high
  - [china] Chinese Carmakers Tighten Grip on Overseas Sales Channels
  - [china] China's central bank to sell $7.5 billion worth of yuan bills in Hong Kong
  - [korea] Bank of Korea, last Monetary Policy Committee meeting of the year on the 26th... Should we raise the base inte
  - [japan] Stock price fell by more than 3,000 yen, almost completely down due to concerns about the future of the AI ​​a
  - [korea] The KOSPI and KOSDAQ plunged by 5%. While foreigners and institutions sold more than KRW 2 trillion
  - [japan] M3 Inc - To Expand Buy Back Up Scheme To Up To 5.06% Of Own Shares From Previous Up To 3% Worth 5.5 Billion Ye
  - [china] China's October coal imports from Australia hit six-year high
  - [korea] South Korean shares hit 10-month low as chipmakers slump on US tech selloff
  - [taiwan] Foxconn Technology: Global manufacturing capabilities support gaming, casing and thermal products, alongside E
  - [japan] Nikkei average closing price drops by 3007 yen Confusion over AI
  - [korea] SK Hynix weighs converting Kioxia bonds to shares, report says
  - [korea] The top 1% return on stock investment, which sold the largest amount of Samsung Electronics' common

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
      "published_utc": "2026-11-20T09:42:42+00:00",
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

