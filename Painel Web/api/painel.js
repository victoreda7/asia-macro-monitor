// GET /  →  o mesmo HTML que o Actions gera e commita, com a marca de modo web.
import { autorizado, lerArquivo, semCache } from "./_comum.js";

export default async function handler(req, res) {
  if (!autorizado(req, res)) return;
  try {
    let html = await lerArquivo("Monitor de Notícias Macro.html");
    // Favicon 🗻 desenhado (Painel Web/favicon.*): troca qualquer ícone que
    // o HTML traga, para o painel web não depender da versão do render_html.
    // O ?v= força o navegador a largar o ícone antigo do cache.
    html = html
      .replace(/<!-- favicon[\s\S]*?-->\s*/g, "")
      .replace(/<link rel="(?:icon|alternate icon|apple-touch-icon)"[^>]*>\s*/g, "");
    const icone =
      '\n<link rel="icon" href="/favicon.svg?v=2" type="image/svg+xml">' +
      '\n<link rel="icon" href="/favicon-32.png?v=2" type="image/png" sizes="32x32">' +
      '\n<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">';
    // Liga o modo web do painel: botões passam a falar com as funções daqui
    // (e não com o server.py local), e o "Desligar" some.
    html = html.replace(
      "<head>",
      '<head>\n<script>window.__MODO_WEB__=true;</script>\n<meta name="robots" content="noindex, nofollow">' + icone,
    );
    semCache(res);
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.status(200).send(html);
  } catch (e) {
    res.status(502).send(`Não consegui ler o painel no GitHub: ${e.message}`);
  }
}
