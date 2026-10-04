// Peças compartilhadas pelas funções do painel. Arquivos que começam com "_"
// não viram rota na Vercel.
//
// O GitHub é a única fonte de verdade: o Actions coleta e commita o feed; aqui
// a gente só lê o que está no repositório e, quando pedido, dispara uma coleta
// nova (workflow_dispatch). Nada fica guardado na Vercel além das variáveis.

import { createHash, createHmac, timingSafeEqual } from "node:crypto";

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

// Login com senha única e cookie de sessão de longa duração.
//
// Depois de entrar uma vez, o navegador guarda o cookie "amm_sessao" e não
// pede mais a senha. Cada acesso renova o cookie por mais 400 dias (o teto
// que Chrome e Safari aceitam), então, usando o painel de vez em quando, a
// sessão não expira nunca. Trocar PAINEL_SENHA na Vercel derruba todas as
// sessões, porque o cookie é derivado dela.
//
// O cabeçalho Basic Auth continua aceito (útil para testes com curl), mas o
// navegador não é mais desafiado com a janelinha nativa.

const COOKIE = "amm_sessao";
const VALIDADE_S = 400 * 24 * 3600;

function tokenSessao(senha) {
  return createHmac("sha256", senha).update("asia-macro-monitor:sessao:v1").digest("hex");
}

function lerCookie(req, nome) {
  const bruto = req.headers.cookie || "";
  for (const parte of bruto.split(";")) {
    const i = parte.indexOf("=");
    if (i > 0 && parte.slice(0, i).trim() === nome) return decodeURIComponent(parte.slice(i + 1).trim());
  }
  return "";
}

export function gravarSessao(res) {
  const valor = tokenSessao(process.env.PAINEL_SENHA);
  res.setHeader(
    "Set-Cookie",
    `${COOKIE}=${valor}; Max-Age=${VALIDADE_S}; Path=/; HttpOnly; Secure; SameSite=Lax`,
  );
}

export function apagarSessao(res) {
  res.setHeader("Set-Cookie", `${COOKIE}=; Max-Age=0; Path=/; HttpOnly; Secure; SameSite=Lax`);
}

export function senhaConfere(senha) {
  return !!process.env.PAINEL_SENHA && igual(senha, process.env.PAINEL_SENHA);
}

// pagina=true: quem pede é o navegador abrindo o painel → mostra a tela de
// login. Nas rotas /api/* devolve 401 em JSON.
export function autorizado(req, res, { pagina = false } = {}) {
  const senha = process.env.PAINEL_SENHA;
  if (!senha) {
    res.status(500).json({ ok: false, error: "PAINEL_SENHA não configurada na Vercel" });
    return false;
  }
  const cookie = lerCookie(req, COOKIE);
  if (cookie && igual(cookie, tokenSessao(senha))) {
    gravarSessao(res); // renova os 400 dias a cada uso
    return true;
  }
  const h = req.headers.authorization || "";
  if (h.startsWith("Basic ")) {
    const dec = Buffer.from(h.slice(6), "base64").toString("utf8");
    if (igual(dec.slice(dec.indexOf(":") + 1), senha)) return true;
  }
  if (pagina) {
    const erro = /[?&]erro=1\b/.test(req.url || "");
    semCache(res);
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.status(401).send(paginaLogin(erro));
  } else {
    res.status(401).json({ ok: false, error: "sessão expirada — recarregue a página e entre de novo" });
  }
  return false;
}

