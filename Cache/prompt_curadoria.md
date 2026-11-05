atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-05T22:12:43.051513+00:00
Total: 3000 manchetes

  🇯🇵 Japão          898
  🇨🇳 China          898
  🇹🇼 Taiwan         321
  🇰🇷 Coreia do Sul  883

## O que já está no feed (não repita)

  - [korea] KT&G: Compound 2030 pairs global growth with KRW 5T in regular shareholder returns
  - [japan] Japanese savers have rediscovered interest rates and banks are feeling it
  - [japan] Dollar flat as Wall Street rout lifts safe-haven yen; pound in focus as BOE hikes
  - [japan] The long-awaited interest rate hike is a "big miscalculation", and about half of the credit unions and credit 
  - [japan] The "overall picture of finances" should be questioned rather than tax cut revenue sources; why is the Takaich
  - [japan] Will Trump, who suffered a crushing defeat in the midterm elections, approach Kim Jong Un at the US-North Kore
  - [china] Chinese cars' share in the UK market rapidly increases, reaching 17.5% in the January-September period...More 
  - [japan] Consumption tax reduction bill: ruling party poised to vote today; opposition party “concrete picture vague”
  - [china] Nvidia chips lie stockpiled in Hong Kong amid China's import restrictions: Report
  - [taiwan] SuperAlloy enters semiconductor pilot production in 3Q26
  - [china] Avoiding U.S. export controls, the dark side of China's AI start-up moon turns to Europe to rent Huida chip co
  - [japan] Foreign-student spending in Japan hits $4.3bn amid soft yen
  - [japan] Democratic 'blue wave' may buoy yen if AI trade reverses: FX traders
  - [taiwan] TI targets next semiconductor supercycle as humanoid robots surge
  - [korea] Micron, SanDisk and SK Hynix drop up to 20% as memory stocks sell off
  - [china] Nutrien Sees Tight Nitrogen Markets In 2027 As Higher China Urea Exports Only Partially Offset Outages
  - [china] China’s Central Bank Pledges More Support to Stabilize Markets
  - [china] Kimberly-Clark Backs Full-Year Growth Forecast Despite China Controversy — Update
  - [taiwan] Siemens To Modernize Taiwan Taoyuan Metro Signaling
  - [china] What does midterm humbling mean for Bessent ahead of US-China trade talks?
  - [korea] S.Korea’s current account surplus hits record $61 bn as global IBs hike GDP growth forecasts
  - [japan] Bernstein raises Sony stock price target to $26 on yen weakness By Investing.com
  - [korea] S.Korea eyes massive US Treasury purchase to boost FX reserves, offer relief to Washington
  - [japan] Bernstein raises Sony stock price target to $26 on yen weakness
  - [korea] SK Hynix losing out on US plant has major implications, Wedbush says
  - [japan] Yen market: Slight price movements; drop in crude oil futures causes temporary appreciation of yen and depreci
  - [taiwan] Taiwan's October CPI rises 2.33%, stays above 2% for sixth month
  - [china] Scholars who report on export capabilities for the first time at the CIIE: Teach you how to sell things to Chi
  - [japan] Fiscal System Council: Securing stable financial resources to strengthen defense capabilities
  - [taiwan] The central bank adjusted to prevent depreciation and foreign exchange deposits fell by US$4.308 billion at th
  - [japan] Citi sees dollar weakening against yen after U.S. midterms By Investing.com
  - [korea] LG Electronics India Enters Automotive Tech, Plans Manufacturing In Andhra
  - [china] China ready to expand US agricultural imports if Board of Trade tariff cuts take effect
  - [china] China ready to expand US farm imports – on 1 condition
  - [china] China controls rare earth exports to Japan, yttrium oxide plummets by 98% from January to September
  - [japan] Citi sees dollar weakening against yen after U.S. midterms
  - [china] KMB: China disruption constrained sales as Kenvue integration reshapes the growth outlook
  - [korea] Rupee gains nearly 1% in October, second-best performer in Asia after Korean won
  - [china] Nvidia chips pile up in Hong Kong as China withholds import approval
  - [china] China Plans Debut Yuan Bond Sales in Canada Amid Warming Ties

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
      "published_utc": "2026-11-05T22:12:43+00:00",
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

