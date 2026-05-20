"""Wikipedia article extractor with template fallback chain for plant data.

Parses raw HTML from the Wikipedia REST API and extracts structured plant
data using a three-tier fallback strategy:
  1. Infobox table rows (taxonomic and descriptive fields)
  2. Section text (keywords in Uses, Distribution, Description headings)
  3. Minimal entry (article title only, flagged for manual research)

Stdlib-only: re, html.parser, json. Never raises on bad input -- always
returns a valid entry dict.
"""

from __future__ import annotations

import re


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Wikipedia infobox class patterns
_INFOBOX_RE = re.compile(
    r'<table[^>]+class="[^"]*infobox[^"]*"[^>]*>',
    re.IGNORECASE | re.DOTALL,
)

# Section headline: <span class="mw-headline" id="...">
_HEADLINE_RE = re.compile(
    r'<span\s+class="mw-headline"\s+id="([^"]*)">',
    re.IGNORECASE,
)

# Italic binomial name in first paragraph: <i>Genus species</i>
_ITALIC_BINOMIAL_RE = re.compile(
    r"<i>\s*([A-Z][a-z]+\s+[a-z]{2,}(?:\s+[a-z]+)?)\s*</i>",
)

# Simplified binomial outside tags (fallback)
_BARE_BINOMIAL_RE = re.compile(
    r"\b([A-Z][a-z]+\s+[a-z]{2,}(?:\s+[a-z]+)?)\b",
)

# Disambiguation signals
_DISAMBIG_ID_RE = re.compile(r'id="disambig"', re.IGNORECASE)
_DISAMBIG_CLASS_RE = re.compile(
    r'class="[^"]*disambig[^"]*"', re.IGNORECASE,
)
_DISAMBIG_TITLE_RE = re.compile(
    r"\(disambiguation\)", re.IGNORECASE,
)

# Redirect detection
_REDIRECT_RE = re.compile(
    r'<div\s+class="redirectMsg"', re.IGNORECASE,
)

# Strip HTML tags for plain-text extraction
_STRIP_TAGS_RE = re.compile(r"<[^>]+>")
_COLLAPSE_WS_RE = re.compile(r"\s+")

# Infobox row: <tr>...</tr> (non-greedy, handles nested tables poorly but
# sufficient for simple label-value rows)
_TR_RE = re.compile(
    r"<tr[^>]*>(.*?)</tr>",
    re.IGNORECASE | re.DOTALL,
)

# Paragraph block
_P_RE = re.compile(
    r"<p[^>]*>(.*?)</p>",
    re.IGNORECASE | re.DOTALL,
)

# Headings that indicate useful section content
_SECTION_IDS_USES = {"uses", "use", "usage", "uses_and_economic_importance"}
_SECTION_IDS_DIST = {
    "distribution", "distribution_and_habitat",
    "native_range", "range", "habitat",
    "geographic_distribution",
}
_SECTION_IDS_DESC = {"description", "characteristics", "morphology"}
_SECTION_IDS_CULT = {"cultivation", "agriculture", "growing"}

# Label-to-field mapping for infobox row extraction
_LABEL_FIELD_MAP = [
    (re.compile(r"family", re.IGNORECASE), "family"),
    (re.compile(r"order\b", re.IGNORECASE), "order"),
    (re.compile(r"genus", re.IGNORECASE), "genus"),
    (re.compile(r"species", re.IGNORECASE), "species_field"),
    (re.compile(r"native|origin|distribution", re.IGNORECASE), "native_region"),
    (re.compile(r"binomial name|scientific name|binomial", re.IGNORECASE),
     "scientific_name"),
    (re.compile(r"common\s*names?", re.IGNORECASE), "common_names_str"),
]

# Default use-category config (overridden by caller-supplied config)
_DEFAULT_USE_CATEGORIES = [
    {"id": "edible", "keywords": [
        "edible", "food", "fruit", "vegetable", "grain", "cereal", "nut",
    ]},
    {"id": "medicinal", "keywords": [
        "medicinal", "herbal", "pharmaceutical", "remedy",
        "traditional medicine",
    ]},
    {"id": "structural", "keywords": [
        "timber", "wood", "construction", "building", "structural", "lumber",
    ]},
    {"id": "fiber", "keywords": [
        "fiber", "fibre", "cordage", "rope", "textile", "weaving",
    ]},
    {"id": "dye", "keywords": [
        "dye", "pigment", "colorant", "stain",
    ]},
]


