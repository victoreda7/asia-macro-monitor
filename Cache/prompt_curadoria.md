atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-29T14:42:44.284043+00:00
Total: 3000 manchetes

  🇯🇵 Japão          877
  🇨🇳 China          851
  🇹🇼 Taiwan         382
  🇰🇷 Coreia do Sul  890

## O que já está no feed (não repita)

  - [china] EU to Add €2 Fee on E-Commerce Imports Ahead of Holiday Season
  - [china] The European Central Bank decides to keep interest rates unchanged at 2.5% | International
  - [china] Angang Steel Q3 Net Loss At 2.0 Billion Yuan
  - [taiwan] U.S. GDP expanded by 3.4% in the third quarter, higher than expected, and core inflation increased by 3.1% in 
  - [china] Jiangxi Zhengbang Tech Q3 Net Loss At 353.8 Million Yuan
  - [china] Maanshan Iron & Steel Q3 Net Loss At 108.3 Million Yuan
  - [china] Shanghai Yuyuan Tourist Mart Q3 Net Profit At 6.7 Million Yuan
  - [china] China Longyuan Power Group: Solar expansion lifted capacity, but weaker wind conditions weighed on 9M earnings
  - [china] Jiangsu Yanghe Distillery Q3 Net Loss At 770.9 Million Yuan
  - [china] Sanan Optoelectronics Q3 Net Loss At 22.5 Million Yuan
  - [china] Kunlun Tech Q3 Net Loss At 1.1 Billion Yuan
  - [korea] SK Hynix Is Sold Out Through 2029 as Seagate Locks In Demand Into 2030
  - [japan] Japan plans to start reducing gasoline subsidies from December
  - [japan] Ritsumeikan Counterproposal to the consumption tax reduction bill: “50,000 yen benefit to tax-exempt household
  - [china] Former President Peng Huainan was also impostored by the central bank: people should not be deceived | Sankei
  - [china] European Central Bank President Christine Lagarde resigns ahead of schedule and will step down in February 202
  - [korea] Samsung Electronics earned nearly as much as Microsoft and Alphabet combined. What the Korean giant is now say
  - [korea] Asia report: Markets diverge amid steady central bank signals, Samsung slips on record profits
  - [korea] Samsung prevê que escassez de chips de IA se agrave
  - [china] China Names New Politburo Member, Plans Party Congress in 2027
  - [china] Geely Profit Climbs as Surging Exports Help Offset China Slump
  - [china] Volkswagen expects exports to compensate for part of the slowdown in China, says chief financial officer
  - [japan] Advantest Corp. Stock 12‑Month Price Target Raised to JPY 46013.64, Implies 32% Upside
  - [japan] Dollar pulls back as Warsh leaves tightening path murky; Euro tread water
  - [japan] [After the mid-term elections, ``Stocks will go up no matter what happens''] The future of the ``US stock mark
  - [taiwan] Taiwan central bank board members flag inflation woes, minutes show
  - [japan] Volkswagen's July-September fiscal year results in a large deficit of over 800 billion yen
  - [china] RemeGen Q3 Net Profit At 610.9 Million Yuan
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Charitable Contribution
  - [china] Governor of the Central Bank: Tightening again if necessary will maintain the housing market in a situation of
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Decision on Share Disposition
  - [japan] Yomiuri: Sumitomo Mitsui Trust Bank to Launch 10 Billion Yen Anime Fund
  - [japan] Electricity charges for November hit record highs for seven major companies
  - [japan] Yomiuri: Ward in Central Tokyo Calls on Condominium Developers to Prohibit Resale Within 5 Years
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Transactions with Affiliate Company
  - [china] The minutes of the central bank's proceedings reveal that 2 board members opposed the 10th consecutive freeze 
  - [china] Beijing Capital Development Q3 Net Loss At 1.1 Billion Yuan
  - [taiwan] AUO sells Taichung plant to TSMC for NT$38.8B, scraps Quanta deal
  - [china] Alphabet spells out more AI capex, China+1 doesn't add up
  - [china] CanSemi Tech Q3 Net Loss At 349.1 Million Yuan

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
      "published_utc": "2026-10-29T14:42:44+00:00",
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

