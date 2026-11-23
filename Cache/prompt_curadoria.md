atualizar noticias asia

Você vai completar o feed do Asia Macro News Monitor com as manchetes macro
que a coleta automática não pegou. O automático é bom em wires e fraco em
portal oficial sem RSS — fiscal japonês, comunicado do PBoC, CBC e BOK são os
buracos recorrentes.

## Estado atual do feed

Última coleta: 2026-11-23T12:52:42.320696+00:00
Total: 3000 manchetes

  🇯🇵 Japão          1023
  🇨🇳 China          945
  🇹🇼 Taiwan         330
  🇰🇷 Coreia do Sul  702

## O que já está no feed (não repita)

  - [japan] Regional banks and others significantly raise interest rates on fixed deposits
  - [china] Zhongji Innolight Plans A-Share Buyback With 2-4 Billion Yuan
  - [china] LCY’s China chip chemicals business draws $600M takeover interest from HSG-led consortium - report
  - [china] The Taiwan Affairs Office of the State Council and the Export-Import Bank of China signed a contract to increa
  - [korea] Samsung, SK Hynix’s long-term supply deals with Big Tech hold firm despite market peak fears
  - [china] Consortium in talks to buy LCY's $600 million China chip chemicals business, people say
  - [china] Yuan Heng Gas Expects Unaudited Consolidated Net Loss Of RMB60 Million For Half-Year
  - [japan] Rising prices: Even universities and condominiums that emphasize safety are reconsidering their asset manageme
  - [korea] Jupiter Wagons to manufacture metro coaches, propulsion systems with Korea's Woojin in JV
  - [china] CapitaLand China Trust: Retail sales grew as leasing and capital actions targeted portfolio resilience
  - [korea] Bank of Korea Expected to Tighten Policy Twice More in Cycle — Market Talk
  - [china] Gold Deluge Keeps China’s $1 Trillion Trade Surplus in Check
  - [taiwan] Chip prices set to rise through 2027, driving semiconductor growth
  - [japan] Dollar edges off 19-month high after stocks rout; yen softens By Reuters
  - [korea] Posco Future M targets next-generation battery anodes with China-free supply chain
  - [korea] The Bank of Korea is likely to raise the base interest rate to 3.25% in November... All 14 experts predict ‘ra
  - [korea] AI chip boom lifts Samsung Electro-Mechanics ahead of LG Innotek in substrate profits
  - [korea] Park Jong-bok, former president of SC First Bank, has been selected as the next chairman of the Nati..
  - [taiwan] SinoPac predicts that the central bank will rise by half a yard each by the end of this year and the beginning
  - [korea] How long will the interest rate rise... Asset markets 'stumble' due to additional hikes in Korea and the US?
  - [japan] Dollar edges off 19-month high after stocks rout; yen softens
  - [china] Asia FX broadly firmer as dollar retreats from 19-month high; yuan, won gain
  - [china] Chinese state media hits out at ‘deflation trap’ warnings, defends economic performance
  - [china] Chinese state media hits out at ‘deflation trap’ warnings, defends economy
  - [korea] S. Korea's exports forecast to exceed US$1 tln for 2nd straight year in 2027
  - [korea] Samsung, SK hynix, LG redraw playbooks for AI boom
  - [korea] Kmpharmaceutical To Divest Real Estate Worth 11.3 Billion Won
  - [korea] Bank of Korea, last Monetary Policy Committee meeting of the year on the 26th... The outlook for a 0.25% point
  - [korea] (LEAD) Finance minister says gov't has contingency plan beyond stock market fund
  - [taiwan] AI stock rout puts Taiwan's tech supply chain on alert, prompting government scrutiny of capital flows
  - [china] China's yuan steadies after wild swings, more volatility seen ahead
  - [japan] Japan Spot Power Price Reaches More Than Four-Year High on Cold-Weather Outlook
  - [korea] “Strong growth next year”... 한은 기준금리 3.5% 바라보나
  - [china] China's gold imports said to have surged to record $209B through Oct.
  - [korea] Korea's finance minister upbeat on growth despite AI jitters
  - [japan] Japan Power Prices Extend Rise to Four-Year High on Cold Outlook
  - [korea] “We will raise it this time” ⋯ 14 experts speak with one voice on raising the base interest rate in November [
  - [japan] Asia FX mixed as dollar retreats from 19-month high; yen, won weaken
  - [china] China stocks hit 16-month low as US chip curbs, rout in AI shares sour mood
  - [china] Beijing steps up market rescue with record 90B yuan ETF purchases

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
      "published_utc": "2026-11-23T12:52:42+00:00",
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

