# Ásia - Monitor de Notícias Macro

Painel unificado de manchetes macro de **Japão, China, Taiwan e Coreia do Sul**.
Um script Python busca em ~34 fontes, descarta o que não é macro asiática,
traduz títulos JA/ZH/KO/PT para inglês e gera a página. Roda inteiro na sua
máquina com o **Python 3.9 que já vem no macOS** e só biblioteca padrão —
nenhum `pip install`, nenhum Homebrew.

## Começar

**Duplo-clique em `Abrir Monitor.command`.**

Ele confere o Python, faz a primeira coleta se ainda não houver feed, sobe o
painel em segundo plano e abre o navegador. **Pode fechar a janela do
Terminal** — o monitor continua rodando e coletando de 10 em 10 minutos.

Clicar em Abrir de novo com o monitor já no ar não sobe um segundo: ele detecta
e só reabre a aba.

Para desligar, use o botão **Desligar** no canto do painel — dois cliques, o
primeiro arma e o segundo executa. Não existe script de parada porque o lugar
natural de desligar é onde você já está olhando.

## Painel web (sem o Mac)

Desde set/2026 o monitor também roda **inteiro na nuvem**: dá para abrir no
celular ou em qualquer computador, com o Mac desligado.

- **Endereço:** o link do projeto `asia-macro-monitor` na Vercel. Pede uma
  senha na primeira vez (o usuário pode ser qualquer coisa); ela está em
  `.env.local` como `PAINEL_SENHA`.
- **Quem coleta:** o GitHub Actions (repositório público
  `victoreda7/asia-macro-monitor`). Quem dita o ritmo é o **cron-job.org**,
  que chama `/api/coletar?chave=…` no painel a cada 10 min. O agendador do
  próprio GitHub ficou de reserva (2 vezes por hora) porque sozinho ele
  atrasava horas.
- **Atualizar agora:** pede uma coleta ao GitHub e espera o feed mudar
  (1 a 3 min). Dá para continuar lendo enquanto isso.
- **Curadoria IA:** gera o prompt; você roda num chat de IA com web, cola o
  JSON da resposta no campo *Resultado da IA* e clica em **Enviar**. O painel
  grava `Cache/manual_additions.json` no GitHub e dispara a coleta que funde.
- **Desligar** não aparece: não há nada rodando que precise ser desligado.

Peças: o código da Vercel fica em `Painel Web/` (funções Node, sem build). Ele
não guarda nada; só lê o que o Actions commitou e dispara coletas. Variáveis na
Vercel: `GITHUB_TOKEN` (token fine-grained só deste repositório, Actions e
Contents de leitura e escrita), `PAINEL_SENHA` e `CRON_CHAVE`.

O monitor local (`Abrir Monitor.command`) continua funcionando como antes. Os
dois leem o mesmo feed do GitHub.

**Quando os tokens vencerem** (1 ano): gere outro `github_pat_` com as mesmas
permissões e troque `GITHUB_TOKEN` na Vercel (Settings → Environment
Variables). Depois é preciso republicar, porque a variável só vale em
deploys novos.

## Os dois relógios

Vale separar, porque parecem a mesma coisa e não são:

| Quem | Ritmo | O que faz | Sem ele |
|---|---|---|---|
| **Servidor, em segundo plano** | 10 min | Vai de fato à internet: baixa RSS, Google News e wires, filtra, traduz e regrava o `feed.json`. Cada coleta leva ~90s. | Nada de novo aparece nunca. |
| **Página, no navegador** | 5 min | Relê o `feed.json` do disco e redesenha. É de graça, por isso é mais frequente. | Você teria que dar F5 para ver o que já foi coletado. |

O intervalo de 10 minutos não é conservadorismo à toa: a coleta leva 90
segundos, então a 5 min o monitor passava um terço do tempo batendo nas fontes.
TradingView e o tradutor do Google são APIs não oficiais. Para mudar, é
`--interval` no `Abrir Monitor.command`.

