atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-13T10:42:47.594938+00:00
Total: 3000 manchetes

  🇯🇵 Japão          989
  🇨🇳 China          868
  🇹🇼 Taiwan         309
  🇰🇷 Coreia do Sul  834

## O que já está no feed (não repita)

  - [china] China's New Yuan Loans Contracted in October
  - [korea] VKAISS 2026 Strengthens Vietnam and South Korea Cooperation in AI and Semiconductors
  - [japan] Prime Minister Takaichi says consumption tax reduction bill support funds will be considered for 50% or more o
  - [china] Metro Holdings: Indonesian property sales and improved China results drove a return to pre-tax profit
  - [china] Metallurgical Corporation Of China's January-October New Contracts Totalled 548.8 Billion Yuan
  - [china] Alice Huang-Linked Firm Procured Banned Nvidia Chips in China
  - [taiwan] Taiwan chip suppliers see limited impact from Nvidia leadership change
  - [china] The increase in social financing exceeded 28 trillion! The latest release from the central bank shows that the
  - [china] 664 billion! After the anchor change, the central bank’s first “overnight + 7 days” matching operation will re
  - [china] Central Bank: Will launch 200 billion yuan buyout reverse repurchase operation on November 16
  - [china] Central Bank: The stock of social financing at the end of October 2026 was 469.16 trillion yuan, a year-on-yea
  - [china] The central bank will launch a 200 billion yuan buyout reverse repurchase operation
  - [china] Banned Nvidia chips traced to Alice Huang-linked data center in Shanghai - report
  - [china] China Haisum Engineering's Unit Signs 1.4 Billion Yuan EPC Contract For UK Waste-To-Energy Project
  - [japan] Appier Group, Inc. Raises FY26 Operating Income Guidance to JPY 5.9B
  - [korea] As Google completes security measures to export precision maps abroad, such as covering military and..
  - [korea] Google to compete with Korean mapping firms after Seoul clears high-resolution map exports
  - [japan] Japan Post Bank Lifts Annual Earnings Outlook On Increased Policy Interest Rates
  - [japan] Japan core inflation seen above BOJ target for second month in October: Reuters poll
  - [japan] MUFG raises annual profit target, announces 200 billion yen buyback
  - [taiwan] Mars Semiconductor posts slight revenue growth, expects eBMC orders in 2H27
  - [china] China's Industrial Production Growth Likely Slowed in October — Market Talk
  - [taiwan] The central bank will pay more than 220 billion to the treasury next year. The sharp increase in the proportio
  - [china] China’s access to some Nvidia chips in doubt as curbs gain traction in US Congress
  - [japan] Fund Inflows Into Japan Likely to Support Yen in Long Term — Market Talk
  - [japan] Japan warns arms suppliers of deep order cuts as budget squeeze hits military buildup: sources
  - [japan] [Prices 30 years ago and now] How many times more expensive are rice, eggs, and white bread? Eggs were about 1
  - [china] China's Retail Sales Growth Likely Eased in October — Market Talk
  - [korea] Park Systems: Revenue grew, profit fell, and KRW 100bn in hybrid financing targets expansion and M&A
  - [china] Jensen Huang Exit Sets Up US-China Showdown Over AI Chip Curbs
  - [korea] Classys Reports Nine-Month 2026 Revenue of KRW 275.7 Billion, Up 13% Year over Year; Prepares to Accelerate Gr
  - [korea] Classys Nine-Month Revenue Rose 13% to KRW 275.7B
  - [korea] VINA TECH: Data-center demand and Vietnam expansion meet a KRW 39.69bn 9M net loss
  - [japan] Case for BOJ Rate Hikes Seen Strengthening — Market Talk
  - [china] CNOOC Limited Class A Stock 12‑Month Price Target Raised to CNY 44.93, Implies 49% Upside
  - [japan] Japan's Likely Soft GDP Data Unlikely to Stop BOJ Rate Hikes — Market Talk
  - [japan] Mitsubishi Ufj Financial Group, Inc. - To Buy Back Up To 0.62% Of Own Shares Worth 200 Billion Yen
  - [japan] Japan futures post first weekly gain in five as yen weakens, Tokyo shares rebound
  - [japan] Ut Group Co Ltd - To Buy Back Up To 7.2% Of Own Shares Worth 6 Billion Yen
  - [korea] REG - Samsung Electronics Samsung Elec - SMSD - Announcement of Investor Relations Event

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
      "published_utc": "2026-11-13T10:42:47+00:00",
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

