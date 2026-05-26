(function () {
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  if (!input || !results) return;

  function snippet(text, indices, len) {
    if (!text) return "";
    if (!indices || indices.length === 0) {
      return text.length > len ? text.substring(0, len) + "..." : text;
    }
    var best = indices[0];
    var start = Math.max(0, best[0] - Math.floor(len / 2));
    var end = Math.min(text.length, start + len);
    var s = text.substring(start, end);
    if (start > 0) s = "..." + s;
    if (end < text.length) s = s + "...";
    return s;
  }

  var fuse = null;
  var activeIndex = -1;

  function initFuse() {
    if (fuse || !window.SEARCH_INDEX) return;
    fuse = new Fuse(window.SEARCH_INDEX, {
      keys: [
        { name: "title", weight: 0.7 },
        { name: "content", weight: 0.3 }
      ],
      threshold: 0.3,
      ignoreLocation: true,
      includeMatches: true,
      minMatchCharLength: 2
    });
  }

  function renderResults(hits) {
    if (hits.length === 0) {
      results.className = "";
      results.innerHTML = "";
      return;
    }
    activeIndex = -1;
    results.innerHTML = hits.map(function (h, i) {
      var titleIndices = [];
      var contentIndices = [];
      if (h.matches) {
        for (var m = 0; m < h.matches.length; m++) {
          if (h.matches[m].key === "title") titleIndices = h.matches[m].indices;
          if (h.matches[m].key === "content") contentIndices = h.matches[m].indices;
        }
      }
      var snip = snippet(h.item.content, contentIndices, 100);
      return '<a href="' + h.item.url + '" data-index="' + i + '">'
        + h.item.title
        + "<br><small>" + snip + "</small></a>";
    }).join("");
    results.className = "active";
  }

  function setActive(idx) {
    var links = results.querySelectorAll("a");
    for (var i = 0; i < links.length; i++) {
      links[i].classList.remove("search-active");
    }
    activeIndex = idx;
    if (idx >= 0 && idx < links.length) {
      links[idx].classList.add("search-active");
    }
  }

  var debounce = null;
  input.addEventListener("input", function () {
    clearTimeout(debounce);
    debounce = setTimeout(function () {
      var q = input.value.trim();
      if (q.length < 2) {
        results.className = "";
        results.innerHTML = "";
        return;
      }
      initFuse();
      if (!fuse) return;
      var hits = fuse.search(q);
      renderResults(hits.slice(0, 20));
    }, 200);
  });

  input.addEventListener("keydown", function (e) {
    var links = results.querySelectorAll("a");
    var count = links.length;
    if (count === 0) return;

    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActive(activeIndex < count - 1 ? activeIndex + 1 : 0);
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActive(activeIndex > 0 ? activeIndex - 1 : count - 1);
    } else if (e.key === "Enter") {
      if (activeIndex >= 0 && activeIndex < count) {
        e.preventDefault();
        links[activeIndex].click();
      }
    }
  });

  document.addEventListener("click", function (e) {
    if (!results.contains(e.target) && e.target !== input) {
      results.className = "";
      results.innerHTML = "";
    }
  });
})();
