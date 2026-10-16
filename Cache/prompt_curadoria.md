atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-16T16:22:41.971706+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1087
  🇨🇳 China          866
  🇹🇼 Taiwan         331
  🇰🇷 Coreia do Sul  716

## O que já está no feed (não repita)

  - [korea] Seoul stocks rebound over 2% on eased chip rout, Fed bets
  - [japan] The underlying price increase rate is “approaching 2%”; Bank of Japan Governor Ueda says, “We cannot tolerate 
  - [china] China seeks tighter controls on AI-related exports amid rivalry with US
  - [china] EU urges safeguards against Chinese chemicals, machinery imports
  - [china] Chinese premier chairs State Council executive meeting
  - [japan] Fiscal System Council proposes use of imported rice for stockpiled rice
  - [japan] BOJ's Ueda says inflation can't be allowed to rise further
  - [japan] Bank of Japan Governor maintains interest rate hike stance, keeping a close eye on energy prices and AI demand
  - [japan] BOJ chief vows to keep raising rates, anchor inflation around target
  - [japan] Bank of Japan Governor Ueda emphasizes stance on continuing interest rate hikes: ``We cannot accept any furthe
  - [japan] Bank of Japan Governor Ueda calls upward movement in prices ``unacceptable'', approaches 2% target, continues 
  - [japan] Bank of Japan Governor Ueda calls upward price hike ``unacceptable'', approaches 2% target, continues rate hik
  - [japan] Decision on 2% underlying inflation rate will be thoroughly discussed at October meeting; economy is in line w
  - [japan] BOJ Must Ensure Underlying Inflation Doesn't Go Above 2%, Ueda Says
  - [china] Shenzhen Techwinsemi Sees 9-Month Net Profit At 8.7 Billion Yuan-9.0 Billion Yuan
  - [japan] Instinct Bio Returns to Profit and Grows Revenue Nearly 10% in Yen Terms in First Half of Fiscal 2026
  - [japan] Instinct Bio Technical Company Holdings Inc. (BIOT) Returns To Profit; Revenue Up ~10% YoY in Yen
  - [taiwan] Taiwan Eyes $4 Billion Texas Hub to Supercharge Nvidia's AI Supply Chain
  - [japan] BREAKING NEWS: Stabilizing underlying inflation around 2% is key goal for BOJ: Ueda
  - [china] Li Auto raises 1.6B Yuan for chip business expansion
  - [taiwan] Taiwan Plans $4 Billion Texas AI Hub for Nvidia Supply Chain
  - [japan] BREAKING NEWS: Japan data broadly in line with BOJ outlook since Sept. policy meet: Ueda
  - [japan] BREAKING NEWS: BOJ to keep raising rates, adjust monetary easing: Ueda
  - [china] Beijing seeks tighter grip on AI exports amid US rivalry
  - [japan] Japan's economy is progressing as expected, says Bank of Japan president (Kyodo News)
  - [japan] ``We will raise the policy interest rate,'' says the Bank of Japan Governor (Kyodo News)
  - [japan] Bank of Japan Governor says underlying inflation is approaching 2% (Kyodo News)
  - [china] Zenta Group Subsidiary ZentoAI Signs Binding MOU for Strategic Acquisition in China
  - [taiwan] TSMC’s ‘Leave No Food On The Table’ Pledge Signals More AI Chip Investment, Morningstar Says
  - [taiwan] Taiwan lawmakers pass health insurance premium subsidies for seniors
  - [china] Shanghai Bright Power Semiconductor Says Lock-Up Period For 23.6 Million Shares To End
  - [taiwan] Mitsubishi Electric: To Sell 50% Stake In Subsidiary Mitsubishi Electric Mobility To Hon Hai Precision Industr
  - [taiwan] Hon Hai subsidiary acquires 50% stake in Mitsubishi Electric Mobility
  - [korea] South Korea warns of 200-times leveraged bets on Samsung, SK Hynix
  - [china] Central China Real Estate Posts September Contracted Sales Of RMB438 MLN
  - [china] Shoucheng Holdings Says Fund Managed By Unit Invested In Shanghai Yuanhuan Intelligent Technology
  - [china] Shenzhen hongfuhan Technology's Unit To Invest 1.0 Billion Yuan In Project
  - [china] China Proposes Export Controls on AI Technologies
  - [china] PBOC’s Pan Touts Yuan Assets to Investors at Deutsche Bank Event
  - [china] China's Xi stresses importance of national computing power network

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
      "published_utc": "2026-10-16T16:22:42+00:00",
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

