atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-02T01:22:45.459235+00:00
Total: 3000 manchetes

  🇯🇵 Japão          926
  🇨🇳 China          865
  🇹🇼 Taiwan         361
  🇰🇷 Coreia do Sul  848

## O que já está no feed (não repita)

  - [korea] Sk Square Co., Expects More Than 6.2 Trln Won Of Dividend Income From Sk Hynix
  - [japan] Japan MOF To Auction Y3.0T Of TD-Bills Nov 9
  - [japan] Japan Manufacturing PMI Slips To 53.3 In October - S&P Global
  - [japan] Attendance at Bank of Japan meeting: ``It depends on the situation at the time,'' Economy and Finance Minister
  - [china] Bond market early participation November 2 | The central bank's policy interest rate "change anchor" was imple
  - [korea] Bank of Korea Surveys Banks and Securities Firms on Virtual Asset Business Risks
  - [china] China's robot makers already dominate the moves. Now the race for intelligence begins
  - [korea] South Korea Manufacturing Growth Slows to 8-Month Low
  - [japan] Japan’s October factory growth slows as costs pick up, PMI shows By Reuters
  - [japan] Japan finance minister: government remains ready to take action against disorderly FX moves
  - [taiwan] Taiwan Manufacturing Maintains Momentum
  - [japan] Japan’s October factory growth slows as costs pick up, PMI shows
  - [korea] South Korea factory activity growth slows to 8-month low, PMI shows
  - [china] The central bank has 1.749 billion yuan of open market reverse repos due this week
  - [china] The central bank has 1.749 billion yuan of open market reverse repos due this week_Company News_Finance
  - [korea] The US Dairy Export Association (USEC) will introduce a unique pairing set that combines Korean trad..
  - [korea] That's why it has become a country that is less able to grow than South Korea...The obvious reason why Japan h
  - [japan] Why did he accept the position of Governor of the Bank of Japan, something he once hesitated to do? Haruhiko K
  - [japan] Will the real estate myth end with the Bank of Japan interest rate hike? “Aggressive cash conversion” promoted
  - [korea] South Korea is on the verge of achieving a record $1 trillion in annual exports this month thanks to..
  - [taiwan] Bulgarian presidential runoff exit poll: Acting President Jotova wins | International
  - [japan] Debate continues over the abolition of Japan Post Bank's savings interest cap
  - [japan] Consumption tax reduction bill Ruling party: “Consults for vote” Opposition: “Prime Minister to attend”
  - [china] China's BYD Continues Massive EV Exports. It Isn't Helping. — Barrons.com
  - [korea] South Korea set to become world’s 4th country to hit $1 trillion in annual exports
  - [japan] Japan Weeks Ahead: BOJ Has Cleared First Major Goal of Lifting Near 2% But Still Needs to Anchor Price Rises a
  - [taiwan] The 20% problem: why Taiwan's imported equipment parts still carry 70% of the cost
  - [china] The People's Bank of China will conduct overnight reverse repurchases every working day starting from 11/2 to 
  - [korea] Top global stories this week: Shell, HSBC, SK Hynix among notable names
  - [taiwan] The pioneer behind TSMC's FinFET leap: a personal look at Chenming Hu
  - [taiwan] Six decades in the making: Why the world can't easily copy Taiwan's chip ecosystem
  - [taiwan] Benefitting from AI investment, South Korea's exports doubled in October, the largest increase in half a centu
  - [taiwan] South Korea's exports nearly doubled in October thanks to AI investment, the largest increase in half a centur
  - [china] China’s Communist Party demands loyalty, vows to tighten discipline
  - [korea] Samsung chief Lee visits Japan chip packaging lab
  - [taiwan] Nuit Blanche Taipei brings night of art, performances to Yuanshan
  - [china] China's BYD extends sales growth streak on strong exports
  - [japan] Bank of Japan Maebashi Branch September Tankan flat rate at +15 for third consecutive period (Gunma TV)
  - [japan] Bank of Japan Maebashi Branch September Tankan flat at +15 for third consecutive period (Gunma TV)
  - [china] Tomorrow, the central bank will make important adjustments! A look at next week’s major financial events

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
      "published_utc": "2026-11-02T01:22:45+00:00",
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

