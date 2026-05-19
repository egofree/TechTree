(function () {
  var current = document.querySelector(".sidebar a.active");
  if (current) { var details = current.closest("details"); if (details) details.open = true; }

  if (!window.mermaid) return;

  var containers = document.querySelectorAll('.mermaid-container');
  var sources = [];
  for (var i = 0; i < containers.length; i++) {
    var pre = containers[i].querySelector('pre.mermaid');
    sources.push(pre ? pre.textContent : '');
  }

  mermaid.initialize({ startOnLoad: false, theme: 'default' });
  mermaid.run().then(function () {
    for (var i = 0; i < containers.length; i++) setupDiagram(containers[i], sources[i]);
  });

  function setupDiagram(container, source) {
    var svg = container.querySelector('svg');
    if (!svg) return;

    var viewport = document.createElement('div');
    viewport.className = 'diagram-viewport';
    container.appendChild(viewport);
    viewport.appendChild(svg);

    var wrapper = document.createElement('div');
    wrapper.className = 'diagram-wrapper';
    container.parentNode.insertBefore(wrapper, container);
    wrapper.appendChild(container);

    var scale = 1, tx = 0, ty = 0;
    function applyTransform() {
      viewport.style.transform = 'scale(' + scale + ') translate(' + tx + 'px, ' + ty + 'px)';
    }

    var toggleBtn = document.createElement('button');
    toggleBtn.className = 'diagram-toggle';
    toggleBtn.textContent = 'View Source';
    toggleBtn.setAttribute('type', 'button');
    wrapper.insertBefore(toggleBtn, container);

    var sourcePre = document.createElement('pre');
    sourcePre.className = 'diagram-source';
    sourcePre.textContent = source;
    sourcePre.style.display = 'none';
    wrapper.appendChild(sourcePre);

    toggleBtn.addEventListener('click', function () {
      var isRendered = container.style.display !== 'none';
      if (isRendered) {
        container.style.display = 'none'; sourcePre.style.display = 'block';
        toggleBtn.textContent = 'View Diagram';
      } else {
        container.style.display = ''; sourcePre.style.display = 'none';
        toggleBtn.textContent = 'View Source';
        scale = 1; tx = 0; ty = 0; applyTransform();
      }
    });

    var controls = document.createElement('div');
    controls.className = 'diagram-controls';
    var btnDefs = [['+', 'Zoom in'], ['\u2212', 'Zoom out'], ['\u229e', 'Fit to view'], ['\u26f6', 'Fullscreen']];
    var btns = [];
    for (var b = 0; b < btnDefs.length; b++) {
      var btn = document.createElement('button');
      btn.textContent = btnDefs[b][0];
      btn.setAttribute('type', 'button');
      btn.setAttribute('title', btnDefs[b][1]);
      controls.appendChild(btn); btns.push(btn);
    }
    wrapper.insertBefore(controls, container);

    var MIN_SCALE = 0.1, MAX_SCALE = 5, ZOOM_STEP = 0.2;
    function clampScale(s) { return s < MIN_SCALE ? MIN_SCALE : (s > MAX_SCALE ? MAX_SCALE : s); }
    function zoomAtPoint(factor, px, py) {
      var ns = clampScale(scale * factor), r = ns / scale;
      tx = px - (px - tx) * r; ty = py - (py - ty) * r; scale = ns; applyTransform();
    }
    function zoomCenter(factor) {
      var rect = viewport.getBoundingClientRect();
      zoomAtPoint(factor, rect.width / 2, rect.height / 2);
    }

    btns[0].addEventListener('click', function () { zoomCenter(1 + ZOOM_STEP); });
    btns[1].addEventListener('click', function () { zoomCenter(1 / (1 + ZOOM_STEP)); });
    btns[2].addEventListener('click', function () { scale = 1; tx = 0; ty = 0; applyTransform(); });
    btns[3].addEventListener('click', function () { openFullscreen(svg); });

    container.addEventListener('wheel', function (e) {
      e.preventDefault();
      var rect = viewport.getBoundingClientRect();
      zoomAtPoint(e.deltaY < 0 ? (1 + ZOOM_STEP) : (1 / (1 + ZOOM_STEP)), e.clientX - rect.left, e.clientY - rect.top);
    }, { passive: false });

    var dragging = false, startX, startY, startTx, startTy;
    viewport.addEventListener('mousedown', function (e) {
      if (e.button !== 0) return;
      dragging = true; startX = e.clientX; startY = e.clientY; startTx = tx; startTy = ty;
      viewport.classList.add('diagram-pan-active'); e.preventDefault();
    });
    document.addEventListener('mousemove', function (e) {
      if (!dragging) return;
      tx = startTx + (e.clientX - startX) / scale; ty = startTy + (e.clientY - startY) / scale; applyTransform();
    });
    document.addEventListener('mouseup', function () {
      if (!dragging) return;
      dragging = false; viewport.classList.remove('diagram-pan-active');
    });
  }

  var overlay = document.createElement('div');
  overlay.className = 'fullscreen-overlay';
  document.body.appendChild(overlay);

  var closeBtn = document.createElement('button');
  closeBtn.className = 'close-btn'; closeBtn.textContent = '\u2715'; closeBtn.setAttribute('type', 'button');
  overlay.appendChild(closeBtn);

  var fsControls = document.createElement('div');
  fsControls.className = 'fullscreen-controls';
  var fsBtnDefs = [['+', 'Zoom in'], ['\u2212', 'Zoom out'], ['\u229e', 'Fit to view']];
  var fsBtns = [];
  for (var f = 0; f < fsBtnDefs.length; f++) {
    var fb = document.createElement('button');
    fb.textContent = fsBtnDefs[f][0]; fb.setAttribute('type', 'button'); fb.setAttribute('title', fsBtnDefs[f][1]);
    fsControls.appendChild(fb); fsBtns.push(fb);
  }
  overlay.appendChild(fsControls);

  var fsViewport = document.createElement('div');
  fsViewport.className = 'fullscreen-viewport';
  overlay.appendChild(fsViewport);

  var fsScale = 1, fsTx = 0, fsTy = 0;

  function openFullscreen(svg) {
    var existing = fsViewport.querySelector('.diagram-viewport');
    if (existing) fsViewport.removeChild(existing);
    var vp = document.createElement('div');
    vp.className = 'diagram-viewport';
    var clone = svg.cloneNode(true); clone.style.maxWidth = 'none';
    vp.appendChild(clone); fsViewport.appendChild(vp);
    fsScale = 1; fsTx = 0; fsTy = 0;
    vp.style.transform = 'scale(1) translate(0px, 0px)';
    overlay.classList.add('active');

    vp.addEventListener('wheel', function (e) {
      e.preventDefault(); e.stopPropagation();
      var rect = vp.getBoundingClientRect(), mx = e.clientX - rect.left, my = e.clientY - rect.top;
      var factor = e.deltaY < 0 ? 1.2 : (1 / 1.2);
      var ns = fsScale * factor; if (ns < 0.1) ns = 0.1; if (ns > 5) ns = 5;
      var r = ns / fsScale; fsTx = mx - (mx - fsTx) * r; fsTy = my - (my - fsTy) * r;
      fsScale = ns; vp.style.transform = 'scale(' + fsScale + ') translate(' + fsTx + 'px, ' + fsTy + 'px)';
    }, { passive: false });

    var oDragging = false, oStartX, oStartY, oStartTx, oStartTy;
    vp.addEventListener('mousedown', function (e) {
      if (e.button !== 0) return;
      oDragging = true; oStartX = e.clientX; oStartY = e.clientY; oStartTx = fsTx; oStartTy = fsTy;
      vp.classList.add('diagram-pan-active'); e.preventDefault();
    });
    overlay._moveHandler = function (e) {
      if (!oDragging) return;
      fsTx = oStartTx + (e.clientX - oStartX) / fsScale; fsTy = oStartTy + (e.clientY - oStartY) / fsScale;
      vp.style.transform = 'scale(' + fsScale + ') translate(' + fsTx + 'px, ' + fsTy + 'px)';
    };
    overlay._upHandler = function () {
      if (!oDragging) return; oDragging = false; vp.classList.remove('diagram-pan-active');
    };
    document.addEventListener('mousemove', overlay._moveHandler);
    document.addEventListener('mouseup', overlay._upHandler);

    fsBtns[0].onclick = function () {
      fsScale = Math.min(fsScale * 1.2, 5);
      vp.style.transform = 'scale(' + fsScale + ') translate(' + fsTx + 'px, ' + fsTy + 'px)';
    };
    fsBtns[1].onclick = function () {
      fsScale = Math.max(fsScale / 1.2, 0.1);
      vp.style.transform = 'scale(' + fsScale + ') translate(' + fsTx + 'px, ' + fsTy + 'px)';
    };
    fsBtns[2].onclick = function () {
      fsScale = 1; fsTx = 0; fsTy = 0; vp.style.transform = 'scale(1) translate(0px, 0px)';
    };
  }

  function closeFullscreen() {
    overlay.classList.remove('active');
    if (overlay._moveHandler) { document.removeEventListener('mousemove', overlay._moveHandler); overlay._moveHandler = null; }
    if (overlay._upHandler) { document.removeEventListener('mouseup', overlay._upHandler); overlay._upHandler = null; }
    var vp = fsViewport.querySelector('.diagram-viewport');
    if (vp) fsViewport.removeChild(vp);
  }

  closeBtn.addEventListener('click', closeFullscreen);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && overlay.classList.contains('active')) closeFullscreen();
  });
})();