O navegador **nunca** acessa NHK, Reuters ou Google News. Quem sai para a rede
é sempre o Python. O botão *Atualizar agora* é o mesmo `run_once` do laço
automático — uma função, dois gatilhos: relógio e clique.

Os dois compartilham um lock, então uma coleta automática em curso faz o botão
responder *"tente em instantes"* em vez de disparar um segundo fetcher.

O log do que aconteceu em segundo plano fica em `Cache/monitor.log`.

Na primeira vez o macOS pode recusar. Se acontecer, autorize em
*Ajustes do Sistema › Privacidade e Segurança › Abrir Mesmo Assim*, ou rode uma
vez no Terminal:

```bash
chmod +x "Abrir Monitor.command"
```

Pela linha de comando, se preferir:

```bash
cd "Código"
python3 fetch_asia_news.py     # coleta
python3 server.py              # painel
```

Duplo-clique no `Monitor de Notícias Macro.html` também abre, mas aí os dois
botões só releem o disco. Buscar na web exige o painel, porque é o servidor
local que roda o fetcher.

## Os dois botões

**↻ Atualizar agora** — roda a coleta inteira e recarrega o feed. Uma coleta
por vez; dois cliques não viram dois fetchers.

**Curadoria IA** — monta um prompt e abre num modal, já copiado para a área de
transferência. Cole num chat de IA com acesso à web. A IA visita os portais
oficiais que o automático não alcança, grava `Cache/manual_additions.json`, e
você clica em Atualizar agora para fundir. O fetcher nunca apaga esse arquivo:
só lê e mistura.

## Por que a curadoria existe

O automático é forte em wire e fraco em portal oficial. MOF japonês, PBoC, CBC
e BOK publicam PDF sem RSS, e NHK World English não tem feed público. Esses são
os buracos recorrentes — e são justamente os itens que mais importam.

## Como o filtro decide

Um título só entra se sobreviver a quatro portões, nesta ordem:

1. **Tape de bolsa** cai — fechamento, pregão, 涨停, 상한가 — a menos que traga
   uma âncora macro no mesmo título ("Nikkei falls as BOJ signals hike" fica).
2. **Fora de escopo** cai — esporte, cultura, lançamento de produto, militar,
   clima e polícia. Foldable da Samsung entope o feed coreano; míssil,
   tufão e aniversário de bomba atômica entopem todos.
   Cuidado ao editar: *defence spending* e *defence budget* ficam **fora**
   dessa lista de propósito — orçamento militar é fiscal.
3. **Lede de outro mercado** cai — Fed, ECB, Copom — se não houver âncora Ásia
   no título.
4. **Precisa casar um tópico**: monetária, fiscal, câmbio, inflação, atividade,
   comércio, imobiliário, indústria e chips, ou sinalização. E precisa ter
   região: ou a fonte é de país fixo, ou o país aparece no título.

Exceção útil: RSS doméstico japonês é telegráfico (`首相、補正予算の編成を指示`)
e escapa dos regex em inglês. Com kana e dica macro, entra como sinalização —
e depois de traduzido é reclassificado, quase sempre para fiscal.

Os tickers relacionados que o TradingView manda junto contam para **tópico**
(`TWSE:2330` sugere semicondutor) mas nunca para **região** — uma notícia do
Fed carrega `FX:USDJPY` e viraria "Japão" por engano.

Duas armadilhas que já custaram caro e estão documentadas no código:

**`signaling` é o tópico mais perigoso.** Se ele aceitar verbo solto — *said*,
*says*, *warns*, *official*, *minister* — o filtro de tópico se desliga na
prática, porque quase toda manchete tem um desses. Chegou a 15% do feed entrando
por aí, tudo míssil e tufão. Hoje ele exige âncora institucional (State Council,
BOJ minutes, finance minister) ou substantivo de política econômica.

