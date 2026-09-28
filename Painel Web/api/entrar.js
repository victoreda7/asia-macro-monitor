// POST /entrar (formulário da tela de login) → grava o cookie de sessão e
// volta para o painel. Senha errada: espera 1 s (freia tentativa em massa)
// e volta para a tela com o aviso.
import { gravarSessao, semCache, senhaConfere } from "./_comum.js";

function lerSenha(req) {
  const b = req.body;
  if (b && typeof b === "object") return String(b.senha || "");
  if (typeof b === "string") return new URLSearchParams(b).get("senha") || "";
  return "";
}

export default async function handler(req, res) {
  semCache(res);
  if (req.method !== "POST") {
    res.setHeader("Location", "/");
    return res.status(303).end();
  }
  if (senhaConfere(lerSenha(req))) {
    gravarSessao(res);
    res.setHeader("Location", "/");
  } else {
    await new Promise((ok) => setTimeout(ok, 1000));
    res.setHeader("Location", "/?erro=1");
  }
  res.status(303).end();
}
