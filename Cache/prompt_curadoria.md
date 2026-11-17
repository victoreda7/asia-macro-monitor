atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-17T05:13:31.733449+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1042
  🇨🇳 China          887
  🇹🇼 Taiwan         302
  🇰🇷 Coreia do Sul  769

## O que já está no feed (não repita)

  - [korea] IMF raises Korea's 2026 growth forecast to 3.9% on AI chip boom
  - [china] China stocks flat as chip curbs lift local tech, hit internet giants
  - [china] U.S. tightens rules to restrict China’s access to advanced AI chips overseas
  - [china] New rules for beauty festival before Sichuan-Xi meeting! Restricting the export of chips to overseas data cent
  - [china] Exclusive-China taps US AI models to train homegrown rivals as chip curbs bite
  - [china] Chinese firms turn to US AI models for training as export restrictions tighten: Reuters
  - [taiwan] Daxin aims for semiconductor materials to exceed half of revenue by 2030
  - [japan] Understanding the loans of the government, the Bank of Japan, and credit unions; analyzing the soundness of ma
  - [japan] Liberal Democratic Party Policy Research Council Chairman Kobayashi ``negotiates to gain understanding'' of co
  - [japan] Europe and Japan deepen semiconductor ties as imec expands in Hokkaido and JASMINE mobilizes
  - [japan] Government, Bank of Japan to grasp loan information of Shinkin Banks (Kyodo News)
  - [china] AMD, MU, SKHY, AVGO: Chip Stocks Ease Overnight After Selloff On New US Chip Restrictions Targeting China
  - [china] China AI Highflier Crashes 85% as Chip Fears Hit Model Makers
  - [china] Yuan steady despite firm dollar as PBOC strengthens fixing ahead of APEC
  - [china] China, Canada Expand Tariff Relief in Deepening Trade Thaw
  - [china] Chip Stocks Slide as US Sets New Curbs on China’s Compute Access
  - [china] Latest U.S. Chip Export Rules to Hurt Chinese AI Companies — Market Talk
  - [japan] Stock prices fall Sell orders centered on AI and semiconductor related stocks
  - [japan] BOJ board member calls for 'nimble' monetary policy | NHK WORLD-JAPAN News
  - [japan] BOJ board member calls for 'nimble' monetary policy
  - [japan] [Today's Oha Biz Tuesday, November 17th] Develop semiconductor design talent
  - [china] US moves to curb China's remote access to AI chips after Nvidia scandal
  - [taiwan] TSMC 3nm enters HBM as NVHBM reshapes base-die competition
  - [korea] P&T Link, a subsidiary of M83 and specializing in server and artificial intelligence (AI) infras..
  - [japan] Japan Data Preview: Forecasters See Another Month of Strong Gains for Exports, Imports in October
  - [korea] Samsung, SK hynix spend W88tr on capex as cash holdings soar
  - [korea] S. Korea regains top spot in global OLED shipments in H1
  - [japan] Difference over “financial burden”? Jeonbuk-Seoul joint hosting of Olympics canceled (2) (JoongAng Ilbo Japane
  - [japan] Difference over “financial burden”? Jeonbuk-Seoul joint hosting of the Olympics has been canceled (1) (JoongAn
  - [china] CHINA PBOC CONDUCTS CNY714 BLN VIA O/N REVERSE REPO TUES
  - [korea] Higher interest rates, sluggish consumer spending take toll on Korea’s credit card firms
  - [japan] JGB yields climb as buyers hold back on long-dated debt
  - [china] On November 17, the central bank launched a 714 billion yuan overnight reverse repurchase operation.
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7132 TUES VS 6.7141
  - [japan] Fed Policy, Weak Yen Hold Key for BOJ Rate Hikes — Market Talk
  - [china] China’s $17 Billion Crop Pledge Falters Ahead of Trump-Xi Summit
  - [japan] Bank of Japan policy management, comprehensive judgment and understanding of the economy and prices, including
  - [china] The central bank raised the foreign exchange deposit reserve ratio by 2 percentage points
  - [taiwan] Key facts: TSMC sales +59.7%; $500M Anthropic stake; Viking +23.2%
  - [japan] Interest Rate (November 16 2026)

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
      "published_utc": "2026-11-17T05:13:31+00:00",
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

