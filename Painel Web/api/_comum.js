// Peças compartilhadas pelas funções do painel. Arquivos que começam com "_"
// não viram rota na Vercel.
//
// O GitHub é a única fonte de verdade: o Actions coleta e commita o feed; aqui
// a gente só lê o que está no repositório e, quando pedido, dispara uma coleta
// nova (workflow_dispatch). Nada fica guardado na Vercel além das variáveis.

import { createHash, timingSafeEqual } from "node:crypto";

export const REPO = process.env.GITHUB_REPO || "victoreda7/asia-macro-monitor";
export const BRANCH = process.env.GITHUB_BRANCH || "main";
export const WORKFLOW = process.env.GITHUB_WORKFLOW || "collect.yml";
const TOKEN = process.env.GITHUB_TOKEN || "";

// Comparação em tempo constante: hash dos dois lados para igualar o tamanho.
export function igual(a, b) {
  const ha = createHash("sha256").update(String(a ?? "")).digest();
  const hb = createHash("sha256").update(String(b ?? "")).digest();
  return timingSafeEqual(ha, hb);
}

// Senha única via Basic Auth: o navegador pergunta uma vez e reenvia sozinho
// em todos os fetch() da página (mesma origem). O usuário pode ser qualquer um.
export function autorizado(req, res) {
  const senha = process.env.PAINEL_SENHA;
  if (!senha) {
    res.status(500).json({ ok: false, error: "PAINEL_SENHA não configurada na Vercel" });
    return false;
  }
  const h = req.headers.authorization || "";
  if (h.startsWith("Basic ")) {
    const dec = Buffer.from(h.slice(6), "base64").toString("utf8");
    const pw = dec.slice(dec.indexOf(":") + 1);
    if (igual(pw, senha)) return true;
  }
  res.setHeader("WWW-Authenticate", 'Basic realm="Asia Macro Monitor", charset="UTF-8"');
  res.status(401).send("Senha necessária.");
  return false;
}

export function semCache(res) {
  res.setHeader("Cache-Control", "no-store, max-age=0");
}

function cabecalhos(extra = {}) {
  const h = {
    "User-Agent": "asia-macro-painel",
    "X-GitHub-Api-Version": "2022-11-28",
    ...extra,
  };
  if (TOKEN) h.Authorization = `Bearer ${TOKEN}`;
  return h;
}

const codificar = (caminho) => caminho.split("/").map(encodeURIComponent).join("/");

// Lê um arquivo do repositório. A API de conteúdo não tem o cache de ~5 min
// do raw.githubusercontent.com — que atrasaria cada coleta nova no painel.
export async function lerArquivo(caminho) {
  const url = `https://api.github.com/repos/${REPO}/contents/${codificar(caminho)}?ref=${BRANCH}`;
  const r = await fetch(url, {
    headers: cabecalhos({ Accept: "application/vnd.github.raw" }),
    cache: "no-store",
  });
  if (r.ok) return await r.text();
  // Sem token (ou limite estourado), o repositório público ainda serve pelo raw.
  const r2 = await fetch(
    `https://raw.githubusercontent.com/${REPO}/${BRANCH}/${codificar(caminho)}`,
    { cache: "no-store" },
  );
  if (r2.ok) return await r2.text();
  throw new Error(`GitHub respondeu ${r.status} ao ler ${caminho}`);
}

// Pede uma coleta ao GitHub Actions. Se já houver uma rodando, a nova fica na
// fila (o workflow tem concurrency group), então disparar a mais não faz mal.
export async function dispararColeta() {
  if (!TOKEN) throw new Error("GITHUB_TOKEN não configurado na Vercel");
  const r = await fetch(
    `https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW}/dispatches`,
    {
      method: "POST",
      headers: cabecalhos({ Accept: "application/vnd.github+json", "Content-Type": "application/json" }),
      body: JSON.stringify({ ref: BRANCH }),
    },
  );
  if (r.status !== 204 && r.status !== 200) {
    const txt = (await r.text()).slice(0, 200);
    throw new Error(`GitHub recusou o disparo (${r.status}): ${txt}`);
  }
}

// Cria ou substitui um arquivo no repositório com um commit.
export async function gravarArquivo(caminho, conteudo, mensagem) {
  if (!TOKEN) throw new Error("GITHUB_TOKEN não configurado na Vercel");
  const url = `https://api.github.com/repos/${REPO}/contents/${codificar(caminho)}`;
  let sha;
  const atual = await fetch(`${url}?ref=${BRANCH}`, {
    headers: cabecalhos({ Accept: "application/vnd.github+json" }),
    cache: "no-store",
  });
  if (atual.ok) sha = (await atual.json()).sha;
  const r = await fetch(url, {
    method: "PUT",
    headers: cabecalhos({ Accept: "application/vnd.github+json", "Content-Type": "application/json" }),
    body: JSON.stringify({
      message: mensagem,
      content: Buffer.from(conteudo, "utf8").toString("base64"),
      branch: BRANCH,
      ...(sha ? { sha } : {}),
    }),
  });
  if (!r.ok) {
    const txt = (await r.text()).slice(0, 200);
    throw new Error(`GitHub recusou a gravação (${r.status}): ${txt}`);
  }
}
