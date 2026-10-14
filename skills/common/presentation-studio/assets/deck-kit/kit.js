// presentation-studio deck kit — editable PPTX from a content JSON (pptxgenjs 4.x)
// The model writes deck.json (content + layout per slide); this kit owns design,
// type sizes, safe fonts, source lines, slide numbers and speaker-note assembly.
'use strict';
const fs = require('fs');
const path = require('path');

let pptxgen;
try { pptxgen = require('pptxgenjs'); } catch (e) {
  throw new Error('pptxgenjs is missing. Run: npm install pptxgenjs@4  (in the build folder)');
}
let imageSize = null;
try { imageSize = require('image-size'); imageSize = imageSize.imageSize || imageSize.default || imageSize; } catch (e) { imageSize = null; }

// ---------------------------------------------------------------- themes
// Fonts: only families that ship with Windows + macOS Office and have metric-compatible
// substitutes in LibreOffice (Carlito/Liberation) and exist in Google Slides.
// Default Calibri (one family for titles and body); fallback Arial.
const SAFE_FONTS = ['Arial', 'Calibri', 'Cambria', 'Times New Roman', 'Georgia', 'Verdana', 'Tahoma'];
const THEMES = {
  klinik:   { dark: '15303D', ink: '1E2A33', muted: '5A6B76', light: 'F3F6F8', card: 'E8EEF2', accent: '0E7C86', accent2: 'D2553F', accent3: 'E9A23B', white: 'FFFFFF' },
  akademik: { dark: '1B2430', ink: '1F2733', muted: '5B6676', light: 'F4F5F8', card: 'E9ECF2', accent: 'B0303F', accent2: '0F6E8C', accent3: 'E0A43A', white: 'FFFFFF' },
  sade:     { dark: '22262E', ink: '23272F', muted: '626A75', light: 'F5F6F7', card: 'ECEEF1', accent: '2F5DA8', accent2: 'C2453A', accent3: 'D99A2B', white: 'FFFFFF' },
  doga:     { dark: '1F3326', ink: '1F2A22', muted: '5C6B60', light: 'F4F6F2', card: 'E7ECE4', accent: '3C7A4A', accent2: 'B8573A', accent3: 'D6A33A', white: 'FFFFFF' },
};

// Type roles (pt). minBody is the floor for every role not listed in `exceptions`.
const DEFAULT_TYPE = {
  minBody: 36,
  title: 40, body: 36, stat: 80, statLabel: 36, section: 54, sectionNum: 110, coverTitle: 54, coverSub: 36,
  // Exceptions below the floor. 'kicker' (small section label) is OFF by default: enable only after the user agrees.
  exceptions: { source: 16, references: 16, slideNumber: 14, credit: 14 },
};

const W = 13.333, H = 7.5, MX = 0.6;
const GRID = { titleY: 0.42, titleH: 1.25, bodyY: 1.85, bodyB: 6.75, sourceY: 6.95, sourceH: 0.38 };

