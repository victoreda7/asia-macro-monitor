atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-13T03:02:42.745431+00:00
Total: 3000 manchetes

  🇯🇵 Japão          986
  🇨🇳 China          865
  🇹🇼 Taiwan         309
  🇰🇷 Coreia do Sul  840

## O que já está no feed (não repita)

  - [taiwan] TSMC seeks to back next chip titan with new investment arm
  - [japan] Obayashi Corporation - To Buy Back Up To 2.9% Of Own Shares Worth 30 Billion Yen
  - [korea] Cloud: Upbit opens spot trading in KRW, BTC and USDT markets - 13 Nov 2026
  - [japan] Toda Corporation Says It Will Buy Back Up To 2.7% Of Own Shares Worth 10 Billion Yen
  - [china] The U.S. Congress has launched a bipartisan effort to regulate semiconductors...It will also affect Samsung El
  - [japan] Japan futures set for first weekly gain in five as yen weakens, oil jumps
  - [korea] South Korean won gains most among tepid Asian FX
  - [korea] i3system: Infrared-led growth lifted 9M revenue and operating income; orders reached KRW 151.82bn.
  - [japan] Japan’s finance minister vows action as yen breaches 160 threshold
  - [korea] Samsung, SK hynix gain over 2% despite Nvidia sell-off
  - [japan] Dollar near 19-month high on Fed hike bets, yen tests 160
  - [china] The central bank announced: Today it will launch a 364 billion yuan overnight reverse repurchase operation
  - [china] The central bank launched a 300 billion yuan 7-day reverse repurchase operation in the open market today
  - [japan] Japan's Finance Minister Warns Against Rapid Yen Moves
  - [china] CHINA PBOC CONDUCTS CNY300 BLN VIA 7D REVERSE REPO FRI
  - [china] CHINA PBOC CONDUCTS CNY364 BLN VIA O/N REVERSE REPO FRI
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7152 FRI VS 6.7174
  - [china] Central Bank: Launching 364 billion yuan overnight reverse repurchase operation today
  - [china] On November 13, the central bank launched a 364 billion yuan overnight reverse repurchase operation.
  - [korea] BHI: 9M sales rose, earnings strengthened, and the order backlog reached KRW 2.458tn
  - [china] The central bank launched a 364 billion yuan overnight reverse repurchase operation
  - [china] The Central Bank of China: Today it launched a 364 billion yuan overnight reverse repurchase operation, with a
  - [japan] Bank of Japan's Councilor Asada gives speech in Nagasaki: Future rate hike pace "needs to be kept in mind" (Na
  - [japan] Japan MOF To Auction Y3.1T Of TD-Bills Nov 20
  - [japan] Yen market price temporarily fell to the 160 yen level to the dollar, the weakest yen level in about 2 months
  - [japan] BREAKING NEWS: Japan to take appropriate action vs. yen slide if necessary: finance chief
  - [japan] Yen jumps in ‘jittery’ trading after hitting 160 against US dollar
  - [china] China’s access to Nvidia chips in doubt as curbs gain traction in US Congress
  - [japan] JGB Yields Rise After Selloff in U.S. Treasurys Overnight — Market Talk
  - [japan] U.S. demands Japan triple troop-hosting costs to 3 tril. yen over 5 yrs
  - [china] HSBC Says Yuan Could Double Its Global Payments Share
  - [japan] Japan's finance minister warns of potential action against FX volatility
  - [korea] Why is Samsung Electronics stock rallying today?
  - [japan] Japan Q3 GDP Seen Slightly Up as Capex Offsets First Private Consumption Drop in 10 Quarters
  - [japan] Nissan Motor Co., Ltd. Stock 12‑Month Price Target Cut to JPY 366.43, Implies 32% Upside
  - [japan] US Treasury bought yen in July; Fed made no solo FX interventions in Q3
  - [japan] Bank of Japan Deputy Governor Himino attends a special committee meeting of the House of Councilors at 1:26 p.
  - [japan] BREAKING NEWS: U.S. government bought 79.4 billion yen in forex intervention in July: Fed
  - [japan] Yen Falls to Key 160 Level Per Dollar, Raising Intervention Risk
  - [japan] House wine remains the same even though Doria prices have increased... Why Saizeriya, which has been reconfirm

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
      "published_utc": "2026-11-13T03:02:42+00:00",
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

