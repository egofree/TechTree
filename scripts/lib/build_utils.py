"""Markdown rendering and metadata extraction for bootciv docs."""

import json
import re
from pathlib import Path

from markdown_it import MarkdownIt

from .templates import render_page, render_sidebar


def _get_md_renderer() -> MarkdownIt:
    md = MarkdownIt().enable("table")
    return md


def render_markdown(md_content: str) -> str:
    """Render markdown to HTML using markdown-it-py.

    Converts relative .md links to .html links before rendering.
    Preserves HTML entities and unicode.
    """
    converted = re.sub(
        r"\[([^\]]*)\]\(([^)]+)\.md\)",
        r"[\1](\2.html)",
        md_content,
    )
    md = _get_md_renderer()
    return md.render(converted)


def extract_metadata(md_content: str) -> dict:
    """Parse blockquote metadata headers from markdown.

    Extracts fields matching: > **Field**: `value`[, `value2`, ...]
    Returns dict with normalized field names.
    """
    metadata = {}
    field_pattern = re.compile(r"^>\s+\*\*([^*]+)\*\*:\s+(.+)$", re.MULTILINE)

    for match in field_pattern.finditer(md_content):
        field = match.group(1).strip()
        value_line = match.group(2).strip()
        key = field.lower().replace(" ", "_")

        tick_values = re.findall(r"`([^`]*)`", value_line)

        if key == "also_covers":
            metadata["also_covers"] = [v.strip() for v in tick_values if v.strip()]
        elif key in ("dependencies", "enables"):
            metadata[key] = [v.strip() for v in tick_values if v.strip()]
        elif key == "outputs":
            metadata[key] = [v.strip() for v in value_line.split(",") if v.strip()]
        else:
            if tick_values:
                metadata[key] = tick_values[0].strip()
            else:
                metadata[key] = value_line

    return metadata


def read_all_markdown(docs_dir: str) -> list[dict]:
    """Walk docs/ directory and read all .md files.

    Skips the supporting/ directory.
    Returns list of dicts with: path, relative_path, domain, filename,
    metadata, html_body.
    """
    docs_path = Path(docs_dir)
    results = []

    for md_file in sorted(docs_path.rglob("*.md")):
        rel = md_file.relative_to(docs_path)
        parts = rel.parts

        if parts[0] == "supporting":
            continue

        content = md_file.read_text(encoding="utf-8")
        metadata = extract_metadata(content)
        html_body = render_markdown(content)

        if len(parts) == 1:
            domain = ""
        else:
            domain = parts[0]

        results.append({
            "path": str(md_file),
            "relative_path": str(rel),
            "domain": domain,
            "filename": md_file.name,
            "metadata": metadata,
            "html_body": html_body,
        })

    return results


def build_node_page_map(docs_dir: str, nodes_json: dict) -> dict[str, str]:
    """Build a mapping from node IDs to their HTML page paths.

    Walks docs/ for .md files, extracts metadata to get the Node ID,
    and maps each node ID (plus any "Also covers" aliases) to the
    relative HTML path for that page.

    Args:
        docs_dir: Path to the docs/ directory.
        nodes_json: Parsed nodes.json dict (used for node ID validation).

    Returns:
        Dict mapping node_id -> relative HTML path
        (e.g. ``{'metallurgy.iron-steel': 'docs/metallurgy/iron-steel.html'}``).
    """
    docs_path = Path(docs_dir)
    node_page_map: dict[str, str] = {}

    for md_file in sorted(docs_path.rglob("*.md")):
        rel = md_file.relative_to(docs_path)
        parts = rel.parts

        if parts[0] == "supporting":
            continue

        content = md_file.read_text(encoding="utf-8")
        metadata = extract_metadata(content)

        node_id = metadata.get("node_id")
        if not node_id:
            continue

        html_rel = "docs/" + str(rel.with_suffix(".html"))
        node_page_map[node_id] = html_rel

        for alias in metadata.get("also_covers", []):
            node_page_map[alias] = html_rel

    # Add domain-level nodes (they have generated index.html pages)
    for node in nodes_json["nodes"]:
        if node.get("level") == "domain" and node["id"] not in node_page_map:
            node_page_map[node["id"]] = f"docs/{node['id']}/index.html"

    return node_page_map


