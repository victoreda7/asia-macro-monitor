atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-21T10:02:51.271040+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1034
  🇨🇳 China          921
  🇹🇼 Taiwan         325
  🇰🇷 Coreia do Sul  720

## O que já está no feed (não repita)

  - [china] Trump boasts of unprecedented achievements in U.S.-China-Russia talks and exceeded full marks | Trump: The rel
  - [taiwan] Ministry of Economic Affairs: The electronics industry is still confident about its prospects and exports are 
  - [taiwan] Taiwan further tightens short-selling rules after market rout
  - [korea] Samsung, SK hynix tumble as analysts split on chip outlook
  - [china] Chuck Schumer Says Trump, Lutnick ‘Sold Out America’ by Approving Nvidia, AMD AI Chip Sales to China: ‘They Ge
  - [taiwan] Taiwan's Q3 current account surplus hits 2nd highest due to global AI demand
  - [korea] SoftBank's Son studied the possibility of a $1 trillion acquisition of SK Hynix, according to The Information
  - [korea] SoftBank’s Son explored $1 trillion buyout of SK Hynix, the Information reports
  - [korea] “Masayoshi Son Mulls Acquiring SK hynix for 1,346 Trillion Won...Asks Wall Street About Financing Plan”
  - [taiwan] Retail investors snatch up odd lot shares amid TSMC's plunge
  - [korea] Is the Bank of Korea inclined to raise interest rates? Hot economic issues next week, including whether KOSPI 
  - [taiwan] SolidWizard sees AI, semiconductor orders through 2027
  - [china] China’s Offshore Tax Clampdown Pushes Budget Into Rare Surplus
  - [korea] SoftBank’S Masayoshi Son Explored $1 Trillion Moonshot Buyout Of SK Hynix - The Information
  - [korea] [Next week's economy] Waiting to see whether the Bank of Korea will raise interest rates... Growth forecast an
  - [japan] Considering curbing speculative transactions for newly built condominiums Tax reform next year
  - [korea] Bank of Korea, last Monetary Policy Committee meeting of the year on the 26th... Pay attention to whether the 
  - [korea] From determining the base interest rate to coin regulation… Financial market watershed next week
  - [korea] [N Week] Last base interest rate increase of this year?... Digital Asset Act and Financial Reform Plan Reveale
  - [korea] Key facts: SK hynix results surge; Kioxia stake rises; HYAICO formed
  - [korea] The Bank of Korea decides on the base interest rate on the 26th... Will the increase resume after two months?:
  - [korea] [Next week's economy] Let's take a breather. Will the base interest rate be raised? The Bank of Korea’s growth
  - [korea] Exports reach $1 trillion and growth forecast is ‘worsening’… Additional interest rate hike by the Bank of Kor
  - [china] Tongda International Group Operating Subsidiaries Provides E-Commerce Services in China
  - [japan] Dollar set for 4-week win streak; yen jumps on safe-haven bid, hot inflation data
  - [japan] AI Selloff Boosts Haven Demand for Yen, Franc as Dollar Slips
  - [japan] AI Selloff Spurs Haven Demand for Yen, Franc as Dollar Slips
  - [china] Verlinvest: China Resources Indirect Subsidiary Blossom Key Holds 50% Indirect Interest in Oatly Shares
  - [korea] [Money Briefing] The last Monetary Policy Committee of the year weighs on a 3.25% increase in the base interes
  - [japan] Japan weighs early funding to ICC before US sanctions cutoff
  - [japan] Nvidia Server Suppliers Halt Southeast Asia Shipments - Nikkei
  - [china] FCC approves 71 firms to import tech gear despite China ban
  - [korea] SK hynix, IPG Photonics, and Diodes shares plummet, what you need to know
  - [china] U.S. Approves 879,000 AI Chips To China
  - [japan] Dollar weaker as Fed-fueled rally stalls; lower US yields help yen
  - [china] Trump Says Jensen Huang Made 'Bad Decisions,' Vows China to Get Old Chips Only
  - [china] Trump says only older chips should be sold to China
  - [china] Trump says US wants only older chips sold to China
  - [china] U.S. Cleared Nearly 880,000 AI Chips for Chinese Buyers
  - [china] Trump: we want only older chips to China

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
      "published_utc": "2026-11-21T10:02:51+00:00",
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

