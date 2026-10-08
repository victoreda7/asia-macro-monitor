#!/usr/bin/env python3
"""
Painel local do Asia Macro News Monitor.

    python3 server.py              sobe em http://127.0.0.1:8765 e abre o browser
    python3 server.py --port 9000  outra porta
    python3 server.py --no-open    não abre o browser

Serve a pasta do projeto e expõe duas rotas POST:
  /api/asia-news-refresh        pede coleta nova ao GitHub (ou raspa local) e devolve {ok, generated_at_utc, count}
  /api/asia-news-manual-prompt  devolve {ok, prompt} para a curadoria por IA

Também roda o laço de coleta automática numa thread de fundo: a cada 5 minutos
ele vai de fato à internet e regrava o feed. Quem atualiza é este laço; a página
no navegador só relê o feed.json do disco.

Escuta só em 127.0.0.1 de propósito — é uma ferramenta de mesa, não um serviço.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import threading
import time
import webbrowser
from datetime import datetime, timezone
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
CODE = ROOT / "Código"
FEED_PATH = ROOT / "Cache" / "feed.json"

# O nome do arquivo segue a convenção do iCloud (Title Case, com espaço e
# acento), então precisa ser percent-encoded para virar URL.
HOME_FILE = "Monitor de Notícias Macro.html"
HOME_PAGE = "/" + quote(HOME_FILE)

FETCH_TIMEOUT = 420   # a primeira coleta pode passar de 3 min
# Idade máxima do feed que o git pull trouxe para ele valer como fresco.
# Acima disso o GitHub Actions parou (cron atrasado, workflow desabilitado,
# repositório sem créditos) e vale gastar os ~90s de uma raspagem local —
# sem isto, um pull que dá "nada novo" a cada 10 min mascarava o Actions
# parado por horas e o Mac nunca coletava sozinho.
FEED_FRESCO_MIN = 25
PROMPT_TIMEOUT = 60
MIN_INTERVAL = 60     # piso de segurança para o laço automático
PIDFILE = ROOT / "Cache" / "monitor.pid"

# Uma coleta por vez. O botão Atualizar e o laço automático disputam este lock,
# então um clique durante a coleta de fundo não dispara um segundo fetcher.
_fetch_lock = threading.Lock()

# Preenchido em main(). O botão Desligar precisa da instância para encerrar.
_servidor = None


def _ler_feed() -> dict:
    """Lê o feed do disco. Nunca levanta."""
    try:
        return json.loads(FEED_PATH.read_text("utf-8"))
    except (json.JSONDecodeError, OSError, ValueError):
        return {}


def _idade_feed_min(feed: dict | None = None) -> float:
    """Minutos desde a última coleta que de fato alcançou as fontes.

    Usa generated_at_utc, que o fetcher só avança quando a coleta foi boa;
    numa coleta degradada ele fica parado e a idade aqui cresce, que é
    exatamente o sinal de que precisamos tentar de novo."""
    feed = _ler_feed() if feed is None else feed
    marca = feed.get("generated_at_utc")
    if not marca:
        return float("inf")
    try:
        dt = datetime.fromisoformat(marca)
    except ValueError:
        return float("inf")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - dt).total_seconds() / 60


def _renderizar() -> tuple[bool, str]:
    """Regera o HTML a partir do feed.json em disco.

    Roda em subprocesso de propósito: importar render_html aqui dentro
    congelava o template na versão carregada no boot, então toda correção
    no painel vinda de um git pull só aparecia depois de reiniciar o
    monitor. Em subprocesso, o código novo vale na hora."""
    try:
        proc = subprocess.run(
            [sys.executable, str(CODE / "render_html.py")],
            cwd=str(CODE), capture_output=True, text=True, timeout=60,
        )
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"
    if proc.returncode != 0:
        linhas = (proc.stderr or proc.stdout or "").strip().splitlines()
        return False, linhas[-1] if linhas else "render falhou"
    return True, "html regerado"


def _rodar_fetcher(timeout: int = FETCH_TIMEOUT) -> tuple[bool, str]:
    """Executa uma coleta local (raspa as fontes daqui mesmo). Devolve (ok, mensagem).

    É o caminho lento (~1-3 min) e o único que existe se o projeto não for um
    repositório git. Ver `_atualizar` para o caminho rápido via GitHub Actions.
    """
    try:
        proc = subprocess.run(
            [sys.executable, str(CODE / "fetch_asia_news.py")],
            cwd=str(CODE), capture_output=True, text=True, timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return False, f"tempo esgotado depois de {timeout}s"
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"

    if proc.returncode != 0:
        linhas = (proc.stderr or proc.stdout or "").strip().splitlines()
        return False, linhas[-1] if linhas else "o fetcher falhou"

    linhas = (proc.stdout or "").splitlines()
    aviso = [ln for ln in linhas if ln.startswith("⚠")]
    resumo = [ln for ln in linhas if ln.startswith("✓")]
    msg = resumo[-1] if resumo else "coleta concluída"
    if aviso:
        msg = f"{aviso[-1].strip()} | {msg.strip()}"
    return True, msg


# Arquivos que o próprio monitor regrava a cada coleta (local ou via GitHub
# Actions). Nunca são editados à mão, então descartar a versão local deles
# antes de um pull é seguro — é só abrir espaço pro que o Actions coletou.
_GERADOS = ("Cache/feed.json", "Cache/translation_cache.json",
            "Cache/first_seen_cache.json", HOME_FILE)


def _head() -> str:
    """SHA do commit atual, ou string vazia se nem isso der."""
    try:
        proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT),
                              capture_output=True, text=True, timeout=10)
    except Exception:
        return ""
    return (proc.stdout or "").strip() if proc.returncode == 0 else ""


def _git_pull() -> tuple[bool, str]:
    """Puxa a coleta mais recente feita pelo GitHub Actions, se o projeto for
    um repositório git com remoto configurado.

    Isto é o que resolve a coleta perdida quando o Mac fica desligado: o
    Actions continua raspando as fontes a cada poucos minutos lá no GitHub
    mesmo com este computador apagado, e quando o app reabre, este pull traz
    tudo que rolou enquanto ninguém estava olhando — em ~1s, contra os
    1-3 minutos de uma raspagem local completa.
    """
    if not (ROOT / ".git").exists():
        return False, "pasta não é um repositório git"

    antes = _head()

    def puxar():
        try:
            proc = subprocess.run(
                ["git", "pull", "--ff-only", "--quiet"],
                cwd=str(ROOT), capture_output=True, text=True, timeout=30,
            )
        except subprocess.TimeoutExpired:
            return None, "git pull demorou demais (sem internet?)"
        except Exception as exc:
            return None, f"{type(exc).__name__}: {exc}"
        if proc.returncode == 0:
            return True, ""
        linhas = (proc.stderr or proc.stdout or "").strip().splitlines()
        return False, linhas[-1] if linhas else "git pull falhou"

    ok, erro = puxar()

    # O `git pull --ff-only` trava pra sempre se ninguém limpar a árvore: o
    # próprio monitor reescreve feed.json e o HTML a cada coleta, o que suja
    # a árvore, o que faz o `--ff-only` seguinte recusar rodar por mudança
    # local não commitada — um ciclo que não se resolve sozinho. Descartar os
    # arquivos gerados quebra o ciclo sem risco para edição manual de verdade
    # (manual_additions.json fica de fora de propósito).
    #
    # Mas só depois de o pull falhar, e não antes dele como era: quando não há
    # commit novo no GitHub, o descarte de antes jogava fora a coleta local
    # recém-feita e devolvia o feed commitado, mais velho. Com o Actions em
    # cadência baixa, isso era a coleta local sendo desfeita a cada 10 min.
    if ok is False:
        subprocess.run(["git", "checkout", "--", *_GERADOS],
                       cwd=str(ROOT), capture_output=True, text=True, timeout=15)
        ok, erro = puxar()

    if not ok:
        return False, erro

    # Com --quiet o stdout vem vazio tanto quando trouxe commit novo quanto
    # quando não trouxe, e o log dizia "já estava atualizado" para sempre —
    # inclusive nas horas em que o Actions estava parado. Comparar o HEAD
    # antes e depois é o único jeito honesto de saber.
    depois = _head()
    if antes and depois and antes != depois:
        return True, "coleta nova do GitHub"
    return True, "nada novo no GitHub"


def _atualizar(timeout: int = FETCH_TIMEOUT) -> tuple[bool, str]:
    """Atualiza o feed: tenta git pull primeiro (rápido); só raspa localmente
    se o pull não der certo (sem git configurado, sem internet, etc.) — assim
    o monitor continua funcionando sozinho mesmo sem o GitHub Actions."""
    ok, msg = _git_pull()
    if ok:
        ok_render, msg_render = _renderizar()
        if not ok_render:
            return False, f"pull ok mas falhou ao renderizar: {msg_render}"
        idade = _idade_feed_min()
        if idade <= FEED_FRESCO_MIN:
            return True, f"git pull: {msg}"
        # O repositório não tem coleta recente: o Actions parou. Raspa aqui.
        ok_local, msg_local = _rodar_fetcher(timeout)
        idade_txt = "?" if idade == float("inf") else f"{int(idade)} min"
        return ok_local, f"{msg_local} (GitHub sem coleta há {idade_txt})"
    return _rodar_fetcher(timeout)


# ---- "Atualizar agora": pedir uma coleta nova, não só puxar a última ----
#
# Até 08/10/2026 o botão chamava _atualizar(), que só faz git pull: se a
# última coleta do GitHub tinha menos de 25 min, nada era raspado e o clique
# não mudava nada. Agora o botão faz o mesmo que o do painel web — dispara o
# workflow no GitHub Actions, espera a run terminar e puxa o resultado. Sem
# token ou sem GitHub, raspa aqui mesmo.
WORKFLOW_ARQ = "collect.yml"
MANUAL_ESPERA = 300   # segundos esperando a run do GitHub terminar
MANUAL_POLL = 8


def _token_github() -> str:
    """GITHUB_TOKEN do .env.local (gitignored). Vazio se não houver."""
    try:
        for linha in (ROOT / ".env.local").read_text("utf-8").splitlines():
            linha = linha.strip()
            if linha.startswith("GITHUB_TOKEN="):
                return linha.split("=", 1)[1].strip().strip('"').strip("'")
    except OSError:
        pass
    return ""


def _repo_github() -> str:
    """'dono/repo' a partir do remoto origin. Vazio se não der."""
    try:
        proc = subprocess.run(["git", "remote", "get-url", "origin"], cwd=str(ROOT),
                              capture_output=True, text=True, timeout=10)
    except Exception:
        return ""
    url = (proc.stdout or "").strip()
    for prefixo in ("https://github.com/", "git@github.com:"):
        if url.startswith(prefixo):
            resto = url[len(prefixo):]
            return resto[:-4] if resto.endswith(".git") else resto
    return ""


def _api_github(metodo: str, caminho: str, token: str, corpo: dict | None = None):
    import urllib.request
    dados = json.dumps(corpo).encode() if corpo is not None else None
    req = urllib.request.Request(
        "https://api.github.com" + caminho, data=dados, method=metodo,
        headers={"Authorization": f"Bearer {token}",
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "User-Agent": "asia-macro-monitor-local"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        txt = resp.read().decode("utf-8") or "{}"
        return resp.status, json.loads(txt)


def _coleta_github(token: str, repo: str) -> tuple[bool | None, str]:
    """Dispara o workflow e espera ele terminar.

    (True, msg) run concluída com sucesso; (False, msg) run falhou ou a
    espera estourou; (None, msg) nem deu para disparar (sem rede, token)."""
    inicio = datetime.now(timezone.utc).replace(microsecond=0)
    marca = (inicio.timestamp() - 5)
    try:
        _api_github("POST", f"/repos/{repo}/actions/workflows/{WORKFLOW_ARQ}/dispatches",
                    token, {"ref": "main"})
    except Exception as exc:
        return None, f"não consegui disparar no GitHub ({type(exc).__name__}: {exc})"

    desde = datetime.fromtimestamp(marca, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    caminho = (f"/repos/{repo}/actions/workflows/{WORKFLOW_ARQ}/runs"
               f"?event=workflow_dispatch&per_page=10&created=%3E%3D{desde}")
    t0 = time.time()
    while time.time() - t0 < MANUAL_ESPERA:
        time.sleep(MANUAL_POLL)
        try:
            _, dados = _api_github("GET", caminho, token)
        except Exception:
            continue
        runs = dados.get("workflow_runs") or []
        # A mais antiga criada depois do clique é a nossa (o cron-job.org
        # também dispara; se a dele terminar primeiro, serve do mesmo jeito).
        prontas = [r for r in runs if r.get("status") == "completed"]
        if any(r.get("conclusion") == "success" for r in prontas):
            return True, f"coleta nova no GitHub em {int(time.time() - t0)}s"
        if prontas and len(prontas) == len(runs):
            return False, f"run do GitHub terminou com '{prontas[0].get('conclusion')}'"
    return False, f"GitHub não terminou em {MANUAL_ESPERA}s"


def _atualizar_agora(timeout: int = FETCH_TIMEOUT) -> tuple[bool, str]:
    """O que o botão "Atualizar agora" faz: uma varredura nova de verdade."""
    token, repo = _token_github(), _repo_github()
    if token and repo:
        ok_gh, msg_gh = _coleta_github(token, repo)
        if ok_gh:
            ok, msg = _git_pull()
            if ok:
                ok_r, msg_r = _renderizar()
                if not ok_r:
                    return False, f"pull ok mas falhou ao renderizar: {msg_r}"
                return True, msg_gh
            msg_gh = f"{msg_gh}, mas o git pull falhou ({msg})"
        # GitHub fora, run falhou ou demorou: raspa aqui.
        ok_l, msg_l = _rodar_fetcher(timeout)
        return ok_l, f"{msg_l} (coleta local — {msg_gh})"
    ok_l, msg_l = _rodar_fetcher(timeout)
    return ok_l, f"{msg_l} (coleta local — sem GITHUB_TOKEN no .env.local)"


def _laco_automatico(intervalo: int, parar: threading.Event) -> None:
    """Coleta a cada `intervalo` segundos, para sempre.

    Roda como thread daemon. Se uma coleta demorar mais que o intervalo, a
    próxima simplesmente não acontece — o lock garante que nunca há duas.
    """
    while not parar.wait(intervalo):
        if not _fetch_lock.acquire(blocking=False):
            continue   # o botão está coletando agora; pula esta rodada
        try:
            agora = datetime.now().strftime("%H:%M:%S")
            ok, msg = _atualizar()
            print(f"  [{agora}] coleta automática: {msg}", flush=True)
        finally:
            _fetch_lock.release()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    # ---- respostas ----

    def _json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def end_headers(self) -> None:
        # o feed muda a cada coleta; cache do browser aqui só atrapalha
        if self.path.endswith((".json", ".html")):
            self.send_header("Cache-Control", "no-store, must-revalidate")
        super().end_headers()

    # ---- rotas ----

    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            self.send_response(302)
            self.send_header("Location", HOME_PAGE)
            self.end_headers()
            return
        if self.path == "/api/health":
            self._json({"ok": True, "features": ["asia-news-refresh",
                                                 "asia-news-manual-prompt",
                                                 "asia-news-shutdown"]})
            return
        super().do_GET()

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length") or 0)
        if length:
            self.rfile.read(length)

        if self.path == "/api/asia-news-refresh":
            self._refresh()
        elif self.path == "/api/asia-news-manual-prompt":
            self._manual_prompt()
        elif self.path == "/api/asia-news-shutdown":
            self._shutdown()
        else:
            self._json({"ok": False, "error": "rota desconhecida"}, 404)

    def _shutdown(self) -> None:
        """Encerra o monitor a pedido do painel.

        O shutdown() precisa rodar em outra thread: chamado de dentro do
        handler ele espera a própria requisição terminar e trava.
        """
        self._json({"ok": True})
        PIDFILE.unlink(missing_ok=True)

        def encerrar():
            time.sleep(0.4)          # deixa a resposta chegar no navegador
            if _servidor is not None:
                _servidor.shutdown()

        threading.Thread(target=encerrar, daemon=True).start()

    # ---- implementação ----

    def _run(self, args: list[str], timeout: int) -> tuple[bool, str, str]:
        try:
            proc = subprocess.run(
                [sys.executable, *args],
                cwd=str(CODE), capture_output=True, text=True, timeout=timeout,
            )
            return proc.returncode == 0, proc.stdout, proc.stderr
        except subprocess.TimeoutExpired:
            return False, "", f"tempo esgotado depois de {timeout}s"
        except Exception as exc:
            return False, "", f"{type(exc).__name__}: {exc}"

    def _refresh(self) -> None:
        if not _fetch_lock.acquire(blocking=False):
            self._json({"ok": False,
                        "error": "coleta automática em andamento, tente em instantes"}, 409)
            return
        try:
            ok, msg = _atualizar_agora()
            print(f"  [{datetime.now():%H:%M:%S}] atualizar agora: {msg}", flush=True)
            if not ok:
                self._json({"ok": False, "error": msg}, 500)
                return
            try:
                feed = json.loads(FEED_PATH.read_text("utf-8"))
            except (json.JSONDecodeError, OSError) as exc:
                self._json({"ok": False, "error": f"feed.json ilegível: {exc}"}, 500)
                return
            self._json({"ok": True,
                        "msg": msg,
                        "generated_at_utc": feed.get("generated_at_utc"),
                        "collected_at_utc": feed.get("collected_at_utc"),
                        "degraded": bool(feed.get("degraded")),
                        "sources_ok": feed.get("sources_ok"),
                        "sources_total": feed.get("sources_total"),
                        "count": feed.get("count", len(feed.get("items", []))),
                        "by_region": feed.get("by_region", {})})
        finally:
            _fetch_lock.release()

    def _manual_prompt(self) -> None:
        ok, out, err = self._run([str(CODE / "build_prompt.py"), "--json"],
                                 PROMPT_TIMEOUT)
        if not ok:
            self._json({"ok": False, "error": (err or "falhou").strip()[:200]}, 500)
            return
        try:
            self._json(json.loads(out))
        except json.JSONDecodeError:
            self._json({"ok": False, "error": "saída do builder não era JSON"}, 500)

    # ---- log enxuto ----

    def log_message(self, fmt: str, *args) -> None:
        if self.path.startswith("/api/"):
            sys.stderr.write(f"  {self.command} {self.path}\n")


def main() -> int:
    p = argparse.ArgumentParser(description="Painel local do Asia Macro News Monitor")
    p.add_argument("--port", type=int, default=8765)
    p.add_argument("--no-open", action="store_true")
    # 600s e não 300s: a coleta em si leva ~90s, então a 5 min o monitor
    # passava um terço do tempo batendo nas fontes. TradingView e o tradutor
    # do Google são APIs não oficiais — a 10 min a carga cai pela metade e
    # ninguém perde notícia, porque quase nada macro sai em janela de 5 min.
    p.add_argument("--interval", type=int, default=600,
                   help="segundos entre coletas automáticas (padrão 600 = 10 min)")
    p.add_argument("--no-watch", action="store_true",
                   help="não coletar automaticamente; só servir o painel")
    args = p.parse_args()

    if not (ROOT / HOME_FILE).exists():
        print(f"! {HOME_FILE} ainda não existe.")
        print(f"  Rode primeiro:  python3 \"{CODE / 'fetch_asia_news.py'}\"\n")

    global _servidor
    url = f"http://127.0.0.1:{args.port}{HOME_PAGE}"
    try:
        server = _servidor = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    except OSError as exc:
        print(f"! Não consegui abrir a porta {args.port}: {exc}")
        print("  Provavelmente o monitor já está rodando. Abra:")
        print(f"    {url}")
        return 1

    print(f"Asia Macro News Monitor em {url}")

    parar = threading.Event()
    if not args.no_watch:
        intervalo = max(MIN_INTERVAL, args.interval)
        threading.Thread(target=_laco_automatico, args=(intervalo, parar),
                         daemon=True).start()
        print(f"Coleta automática a cada {intervalo // 60} min "
              f"(primeira em {intervalo // 60} min).")
    print("Ctrl+C para parar.\n")

    if not args.no_open:
        threading.Timer(0.6, partial(webbrowser.open, url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        parar.set()
        server.server_close()
        PIDFILE.unlink(missing_ok=True)
    print("encerrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
