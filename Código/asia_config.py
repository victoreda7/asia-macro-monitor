"""
Configuração do Asia Macro News Monitor.

Tudo que você provavelmente vai querer mexer está aqui: fontes, queries do
Google News, os regex que definem "isto é macro" e "isto é sobre qual país",
e os limites do pipeline. Os outros módulos não têm constantes de negócio.

Regex são compilados uma vez, com re.IGNORECASE, e são multilíngues
(inglês + japonês + chinês + coreano) porque metade do valor do monitor está
em pegar o comunicado oficial antes da tradução do wire em inglês.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Limites do pipeline
# ---------------------------------------------------------------------------

RSS_PER_SOURCE_LIMIT = 60      # itens por feed RSS
GN_PER_QUERY_LIMIT = 30        # itens por query do Google News
# Teto do feed. Em set/2026 o teto de 420 guardava só ~6 dias: das 1.259
# manchetes que passaram no filtro em 9 dias, 850 tinham sumido — os dias 21 e
# 22/09 inteiros, e metade de 23 a 25/09. Com ~110 manchetes/dia, 3.000 cobre
# o período de 30 dias da UI (o corte por idade abaixo faz o resto).
# Itens curados à mão NÃO contam para este teto.
FEED_ITEM_CAP = 3000
# Nenhuma fonte pode ocupar mais que isto POR DIA, para um wire tagarela não
# afogar o resto. Antes o teto era de 30 no feed inteiro: com o feed
# acumulando dias, PBoC, BOK, Bloomberg e Yahoo batiam o teto e passavam a
# perder manchetes do próprio dia.
PER_SOURCE_DAILY_CAP = 30
HTTP_TIMEOUT = 20              # segundos por request
HTTP_RETRIES = 4               # tentativas em 429/503/erro de rede
FETCH_WORKERS = 6              # downloads em paralelo
TRANSLATE_WORKERS = 4          # traduções em paralelo
TRANSLATE_PAUSE = 0.25         # segundos entre chamadas de tradução, por worker
MAX_ITEM_AGE_DAYS = 30         # descarta o que for mais velho que isso (= maior período da UI)
STALE_SOURCE_DAYS = 20         # fonte sem nada novo há mais que isso vira alerta

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

REGIONS = ("japan", "china", "taiwan", "korea")

REGION_LABEL = {
    "japan": "Japão",
    "china": "China",
    "taiwan": "Taiwan",
    "korea": "Coreia do Sul",
}

REGION_FLAG = {
    "japan": "🇯🇵",
    "china": "🇨🇳",
    "taiwan": "🇹🇼",
    "korea": "🇰🇷",
}

TOPIC_LABEL = {
    "monetary": "Monetária",
    "fiscal": "Fiscal",
    "fx": "Câmbio",
    "inflation": "Inflação",
    "activity": "Atividade",
    "trade": "Comércio",
    "property": "Imobiliário",
    "industrial": "Indústria e chips",
    "signaling": "Sinalização",
}

# Ordem de exibição e de prioridade quando um item casa vários tópicos.
TOPIC_ORDER = (
    "monetary", "fiscal", "fx", "inflation",
    "activity", "trade", "property", "industrial", "signaling",
)


def _rx(pattern: str) -> re.Pattern:
    return re.compile(pattern, re.IGNORECASE | re.UNICODE)


# O filtro roda sobre o título ORIGINAL, antes de traduzir — traduzir os ~1000
# itens brutos de cada coleta seria caro demais. Por isso cada tópico precisa
# de padrão em toda língua que entra no pipeline. Faltava o português, e o
# feed em PT do TradingView estava sendo descartado quase inteiro.
_PT = {
    "monetary": r"juros|taxa b[áa]sica|pol[íi]tica monet[áa]ria|banco central|"
                r"aperto monet[áa]rio|afrouxamento|compuls[óo]rio|liquidez",
    "fiscal":   r"fiscal|or[çc]amento|d[íi]vida p[úu]blica|t[íi]tulos p[úu]blicos|"
                r"imposto|tribut[áa]ri|gasto p[úu]blico|est[íi]mulo|emiss[ãa]o de t[íi]tulos",
    "fx":       r"c[âa]mbio|cambial|moeda|iene|yuan|renminbi|d[óo]lar taiwan[êe]s|"
                r"desvaloriza|valoriza|interven[çc][ãa]o cambial|taxa de c[âa]mbio",
    "inflation": r"infla[çc][ãa]o|defla[çc][ãa]o|pre[çc]os ao consumidor|"
                r"[íi]ndice de pre[çc]os|custo de vida",
    "activity": r"\bPIB\b|crescimento econ[óo]mico|produ[çc][ãa]o industrial|"
                r"desemprego|vendas no varejo|atividade econ[óo]mica|recess[ãa]o",
    "trade":    r"exporta[çc]|importa[çc]|com[ée]rcio|tarifa|balan[çc]a comercial|"
                r"super[áa]vit comercial|d[ée]ficit comercial|alf[âa]ndega|"
                r"controle de exporta[çc]",
    "property": r"imobili[áa]ri|habita[çc][ãa]o|im[óo]veis|hipoteca|incorporadora",
    "industrial": r"semicondutor|chips? de mem[óo]ria|f[áa]brica|capacidade produtiva|"
                r"manufatura|montadora",
    "signaling": r"pol[íi]tica monet[áa]ria|pol[íi]tica fiscal|pol[íi]tica econ[óo]mica|"
                r"ministro d[ao]s? (finan[çc]as|economia)|conselho de estado|"
                r"pacote de est[íi]mulo|banco central",
}


# ---------------------------------------------------------------------------
# Fontes RSS
#
# scope="japan"|"china"|"taiwan"|"korea"  -> região fixa, não precisa aparecer no título
# scope="global"                          -> só entra se o título citar um dos quatro países
# ---------------------------------------------------------------------------

RSS_SOURCES = [
    # ---- Japão ----
    {"id": "nhk_economy",  "name": "NHK 経済",            "url": "https://news.web.nhk/n-data/conf/na/rss/cat5.xml",           "scope": "japan",  "domestic_jp": True},
    {"id": "nhk_politics", "name": "NHK 政治",            "url": "https://news.web.nhk/n-data/conf/na/rss/cat4.xml",           "scope": "japan",  "domestic_jp": True},
    {"id": "yahoo_business", "name": "Yahoo! ニュース 経済", "url": "https://news.yahoo.co.jp/rss/topics/business.xml",     "scope": "japan",  "domestic_jp": True},
    # Fonte oficial do BOJ (comunicados, resultados de operação, notas de
    # pesquisa). Feed em inglês, então os títulos já casam os padrões em EN.
    {"id": "boj_whatsnew", "name": "BOJ What's New (EN)", "url": "https://www.boj.or.jp/en/rss/whatsnew.xml",             "scope": "japan"},
    # Site oficial do primeiro-ministro/gabinete. Só em japonês — precisa de
    # domestic_jp para o fallback por kana+dica macro pegar agenda política.
    {"id": "kantei_jnews", "name": "Kantei 首相官邸",      "url": "https://www.kantei.go.jp/index-jnews.rdf",              "scope": "japan",  "domestic_jp": True},
    # Revista de negócios japonesa; bastante ruído de conteúdo não-macro, mas
    # o filtro de tópico/macro_hint já cuida disso.
    {"id": "toyo_keizai",  "name": "東洋経済オンライン",     "url": "https://toyokeizai.net/list/feed/rss",                  "scope": "japan",  "domestic_jp": True},

    # ---- China ----
    {"id": "scmp_business", "name": "SCMP Business",      "url": "https://www.scmp.com/rss/5/feed",                       "scope": "global"},
    # Xinhua: o worldrss.xml responde 200 mas está congelado desde jan/2018.
    # Cobertura vem pela query do Google News (gn_cn_xinhua).
    # NBS (estatística oficial) tem RSS ao vivo em
    # stats.gov.cn/english/PressRelease/rss.xml, mas o XML vem malformado
    # (tag <meta> sem fechar dentro do <channel>) e quebra o parser estrito
    # (xml.etree) lá pela linha 10498 — testado e confirmado, não é bloqueio
    # de rede. Em vez de amaciar o parser globalmente (arriscado para as
    # outras 15 fontes), a ponte é via Google News, que reembala em XML
    # válido (ver gn_cn_nbs abaixo).

    # ---- Taiwan ----
    # O /cna/rss devolve corpo vazio. O feed vivo é o do FeedBurner, que o
    # próprio rodapé do Focus Taiwan aponta.
    {"id": "focus_taiwan",  "name": "Focus Taiwan (CNA)", "url": "https://feeds.feedburner.com/rsscna/engnews",           "scope": "taiwan"},

    # ---- Coreia ----
    # yonhap_en (en.yna.co.kr/rss/industry.xml) está morto — devolve HTML, não
    # XML. Substituído pelo Korea Herald Business, confirmado ativo.
    {"id": "korea_herald_biz", "name": "Korea Herald Business", "url": "https://www.koreaherald.com/rss/kh_Business",     "scope": "korea"},
    # KED Global: a URL certa é /rss, não /newsRss (que devolve um feed quase
    # vazio, 756 bytes). Substitui a query gn_kr_hankyung, que ficou morta.
    {"id": "ked_global",    "name": "KED Global",         "url": "https://www.kedglobal.com/rss",                        "scope": "korea"},

    # ---- Pan-Ásia / global ----
    {"id": "nikkei_asia",   "name": "Nikkei Asia",        "url": "https://asia.nikkei.com/rss/feed/nar",                  "scope": "global"},
    {"id": "investing_econ", "name": "Investing Economy", "url": "https://www.investing.com/rss/news_14.rss",             "scope": "global"},
    {"id": "investing_fx",  "name": "Investing Forex",    "url": "https://www.investing.com/rss/news_1.rss",              "scope": "global"},
]

# ---------------------------------------------------------------------------
# Pontes via Google News
#
# region=None -> deixa o filtro inferir pelo título (fontes multi-país)
# ---------------------------------------------------------------------------

GOOGLE_NEWS_QUERIES = [
    # ---- Japão ----
    {"id": "gn_jp_reuters", "name": "Reuters Japan",   "region": "japan",
     "q": "site:reuters.com (Japan OR Japanese OR yen OR BOJ OR Tokyo)"},
    {"id": "gn_jp_nhkworld", "name": "NHK World EN",   "region": "japan",
     "q": "site:www3.nhk.or.jp/nhkworld (economy OR fiscal OR budget OR tax OR BOJ OR yen OR GDP OR MOF)"},
    {"id": "gn_jp_kyodo",   "name": "Kyodo News EN",   "region": "japan",
     "q": "site:english.kyodonews.net (economy OR BOJ OR yen OR inflation OR GDP OR fiscal OR budget)"},
    {"id": "gn_jp_mof",     "name": "MOF Japan",       "region": "japan",
     "q": "site:mof.go.jp OR site:www.mof.go.jp (budget OR fiscal OR tax OR bond)"},
    {"id": "gn_jp_investing", "name": "Investing Japan", "region": "japan",
     "q": "site:investing.com (Japan OR yen OR BOJ OR intervention OR JGB)"},
    # region=None de propósito: "物価" (preço/inflação) sozinho traz qualquer
    # notícia de inflação do mundo que a Yahoo JP traduziu (ex.: CPI dos EUA),
    # não só a do Japão. Sem fixed_region, o item só fica se o título citar
    # um dos quatro países — a mesma regra do Bloomberg/FT Asia abaixo.
    {"id": "gn_jp_yahoo", "name": "Yahoo! JP News", "region": None,
     "q": "site:news.yahoo.co.jp 日銀 OR 財政 OR 経済対策 OR 予算 OR 物価 when:7d",
     "locale": ("ja", "JP", "JP:ja")},

    # ---- China ----
    {"id": "gn_cn_reuters", "name": "Reuters China",   "region": "china",
     "q": "site:reuters.com (China OR Chinese OR yuan OR PBOC OR Beijing)"},
    {"id": "gn_cn_scmp",    "name": "SCMP Economy",    "region": "china",
     "q": "site:scmp.com (China economy OR yuan OR PBOC OR property OR fiscal)"},
    {"id": "gn_cn_caixin",  "name": "Caixin",          "region": "china",
     "q": "site:caixin.com OR site:caixinglobal.com (China OR economy OR PBOC OR fiscal)"},
    # Ampliado além de "逆回购 OR MLF OR 降准": compulsório, MLF por extenso,
    # operações de compra/venda de títulos, financiamento social agregado
    # (社融) e a reunião executiva do Conselho de Estado (国常会) — termos que
    # a auditoria de cobertura apontou como faltantes.
    {"id": "gn_cn_pboc",    "name": "PBoC 中文",        "region": "china",
     "q": "央行 (逆回购 OR 买断式逆回购 OR MLF OR 中期借贷便利 OR 降准 OR "
          "存款准备金率 OR 国债买卖 OR 社融 OR 国常会) when:7d",
     "locale": ("zh-CN", "CN", "CN:zh-Hans")},
    {"id": "gn_cn_xinhua",  "name": "Xinhua / 新华",    "region": "china",
     "q": "site:news.cn OR site:xinhuanet.com (economy OR Politburo OR State Council)"},
    {"id": "gn_cn_nbs",     "name": "NBS China (GN)",   "region": "china",
     "q": "site:stats.gov.cn (GDP OR CPI OR PPI OR PMI OR industrial production OR "
          "retail sales OR fixed asset investment)"},

    # ---- Taiwan ----
    {"id": "gn_tw_focus",   "name": "Focus Taiwan",    "region": "taiwan",
     "q": "site:focustaiwan.tw (economy OR CBC OR GDP OR export OR inflation)"},
    {"id": "gn_tw_cna",     "name": "中央社 CNA",       "region": "taiwan",
     "q": "site:cna.com.tw (economy OR 央行 OR 出口 OR 通膨 OR GDP)"},
    {"id": "gn_tw_udn",     "name": "UDN / 經濟日報",   "region": "taiwan",
     "q": "site:udn.com OR site:money.udn.com (Taiwan OR 台灣 OR 央行 OR 出口)"},
    {"id": "gn_tw_reuters", "name": "Reuters Taiwan",  "region": "taiwan",
     "q": "site:reuters.com (Taiwan OR TSMC OR TWD OR CBC OR Taipei)"},
    {"id": "gn_tw_digitimes", "name": "DIGITIMES",     "region": "taiwan",
     "q": "site:digitimes.com (Taiwan OR semiconductor OR TSMC OR economy)"},
    {"id": "gn_tw_taipeitimes", "name": "Taipei Times", "region": "taiwan",
     "q": "site:taipeitimes.com (business OR economy OR CBC OR GDP)"},

    # ---- Coreia ----
    {"id": "gn_kr_yonhap",  "name": "Yonhap",          "region": "korea",
     "q": "site:yonhapnews.co.kr OR site:yna.co.kr (economy OR BOK OR export OR inflation)"},
    # gn_kr_hankyung (site:hankyung.com) ficou sem resultado novo desde
    # fev/2026 — retirado. KED Global entra como fonte RSS direta em vez de
    # query (ver ked_global em RSS_SOURCES), que é mais confiável.
    {"id": "gn_kr_mk",      "name": "매일경제",          "region": "korea",
     "q": "site:mk.co.kr (economy OR BOK OR export OR won)"},
    {"id": "gn_kr_reuters", "name": "Reuters Korea",   "region": "korea",
     "q": "site:reuters.com (South Korea OR Korean OR won OR BOK OR Seoul)"},
    {"id": "gn_kr_herald",  "name": "Korea Herald",    "region": "korea",
     "q": "site:koreaherald.com (economy OR BOK OR inflation OR export)"},
    # -경시대회 exclui o concurso universitário anual do BOK sobre política
    # monetária: sem isso, os 30 slots da busca viravam só "faculdade X ganha
    # o concurso do BOK" — a mesma frase repetida por dezenas de veículos
    # locais, empurrando a política monetária de verdade pra fora do topo.
    {"id": "gn_kr_bok",     "name": "한국은행",          "region": "korea",
     "q": "한국은행 기준금리 OR 통화정책 -경시대회 when:7d",
     "locale": ("ko", "KR", "KR:ko")},
    {"id": "gn_kr_ked",     "name": "KED Global",      "region": "korea",
     "q": "site:kedglobal.com (Korea OR economy OR BOK OR export)"},

    # ---- Pan-Ásia ----
    {"id": "gn_asia_bloomberg", "name": "Bloomberg Asia", "region": None,
     "q": "site:bloomberg.com (Japan OR China OR Taiwan OR Korea OR yuan OR yen OR won)"},
    {"id": "gn_asia_ft",    "name": "FT Asia",         "region": None,
     "q": "site:ft.com (China OR Japan OR Taiwan OR South Korea economy)"},
]

# ---------------------------------------------------------------------------
# Wires ao vivo
# ---------------------------------------------------------------------------

INVESTING_HEADLINES_URL = "https://www.investing.com/news/headlines"
INVESTING_RSS_URL = "https://www.investing.com/rss/news.rss"

TRADINGVIEW_NEWS_URL = (
    "https://news-mediator.tradingview.com/public/news-flow/v2/news"
    "?client=web&user_prostatus=non_pro&filter=lang%3A{lang}"
)
TRADINGVIEW_LANGS = ("en", "pt")
TRADINGVIEW_ORIGIN = "https://br.tradingview.com"

# ---------------------------------------------------------------------------
# Contexto de região — usado só sobre o TÍTULO, nunca sobre tickers
# ---------------------------------------------------------------------------

REGION_CONTEXT = {
    "japan": _rx(
        r"\b(japan|japanese|tokyo|yen|jpy|boj|bank of japan|jgb|nikkei|"
        r"topix|kishida|ishiba|takaichi|ueda)\b"
        r"|日本|東京|日銀|日本銀行|円安|円高|財務省|日経"
        r"|일본|엔화"
    ),
    "china": _rx(
        r"\b(china|chinese|beijing|shanghai|shenzhen|yuan|renminbi|rmb|cny|"
        r"pboc|people'?s bank of china|politburo|state council|evergrande|"
        r"vanke|csi ?300|hang seng)\b"
        r"|中国|中國|北京|上海|人民银行|人民銀行|央行|人民币|人民幣|国务院|政治局"
        r"|중국|위안"
    ),
    "taiwan": _rx(
        r"\b(taiwan|taiwanese|taipei|twd|taiwan dollar|tsmc|taiex|"
        r"executive yuan|cbc taiwan|hon hai|foxconn|mediatek)\b"
        r"|台灣|台湾|臺灣|新台幣|台積電|行政院"
        r"|대만"
    ),
    "korea": _rx(
        r"\b(south korea|korean?|seoul|won(?!['’]t)|krw|bok|bank of korea|kospi|"
        r"samsung|sk hynix|yonhap|kostat|motie)\b"
        r"|한국|서울|한국은행|원화|기준금리|수출"
        r"|韓国|韩国|ウォン"
    ),
}

# Âncora genérica: "isto tem alguma coisa a ver com a Ásia?"
ASIA_ANCHOR = _rx(
    r"\b(japan|japanese|china|chinese|taiwan|taiwanese|korea|korean|"
    r"tokyo|beijing|shanghai|taipei|seoul|hong kong|"
    r"yen|yuan|renminbi|won|twd|jpy|cny|krw|"
    r"boj|pboc|bok|cbc|tsmc|samsung|sk hynix|nikkei|kospi|taiex|hang seng|asia)\b"
    r"|[぀-ヿ]|[一-鿿]|[가-힯]"
)

# ---------------------------------------------------------------------------
# Tópicos — o item precisa casar pelo menos um, senão cai
# ---------------------------------------------------------------------------

#
# Cuidado ao editar: o sufixo importa. `\b(tariff)\b` NÃO casa "tariffs" — o
# \b final exige fronteira logo depois de "tariff". Por isso quase todo
# substantivo aqui leva `s?` ou `\w*`. E siglas que costumam colar em CJK
# (MLF操作, LPR报价) ficam FORA do grupo com \b, porque em Python o ideograma
# conta como caractere de palavra e mata a fronteira.
#
TOPIC_PATTERNS = {
    "monetary": _rx(
        r"\b(interest rates?|policy rates?|benchmark rates?|base rates?|bank rate|"
        r"rate (hikes?|cuts?|decisions?|hold|rise|move)|"
        r"(hikes?|cuts?|raises?|lowers?|lifts?|trims?) (the )?(rates?|borrowing costs)|"
        r"central banks?|monetary polic\w+|"
        r"bank of (japan|korea)|people'?s bank( of china)?|"
        r"reserve requirements?|repos?|reverse repos?|open market operation|"
        r"quantitative easing|tapering|tighten\w*|easing (cycle|polic\w+|bias)|"
        r"yield curve control|liquidity (injection|operation))\b"
        r"|\b(boj|pboc|bok|cbc|rrr|ycc)\b"
        # Nome do relatório trimestral do BOJ ("Outlook for Economic Activity
        # and Prices") — sem isso a manchete caía como sem-topico porque não
        # cita "BOJ" nem "growth outlook" no título.
        r"|outlook for economic activity and prices"
        # Comunicados operacionais do BOJ que mexem com a curva: pesquisa do
        # mercado de títulos, reunião sobre operações, compras de JGB.
        r"|\bbond market survey\b|\bmarket operations?\b"
        r"|\bjgb (purchases?|buying|bond[- ]buying)\b|国債買い入れ|국고채 매입"
        r"|MLF|LPR|央行|公开市场|公開市場"
        r"|金利|利上げ|利下げ|金融政策|日銀|緩和|据え置き"
        r"|降准|降息|加息|逆回购|中期借贷便利|货币政策|存款准备金|貨幣政策|升息"
        r"|기준금리|통화정책|한국은행|금리"
    ),
    "fiscal": _rx(
        r"\b(fiscal|budgets?|stimulus( package)?|government spending|public spending|"
        r"deficits?|bond issuance|debt issuance|sovereign (bonds?|debt)|jgbs?|"
        r"tax (cuts?|hikes?|reform|revenue)|subsid\w+|supplementary budget|"
        r"treasury bonds?|special bonds?|local government (bonds?|debt)|"
        r"spending plan|fiscal (package|stimulus|expansion)|"
        r"defen[cs]e (spending|budget)|budget request)\b"
        r"|財政|補正予算|国債|増税|減税|歳出|予算案"
        r"|财政|专项债|国债|减税|增税|赤字|刺激"
        r"|재정|추경|국채|예산|감세"
    ),
    "fx": _rx(
        r"\b(exchange rates?|currenc(y|ies)|forex|fx (market|intervention|reserves)|"
        r"intervention|deprecia\w+|apprecia\w+|devalu\w+|"
        r"(weaker|stronger|weak|strong) (yen|yuan|won|taiwan dollar)|"
        r"yen|yuan|renminbi|taiwan dollar|korean won|"
        r"(won|yen|yuan) (weaken\w*|strengthen\w*|slid\w*|slump\w*|rall\w+|"
        r"rises?|falls?|hits?|tumbl\w+)|"
        r"currency (fixing|midpoint)|capital (outflow|inflow)s?)\b"
        r"|\b(jpy|cny|krw|twd)\b"
        r"|為替|円安|円高|介入|外国為替"
        r"|汇率|人民币|中间价|贬值|升值|外匯|新台幣"
        r"|환율|원화|외환"
    ),
    "inflation": _rx(
        r"\b(inflation\w*|deflation\w*|disinflation|consumer prices?|producer prices?|"
        r"price index|core (cpi|inflation|prices?)|cost of living|"
        r"price (pressure|growth|gains?)|"
        # Preço administrado (luz, gás encanado, alimentos): o "Korea freezes
        # Q4 electricity rates" e o "Taiwan freezes electricity rates" caíam
        # como sem-topico. Petróleo fica de fora — é commodity global e traria
        # tape de mercado.
        r"(electricity|power|utility|energy|food) (rates?|prices?|bills?|tariffs?|costs?))\b"
        r"|電気料金|电价|전기요금"
        r"|\b(cpi|ppi)\b"
        r"|物価|インフレ|デフレ|消費者物価"
        r"|通胀|通缩|物价|居民消费价格|通膨"
        r"|물가|소비자물가|인플레"
    ),
    "activity": _rx(
        r"\b(economic growth|growth (forecasts?|outlook|targets?|rate)|"
        r"industrial (production|output)|retail sales|fixed asset investment|"
        r"investment in fixed assets|"
        r"unemployment|jobless|payrolls?|employment|consumption|"
        r"econom(y|ies) (grew|expanded|contracted|slowed|shrank)|recession|"
        r"business (sentiment|confidence)|tankan|"
        r"purchasing managers)\b"
        r"|\b(gdp|pmi)\b"
        # Título-padrão dos comunicados mensais/trimestrais "guarda-chuva" da
        # NBS chinesa (ex.: "National Economy Maintained Steady Momentum...")
        # — cobre PIB, produção industrial, varejo e investimento num só
        # release, mas sem citar nenhum termo específico o bastante para
        # bater os padrões acima.
        r"|national economy (maintained|witnessed|operated|showed|made|got off)"
        r"|景気|国内総生産|鉱工業生産|小売|失業|雇用|短観"
        r"|经济增长|国内生产总值|工业增加值|社会消费品零售|固定资产投资|失业率|采购经理"
        r"|성장률|생산|고용|실업|소매판매"
    ),
    "trade": _rx(
        r"\b(exports?\w*|imports?\w*|trade (balance|surplus|deficit|war|deal|"
        r"talks|data|tension\w*)|tariffs?|customs|shipments?|current account|"
        r"export controls?|sanctions?|supply chains?|trade agreement|"
        # Cúpula e trégua comercial EUA–China e pacotes de investimento
        # bilaterais (ex.: os US$ 350 bi da Coreia nos EUA) — em set/2026 a
        # cúpula Trump–Xi inteira caiu como sem-topico.
        r"(trade|tariff) (truce|pact|framework|negotiat\w+)|"
        r"investment (plan|pledge|package|fund|deal)|"
        r"(us|u\.s\.)[- ]china (summit|talks|deal|truce|consensus|relations)|"
        r"trump[- ]xi|xi'?s (visit|summit))\b"
        r"|輸出|輸入|貿易|関税|経常収支"
        r"|出口|进口|贸易|关税|海关|经常账户|出口管制"
        r"|수출|수입|무역|관세|경상수지"
    ),
    "property": _rx(
        r"\b(property (market|sector|prices?|sales?)|real estate|housing|"
        r"home prices?|house prices?|developers?|mortgages?|land sales?|"
        r"residential (market|sales))\b"
        r"|不動産|住宅|地価"
        r"|房地产|楼市|房价|开发商|土地出让|按揭"
        r"|부동산|주택|집값"
    ),
    "industrial": _rx(
        r"\b(semiconductors?|chips?|chipmakers?|foundr(y|ies)|wafers?|"
        r"memory chips?|capital expenditure|capex|factory (output|orders)|"
        r"manufactur\w+|machine tools?|auto production|"
        r"tsmc|samsung electronics|sk hynix)\b"
        r"|\b(dram|nand|hbm)\b"
        r"|半導体|工作機械|設備投資"
        r"|半导体|芯片|晶圆|产能|制造业|台積電"
        r"|반도체|파운드리|메모리"
    ),
    # ATENÇÃO: sinalização é o tópico mais perigoso do conjunto.
    #
    # A versão anterior aceitava verbo solto — said, says, warns, official,
    # minister. Como quase toda manchete tem um desses, o filtro de tópico
    # ficava desligado na prática: 15% do feed entrava por aqui, e era míssil
    # norte-coreano, aviso de tufão e aniversário de bomba atômica.
    #
    # Agora exige ÂNCORA institucional ou substantivo de política econômica.
    # Verbo nenhum basta sozinho.
    "signaling": _rx(
        r"\b(monetary polic\w+|fiscal polic\w+|economic polic\w+|"
        r"polic(y|ies) (outlook|stance|meeting|minutes|guidance|mix|shift|decision|statement)|"
        r"stimulus (package|measures|plan)|economic (outlook|package|plan|stimulus|agenda)|"
        r"growth (outlook|target|forecast)|inflation (outlook|target|forecast)|"
        r"central bank governor|"
        r"(finance|economy|trade|industry) minister|minister of (finance|economy|trade)|"
        r"ministry of (finance|economy|trade|data and statistics)|"
        r"state council|politburo|two sessions|national people'?s congress|"
        r"executive yuan|cabinet office|"
        r"(boj|bok|pboc|cbc) (board|meeting|minutes|statement|governor)|"
        r"policymakers?|policy makers?)\b"
        r"|\b(mof|motie|kostat|dgbas)\b"
        r"|金融政策|財政政策|経済対策|日銀総裁|財務相|財務省|経済財政|補正"
        # Termos político-domésticos do Japão: aprovação de gabinete, pesquisa
        # de opinião, coalizão — sem isso, notícia de queda de popularidade
        # do premiê (que costuma anteceder mudança de política econômica)
        # caía como "sem-topico".
        r"|支持率|世論調査|連立"
        # Cúpulas de chefe de governo com os EUA/China (首脳会談 = cúpula).
        r"|\b(summit|talks) with (trump|xi)\b|\b(takaichi|lee jae[- ]myung|lai ching[- ]te) and trump\b"
        r"|首脳会談|元首会晤|정상회담"
        r"|货币政策|财政政策|国务院|政治局|两会|全国人大|经济工作会议|央行行长|财政部"
        r"|통화정책|재정정책|한국은행 총재|기획재정부|경제정책"
    ),
}

# ---------------------------------------------------------------------------
# Ruído — o que descartar
# ---------------------------------------------------------------------------

# Tape de bolsa: preço, pregão, movimento intradiário. Só passa se houver MACRO_HINT.
STOCK_TAPE_NOISE = _rx(
    r"\b(shares? (close|closes|closed|open|opens|opened|rise|rises|fall|falls|"
    r"jump|jumps|slump|slumps|gain|gains|drop|drops|end|ends)|"
    r"stocks? (close|open|rise|fall|end|edge)|"
    r"index (rises|falls|closes|opens|edges)|"
    r"closes? (up|down|higher|lower)|opens? (higher|lower|flat)|"
    r"taiex closes|nikkei (closes|ends|rises|falls)|kospi (closes|ends)|"
    r"session (high|low)|premarket|pre-market|after-hours|"
    r"top gainers|top losers|most active|trading halt)\b"
    r"|\b\d+(\.\d+)? ?% (higher|lower|up|down)\b"
    r"|涨停|跌停|收盘|开盘|涨幅|跌幅|盘中|个股"
    r"|急騰|急落|ストップ高|ストップ安|前引け|大引け"
    r"|상한가|하한가|장중|코스피 마감|코스닥"
)

# Se o título tem tape mas também tem isto, é macro de verdade e fica.
MACRO_HINT = _rx(
    r"\b(gdp|cpi|ppi|inflation|deflation|central bank|boj|pboc|bok|cbc|"
    r"interest rate|policy rate|rate (cut|hike|decision)|monetary|fiscal|"
    r"budget|stimulus|tariff|trade (balance|surplus|deficit)|"
    r"intervention|exchange rate|pmi|unemployment|export|import|"
    r"mof|ministry of finance|state council|politburo)\b"
    r"|央行|人民银行|日銀|金融政策|財政|国債|降准|降息|物価|通胀|关税|财政"
    r"|한국은행|기준금리|물가|재정|관세"
    # Sem isto, "支持率が急落" (aprovação do gabinete despenca) caía como
    # tape-de-bolsa antes de chegar no filtro de tópico: 急落/急騰 batem no
    # STOCK_TAPE_NOISE, e só sobrevivem com uma dica de macro no título.
    r"|支持率|世論調査|連立"
)

# Manchete cravada em outro mercado. Só cai se NÃO houver âncora Ásia.
#
# Sem âncora no início de propósito: ancorar em ^ deixava passar tudo que vem
# com prefixo de wire — "Analysis: Fed's path...", "UPDATE 2-ECB cuts...".
# A proteção contra falso positivo é o ASIA_ANCHOR, não a posição no texto.
US_LEDE_NO_ASIA = _rx(
    r"\b(u\.s\.|usa|american|fed|federal reserve|fomc|powell|"
    r"wall street|dow jones|nasdaq|s&p ?500|treasury yields|"
    r"white house|congress|senate|"
    r"ecb|lagarde|euro ?zone|bundesbank|"
    r"boe|bank of england|gilt|"
    r"selic|copom|ibovespa|"
    r"rbi|rba|banxico)\b"
)

# Mercados que não são o escopo. Caem se nenhum dos quatro países aparecer.
OUTRO_MERCADO = _rx(
    r"\b(brazil|brazilian|brl|canada|canadian|cad|mexico|mexican|"
    r"united states|europe|european|germany|german|france|french|"
    r"uk|britain|british|sterling|gbp|eur\b|"
    r"india|indian|australia|australian|new zealand|"
    r"russia|russian|turkey|argentina)\b"
)

# Assuntos que não são macro asiática mesmo com país no título.
# A segunda linha existe porque lançamento de produto da Samsung, TSMC e Sony
# entope os feeds coreano e taiwanês — e "chip" no título faz passar batido
# pelo filtro de tópico se a gente não cortar aqui.
NON_ASIA_HEADLINE = _rx(
    # esporte, cultura, entretenimento
    r"\b(football|soccer|olympic|world cup|celebrity|movie|film|album|"
    r"k-?pop|drama series|box office|actor|actress|singer|idol group|"
    r"recipe|tourism guide|travel tips|horoscope)\b"
    # lançamento de produto — entope os feeds coreano e taiwanês
    r"|\b(foldable|smartphone|handset|tablet|earbuds|wearable|"
    r"gaming console|flagship phone|camera lens|home appliance)\b"
    # militar e segurança: importa, mas não é macro. Note que "defence
    # spending" e "defence budget" NÃO estão aqui — orçamento é fiscal.
    r"|\b(missiles?|warships?|naval|troops|military (drill|exercise|parade)|"
    r"fighter jets?|submarines?|espionage|spy(ing)?|"
    r"air ?defen[cs]e drill|war anniversary|a-?bomb|atomic bomb|nuclear war|"
    r"shoal|territorial waters|coast guard vessel)\b"
    # clima e desastre
    r"|\b(typhoons?|earthquakes?|heat ?wave|flood(ing)? warning|sea warning|"
    r"land warning|storm warning|tsunami|wildfire)\b"
    # polícia e tribunal
    r"|\b(arrested|indicted|jailed|sentenced|lawsuit|fraud scheme|"
    r"prosecutors?|manhunt|kidnap)\b"
)


# Cola os padrões em português no fim de cada tópico. Fica fora dos blocos
# acima de propósito: assim dá para ver a lista PT inteira num lugar só, em vez
# de caçá-la espalhada por nove regex.
for _topico, _pt in _PT.items():
    TOPIC_PATTERNS[_topico] = _rx(TOPIC_PATTERNS[_topico].pattern + "|" + _pt)
del _topico, _pt


def region_of_title(title: str) -> str | None:
    """Retorna a região cujo contexto aparece no título, ou None.

    Quando mais de uma casa, vence a de match mais cedo no texto — na prática
    isso resolve bem manchetes tipo 'China cuts rates, yen weakens'.
    """
    best, best_pos = None, len(title) + 1
    for region in REGIONS:
        m = REGION_CONTEXT[region].search(title)
        if m and m.start() < best_pos:
            best, best_pos = region, m.start()
    return best


def topics_of_title(title: str) -> list[str]:
    """Todos os tópicos que o título casa, em TOPIC_ORDER."""
    return [t for t in TOPIC_ORDER if TOPIC_PATTERNS[t].search(title)]