# ---------------------------------------------------------------------------
# HTML helpers
# ---------------------------------------------------------------------------


def _strip_tags(html: str) -> str:
    """Remove all HTML tags and collapse whitespace."""
    text = _STRIP_TAGS_RE.sub(" ", html)
    text = _COLLAPSE_WS_RE.sub(" ", text).strip()
    return text


def _strip_and_unescape(html: str) -> str:
    """Remove tags and decode common HTML entities."""
    text = _strip_tags(html)
    text = text.replace("&amp;", "&")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&quot;", '"')
    text = text.replace("&#39;", "'")
    text = text.replace("&nbsp;", " ")
    return text.strip()


def _find_infobox(html: str) -> str | None:
    """Extract the first infobox <table>...</table> block from HTML.

    Uses a simple brace-counting approach to find the matching </table>.
    """
    m = _INFOBOX_RE.search(html)
    if not m:
        return None
    start = m.start()
    depth = 0
    pos = start
    while pos < len(html):
        open_m = re.search(r"<table[^>]*>", html[pos:], re.IGNORECASE)
        close_m = re.search(r"</table>", html[pos:], re.IGNORECASE)
        if close_m is None:
            break
        if open_m and open_m.start() < close_m.start():
            depth += 1
            pos += open_m.end()
        else:
            depth -= 1
            pos += close_m.end()
            if depth <= 0:
                return html[start:pos]
    return None


def _extract_table_rows(infobox_html: str) -> list[tuple[str, str]]:
    """Parse infobox rows into (label, value) pairs.

    Handles both <th>label</th><td>value</td> and
    <td>label</td><td>value</td> patterns.
    """
    rows: list[tuple[str, str]] = []
    for tr_m in _TR_RE.finditer(infobox_html):
        tr_html = tr_m.group(1)
        cells: list[str] = []
        for cell_m in re.finditer(
            r"<(th|td)[^>]*>(.*?)</\1>", tr_html, re.IGNORECASE | re.DOTALL
        ):
            cells.append(_strip_and_unescape(cell_m.group(2)))
        if len(cells) >= 2:
            rows.append((cells[0], cells[1]))
        elif len(cells) == 1:
            rows.append((cells[0], ""))
    return rows


def _extract_sections(html: str) -> dict[str, str]:
    """Split HTML into sections keyed by headline id.

    Returns a dict mapping lowercase section id to the raw HTML content
    until the next heading or end of document.
    """
    sections: dict[str, str] = {}
    headlines = list(_HEADLINE_RE.finditer(html))
    for i, hm in enumerate(headlines):
        section_id = hm.group(1).lower()
        start = hm.end()
        end = headlines[i + 1].start() if i + 1 < len(headlines) else len(html)
        sections[section_id] = html[start:end]
    return sections


def _extract_first_paragraphs(html: str, max_paragraphs: int = 3) -> str:
    """Extract the text of the first N <p> elements after the infobox.

    Falls back to the first <p> elements in the document if no infobox
    is found.
    """
    infobox_m = _INFOBOX_RE.search(html)
    search_start = 0
    if infobox_m:
        infobox_block = _find_infobox(html)
        if infobox_block:
            search_start = html.find(infobox_block) + len(infobox_block)
    chunk = html[search_start:]
    texts: list[str] = []
    for pm in _P_RE.finditer(chunk):
        para_text = _strip_and_unescape(pm.group(1))
        if len(para_text) < 20:
            continue
        texts.append(para_text)
        if len(texts) >= max_paragraphs:
            break
    return " ".join(texts)


def _extract_scientific_name(html: str, infobox_rows: list[tuple[str, str]]) -> str:
    """Try multiple strategies to find the scientific (binomial) name.

    Strategy order:
      1. Infobox row labeled "binomial name" / "scientific name"
      2. Italic text in first paragraph: <i>Genus species</i>
      3. Bare binomial pattern in first paragraph text
    """
    for label, value in infobox_rows:
        lbl = label.lower().strip()
        lbl_stripped = lbl.rstrip(":")
        if lbl_stripped in ("binomial name", "scientific name", "binomial"):
            name = value.strip()
            if name:
                return name

    paras = _extract_first_paragraphs(html, max_paragraphs=1)
    m = _ITALIC_BINOMIAL_RE.search(paras)
    if m:
        return m.group(1).strip()

    m = _BARE_BINOMIAL_RE.search(paras)
    if m:
        return m.group(1).strip()

    return ""


