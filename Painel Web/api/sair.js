// GET /sair → apaga o cookie de sessão deste navegador.
import { apagarSessao, semCache } from "./_comum.js";

export default function handler(req, res) {
  semCache(res);
  apagarSessao(res);
  res.setHeader("Location", "/");
  res.status(303).end();
}
