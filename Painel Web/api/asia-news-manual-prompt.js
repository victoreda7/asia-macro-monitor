// POST  →  {ok, prompt}. O prompt é gerado pelo Actions a cada coleta
// (Cache/prompt_curadoria.md, com as estatísticas do feed daquele momento).
import { autorizado, lerArquivo, semCache } from "./_comum.js";

export default async function handler(req, res) {
  if (!autorizado(req, res)) return;
  semCache(res);
  try {
    const prompt = await lerArquivo("Cache/prompt_curadoria.md");
    res.status(200).json({ ok: true, prompt });
  } catch (e) {
    res.status(502).json({
      ok: false,
      error: "Prompt ainda não gerado — ele aparece depois da primeira coleta com o código novo. " + e.message,
    });
  }
}