def _detect_uses(
    text: str,
    use_categories: list[dict] | None = None,
) -> list[str]:
    """Scan text for keywords matching use categories.

    Args:
        text: Plain text to scan (typically the full article text).
        use_categories: List of dicts with 'id' and 'keywords' keys.
            Defaults to _DEFAULT_USE_CATEGORIES.

    Returns:
        Sorted list of matched category ids.
    """
    categories = use_categories or _DEFAULT_USE_CATEGORIES
    text_lower = text.lower()
    matched: list[str] = []
    for cat in categories:
        cat_id = cat.get("id", "")
        keywords = cat.get("keywords", [])
        for kw in keywords:
            if kw.lower() in text_lower:
                matched.append(cat_id)
                break
    return sorted(set(matched))


def _extract_native_region(
    infobox_rows: list[tuple[str, str]],
    sections: dict[str, str],
) -> str:
    """Extract native region from infobox or Distribution section."""
    for label, value in infobox_rows:
        lbl = label.lower().strip().rstrip(":")
        if any(kw in lbl for kw in ("native", "origin", "distribution")):
            if value.strip():
                return value.strip()

    for section_id in _SECTION_IDS_DIST:
        section_html = sections.get(section_id, "")
        if section_html:
            text = _strip_and_unescape(section_html)
            sentence = text.split(".")[0].strip()
            if sentence:
                return sentence[:200]

    return ""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def is_disambiguation(html: str) -> bool:
    """Detect whether HTML represents a Wikipedia disambiguation page.

    Checks for:
      - id="disambig" attribute
      - CSS class containing "disambig"
      - Title containing "(disambiguation)"

    Args:
        html: Raw HTML string from Wikipedia REST API.

    Returns:
        True if the page is a disambiguation page.
    """
    if not html:
        return False
    if _DISAMBIG_ID_RE.search(html):
        return True
    if _DISAMBIG_CLASS_RE.search(html):
        return True
    title_m = re.search(r"<title>([^<]*)</title>", html, re.IGNORECASE)
    if title_m and _DISAMBIG_TITLE_RE.search(title_m.group(1)):
        return True
    return False


def is_redirect(html: str) -> bool:
    """Detect whether HTML represents a Wikipedia redirect page."""
    if not html:
        return False
    return bool(_REDIRECT_RE.search(html))


