atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-19T06:32:42.500051+00:00
Total: 3000 manchetes

  🇯🇵 Japão          996
  🇨🇳 China          906
  🇹🇼 Taiwan         344
  🇰🇷 Coreia do Sul  754

## O que já está no feed (não repita)

  - [korea] SK hynix launches W2tr financing program to bolster chip suppliers
  - [japan] Fiscal Concerns May Weigh on 20-Year JGB Auction Demand — Market Talk
  - [korea] S.Korea says SK Hynix’s Solidigm listing could violate rules- reports
  - [china] China Q3 GDP Growth Improves
  - [korea] Although Korea Western Power Co. has invested more than 630 billion won in safety-related budgets an..
  - [japan] Rice Prices Key to Japan Inflation Expectations — Market Talk
  - [japan] House of Councilors, Liberal Democratic Party, Ritsumeikan Committee on National Affairs meeting, discussion o
  - [korea] South Korean Won Extends Gains Near 2-Year High
  - [taiwan] Central bank mulls forex intervention after Taiwan dollar losses
  - [korea] SK Hynix bounces from extreme oversold-bear risk stays: Live levels
  - [japan] Nikkei 225 in strong downtrend at JPY 65,000: Live levels
  - [china] China’s CXMT shares slide despite ninefold revenue growth forecast
  - [japan] USD/JPY Seen Range-Bound Ahead of Central Bank Meetings — Market Talk
  - [china] China Fangda Unit's IKK Fangda JV Signs 2.05 Bln Yuan Curtain Wall Works For Stadium In Saudi Arabia
  - [korea] The Bank of Korea is expected to freeze its base interest rate on the 22nd... Weighted at maintaining 3.00% pe
  - [china] China's GDP Growth Accelerates, but Underlying Momentum Remains Weak — Market Talk
  - [china] Asia FX ticks higher; yuan hits 4-yr high after China Q3 GDP beat
  - [china] China stocks inch higher as strong GDP offsets weak AI mood
  - [china] China's Economy Expanded 4.5% in Third Quarter, Powered by Exports — WSJ
  - [korea] Samsung Electronics, SK Hynix Slide as Korea Pension Fund Takes $137 Billion Hit
  - [korea] Samsung and SK Hynix stocks slide; is there a reversal in sight?
  - [korea] Samsung, SK Hynix Slide Causes $137 Billion Hit to Korea Pension
  - [korea] Bitcoin, Korea’s Kospi and Nasdaq Futures Rally as China GDP Beats Estimates
  - [taiwan] Finance minister leads Taiwan delegation to APEC meeting in Hong Kong
  - [china] Iron ore rises as China's economic growth accelerates, steel output climbs
  - [china] Yuan hits 4-year high as strong GDP data tempers need for stimulus
  - [japan] Prime Minister Takaichi secures financial resources for consumption tax reduction “Proceed with review of expe
  - [japan] Yen Steady as Ueda Signals Inflation Near Target
  - [taiwan] Taiwan central bank says currency depreciation reflects global stock market 'turmoil'
  - [china] China GDP growth picks up to 4.5% from 3-year low
  - [china] CITIC Securities: Funding is expected to be relatively loose and the central bank has room to cut interest rat
  - [japan] Japan futures rise as tyre manufacturing resumes; equity selloff weighs
  - [china] Putin proposes summit with Trump and Xi to discuss Ukraine deal, WSJ says
  - [china] China’s new home prices fall again in September as recovery stays elusive
  - [china] China's new home prices fall again as recovery remains elusive
  - [china] China’s economic growth accelerates to 4.5% in third quarter
  - [china] Offshore Yuan Hits Fresh 4-Year High
  - [china] VIEW China's economic growth accelerates to 4.5% in third quarter
  - [japan] Japan Week Ahead: BOJ Policymakers Set for More Rate Hikes While Prime Minister Takaichi in Rough Seas Seeking
  - [china] China industrial output, retail sales beat forecasts in September

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
      "published_utc": "2026-10-19T06:32:42+00:00",
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

