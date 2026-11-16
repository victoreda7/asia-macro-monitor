atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-16T06:32:42.285129+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1010
  🇨🇳 China          877
  🇹🇼 Taiwan         302
  🇰🇷 Coreia do Sul  811

## O que já está no feed (não repita)

  - [japan] Net Protections Holdings, Inc. - To Buy Back Up To 3.5% Of Shares Worth 1.2 Billion Yen
  - [korea] Benchmark rate for banks' mortgage loans continues to rise
  - [japan] Asian markets mostly lower as weak Japan GDP, soft China data, and Nvidia caution weigh
  - [china] Asia stocks tumble as chipmakers slide and weak China data adds pressure
  - [korea] Hyundai Green Food: 9M earnings improved, while working-capital outflows and buybacks shaped cash deployment
  - [japan] Hawkish BOJ policymaker Takata calls for swift hike in rates to ’good’ position
  - [china] China's October retail sales ease to 0.4%, factory output slows to 4.8%, while jobless rate dips to 5.1%
  - [taiwan] Qisda affiliate Ace Pillar deepens semiconductor and AI automation push, expanding into wafer regeneration and
  - [japan] Japan’s economy contracts 0.1% annualized in Q3; September industrial output rebounds 2.0%
  - [taiwan] Interest rate hike in December? Yang Jinlong: Three key points need to be considered: inflation and lending po
  - [korea] Korea's wage, productivity gaps widen amid chip-led growth: KDI
  - [japan] Weak Consumption Likely to Keep Japan's Economy in Low Gear — Market Talk
  - [japan] Weak Japan Consumption Could Deepen BOJ Board Divisions — Market Talk
  - [china] China factory output, retail sales miss forecasts in Oct amid weak domestic demand
  - [korea] Samlip, which emerged from the deficit in the first quarter of this year, has continued to improve i..
  - [japan] Hawkish BOJ Member Urges Nimble Rate Hikes
  - [japan] Bank of Japan member Takada (Reuters): Set policy interest rates to neutral levels in advance and raise intere
  - [japan] Japan's Economic Growth Trend Likely to Remain Intact — Market Talk
  - [china] China’s Industrial Output Growth Slows
  - [japan] BOJ hawk Takata calls for quick pace of rate hikes
  - [china] China’s Retail Sales Growth Slows to 0.4%, Missing Forecasts
  - [japan] Dollar extends gains, yen looks past soft Japan GDP data
  - [china] China's economy falters in October as factory output, retail sales miss forecasts
  - [japan] Asia FX muted as dollar holds near 19-mth high; yen steady after weak GDP
  - [china] HKEX Launches First-Ever Offshore Yuan Bond Index
  - [china] China’s ZAI, Minimax tumble as Nvidia row drives fears of more chip restrictions
  - [korea] SK Hynix in 24/7 race to complete colossal chip plant
  - [china] China is accused of manipulating the iron ore trade and the Australian government is worried about the impact 
  - [korea] STIC Investments: Lower fee revenue, stronger profit and KRW 10.3tn in fund commitments defined 9M 2026
  - [taiwan] Taiwan's Taiex Extends Losses as Chip Makers Weigh — Market Talk
  - [china] Hong Kong exchange launches first offshore yuan bond index
  - [taiwan] Taiwan will take inflation and measures taken by other countries into account when setting interest rates
  - [taiwan] Taiwan to consider inflation, other countries' moves when deciding interest rates
  - [korea] A major semiconductor manufacturing base in South Korea is unveiled to help foster small and medium-sized ente
  - [china] China Industrial Output Rises 4.8% On Year
  - [taiwan] Taiwan's Nanya and Winbond adopt EUV, challenging South Korean DRAM dominance
  - [china] Yuan steady as disappointing economic data offset by robust corporate year-end demand
  - [japan] Japan's $12 bln chip deal courts needless strife
  - [china] China's economy softens across the board as factory output, spending slow
  - [taiwan] AI giants shift decarbonization pressure upstream, testing Taiwan's chip supply chain

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
      "published_utc": "2026-11-16T06:32:42+00:00",
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