def get_node_children(nodes_json: dict, parent_id: str) -> list[dict]:
    """Find all direct children of a given node.

    Args:
        nodes_json: Parsed nodes.json dict.
        parent_id: The node ID to find children for.

    Returns:
        List of child node dicts, sorted by name.
    """
    children = [
        node
        for node in nodes_json["nodes"]
        if node.get("parent") == parent_id
    ]
    return sorted(children, key=lambda n: n["name"])


def build_sidebar_tree(nodes_json: dict) -> list[dict]:
    """Build a tree structure for sidebar navigation.

    Finds all domain-level nodes and their direct children.

    Args:
        nodes_json: Parsed nodes.json dict.

    Returns:
        List of domain dicts, each with ``children`` list, sorted by name.
        Each entry: ``{id, name, critical, early_win, pinnacle, children: [...]}``
    """
    def _node_summary(node: dict) -> dict:
        return {
            "id": node["id"],
            "name": node["name"],
            "critical": node.get("critical", False),
            "early_win": node.get("early_win", False),
            "pinnacle": node.get("pinnacle", False),
        }

    domains = [
        node for node in nodes_json["nodes"]
        if node.get("level") == "domain"
    ]

    result = []
    for domain in sorted(domains, key=lambda n: n["name"]):
        children = get_node_children(nodes_json, domain["id"])
        entry = _node_summary(domain)
        entry["children"] = [_node_summary(c) for c in children]
        result.append(entry)

    return result


# ---------------------------------------------------------------------------
# T9: Cross-reference linkification
# ---------------------------------------------------------------------------

_NODE_ID_RE = re.compile(
    r"<code>([a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)+)</code>"
)


def linkify_node_ids(html: str, page_map: dict[str, str], link_prefix: str = "") -> str:
    """Replace backtick-wrapped node IDs in HTML with clickable links.

    Only replaces IDs that exist in *page_map*. Unknown IDs are left as-is.
    """
    def _replace(match: re.Match) -> str:
        node_id = match.group(1)
        if node_id in page_map:
            href = link_prefix + page_map[node_id]
            return f'<a class="node-ref" href="{href}">{node_id}</a>'
        return match.group(0)

    return _NODE_ID_RE.sub(_replace, html)


# ---------------------------------------------------------------------------
# Node lookup helpers
# ---------------------------------------------------------------------------

def _node_by_id(nodes_json: dict, node_id: str) -> dict | None:
    for node in nodes_json["nodes"]:
        if node["id"] == node_id:
            return node
    return None


def _edges_for(edges: list[dict], node_id: str):
    deps = sorted(set(e["to"] for e in edges if e.get("from") == node_id))
    enables = sorted(set(e["from"] for e in edges if e.get("to") == node_id))
    return deps, enables


# ---------------------------------------------------------------------------
# Mermaid diagram helpers
# ---------------------------------------------------------------------------

def _strip_elk_init(mmd_content: str) -> str:
    """Replace ELK renderer init block with dagre for client-side use."""
    return re.sub(
        r'%%\{init: \{"flowchart": \{"defaultRenderer": "elk"',
        '%%{init: {"flowchart": {"defaultRenderer": "dagre"',
        mmd_content,
    )


def _embed_diagram(domain_id: str, site_dir: str, mermaid_dir: str, link_prefix: str) -> str:
    """Build diagram HTML for a domain page — SVG img if available, else mermaid source."""
    svg_path = Path(site_dir) / "diagrams" / f"{domain_id}.svg"
    if svg_path.exists():
        return (
            f'<div class="mermaid-container">'
            f'<img src="{link_prefix}diagrams/{domain_id}.svg" '
            f'alt="{domain_id} dependency diagram" />'
            f'</div>'
        )
    mmd_path = Path(mermaid_dir) / f"{domain_id}.mmd"
    if mmd_path.exists():
        source = _strip_elk_init(mmd_path.read_text(encoding="utf-8"))
        import html as _html
        escaped = _html.escape(source)
        return (
            f'<div class="mermaid-container">'
            f'<pre class="mermaid">{escaped}</pre>'
            f'</div>'
        )
    return ""


# ---------------------------------------------------------------------------
# T6: Capability page generator
# ---------------------------------------------------------------------------

