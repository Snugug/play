/* Hand-inked rules, drawn with Rough.js.
   Every line on the sheet — table boxes, dividers, heading rules — is drawn
   here rather than with CSS borders. Each target gets its own <svg> child so
   the strokes live in that element's coordinate space and inherit its
   rotation. Seeds are fixed, so the sheet looks identical every load and the
   print matches the screen. */
(function () {
  'use strict';

  var INK = '#1d1b16';

  /* Restrained: a ruler-assisted hand, not a shaky one. */
  var PEN = {
    box:     { roughness: 0.6,  bowing: 0.4, strokeWidth: 1.5 },
    heavy:   { roughness: 0.55, bowing: 0.4, strokeWidth: 1.6 },
    divider: { roughness: 0.45, bowing: 0.3, strokeWidth: 0.7, disableMultiStroke: true },
    column:  { roughness: 0.4,  bowing: 0.25, strokeWidth: 0.6, disableMultiStroke: true }
  };

  var seed = 41;
  function pen(kind) {
    var o = PEN[kind];
    seed = (seed * 31 + 17) % 9973;
    return {
      stroke: INK,
      roughness: o.roughness,
      bowing: o.bowing,
      strokeWidth: o.strokeWidth,
      disableMultiStroke: o.disableMultiStroke,
      seed: seed
    };
  }

  function layerFor(el) {
    var old = el.querySelector(':scope > svg.ink');
    if (old) old.remove();
    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('class', 'ink');
    svg.setAttribute('aria-hidden', 'true');
    el.appendChild(svg);
    return svg;
  }

  /* The sheet may be scaled down to fit a narrow viewport. Measure in the
     sheet's own units so the strokes land in the right place either way. */
  function sheetScale() {
    var sheet = document.querySelector('.sheet');
    if (!sheet || !sheet.offsetWidth) return 1;
    return sheet.getBoundingClientRect().width / sheet.offsetWidth || 1;
  }

  function boxOf(el, origin, scale) {
    var b = el.getBoundingClientRect();
    return {
      x: (b.left - origin.left) / scale,
      y: (b.top - origin.top) / scale,
      w: b.width / scale,
      h: b.height / scale,
      right: (b.right - origin.left) / scale,
      bottom: (b.bottom - origin.top) / scale
    };
  }

  /* Scale the whole sheet down to fit a narrow screen rather than reflowing
     it: the page is a document, not a responsive layout. */
  function fit() {
    var stage = document.querySelector('.stage');
    var sheet = document.querySelector('.sheet');
    if (!stage || !sheet) return;
    var room = stage.clientWidth - 16;
    var scale = Math.min(1, room / sheet.offsetWidth);
    stage.style.setProperty('--fit', scale > 0 ? scale : 1);
  }

  function draw() {
    if (typeof rough === 'undefined') return;
    seed = 41;

    var scale = sheetScale();

    /* A rule under an element, spanning its full width. offsetWidth/Height are
       the untransformed layout box — getBoundingClientRect would hand back the
       bounding box of the rotation and draw the line too low and too wide. */
    document.querySelectorAll('.masthead, .zone').forEach(function (el) {
      var svg = layerFor(el);
      var r = rough.svg(svg);
      svg.appendChild(r.line(0, el.offsetHeight - 1.5, el.offsetWidth, el.offsetHeight - 1.5, pen('heavy')));
    });

    /* Tables: outer box, a rule under the header, a light divider between
       rows, and light column dividers. */
    document.querySelectorAll('.tbl-wrap').forEach(function (wrap) {
      var table = wrap.querySelector('table');
      if (!table) return;
      var svg = layerFor(wrap);
      var r = rough.svg(svg);
      var origin = wrap.getBoundingClientRect();
      var t = boxOf(table, origin, scale);

      svg.appendChild(r.rectangle(t.x, t.y, t.w, t.h, pen('box')));

      var head = table.querySelector('thead');
      if (head) {
        var h = boxOf(head, origin, scale);
        svg.appendChild(r.line(t.x, h.bottom, t.right, h.bottom, pen('heavy')));
      }

      var rows = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
      rows.slice(0, -1).forEach(function (tr) {
        var rb = boxOf(tr, origin, scale);
        svg.appendChild(r.line(t.x, rb.bottom, t.right, rb.bottom, pen('divider')));
      });

      if (rows.length) {
        var cells = Array.prototype.slice.call(rows[0].children);
        cells.slice(0, -1).forEach(function (cell) {
          var cb = boxOf(cell, origin, scale);
          svg.appendChild(r.line(cb.right, t.y, cb.right, t.bottom, pen('column')));
        });
      }
    });

    /* The closing line sits in its own scrawled box, on the tilt the element
       already carries. */
    document.querySelectorAll('.win').forEach(function (el) {
      var svg = layerFor(el);
      var r = rough.svg(svg);
      svg.appendChild(r.rectangle(1, 1, el.offsetWidth - 2, el.offsetHeight - 2, pen('box')));
    });
  }

  function ready() {
    fit();
    draw();
    /* Re-measure once webfonts land: they change how the text wraps, which
       changes every row height. */
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
  } else {
    ready();
  }

  var t;
  window.addEventListener('resize', function () {
    clearTimeout(t);
    t = setTimeout(function () { fit(); draw(); }, 150);
  });
  window.addEventListener('beforeprint', draw);

  /* The font picker changes text metrics, so it needs to re-run both. */
  window.DiceInk = { draw: draw, fit: fit };
})();
