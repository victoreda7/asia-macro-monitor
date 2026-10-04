// GET/POST /api/coletar?chave=...  →  chamado pelo cron-job.org a cada 10 min.
// É o que mantém a coleta no ritmo: o agendador do próprio GitHub atrasa
// horas nesse intervalo (medido: ~6 coletas/dia em vez de 144).
import { dispararColeta, igual, semCache } from "./_comum.js";

export default async function handler(req, res) {
  semCache(res);
  const chave = process.env.CRON_CHAVE;
  const recebida = req.query?.chave || req.headers["x-cron-chave"] || "";
  if (!chave || !igual(recebida, chave)) {
    return res.status(401).json({ ok: false, error: "chave inválida" });
  }
  try {
    const { tentativas } = await dispararColeta();
    res.status(202).json({ ok: true, dispatched: true, tentativas, at: new Date().toISOString() });
  } catch (e) {
    res.status(502).json({ ok: false, error: e.message });
  }
}
