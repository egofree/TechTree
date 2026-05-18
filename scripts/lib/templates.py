"""HTML template generation for the Bootciv offline browser.

Pure-Python HTML5 generation using f-strings. No template engine, no
external URLs, fully file:// compatible.
"""

from __future__ import annotations

from typing import Any


# ---------------------------------------------------------------------------
# Badge helpers
# ---------------------------------------------------------------------------

_BADGE_ICONS = {
    "critical": "\u2605",       # ★
    "early_win": "\u26a1",     # ⚡
    "pinnacle": "\U0001f53a",  # 🔺
}

_BADGE_CSS = {
    "critical": "badge badge--critical",
    "early_win": "badge badge--early-win",
    "pinnacle": "badge badge--pinnacle",
}


def _badge_html(flag: str, note: str | None = None) -> str:
    """Return a single badge <span>, optionally with a title tooltip."""
    icon = _BADGE_ICONS.get(flag, "?")
    css = _BADGE_CSS.get(flag, "badge")
    title_attr = f' title="{note}"' if note else ""
    return f'<span class="{css}"{title_attr}>{icon}</span>'


def _flags(node: dict[str, Any]) -> list[tuple[str, str | None]]:
    """Extract (flag_name, note) pairs that are truthy on *node*."""
    out: list[tuple[str, str | None]] = []
    for flag in ("critical", "early_win", "pinnacle"):
        if node.get(flag):
            out.append((flag, node.get(f"{flag}_note")))
    return out


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

def render_sidebar(
    tree: list[dict[str, Any]],
    current_path: str,
    link_prefix: str = "",
    page_map: dict[str, str] | None = None,
) -> str:
    parts: list[str] = []

    parts.append('<nav class="sidebar">')
    parts.append(
        '<input type="text" id="search-input" placeholder="Search..." '
        'autocomplete="off" />'
    )
    parts.append('<div id="search-results"></div>')

    for domain in tree:
        domain_badges = "".join(
            _badge_html(f, n) for f, n in _flags(domain)
        )
        domain_open = " open" if _is_active(domain, current_path, page_map) else ""
        parts.append(
            f'<details class="sidebar__domain"{domain_open}>'
        )
        domain_href = link_prefix + _resolve_href(domain["id"], page_map)
        if domain_href:
            parts.append(
                f'<summary class="sidebar__domain-title">'
                f'<a href="{domain_href}" class="sidebar__domain-link">'
                f'{domain["name"]}</a> {domain_badges}</summary>'
            )
        else:
            parts.append(
                f'<summary class="sidebar__domain-title">'
                f'{domain["name"]} {domain_badges}</summary>'
            )
        parts.append('<ul class="sidebar__capabilities">')

        for cap in domain.get("children", []):
            cap_href = link_prefix + _resolve_href(cap["id"], page_map)
            active = ' class="active"' if _is_active(cap, current_path, page_map) else ""
            cap_badges = "".join(
                _badge_html(f, n) for f, n in _flags(cap)
            )
            if cap_href:
                parts.append(
                    f'<li{active}>'
                    f'<a href="{cap_href}">{cap["name"]} {cap_badges}</a>'
                    f'</li>'
                )
            else:
                parts.append(
                    f'<li{active}>'
                    f'{cap["name"]} {cap_badges}'
                    f'</li>'
                )

        parts.append('</ul>')
        parts.append('</details>')

    parts.append('</nav>')
    return "\n".join(parts)


def _is_active(node: dict[str, Any], current_path: str, page_map: dict[str, str] | None = None) -> bool:
    """True if *node* (or any of its children) is the current page."""
    href = _resolve_href(node["id"], page_map)
    if href == current_path:
        return True
    for child in node.get("children", []):
        if _is_active(child, current_path, page_map):
            return True
    return False


def _page_href(node_id: str) -> str:
    """Convert a dotted node ID to a relative HTML path.

    ``metallurgy.iron-steel`` -> ``docs/metallurgy/iron-steel.html``
    ``metallurgy``            -> ``docs/metallurgy/index.html``
    """
    segments = node_id.split(".")
    if len(segments) == 1:
        return f"docs/{segments[0]}/index.html"
    return f"docs/{segments[0]}/{'-'.join(segments[1:])}.html"


def _resolve_href(node_id: str, page_map: dict[str, str] | None) -> str:
    """Resolve node ID to href using page_map. Returns '' if no page exists."""
    if page_map and node_id in page_map:
        return page_map[node_id]
    return ""


# ---------------------------------------------------------------------------
# Metadata block (info card)
# ---------------------------------------------------------------------------

