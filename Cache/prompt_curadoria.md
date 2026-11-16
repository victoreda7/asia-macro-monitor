atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-16T03:02:49.016475+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1003
  🇨🇳 China          878
  🇹🇼 Taiwan         305
  🇰🇷 Coreia do Sul  814

## O que já está no feed (não repita)

  - [china] China's new home prices fall again in October; slowest annual decline in almost a year
  - [japan] Stock prices fall; sell orders spread for AI and semiconductor-related stocks
  - [japan] Japan's Economy Contracts Amid Inflation Squeeze — Update
  - [japan] Japan's 3Q GDP Data Missing Expectations Looks Like a Near-Term Yen-Negative — Market Talk
  - [japan] Hokkaido governor requests strict response from agriculture minister regarding lifting of ban on imports of US
  - [china] China's economy falters in October as factory output, retail sales miss forecasts
  - [korea] SK Hynix to Spend About $1B to Support Local Suppliers
  - [taiwan] Indonesian rupiah, Taiwan dollar fall most among subdued Asian currencies
  - [korea] Korea Computer: Revenue and earnings declined as cash tightened and inventory expanded
  - [china] NVDA Stock Dips Again After Worst Week In 19 Months: Why Michael Burry Sees ‘Mild Manipulation’ In AI Chipmake
  - [japan] Japan rubber trades in tight range as weaker yen offsets lower oil
  - [china] The first increase in the past five years! The foreign exchange deposit reserve ratio was increased from 4% to
  - [china] China's factory output grows but household spending remains subdued
  - [china] China's Home Price Decline Gathered Pace in October — Update
  - [china] China’s Economy Weakens More Than Forecast Despite Stimulus Push
  - [china] CHINA YTD INDUSTRIAL OUTPUT +5.3% Y/Y VS JAN-SEP +5.3% Y/Y
  - [china] CHINA YTD RETAIL SALES +1.0% Y/Y VS JAN-SEP +1.1% Y/Y
  - [china] China factory output, retail sales miss forecasts in Oct
  - [china] China’s factory output, retail sales growth slow in October
  - [china] China's Home Price Decline Gathered Pace in October
  - [china] HKEX launches offshore yuan bond index amid yuan internationalisation push
  - [china] China Oct Industrial Output +4.8% On Year; Market Expected +5.2%
  - [china] China Oct Industrial Output +0.21% On Month
  - [china] The added value of industries above designated size increased by 4.8% in October 2026
  - [korea] NH Nongwoobio: 9M earnings improved, while a KRW 36,738 million seed-business acquisition is pending
  - [japan] Japan's economy stagnated in the third quarter as the war with Iran pushed up inflation and suppressed consump
  - [china] Drop in China's new home prices narrows to 11-month low
  - [korea] Bank of Korea freezes base interest rate for 6 consecutive times... Formalization of the ‘long-term freeze’ po
  - [china] CHINA PBOC CONDUCTS CNY460 BLN VIA O/N REVERSE REPO MON
  - [japan] Dollar's Rise Toward 160 Yen Brings Intervention Risk Back Into Focus — Market Talk
  - [china] On November 16, the central bank conducted an overnight reverse repurchase operation of RMB 460 billion.
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7141 MON VS 6.7152
  - [taiwan] TSMC's new US$500 million arm could invest in chip suppliers
  - [japan] Japan Auctioning Y250.0B Of 10-Year CPI-Indexed Bonds
  - [china] Changes in Residential Property Sales Prices in 70 Major and Medium-Sized Cities in October 2026
  - [china] The central bank launches 460 billion yuan overnight reverse repurchase operation
  - [japan] Nikkei, Kospi slide: Asian markets fall as Nvidia results, US inflation concerns keep investors cautious
  - [japan] Japan's Economic Growth Underwhelms as Demand, Exports Drag — Market Talk
  - [japan] Yen steady against euro and dollar after soft Japanese GDP data
  - [japan] Urgent proposal to the government to reflect the reality of Tokyo in nursing care/disability compensation due 

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
      "published_utc": "2026-11-16T03:02:49+00:00",
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

