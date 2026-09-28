// GET /Cache/feed.json  →  feed mais recente commitado pelo Actions.
// O painel relê este endereço a cada 5 min e depois de cada "Atualizar agora".
import { autorizado, lerArquivo, semCache } from "./_comum.js";

export default async function handler(req, res) {
  if (!autorizado(req, res)) return;
  try {
    const txt = await lerArquivo("Cache/feed.json");
    semCache(res);
    res.setHeader("Content-Type", "application/json; charset=utf-8");
    res.status(200).send(txt);
  } catch (e) {
    res.status(502).json({ ok: false, error: e.message });
  }
}
