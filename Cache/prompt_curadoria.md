atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-21T01:02:42.154732+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1032
  🇨🇳 China          891
  🇹🇼 Taiwan         350
  🇰🇷 Coreia do Sul  727

## O que já está no feed (não repita)

  - [korea] Producer prices up for 2nd month in Sept. on higher prices of agricultural goods
  - [japan] Japan’s September exports rise 16.7%, helped by chip demand By Reuters
  - [korea] South Korea October 1-20 exports surge 105% on record chip sales
  - [korea] Bank of Korea Expected to Stand Pat Thursday, Poll Shows — Market Talk
  - [japan] Japan shifting to wage-driven inflation phase, finance minister says
  - [china] China uses crude stockpiles, but rising oil imports may curtail draws: Russell
  - [japan] Japan posts bigger-than-expected trade deficit in Sept as export growth slows
  - [japan] Japan’s September exports rise 16.7%, helped by chip demand
  - [japan] Japan's Exports Continued to Rise in September Amid AI Boom
  - [japan] JAPAN SEPT EXPORTS POST 13TH STRAIGHT Y/Y RISE
  - [japan] JAPAN SEPT EXPORTS TO CHINA +8.6% Y/Y, 7TH STRAIGHT RISE (AUG REVISED +20.5%) LED BY CHIP-MAKING EQUIPMENT, RA
  - [japan] MNI: JAPAN SEPT EXPORTS +16.7% Y/Y; AUG +19.3%
  - [japan] Japan September exports rise 16.7% y/y, slower than forecast By Reuters
  - [japan] JAPAN SEPT EXPORTS TO EU +10.5%, 14TH STRAIGHT RISE (AUG +11.0%) , LED BY AUTO, SHIPS, DRUGS
  - [japan] Trade statistics for the first half of this fiscal year: 2.8 trillion yen deficit, 98.8% larger than last year
  - [japan] JAPAN SEPT EXPORTS TO US +22.9% Y/Y, 7TH STRAIGHT RISE (AUG +24.9%), LED BY AUTOS, DRUGS, CHIP-MAKING EQUIPMEN
  - [japan] Japan September exports rise 16.7% y/y, slower than forecast
  - [korea] South Korea October 1-20 exports rise 105.4% year/year
  - [japan] JAPAN SEPT IMPORT Y/Y RISE LED BY CRUDE OIL, CHIPMAKING EQUIPMENT, LNG
  - [japan] Japan Import Growth Slows to 5-Month Low
  - [japan] JAPAN SEPT EXPORT Y/Y RISE LED BY COMPUTER CHIPS, AUTO, CHIPMAKING EQUIPMENT
  - [japan] Japan Export Growth Slows to 4-Month Low
  - [japan] JAPAN SEPT TRADE DEFICIT ¥536.5 BLN (AUG REVISED ¥1,112 BLN DEFICIT); 5TH STRAIGHT DEFICIT; MEDIAN FORECAST ¥7
  - [china] Kazakh borrowers issue billions of yuan debt as China ties tighten
  - [japan] JAPAN SEPT IMPORTS +18.9% Y/Y (AUG +28.0%), 8TH STRAIGHT RISE; MEDIAN FORECAST +19.9%
  - [japan] BREAKING NEWS: Japan logs 536.5 billion yen trade deficit in Sept.
  - [japan] JAPAN SEPT EXPORTS +16.7% Y/Y (AUG +19.3%), 13TH STRAIGHT RISE; MEDIAN FORECAST +21.7%
  - [japan] From wars to El Niño...World food prices become scary at the end of the year (JoongAng Ilbo Japanese version)
  - [japan] Bank of Japan Governor Ueda will attend the House of Representatives Finance and Financial Services Committee 
  - [japan] BOJ to raise rates to 1.50% in December, sticking to quarterly pace: Reuters poll
  - [japan] BOJ to raise rates to 1.50% in December, sticking to quarterly pace: Reuters poll By Reuters
  - [china] Why more Chinese firms are eyeing Thailand over Vietnam after trade war 2.0
  - [japan] BOJ to raise rates to 1.50% in December, sticking to quarterly pace
  - [china] Commerzbank: The central bank’s policy interest rate shifts to overnight reverse repurchase, and the RMB will 
  - [korea] South Korea Producer Inflation Eases Slightly
  - [china] Even the legendary man who transformed Shanghai and Chongqing was taken away... The shadow of China's economy,
  - [japan] Consumption tax reduction bill: Opposition parties offer counterproposals, ruling party seeks compromise to en
  - [japan] Will AI really push up long-term interest rates? The key is the difficult issue of determining whether product
  - [japan] Japan oil refiner Idemitsu to import non-Mideast LNG
  - [japan] One year since the Takauchi Cabinet was established, it is putting all its effort into enacting the consumptio

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
      "published_utc": "2026-10-21T01:02:42+00:00",
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

