atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-30T09:32:46.049311+00:00
Total: 3000 manchetes

  🇯🇵 Japão          920
  🇨🇳 China          847
  🇹🇼 Taiwan         365
  🇰🇷 Coreia do Sul  868

## O que já está no feed (não repita)

  - [china] Anhui Jianghuai Automobile Group Q3 Net Loss At 391.8 Million Yuan
  - [taiwan] Soaring inflation erodes purchasing power, and French people tighten their pants to survive
  - [china] Henan Dayou Energy Q3 Net Loss At 436.4 Million Yuan
  - [china] Shanghai Electric Power: Q3 profit nearly vanished as lower tariffs and higher fuel costs pressured results
  - [china] Next week, 1.749 billion yuan of reverse repos will mature in the central bank’s open market.
  - [china] Central Bank: Starting from November 2, 2026, bidding for overnight reverse repurchase operations will be laun
  - [china] China's central bank to conduct overnight reserve repos every working day from November 2, rate at 1.25%
  - [japan] Market moves ``as expected'' at Bank of Japan meeting, with limited movement even after announcement of accele
  - [china] Central Bank: Starting from November 2, bidding for overnight reverse repurchase operations will be launched e
  - [japan] Is achieving the 2% target with good price increases that was initially aimed at a dream that cannot be fulfil
  - [china] Central Bank: Conduct bidding for overnight reverse repurchase operations every working day
  - [japan] Why did the Bank of Japan aim for 2%? Adjust the economy and prices by moving interest rates
  - [china] Yonyou Network Technology Q3 Net Loss At 318.6 Million Yuan
  - [japan] Bank of Japan Is Likely to Roll out Two More Hikes — Market Talk
  - [china] Jinko Solar Q3 Net Loss At 290.4 Million Yuan
  - [taiwan] Taiwan's economic indicator signals 'booming' for 10th straight month on AI-driven shipments
  - [china] Chinese Yuan traded below 6.65
  - [japan] Japan to consider how to handle BOJ ETF surplus in FY2027 budget, Katayama says
  - [korea] The National Assembly has begun reviewing the 2027 budget, which is worth 821 trillion won. Next yea..
  - [japan] Chief Cabinet Secretary Kihara: ``Appropriately operate monetary policy to achieve the 2% price stability targ
  - [china] China Life Insurance Q3 Net Loss At 45.1 Billion Yuan
  - [japan] BOJ says 2% inflation target generally achieved, maintains policy rate
  - [japan] BOJ's Ueda Hails Inflation Progress But Says Battle Isn't Over
  - [china] Trump’s days of running US-China relations on personal ties are numbered
  - [japan] BOJ's Decision to Hold Likely to Have Limited Impact on Yen — Market Talk
  - [taiwan] Chip design company MediaTek says growth in demand for AI will "absolutely" continue
  - [china] Flat Glass Q3 Net Loss At 472.7 Million Yuan
  - [japan] [Key points explained] Reading Bank of Japan Governor Ueda's press conference & economists' predictions for in
  - [china] New Hope Liuhe Q3 Net Loss At 865.8 Million Yuan
  - [china] China set to lose LNG import crown to Japan on weak demand
  - [taiwan] Taiwan Q3 GDP Growth Beats Expectations
  - [japan] Yen Rises Against Majors
  - [taiwan] Chip designer MediaTek says AI demand growth will continue 'for sure'
  - [japan] BOJ May Move Away From Predictable Hiking Cadence Beyond March 2027 — Market Talk
  - [china] BBMG Q3 Net Loss At 1.5 Billion Yuan
  - [japan] BOJ chief Ueda says 2% inflation goal not yet sustainably achieved
  - [taiwan] Taiwan Q3 preliminary GDP beats forecasts on solid AI demand
  - [japan] USD/JPY Falls for 3rd Straight Day: Yen Supported by BoJ Decision
  - [japan] Today's Oha Biz October 30th (Friday) What is the terminal rate (achieved interest rate)?
  - [japan] Bank of Japan Likely to Wait Before Further Tightening — Market Talk

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
      "published_utc": "2026-10-30T09:32:46+00:00",
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

