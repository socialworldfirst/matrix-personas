#!/usr/bin/env python3
"""Matrix-accounts persona deck. AES-GCM gated (wf), single-file. Run: python3 build.py"""
import os, json, base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes

PASSWORD = "wf"
ITER = 100_000

def encrypt_payload(plaintext: str, password: str = PASSWORD) -> dict:
    salt = os.urandom(16); iv = os.urandom(12)
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(password.encode())
    ct = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    b64 = lambda b: base64.b64encode(b).decode()
    return {"salt": b64(salt), "iv": b64(iv), "ct": b64(ct), "iter": ITER}

DECK = {
  "title": "Matrix accounts: 3 personas per region",
  "intro": "You set the premise: a clear account positioning before anyone posts. Here is one to react to. The core idea, the 3 accounts in each region are not 3 lookalikes. They are the 3 layers of our live KOL funnel (reach, bridge, convert) turned into owned accounts, so they plug straight into the plan we already deployed. Tick the personas, regions and calls that work, note any change on the card, paste the prompt back. We line this up against the team's own ideas next.",
  "stamp": "30 Jun 2026 · build now: UK · Singapore · Thailand · Malaysia   ·   warm only: US · Hong Kong",
  "promptHeader": "WF matrix accounts · persona + positioning picks",
  "promptAction": "Turn these into (1) a one-page account-positioning brief per build-now region for the team + Jelly, and (2) draft 人设 bios + 5 sample post hooks for each chosen account in UK / SG / TH / MY.",
  "globalNote": {
    "label": "Anything to fold in (the team's ideas, account names/handles, other regions, platform calls)",
    "placeholder": "e.g. swap the Insider for the Operator in MY · handle ideas · which platform leads in SG · what the team proposed..."
  },
  "sections": [
    {
      "key": "personas", "label": "The 3 personas (人设)",
      "sub": "Suggested set is the funnel trio (Scout / Guide / Insider). Pick the three you want per region, swap in an alt for any slot. Note name or voice tweaks on the card.",
      "pick": 3, "notes": True,
      "items": [
        {"name": "情报员 · The Scout", "tag": "Layer 1 · reach", "rec": True,
         "desc": "<b>Top of funnel.</b> The plugged-in peer who surfaces what every cross-border seller wants to know first: FX swings, fresh 1688 / 工厂 finds, policy and platform changes, 避坑 warnings. High volume, trend-led, built for saves and follows, soft sell or none. Its one job is to pull cold viewers in and hand them down the funnel. Voice: fast, generous, \"刚发现… / 别踩这个坑\". <b>Score on:</b> reach, saves, follows, lift in branded search."},
        {"name": "老带新 · The Guide", "tag": "Layer 2 · bridge", "rec": True,
         "desc": "<b>The answer that owns the RedNote search grid.</b> When the Scout or a big KOL makes someone curious and they search \"美国电商第一步怎么开\" or \"收款工具怎么选\", our answer is sitting right there. Comparisons, how-to-open, \"适不适合你\". This is the floor the KOL plan says is missing today. Calm, structured, been-there. Medium nudge. <b>Score on:</b> profile visits, comment depth, search ranking, intent to ask."},
        {"name": "内部人 · The Insider", "tag": "Layer 3 · convert", "rec": True,
         "desc": "<b>Access, not advice</b> (the James-US model). A real WF-side person who can actually open doors: 对接, real cases, setup walkthroughs, the inside line. WF / Ant credibility visible = the trust anchor. Converts via public proof + profile for now (private-message funnel parked per your call), switches to group / 1:1 when you green-light it. <b>Score on:</b> profile-to-product, qualified interest."},
        {"name": "避坑情报站 · The Watchdog", "tag": "alt · risk niche",
         "desc": "A sharper, risk-only cut of the Scout: 冻结, 风控, 税务, 政策红线. Turns \"a payments brand has to earn trust\" into the content itself, very high save-and-share, very credible. Could replace or sit beside the Scout where the audience is anxious about getting money in and out safely."},
        {"name": "操盘手 · The Operator", "tag": "alt · trust face",
         "desc": "A named real face (a WF BD, or a partnered seller) running a founder-style account: \"我在帮卖家做的事\". Maximum trust and personality, harder to copy-paste across regions. Can BE the Insider or stand on its own. A strong answer to the \"matrix feels fake\" risk."},
        {"name": "社群主理人 · The Host", "tag": "alt · community (parked)",
         "desc": "A community host whose whole job is the private domain: runs the group, hosts Q&As, lives in the comments. The real convert engine once DM + group are switched on. Parked for now since you've deferred private-message conversion, the natural partner to the Insider when it goes live."}
      ]
    },
    {
      "key": "regions", "label": "Per-region build",
      "sub": "Which regions get accounts now. The four build-now markets are pre-ticked. Note language lead, platform or any local call on the card.",
      "pick": 4, "notes": True,
      "items": [
        {"name": "United Kingdom", "tag": "build now", "rec": True,
         "desc": "Chinese-diaspora operators (创业 / 跨境 / 财税). RED as the core, IG optional. Mostly Chinese, a little English. Build + warm this week, post from next week."},
        {"name": "Singapore", "tag": "build now · WhatsApp live", "rec": True,
         "desc": "Chinese + English split. RED / TikTok. The one market where WhatsApp can run ad-hoc, so the Insider has a real lower-funnel home here. Build + warm this week."},
        {"name": "Thailand", "tag": "build now", "rec": True,
         "desc": "~60% native Thai, so one clean channel beats three: Thai-language Facebook is the obvious lead, Chinese secondary. Keep convert claims to what the product does here today. Build + warm this week."},
        {"name": "Malaysia", "tag": "build now · trust-careful", "rec": True,
         "desc": "Three audiences in parallel (Chinese / Malay / English). RED for the Chinese community + TikTok (70/30 Malay/Chinese). Trust-careful: lean on KOC seeding alongside the owned accounts, keep claims accurate to what's live in MY today. Build + warm this week."},
        {"name": "United States", "tag": "warm only",
         "desc": "Chinese operators, RED via Jelly / 逐帧 (聚光 + 蒲公英). Warm the accounts now, no posting yet."},
        {"name": "Hong Kong", "tag": "warm only",
         "desc": "Cantonese / Chinese. Warm now, no posting yet."}
      ]
    },
    {
      "key": "calls", "label": "Positioning calls to lock",
      "sub": "The premise behind it all, and the answers to bring back to the team + Jelly. Tick the stances you're locking, note any you'd phrase differently.",
      "pick": 6, "notes": True,
      "items": [
        {"name": "3 accounts = 3 funnel layers, not 3 lookalikes", "rec": True,
         "desc": "Each account has one job (reach / bridge / convert) and plugs into the live KOL full-funnel plan. This is what stops \"matrix\" turning into a wall of samey sub-accounts."},
        {"name": "Every account is a person, not a sub-brand", "rec": True,
         "desc": "A real voice and face plus visible WF / Ant credibility. For a payments brand, trust is the whole game, faceless matrix accounts work against it."},
        {"name": "Private-message conversion off for now", "rec": True,
         "desc": "Accounts still play their funnel role and convert through public proof + profile. Switch DM / group on later, market by market (Singapore first, since WhatsApp is live there)."},
        {"name": "Content stays accurate to each market's product", "rec": True,
         "desc": "Only say what the product actually does in that country today. Social position sits downstream of the product, no claims it can't back."},
        {"name": "Team plans cadence + content, we own positioning", "rec": True,
         "desc": "Jelly / 逐帧 propose frequency and ideas. This positioning is the brief they work inside, not the other way round. Posting isn't urgent, so there's time to get it right."},
        {"name": "Warm all six regions, post from four", "rec": True,
         "desc": "UK / SG / TH / MY build, warm and post from next week. US + HK warm only for now."}
      ]
    }
  ]
}

