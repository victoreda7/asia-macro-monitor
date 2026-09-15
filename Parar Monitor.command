#!/bin/bash
#
# Para o Ásia - Monitor de Notícias Macro. Duplo-clique neste arquivo.
#
# Encerra o painel e a coleta automática. As notícias já coletadas continuam
# no disco — nada é apagado. Para voltar, use "Abrir Monitor.command".
#
# Existe porque "Abrir Monitor.command" já mandava usar este arquivo aqui, que
# nunca tinha sido escrito: sem ele, a única forma de desligar era o botão
# Desligar do painel (e, se o painel não abrisse, um kill na mão).

cd "$(dirname "$0")" || exit 1
PIDFILE="$(pwd)/Cache/monitor.pid"

printf '\n  Ásia - Monitor de Notícias Macro\n'
printf '  %s\n\n' "$(printf '─%.0s' {1..46})"

if [ ! -f "$PIDFILE" ]; then
  printf '  O monitor não está rodando.\n\n'
  sleep 1.5
  exit 0
fi

PID="$(cat "$PIDFILE" 2>/dev/null)"
if ! kill -0 "$PID" 2>/dev/null; then
  printf '  O monitor não está rodando (PID %s já encerrado).\n\n' "$PID"
  rm -f "$PIDFILE"
  sleep 1.5
  exit 0
fi

kill "$PID" 2>/dev/null
for _ in $(seq 1 20); do
  kill -0 "$PID" 2>/dev/null || break
  sleep 0.3
done
if kill -0 "$PID" 2>/dev/null; then
  kill -9 "$PID" 2>/dev/null       # não saiu no pedido educado
  sleep 0.5
fi
rm -f "$PIDFILE"

printf '  Monitor parado (PID %s).\n' "$PID"
printf '  As notícias já coletadas continuam no disco.\n'
printf '  Para voltar, duplo-clique em "Abrir Monitor.command".\n\n'
sleep 2
