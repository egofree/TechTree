(function () {
  // Sidebar auto-expand: open the <details> containing the active link
  var current = document.querySelector(".sidebar a.active");
  if (current) {
    var details = current.closest("details");
    if (details) details.open = true;
  }

  // Only proceed if mermaid.js is loaded
  if (!window.mermaid) return;

  // Find all mermaid diagram containers
  var containers = document.querySelectorAll('.mermaid-container');
  for (var i = 0; i < containers.length; i++) {
    var container = containers[i];
    var pre = container.querySelector('pre.mermaid');
    if (!pre) continue;

    // Store original source
    var source = pre.textContent;
    pre.setAttribute('data-mermaid-source', source);

    // Create a wrapper div for toggle functionality
    var wrapper = document.createElement('div');
    wrapper.className = 'diagram-wrapper';
    container.parentNode.insertBefore(wrapper, container);
    wrapper.appendChild(container);

    // Create toggle button
    var toggleBtn = document.createElement('button');
    toggleBtn.className = 'diagram-toggle';
    toggleBtn.textContent = 'View Source';
    toggleBtn.setAttribute('type', 'button');
    wrapper.insertBefore(toggleBtn, container);

    // Create source view (hidden by default)
    var sourcePre = document.createElement('pre');
    sourcePre.className = 'diagram-source';
    sourcePre.textContent = source;
    sourcePre.style.display = 'none';
    wrapper.appendChild(sourcePre);

    // Toggle handler
    (function (container, sourcePre, toggleBtn) {
      toggleBtn.addEventListener('click', function () {
        var isRendered = container.style.display !== 'none';
        if (isRendered) {
          container.style.display = 'none';
          sourcePre.style.display = 'block';
          toggleBtn.textContent = 'View Diagram';
        } else {
          container.style.display = '';
          sourcePre.style.display = 'none';
          toggleBtn.textContent = 'View Source';
        }
      });
    })(container, sourcePre, toggleBtn);
  }

  // Initialize mermaid and render all diagrams
  mermaid.initialize({ startOnLoad: false, theme: 'default' });
  mermaid.run();
})();
