"""
Detecção de idioma e tradução de títulos para inglês, com cache em disco.

A tradução é o gargalo do pipeline, então três coisas importam aqui:
o cache (chave SHA256 de "idioma|texto"), o paralelismo modesto, e nunca
deixar uma falha de tradução derrubar o item — se não der para traduzir,
o título original segue em frente.

A API translate.googleapis.com/translate_a/single é não oficial. Use com
parcimônia: sem loop agressivo, sem lote gigante.
"""

from __future__ import annotations

import hashlib
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote

import asia_config as cfg
from http_util import get_text


# ---------------------------------------------------------------------------
# Detecção de idioma por faixa Unicode
# ---------------------------------------------------------------------------

def _ranges(text: str) -> tuple[bool, bool, bool]:
    hangul = kana = han = False
    for ch in text:
        if "가" <= ch <= "힯" or "ᄀ" <= ch <= "ᇿ":
            hangul = True
        elif "぀" <= ch <= "ヿ":
            kana = True
        elif "一" <= ch <= "鿿" or "㐀" <= ch <= "䶿":
            han = True
    return hangul, kana, han


_PT_HINTS = (
    " de ", " da ", " do ", " para ", " com ", " não ", " está ", " são ",
    "ções", "ação", "mercado", "juros", "bolsa", "após", "governo", "câmbio",
)


def detect_lang(text: str) -> str:
    """Devolve 'ko' | 'ja' | 'zh-CN' | 'pt' | 'en'."""
    if not text:
        return "en"
    hangul, kana, han = _ranges(text)
    if hangul:
        return "ko"
    if kana:
        return "ja"
    if han:
        return "zh-CN"

    low = f" {text.lower()} "
    if sum(h in low for h in _PT_HINTS) >= 2:
        return "pt"
    return "en"


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------

class TranslationCache:
    def __init__(self, path: Path):
        self.path = path
        self._lock = threading.Lock()
        self._data: dict[str, str] = {}
        self._dirty = False
        if path.exists():
            try:
                self._data = json.loads(path.read_text("utf-8"))
            except (json.JSONDecodeError, OSError):
                self._data = {}

    @staticmethod
    def key(lang: str, text: str) -> str:
        return hashlib.sha256(f"{lang}|{text}".encode("utf-8")).hexdigest()

    def get(self, lang: str, text: str) -> str | None:
        with self._lock:
            return self._data.get(self.key(lang, text))

    def put(self, lang: str, text: str, value: str) -> None:
        with self._lock:
            self._data[self.key(lang, text)] = value
            self._dirty = True

    def save(self) -> None:
        with self._lock:
            if not self._dirty:
                return
            self.path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(self._data, ensure_ascii=False), "utf-8")
            tmp.replace(self.path)
            self._dirty = False

    def __len__(self) -> int:
        return len(self._data)


# ---------------------------------------------------------------------------
# Tradução
# ---------------------------------------------------------------------------

_ENDPOINT = "https://translate.googleapis.com/translate_a/single"


def _translate_once(text: str, lang: str) -> str | None:
    url = f"{_ENDPOINT}?client=gtx&sl={lang}&tl=en&dt=t&q={quote(text)}"
    body = get_text(url, retries=2, timeout=15)
    if not body:
        return None
    try:
        data = json.loads(body)
        # formato: [[["traduzido","original",...], ...], ...]
        chunks = [seg[0] for seg in data[0] if seg and seg[0]]
        out = "".join(chunks).strip()
        return out or None
    except (json.JSONDecodeError, IndexError, TypeError):
        return None


def translate_items(items, cache: TranslationCache) -> None:
    """Preenche title_en/lang_original/translated in place.

    Só chama a rede para o que não estiver em cache e não for inglês.
    """
    pending = []
    for it in items:
        lang = detect_lang(it.title_original)
        it.lang_original = lang
        if lang == "en":
            it.title_en = it.title_original
            it.translated = False
            continue
        cached = cache.get(lang, it.title_original)
        if cached:
            it.title_en = cached
            it.translated = True
        else:
            pending.append((it, lang))

    if not pending:
        return

    lock = threading.Lock()

    def work(job):
        it, lang = job
        with lock:
            time.sleep(cfg.TRANSLATE_PAUSE / max(cfg.TRANSLATE_WORKERS, 1))
        out = _translate_once(it.title_original, lang)
        if out:
            cache.put(lang, it.title_original, out)
            it.title_en = out
            it.translated = True
        else:
            # falhou: mantém o original, marca como não traduzido.
            it.title_en = it.title_original
            it.translated = False

    with ThreadPoolExecutor(max_workers=cfg.TRANSLATE_WORKERS) as pool:
        list(pool.map(work, pending))

    cache.save()
