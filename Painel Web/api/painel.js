// GET /  →  o mesmo HTML que o Actions gera e commita, com a marca de modo web.
import { autorizado, lerArquivo, semCache } from "./_comum.js";

export default async function handler(req, res) {
  if (!autorizado(req, res)) return;
  try {
    let html = await lerArquivo("Monitor de Notícias Macro.html");
    // Liga o modo web do painel: botões passam a falar com as funções daqui
    // (e não com o server.py local), e o "Desligar" some.
    // Favicon 🗻: arquivos estáticos desta pasta. Só entra se o HTML ainda não
    // trouxer o seu (o render_html.py novo já embute o mesmo ícone).
    const icone = html.includes('rel="icon"')
      ? ""
      : '\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">' +
        '\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">';
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
