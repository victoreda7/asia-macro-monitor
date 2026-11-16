atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-16T15:02:57.752307+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1010
  🇨🇳 China          876
  🇹🇼 Taiwan         304
  🇰🇷 Coreia do Sul  810

## O que já está no feed (não repita)

  - [japan] Yen Could Strengthen Versus Dollar by Year-End — Market Talk
  - [china] US to curb China’s access to AI chips as Trump heads to Asia
  - [korea] Samsung plans to build satellite chips at Texas fab for SpaceX: report
  - [china] China Resources Power Posts October Net Generation Of Subsidiary Power Plants Up 20.9% To 20.1 MLN MWh
  - [japan] Japanese Yen Offers Best Risk-Reward — Market Talk
  - [japan] Yomiuri: JIC Expects Capital Gain of Over 900 Billion Yen from Sale of JSR Shares to Mitsui Chemicals
  - [japan] Bank of Japan Councilor Takada: “Move to a good position: Flexible interest rate hikes”
  - [taiwan] Approved FDI hits Jan.-Oct. high; TSMC boosts outbound investments
  - [china] Alibaba details new AI safeguards as Chinese developers step up test disclosures
  - [japan] Japan Real Estate Investment: Strong leasing and higher distributions offset rate, refinancing and acquisition
  - [korea] Coatue Management Raises Stake In Meta, Reports Stake in SK Hynix - SEC Filing
  - [japan] Negotiations resume between national and local governments, aiming to settle financial burden ratio of support
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Announcement on behalf of subsidiary FII
  - [japan] Dollar at 19-month peaks as Japan GDP contraction pins yen in intervention zone
  - [japan] Dollar extends rally, yen looks past soft Japan GDP data
  - [japan] BOJ chief Ueda tells government panel wage growth ’quite strong’
  - [japan] Nickname decision for the advance utilization period of the former Bank of Japan Kanazawa branch site (HAB Hok
  - [taiwan] Unborn fetuses to count toward social housing priority: Interior ministry
  - [china] Senator accuses US Commerce Department of failing to stem flow of AI chips to China
  - [china] Central China Real Estate Posts October 2026 Contracted Sales Rmb493 Million
  - [korea] SK Square: SK hynix’s record quarter drove ₩7.94tn operating profit as portfolio NAV declined
  - [china] China's economy falters with lower-than-expected industrial production and retail sales
  - [japan] Finance Minister Katayama Consumption tax reduction bill Targets of support funds “to be determined after data
  - [china] Kuang-Chi Technologies' Unit Signs 1.8 Billion Yuan Supply Framework Contract
  - [china] RMB deposit balance fell for two consecutive months in October. Central Bank: Concerned about the expected imp
  - [japan] Japan’s economy unexpectedly shrinks as inflation squeezes households By Reuters
  - [japan] Yen Likely to Benefit From BOJ Interest-Rate Rises — Market Talk
  - [japan] The nickname for the site of the former Bank of Japan Kanazawa branch is ``Machinowa Korinbo.'' A high school 
  - [china] Hungary tightens oversight of Chinese, South Korean battery plants
  - [china] Chip tensions loom over Trump-Xi summit, as US and China push AI safety steps
  - [japan] Rise in the yen market, there are concerns about market intervention and concerns about early interest rate hi
  - [japan] Former Bank of Japan branch will be nicknamed ``Machinowa Korinbo'' by Kanazawa City, starting in May next yea
  - [china] Hindalco's Novelis To Sell Two China Subsidiaries For $265 Million
  - [korea] Enchem: Sales increased, but deep losses and a KRW 274.6bn working-capital deficit put liquidity in focus
  - [korea] Bithumb, a virtual asset exchange, turned into a deficit in both operating profit and net profit in
  - [japan] Yen Expected to Strengthen in 2027 Due to Supportive Policies — Market Talk
  - [china] China's Real GDP Growth May Ease to 4.4% Next Year — Market Talk
  - [japan] Takada, a Bank of Japan council member, emphasizes the risk of price rises as a new phase accelerates the pace
  - [china] China-ASEAN Summit China calls for promotion of cooperation in economic and trade fields
  - [japan] Highlights of the Outlook for Economic Activity and Prices (October 2026)

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
      "published_utc": "2026-11-16T15:02:57+00:00",
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

