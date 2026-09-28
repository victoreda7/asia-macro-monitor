// POST {texto}  →  valida o JSON que a IA devolveu, grava como
// Cache/manual_additions.json no GitHub e dispara uma coleta para fundir.
import { autorizado, dispararColeta, gravarArquivo, semCache } from "./_comum.js";

const REGIOES = ["japan", "china", "taiwan", "korea"];

function extrairJson(texto) {
  let t = String(texto || "").trim();
  // A IA quase sempre devolve dentro de ```json ... ```
  const cerca = t.match(/```(?:json)?\s*([\s\S]*?)```/i);
  if (cerca) t = cerca[1].trim();
  const ini = t.indexOf("{"), fim = t.lastIndexOf("}");
  if (ini < 0 || fim < ini) throw new Error("não achei um objeto JSON no texto colado");
  return JSON.parse(t.slice(ini, fim + 1));
}

export default async function handler(req, res) {
  if (!autorizado(req, res)) return;
  semCache(res);
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "use POST" });

  let dados;
  try {
    const corpo = typeof req.body === "string" ? JSON.parse(req.body) : req.body || {};
    dados = extrairJson(corpo.texto);
  } catch (e) {
    return res.status(400).json({ ok: false, error: `JSON inválido: ${e.message}` });
  }

  const itens = Array.isArray(dados.items) ? dados.items : null;
  if (!itens || !itens.length) {
    return res.status(400).json({ ok: false, error: "esperava uma lista não vazia em \"items\"" });
  }
  if (itens.length > 80) {
    return res.status(400).json({ ok: false, error: `itens demais (${itens.length}); o limite é 80` });
  }
  const validos = itens.filter(
    (i) => i && typeof i.title_en === "string" && i.title_en.trim() &&
      typeof i.url === "string" && /^https?:\/\//.test(i.url) && REGIOES.includes(i.region),
  );
  if (!validos.length) {
    return res.status(400).json({
      ok: false,
      error: "nenhum item válido — cada um precisa de title_en, url (http…) e region (japan/china/taiwan/korea)",
    });
  }

  const arquivo = {
    items: validos,
    ...(dados.notes ? { notes: String(dados.notes).slice(0, 2000) } : {}),
    saved_at_utc: new Date().toISOString(),
    saved_via: "painel web",
  };

  try {
    await gravarArquivo(
      "Cache/manual_additions.json",
      JSON.stringify(arquivo, null, 2) + "\n",
      `curadoria IA via painel (${validos.length} itens)`,
    );
  } catch (e) {
    return res.status(502).json({ ok: false, error: e.message });
  }
  let disparou = true;
  try { await dispararColeta(); } catch { disparou = false; }
  res.status(200).json({
    ok: true,
    count: validos.length,
    discarded: itens.length - validos.length,
    dispatched: disparou,
  });
}
