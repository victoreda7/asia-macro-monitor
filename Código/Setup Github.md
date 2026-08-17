# Setup Github Actions

O que muda: a partir de agora, quem sai à internet buscar notícia é um robô do
GitHub, a cada ~10 minutos, **mesmo com este Mac desligado**. O `server.py`
local passa a só puxar (`git pull`) o que o robô já coletou — por isso o
"Atualizar" fica quase instantâneo, e reabrir o monitor depois de um fim de
semana fora já chega com tudo em dia, em vez de começar do zero.

Se por algum motivo o `git pull` falhar (sem internet, git não configurado),
o monitor volta sozinho a raspar localmente como sempre fez — nada quebra.

## 1. Pré-requisito: git autenticado no GitHub

Rode no Terminal:

```bash
git --version          # confirma que o git está instalado
gh auth status          # se usar o GitHub CLI — mostra se já está logado
```

Se `gh auth status` disser que não está logado (ou você não usa o `gh`), rode
`gh auth login` e siga o fluxo pelo navegador — isso configura o git para
autenticar sozinho em toda operação HTTPS com o GitHub, inclusive o `git
pull` automático que o monitor vai passar a fazer.

## 2. Subir o projeto pela primeira vez

Os arquivos novos (`.gitignore`, `SETUP_GITHUB_ACTIONS.md`) e o
`Código/server.py` atualizado já foram colocados na sua pasta do projeto.

O arquivo do workflow não pude gravar direto em `.github/workflows/` — essa
pasta é bloqueada para escrita remota por segurança (faz sentido: é onde
mora código que roda automaticamente com permissão de escrita no seu repo).
Ele está esperando em `_setup_github/collect.yml`; o primeiro comando abaixo
só move ele pro lugar certo.

```bash
cd "/Users/victoreda/Library/Mobile Documents/com~apple~CloudDocs/Projetos IA/Claude/Projetos/Ásia - Monitor de Notícias Macro"

mkdir -p .github/workflows
mv _setup_github/collect.yml .github/workflows/collect.yml
rmdir _setup_github

git init
git add -A
git commit -m "coleta inicial + GitHub Actions"
git branch -M main
git remote add origin https://github.com/victoreda7/asia-macro-monitor.git
git push -u origin main
```

(Se preferir SSH em vez de HTTPS, troque a URL do `remote add` por
`git@github.com:victoreda7/asia-macro-monitor.git` — só funciona se você já
tiver uma chave SSH cadastrada na sua conta.)

## 3. Testar o workflow manualmente ANTES de confiar no agendamento

Existe um risco real de o Investing.com e o TradingView (as duas fontes "ao
vivo") tratarem os IPs compartilhados do GitHub Actions com mais suspeita do
que o IP residencial do seu Mac — podem devolver 403 de lá mesmo respondendo
normal aqui.

Depois do push:

1. Vá em `github.com/victoreda7/asia-macro-monitor` → aba **Actions**.
2. Clique no workflow **Coleta Asia Macro News** → **Run workflow** → **Run
   workflow** (botão verde). Isso dispara uma coleta manual sem esperar o
   cron.
3. Espere terminar (~1-3 min) e abra o log do job **collect** → passo
   **Coletar notícias**. Confira a linha `X com problema` no resumo — se o
   número de fontes com problema estiver bem mais alto do que quando você
   roda localmente, é sinal de bloqueio por IP.
4. Se `investing_live` ou `tradingview_live` aparecerem quebrados só no
   Actions (e funcionando local), me avisa — dá pra ajustar (por exemplo,
   tirando essas duas do Actions e deixando só pro monitor local raspar,
   já que as outras 34 fontes RSS/Google News não costumam ter esse
   problema).

## 4. Deixar rodando sozinho

Se o teste manual passou, não precisa fazer mais nada — o cron
(`*/10 * * * *` no `collect.yml`) já está ativo a partir do primeiro push.
O GitHub não garante o minuto exato em horários de pico (a defasagem típica
é de alguns minutos), mas é uma diferença enorme em relação a "só coleta
quando alguém abre o Mac".

## 5. Curadoria manual (`manual_additions.json`)

Isso continua funcionando como antes, com um detalhe novo: como o feed
"oficial" agora vive no GitHub, uma edição feita só no seu Mac em
`Cache/manual_additions.json` não chega ao robô até você mandar pro GitHub:

```bash
cd "/Users/victoreda/Library/Mobile Documents/com~apple~CloudDocs/Projetos IA/Claude/Projetos/Ásia - Monitor de Notícias Macro"
git add Cache/manual_additions.json
git commit -m "curadoria manual"
git push
```

Se isso virar rotina, um próximo passo natural é automatizar esse push
dentro do próprio fluxo de curadoria — posso montar isso depois se fizer
sentido pra você.