def render_metadata_block(
    metadata: dict[str, Any],
    node_page_map: dict[str, str],
    edges: list[dict[str, Any]],
    link_prefix: str = "",
) -> str:
    """Render a styled metadata info card for a capability page.

    Parameters
    ----------
    metadata:
        Node data dict (from nodes.json) with keys like ``id, name,
        timeline, outputs, critical, …``.
    node_page_map:
        ``{node_id: relative_html_path}`` for resolving dependency links.
    edges:
        Full edge list (from edges.json). Each edge has ``from, to, type``.
    """
    node_id = metadata.get("id", "")
    parts: list[str] = ['<div class="metadata-card">']

    flags = _flags(metadata)
    badge_html = " ".join(_badge_html(f, n) for f, n in flags)
    parts.append(
        f'<h2 class="metadata-card__title">'
        f'{metadata.get("name", node_id)} {badge_html}</h2>'
    )

    def _field(label: str, value: str) -> None:
        parts.append(
            f'<div class="metadata-card__field">'
            f'<span class="metadata-card__label">{label}</span>'
            f'<span class="metadata-card__value">{value}</span>'
            f'</div>'
        )

    _field("Node ID", f"<code>{node_id}</code>")

    domain = node_id.split(".")[0] if "." in node_id else node_id
    _field("Domain", domain)

    timeline = metadata.get("timeline", "")
    if timeline:
        _field("Timeline", timeline)

    outputs = metadata.get("outputs", [])
    if outputs:
        _field("Outputs", ", ".join(f"<code>{o}</code>" for o in outputs))

    deps = [e["from"] for e in edges if e.get("to") == node_id]
    if deps:
        links = " ".join(_node_link(d, node_page_map, link_prefix) for d in sorted(set(deps)))
        _field("Dependencies", links)

    enables = [e["to"] for e in edges if e.get("from") == node_id]
    if enables:
        links = " ".join(_node_link(t, node_page_map, link_prefix) for t in sorted(set(enables)))
        _field("Enables", links)

    if flags:
        badge_row = " ".join(
            f'<span class="metadata-card__flag">{_badge_html(f, n)} '
            f'{f.replace("_", " ").title()}</span>'
            for f, n in flags
        )
        parts.append(
            f'<div class="metadata-card__flags">{badge_row}</div>'
        )

    parts.append('</div>')
    return "\n".join(parts)


def _node_link(node_id: str, node_page_map: dict[str, str], link_prefix: str = "") -> str:
    """Build an <a> tag for a dependency/enables link."""
    href = link_prefix + node_page_map.get(node_id, "#")
    return f'<a class="metadata-card__link" href="{href}">{node_id}</a>'


# ---------------------------------------------------------------------------
# Full page
# ---------------------------------------------------------------------------

def render_page(
    title: str,
    content: str,
    sidebar_html: str,
    current_path: str,
    metadata: dict[str, Any] | None = None,
    node_page_map: dict[str, str] | None = None,
    edges: list[dict[str, Any]] | None = None,
    asset_prefix: str = "",
    search_index_js: str = "",
) -> str:
    """Render a complete HTML5 page.

    Parameters
    ----------
    title:
        Page <title> and visible heading.
    content:
        Main-body HTML (already rendered from Markdown or otherwise).
    sidebar_html:
        Pre-rendered sidebar HTML (from :func:`render_sidebar`).
    current_path:
        Relative path of this page for active-state highlighting.
    metadata:
        Optional node data. If provided along with *node_page_map* and
        *edges*, a metadata card is rendered above *content*.
    node_page_map:
        ``{node_id: relative_html_path}`` — required if *metadata* is given.
    edges:
        Full edge list — required if *metadata* is given.
    asset_prefix:
        Prefix for asset paths. ``""`` for root-level pages,
        ``"../../"`` for depth-2 pages like docs/domain/page.html.
    search_index_js:
        If non-empty, inline ``<script>`` block with window.SEARCH_INDEX.
    """
    meta_block = ""
    if metadata and node_page_map is not None and edges is not None:
        meta_block = render_metadata_block(metadata, node_page_map, edges, asset_prefix)

    search_index_block = ""
    if search_index_js:
        search_index_block = f"<script>{search_index_js}</script>"

    h1_block = ""
    if not content.lstrip().startswith("<h1>"):
        h1_block = f"<h1>{_esc(title)}</h1>\n"

    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{_esc(title)}</title>
<link rel="stylesheet" href="{asset_prefix}assets/style.css" />
</head>
<body>
<div class="layout">
{sidebar_html}
<main class="content">
{h1_block}{meta_block}
{content}
</main>
</div>
<footer class="footer">
<p>Part of the Bootciv Tech Tree</p>
</footer>
<script src="{asset_prefix}assets/mermaid.min.js"></script>
<script src="{asset_prefix}assets/search-index.js"></script>
<script src="{asset_prefix}assets/search.js"></script>
<script src="{asset_prefix}assets/main.js"></script>
</body>
</html>"""


def _esc(text: str) -> str:
    """Minimal HTML escaping for title text."""
    return (
        text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