**O filtro roda sobre o título original, antes da tradução.** Traduzir os ~1000
itens brutos de cada coleta seria caro demais, então cada tópico precisa de
padrão em toda língua que entra: inglês, japonês, chinês, coreano **e
português** — o feed em PT do TradingView estava sendo descartado quase inteiro
por falta dele. A lista PT fica agrupada no `_PT`, no topo do `asia_config.py`.

Quando uma manchete importante sumir, não saia mexendo em regex no escuro:

```bash
python3 fetch_asia_news.py --explain
```

Isso imprime quantos itens cada regra comeu, com um exemplo de cada.

## Comandos

| Comando | O que faz |
|---|---|
| `python3 fetch_asia_news.py` | coleta uma vez |
| `python3 fetch_asia_news.py --watch` | loop a cada 300s (`--interval` muda) |
| `python3 fetch_asia_news.py --explain` | mostra os motivos de descarte |
| `python3 fetch_asia_news.py --no-live` | pula Investing e TradingView |
| `python3 fetch_asia_news.py --check` | testa as fontes, não grava nada |
| `python3 server.py` | painel + coleta automática de 10 em 10 min |
| `python3 server.py --interval 300` | coleta de 5 em 5 min |
| `python3 server.py --no-watch` | só serve o painel, sem coletar sozinho |
| `python3 build_prompt.py` | imprime o prompt de curadoria no terminal |

## Arquivos

Todos são necessários. A coluna diz para quê.

| Arquivo | Precisa para | O que é |
|---|---|---|
| `Abrir Monitor.command` | abrir | **o atalho.** Sobe o painel em segundo plano com a coleta de 10 em 10 min. |
| `Monitor de Notícias Macro.html` | ver | a página, com o feed embutido. Regerada a cada coleta. |
| `Código/fetch_asia_news.py` | coletar | orquestra tudo. É o que você roda. |
| `Código/asia_config.py` | coletar | **onde você mexe**: fontes, queries, regex de tópico e de país, limites. |
| `Código/filters.py` | coletar | o núcleo: filtro macro, região, tópicos, dedupe. Puro, sem rede. |
| `Código/sources.py` | coletar | RSS, Google News, Investing, TradingView. Coleta em paralelo. |
| `Código/http_util.py` | coletar | GET com retry e backoff. Todo fetch passa por aqui. |
| `Código/translate.py` | coletar | detecção de idioma e tradução com cache. |
| `Código/render_html.py` | coletar | gera a página. |
| `Código/server.py` | os botões | painel local com as duas rotas POST. |
| `Código/build_prompt.py` | botão Curadoria IA | monta o prompt. |
| `Cache/feed.json` | — | o feed atual. |
| `Cache/translation_cache.json` | — | traduções já feitas, para não repetir chamada. |
| `Cache/manual_additions.json` | — | o que a IA curou. Você ou a IA escrevem; o fetcher só lê. |

Os sete primeiros de `Código/` são a cadeia mínima para uma coleta rodar.
Tirar qualquer um quebra o import. A árvore de dependências é rasa de
propósito — só `fetch_asia_news` conhece os outros:

```
asia_config      (não importa ninguém)
  ├── filters
  ├── http_util
  │     ├── sources
  │     └── translate
  ├── render_html
  └── build_prompt
fetch_asia_news  → asia_config, filters, sources, translate, render_html
server           → nenhum (chama os scripts por subprocess)
```

## Nomenclatura

A pasta segue o `ORGANIZACAO.md` do iCloud: Title Case em português, acento
correto, hífen separando blocos, espaço no lugar de `_`.

Os módulos em `Código/` são a exceção — nome de módulo Python precisa ser um
identificador válido, então `fetch_asia_news.py` não pode virar
`Fetch Asia News.py` sem quebrar o `import`. Mesmo caso do `Capitale/` na lista
de intocadas. Tudo que o usuário vê (pasta, página, este documento) segue a
convenção.

Os arquivos em `Cache/` mantêm o nome minúsculo porque são lidos por código,
nunca abertos à mão.

