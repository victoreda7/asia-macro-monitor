atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-17T10:22:55.699243+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1035
  🇨🇳 China          899
  🇹🇼 Taiwan         306
  🇰🇷 Coreia do Sul  760

## O que já está no feed (não repita)

  - [china] JSW Steel CEO flags Chinese exports, trade barriers as key challenges
  - [taiwan] The United States strictly controls the export of advanced AI chips: some orders may be delayed | Sankei
  - [korea] Samsung and Apple near long-term DRAM supply agreement
  - [china] Shanghai Runda Medical Technology Plans Bond Issuance
  - [japan] House of Councilors Special Committee Confirms Second Question Asked for Prime Minister Takaichi's Attendance 
  - [japan] Yomiuri: Asics Aims for 1.5 Trillion Yen in Net Sales for 2029
  - [korea] [Counterattack of digital dollar hegemony] Strengthening dollar hegemony through financial innovation... Bank 
  - [japan] Local Finance Council “Take concrete steps through tax reform to correct uneven distribution of taxes”
  - [taiwan] New rules for US exports of AI chips to prevent transshipment Quanta and Wistron’s assessment will not be affe
  - [korea] Who sets the base interest rate and how?: A summary of the Monetary Policy Committee
  - [china] China will adopt "necessary measures" after new US restrictions on chip exports
  - [china] Chinese envoy says restrictions on exports of equipment for the chip industry threaten the unfreezing of trade
  - [china] Chinese envoy says chip equipment export curbs threaten EU-China trade thaw
  - [china] China's JD Logistics Q3 revenue rises on growth in external integrated supply chain customers
  - [china] US to curb China’s access to AI chips as Trump heads to Asia
  - [china] US confirms investigation into Megaspeed for alleged diversion of chips to China
  - [taiwan] AI Server Tracker: AI upgrades spark structural shift across Taiwan's PCB supply chain amid rising material co
  - [china] Chip Stocks Slide as US Sets New Curbs on China’s Compute Access
  - [china] China stocks dip as US chip curbs weigh sentiment, internet majors slide
  - [korea] Although the local stock market is sluggish due to weak semiconductor stocks, Celltrion has risen ne..
  - [china] Exclusive-China taps US AI models to train homegrown rivals as chip curbs bite
  - [china] Clampdown on China Chip Loophole Puts Billions in Loans at Risk
  - [taiwan] AI server tracker: TSMC, Alchip post big October gains powered by 2nm and ASIC orders
  - [korea] [Exclusive] 1 Trillion Won Investment in Rare Earth Supply Chain... POSCO International Eyed for National Grow
  - [china] New wave of insolvency in China's real estate sector causes credit risk to resurface
  - [korea] South Korea tightens university exam checks to screen for hidden cameras
  - [taiwan] The catering industry cannot withstand inflation. Five brands in Wacheng will increase their prices by about 3
  - [china] Before the Trump-Xi meeting, the US strictly controlled the export of advanced AI chips and Beijing approved e
  - [china] Key facts: Apollo Go; Kunlunxin Listing; Cloud Cash Flow 2.8B Yuan
  - [japan] Understanding the loans of the government, the Bank of Japan, and credit unions; analyzing the soundness of ma
  - [china] U.S. Chip Curbs Pose Double-Edged Sword for China AI Industry — Market Talk
  - [china] Nvidia to halt chip sales to data centers renting over half to China - report
  - [china] Nvidia warns chip buyers of legal risks tied to China AI access, CNBC reports
  - [korea] Higher interest rates, sluggish consumer spending take toll on Korea’s credit card firms
  - [china] Nvidia warns chip buyers about legal risks related to access to AI in China, according to CNBC report
  - [korea] “Key Players in Accelerating the $1 Trillion Export Milestone”... World Class Products Expand to 1,100 Compani
  - [japan] Stock prices fall Sell orders centered on AI and semiconductor related stocks
  - [china] Secondhand Home Prices Rise in Fewer Major Chinese Cities
  - [korea] Kospi Falls for Fourth Straight Session; Chip, Defense Stocks Retreat
  - [korea] S. Korea set to achieve US$1 trillion export milestone for 1st time

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
      "published_utc": "2026-11-17T10:22:55+00:00",
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

