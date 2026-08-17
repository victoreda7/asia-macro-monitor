#!/usr/bin/env python3
"""
Painel local do Asia Macro News Monitor.

    python3 server.py              sobe em http://127.0.0.1:8765 e abre o browser
    python3 server.py --port 9000  outra porta
    python3 server.py --no-open    não abre o browser

Serve a pasta do projeto e expõe duas rotas POST:
  /api/asia-news-refresh        roda o fetcher e devolve {ok, generated_at_utc, count}
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
from datetime import datetime
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
PROMPT_TIMEOUT = 60
MIN_INTERVAL = 60     # piso de segurança para o laço automático
PIDFILE = ROOT / "Cache" / "monitor.pid"

# Uma coleta por vez. O botão Atualizar e o laço automático disputam este lock,
# então um clique durante a coleta de fundo não dispara um segundo fetcher.
_fetch_lock = threading.Lock()

# Preenchido em main(). O botão Desligar precisa da instância para encerrar.
_servidor = None


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

    resumo = [ln for ln in (proc.stdout or "").splitlines() if ln.startswith("✓")]
    return True, resumo[-1] if resumo else "coleta concluída"


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
    try:
        proc = subprocess.run(
            ["git", "pull", "--ff-only", "--quiet"],
            cwd=str(ROOT), capture_output=True, text=True, timeout=30,
        )
    except subprocess.TimeoutExpired:
        return False, "git pull demorou demais (sem internet?)"
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"

    if proc.returncode != 0:
        linhas = (proc.stderr or proc.stdout or "").strip().splitlines()
        return False, linhas[-1] if linhas else "git pull falhou"
    return True, (proc.stdout or "").strip() or "já estava atualizado"


def _atualizar(timeout: int = FETCH_TIMEOUT) -> tuple[bool, str]:
    """Atualiza o feed: tenta git pull primeiro (rápido); só raspa localmente
    se o pull não der certo (sem git configurado, sem internet, etc.) — assim
    o monitor continua funcionando sozinho mesmo sem o GitHub Actions."""
    ok, msg = _git_pull()
    if ok:
        try:
            sys.path.insert(0, str(CODE))
            import render_html  # import tardio: só pesa o boot de quem usa git
            feed = json.loads(FEED_PATH.read_text("utf-8"))
            render_html.render(feed, ROOT / HOME_FILE)
        except Exception as exc:
            return False, f"pull ok mas falhou ao renderizar: {exc}"
        return True, f"git pull: {msg}"
    return _rodar_fetcher(timeout)


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
            ok, msg = _atualizar()
            if not ok:
                self._json({"ok": False, "error": msg}, 500)
                return
            try:
                feed = json.loads(FEED_PATH.read_text("utf-8"))
            except (json.JSONDecodeError, OSError) as exc:
                self._json({"ok": False, "error": f"feed.json ilegível: {exc}"}, 500)
                return
            self._json({"ok": True,
                        "generated_at_utc": feed.get("generated_at_utc"),
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
