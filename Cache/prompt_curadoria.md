atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-26T09:22:46.152503+00:00
Total: 3000 manchetes

  🇯🇵 Japão          920
  🇨🇳 China          978
  🇹🇼 Taiwan         335
  🇰🇷 Coreia do Sul  767

## O que já está no feed (não repita)

  - [japan] Japan may raise shorter-term bond issuance if FY2027 debt sales increase
  - [korea] Bank of Korea May Hold Off on Raising Rates at January Meeting — Market Talk
  - [japan] Tepco To Invest Total Of 10.2 Trillion Yen By Fiscal Year 2035 In Power Grids, Nuclear Power Plants That Will 
  - [japan] Bank of Japan ETF valuation gain expands to 76 trillion yen, but valuation loss on government bonds expands to
  - [china] Southeast Asia No Longer a Tariff-Safe Alternative to China — Market Talk
  - [korea] The number of people subject to comprehensive real estate tax this year increased by 190,000 in a ye..
  - [china] New Tariffs on China Could Undermine Trade Truce with U.S. — WSJ
  - [korea] The Ministry of Finance and Economy announced on the 26th that it has decided not to issue governmen..
  - [japan] Japan may raise short-term bond issuance if FY2027 debt sales increase, official says
  - [japan] Aggressive Fed Tightening, Japan Fiscal Response Could Push BOJ Rates Above 2% — Market Talk
  - [japan] Bank of Japan member Tamura: ``A quick response such as accelerating the pace of interest rate hikes'' believe
  - [china] China hits back at Trump tariff threat
  - [korea] How a deal with Bain Capital made SK Hynix the main shareholder of competitor Kioxia
  - [china] China Braces for Tariff Hike After US Announcement
  - [korea] The Bank of Korea raised its base interest rate to 3.25%. Why did it choose to raise it this time?
  - [japan] Mitsubishi UFJ Raises BOJ Terminal Rate Forecast to 2% — Market Talk
  - [japan] Prime Minister Takaichi will revise the tax system next year “to promote investment and lead to growth”
  - [japan] Bank of Japan member Tamura: ``React swiftly, such as accelerating the pace of interest rate hikes.'' The ``ne
  - [taiwan] Agricultural minister says no new U.S. tariffs on 322 Taiwan products
  - [china] Trump Riles Trade Partners With Tariffs That Undercut ‘China+1’
  - [japan] BOJ's net income shrinks as interest payments on excess reserves grow
  - [japan] BOJ's net income shrinks on higher interest payments on reserves
  - [japan] Miyagi Prefectural Assembly November regular meeting submits general account supplementary budget bill of appr
  - [japan] BOJ Tamura's Remarks Reinforce Case for December Rate Hike — Market Talk
  - [korea] [Issue & People] Bank of Korea raises base interest rate to 3.25%... Next year’s growth forecast has been sign
  - [china] Asia rejects basis of new Trump tariffs as US gathers China ammunition
  - [korea] S. Korean won gains slightly against U.S. dollar after BOK hikes key rate
  - [china] Exclusive-US chip curbs, distillation crackdown threaten Chinese AI model development, sources say
  - [japan] Hawkish Bank of Japan member seeks quick rate hikes on inflation
  - [japan] EQT Raises Tender Offer Price For Kakaku.Com Inc To 3,701 Yen From 3,700 Yen, Filing Shows
  - [china] US restrictions on chips and strict measures against distillation threaten the development of AI models in Chi
  - [korea] (News Focus) Chip boom prompts BOK to deliver 3rd rate hike, revise up 2027 forecast
  - [japan] Bank of Japan member Tamura: “Inflation rates should be fixed at 2%, raise interest rate to neutral rate as so
  - [taiwan] Commentary: Taiwan supply chains monitor Trump's potential interference with Nvidia
  - [china] Analysis-Trump’s new tariffs aim to prise global trade from China’s grip
  - [korea] South Korean shares rebound from 10-month low; rate hike caps gains
  - [japan] BOJ's net income shrinks as interest payment on excess reserves grow
  - [korea] Bank of Korea raises interest rates amid AI chip boom
  - [korea] Korea stands by industrial policy after US tariff proposal
  - [japan] Stock price rise, buyback movement in AI/semiconductor related stocks

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
      "published_utc": "2026-11-26T09:22:46+00:00",
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

