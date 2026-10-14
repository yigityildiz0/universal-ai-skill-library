// Usage: node build.js deck.json [out.pptx]
// Reads the content JSON, assembles speaker notes in the agreed template, builds the PPTX with kit.js,
// prints warnings and a timing table. Exit code 2 when warnings exist (fix, then rebuild).
//
// Speaker-note template (one block per slide, empty parts are skipped):
//   [7/55]  Hedef ≈ 0:55 · Bitişte ≈ 6:10 / 38:48
//   <say: 2–5 short spoken sentences, presenter's own voice>
//   ÖZETLE: <technical slides: what we must understand from this slide>
//   ARAŞTIRMA — Yazar ve ark., yıl
//   • Neden burada: …   • Ne yapılmış, ne bulunmuş: …   • Nasıl yorumlanır: …
//   TERİMLER:
//   • ICC (ay-si-si): sınıf içi korelasyon katsayısı (intraclass correlation coefficient): …
//   → Geçiş: <bridge sentence>
'use strict';
const fs = require('fs');
const path = require('path');
const { createDeck } = require('./kit.js');

const src = process.argv[2] || 'deck.json';
const deck = JSON.parse(fs.readFileSync(src, 'utf8'));
const meta = deck.meta || {};
const out = process.argv[3] || meta.output || 'sunum.pptx';
const WPM = meta.wordsPerMinute || 112;        // calm Turkish read-aloud speed
const PAUSE = meta.pausePerSlide ?? 7;         // seconds for showing the visual / transition
const ABBR_MODE = meta.abbreviationMode || 'every'; // 'every' = (okunuş; açılım) at every mention; 'first' = full once per block, then (okunuş)
const SOFT = meta.noteWordsSoft || 120, HARD = meta.noteWordsHard || 160;
const FORBID = (meta.forbiddenOnSlides || ['bu akşam', 'bugün', 'iyi akşamlar', 'geçen hafta', 'haftaya', 'tartışalım', 'öğretim örneği', 'sorular?'])
  .map(x => x.toLowerCase());

// ---------------------------------------------------------------- abbreviations
const ABBR = deck.abbreviations || {};   // { "ICC": ["ay-si-si", "sınıf içi korelasyon katsayısı"] }
const NAMES = deck.names || {};          // { "Jamar": "ceymar" } — first mention in the deck gets (okunuş)
const esc = (s) => s.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&');
function expand(t, seenNames) {
  if (!t) return t;
  for (const [ab, [say, full]] of Object.entries(ABBR)) {
    const re = new RegExp(`(?<![\\p{L}\\d-])${esc(ab)}((?:['’][\\p{L}]+)?)(?![\\p{L}\\d])(?! \\()`, 'gu');
    let k = 0;
    t = t.replace(re, (m, suf) => ((ABBR_MODE === 'every' || k++ === 0) ? `${ab}${suf} (${say}; ${full})` : `${ab}${suf} (${say})`));
  }
  for (const [nm, say] of Object.entries(NAMES)) {
    if (seenNames.has(nm)) continue;
    const re = new RegExp(`(?<![\\p{L}])${esc(nm)}((?:['’][\\p{L}]+)?)(?![\\p{L}])`, 'u');
    if (re.test(t)) { t = t.replace(re, (m, suf) => `${nm}${suf} (${say})`); seenNames.add(nm); }
  }
  return t;
}
const words = (t) => (t || '').replace(/\([^)]*\)/g, ' ').split(/\s+/).filter(Boolean).length;
const fmt = (sec) => `${Math.floor(sec / 60)}:${String(Math.round(sec % 60)).padStart(2, '0')}`;
const round5 = (s) => Math.max(5, Math.round(s / 5) * 5);
const L = { summary: 'ÖZETLE', research: 'ARAŞTIRMA', why: 'Neden burada', what: 'Ne yapılmış, ne bulunmuş', how: 'Nasıl yorumlanır',
  terms: 'TERİMLER', transition: '→ Geçiş', question: 'OLASI SORU', ...(meta.noteLabels || {}) };

function termLine(t, seen) {
  if (typeof t === 'string') return '• ' + t;
  const ab = ABBR[t.term];
  const say = t.say || (ab ? ab[0] : null);
  const head = say ? `${t.term} (${say})` : t.term;
  const full = t.full || (ab ? ab[1] : '');
  return `• ${head}: ${[full, t.english ? `(${t.english})` : '', t.def ? `${full ? '— ' : ''}${expand(t.def, seen)}` : ''].filter(Boolean).join(' ')}`;
}

