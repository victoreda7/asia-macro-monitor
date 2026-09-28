"""
Gera "Monitor de Notícias Macro.html" com o feed embutido.

O HTML é autocontido de propósito: abre por duplo-clique e já mostra as
notícias. Quando servido pelo painel local (127.0.0.1), ganha os dois botões
que realmente fazem coisa — atualizar agora e gerar o prompt de curadoria.
"""

from __future__ import annotations

import json
from pathlib import Path

import asia_config as cfg

TEMPLATE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Asia Macro News Monitor</title>
<!-- favicon 🗻: SVG com o emoji (Chrome/Firefox/Edge) e PNG para Safari e
     para o ícone da tela inicial do iPhone -->
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%97%BB%3C/text%3E%3C/svg%3E">
<link rel="apple-touch-icon" href="data:image/png;base64,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">
<style>
:root{color-scheme:light;--bg:#fff;--panel:#f7f8fa;--line:#e3e6eb;--line2:#eef0f4;
 --tx:#14181f;--tx2:#5b6472;--tx3:#8b95a3;--acc:#1a56db;--acc-soft:#eef3fe;
 --jp:#1f6feb;--cn:#d92626;--tw:#8b5cf6;--kr:#0f9d63;
 --ok:#0f9d63;--warn:#c2761a;--err:#dc2626}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--tx);
 font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,sans-serif;
 -webkit-font-smoothing:antialiased}
a{color:inherit}
header{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.95);
 backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:14px 20px 0}
