atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-16T02:12:51.076396+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1014
  🇨🇳 China          866
  🇹🇼 Taiwan         308
  🇰🇷 Coreia do Sul  812

## O que já está no feed (não repita)

  - [china] HKEX launches offshore yuan bond index amid yuan internationalisation push
  - [china] China Oct Industrial Output +4.8% On Year; Market Expected +5.2%
  - [china] China Oct Industrial Output +0.21% On Month
  - [korea] NH Nongwoobio: 9M earnings improved, while a KRW 36,738 million seed-business acquisition is pending
  - [japan] Japan's economy stagnated in the third quarter as the war with Iran pushed up inflation and suppressed consump
  - [china] China's Home Price Decline Gathered Pace in October
  - [china] Drop in China’s new home prices narrows to 11-month low
  - [korea] Bank of Korea freezes base interest rate for 6 consecutive times... Formalization of the ‘long-term freeze’ po
  - [china] CHINA PBOC CONDUCTS CNY460 BLN VIA O/N REVERSE REPO MON
  - [japan] Dollar's Rise Toward 160 Yen Brings Intervention Risk Back Into Focus — Market Talk
  - [china] On November 16, the central bank conducted an overnight reverse repurchase operation of RMB 460 billion.
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7141 MON VS 6.7152
  - [taiwan] TSMC's new US$500 million arm could invest in chip suppliers
  - [japan] Japan Auctioning Y250.0B Of 10-Year CPI-Indexed Bonds
  - [china] Changes in Residential Property Sales Prices in 70 Major and Medium-Sized Cities in October 2026
  - [japan] Nikkei, Kospi slide: Asian markets fall as Nvidia results, US inflation concerns keep investors cautious
  - [japan] Japan's Economic Growth Underwhelms as Demand, Exports Drag — Market Talk
  - [japan] Yen steady against euro and dollar after soft Japanese GDP data
  - [japan] Urgent proposal to the government to reflect the reality of Tokyo in nursing care/disability compensation due 
  - [japan] Japan's Q3 GDP drops an annualized 0.1%, below market expectations
  - [japan] BOJ Still Poised to Tighten Despite Sluggish Economic Growth — Market Talk
  - [korea] Future Fund 'fiscal paradigm shift' for strategic investment: policy report
  - [japan] Japan’s economy unexpectedly shrinks in July-September as consumption falters
  - [japan] Goldman, Morgan Stanley Split on Yen Outlook on Diverging Forces
  - [japan] JGB Futures Fall, Tracking Declines in U.S. Treasurys Market — Market Talk
  - [japan] CABINET OFFICE: JAPAN GDP MUST GROW REAL 0.09% Q/Q, OR ANNUALIZED 0.4% IN EACH QUARTER OF FISCAL 2026 (TO MARC
  - [japan] Japan's Q3 GDP dropped an annualized 0.1%
  - [japan] Japan Q3 GDP unexpectedly shrinks as slowing exports, weak spending weigh By Investing.com
  - [japan] Japan Q3 GDP Flat On Quarter
  - [japan] Dollar Expected to Rise Further to 162 Yen in 2027 — Market Talk
  - [korea] SK Hynix to Invest $1 Billion Over Five Years to Support Chip Suppliers
  - [japan] JAPAN Q3 GDP ADJUSTED DEFLATOR +0.4% Q/Q VS. +1.0% IN Q 2
  - [japan] JAPAN Q3 GDP UNADJUSTED DEFLATOR +2.4% Y/Y VS. +2.6% IN Q2
  - [japan] JAPAN Q3 CONSUMPTION -0.3% Q/Q; -0.1 PP CONTRIBUTION
  - [japan] JAPAN Q3 REAL GDP -0.1% ANNUALIZED; MNI MEDIAN +0.1%
  - [japan] JAPAN Q3 CAPEX +1.6% Q/Q +0.3 PP CONTRIBUTION
  - [japan] JAPAN Q3 GDP POSTS 1ST DROP IN 4 QUARTERS
  - [japan] MNI JAPAN Q3 REAL GDP -0.0% Q/Q; MNI MEDIAN +0.0%
  - [japan] JAPAN Q2 REAL GDP REVISED TO +1.7% ANNUALIZED FROM +1.4%
  - [japan] JAPAN Q2 REAL GDP UNREVISED AT +0.4% Q/Q

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
      "published_utc": "2026-11-16T02:12:51+00:00",
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