// ---------------------------------------------------------------- helpers
const NBSP = ' ';
function noBreak(t) {
  // keep number+unit and operator+number together
  return String(t)
    .replace(/(\d) (?=(%|N·m\/kg|N·m|Nm|N|kg|kgf|g|ms|sn|s|dk|min|m|cm|mm|°|yaş|kişi|hasta|hafta|gün|Hz|dB|mmHg|bpm)(?![\p{L}]))/gu, '$1' + NBSP)
    .replace(/([≥≤≈<>=±→×÷]) (?=[\d%−\-~])/g, '$1' + NBSP)
    .replace(/(\b[A-ZÇĞİÖŞÜ]{1,6}) (?=[=≥≤≈<>])/g, '$1' + NBSP);
}
// **bold**, ^{sup}, _{sub}, \n line breaks
function runs(str, base) {
  const out = [];
  const lines = noBreak(str).split('\n');
  lines.forEach((ln, li) => {
    const seg = [];
    ln.split(/(\*\*[^*]+\*\*|\^\{[^}]+\}|_\{[^}]+\})/).forEach(p => {
      if (!p) return;
      if (p.startsWith('**')) seg.push({ text: p.slice(2, -2), options: { ...base, bold: true } });
      else if (p.startsWith('^{')) seg.push({ text: p.slice(2, -1), options: { ...base, superscript: true } });
      else if (p.startsWith('_{')) seg.push({ text: p.slice(2, -1), options: { ...base, subscript: true } });
      else seg.push({ text: p, options: { ...base } });
    });
    if (!seg.length) seg.push({ text: '', options: { ...base } });
    if (li < lines.length - 1) seg[seg.length - 1].options.breakLine = true;
    out.push(...seg);
  });
  return out;
}
const plain = (s) => String(s || '').replace(/\*\*|\^\{|_\{|\}/g, '');

// average glyph width (em) per family, used for fit estimates
const FONT_EM = { Calibri: 0.46, Arial: 0.5, Verdana: 0.56, Tahoma: 0.5, Cambria: 0.5, Georgia: 0.52, 'Times New Roman': 0.45 };
let CUR_FONT = 'Calibri';
// Rough fit estimate: average glyph ≈ 0.52 em, line ≈ 1.2 em.
function estimateLines(text, fs, wIn) {
  const perLine = Math.max(1, Math.floor(wIn / (fs * (FONT_EM[CUR_FONT] || 0.5) / 72)));
  return plain(text).split('\n').reduce((n, ln) => n + Math.max(1, Math.ceil(ln.length / perLine)), 0);
}
function blockH(text, fs, wIn, spacing = 1.2) { return estimateLines(text, fs, wIn) * fs * spacing / 72; }
function fits(text, fs, wIn, hIn, spacing = 1.2) {
  return estimateLines(text, fs, wIn) * fs * spacing / 72 <= hIn + 0.02;
}

// ---------------------------------------------------------------- deck
function createDeck(cfg = {}) {
  const theme = { ...(THEMES[cfg.theme] || THEMES.klinik), ...(cfg.colors || {}) };
  const type = { ...DEFAULT_TYPE, ...(cfg.type || {}), exceptions: { ...DEFAULT_TYPE.exceptions, ...((cfg.type || {}).exceptions || {}) } };
  const font = cfg.font || 'Calibri';
  const headFont = cfg.headFont || font;
  CUR_FONT = font;
  if (!SAFE_FONTS.includes(font) || !SAFE_FONTS.includes(headFont)) {
    console.warn(`[kit] font "${font}/${headFont}" is outside the safe list ${SAFE_FONTS.join(', ')} — ask the user before shipping.`);
  }
  const baseDir = cfg.baseDir || process.cwd();
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE';
  pres.author = cfg.author || '';
  pres.title = cfg.title || '';
  pres.theme = { headFontFace: headFont, bodyFontFace: font };
  const warnings = [];
  let n = 0;
  const layoutLog = [];

  const floor = (role, fs) => {
    if (type.exceptions[role] != null) return fs ?? type.exceptions[role];
    return Math.max(fs ?? type.body, type.minBody);
  };
  function text(slide, str, o) {
    const role = o.role || 'body';
    const fs = floor(role, o.fs);
    if (o.h && o.w && !fits(str, fs, o.w, o.h, o.spacing || 1.2)) {
      warnings.push(`slide ${n}: "${plain(str).slice(0, 40)}…" may overflow (${fs} pt in ${o.w}×${o.h} in) — shorten, split or move detail to notes`);
    }
    slide.addText(runs(str, { color: o.color || theme.ink, fontFace: o.font || (role === 'title' ? headFont : font) }), {
      x: o.x, y: o.y, w: o.w, h: o.h, fontSize: fs, bold: !!o.bold, italic: !!o.italic,
      align: o.align || 'left', valign: o.valign || 'top', margin: o.margin ?? 0, isTextBox: true,
      objectName: o.name || ('Metin:' + role), fit: 'none', lineSpacingMultiple: o.lsm || 1.0,
      color: o.color || theme.ink, fontFace: o.font || (role === 'title' ? headFont : font),
    });
  }
  function bullets(slide, items, o) {
    const fs = floor('body', o.fs);
    const need = items.reduce((a, it) => a + blockH(it, fs, o.w - 0.45, 1.2), 0) + (items.length - 1) * (o.gap ?? 12) / 72;
    if (need > o.h + 0.05) warnings.push(`slide ${n}: bullet list may overflow (${need.toFixed(2)} of ${o.h.toFixed(2)} in) — shorten or split`);
    const paras = [];
    items.forEach((it, i) => {
      const rs = runs(it, { color: o.color || theme.ink, fontFace: font });
      rs[0].options = { ...rs[0].options, bullet: { indent: 32 }, paraSpaceBefore: i ? (o.gap ?? 12) : 0 };
      if (i < items.length - 1) rs[rs.length - 1].options.breakLine = true;
      paras.push(...rs);
    });
    slide.addText(paras, { x: o.x, y: o.y, w: o.w, h: o.h, fontSize: fs, color: o.color || theme.ink, fontFace: font,
      valign: 'top', margin: 2, isTextBox: true, objectName: 'Metin:maddeler', fit: 'none' });
  }
  function rect(slide, x, y, w, h, fill, name, radius) {
    slide.addShape(radius ? pres.shapes.ROUNDED_RECTANGLE : pres.shapes.RECTANGLE,
      { x, y, w, h, fill: { color: fill }, line: { color: fill, width: 0 }, rectRadius: radius || 0, objectName: name || 'Kutu' });
  }
  function chip(slide, label, x, y, d, fill) {
    slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: fill || theme.accent }, line: { color: fill || theme.accent, width: 0 }, objectName: 'Numara' });
    slide.addText(String(label), { x, y, w: d, h: d, fontSize: Math.max(type.minBody, Math.round(d * 38)), bold: true, color: theme.white,
      fontFace: font, align: 'center', valign: 'middle', margin: 0, isTextBox: true, objectName: 'Metin:numara', fit: 'none' });
  }
  function image(slide, img, box, mode = 'contain') {
    const file = path.isAbsolute(img.file) ? img.file : path.join(baseDir, img.file);
    if (!fs.existsSync(file)) {
      warnings.push(`slide ${n}: image missing ${img.file} — placeholder drawn`);
      rect(slide, box.x, box.y, box.w, box.h, theme.card, 'Gorsel yok', 0.1);
      text(slide, 'Görsel: ' + (img.alt || img.file), { x: box.x + 0.2, y: box.y + box.h / 2 - 0.3, w: box.w - 0.4, h: 0.6, role: 'credit', fs: 18, color: theme.muted, align: 'center' });
      return box;
    }
    let r = img.ratio;
    if (!r && imageSize) { try { const d = imageSize(fs.readFileSync(file)); r = d.width / d.height; } catch (e) { /* ignore */ } }
    r = r || 1.5;
    if (mode === 'cover') {
      slide.addImage({ path: file, x: box.x, y: box.y, w: box.w, h: box.h, sizing: { type: 'cover', w: box.w, h: box.h },
        altText: img.alt || '', objectName: 'Gorsel' });
      return box;
    }
    let iw = box.w, ih = box.w / r;
    if (ih > box.h) { ih = box.h; iw = box.h * r; }
    const ix = box.x + (box.w - iw) / 2, iy = box.y + (box.h - ih) / 2;
    slide.addImage({ path: file, x: ix, y: iy, w: iw, h: ih, altText: img.alt || '', objectName: 'Gorsel' });
    return { x: ix, y: iy, w: iw, h: ih };
  }
  function frame(slide, s, dark) {
    // title, optional kicker, source line, slide number, layout marker, notes
    if (s.kicker && !type.exceptions.kicker) warnings.push(`slide ${n}: kicker ignored — small section labels are off unless the brief enables exceptions.kicker`);
    if (s.kicker && type.exceptions.kicker) {
      text(slide, s.kicker.toUpperCase(), { x: MX, y: 0.22, w: W - 2 * MX, h: 0.36, role: 'kicker', bold: true, color: dark ? theme.accent3 : theme.accent, name: 'Ust etiket' });
    }
    if (s.title) text(slide, s.title, { x: MX, y: GRID.titleY + (s.kicker ? 0.1 : 0), w: W - 2 * MX, h: GRID.titleH, role: 'title', fs: type.title, bold: true, color: dark ? theme.white : theme.dark, name: 'Baslik', valign: 'top' });
    if (s.source) text(slide, (s.sourcePrefix ?? 'Kaynak: ') + s.source, { x: MX, y: GRID.sourceY, w: W - 2 * MX - 1.0, h: GRID.sourceH, role: 'source', color: dark ? 'C9D2DA' : theme.muted, name: 'Kaynak satiri', valign: 'middle' });
    if (s.credit) text(slide, s.credit, { x: MX, y: (s.noNumber && !s.source) ? GRID.sourceY + 0.05 : GRID.sourceY - 0.32, w: W - 2 * MX - 1.0, h: 0.3, role: 'credit', color: dark ? 'C9D2DA' : theme.muted, name: 'Gorsel kredisi' });
    if (!s.noNumber) text(slide, String(n), { x: W - MX - 0.8, y: GRID.sourceY, w: 0.8, h: GRID.sourceH, role: 'slideNumber', color: dark ? 'C9D2DA' : theme.muted, align: 'right', name: 'Slayt no', valign: 'middle' });
    slide.addText('', { x: 0, y: 0, w: 0.01, h: 0.01, objectName: 'layout:' + s.layout, isTextBox: true, fontSize: 1 });
    if (s.notes) slide.addNotes(s.notes);
  }

  // ---------------------------------------------------------------- layouts
  const L = {};
  L.cover = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.dark };
    const hasImg = !!s.image;
    const tw = hasImg ? 7.0 : W - 2 * MX;
    if (hasImg) image(sl, s.image, { x: 7.55, y: 0, w: W - 7.55, h: H }, 'cover');
    let y = 0.9;
    if (s.kicker && type.exceptions.kicker) { text(sl, s.kicker.toUpperCase(), { x: MX, y, w: tw, h: 0.4, role: 'kicker', bold: true, color: theme.accent3, name: 'Ust etiket' }); y += 0.55; }
    let tfs = type.coverTitle;
    while (tfs > type.title && estimateLines(s.title, tfs, tw) > 3) tfs -= 4;
    const th = blockH(s.title, tfs, tw, 1.12) + 0.1;
    text(sl, s.title, { x: MX, y, w: tw, h: th, role: 'title', fs: tfs, bold: true, color: theme.white, name: 'Baslik', lsm: 0.95 });
    y += th + 0.3;
    if (s.subtitle) { const sh = blockH(s.subtitle, type.coverSub, tw) + 0.1; text(sl, s.subtitle, { x: MX, y, w: tw, h: sh, fs: type.coverSub, color: 'DCE3E8' }); y += sh + 0.3; }
    if (s.meta) text(sl, s.meta, { x: MX, y: Math.max(y, 5.2), w: tw, h: blockH(s.meta, type.body, tw) + 0.1, fs: type.body, color: theme.white, bold: true });
    if (y > 6.6) warnings.push(`slide ${n}: cover text too long — shorten title/subtitle`);
    frame(sl, { ...s, title: null, kicker: null, noNumber: true }, true);
  };
  L.agenda = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const items = s.items || []; const tw = W - 2 * MX - 1.0;
    const hs = items.map(t => Math.max(0.72, blockH(t, type.body, tw, 1.15)));
    const avail = GRID.bodyB - GRID.bodyY; const used = hs.reduce((a, b) => a + b, 0);
    const gap = items.length > 1 ? Math.max(0.1, Math.min(0.3, (avail - used) / (items.length - 1))) : 0;
    if (used + gap * (items.length - 1) > avail + 0.05) warnings.push(`slide ${n}: agenda too long — max ~6 one-line items`);
    let y = GRID.bodyY;
    items.forEach((it, i) => {
      chip(sl, i + 1, MX, y, 0.72, [theme.accent, theme.accent2, theme.accent3][i % 3]);
      text(sl, it, { x: MX + 1.0, y, w: tw, h: hs[i], valign: 'middle' });
      y += hs[i] + gap;
    });
    frame(sl, s);
  };
  L.section = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.dark };
    if (s.num != null) text(sl, String(s.num), { x: MX, y: 1.1, w: 3, h: 1.9, role: 'stat', fs: type.sectionNum, bold: true, color: theme.accent3, name: 'Bolum no' });
    text(sl, s.title, { x: MX, y: 3.15, w: W - 2 * MX, h: 1.6, role: 'title', fs: type.section, bold: true, color: theme.white, name: 'Baslik' });
    if (s.subtitle) text(sl, s.subtitle, { x: MX, y: 4.85, w: W - 2 * MX, h: 1.4, color: 'DCE3E8' });
    frame(sl, { ...s, title: null }, true);
  };
  L.bullets = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const hasImg = !!s.image; const w = hasImg ? 6.6 : W - 2 * MX;
    bullets(sl, s.items || [], { x: MX, y: GRID.bodyY, w, h: GRID.bodyB - GRID.bodyY });
    if (hasImg) image(sl, s.image, { x: MX + w + 0.35, y: GRID.bodyY, w: W - MX - (MX + w + 0.35), h: GRID.bodyB - GRID.bodyY - 0.35 }, s.imageMode || 'contain');
    frame(sl, s);
  };
  L.stat = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const st = s.stats || []; const cw = (W - 2 * MX - 0.4 * (st.length - 1)) / Math.max(st.length, 1);
    st.forEach((x, i) => {
      const cx = MX + i * (cw + 0.4);
      rect(sl, cx, GRID.bodyY, cw, 3.55, theme.light, 'Kart', 0.12);
      text(sl, x.big, { x: cx + 0.3, y: GRID.bodyY + 0.25, w: cw - 0.6, h: 1.5, role: 'stat', fs: x.fs || type.stat, bold: true, color: [theme.accent, theme.accent2, theme.accent3][i % 3], name: 'Buyuk sayi' });
      text(sl, x.label, { x: cx + 0.3, y: GRID.bodyY + 1.8, w: cw - 0.6, h: 1.6, fs: type.statLabel });
    });
    if (s.takeaway) text(sl, s.takeaway, { x: MX, y: GRID.bodyY + 3.75, w: W - 2 * MX, h: 1.1, bold: true, color: theme.dark });
    frame(sl, s);
  };
  L.cards = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const cs = s.cards || []; const gap = 0.35; const cw = (W - 2 * MX - gap * (cs.length - 1)) / Math.max(cs.length, 1);
    const ch = s.takeaway ? 3.75 : 4.8;
    cs.forEach((c, i) => {
      const cx = MX + i * (cw + gap); const col = [theme.accent, theme.accent2, theme.accent3, theme.dark][i % 4];
      rect(sl, cx, GRID.bodyY, cw, ch, theme.light, 'Kart', 0.12);
      if (c.image) image(sl, c.image, { x: cx + 0.25, y: GRID.bodyY + 0.25, w: cw - 0.5, h: 1.5 });
      else chip(sl, c.mark || (i + 1), cx + 0.3, GRID.bodyY + 0.3, 0.8, col);
      text(sl, c.head, { x: cx + 0.3, y: GRID.bodyY + 1.25 + (c.image ? 0.65 : 0), w: cw - 0.6, h: 0.75, bold: true, color: col, name: 'Kart basligi' });
      if (c.body) text(sl, c.body, { x: cx + 0.3, y: GRID.bodyY + 2.05 + (c.image ? 0.65 : 0), w: cw - 0.6, h: ch - 2.2 - (c.image ? 0.65 : 0) });
    });
    if (s.takeaway) text(sl, s.takeaway, { x: MX, y: GRID.bodyY + ch + 0.15, w: W - 2 * MX, h: 0.8, bold: true, color: theme.dark });
    frame(sl, s);
  };
  L.photoSteps = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const steps = s.steps || []; const lw = s.textWidth || 7.4; const tw = lw - 0.85; const fsb = type.body;
    const hs = steps.map(t => blockH(t, fsb, tw, 1.15));
    const avail = GRID.bodyB - GRID.bodyY; const used = hs.reduce((a, b) => a + b, 0);
    const gap = steps.length > 1 ? Math.max(0.08, Math.min(0.35, (avail - used) / (steps.length - 1))) : 0;
    if (used + gap * (steps.length - 1) > avail + 0.05) warnings.push(`slide ${n}: steps too long for one slide — shorten each step to one line or split`);
    let y = GRID.bodyY;
    steps.forEach((t, i) => {
      chip(sl, i + 1, MX, y + 0.02, 0.62, theme.accent);
      text(sl, t, { x: MX + 0.85, y, w: tw, h: hs[i] + 0.05, lsm: 0.95 });
      y += hs[i] + gap;
    });
    const ix = MX + lw + 0.3; const iw = W - MX - ix; const calloutH = s.callout ? Math.max(1.0, blockH(s.callout, fsb, iw - 0.4, 1.15) + 0.25) : 0;
    image(sl, s.image, { x: ix, y: GRID.bodyY, w: iw, h: GRID.bodyB - GRID.bodyY - calloutH - 0.1 }, s.imageMode || 'cover');
    if (s.callout) { rect(sl, ix, GRID.bodyB - calloutH, iw, calloutH, theme.light, 'Sonuc kutusu', 0.12); text(sl, s.callout, { x: ix + 0.2, y: GRID.bodyB - calloutH + 0.08, w: iw - 0.4, h: calloutH - 0.16, align: 'center', valign: 'middle', bold: true, color: theme.dark, lsm: 0.95 }); }
    frame(sl, s);
  };
  L.compare = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const cw = (W - 2 * MX - 0.5) / 2; const ch = s.takeaway ? 3.85 : 4.8;
    [[s.left, theme.accent], [s.right, theme.accent2]].forEach(([side, col], i) => {
      const cx = MX + i * (cw + 0.5);
      rect(sl, cx, GRID.bodyY, cw, ch, theme.light, 'Kart', 0.12);
      text(sl, side.head, { x: cx + 0.3, y: GRID.bodyY + 0.25, w: cw - 0.6, h: 0.75, bold: true, color: col, name: 'Kart basligi' });
      if (side.image) image(sl, side.image, { x: cx + 0.3, y: GRID.bodyY + 1.05, w: cw - 0.6, h: 1.6 });
      bullets(sl, side.items || [], { x: cx + 0.3, y: GRID.bodyY + 1.05 + (side.image ? 1.7 : 0), w: cw - 0.6, h: ch - 1.2 - (side.image ? 1.7 : 0) });
    });
    if (s.takeaway) text(sl, s.takeaway, { x: MX, y: GRID.bodyY + ch + 0.15, w: W - 2 * MX, h: 0.8, bold: true, color: theme.dark });
    frame(sl, s);
  };
  L.process = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const st = s.steps || []; const gap = 0.45; const cw = (W - 2 * MX - gap * (st.length - 1)) / Math.max(st.length, 1);
    st.forEach((t, i) => {
      const cx = MX + i * (cw + gap);
      chip(sl, i + 1, cx, GRID.bodyY + 0.1, 0.8, theme.accent);
      if (i < st.length - 1) sl.addShape(pres.shapes.LINE, { x: cx + 0.9, y: GRID.bodyY + 0.5, w: cw + gap - 1.0, h: 0, line: { color: theme.muted, width: 2.5, endArrowType: 'triangle' }, objectName: 'Ok' });
      text(sl, t.head || t, { x: cx, y: GRID.bodyY + 1.15, w: cw, h: 0.75, bold: true, color: theme.dark });
      if (t.body) text(sl, t.body, { x: cx, y: GRID.bodyY + 1.95, w: cw, h: 2.9 });
    });
    if (s.takeaway) text(sl, s.takeaway, { x: MX, y: 5.85, w: W - 2 * MX, h: 0.8, bold: true, color: theme.dark });
    frame(sl, s);
  };
  L.chart = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const cw = s.takeaway ? 7.6 : W - 2 * MX;
    const typeMap = { bar: pres.charts.BAR, line: pres.charts.LINE, pie: pres.charts.PIE, doughnut: pres.charts.DOUGHNUT, scatter: pres.charts.SCATTER };
    const fsChart = type.minBody; // chart labels follow the floor unless the brief declares exceptions.chart
    sl.addChart(typeMap[s.chartType || 'bar'], s.data, {
      x: MX, y: GRID.bodyY, w: cw, h: GRID.bodyB - GRID.bodyY,
      barDir: s.barDir || 'col', chartColors: [theme.accent, theme.accent2, theme.accent3, theme.dark],
      showValue: true, dataLabelFontSize: s.labelFs || type.exceptions.chart || fsChart, dataLabelColor: theme.ink,
      catAxisLabelFontSize: s.labelFs || type.exceptions.chart || fsChart, valAxisLabelFontSize: s.labelFs || type.exceptions.chart || fsChart,
      catAxisLabelColor: theme.muted, valAxisLabelColor: theme.muted, valGridLine: { color: 'E3E7EB', size: 1 }, catGridLine: { style: 'none' },
      showLegend: (s.data || []).length > 1, legendFontSize: s.labelFs || type.exceptions.chart || fsChart, legendPos: 'b',
      catAxisLabelFontFace: font, valAxisLabelFontFace: font, dataLabelFontFace: font, legendFontFace: font, objectName: 'Grafik',
    });
    if (s.takeaway) { rect(sl, MX + cw + 0.35, GRID.bodyY, W - MX - (MX + cw + 0.35), GRID.bodyB - GRID.bodyY, theme.light, 'Yorum kutusu', 0.12); text(sl, s.takeaway, { x: MX + cw + 0.6, y: GRID.bodyY + 0.3, w: W - MX - (MX + cw + 0.6) - 0.25, h: GRID.bodyB - GRID.bodyY - 0.6, color: theme.dark }); }
    frame(sl, s);
  };
  L.table = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const fsT = floor('body', s.fs);
    const rows = (s.rows || []).map((r, ri) => r.map(c => ({ text: noBreak(c), options: { bold: ri === 0, color: ri === 0 ? theme.white : theme.ink, fill: { color: ri === 0 ? theme.dark : (ri % 2 ? theme.light : theme.white) } } })));
    sl.addTable(rows, { x: MX, y: GRID.bodyY, w: W - 2 * MX, fontSize: fsT, fontFace: font, border: { type: 'solid', color: 'D5DCE2', pt: 1 }, margin: 0.08, objectName: 'Tablo', valign: 'middle' });
    if ((s.rows || []).length > 5) warnings.push(`slide ${n}: table has ${(s.rows || []).length} rows at ${fsT} pt — likely too tall; split or move to notes`);
    frame(sl, s);
  };
  L.quote = (s) => {
    const sl = pres.addSlide(); sl.background = { color: s.dark === false ? theme.light : theme.dark };
    const dark = s.dark !== false;
    text(sl, s.text, { x: 1.1, y: 1.6, w: W - 2.2, h: 3.4, fs: s.fs || 44, bold: true, color: dark ? theme.white : theme.dark, valign: 'middle' });
    if (s.by) text(sl, s.by, { x: 1.1, y: 5.15, w: W - 2.2, h: 0.9, color: dark ? theme.accent3 : theme.accent });
    frame(sl, { ...s, title: s.title }, dark);
  };
  L.references = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.white };
    const items = s.items || []; const fsR = type.exceptions.references;
    sl.addText(items.map((r, i) => ({ text: noBreak(r), options: { breakLine: i < items.length - 1, paraSpaceAfter: 4, fontFace: font } })),
      { x: MX, y: GRID.bodyY - 0.2, w: W - 2 * MX, h: GRID.bodyB - GRID.bodyY + 0.6, fontSize: fsR, color: theme.ink, valign: 'top', margin: 0, isTextBox: true, objectName: 'Kaynakca', fit: 'none' });
    if (estimateLines(items.join('\n'), fsR, W - 2 * MX) * fsR * 1.25 / 72 > 5.2) warnings.push(`slide ${n}: references overflow — split into another references slide`);
    frame(sl, { ...s, source: null });
  };
  L.closing = (s) => {
    const sl = pres.addSlide(); sl.background = { color: theme.dark };
    text(sl, s.title || 'Özet', { x: MX, y: 0.6, w: W - 2 * MX, h: 1.0, role: 'title', fs: type.title, bold: true, color: theme.white, name: 'Baslik' });
    bullets(sl, s.items || [], { x: MX, y: 1.9, w: W - 2 * MX, h: 4.6, color: theme.white });
    frame(sl, { ...s, title: null }, true);
  };

  function addSlide(s) {
    n += 1;
    const fn = L[s.layout];
    if (!fn) throw new Error(`slide ${n}: unknown layout "${s.layout}". Use one of: ${Object.keys(L).join(', ')}`);
    layoutLog.push(s.layout);
    const k = layoutLog.length;
    if (k >= 3 && layoutLog[k - 1] === layoutLog[k - 2] && layoutLog[k - 2] === layoutLog[k - 3] && !['references'].includes(s.layout)) {
      warnings.push(`slide ${n}: layout "${s.layout}" used 3 times in a row — vary the layout`);
    }
    fn(s);
  }
  async function save(file) {
    await pres.writeFile({ fileName: file });
    return { file, slides: n, warnings };
  }
  return { pres, addSlide, save, warnings, theme, type, layouts: Object.keys(L) };
}

module.exports = { createDeck, THEMES, SAFE_FONTS, DEFAULT_TYPE, estimateLines, blockH, fits, noBreak };
