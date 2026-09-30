atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-09-30T12:22:45.274121+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1264
  🇨🇳 China          775
  🇹🇼 Taiwan         253
  🇰🇷 Coreia do Sul  708

## O que já está no feed (não repita)

  - [japan] Prime Minister Takaichi held the 13th Economic and Fiscal Council Meeting in 2020
  - [taiwan] Why TSMC’s capacity crunch opens the door for Samsung’s foundry
  - [korea] Korea lifts tax revenue forecast to record W478.6tr on chip boom
  - [china] ACM Research subsidiary reports RMB 17.1B backlog, 88% YoY rise
  - [japan] Private-sector politicians make proposals for economic policy management based on movements in interest rates 
  - [china] China’s next big export could be $1.5 trln of debt
  - [japan] Discussions begin at the Fiscal System Council for next year's budget formulation
  - [japan] Crude oil imports in August Imports from the United States were 12 times higher than in the same month last ye
  - [china] Retail Export Strategies Give Way to Integrated China-ASEAN Supply Chains
  - [japan] Prime Minister Takaichi "examines financial scale" in preparation for next year's budget draft
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Subsidiary obtaining Shares
  - [china] China's metal-heavy commodity imports map a messy energy transition: Maguire
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Subsidiary Factory Right-of-Use Acquisition
  - [japan] Japan Paused Forex Intervention as Yen Strengthened Modestly — Update
  - [japan] Japan economic panel members underline BOJ independence By Reuters
  - [japan] Hyperscale Data Secures $22.58 Million Notes, Extends JGB Loan Maturity to 2027
  - [japan] Japan Paused Forex Intervention as Yen Strengthened Modestly
  - [china] China Aoyuan Is Close To Finalizing Onshore Debt Restructuring Proposal
  - [taiwan] TSMC weighs Texas investment to expand U.S. chip production: report
  - [china] Central Bank: Will launch 1.2 trillion yuan buyout reverse repurchase operation on October 8
  - [japan] I don't think there is a big discrepancy in perception between the Bank of Japan and the economy and prices - 
  - [japan] There has been no foreign exchange intervention in the past month, and the yen continues to appreciate as the 
  - [japan] Japanese economic panel members emphasise BOJ’s independence
  - [japan] Respect the Bank of Japan's autonomy, explain economic and fiscal risks and secure confidence - Member of the 
  - [china] China's Central Bank May Still Prefer Targeted, Low-Profile Credit Easing — Market Talk
  - [korea] Deputy Prime Minister and Minister of Finance and Economy Lee Hyung-il and Minister of Land, Infrast..
  - [china] Central Bank: Will carry out 1.2 trillion yuan buyout reverse repurchase operation
  - [taiwan] TSMC avalia possível investimento no Texas, segundo fontes
  - [taiwan] TSMC evaluates potential Texas investment, sources say
  - [korea] Global interest rates are resembling 'Corona tightening'... Will Korea also go up by 3.5% per year?
  - [china] 17:04:27 [Central Bank: A 1.2 trillion yuan buyout reverse repurchase operation will be carried out on October
  - [china] China enables four new Brazilian plants to export meat
  - [china] Central Bank: On October 8, it will launch a 1.2 trillion yuan buyout reverse repurchase operation with a peri
  - [korea] Korea’s Aug factory output, consumption, investment tumble on Hyundai strike; bond yields fall
  - [korea] Industrial output, retail sales, facility investment down in Aug.
  - [taiwan] Taiwan backs TSMC's US push but insists core R&D stays home
  - [china] China stocks flat, limp to quarterly drop, as stimulus falls short
  - [japan] Nidek has a deficit of 564.6 billion yen due to huge losses due to accounting fraud, etc.
  - [china] Scottish Mortgage Investment Trust cuts China exposure to 11%
  - [japan] Japan's oil imports rise 13% in August as US supplies surge

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
      "published_utc": "2026-09-30T12:22:45+00:00",
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