def extract_plant_data(
    html: str,
    title: str,
    config: dict | None = None,
) -> dict:
    """Extract structured plant data from Wikipedia HTML.

    Uses a three-tier fallback chain:
      1. **Infobox**: Parse <table class="infobox ..."> rows for taxonomic
         fields (family, order, scientific name) and native region.
      2. **Section text**: Scan sections (Uses, Distribution, Description)
         for keywords matching configured use_categories.
      3. **Minimal entry**: If nothing useful is found, create a stub entry
         with the article title as common_name and ``needs_research=True``.

    Never raises on bad input. Always returns a valid entry dict.

    Args:
        html: Raw HTML from the Wikipedia REST API.
        title: Article title (used as fallback common_name and source_url).
        config: Optional extraction config dict. Recognised keys:
            - ``use_categories``: list of {id, keywords} dicts overriding
              the default categories.

    Returns:
        Dict with keys: scientific_name, common_names, family, order,
        native_region, uses, description, source_url, extraction_quality,
        needs_research, is_disambiguation, raw_sections.
    """
    if not html or not isinstance(html, str):
        return _minimal_entry(title or "unknown", "empty_html")

    disambig = is_disambiguation(html)
    if disambig:
        return _minimal_entry(title or "unknown", "disambiguation", is_disambig=True)

    if is_redirect(html):
        return _minimal_entry(title or "unknown", "redirect")

    use_categories = None
    if config and "use_categories" in config:
        use_categories = config["use_categories"]

    # Tier 1: Infobox extraction
    infobox_html = _find_infobox(html)
    infobox_rows: list[tuple[str, str]] = []
    infobox_fields: dict[str, str] = {}

    if infobox_html:
        infobox_rows = _extract_table_rows(infobox_html)
        infobox_fields = _extract_infobox_fields(infobox_rows)

    # Tier 2: Section text extraction
    sections = _extract_sections(html)
    all_text = _strip_and_unescape(html)

    scientific_name = _extract_scientific_name(html, infobox_rows)
    if not scientific_name and "scientific_name" in infobox_fields:
        scientific_name = infobox_fields["scientific_name"]

    common_names = _extract_common_names(title, infobox_rows, infobox_fields)

    family = infobox_fields.get("family", "")
    order = infobox_fields.get("order", "")

    native_region = _extract_native_region(infobox_rows, sections)

    description = _extract_first_paragraphs(html, max_paragraphs=2)
    if len(description) > 500:
        description = description[:497] + "..."

    uses = _detect_uses(all_text, use_categories)

    source_url = ""
    if title:
        encoded = title.replace(" ", "_")
        source_url = "https://en.wikipedia.org/wiki/{}".format(encoded)

    quality = _assess_quality(
        scientific_name=scientific_name,
        family=family,
        uses=uses,
        description=description,
    )

    needs_research = quality in ("minimal", "partial")

    return {
        "scientific_name": scientific_name,
        "common_names": common_names,
        "family": family,
        "order": order,
        "native_region": native_region,
        "uses": uses,
        "description": description,
        "source_url": source_url,
        "extraction_quality": quality,
        "needs_research": needs_research,
        "is_disambiguation": disambig,
        "raw_sections": {
            k: _strip_and_unescape(v)[:300]
            for k, v in sections.items()
        },
    }


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _minimal_entry(
    title: str,
    reason: str,
    is_disambig: bool = False,
) -> dict:
    """Build a minimal stub entry for articles that cannot be parsed."""
    print(
        "    article_extractor: minimal entry for '{}' ({})".format(
            title, reason
        )
    )
    source_url = ""
    if title and title != "unknown":
        encoded = title.replace(" ", "_")
        source_url = "https://en.wikipedia.org/wiki/{}".format(encoded)

    return {
        "scientific_name": "",
        "common_names": [title] if title and title != "unknown" else [],
        "family": "",
        "order": "",
        "native_region": "",
        "uses": [],
        "description": "",
        "source_url": source_url,
        "extraction_quality": "minimal",
        "needs_research": True,
        "is_disambiguation": is_disambig,
        "raw_sections": {},
    }


def _extract_infobox_fields(rows: list[tuple[str, str]]) -> dict[str, str]:
    """Map infobox label text to field names.

    Returns a dict of matched fields (e.g. {"family": "Poaceae"}).
    """
    fields: dict[str, str] = {}
    for label, value in rows:
        lbl = label.strip().rstrip(":").lower()
        for pattern, field_name in _LABEL_FIELD_MAP:
            if pattern.search(lbl):
                val = value.strip()
                if val:
                    fields[field_name] = val
                break
    return fields


def _extract_common_names(
    title: str | None,
    infobox_rows: list[tuple[str, str]],
    infobox_fields: dict[str, str],
) -> list[str]:
    """Collect common names from title, infobox, and first sentence.

    Deduplicates while preserving order.
    """
    names: list[str] = []

    if title:
        cleaned = title.strip()
        if cleaned:
            names.append(cleaned)

    raw = infobox_fields.get("common_names_str", "")
    if raw:
        for part in re.split(r"[,\n;]", raw):
            part = part.strip()
            if part and part not in names:
                names.append(part)

    return names


def _assess_quality(
    scientific_name: str,
    family: str,
    uses: list[str],
    description: str,
) -> str:
    """Rate the extraction quality as 'complete', 'partial', or 'minimal'.

    - 'complete': scientific_name present plus at least one of (family, uses,
      description with substantial content).
    - 'partial': some fields present but not enough for 'complete'.
    - 'minimal': nothing useful extracted.
    """
    score = 0
    if scientific_name:
        score += 2
    if family:
        score += 1
    if uses:
        score += 1
    if description and len(description) > 50:
        score += 1

    if score >= 3:
        return "complete"
    if score >= 1:
        return "partial"
    return "minimal"
