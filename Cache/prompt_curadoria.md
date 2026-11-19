atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-19T21:12:46.859863+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1014
  🇨🇳 China          912
  🇹🇼 Taiwan         326
  🇰🇷 Coreia do Sul  748

## O que já está no feed (não repita)

  - [china] Bipartisan panel says China 'doubling down' on control of pharma supply chain
  - [china] Paying close attention to the impact of the US-China-Russia summit meeting Strengthening cooperation with alli
  - [korea] Producer prices drop in Oct. on lower food prices
  - [japan] Is there a sharp rise in ``eat-in tax evasion'' due to the food tax cut?The National Tax Agency's opinion on c
  - [china] The large influx of Chinese cars has led to excessive competition in the Australian car market...Sellers are i
  - [japan] 〈Buy it! 〉Who is right about the doubling of sales of government bonds to individuals: individuals who think i
  - [taiwan] "Full tuition fee exemption, 50,000 yen monthly scholarship" Reasons why Taiwanese universities treat Japanese
  - [korea] [Defense Industry] Interceptor missiles are classified as "weapons" like rifles, and they are told to "repay t
  - [japan] Consumption tax reduction bill: support from Komeito expected to support lower income limit of 560,000 yen
  - [korea] At 4 p.m. on the 17th, Incheon Arenas Yeongjong Logistics Center, one of the forward export bases of..
  - [china] License information for AI chips sent to China released by US House committee
  - [china] Why China's EVs could throw a wrench into EU, UK trade talks
  - [china] The US approved the sale of almost 900,000 AI chips to China in six months, the commission says
  - [china] US signed off on sales of nearly 900,000 AI chips to China in six months, committee says
  - [china] US signed off on sales of nearly 900,000 AI chips to China in six months-committee
  - [china] U.S. House Foreign Affairs Committee releases information on licenses for NVIDIA and AMD AI chips sent to Chin
  - [china] US House of Representatives Committee releases information on licenses for AI chips sent to China
  - [china] Offshore yuan dip looks like a liquidity blip, not a trend shift
  - [taiwan] TSMC and Samsung's China Chip Pause Has Stakes Beyond AI
  - [china] Canada's National Bank plans regular panda bond issuance as Ottawa-Beijing ties improve
  - [korea] Kinetiq: Bithumb Lists KNTQ for Spot Trading Against Korean Won - 19 Nov 2026
  - [china] DeepSeek Closes 100 Billion Yuan Funding Round
  - [china] Short seller Hunterbrook shorts AMD citing concerns over China exports
  - [japan] Prime Minister Takaichi receives an explanation from President Trump about the U.S.-China-Russia summit meetin
  - [japan] Prime Minister Takaichi held a press conference regarding his telephone conversation with US President Trump
  - [korea] Boston Dynamics to test Atlas humanoid robots at GlobalFoundries chip plants
  - [china] Nvidia Faces a New China Reality After Trump's Latest AI Chip Comments
  - [china] The first U.S.-China-Russia summit in history, what are the major powers' intentions, and what will be the imp
  - [china] NetEase: CNY 27.9 billion in Q3 revenue, higher gross margin and expanding global game reach
  - [taiwan] TSMC and Samsung pause some chip shipments to China due to new US export rules: report
  - [china] Musk promete aumentar a produção da Tesla na fábrica da China, segundo a mídia estatal chinesa
  - [japan] JT to post 1.3 trillion yen loss on Russian business
  - [japan] Next fiscal year's tax reform: LDP tax review begins discussion; issues include correction of tax revenue disp
  - [taiwan] TSMC acquires 0.03% stake in Anthropic for US$500 million
  - [taiwan] TSMC tightens China AI chip curbs as new US rules close manufacturing loophole, sources say
  - [taiwan] TSMC, Samsung Reportedly Suspend Some Chip Deliveries To Chinese Customers Amid New US Export Rules
  - [taiwan] Taiwan's APEC envoy urges 'wise' AI development, chip resilience
  - [taiwan] It is rumored that the new US export control regulations have impacted TSMC and Samsung to suspend some chip s
  - [japan] [Toyo Keizai "Market Commentary" Live Stream] What will happen to Japanese stocks in 2027? / Commentary by Tak
  - [china] Trump suggests Nvidia's Blackwell chips could go to China later

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
      "published_utc": "2026-11-19T21:12:47+00:00",
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