function paginaLogin(erro) {
  return `<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Asia Macro News Monitor</title>
<link rel="icon" href="/favicon.svg?v=3" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png?v=3" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=3">
<style>
:root{--bg:#f4f5f7;--card:#fff;--tx:#14181f;--tx2:#5b6472;--line:#dfe3e8;--acc:#1f5fd6;--err:#c62a26}
@media (prefers-color-scheme:dark){:root{--bg:#15181d;--card:#1e2229;--tx:#e8ebf0;--tx2:#9aa3b0;--line:#2e343d;--acc:#5b8ff0;--err:#f06a5c}}
*{box-sizing:border-box}
body{margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:16px;
  background:var(--bg);color:var(--tx);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
form{width:100%;max-width:340px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:26px 24px}
img{display:block;width:56px;height:56px;margin:0 auto 12px}
h1{font-size:17px;font-weight:650;margin:0 0 4px;text-align:center}
p{margin:0 0 18px;color:var(--tx2);font-size:13px;text-align:center}
input{width:100%;font:inherit;padding:10px 12px;border:1px solid var(--line);border-radius:9px;background:var(--bg);color:var(--tx)}
input:focus{outline:2px solid var(--acc);outline-offset:1px}
button{width:100%;margin-top:12px;font:inherit;font-weight:600;padding:10px;border:0;border-radius:9px;background:var(--acc);color:#fff;cursor:pointer}
.erro{color:var(--err);font-size:13px;margin:10px 0 0;text-align:center}
.user{position:absolute;left:-9999px}
</style></head><body>
<form method="post" action="/entrar">
  <img src="/favicon.svg?v=3" alt="">
  <h1>Asia Macro News Monitor</h1>
  <p>Entre uma vez; este navegador fica conectado.</p>
  <input class="user" type="text" name="usuario" autocomplete="username" value="victor" tabindex="-1" aria-hidden="true">
  <input type="password" name="senha" placeholder="Senha" autocomplete="current-password" autofocus required>
  <button type="submit">Entrar</button>
  ${erro ? '<div class="erro">Senha incorreta.</div>' : ""}
</form></body></html>`;
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
//
// Cada tentativa tem prazo próprio e há até 3 tentativas. Motivo: em 03/10
// 22:02 UTC uma chamada ao GitHub ficou pendurada sem resposta, a função
// esperou até o fim e o cron-job.org (limite de 30 s) registrou "Timeout" —
// a coleta daquele horário nunca foi disparada. Com prazo + nova tentativa, um
// soluço isolado do GitHub é absorvido dentro da mesma chamada. Se uma
// tentativa "expirada" tiver chegado ao GitHub, o pior caso é uma coleta extra
// na fila, inofensiva.
const PRAZO_TENTATIVA_MS = 7000;
const TENTATIVAS = 3;

export async function dispararColeta() {
  if (!TOKEN) throw new Error("GITHUB_TOKEN não configurado na Vercel");
  let ultimoErro;
  let feitas = 0;
  for (let i = 1; i <= TENTATIVAS; i++) {
    feitas = i;
    try {
      const r = await fetch(
        `https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW}/dispatches`,
        {
          method: "POST",
          headers: cabecalhos({ Accept: "application/vnd.github+json", "Content-Type": "application/json" }),
          body: JSON.stringify({ ref: BRANCH }),
          signal: AbortSignal.timeout(PRAZO_TENTATIVA_MS),
        },
      );
      if (r.status === 204 || r.status === 200) return { tentativas: i };
      const txt = (await r.text()).slice(0, 200);
      ultimoErro = new Error(`GitHub recusou o disparo (${r.status}): ${txt}`);
      // 4xx (token, permissão, workflow inexistente) não melhora tentando de novo.
      if (r.status >= 400 && r.status < 500 && r.status !== 429) break;
    } catch (e) {
      const expirou = e?.name === "TimeoutError" || e?.name === "AbortError";
      ultimoErro = new Error(
        expirou ? `GitHub não respondeu em ${PRAZO_TENTATIVA_MS / 1000} s` : `falha de rede: ${e.message}`,
      );
    }
    if (i < TENTATIVAS) await new Promise((ok) => setTimeout(ok, 1000 * i));
  }
  throw new Error(`${ultimoErro.message} (após ${feitas} tentativa${feitas > 1 ? "s" : ""})`);
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
