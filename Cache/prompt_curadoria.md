atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-16T12:22:42.909002+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1086
  🇨🇳 China          867
  🇹🇼 Taiwan         332
  🇰🇷 Coreia do Sul  715

## O que já está no feed (não repita)

  - [china] Li Auto raises 1.6B Yuan for chip business expansion
  - [taiwan] Taiwan Plans $4 Billion Texas AI Hub for Nvidia Supply Chain
  - [japan] BREAKING NEWS: Japan data broadly in line with BOJ outlook since Sept. policy meet: Ueda
  - [japan] BREAKING NEWS: BOJ to keep raising rates, adjust monetary easing: Ueda
  - [japan] Japan's economy is progressing as expected, says Bank of Japan president (Kyodo News)
  - [japan] BOJ chief vows to keep raising rates, anchor inflation around target
  - [japan] Bank of Japan Governor says underlying inflation is approaching 2% (Kyodo News)
  - [china] Zenta Group Subsidiary ZentoAI Signs Binding MOU for Strategic Acquisition in China
  - [taiwan] TSMC’s ‘Leave No Food On The Table’ Pledge Signals More AI Chip Investment, Morningstar Says
  - [taiwan] Taiwan lawmakers pass health insurance premium subsidies for seniors
  - [china] Shanghai Bright Power Semiconductor Says Lock-Up Period For 23.6 Million Shares To End
  - [taiwan] Mitsubishi Electric: To Sell 50% Stake In Subsidiary Mitsubishi Electric Mobility To Hon Hai Precision Industr
  - [china] Beijing seeks tighter grip on AI exports amid US rivalry
  - [taiwan] Hon Hai subsidiary acquires 50% stake in Mitsubishi Electric Mobility
  - [korea] South Korea warns of 200-times leveraged bets on Samsung, SK Hynix
  - [china] Central China Real Estate Posts September Contracted Sales Of RMB438 MLN
  - [china] Shoucheng Holdings Says Fund Managed By Unit Invested In Shanghai Yuanhuan Intelligent Technology
  - [china] Shenzhen hongfuhan Technology's Unit To Invest 1.0 Billion Yuan In Project
  - [china] China Proposes Export Controls on AI Technologies
  - [china] PBOC’s Pan Touts Yuan Assets to Investors at Deutsche Bank Event
  - [china] China's Xi stresses importance of national computing power network
  - [china] China to add AI, biopharma and solar tech to export control list
  - [taiwan] REG - Hon Hai Prec.Ind.Co - Subsidiary Announces Cash Dividend Distribution
  - [korea] USD/KRW: Goldman Sachs sees Korean won strengthening
  - [japan] Bank of Japan Governor Ueda emphasizes in his greeting that he will “continue to raise policy interest rates” 
  - [china] China Petroleum Engineering Says January-September New Contracts Totalled 105.9 Billion Yuan
  - [china] China Moves to Restrict Exports of Some Solar Technologies
  - [korea] SK hynix tops list of most sought-after firms among S. Korean job seekers: survey
  - [korea] Kospi rebound after 20% drop as foreigners buy; AI doubts trim Samsung, SK Hynix gains
  - [japan] Global inflation debate puts BOJ rate-hike pace in spotlight
  - [china] China Proposes Export Controls on AI Models, Chips and Agents
  - [china] China Plans AI Tech Export Curbs to Manage Security Risks
  - [japan] Consumption tax reduction bill agreed to be discussed on 20th; Liberal Democratic Party and Democratic Party o
  - [korea] The Export-Import Bank of Korea has set out to establish a system to evaluate and select candidate p..
  - [korea] Entering a rate hike phase, the upper end of mortgage fluctuation rates of major commercial banks ha..
  - [china] Developing | China mulls new tech export bans covering AI, biotech and solar power
  - [china] Jinko Solar Sees 9-Month Net Loss At 3.0 Billion Yuan - 3.6 Billion Yuan
  - [china] China proposes adding 40 AI, biotech, solar technologies to export control list
  - [china] Poly Developments September Contract Sales Down 21.1% Y/Y To 16.2 Billion Yuan
  - [china] Tardy China Stimulus Sets Up Second Quarter of Sub-Target Growth

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
      "published_utc": "2026-10-16T12:22:43+00:00",
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