## Fontes

**Japão** — NHK 経済 e 政治 (RSS), Yahoo! Business (RSS); via Google News:
Reuters Japan, NHK World EN, Kyodo EN, MOF, Investing.

**China** — SCMP Business (RSS), Xinhua EN (RSS); via GN: Reuters China,
SCMP Economy, Caixin, PBoC em chinês (`央行 逆回购 OR MLF OR 降准`), Xinhua/新华.

**Taiwan** — Focus Taiwan/CNA (RSS); via GN: Focus Taiwan, 中央社, UDN/經濟日報,
Reuters Taiwan, DIGITIMES, Taipei Times.

**Coreia** — Yonhap Economy EN (RSS); via GN: Yonhap, 한국경제, 매일경제,
Reuters Korea, Korea Herald, BOK em coreano, KED Global.

**Pan-Ásia** — Nikkei Asia, Investing Economy e Forex (RSS); via GN: Bloomberg
Ásia, FT Asia. Entram só se o título citar um dos quatro países.

**Ao vivo** — Investing (página + RSS) e TradingView News Flow (EN e PT).

Na curadoria, a prioridade é: oficial e estatal → NHK, Focus Taiwan, Yonhap,
Xinhua EN → Reuters, Kyodo, SCMP, Nikkei Asia.

## O que esperar que dê errado

- **Google News** devolve link de redirect. O `decode_google_news_url` recupera
  a URL canônica lendo o varint de comprimento do protobuf embutido no base64.
  É best-effort: quando falha, o link do GN continua funcionando no browser.
- **Investing** às vezes responde 403, e o `__NEXT_DATA__` muda de shape. Por
  isso o parser procura pela *forma* do objeto em vez de fixar um caminho de
  chaves.
- **TradingView e translate.googleapis** são APIs não oficiais. Uso de mesa,
  sem loop agressivo. Se pararem, o resto do pipeline continua.
- **Caixin** tem paywall — o título entra, o corpo não.
- Fonte fora do ar não quebra nada: vira uma linha vermelha na aba
  **Saúde das fontes**, e o feed sai com as outras.
- **Entidades HTML.** Feeds mandam `&#39;`, `&quot;`, e agregador às vezes
  manda `&amp;amp;` duplamente codificado. A limpeza acontece no `NewsItem`,
  não em cada coletor — senão TradingView e Investing, que chegam por JSON e
  não passam pelo parser de RSS, escapariam dela.
- **Feed com namespace.** O parser compara o *nome local* da tag, então lê RSS
  2.0, RDF 1.0 e Atom com o mesmo código. Fixar `<item>` sem namespace perde
  feeds inteiros em silêncio.
- **Rate limit do Google News.** São 25 queries no mesmo host; disparadas juntas
  ele devolve 429 para quase todas — na primeira coleta isso derrubou 27 das 36
  fontes. Agora há um throttle por host (`HOST_MIN_INTERVAL` no `http_util.py`):
  1,1s entre chamadas ao `news.google.com`, e o intervalo dobra sozinho se
  mesmo assim vier um 429. Hosts diferentes seguem em paralelo total, então a
  coleta não ficou lenta na mesma proporção.
- **Feed abandonado é pior que feed morto.** O RSS mundial do Xinhua responde
  200 com XML impecável, mas a notícia mais nova é de janeiro de 2018 — passava
  por fonte saudável entregando zero. Por isso a aba de saúde mostra a idade do
  item mais recente e marca *parada desde* quando passa de 20 dias
  (`STALE_SOURCE_DAYS`). O RSS do Focus Taiwan em `/cna/rss` também morreu; o
  vivo é o do FeedBurner, que está configurado.

## Testes

Existia um `test_filters.py` com 74 casos do núcleo. Foi removido porque não é
necessário para rodar, mas ele pegou cinco bugs antes da primeira coleta — vale
regerar antes de qualquer mexida grande no `asia_config.py`. Peça e ele volta
em segundos.
