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

/* o painel local é o único que consegue rodar o fetcher */
function canRunPanel(){
  return location.protocol==="http:" &&
    (location.hostname==="127.0.0.1"||location.hostname==="localhost");
}

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

  var gen=FEED.generated_at_utc;
  document.getElementById("sub").innerHTML =
    "Japão · China · Taiwan · Coreia do Sul — última coleta <strong>"+esc(fmtFull(gen))+"</strong>";

  var rows=items().filter(match);
  var bad=(FEED.sources||[]).filter(function(s){return !s.ok;}).length;
  var horas=(Date.now()-new Date(gen).getTime())/3600000;
  var cls = horas>12 ? "err" : (horas>3?"warn":"");

  document.getElementById("status").innerHTML=
    '<span class="dot '+cls+'"></span><span>'+rows.length+" de "+items().length+" manchetes</span>"+
    "<span>·</span><span>coleta há "+esc(ago(gen))+"</span>"+
    (bad?'<span>·</span><span style="color:var(--err)">'+bad+" fonte"+(bad>1?"s":"")+" com problema</span>":"");

  document.getElementById("banner").innerHTML = canRunPanel() ? "" :
    '<div class="note warn">Aberto como arquivo local: os botões só releem o que está em disco. '+
    "Para buscar na web, feche esta aba e dê duplo-clique em <strong>Abrir Monitor.command</strong>.</div>";

  var list=document.getElementById("list");
  if(!rows.length){
    list.innerHTML = items().length
      ? '<div class="empty">Nada com esses filtros. Tente ampliar o período.</div>'
      : '<div class="empty"><strong>Nenhuma coleta ainda.</strong><br><br>'+
        'Feche esta aba e dê duplo-clique em <strong>Abrir Monitor.command</strong>, '+
        'na pasta do projeto.<br>A primeira coleta leva de 1 a 3 minutos.</div>';
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
    if(d.ok){
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
