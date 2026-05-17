(function () {
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  if (!input || !results) return;

  function snippet(text, query, len) {
    var lower = text.toLowerCase();
    var idx = lower.indexOf(query);
    if (idx === -1) return text.substring(0, len) + "...";
    var start = Math.max(0, idx - Math.floor(len / 2));
    var end = Math.min(text.length, start + len);
    var s = text.substring(start, end);
    if (start > 0) s = "..." + s;
    if (end < text.length) s = s + "...";
    return s;
  }

  window.siteSearch = function (query) {
    if (!window.SEARCH_INDEX || !query) return [];
    var q = query.toLowerCase();
    var out = [];
    for (var i = 0; i < window.SEARCH_INDEX.length; i++) {
      var entry = window.SEARCH_INDEX[i];
      var titleMatch = entry.title.toLowerCase().indexOf(q) !== -1;
      var contentMatch = entry.content.toLowerCase().indexOf(q) !== -1;
      if (titleMatch || contentMatch) {
        out.push({
          title: entry.title,
          url: entry.url,
          snippet: snippet(entry.content, q, 100),
        });
        if (out.length >= 20) break;
      }
    }
    return out;
  };

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
      var hits = window.siteSearch(q);
      if (hits.length === 0) {
        results.className = "";
        results.innerHTML = "";
        return;
      }
      results.innerHTML = hits
        .map(function (h) {
          return '<a href="' + h.url + '">' + h.title + "<br><small>" + h.snippet + "</small></a>";
        })
        .join("");
      results.className = "active";
    }, 200);
  });
})();
