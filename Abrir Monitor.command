#!/bin/bash
#
# Abre o Ásia - Monitor de Notícias Macro. Duplo-clique neste arquivo.
#
# Sobe o painel em segundo plano com a coleta automática de 10 em 10 minutos.
# Pode fechar esta janela do Terminal: o monitor continua rodando.
# Para desligar, use "Parar Monitor.command".

cd "$(dirname "$0")" || exit 1
PROJETO="$(pwd)"
CODIGO="$PROJETO/Código"
CACHE="$PROJETO/Cache"
PIDFILE="$CACHE/monitor.pid"
LOG="$CACHE/monitor.log"
PORTA=8765
URL="http://127.0.0.1:$PORTA/Monitor%20de%20Not%C3%ADcias%20Macro.html"

mkdir -p "$CACHE"

printf '\n  Ásia - Monitor de Notícias Macro\n'
printf '  %s\n\n' "$(printf '─%.0s' {1..46})"

# --- Já está rodando? -------------------------------------------------------
if [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE" 2>/dev/null)" 2>/dev/null; then
  printf '  Já estava rodando (PID %s).\n' "$(cat "$PIDFILE")"
  printf '  Abrindo o painel.\n\n'
  open "$URL"
  sleep 1
  exit 0
fi
rm -f "$PIDFILE"

# --- Python -----------------------------------------------------------------
PY=""
for cmd in python3 /usr/local/bin/python3 /opt/homebrew/bin/python3 /usr/bin/python3; do
  if command -v "$cmd" >/dev/null 2>&1; then PY="$cmd"; break; fi
done

if [ -z "$PY" ]; then
  printf '  Python 3 não encontrado.\n\n'
  printf '  Instale com:  xcode-select --install\n\n'
  read -r -p "  Enter para fechar."
  exit 1
fi

if [ "$("$PY" -c 'import sys; print(1 if sys.version_info >= (3,9) else 0)' 2>/dev/null)" != "1" ]; then
  printf '  ! Precisa de Python 3.9 ou mais novo.\n'
  printf '    Atualize com:  xcode-select --install\n\n'
  read -r -p "  Enter para fechar."
  exit 1
fi
printf '  Python %s\n' "$("$PY" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"

# --- Primeira coleta, em primeiro plano para você ver o progresso ------------
if [ ! -f "$CACHE/feed.json" ]; then
  printf '  Sem feed ainda — fazendo a primeira coleta.\n'
  printf '  Leva de 1 a 3 minutos. Só nesta primeira vez.\n\n'
  if ! "$PY" "$CODIGO/fetch_asia_news.py"; then
    printf '\n  ! A coleta falhou. Para ver quais fontes responderam:\n'
    printf '      cd "%s" && python3 fetch_asia_news.py --check\n\n' "$CODIGO"
    read -r -p "  Enter para fechar."
    exit 1
  fi
  printf '\n'
fi

# --- Painel em segundo plano ------------------------------------------------
# nohup faz o processo ignorar o SIGHUP que o macOS manda ao fechar o Terminal.
# O -u é necessário: sem tty o Python bufferiza a saída e o log fica mudo por
# minutos, o que atrapalha justamente quando você precisa dele.
: > "$LOG"
nohup "$PY" -u "$CODIGO/server.py" --port "$PORTA" --interval 600 --no-open \
      >> "$LOG" 2>&1 &
echo $! > "$PIDFILE"

# Espera a porta responder antes de abrir o navegador.
for _ in $(seq 1 25); do
  if "$PY" - "$PORTA" <<'EOF' 2>/dev/null
import socket, sys
s = socket.socket()
s.settimeout(0.4)
sys.exit(0 if s.connect_ex(("127.0.0.1", int(sys.argv[1]))) == 0 else 1)
EOF
  then break; fi
  sleep 0.4
done

if ! kill -0 "$(cat "$PIDFILE" 2>/dev/null)" 2>/dev/null; then
  printf '  ! O painel não subiu. Últimas linhas do log:\n\n'
  tail -12 "$LOG" | sed 's/^/    /'
  printf '\n'
  rm -f "$PIDFILE"
  read -r -p "  Enter para fechar."
  exit 1
fi

open "$URL"

printf '  Painel no ar (PID %s)\n' "$(cat "$PIDFILE")"
printf '  %s\n\n' "$URL"
printf '  Coleta automática a cada 10 minutos.\n'
printf '  Pode fechar esta janela — o monitor continua rodando.\n'
printf '  Para desligar, use "Parar Monitor.command".\n\n'
sleep 2