def generate_capability_pages(
    docs_dir: str,
    site_dir: str,
    nodes_json: dict,
    edges_json: list[dict],
    page_map: dict[str, str],
    sidebar_tree: list[dict],
) -> list[dict]:
    """Generate HTML pages for each capability .md file.

    Returns list of {title, url, content} for search index.
    """
    md_files = read_all_markdown(docs_dir)
    search_entries = []
    edges = edges_json
    count = 0

    for md in md_files:
        if not md["domain"]:
            continue

        node_id = md["metadata"].get("node_id", "")
        node_data = _node_by_id(nodes_json, node_id) if node_id else None

        html_body = linkify_node_ids(md["html_body"], page_map, "../../")

        html_filename = Path(md["filename"]).with_suffix(".html").name
        current_path = f"docs/{md['domain']}/{html_filename}"

        sidebar_html = render_sidebar(sidebar_tree, current_path, link_prefix="../../", page_map=page_map)

        meta_for_template = node_data if node_data else None

        page_title = node_data.get("name", node_id) if node_data else html_filename

        page_html = render_page(
            title=page_title,
            content=html_body,
            sidebar_html=sidebar_html,
            current_path=current_path,
            metadata=meta_for_template,
            node_page_map=page_map,
            edges=edges,
            asset_prefix="../../",
        )

        out_path = Path(site_dir) / "docs" / md["domain"] / html_filename
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page_html, encoding="utf-8")
        count += 1

        search_entries.append({
            "title": page_title,
            "url": current_path,
            "content": _strip_html_tags(html_body),
        })

    print(f"  Generated {count} capability pages")
    return search_entries


# ---------------------------------------------------------------------------
# T7: Domain landing page generator
# ---------------------------------------------------------------------------

def generate_domain_pages(
    site_dir: str,
    nodes_json: dict,
    edges_json: list[dict],
    page_map: dict[str, str],
    sidebar_tree: list[dict],
    mermaid_dir: str,
) -> list[dict]:
    """Generate index.html for each domain.

    Returns list of {title, url, content} for search index.
    """
    search_entries = []
    count = 0

    for domain_node in nodes_json["nodes"]:
        if domain_node.get("level") != "domain":
            continue

        domain_id = domain_node["id"]
        domain_name = domain_node["name"]
        domain_desc = domain_node.get("description", "")

        children = get_node_children(nodes_json, domain_id)

        current_path = f"docs/{domain_id}/index.html"
        sidebar_html = render_sidebar(sidebar_tree, current_path, link_prefix="../../", page_map=page_map)

        parts = []
        parts.append(f"<p>{domain_desc}</p>")

        if children:
            parts.append("<h2>Capabilities</h2>")
            parts.append('<ul class="capability-list">')
            for child in children:
                child_href_raw = page_map.get(child["id"], "")
                child_href = f"../../{child_href_raw}" if child_href_raw else ""
                child_desc = child.get("description", "")
                if child_href:
                    parts.append(
                        f'<li><a href="{child_href}"><strong>{child["name"]}</strong></a>'
                        f'<p>{child_desc}</p></li>'
                    )
                else:
                    parts.append(
                        f'<li><strong>{child["name"]}</strong>'
                        f'<p>{child_desc}</p></li>'
                    )
            parts.append("</ul>")

        diagram_html = _embed_diagram(domain_id, site_dir, mermaid_dir, "../../")
        if diagram_html:
            parts.append('<h2>Dependency Diagram</h2>')
            parts.append(diagram_html)

        content = "\n".join(parts)

        page_html = render_page(
            title=domain_name,
            content=content,
            sidebar_html=sidebar_html,
            current_path=current_path,
            asset_prefix="../../",
        )

        out_path = Path(site_dir) / "docs" / domain_id / "index.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page_html, encoding="utf-8")
        count += 1

        search_entries.append({
            "title": domain_name,
            "url": current_path,
            "content": _strip_html_tags(content),
        })

    print(f"  Generated {count} domain pages")
    return search_entries


def _page_href_simple(node_id: str) -> str:
    segments = node_id.split(".")
    if len(segments) == 1:
        return f"docs/{segments[0]}/index.html"
    return f"docs/{segments[0]}/{'-'.join(segments[1:])}.html"


# ---------------------------------------------------------------------------
# T8: Home page generator
# ---------------------------------------------------------------------------