// returns { body, spokenWords, sec }
function noteBody(s, seen) {
  const n = s.notes;
  if (!n) return { body: '', spokenWords: 0, sec: s.layout === 'section' ? 10 : PAUSE };
  if (typeof n === 'string') { const w = words(n); return { body: expand(n, seen), spokenWords: w, sec: round5(w / WPM * 60 + PAUSE) }; }
  const parts = [];
  let spoken = words(n.say) + words(n.summary) + words(n.transition);
  let half = 0;
  if (n.say) parts.push(expand(n.say, seen));
  if (n.summary) parts.push(`${L.summary}: ${expand(n.summary, seen)}`);
  const rs = Array.isArray(n.research) ? n.research : (n.research ? [n.research] : []);
  rs.forEach(r => {
    if (typeof r === 'string') { parts.push(`${L.research}: ${expand(r, seen)}`); spoken += words(r); return; }
    const lines = [`${L.research} — ${r.cite || ''}`.trim()];
    if (r.why) { lines.push(`• ${L.why}: ${expand(r.why, seen)}`); half += words(r.why); }
    if (r.what) { lines.push(`• ${L.what}: ${expand(r.what, seen)}`); spoken += words(r.what); }
    if (r.interpret) { lines.push(`• ${L.how}: ${expand(r.interpret, seen)}`); spoken += words(r.interpret); }
    else if (r.what && /\d/.test(r.what)) warns.push(`slide ${s.__i}: research numbers without "interpret" — add threshold + meaning (e.g. ICC > 0,90 mükemmel)`);
    parts.push(lines.join('\n'));
  });
  if (n.terms && n.terms.length) parts.push(`${L.terms}:\n` + n.terms.map(t => termLine(t, seen)).join('\n'));
  if (n.question) parts.push(`${L.question}: ${expand(n.question, seen)}`);
  if (n.transition) parts.push(`${L.transition}: ${expand(n.transition, seen)}`);
  const sw = spoken + 0.5 * half;
  return { body: parts.join('\n\n'), spokenWords: Math.round(sw), sec: round5(sw / WPM * 60 + PAUSE) };
}

const warns = [];
(async () => {
  const kit = createDeck({ ...meta, baseDir: path.dirname(path.resolve(src)) });
  const seen = new Set();
  const N = deck.slides.length;
  // pass 1: note bodies and timing
  const bodies = deck.slides.map((s, i) => {
    s.__i = i + 1;
    if (s.layout === 'references') return { body: '', spokenWords: 0, sec: 5 };
    return noteBody(s, seen);
  });
  const total = bodies.reduce((a, b) => a + b.sec, 0);
  let acc = 0;
  const timing = [];
  deck.slides.forEach((s, i) => {
    const b = bodies[i];
    acc += b.sec;
    const header = meta.noteHeader === false ? '' : `[${i + 1}/${N}]  Hedef ≈ ${fmt(b.sec)} · Bitişte ≈ ${fmt(acc)} / ${fmt(total)}`;
    const notes = [header, b.body].filter(Boolean).join('\n\n');
    timing.push([i + 1, s.layout, (s.title || '').slice(0, 46), fmt(b.sec), b.spokenWords]);
    if (b.spokenWords > HARD) warns.push(`slide ${i + 1}: notes ${b.spokenWords} spoken words > ${HARD} — too long to read live; cut or split`);
    else if (b.spokenWords > SOFT) warns.push(`slide ${i + 1}: notes ${b.spokenWords} spoken words > ${SOFT} (soft limit)`);
    const content = !['cover', 'section', 'references', 'closing', 'agenda'].includes(s.layout);
    if (content && !s.source && !s.noSource && meta.sourceEverySlide !== false) {
      warns.push(`slide ${i + 1}: content slide without source line (set "source", or "noSource": "<reason>")`);
    }
    if (!s.notes && s.layout !== 'references') warns.push(`slide ${i + 1}: no speaker notes`);
    const onSlide = JSON.stringify({ ...s, notes: undefined }).toLowerCase();
    FORBID.forEach(f => { if (onSlide.includes(f)) warns.push(`slide ${i + 1}: forbidden on-slide phrase "${f}"`); });
    delete s.__i;
    kit.addSlide({ ...s, notes });
  });
  const res = await kit.save(out);
  const all = [...res.warnings, ...warns];
  console.log(`Saved ${res.file} — ${res.slides} slides, estimated talk ${fmt(total)} (${WPM} wpm + ${PAUSE}s/slide)`);
  const target = meta.targetMinutes;
  if (target && (total / 60 < target[0] || total / 60 > target[1])) {
    all.push(`timing ${fmt(total)} outside target ${target[0]}–${target[1]} min — adjust notes or slide count, never shrink type`);
  }
  console.log('\n #  layout       title                                          time  words');
  timing.forEach(r => console.log(`${String(r[0]).padStart(2)}  ${r[1].padEnd(12)} ${r[2].padEnd(46)} ${r[3].padStart(5)} ${String(r[4]).padStart(5)}`));
  if (all.length) {
    console.log(`\n${all.length} warning(s):`);
    all.forEach(w => console.log(' - ' + w));
    process.exitCode = 2;
  } else console.log('\nNo build warnings. Next: render + visual QA + pptx_audit.py');
})().catch(e => { console.error(e.stack || e.message); process.exit(1); });