CIPHER = encrypt_payload(json.dumps(DECK, ensure_ascii=False))

HTML = r"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Matrix accounts · personas</title>
<style>
  :root{--ink:#16181d;--ink2:#3c4148;--mut:#71777f;--faint:#9aa0a6;--line:#e7e7e4;--bg:#fbfbf9;--card:#fff;--ok:#3f7d58;--accent:#16181d;--rec:#b07a2b;}
  *{box-sizing:border-box;margin:0;padding:0}
  body{font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);padding-bottom:120px;-webkit-font-smoothing:antialiased}
  .wrap{max-width:880px;margin:0 auto;padding:48px 24px 0}
  h1{font-size:27px;letter-spacing:-.02em;font-weight:650;margin-bottom:8px}
  .lede{color:var(--ink2);font-size:15.5px;max-width:66ch;margin-bottom:6px}
  .stamp{color:var(--faint);font-size:12.5px;margin-bottom:8px}
  h2{font-size:13px;text-transform:uppercase;letter-spacing:.08em;color:var(--mut);font-weight:650;margin:40px 0 4px;display:flex;align-items:baseline;gap:10px}
  .ct{font-size:12px;color:var(--faint);letter-spacing:.02em;text-transform:none;font-weight:500}
  .ct.full{color:var(--ok)}
  .sub{color:var(--mut);font-size:13.5px;margin-bottom:16px;max-width:66ch}
  .card{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:15px 17px;margin-bottom:11px;cursor:pointer;transition:border-color .12s,box-shadow .12s;position:relative}
  .card:hover{border-color:#cfd2cc}
  .card.sel{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent)}
  .row{display:flex;gap:13px;align-items:flex-start}
  .tick{flex:none;width:22px;height:22px;border-radius:6px;border:1.5px solid #c4c4bf;margin-top:2px;display:flex;align-items:center;justify-content:center;transition:.12s}
  .tick svg{width:12px;height:12px;opacity:0;transition:.12s}
  .card.sel .tick{background:var(--accent);border-color:var(--accent)}
  .card.sel .tick svg{opacity:1}
  .body{flex:1;min-width:0}
  .name{font-weight:600;font-size:15px;letter-spacing:-.01em}
  .name .rec{font-size:11px;color:var(--rec);font-weight:650;margin-left:8px}
  .name .tag{font-size:11px;color:var(--ok);font-weight:650;margin-left:8px}
  .desc{font-size:13.5px;color:var(--ink2);line-height:1.55;margin-top:3px}
  .desc b{color:var(--ink);font-weight:600}
  .note{margin-top:11px;display:none}
  .card.sel .note{display:block}
  .note label{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--faint);font-weight:600;display:block;margin-bottom:5px}
  .note textarea{width:100%;border:1px solid var(--line);border-radius:8px;padding:8px 10px;font:13px/1.45 inherit;resize:vertical;min-height:34px;color:var(--ink);background:#fcfcfa}
  .note textarea:focus{outline:none;border-color:var(--mut)}
  .global{margin-top:24px}
  .global label{font-size:13px;color:var(--mut);font-weight:600;display:block;margin-bottom:7px}
  .global textarea{width:100%;border:1px solid var(--line);border-radius:10px;padding:11px 13px;font:14px/1.5 inherit;resize:vertical;min-height:60px;background:var(--card)}
  .global textarea:focus{outline:none;border-color:var(--mut)}
  .foot{max-width:880px;margin:30px auto 0;padding:0 24px;color:var(--faint);font-size:12px}
  .foot a{color:var(--faint);text-decoration:underline;cursor:pointer}
  .bar{position:fixed;left:0;right:0;bottom:0;background:rgba(251,251,249,.92);backdrop-filter:blur(10px);border-top:1px solid var(--line);padding:14px 24px}
  .bar-in{max-width:880px;margin:0 auto;display:flex;align-items:center;gap:16px;justify-content:space-between}
  .status{font-size:13px;color:var(--mut)} .status b{color:var(--ink)}
  .btn{border:0;background:var(--ink);color:#fff;font:600 14px/1 inherit;padding:13px 22px;border-radius:10px;cursor:pointer;transition:.12s;white-space:nowrap}
  .btn:disabled{background:#c8cdc6;cursor:not-allowed}
  .btn.done{background:var(--ok)}
  /* gate */
  #gate{position:fixed;inset:0;background:var(--bg);display:flex;align-items:center;justify-content:center;z-index:50}
  .gbox{width:300px;max-width:88vw;text-align:center}
  .gbox h3{font-size:15px;font-weight:600;margin-bottom:4px}
  .gbox p{font-size:12.5px;color:var(--mut);margin-bottom:16px}
  .gbox input{width:100%;border:1px solid var(--line);border-radius:9px;padding:11px 13px;font:15px inherit;text-align:center;background:var(--card)}
  .gbox input:focus{outline:none;border-color:var(--accent)}
  .gbox button{width:100%;margin-top:9px;border:0;background:var(--ink);color:#fff;font:600 14px inherit;padding:11px;border-radius:9px;cursor:pointer}
  .gerr{color:#b0392b;font-size:12px;margin-top:9px;min-height:15px}
  @media(max-width:620px){.wrap{padding:32px 16px 0}.bar-in{flex-direction:column;align-items:stretch;gap:10px}.btn{width:100%}.foot{padding:0 16px}}
</style>
</head>
<body>
<div id="gate"><div class="gbox">
  <h3>Internal</h3><p>Enter the team password</p>
  <input id="pw" type="password" autocomplete="off" autofocus>
  <button id="go">Unlock</button>
  <div class="gerr" id="gerr"></div>
</div></div>

<div class="wrap" id="app" style="display:none">
  <h1 id="title"></h1>
  <p class="lede" id="intro"></p>
  <p class="stamp" id="stamp"></p>
  <div id="sections"></div>
  <div class="global" id="globalWrap" style="display:none">
    <label id="gnoteLabel"></label>
    <textarea id="gnote"></textarea>
  </div>
</div>
<div class="foot" id="foot" style="display:none">Internal positioning draft, not final. <a id="lock">lock device</a></div>
<div class="bar" id="barWrap" style="display:none"><div class="bar-in">
  <div class="status" id="status"></div>
  <button class="btn" id="copy" disabled>Copy prompt</button>
</div></div>

<script>
const CIPHER = __CIPHER_JSON__;
const KEYNAME = 'wf_matrix_pw';
const b64 = s => Uint8Array.from(atob(s), c=>c.charCodeAt(0));
async function deriveKey(pw, salt){
  const km = await crypto.subtle.importKey('raw', new TextEncoder().encode(pw), 'PBKDF2', false, ['deriveKey']);
  return crypto.subtle.deriveKey({name:'PBKDF2', salt, iterations:CIPHER.iter||100000, hash:'SHA-256'}, km, {name:'AES-GCM', length:256}, false, ['decrypt']);
}
async function tryUnlock(pw){
  const key = await deriveKey(pw, b64(CIPHER.salt));
  const pt = await crypto.subtle.decrypt({name:'AES-GCM', iv:b64(CIPHER.iv)}, key, b64(CIPHER.ct));
  return JSON.parse(new TextDecoder().decode(pt));
}
async function unlock(pw){
  try{
    const DECK = await tryUnlock(pw);
    localStorage.setItem(KEYNAME, pw);
    document.getElementById('gate').style.display='none';
    document.getElementById('app').style.display='block';
    document.getElementById('foot').style.display='block';
    document.getElementById('barWrap').style.display='block';
    boot(DECK);
    return true;
  }catch(e){ return false; }
}
document.getElementById('go').addEventListener('click', async ()=>{
  const ok = await unlock(document.getElementById('pw').value.trim());
  if(!ok) document.getElementById('gerr').textContent = 'Wrong password';
});
document.getElementById('pw').addEventListener('keydown', e=>{ if(e.key==='Enter') document.getElementById('go').click(); });
document.getElementById('lock').addEventListener('click', ()=>{ localStorage.removeItem(KEYNAME); location.reload(); });
(async ()=>{ const saved = localStorage.getItem(KEYNAME); if(saved){ await unlock(saved); } })();

const CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>';
function boot(DECK){
  const state={}, notes={};
  DECK.sections.forEach(s=>{ state[s.key]= new Set(); notes[s.key]={}; });
  document.getElementById('title').textContent=DECK.title||'Deck';
  document.getElementById('intro').textContent=DECK.intro||'';
  document.getElementById('stamp').textContent=DECK.stamp||'';
  if(DECK.globalNote){ document.getElementById('globalWrap').style.display='block';
    document.getElementById('gnoteLabel').textContent=DECK.globalNote.label||'Notes';
    document.getElementById('gnote').placeholder=DECK.globalNote.placeholder||''; }
  const root=document.getElementById('sections');
  DECK.sections.forEach(s=>{
    const h=document.createElement('h2'); h.innerHTML=`${s.label} <span class="ct" id="ct-${s.key}"></span>`; root.appendChild(h);
    if(s.sub){ const p=document.createElement('p'); p.className='sub'; p.textContent=s.sub; root.appendChild(p); }
    const box=document.createElement('div'); box.id='sec-'+s.key; root.appendChild(box);
    s.items.forEach((o,i)=> box.appendChild(card(s,i,o)));
  });
  function card(s,i,o){
    const el=document.createElement('div'); el.className='card'; el.dataset.k=s.key; el.dataset.i=i;
    const rec=o.rec?'<span class="rec">★ rec</span>':'';
    const tag=o.tag?`<span class="tag">${o.tag}</span>`:'';
    const note=s.notes?`<div class="note"><label>your note (optional)</label><textarea placeholder="note on this pick..."></textarea></div>`:'';
    el.innerHTML=`<div class="row"><div class="tick">${CHECK}</div><div class="body"><div class="name">${o.name}${rec}${tag}</div><div class="desc">${o.desc||''}</div>${note}</div></div>`;
    el.addEventListener('click',e=>{ if(e.target.tagName==='TEXTAREA')return; toggle(s,i,el); });
    const ta=el.querySelector('textarea'); if(ta){ ta.addEventListener('click',e=>e.stopPropagation()); ta.addEventListener('input',e=>{ notes[s.key][i]=e.target.value; }); }
    return el;
  }
  function toggle(s,i,el){ const set=state[s.key]; if(set.has(i)){ set.delete(i); el.classList.remove('sel'); } else { set.add(i); el.classList.add('sel'); } update(); }
  function selCount(s){ return state[s.key].size; }
  function totalCount(){ return DECK.sections.reduce((t,s)=>t+selCount(s),0); }
  function update(){
    DECK.sections.forEach(s=>{ const c=document.getElementById('ct-'+s.key); c.textContent=`suggest ${s.pick} · ${selCount(s)} selected`; c.className='ct'+(selCount(s)>0?' full':''); });
    const total=totalCount(); const btn=document.getElementById('copy'); btn.disabled=total===0; btn.classList.remove('done'); btn.textContent='Copy prompt';
    document.getElementById('status').innerHTML = total===0
      ? 'Select anything. No limits, the prompt carries whatever you pick.'
      : `<b>${total}</b> pick${total===1?'':'s'} in the prompt. Suggested counts are guidance only.`;
  }
  function buildPrompt(){
    let L=['== '+(DECK.promptHeader||'deck')+' =='];
    DECK.sections.forEach(s=>{
      if(selCount(s)===0) return;
      L.push(`${s.label} (${selCount(s)} picked, ${s.pick} suggested):`);
      [...state[s.key]].forEach((i,n)=>{ const o=s.items[i]; const nt=notes[s.key][i]?` [note: ${notes[s.key][i].trim()}]`:''; L.push(`  ${n+1}. ${o.name}${nt}`); });
    });
    const g=DECK.globalNote? document.getElementById('gnote').value.trim():'';
    if(g) L.push('NOTES: '+g);
    L.push('> Counts are my call, work with exactly what I ticked.');
    if(DECK.promptAction) L.push('> '+DECK.promptAction);
    return L.join('\n');
  }
  document.getElementById('copy').addEventListener('click',async()=>{
    const txt=buildPrompt();
    try{ await navigator.clipboard.writeText(txt); }catch(e){ const ta=document.createElement('textarea'); ta.value=txt; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); }
    const b=document.getElementById('copy'); b.classList.add('done'); b.textContent='Copied · paste it to Claude'; setTimeout(()=>{ if(!b.disabled){b.classList.remove('done'); b.textContent='Copy prompt';} },2600);
  });
  update();
}
</script>
</body>
</html>
"""

out = HTML.replace("__CIPHER_JSON__", json.dumps(CIPHER))
with open(os.path.join(os.path.dirname(__file__), "index.html"), "w") as f:
    f.write(out)
print("wrote index.html ·", len(out), "bytes · gated wf")
