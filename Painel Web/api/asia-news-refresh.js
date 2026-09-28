// POST  →  dispara uma coleta no GitHub Actions e volta na hora.
// A coleta em si leva 1–3 min; quem espera o resultado é o painel, relendo o feed.
import { autorizado, dispararColeta, semCache } from "./_comum.js";

export default async function handler(req, res) {
  if (!autorizado(req, res)) return;
  semCache(res);
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "use POST" });
  try {
    await dispararColeta();
    res.status(200).json({ ok: true, dispatched: true });
  } catch (e) {
    res.status(502).json({ ok: false, error: e.message });
  }
}
