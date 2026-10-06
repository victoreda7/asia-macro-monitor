atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-10-06T04:12:45.072262+00:00
Total: 2940 manchetes

  🇯🇵 Japão          1255
  🇨🇳 China          772
  🇹🇼 Taiwan         249
  🇰🇷 Coreia do Sul  664

## O que já está no feed (não repita)

  - [japan] Japan bonds pare losses after strong auction, but fiscal worries weigh
  - [japan] Kawasaki Heavy: Aims For Revenue Of More Than 3.3 Trln Yen And Business Profit Of More Than 330 Billion Yen By
  - [japan] World map made of glass beads in the Bank of Japan underground vault unveiled at Kanazawa Machinaka Arts Festi
  - [japan] Citi Strategist Sees JGB Yields Nearing Peak
  - [japan] Japan Yield Gains as Takaichi Vows Fiscal Expansion
  - [korea] Most Asian FX steady; Philippine peso, South Korean won weaken
  - [japan] Yen Steady as Takaichi Vows Fiscal Expansion
  - [japan] It is reported that the Bank of Japan has determined that the underlying inflation rate has reached 2% (curren
  - [japan] Japan bonds slide before 10-year auction amid fiscal worries at home and abroad
  - [korea] South Korea finance minister sees economic growth in 3% range this year
  - [korea] SK Hynix trapped below SMA20 in tight range: Live levels
  - [korea] Samsung Electro-Mechanics Gains After Chip-Packaging Equipment Purchase Deal
  - [korea] Hanmi to Build Packaging Equipment for Samsung's AI-Chip Substrates
  - [korea] Hanmi Semiconductor Secures KRW24.48B Contract With Samsung Electro-Mechanics
  - [korea] Hanmi Semiconductor Co Wins 24.5 Billion Won Order
  - [japan] The Bank of Japan will consider determining that the underlying price index has reached 2% (Jiji Press)
  - [japan] Bank of Japan to determine that underlying inflation has reached 2% at meeting this month (Jiji Press)
  - [japan] <Machine tool orders> The summer decline continues to be strong, with August orders reaching 197.8 billion yen
  - [japan] Threatening complaints were made, but an "unexpected savior" appeared during the "litigation trouble" with a b
  - [korea] There are a lot of things to say and a lot of trouble, but they say they will strengthen real estate..
  - [taiwan] SPCX Stock Ends Higher On Starship Fuel Plans, Analyst Optimism And TSMC Talks
  - [korea] South Korea FX Reserves End Three-Month Rising Streak
  - [japan] Nasdaq hits new high; buy tech stocks even as long-term interest rates rise
  - [china] Behind Germany's far-right AfD's rise is the "China Shock"...China's industrial competitiveness is exporting t
  - [japan] Prime Minister Takaichi seeks understanding on consumption tax cut, opposition parties plan to provide financi
  - [taiwan] Intel stock slides as TSMC explores Terafab tie-up, analyst flags share losses
  - [taiwan] Tesla Stock Rises After Musk Confirms TSMC Talks
  - [china] Takaichi's ``aggressive fiscal policy'' is state capitalism that imitates China while viewing it as an enemy. 
  - [china] UK considering tariffs on Chinese car imports
  - [taiwan] Intel Stock Tumbles -- TSMC Eyes Elon Musk's Terafab Project
  - [japan] Focus is on “reduction of consumption tax on food products” Extraordinary Diet session convened
  - [korea] Korean shipbuilders, refiners see Q3 estimates upgraded; chipmakers face cuts
  - [china] P2P stablecoin wallets in China grew 43x despite restrictions on cryptocurrencies, according to Chainalysis
  - [china] Antimony Market Faces a Nov. 27 Export-Control Deadline from China
  - [japan] Japan and Australia finance ministers meet to launch new dialogue framework
  - [japan] Japan's chip industry capitalizes on growth in India semiconductor industry
  - [taiwan] Musk hints TSMC may join his mega chip venture, and Intel's stock is taking a hit
  - [china] India may be best placed to fill a China-sized hole in fuel exports: Maguire
  - [korea] A part-timer who posted real estate advertisements online and received 200 won per case and a new em..
  - [china] UK Expected to Follow EU With China EV Tariffs, Report Says

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
      "published_utc": "2026-10-06T04:12:45+00:00",
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