def generate_home_page(
    docs_dir: str,
    site_dir: str,
    nodes_json: dict,
    edges_json: list[dict],
    checklist: dict,
    page_map: dict[str, str],
    sidebar_tree: list[dict],
    mermaid_dir: str,
) -> dict:
    """Generate site/index.html from docs/index.md.

    Returns {title, url, content} for search index.
    """
    index_md_path = Path(docs_dir) / "index.md"
    index_content = index_md_path.read_text(encoding="utf-8")

    html_body = render_markdown(index_content)
    html_body = linkify_node_ids(html_body, page_map)

    valid_domain_dirs = set()
    for path in page_map.values():
        parts = path.split("/")
        if len(parts) == 3 and parts[0] == "docs" and parts[2] == "index.html":
            valid_domain_dirs.add(parts[1])

    def _replace_domain_link(match: re.Match) -> str:
        domain = match.group(1)
        if domain in valid_domain_dirs:
            return f'href="docs/{domain}/index.html"'
        return match.group(0)

    html_body = re.sub(
        r'href="([a-z][a-z0-9-]*)/"',
        _replace_domain_link,
        html_body,
    )
    html_body = re.sub(r'<a href="([a-z][a-z0-9-]*)/"[^>]*>([^<]*)</a>', r'\2', html_body)
    html_body = re.sub(r'<a href="[^"]*\.\./[^"]*"[^>]*>([^<]*)</a>', r'\1', html_body)
    html_body = re.sub(r'<a href="supporting/[^"]*"[^>]*>([^<]*)</a>', r'\1', html_body)
    html_body = re.sub(r'<a href="[^"]*AGENTS[^"]*"[^>]*>([^<]*)</a>', r'\1', html_body)

    tier_sections = []
    for tier_key, tier_data in checklist.items():
        if tier_key.startswith("_"):
            continue
        tier_name = tier_key.replace("_", " ").title()
        timeline = tier_data.get("timeline", "")
        tier_sections.append(f'<h2>{tier_name} ({timeline})</h2>')
        tier_sections.append("<ul>")
        for item in tier_data.get("items", []):
            item_id = item.get("id", "")
            item_name = item.get("name", "")
            if item_id in page_map:
                href = page_map[item_id]
                tier_sections.append(f'<li><a href="{href}">{item_name}</a></li>')
            else:
                tier_sections.append(f"<li>{item_name}</li>")
        tier_sections.append("</ul>")

    if tier_sections:
        html_body += '\n<h2>Milestone Tiers</h2>\n' + "\n".join(tier_sections)

    overview_path = Path(mermaid_dir) / "overview.mmd"
    if overview_path.exists():
        svg_path = Path(site_dir) / "diagrams" / "overview.svg"
        if svg_path.exists():
            html_body += (
                '<h2>Dependency Overview</h2>'
                '<div class="mermaid-container">'
                '<img src="diagrams/overview.svg" alt="Dependency overview diagram" />'
                '</div>'
            )
        else:
            source = _strip_elk_init(overview_path.read_text(encoding="utf-8"))
            import html as _html
            escaped = _html.escape(source)
            html_body += (
                '<h2>Dependency Overview</h2>'
                '<div class="mermaid-container">'
                f'<pre class="mermaid">{escaped}</pre>'
                '</div>'
            )

    current_path = "index.html"
    sidebar_html = render_sidebar(sidebar_tree, current_path, link_prefix="", page_map=page_map)

    page_html = render_page(
        title="Bootciv Tech Tree",
        content=html_body,
        sidebar_html=sidebar_html,
        current_path=current_path,
        asset_prefix="",
    )

    out_path = Path(site_dir) / "index.html"
    out_path.write_text(page_html, encoding="utf-8")
    print("  Generated home page")

    return {
        "title": "Bootciv Tech Tree",
        "url": "index.html",
        "content": _strip_html_tags(html_body),
    }


# ---------------------------------------------------------------------------
# T10: Search index generator
# ---------------------------------------------------------------------------

def generate_search_index(entries: list[dict]) -> str:
    """Build a JavaScript string: window.SEARCH_INDEX = <JSON>;"""
    import json as _json
    json_str = _json.dumps(entries, ensure_ascii=False)
    return f"window.SEARCH_INDEX = {json_str};"


# ---------------------------------------------------------------------------
# HTML tag stripping for search content
# ---------------------------------------------------------------------------

def _strip_html_tags(html: str) -> str:
    """Remove HTML tags and decode entities for plain text search content."""
    import html as _html
    text = re.sub(r"<[^>]+>", " ", html)
    text = _html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text
