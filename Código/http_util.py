"""
Camada HTTP: um GET com User-Agent de browser, retry com backoff e nenhuma
exceção vazando. Todo fetch do projeto passa por aqui.

Só stdlib — o projeto inteiro roda com Python 3.10+ sem pip install.
"""

from __future__ import annotations

import gzip
import random
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from io import BytesIO

import asia_config as cfg

# Códigos que valem uma nova tentativa: rate limit e indisponibilidade.
RETRYABLE_STATUS = {408, 425, 429, 500, 502, 503, 504}


# ---------------------------------------------------------------------------
# Throttle por host
#
# Sem isto, as 25 queries do Google News saem quase juntas com 8 workers e ele
# devolve 429 para a maioria — foi o que derrubou 27 das 36 fontes na primeira
# coleta. O intervalo mínimo é por host, então RSS de sites diferentes continua
# em paralelo total; só o mesmo host é serializado.
# ---------------------------------------------------------------------------

HOST_MIN_INTERVAL = {
    "news.google.com": 1.1,
    "translate.googleapis.com": 0.2,
    "www.investing.com": 0.5,
}
DEFAULT_MIN_INTERVAL = 0.0

_host_lock: dict[str, threading.Lock] = defaultdict(threading.Lock)
_host_last: dict[str, float] = {}
_registry_lock = threading.Lock()


def _throttle(url: str) -> tuple[str, float]:
    """Espera o necessário para respeitar o intervalo mínimo do host."""
    try:
        host = urllib.parse.urlsplit(url).netloc.lower()
    except ValueError:
        return "", 0.0
    minimo = HOST_MIN_INTERVAL.get(host, DEFAULT_MIN_INTERVAL)
    if minimo <= 0:
        return host, 0.0

    with _registry_lock:
        lock = _host_lock[host]
    with lock:
        agora = time.monotonic()
        anterior = _host_last.get(host, 0.0)
        espera = minimo - (agora - anterior)
        if espera > 0:
            time.sleep(espera)
        _host_last[host] = time.monotonic()
    return host, minimo


def _penalizar(host: str) -> None:
    """Depois de um 429, dobra o intervalo daquele host até o fim da coleta."""
    if not host:
        return
    with _registry_lock:
        atual = HOST_MIN_INTERVAL.get(host, DEFAULT_MIN_INTERVAL)
        HOST_MIN_INTERVAL[host] = min(max(atual * 2, 1.0), 8.0)


def get_bytes(
    url: str,
    headers: dict | None = None,
    retries: int = cfg.HTTP_RETRIES,
    timeout: int = cfg.HTTP_TIMEOUT,
) -> bytes | None:
    """GET com retry. Devolve None em vez de levantar — o pipeline nunca para
    por causa de uma fonte fora do ar."""
    req_headers = {
        "User-Agent": cfg.USER_AGENT,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,ja;q=0.7",
        "Accept-Encoding": "gzip",
        "Connection": "close",
    }
    if headers:
        req_headers.update(headers)

    last_error = None
    for attempt in range(retries):
        host, _ = _throttle(url)
        try:
            req = urllib.request.Request(url, headers=req_headers)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                if resp.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.GzipFile(fileobj=BytesIO(raw)).read()
                return raw
        except urllib.error.HTTPError as exc:
            last_error = f"HTTP {exc.code}"
            if exc.code not in RETRYABLE_STATUS:
                return None
            if exc.code == 429:
                _penalizar(host)
                # o servidor às vezes diz quanto esperar; obedecer é o certo
                try:
                    ra = float(exc.headers.get("Retry-After") or 0)
                    if 0 < ra <= 30:
                        time.sleep(ra)
                except (TypeError, ValueError):
                    pass
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = str(getattr(exc, "reason", exc))[:80]

        if attempt < retries - 1:
            # backoff exponencial com jitter, para não sincronizar as threads
            time.sleep((2 ** attempt) * 0.8 + random.random() * 0.4)

    get_bytes.last_error = last_error  # type: ignore[attr-defined]
    return None


def get_text(url: str, **kwargs) -> str | None:
    raw = get_bytes(url, **kwargs)
    if raw is None:
        return None
    for encoding in ("utf-8", "shift_jis", "gb18030", "euc-kr", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")
