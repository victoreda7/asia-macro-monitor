atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-15T02:32:44.350799+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1124
  🇨🇳 China          846
  🇹🇼 Taiwan         292
  🇰🇷 Coreia do Sul  738

## O que já está no feed (não repita)

  - [japan] BOJ Board Member Indicates Further Room for Rate Hikes
  - [korea] Why a memory chip glut could be Korea's weapon against China
  - [japan] BoJ Koeda Urges Timely Rate Hikes Amid Inflation Risks
  - [korea] Exclusive-SK Hynix conditions new US factory on more US chip equipment exports to China, sources say
  - [korea] Why is SK Hynix stock plunging today?
  - [japan] BOJ should not be overly cautious in raising rates, board member Koeda says
  - [korea] Why is Samsung Electronics stock plunging today?
  - [japan] Bank of Japan council member emphasizes continuing interest rate hikes: ``There is no need to be cautious'' (K
  - [taiwan] TSMC Set to Post Sixth Consecutive Quarter of Record Profit, Thanks to AI Boom
  - [taiwan] TSMC expected to report sixth straight quarter of record profit thanks to AI boom
  - [china] China stocks fall, led by tech, as US inflation stokes Fed fears
  - [china] "Three polarizations" are occurring in the Chinese economy, where domestic demand has fallen sharply...The rea
  - [japan] Stock prices temporarily fell by more than 3,000 yen against the backdrop of expectations for a US interest ra
  - [korea] The cancellation of land supply contracts by the Korea Land and Housing Corporation (LH) increased a..
  - [japan] Bank of Japan member says there is "no need to be cautious" in raising interest rates (Kyodo News)
  - [japan] BOJ should not be overly cautious raising rates, board member Koeda says
  - [china] CHINA PBOC CONDUCTS CNY45 BLN VIA 7-DAY REVERSE REPO THURS
  - [korea] Korean memory makers accept ASML parts price hike, leaving TSMC as the open question
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7253 THURS VS 6.7249
  - [korea] Samsung Electronics Co. was counted as the largest net purchase by high-yield investors of Mirae Ass..
  - [japan] Speech by Board Member KOEDA in Kumamoto (Economic Activity, Prices, and Monetary Policy in Japan)
  - [japan] Japan futures fall as Tokyo equities slump, China imports weaken
  - [korea] Hot US inflation hammers Kospi nearly 6% lower as chips buckle
  - [japan] Summary of the "Meeting on Market Operations" (October 2026)
  - [taiwan] Key facts: TSMC (2330) Q3 revenue NT$1.49T record; 2026 capex $60–64B
  - [japan] Japan’s Katayama Renews Warnings on Yen After US CPI Heats Up
  - [japan] Asian markets sell off as AI trades crumble after hot US CPI data
  - [japan] Japan’s Nikkei Slumps on Hot US Inflation
  - [korea] Seoul stocks open sharply lower on lingering concerns over AI, US inflation
  - [china] Securities Star morning news summary on October 15: The central bank released the latest social financing data
  - [korea] Kospi plunges nearly 6% as foreigners dump chip stocks
  - [japan] Japan's Nikkei tumbles as tech stocks hammered on US rate hike worries
  - [korea] (LEAD) Seoul stocks open sharply lower on lingering concerns over AI, U.S. inflation
  - [korea] If I get a housing pension of 2 million won per month, I think I'll be able to travel leisurely and..
  - [japan] How can eel pie companies eliminate departmental deficits?
  - [taiwan] Fujifilm to expand Arizona semiconductor materials output
  - [china] The central bank will launch a 700 billion yuan buyout reverse repurchase operation. In September, imports and
  - [korea] Samsung Semiconductor Highlights 400+ Layer Flash Powering Agentic AI
  - [china] The central bank will launch a 700 billion yuan buyout reverse repurchase operation
  - [korea] Aftermath of interest rate hike… Deposits with high interest rates in the 4% per annum range appear in the ban

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
      "published_utc": "2026-10-15T02:32:44+00:00",
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

