atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-19T02:02:43.476621+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1008
  🇨🇳 China          899
  🇹🇼 Taiwan         343
  🇰🇷 Coreia do Sul  750

## O que já está no feed (não repita)

  - [china] China Sep Industrial Output +5.5% On Year; Market Expected +5.5%
  - [china] China's Q3 GDP growth accelerates to 4.5%, beating f'cast
  - [china] China 3Q GDP +4.5% on Year; Market Expected +4.4%
  - [china] China Sep Industrial Output +0.61% On Month
  - [china] China Jan-Sep GDP +4.6% on Year
  - [china] China 3Q GDP +1.2% on Quarter
  - [china] The central bank launches 80 billion yuan 7-day reverse repurchase operation today
  - [china] China's Home Price Decline Eased Slightly in September
  - [china] China’s EV Exports Double in September Ahead of Tax Rebate Cut
  - [china] Yuan Steady Ahead of Major Chinese Economic Data — Market Talk
  - [china] China's new home prices fall in September as recovery remains elusive
  - [china] CHINA PBOC CONDUCTS CNY80 BLN VIA 7-DAY REVERSE REPO MON
  - [japan] Japan's 10-year yield falls on risk aversion, debt issuance pledge
  - [china] CHINA SETS YUAN CENTRAL PARITY AT 6.7208 MON VS 6.7220
  - [china] China New Home Prices Drop the Least in 9 Months
  - [china] Yang Caifang, senior statistician of the Urban Department of the National Bureau of Statistics, interprets the
  - [china] Changes in sales prices of commercial housing in 70 large and medium-sized cities in September 2026
  - [japan] BOJ may need to tighten faster if inflation beats forecast, IMF says
  - [japan] Inflation Near 2% as AI Demand Adds Pressure: BoJ Gov Ueda
  - [japan] Now is the time when it is more important to stabilize the underlying price index at around 2% - Bank of Japan
  - [korea] SK Hynix crashes -20.6% below 20-period MA: Live levels
  - [japan] Yen Consolidates, But May Be Supported by Risk-Off Mood — Market Talk
  - [korea] Deputy Prime Minister and Minister of Finance and Economy Lee Hyung-il predicted a growth rate of 3...
  - [korea] South Korea finmin: 3.4%-3.6% economic growth possible for 2026, Yonhap says
  - [china] China proposes export controls on solar-manufacturing technologies
  - [japan] Japan PM vows to control size of debt issuance
  - [korea] The won per dollar reached its highest level in two years and one month due to strong exports center..
  - [japan] BOJ chief says underlying inflation 'quite close' to price goal
  - [japan] BOJ Governor Ueda says underlying inflation ’quite close’ to 2% target
  - [japan] Bank of Japan Governor Ueda will attend the House of Councilors Budget Committee meeting from 9 a.m. - Diet so
  - [china] China’s Q3 GDP growth set to pick up as exports power ahead
  - [taiwan] Weekly Recap: Q3 revenue surge at TSMC and Arizona fab mass production in Q3 2027
  - [korea] Chey Tae-won: “If I went back to my 20s, I wouldn’t have gone into semiconductors” ... What would his startup 
  - [china] How China made climate resilience part of its economic growth strategy
  - [japan] An uneasy government and riots in France, etc. = Bank of Japan's uneasy jinx (Hirotoshi Kubozono) - Expert
  - [japan] <Challenging the two powerhouses TOTO and LIXIL> The "two changes" that have enabled Takara Standard to make s
  - [japan] Three traps that prevent you from assuming that the Bank of Japan will continue to raise interest rates becaus
  - [japan] Consumption tax reduction related bill to be debated tomorrow, debate between ruling and opposition parties in
  - [japan] NRI's Rs.3.41 crore FCNR deposits flagged as unexplained money after tax officer mistook yen for rupees, ITAT 
  - [china] China’s proposed solar curbs raise stakes for overseas manufacturers

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
      "published_utc": "2026-10-19T02:02:43+00:00",
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

