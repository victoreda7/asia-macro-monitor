atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-18T18:42:52.962531+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1021
  🇨🇳 China          907
  🇹🇼 Taiwan         310
  🇰🇷 Coreia do Sul  762

## O que já está no feed (não repita)

  - [china] China increases sugar production and should reduce imports in the new harvest, predicts StoneX
  - [taiwan] Taiwan Semiconductor Manufacturing ADR
  - [japan] Toyota, Suzuki rely on weak yen to keep profits growing
  - [china] LVGEM (China) Real Estate Investment Says Public Float Was Below Minimum From Dec 2024 To Nov 2026
  - [china] JD.com, Inc. Class A Stock 12‑Month Price Target Cut to CNY 125.48, Implies 40% Upside
  - [korea] Samvardhana Motherson Says Cheongju District Court Approves Liquidation Of Subsidiary MSSL Korea WH
  - [china] The central bank launches 714 billion yuan overnight reverse repurchase operation
  - [china] 'All Chinese players' will rely on domestic chips eventually: Tencent
  - [china] JD.com, Inc. Class A Stock 12‑Month Price Target Cut to CNY 126.21, Implies 41% Upside
  - [japan] SoftBank Group Corp. Stock 12‑Month Price Target Cut to JPY 8,156, Implies 149% Upside
  - [china] Tencent Says US Chip Curbs to Slow Chinese AI in the Short Run
  - [taiwan] First winter seafood shipment from Taiwan arrives in Beijing amid push for cross-Strait trade ties
  - [korea] S.Korean pension funds dump SK Hynix, rotate into Samsung and defensive plays
  - [japan] Swiss Franc, Japanese Yen Could Rise if Major Central Bank Peers Cut Rates in 2027 — Market Talk
  - [china] China seeks advanced Nvidia chips for AI weapons despite US restrictions: report
  - [china] China seeks advanced Nvidia chips for AI weapons despite US curbs, report says
  - [china] Nvidia stops shipping US-approved AI chips to China
  - [japan] Bank of Japan Governor Ueda attends the House of Councilors Finance Committee meeting on the 19th for the half
  - [china] Chinese steel exports could hit 130 million tonnes in 2026, threaten Indian industry: T V Narendran
  - [china] Nvidia to Stop Selling Advanced AI Chips to China
  - [china] Nvidia Makes Major China Decision After $2.4 Billion in AI Chip Sales
  - [taiwan] Taiwan Semiconductor Director Purchased Shares Worth Over $500K
  - [china] Nvidia stops shipping "Hopper" AI chips to China
  - [china] Xingyun Technology Signs AI Token Services Contract Worth Up To 2 Billion Yuan
  - [china] Zhongji Innolight's Chairperson Proposes A-Share Buyback With 2-4 Billion Yuan
  - [china] China Warns of Countermeasures Against New U.S. AI Chip Curbs
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Acquisition of equity interest by a subsidiary
  - [china] Commentary: Despite AI Boom, China’s Chipmakers Have Yet to Catch Up to Nvidia
  - [korea] NPS names investment strategy head to lead real estate portfolio
  - [korea] Samsung Electronics plays down concerns about neocloud companies and AI bubble
  - [korea] Samsung Electronics downplays concerns about neocloud firms and AI bubble
  - [taiwan] Taiwan completes Asia's largest single offshore wind project off central coast, connecting 1 GW of capacity to
  - [japan] Swiss Franc Expected to Weaken Against Yen on Policy Divergence — Market Talk
  - [korea] [Principal and interest bomb] ‘Base interest rate hike trend’ Interest rates on variable mortgage loans have r
  - [korea] More than half of the listed companies in Korea recorded a net profit deficit in the third quarter o..
  - [japan] Japan October crude import volume down 0.7%
  - [taiwan] Lawmakers unfreeze 50 MND budget items totaling US$38.2 million
  - [china] Yuan Bond Financing Demand Rises in Central Asia, Southeast Asia
  - [korea] Why did Samsung and SK Hynix shares rally on Wednesday?
  - [china] WuXi AppTec Co., Ltd. Class A Stock 12‑Month Price Target Cut to CNY 204.35, Implies 40% Upside

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
      "published_utc": "2026-11-18T18:42:53+00:00",
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

