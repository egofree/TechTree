"""Wikipedia disambiguation page detector and resolver for the plants domain.

Detects Wikipedia disambiguation pages via HTML markers and resolves them to
the most relevant article for the plants domain by keyword scoring. Follows at
most one hop (never chains disambiguation pages).

Stdlib-only: re, html.parser, urllib.parse.
"""

from __future__ import annotations

import re
import urllib.parse


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_DISAMBIG_ID_RE = re.compile(r'id="disambig"', re.IGNORECASE)
_DISAMBIG_CLASS_RE = re.compile(r'class="[^"]*disambig[^"]*"', re.IGNORECASE)
_DISAMBIG_TITLE_RE = re.compile(r"\(disambiguation\)", re.IGNORECASE)

# Internal wiki link: <a href="/wiki/Page_title" ...>link text</a>
_WIKI_LINK_RE = re.compile(
    r'<a\s+[^>]*href="(/wiki/([^"#]+))"[^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)

# Strip HTML tags for plain-text extraction
_STRIP_TAGS_RE = re.compile(r"<[^>]+>")
_COLLAPSE_WS_RE = re.compile(r"\s+")

# Default use-category keywords (mirrors plants.yaml use_categories)
_DEFAULT_KEYWORDS: dict[str, list[str]] = {
    "edible": ["edible", "food", "fruit", "vegetable", "grain", "cereal", "nut"],
    "medicinal": [
        "medicinal", "herbal", "pharmaceutical", "remedy",
        "traditional medicine",
    ],
    "structural": [
        "timber", "wood", "construction", "building", "structural", "lumber",
    ],
    "fiber": ["fiber", "fibre", "cordage", "rope", "textile", "weaving"],
    "dye": ["dye", "pigment", "colorant", "stain"],
}


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _strip_tags(html: str) -> str:
    """Remove all HTML tags and collapse whitespace."""
    text = _STRIP_TAGS_RE.sub(" ", html)
    return _COLLAPSE_WS_RE.sub(" ", text).strip()


def _extract_wiki_links(html: str) -> list[tuple[str, str, str]]:
    """Extract internal Wikipedia links from HTML.

    Returns list of (href_path, page_title, link_text) tuples.
    Skips special namespaces (File:, Category:, Help:, etc.) and
    fragment-only links.
    """
    _SKIP_PREFIXES = (
        "Special:", "Talk:", "User:", "Wikipedia:", "File:",
        "MediaWiki:", "Template:", "Help:", "Category:", "Portal:",
        "Draft:", "TimedText:", "Module:", "Book:", "MOS:",
    )
    links: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for m in _WIKI_LINK_RE.finditer(html):
        href_path = m.group(1)
        page_title = urllib.parse.unquote(m.group(2)).replace("_", " ")
        link_text = _strip_tags(m.group(3))
        decoded_lower = page_title.lower()
        if any(decoded_lower.startswith(p.lower()) for p in _SKIP_PREFIXES):
            continue
        if page_title in seen:
            continue
        seen.add(page_title)
        links.append((href_path, page_title, link_text))
    return links


def _score_link(
    page_title: str,
    link_text: str,
    keywords: dict[str, list[str]],
) -> float:
    """Score a link's relevance to the plants domain.

    Points:
      +2.0 for each keyword match in the page title
      +1.0 for each keyword match in the link text
      +1.5 bonus if the title contains a parenthetical like "(plant)"
            that matches any keyword category
    """
    score = 0.0
    title_lower = page_title.lower()
    text_lower = link_text.lower()

    all_kw: list[str] = []
    for kw_list in keywords.values():
        all_kw.extend(kw_list)

    for kw in all_kw:
        if kw in title_lower:
            score += 2.0
        if kw in text_lower:
            score += 1.0

    paren_m = re.search(r"\(([^)]+)\)", title_lower)
    if paren_m:
        paren_content = paren_m.group(1).strip()
        for kw in all_kw:
            if kw == paren_content or kw in paren_content:
                score += 1.5
                break

    return score


def _compute_confidence(best_score: float, second_score: float) -> str:
    """Classify confidence level from score gap.

    Returns 'high', 'medium', or 'low'.
    """
    if best_score >= 4.0 and (best_score - second_score) >= 2.0:
        return "high"
    if best_score >= 2.0:
        return "medium"
    return "low"


# ---
# Public API
# ---


def is_disambiguation_page(html: str, title: str = "") -> bool:
    """Detect whether HTML represents a Wikipedia disambiguation page.

    Detection strategies (in order):
      1. HTML contains ``id="disambig"`` attribute
      2. CSS class containing "disambig" on any element
      3. Page title (from ``<title>`` tag or *title* arg) contains
         "(disambiguation)"
      4. Heuristic: many internal links with very short text between them

    Args:
        html: Raw HTML string from Wikipedia REST API.
        title: Optional page title for additional checking.

    Returns:
        True if the page is a disambiguation page.
    """
    # Strategy 3: Title check (works even with empty HTML)
    title_to_check = title or ""
    if html:
        title_tag_m = re.search(r"<title>([^<]*)</title>", html, re.IGNORECASE)
        if title_tag_m:
            title_to_check = title_tag_m.group(1)
    if title_to_check and _DISAMBIG_TITLE_RE.search(title_to_check):
        return True

    if not html:
        return False

    # Strategy 1 & 2: HTML markers
    if _DISAMBIG_ID_RE.search(html):
        return True
    if _DISAMBIG_CLASS_RE.search(html):
        return True

    # Strategy 4: Link-density heuristic
    # Disambiguation pages have many links with minimal intervening text.
    # Look for the main content div and count links vs text density.
    content_m = re.search(
        r'<div[^>]*class="[^"]*mw-parser-output[^"]*"[^>]*>(.*)',
        html, re.IGNORECASE | re.DOTALL,
    )
    content_block = content_m.group(1) if content_m else html

    # Only scan up to the first section heading (disambiguation pages
    # are usually short).
    heading_m = re.search(
        r'<h[12][^>]*>', content_block, re.IGNORECASE
    )
    if heading_m:
        content_block = content_block[:heading_m.start()]

    links = _extract_wiki_links(content_block)
    plain_text = _strip_tags(content_block)

    if len(links) >= 5:
        # Ratio of links to text length — disambiguation pages are link-heavy
        text_len = max(len(plain_text), 1)
        link_ratio = len(links) / (text_len / 100.0)
        if link_ratio >= 3.0:
            return True

    return False


def resolve_disambiguation(
    html: str,
    title: str,
    keywords: dict[str, list[str]] | None = None,
    client: object | None = None,
    limiter: object | None = None,
) -> dict:
    """Resolve a disambiguation page to the most relevant article.

    Extracts all internal links from the disambiguation page, scores each
    against the provided keywords (or default plants-domain keywords), and
    returns the highest-scoring link as the resolved target.

    Follows at most **one hop**: if *client* is provided, fetches the
    resolved page's HTML and includes it. Does NOT chase further
    disambiguation chains.

    Args:
        html: Raw HTML of the disambiguation page.
        title: Page title (e.g. "Apple").
        keywords: Dict mapping category id to keyword list. Defaults to
            the plants-domain use_categories from plants.yaml.
        client: Optional WikiClient instance for fetching the resolved page.
        limiter: Optional rate-limiter with a ``wait()`` method (called
            before any HTTP request).

    Returns:
        Dict with keys:
            - ``resolved_title`` (str): Best-match article title.
            - ``resolved_url`` (str): Full Wikipedia URL of the best match.
            - ``resolved_html`` (str | None): HTML of resolved page if
              *client* was provided and fetch succeeded.
            - ``alternatives`` (list[dict]): Other candidate articles with
              ``title`` and ``relevance_score`` keys, sorted by score desc,
              excluding the best match.
            - ``confidence`` (str): "high", "medium", or "low".
            - ``original_title`` (str): The disambiguation page title.
    """
    kw = keywords if keywords is not None else _DEFAULT_KEYWORDS

    links = _extract_wiki_links(html)

    if not links:
        print("    disambiguation: no internal links found in '{}'".format(title))
        return {
            "resolved_title": title,
            "resolved_url": "",
            "resolved_html": None,
            "alternatives": [],
            "confidence": "low",
            "original_title": title,
        }

    scored: list[dict] = []
    for href_path, page_title, link_text in links:
        score = _score_link(page_title, link_text, kw)
        scored.append({
            "title": page_title,
            "href": href_path,
            "relevance_score": score,
        })

    scored.sort(key=lambda x: (-x["relevance_score"], x["title"]))

    best = scored[0]
    alternatives = [
        {"title": s["title"], "relevance_score": s["relevance_score"]}
        for s in scored[1:]
        if s["relevance_score"] > 0
    ]

    second_score = scored[1]["relevance_score"] if len(scored) > 1 else 0.0
    confidence = _compute_confidence(best["relevance_score"], second_score)

    resolved_url = "https://en.wikipedia.org{}".format(best["href"])

    print(
        "    disambiguation: '{}' -> '{}' (score={:.1f}, confidence={})".format(
            title, best["title"], best["relevance_score"], confidence,
        )
    )

    resolved_html = None
    if client is not None:
        if limiter is not None and hasattr(limiter, "wait"):
            limiter.wait()
        raw = client.get(url=resolved_url)
        if raw is not None:
            resolved_html = raw.decode("utf-8", errors="replace")
        else:
            print(
                "    disambiguation: failed to fetch resolved page '{}'".format(
                    best["title"]
                )
            )

    return {
        "resolved_title": best["title"],
        "resolved_url": resolved_url,
        "resolved_html": resolved_html,
        "alternatives": alternatives,
        "confidence": confidence,
        "original_title": title,
    }