.hrow{display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap}
h1{margin:0;font-size:17px;font-weight:650;letter-spacing:-.01em}
.sub{color:var(--tx3);font-size:12px;margin-top:3px}
.sub strong{color:var(--tx2)}
.spacer{flex:1}
.btns{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
button{font:inherit;font-size:13px;font-weight:500;cursor:pointer;border-radius:8px;
 border:1px solid var(--line);background:#fff;color:var(--tx);padding:7px 13px;
 white-space:nowrap;transition:.12s}
button:hover:not(:disabled){background:var(--panel);border-color:#cfd5de}
button:disabled{opacity:.55;cursor:default}
button.primary{background:var(--acc);border-color:var(--acc);color:#fff}
button.primary:hover:not(:disabled){background:#1546b8;border-color:#1546b8}
button.ghost{border-color:transparent;color:var(--tx3);padding:7px 10px}
button.ghost:hover:not(:disabled){background:#fdf0f0;border-color:#f3c9c9;color:var(--err)}
button.ghost.armado{background:var(--err);border-color:var(--err);color:#fff}
/* bandeiras */
.flags{display:flex;gap:6px;margin-top:13px;flex-wrap:wrap}
.flag{display:inline-flex;align-items:center;gap:7px;padding:6px 13px 6px 10px;
 border:1px solid var(--line);border-radius:22px;background:#fff;cursor:pointer;
 user-select:none;transition:.12s}
.flag:hover{border-color:#aab3c0}
.flag .em{font-size:17px;line-height:1}
.flag .nm{font-size:13px;font-weight:600}
.flag .ct{font-size:11px;font-weight:600;opacity:.5}
.flag.on{background:var(--tx);border-color:var(--tx);color:#fff}
.flag.on .ct{opacity:.75}
.flag.on.japan{background:var(--jp);border-color:var(--jp)}
.flag.on.china{background:var(--cn);border-color:var(--cn)}
.flag.on.taiwan{background:var(--tw);border-color:var(--tw)}
.flag.on.korea{background:var(--kr);border-color:var(--kr)}
nav{display:flex;gap:2px;margin-top:12px}
nav button{border:0;background:none;border-radius:0;padding:8px 12px;color:var(--tx2);
 border-bottom:2px solid transparent}
nav button:hover{background:none;color:var(--tx)}
nav button.on{color:var(--acc);border-bottom-color:var(--acc);font-weight:600}
/* filtros */
.filters{padding:11px 20px;border-bottom:1px solid var(--line2);background:var(--panel);
 display:flex;gap:16px;flex-wrap:wrap;align-items:center}
.fg{display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.fg>.lb{font-size:11px;color:var(--tx3);text-transform:uppercase;letter-spacing:.05em;
 font-weight:600;margin-right:2px}
.chip{border:1px solid var(--line);background:#fff;border-radius:20px;padding:4px 11px;
 font-size:12.5px;color:var(--tx2);cursor:pointer;user-select:none;transition:.12s}
.chip:hover{border-color:#c3cad4}
.chip.on{background:var(--tx);border-color:var(--tx);color:#fff;font-weight:500}
input[type=search]{border:1px solid var(--line);border-radius:8px;padding:6px 11px;
 font:inherit;font-size:13px;min-width:200px;background:#fff}
input[type=search]:focus{outline:none;border-color:var(--acc)}
main{padding:16px 20px 70px;max-width:1060px}
.meta{font-size:12px;color:var(--tx3);margin-bottom:12px;display:flex;gap:9px;flex-wrap:wrap;align-items:center}
.dot{width:6px;height:6px;border-radius:50%;background:var(--ok);display:inline-block}
.dot.warn{background:var(--warn)}.dot.err{background:var(--err)}
/* cards */
.card{border:1px solid var(--line);border-left:3px solid var(--line);border-radius:9px;
 padding:12px 15px;margin-bottom:8px;background:#fff;transition:.12s}
.card:hover{border-color:#cfd5de;box-shadow:0 1px 4px rgba(16,24,40,.06)}
.card.japan{border-left-color:var(--jp)}.card.china{border-left-color:var(--cn)}
.card.taiwan{border-left-color:var(--tw)}.card.korea{border-left-color:var(--kr)}
.tags{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin-bottom:5px}
.tag{font-size:10.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
 padding:2px 7px;border-radius:4px;background:var(--panel);color:var(--tx2)}
.tag.r-japan{background:#e9f1fe;color:var(--jp)}.tag.r-china{background:#fdeaea;color:var(--cn)}
.tag.r-taiwan{background:#f2ecfe;color:var(--tw)}.tag.r-korea{background:#e6f7f0;color:var(--kr)}
.tag.b-live{background:#fff1e8;color:#c2410c}
.tag.b-manual{background:#e6f7f0;color:var(--ok)}
.tag.b-tr{background:#f3f0ff;color:#6d4bd8}
.when{font-size:11.5px;color:var(--tx3);margin-left:auto;white-space:nowrap}
.card h3{margin:0 0 4px;font-size:14.5px;font-weight:600;line-height:1.42;letter-spacing:-.005em}
.card h3 a{text-decoration:none}
.card h3 a:hover{color:var(--acc);text-decoration:underline}
.orig{margin:0 0 5px;font-size:12.5px;color:var(--tx3);line-height:1.45}
.src{font-size:12px;color:var(--tx3)}
.empty{padding:46px 20px;text-align:center;color:var(--tx3);border:1px dashed var(--line);border-radius:10px}
/* saude das fontes */
.health{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:7px}
.hrow2{display:flex;align-items:center;gap:9px;padding:8px 12px;border:1px solid var(--line);
 border-radius:8px;background:#fff;font-size:12.5px}
.hrow2.bad{border-color:#f3c9c9;background:#fffafa}
.hrow2 .nm{font-weight:600;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.hrow2 .ct{margin-left:auto;color:var(--tx3);font-size:11.5px;flex:none}
.hrow2 .er{color:var(--err);font-size:11px}
.note{margin:0 0 14px;padding:11px 14px;background:var(--acc-soft);border:1px solid #d3e0fb;
 border-radius:9px;font-size:12.5px;color:#1e3a8a;line-height:1.5}
.note.warn{background:#fff7e6;border-color:#f5d99a;color:#8a5a00}
/* modal */
.overlay{position:fixed;inset:0;background:rgba(15,20,28,.45);z-index:60;display:flex;
 align-items:center;justify-content:center;padding:26px}
.modal{background:#fff;border-radius:12px;max-width:820px;width:100%;max-height:82vh;
 display:flex;flex-direction:column;box-shadow:0 18px 48px rgba(16,24,40,.22)}
.modal header{position:static;border:0;border-bottom:1px solid var(--line);padding:15px 18px;
 background:none;backdrop-filter:none;display:flex;align-items:center;gap:12px}
.modal h2{margin:0;font-size:15px;font-weight:650}
.modal pre{margin:0;padding:16px 18px;overflow:auto;flex:1;font-size:12px;line-height:1.55;
 font-family:ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap;word-break:break-word}
.modal footer{border-top:1px solid var(--line);padding:12px 18px;display:flex;gap:9px;align-items:center}
.toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%);z-index:80;
 background:var(--tx);color:#fff;padding:10px 18px;border-radius:9px;font-size:13px;
 box-shadow:0 8px 24px rgba(16,24,40,.25)}
.spin{display:inline-block;width:11px;height:11px;border:2px solid #cbd5e1;
 border-top-color:var(--acc);border-radius:50%;animation:sp .7s linear infinite;
 vertical-align:-1px;margin-right:6px}
@keyframes sp{to{transform:rotate(360deg)}}
.hidden{display:none}
</style>
</head>
<body>
<header>
  <div class="hrow">
    <div>
      <h1>Asia Macro News Monitor</h1>
      <div class="sub" id="sub"></div>
    </div>
    <div class="spacer"></div>
    <div class="btns">
      <button id="btnRefresh" title="Roda o fetcher e puxa a web de novo">↻ Atualizar agora</button>
      <button id="btnManual" class="primary" title="Gera o prompt para uma IA curar o que o automático perdeu">Curadoria IA</button>
      <button id="btnOff" class="ghost" title="Encerra o monitor e a coleta automática">Desligar</button>
    </div>
  </div>
  <div class="flags" id="flags"></div>
  <nav>
    <button id="tabFeed" class="on">Notícias</button>
    <button id="tabHealth">Saúde das fontes</button>
  </nav>
</header>

<div class="filters" id="filters">
  <div class="fg" id="fPeriod"><span class="lb">Período</span></div>
  <div class="fg" id="fTopic"><span class="lb">Tópico</span></div>
  <div class="fg"><input type="search" id="q" placeholder="Buscar no título…"></div>
</div>

<main>
  <section id="viewFeed">
    <div id="banner"></div>
    <div class="meta" id="status"></div>
    <div id="list"></div>
  </section>
  <section id="viewHealth" class="hidden">
    <div class="note">Uma fonte vermelha não quebra o feed — o pipeline segue com as outras.
      Falha recorrente costuma ser bloqueio por User-Agent, mudança de layout ou feed que saiu do ar.
      <strong>Parada desde</strong> quer dizer que a fonte respondeu normalmente, mas o item mais
      recente dela é velho — feed abandonado que ainda serve XML.</div>
    <div class="health" id="healthlist"></div>
  </section>
</main>

<script>
var FEED = __FEED__;

var REGIONS = __REGIONS__;
var TOPICS  = __TOPICS__;
var PERIODS = [["24h","24 horas",1],["3d","3 dias",3],["7d","7 dias",7],["30d","30 dias",30],["all","Tudo",0]];

var filt = {region:"all", topic:[], period:"7d", q:""};
try{ var s=localStorage.getItem("amnm-filt"); if(s) filt=Object.assign(filt,JSON.parse(s)); }catch(e){}
function save(){ try{ localStorage.setItem("amnm-filt",JSON.stringify(filt)); }catch(e){} }

function esc(s){ return String(s==null?"":s).replace(/[&<>"']/g,function(c){
  return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]; }); }

function ago(iso){
  var d=(Date.now()-new Date(iso).getTime())/1000;
  if(isNaN(d)) return "";
  if(d<60) return "agora";
  if(d<3600) return Math.round(d/60)+" min";
  if(d<86400) return Math.round(d/3600)+" h";
  if(d<604800) return Math.round(d/86400)+" d";
  try{ return new Date(iso).toLocaleDateString("pt-BR",{day:"2-digit",month:"short"}); }
  catch(e){ return ""; }
}
function fmtFull(iso){
  try{ return new Date(iso).toLocaleString("pt-BR",{day:"2-digit",month:"short",year:"numeric",hour:"2-digit",minute:"2-digit"}); }
  catch(e){ return iso; }
}

/* modo web: servido pela Vercel, que injeta window.__MODO_WEB__ no <head>.
   Lá a coleta roda no GitHub Actions; os botões disparam e esperam o feed. */
function modoWeb(){ return window.__MODO_WEB__===true; }
function painelLocal(){
  return location.protocol==="http:" &&
    (location.hostname==="127.0.0.1"||location.hostname==="localhost");
}
/* quem consegue buscar na web: o painel local (server.py) ou o painel web */
function canRunPanel(){ return painelLocal() || modoWeb(); }

function items(){ return (FEED.items)||[]; }

function inPeriod(it){
  var p=PERIODS.filter(function(x){return x[0]===filt.period;})[0];
  if(!p||!p[2]) return true;
  var t=new Date(it.published_utc).getTime();
  if(isNaN(t)) return true;
  return (Date.now()-t) <= p[2]*86400000;
}
function match(it){
  if(filt.region!=="all" && it.region!==filt.region) return false;
  if(!inPeriod(it)) return false;
  if(filt.topic.length && !(it.topics||[]).some(function(t){return filt.topic.indexOf(t)>=0;})) return false;
  if(filt.q){
    var h=((it.title_en||"")+" "+(it.title_original||"")+" "+(it.source_name||"")).toLowerCase();
    if(h.indexOf(filt.q.toLowerCase())<0) return false;
  }
  return true;
}

function renderFlags(){
  var byRegion={}; items().forEach(function(i){ byRegion[i.region]=(byRegion[i.region]||0)+1; });
  var html='<span class="flag'+(filt.region==="all"?" on":"")+'" data-r="all">'+
    '<span class="em">🌏</span><span class="nm">Todos</span><span class="ct">'+items().length+'</span></span>';
  REGIONS.forEach(function(r){
    var n=byRegion[r.id]||0;
    html+='<span class="flag '+r.id+(filt.region===r.id?" on":"")+'" data-r="'+r.id+'">'+
      '<span class="em">'+r.flag+'</span><span class="nm">'+esc(r.label)+'</span>'+
      '<span class="ct">'+n+'</span></span>';
  });
  document.getElementById("flags").innerHTML=html;
}

function renderChips(){
  var pe=document.getElementById("fPeriod");
  pe.innerHTML='<span class="lb">Período</span>'+PERIODS.map(function(p){
    return '<span class="chip'+(filt.period===p[0]?" on":"")+'" data-p="'+p[0]+'">'+p[1]+"</span>"; }).join("");

  var counts={}; items().filter(function(i){return filt.region==="all"||i.region===filt.region;})
    .forEach(function(i){ (i.topics||[]).forEach(function(t){ counts[t]=(counts[t]||0)+1; }); });
  var te=document.getElementById("fTopic");
  te.innerHTML='<span class="lb">Tópico</span>'+TOPICS.map(function(t){
    var n=counts[t.id]||0;
    return '<span class="chip'+(filt.topic.indexOf(t.id)>=0?" on":"")+'" data-t="'+t.id+'">'+
      esc(t.label)+(n?' <span style="opacity:.55">'+n+"</span>":"")+"</span>"; }).join("");
}

function render(){
  renderFlags(); renderChips();

  /* generated_at_utc = última coleta que alcançou as fontes; collected_at_utc =
     última tentativa. Numa coleta sem rede as duas se separam, e é essa
     diferença que o painel precisa mostrar em vez de fingir que está fresco. */
  var gen=FEED.generated_at_utc;
  var tent=FEED.collected_at_utc||gen;
  document.getElementById("sub").innerHTML =
    "Japão · China · Taiwan · Coreia do Sul — última coleta <strong>"+esc(fmtFull(gen))+"</strong>";

  var rows=items().filter(match);
  var bad=(FEED.sources||[]).filter(function(s){return !s.ok;}).length;
  var horas=(Date.now()-new Date(gen).getTime())/3600000;
  var cls = horas>12 ? "err" : (horas>3?"warn":"");

  document.getElementById("status").innerHTML=
    '<span class="dot '+cls+'"></span><span>'+rows.length+" de "+items().length+" manchetes</span>"+
    "<span>·</span><span>coleta há "+esc(ago(gen))+"</span>"+
    (FEED.degraded?'<span>·</span><span style="color:var(--err)">tentativa de '+esc(ago(tent))+" atrás não alcançou as fontes</span>":"")+
    (bad?'<span>·</span><span style="color:var(--err)">'+bad+" fonte"+(bad>1?"s":"")+" com problema</span>":"");

  var avisos=[];
  if(FEED.degraded){
    avisos.push('<div class="note warn"><strong>A última tentativa de coleta não alcançou as fontes</strong> — '+
      (FEED.sources_ok||0)+" de "+(FEED.sources_total||0)+" responderam"+
      (tent?" (tentativa de "+esc(fmtFull(tent))+")":"")+
      ". Quase sempre é rede desta máquina: VPN, DNS ou Wi-Fi. "+
      "As manchetes abaixo são da última coleta boa, de "+esc(fmtFull(gen))+
      " — nada foi perdido, e a próxima coleta que funcionar volta a somar.</div>");
  }
  if(!canRunPanel()){
    avisos.push('<div class="note warn">Aberto como arquivo local: os botões só releem o que está em disco. '+
      "Para buscar na web, feche esta aba e dê duplo-clique em <strong>Abrir Monitor.command</strong>.</div>");
  }
  document.getElementById("banner").innerHTML = avisos.join("");

  var list=document.getElementById("list");
  if(!rows.length){
    if(!items().length){
      list.innerHTML='<div class="empty"><strong>Nenhuma coleta ainda.</strong><br><br>'+
        'Feche esta aba e dê duplo-clique em <strong>Abrir Monitor.command</strong>, '+
        'na pasta do projeto.<br>A primeira coleta leva de 1 a 3 minutos.</div>';
      return;
    }
    /* "Nada com esses filtros" sozinho não diz se o filtro está apertado ou se
       a coleta parou — e essas duas situações pedem ações opostas. Dizer a
       idade da manchete mais nova resolve a dúvida em uma linha. */
    var maisNova=null, tMax=-Infinity;
    items().forEach(function(i){
      var t=new Date(i.published_utc).getTime();
      if(!isNaN(t) && t>tMax){ tMax=t; maisNova=i.published_utc; }
    });
    list.innerHTML='<div class="empty"><strong>Nada dentro destes filtros.</strong><br><br>'+
      (maisNova?"A manchete mais recente do feed é de "+esc(ago(maisNova))+
                " atrás ("+esc(fmtFull(maisNova))+").<br>":"")+
      "O feed inteiro tem "+items().length+' manchetes.<br><br>'+
      '<button id="verTudo">Limpar filtros e ver tudo</button></div>';
    var vt=document.getElementById("verTudo");
    if(vt) vt.addEventListener("click",function(){
      filt.period="all"; filt.topic=[]; filt.q=""; filt.region="all";
      document.getElementById("q").value="";
      save(); render();
    });
    return;
  }

  list.innerHTML=rows.map(function(it){
    var r=it.region||"";
    var meta=REGIONS.filter(function(x){return x.id===r;})[0];
    var showOrig = it.translated && it.title_original && it.title_original!==it.title_en;
    return '<article class="card '+esc(r)+'"><div class="tags">'+
      (meta?'<span class="tag r-'+esc(r)+'">'+meta.flag+" "+esc(meta.label)+"</span>":"")+
      (it.topics||[]).map(function(t){
        var tl=TOPICS.filter(function(x){return x.id===t;})[0];
        return '<span class="tag">'+esc(tl?tl.label:t)+"</span>"; }).join("")+
      (it.live_wire?'<span class="tag b-live">ao vivo</span>':"")+
      (it.manual?'<span class="tag b-manual">curado</span>':"")+
      (it.translated?'<span class="tag b-tr">traduzido</span>':"")+
      '<span class="when" title="'+esc(fmtFull(it.published_utc))+'">'+esc(ago(it.published_utc))+"</span></div>"+
      '<h3><a href="'+esc(it.url)+'" target="_blank" rel="noopener">'+esc(it.title_en)+"</a></h3>"+
      (showOrig?'<p class="orig">'+esc(it.title_original)+"</p>":"")+
      '<div class="src">'+esc(it.source_name)+"</div></article>";
  }).join("");
}

function renderHealth(){
  var rows=FEED.sources||[];
  document.getElementById("healthlist").innerHTML = rows.length ? rows.map(function(s){
    return '<div class="hrow2'+(s.ok?"":" bad")+'">'+
      '<span class="dot '+(s.ok?"":"err")+'"></span>'+
      '<span class="nm">'+esc(s.name)+"</span>"+
      (s.ok?'<span class="ct">'+s.count+(s.newest?" · "+esc(ago(s.newest)):"")+"</span>"
           :'<span class="ct er">'+esc(s.error||"falhou")+"</span>")+
      "</div>"; }).join("") : '<div class="empty">Sem dados de coleta.</div>';
}

/* ---- interações ---- */
document.getElementById("flags").addEventListener("click",function(e){
  var f=e.target.closest(".flag"); if(!f) return;
  filt.region=f.dataset.r; save(); render();
});
document.getElementById("filters").addEventListener("click",function(e){
  var c=e.target.closest(".chip"); if(!c) return;
  if(c.dataset.p){ filt.period=c.dataset.p; }
  else if(c.dataset.t){
    var i=filt.topic.indexOf(c.dataset.t);
    if(i<0) filt.topic.push(c.dataset.t); else filt.topic.splice(i,1);
  }
  save(); render();
});
document.getElementById("q").addEventListener("input",function(e){ filt.q=e.target.value; save(); render(); });
document.getElementById("q").value=filt.q||"";

function tab(w){
  document.getElementById("tabFeed").classList.toggle("on",w==="feed");
  document.getElementById("tabHealth").classList.toggle("on",w==="health");
  document.getElementById("viewFeed").classList.toggle("hidden",w!=="feed");
  document.getElementById("viewHealth").classList.toggle("hidden",w!=="health");
  document.getElementById("filters").classList.toggle("hidden",w!=="feed");
  if(w==="health") renderHealth();
}
document.getElementById("tabFeed").addEventListener("click",function(){tab("feed");});
document.getElementById("tabHealth").addEventListener("click",function(){tab("health");});

function toast(msg,ms){
  var el=document.createElement("div"); el.className="toast"; el.textContent=msg;
  document.body.appendChild(el);
  setTimeout(function(){ el.remove(); }, ms||3200);
}

/* relê o feed.json do disco sem recarregar a página */
async function reloadFeed(){
  try{
    var r=await fetch("Cache/feed.json?t="+Date.now(),{cache:"no-store"});
    if(!r.ok) return false;
    var data=await r.json();
    if(data && data.items){ FEED=data; render(); return true; }
  }catch(e){}
  return false;
}

document.getElementById("btnRefresh").addEventListener("click",async function(){
  var b=this; if(b.disabled) return;
  b.disabled=true; b.innerHTML='<span class="spin"></span>Buscando…';
  if(!canRunPanel()){
    var ok=await reloadFeed();
    b.disabled=false; b.textContent="↻ Atualizar agora";
    toast(ok?"Feed relido do disco.":"Nada novo em disco. Suba o painel para buscar na web.");
    return;
  }
  if(modoWeb()){ await refreshWeb(b); return; }
  // A coleta leva cerca de 90s. Sem contador a pessoa acha que travou e
  // clica de novo, o que só rende um 409.
  var t0=Date.now();
  var tick=setInterval(function(){
    b.innerHTML='<span class="spin"></span>Buscando… '+Math.round((Date.now()-t0)/1000)+"s";
  },1000);
  try{
    var r=await fetch("/api/asia-news-refresh",{method:"POST",
      headers:{"Content-Type":"application/json"},body:"{}"});
    var d=await r.json();
    clearInterval(tick);
    if(d.ok && d.degraded){
      /* a coleta rodou mas não alcançou nada: dizer "✓ N no feed" aqui foi o
         que fez parecer que as notícias tinham sumido sem motivo */
      await reloadFeed();
      b.textContent="⚠ sem fontes";
      toast("A coleta não alcançou as fontes ("+(d.sources_ok||0)+" de "+
            (d.sources_total||0)+" responderam). O feed anterior foi mantido.",8000);
    }else if(d.ok){
      var antes=items().length;
      await reloadFeed();
      var novas=items().length-antes;
      b.textContent="✓ "+d.count+" no feed"+(novas>0?" (+"+novas+")":"");
      toast("Coleta concluída em "+Math.round((Date.now()-t0)/1000)+"s · "+d.count+" manchetes");
    }else if(r.status===409){
      b.textContent="Aguarde";
      toast("A coleta automática está rodando agora. Ela termina em ~90s e o feed atualiza sozinho.",7000);
      setTimeout(reloadFeed, 90000);
    }else{
      b.textContent="Falhou"; toast(d.error||"O fetcher retornou erro.",7000);
    }
  }catch(e){
    clearInterval(tick);
    b.textContent="Falhou"; toast("Painel não respondeu: "+e.message,7000);
  }
  setTimeout(function(){ b.disabled=false; b.textContent="↻ Atualizar agora"; },3000);
});

/* Painel web: dispara a coleta no GitHub Actions e relê o feed até ele mudar.
   O Actions leva de 1 a 3 min entre entrar na fila, coletar e commitar. */
async function refreshWeb(b){
  var antesCol=FEED.collected_at_utc||FEED.generated_at_utc, antesN=items().length, t0=Date.now();
  function fim(){ setTimeout(function(){ b.disabled=false; b.textContent="↻ Atualizar agora"; },4000); }
  var tick=setInterval(function(){
    b.innerHTML='<span class="spin"></span>Coletando… '+Math.round((Date.now()-t0)/1000)+"s";
  },1000);
  try{
    var r=await fetch("/api/asia-news-refresh",{method:"POST",
      headers:{"Content-Type":"application/json"},body:"{}"});
    var d=await r.json();
    if(!d.ok) throw new Error(d.error||"falhou");
    toast("Coleta pedida ao GitHub. Leva de 1 a 3 minutos — pode continuar lendo.",5000);
    while(Date.now()-t0 < 360000){
      await new Promise(function(ok){ setTimeout(ok,15000); });
      try{
        var rr=await fetch("Cache/feed.json?t="+Date.now(),{cache:"no-store"});
        if(!rr.ok) continue;
        var nd=await rr.json();
      }catch(e){ continue; }
      if(nd && nd.items && (nd.collected_at_utc||nd.generated_at_utc)!==antesCol){
        clearInterval(tick); FEED=nd; render();
        var seg=Math.round((Date.now()-t0)/1000), novas=items().length-antesN;
        if(nd.degraded){
          b.textContent="⚠ sem fontes";
          toast("A coleta não alcançou as fontes ("+(nd.sources_ok||0)+" de "+
                (nd.sources_total||0)+" responderam). O feed anterior foi mantido.",8000);
        }else{
          b.textContent="✓ "+items().length+" no feed"+(novas>0?" (+"+novas+")":"");
          toast("Coleta concluída em "+seg+"s · "+items().length+" manchetes");
        }
        fim(); return;
      }
    }
    clearInterval(tick); b.textContent="Ainda na fila";
    toast("O GitHub ainda não terminou. O painel se atualiza sozinho quando a coleta chegar.",7000);
  }catch(e){
    clearInterval(tick); b.textContent="Falhou";
    toast("Não consegui pedir a coleta: "+e.message,7000);
  }
  fim();
}

document.getElementById("btnManual").addEventListener("click",async function(){
  if(!canRunPanel()){ toast("Precisa do painel local em 127.0.0.1 para gerar o prompt.",4200); return; }
  var b=this; b.disabled=true; b.innerHTML='<span class="spin"></span>Montando…';
  try{
    var r=await fetch("/api/asia-news-manual-prompt",{method:"POST",
      headers:{"Content-Type":"application/json"},body:"{}"});
    var d=await r.json();
    if(d.ok) showPrompt(d.prompt); else toast(d.error||"Não consegui montar o prompt.",5000);
  }catch(e){ toast("Painel não respondeu: "+e.message,5000); }
  b.disabled=false; b.textContent="Curadoria IA";
});

/* Desligar: dois cliques. O primeiro arma, o segundo executa — matar o
   servidor sem querer, num clique só, seria irritante demais. */
var offArmado = null;
document.getElementById("btnOff").addEventListener("click",async function(){
  var b=this;
  if(!canRunPanel()){ toast("O monitor não está rodando por aqui.",3000); return; }
  if(!offArmado){
    b.classList.add("armado"); b.textContent="Confirmar?";
    offArmado=setTimeout(function(){
      offArmado=null; b.classList.remove("armado"); b.textContent="Desligar";
    },4000);
    return;
  }
  clearTimeout(offArmado); offArmado=null;
  b.disabled=true; b.textContent="Desligando…";
  try{ await fetch("/api/asia-news-shutdown",{method:"POST",
        headers:{"Content-Type":"application/json"},body:"{}"}); }catch(e){}
  document.body.innerHTML =
    '<div style="max-width:520px;margin:16vh auto;padding:26px;text-align:center;'+
    'font:15px/1.6 -apple-system,BlinkMacSystemFont,sans-serif;color:#14181f">'+
    '<div style="font-size:17px;font-weight:650;margin-bottom:10px">Monitor desligado</div>'+
    '<div style="color:#5b6472">A coleta automática parou. As notícias já coletadas '+
    'continuam no disco.<br><br>Para voltar, dê duplo-clique em '+
    '<strong>Abrir Monitor.command</strong> na pasta do projeto.</div></div>';
});

function showPrompt(text){
  var ov=document.createElement("div"); ov.className="overlay";
  ov.innerHTML='<div class="modal"><header><h2>Prompt de curadoria</h2>'+
    '<span style="margin-left:auto;font-size:12px;color:var(--tx3)">Cole num chat de IA com acesso à web</span></header>'+
    "<pre></pre>"+
    '<footer><button class="primary" id="pCopy">Copiar</button>'+
    '<button id="pClose">Fechar</button>'+
    '<span style="margin-left:auto;font-size:12px;color:var(--tx3)">Depois de gravar manual_additions.json, clique em Atualizar agora</span></footer></div>';
  ov.querySelector("pre").textContent=text;
  if(modoWeb()){
    ov.querySelector("footer span").textContent="Copie, rode num chat de IA com web e cole a resposta abaixo";
    var box=document.createElement("div");
    box.style.cssText="border-top:1px solid var(--line);padding:12px 18px;display:flex;flex-direction:column;gap:8px";
    box.innerHTML='<label for="pJson" style="font-size:12px;font-weight:600">Resultado da IA</label>'+
      '<textarea id="pJson" rows="6" placeholder="Cole aqui o bloco JSON que a IA devolveu" '+
      'style="width:100%;box-sizing:border-box;font:12px/1.5 ui-monospace,Menlo,monospace;padding:8px;'+
      'border:1px solid var(--line);border-radius:8px;resize:vertical"></textarea>'+
      '<div><button class="primary" id="pSend">Enviar resultado</button></div>';
    ov.querySelector(".modal").insertBefore(box, ov.querySelector(".modal footer"));
    box.querySelector("#pSend").addEventListener("click",async function(){
      var sb=this, txt=box.querySelector("#pJson").value.trim();
      if(!txt){ toast("Cole o JSON da IA primeiro."); return; }
      sb.disabled=true; sb.innerHTML='<span class="spin"></span>Enviando…';
      try{
        var r=await fetch("/api/asia-news-manual-save",{method:"POST",
          headers:{"Content-Type":"application/json"},body:JSON.stringify({texto:txt})});
        var d=await r.json();
        if(!d.ok) throw new Error(d.error||"falhou");
        ov.remove();
        toast(d.count+" manchete"+(d.count>1?"s":"")+" gravada"+(d.count>1?"s":"")+
              (d.discarded?" ("+d.discarded+" descartada"+(d.discarded>1?"s":"")+" por falta de campo)":"")+
              ". A coleta que funde tudo já foi pedida — aparece em 1 a 3 min.",8000);
        setTimeout(reloadFeed,120000); setTimeout(reloadFeed,240000);
      }catch(e){
        sb.disabled=false; sb.textContent="Enviar resultado";
        toast("Não gravei: "+e.message,8000);
      }
    });
  }
  document.body.appendChild(ov);
  ov.addEventListener("click",function(e){ if(e.target===ov) ov.remove(); });
  ov.querySelector("#pClose").addEventListener("click",function(){ ov.remove(); });
  ov.querySelector("#pCopy").addEventListener("click",function(){
    navigator.clipboard.writeText(text).then(
      function(){ toast("Prompt copiado."); },
      function(){ toast("Não consegui copiar — selecione o texto à mão."); });
  });
  if(navigator.clipboard) navigator.clipboard.writeText(text).catch(function(){});
}

/* auto-reload do feed a cada 5 min */
setInterval(reloadFeed, 300000);
document.addEventListener("keydown",function(e){
  if(e.key==="/" && document.activeElement.tagName!=="INPUT"){ e.preventDefault(); document.getElementById("q").focus(); }
});

if(modoWeb()){
  document.getElementById("btnOff").style.display="none";
  document.getElementById("btnRefresh").title="Pede uma coleta nova ao GitHub Actions (1 a 3 min)";
}
reloadFeed();   /* se estiver servido, pega a versão mais recente do disco */
render();
</script>
</body>
</html>
"""


def render(feed: dict, out_path: Path) -> Path:
    regions = [{"id": r, "label": cfg.REGION_LABEL[r], "flag": cfg.REGION_FLAG[r]}
               for r in cfg.REGIONS]
    topics = [{"id": t, "label": cfg.TOPIC_LABEL[t]} for t in cfg.TOPIC_ORDER]

    def dump(obj) -> str:
        return json.dumps(obj, ensure_ascii=False, separators=(",", ":")) \
                   .replace("</script", "<\\/script")

    html = (TEMPLATE
            .replace("__FEED__", dump(feed))
            .replace("__REGIONS__", dump(regions))
            .replace("__TOPICS__", dump(topics)))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_path.with_suffix(".tmp")
    tmp.write_text(html, "utf-8")
    tmp.replace(out_path)
    return out_path


def main() -> int:
    """`python3 render_html.py` regera o HTML a partir do Cache/feed.json.

    Existe para o server.py poder renderizar em subprocesso: importando o
    módulo, o template ficava congelado na versão carregada no boot e uma
    correção do painel vinda do GitHub só aparecia depois de reiniciar o
    monitor.
    """
    raiz = Path(__file__).resolve().parent.parent
    feed_path = raiz / "Cache" / "feed.json"
    try:
        feed = json.loads(feed_path.read_text("utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"! não consegui ler {feed_path.name}: {exc}")
        return 1
    saida = render(feed, raiz / "Monitor de Notícias Macro.html")
    print(f"→ {saida.name} regerado com {len(feed.get('items', []))} manchetes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
