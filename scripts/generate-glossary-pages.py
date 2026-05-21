#!/usr/bin/env python3
"""Generate glossary HTML pages for the bootciv offline browser site.

Reads data/glossary.json and optional docs/glossary/*.md files.
Writes site/glossary/index.html and site/glossary/{slug}.html.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib.build_utils import (
    build_node_page_map,
    build_sidebar_tree,
    render_markdown,
)
from lib.templates import render_page, render_sidebar


# ---------------------------------------------------------------------------
# Glossary badge helpers
# ---------------------------------------------------------------------------

_TIER_BADGES = {
    "critical": ("★", "badge badge--critical"),
    "important": ("●", "badge badge--important"),
    "supporting": ("○", "badge badge--supporting"),
}

_TYPE_ICONS = {
    "noun": "📦",
    "verb": "▶",
    "process": "⚙",
    "material": "🧱",
    "equipment": "🔧",
}


def _tier_badge(tier: str) -> str:
    icon, css = _TIER_BADGES.get(tier, ("?", "badge"))
    return f'<span class="{css}" title="{tier}">{icon}</span>'


def _type_badge(term_type: str) -> str:
    icon = _TYPE_ICONS.get(term_type, "?")
    return f'<span class="badge badge--type badge--type-{term_type}" title="{term_type}">{icon} {term_type}</span>'


# ---------------------------------------------------------------------------
# Individual glossary article pages
# ---------------------------------------------------------------------------

def generate_glossary_articles(
    project_dir: Path,
    site_dir: Path,
    glossary_data: dict,
    nodes_json: dict,
    edges_json: list[dict],
    page_map: dict[str, str],
    sidebar_tree: list[dict],
    dry_run: bool = False,
    verbose: bool = False,
) -> list[dict]:
    """Generate individual HTML pages for ALL glossary terms.

    Terms with .md files get full article pages; others get stub pages
    with definition and metadata.
    """
    glossary_md_dir = project_dir / "docs" / "glossary"

    search_entries = []
    count = 0

    for term_data in sorted(glossary_data["terms"], key=lambda t: t["slug"]):
        slug = term_data["slug"]
        term_name = term_data.get("term", slug.replace("-", " ").title())

        md_path = glossary_md_dir / f"{slug}.md"

        if md_path.exists():
            # Full article page (has .md file)
            md_content = md_path.read_text(encoding="utf-8")
            html_body = render_markdown(md_content)
        else:
            # Stub page (no .md file)
            definition = term_data.get("definition", "")
            html_body = f"<p>{definition}</p>"

        # Build metadata section from glossary.json
        meta_parts = []

        if term_data.get("tier"):
            meta_parts.append(
                f'<div class="glossary-meta">Tier: {_tier_badge(term_data["tier"])} '
                f'<span>{term_data["tier"]}</span></div>'
            )

        if term_data.get("type"):
            meta_parts.append(
                f'<div class="glossary-meta">Type: {_type_badge(term_data["type"])}</div>'
            )

        domains = term_data.get("domains", [])
        if domains:
            domain_links = []
            for d in domains:
                domain_href = f"../docs/{d}/index.html"
                domain_links.append(f'<a href="{domain_href}">{d}</a>')
            meta_parts.append(
                f'<div class="glossary-meta">Domains: {", ".join(domain_links)}</div>'
            )

        source_articles = term_data.get("source_articles", [])
        if source_articles:
            article_links = []
            for node_id in source_articles:
                if node_id in page_map:
                    href = f"../{page_map[node_id]}"
                    article_links.append(f'<a href="{href}">{node_id}</a>')
                else:
                    article_links.append(f'<span>{node_id}</span>')
            meta_parts.append(
                f'<div class="glossary-meta">Source articles: {", ".join(article_links)}</div>'
            )

        see_also = term_data.get("see_also", [])
        if see_also:
            see_links = [f'<a href="{s}.html">{s}</a>' for s in see_also]
            meta_parts.append(
                f'<div class="glossary-meta">See also: {", ".join(see_links)}</div>'
            )

        aliases = term_data.get("aliases", [])
        if aliases:
            meta_parts.append(
                f'<div class="glossary-meta">Aliases: {", ".join(aliases)}</div>'
            )

        back_link = '<div class="glossary-back-link"><a href="index.html">← Back to Glossary</a></div>'
        content = back_link + "\n".join(meta_parts) + "\n" + html_body

        current_path = f"glossary/{slug}.html"
        sidebar_html = render_sidebar(
            sidebar_tree, current_path, link_prefix="../", page_map=page_map,
        )

        page_html = render_page(
            title=term_name,
            content=content,
            sidebar_html=sidebar_html,
            current_path=current_path,
            asset_prefix="../",
        )

        if not dry_run:
            out_path = site_dir / "glossary" / f"{slug}.html"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(page_html, encoding="utf-8")

        count += 1
        search_entries.append({
            "title": term_name,
            "url": current_path,
            "content": html_body,
        })

    if verbose or count > 0:
        print(f"  Generated {count} glossary article pages")
    return search_entries


# ---------------------------------------------------------------------------
# Glossary index page
# ---------------------------------------------------------------------------

def generate_glossary_index(
    site_dir: Path,
    glossary_data: dict,
    nodes_json: dict,
    edges_json: list[dict],
    page_map: dict[str, str],
    sidebar_tree: list[dict],
    dry_run: bool = False,
    verbose: bool = False,
) -> dict:
    """Generate site/glossary/index.html — alphabetical listing with filters."""
    terms = glossary_data["terms"]

    # Sort alphabetically by term name
    terms_sorted = sorted(terms, key=lambda t: t["term"].lower())

    # Group by first letter
    letter_groups: dict[str, list[dict]] = defaultdict(list)
    for t in terms_sorted:
        letter = t["term"][0].upper()
        letter_groups[letter].append(t)

    # Collect unique domains and types for filter controls
    all_domains = sorted(set(d for t in terms for d in t.get("domains", [])))
    all_types = sorted(set(t.get("type", "") for t in terms if t.get("type")))

    # Tier counts
    tier_counts: dict[str, int] = defaultdict(int)
    for t in terms:
        tier_counts[t.get("tier", "")] += 1

    # Type counts
    type_counts: dict[str, int] = defaultdict(int)
    for t in terms:
        typ = t.get("type", "")
        if typ:
            type_counts[typ] += 1

    # Build page content
    parts: list[str] = []

    total = len(terms)
    tier_count_parts = []
    for k, v in sorted(tier_counts.items()):
        tier_count_parts.append(f'{_tier_badge(k)} <span>{v} {k}</span>')
    type_count_parts = []
    for k, v in sorted(type_counts.items()):
        type_count_parts.append(f'<span class="glossary-type-count">{k}: {v}</span>')
    parts.append(
        f'<div class="glossary-stats">Total terms: <strong>{total}</strong> '
        f'{"".join(tier_count_parts)} {"".join(type_count_parts)}</div>'
    )

    # Filter controls
    parts.append('<div class="glossary-filters">')

    # Tier filter buttons
    parts.append('<div class="glossary-filter-group">')
    parts.append('<span class="glossary-filter-label">Tier:</span>')
    for tier in ("critical", "important", "supporting"):
        parts.append(
            f'<button class="glossary-filter-btn" data-filter="tier" data-value="{tier}" '
            f'onclick="toggleFilter(this)">{_tier_badge(tier)} {tier.title()}</button>'
        )
    parts.append(
        '<button class="glossary-filter-btn glossary-filter-btn--clear" '
        'data-filter="tier" data-value="" '
        'onclick="clearFilterGroup(this, \'tier\')">All</button>'
    )
    parts.append('</div>')

    # Type filter
    parts.append('<div class="glossary-filter-group">')
    parts.append('<span class="glossary-filter-label">Type:</span>')
    for t in all_types:
        parts.append(
            f'<button class="glossary-filter-btn" data-filter="type" data-value="{t}" '
            f'onclick="toggleFilter(this)">{t.title()}</button>'
        )
    parts.append(
        '<button class="glossary-filter-btn glossary-filter-btn--clear" '
        'data-filter="type" data-value="" '
        'onclick="clearFilterGroup(this, \'type\')">All</button>'
    )
    parts.append('</div>')

    # Domain filter dropdown
    parts.append('<div class="glossary-filter-group">')
    parts.append('<span class="glossary-filter-label">Domain:</span>')
    parts.append(
        '<select class="glossary-filter-select" data-filter="domain" '
        'onchange="filterByDomain(this)">'
    )
    parts.append('<option value="">All domains</option>')
    for d in all_domains:
        parts.append(f'<option value="{d}">{d.title()}</option>')
    parts.append('</select>')
    parts.append('</div>')

    parts.append('</div>')  # close glossary-filters

    # A-Z quick nav
    parts.append('<div class="glossary-alpha-nav">')
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if letter in letter_groups:
            parts.append(f'<a href="#letter-{letter}" class="glossary-alpha-link">{letter}</a>')
        else:
            parts.append(f'<span class="glossary-alpha-link glossary-alpha-link--empty">{letter}</span>')
    parts.append('</div>')

    # Term listings grouped by letter
    parts.append('<div class="glossary-terms">')
    for letter in sorted(letter_groups.keys()):
        parts.append(f'<div class="glossary-letter-group" id="letter-{letter}">')
        parts.append(f'<h2 class="glossary-letter-heading">{letter}</h2>')
        for t in letter_groups[letter]:
            tier_badge = _tier_badge(t.get("tier", ""))
            type_badge = _type_badge(t.get("type", ""))
            slug = t["slug"]
            definition = t.get("definition", "")
            term_domains = t.get("domains", [])

            # Data attributes for filtering
            data_attrs = (
                f' data-tier="{t.get("tier", "")}"'
                f' data-type="{t.get("type", "")}"'
                f' data-domains="{",".join(term_domains)}"'
            )

            parts.append(f'<div class="glossary-term-entry"{data_attrs}>')

            if t.get("created"):
                parts.append(
                    f'<div class="glossary-term-name">'
                    f'<a href="{slug}.html">{t["term"]}</a> '
                    f'{tier_badge} {type_badge}</div>'
                )
            else:
                parts.append(
                    f'<div class="glossary-term-name">'
                    f'{t["term"]} {tier_badge} {type_badge}</div>'
                )

            parts.append(f'<div class="glossary-term-definition">{definition}</div>')

            # Domain links
            if term_domains:
                domain_links = []
                for d in term_domains:
                    domain_href = f"../docs/{d}/index.html"
                    domain_links.append(f'<a href="{domain_href}">{d}</a>')
                parts.append(
                    f'<div class="glossary-term-domains">{", ".join(domain_links)}</div>'
                )

            # Source article links
            source_articles = t.get("source_articles", [])
            if source_articles:
                article_links = []
                for node_id in source_articles:
                    if node_id in page_map:
                        href = f"../{page_map[node_id]}"
                        article_links.append(f'<a href="{href}">{node_id}</a>')
                    else:
                        article_links.append(node_id)
                parts.append(
                    f'<div class="glossary-term-sources">Sources: {", ".join(article_links)}</div>'
                )

            parts.append('</div>')  # close glossary-term-entry

        parts.append('</div>')  # close glossary-letter-group

    parts.append('</div>')  # close glossary-terms

    content = "\n".join(parts)

    # Client-side filter script
    filter_script = """
<script>
function toggleFilter(btn) {
    var filterGroup = btn.getAttribute('data-filter');
    var value = btn.getAttribute('data-value');
    var wasActive = btn.classList.contains('glossary-filter-btn--active');
    var siblings = btn.parentElement.querySelectorAll('[data-filter="' + filterGroup + '"]:not(.glossary-filter-btn--clear)');
    for (var i = 0; i < siblings.length; i++) {
        siblings[i].classList.remove('glossary-filter-btn--active');
    }
    if (!wasActive) {
        btn.classList.add('glossary-filter-btn--active');
    }
    applyFilters();
}

function clearFilterGroup(btn, filterGroup) {
    var siblings = btn.parentElement.querySelectorAll('[data-filter="' + filterGroup + '"]:not(.glossary-filter-btn--clear)');
    for (var i = 0; i < siblings.length; i++) {
        siblings[i].classList.remove('glossary-filter-btn--active');
    }
    applyFilters();
}

function filterByDomain(select) {
    applyFilters();
}

function applyFilters() {
    var activeTier = getActiveFilter('tier');
    var activeType = getActiveFilter('type');
    var domainSelect = document.querySelector('[data-filter="domain"]');
    var activeDomain = domainSelect ? domainSelect.value : '';
    var entries = document.querySelectorAll('.glossary-term-entry');
    var visibleLetters = {};
    for (var i = 0; i < entries.length; i++) {
        var entry = entries[i];
        var show = true;
        if (activeTier && entry.getAttribute('data-tier') !== activeTier) show = false;
        if (activeType && entry.getAttribute('data-type') !== activeType) show = false;
        if (activeDomain && entry.getAttribute('data-domains').indexOf(activeDomain) === -1) show = false;
        entry.style.display = show ? '' : 'none';
        if (show) {
            var group = entry.closest('.glossary-letter-group');
            if (group) visibleLetters[group.id] = true;
        }
    }
    var groups = document.querySelectorAll('.glossary-letter-group');
    for (var j = 0; j < groups.length; j++) {
        groups[j].style.display = visibleLetters[groups[j].id] ? '' : 'none';
    }
}

function getActiveFilter(filterName) {
    var active = document.querySelector('.glossary-filter-btn--active[data-filter="' + filterName + '"]');
    return active ? active.getAttribute('data-value') : '';
}
</script>
"""

    # Append filter script to content (render_page wraps in main)
    content += filter_script

    current_path = "glossary/index.html"
    sidebar_html = render_sidebar(
        sidebar_tree, current_path, link_prefix="../", page_map=page_map,
    )

    page_html = render_page(
        title="Glossary",
        content=content,
        sidebar_html=sidebar_html,
        current_path=current_path,
        asset_prefix="../",
    )

    if not dry_run:
        out_path = site_dir / "glossary" / "index.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page_html, encoding="utf-8")

    if verbose:
        print(f"  Generated glossary index ({len(terms)} terms)")
    else:
        print(f"  Generated glossary index ({len(terms)} terms)")

    return {
        "title": "Glossary",
        "url": current_path,
        "content": content,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 4:
        print(
            "Usage: generate-glossary-pages.py <project_dir> <site_dir> <verbose> [--dry-run]",
            file=sys.stderr,
        )
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    site_dir = Path(sys.argv[2])
    verbose = sys.argv[3] == "true"
    dry_run = "--dry-run" in sys.argv

    glossary_file = project_dir / "data" / "glossary.json"
    if not glossary_file.exists():
        print(f"Error: {glossary_file} not found", file=sys.stderr)
        sys.exit(1)

    glossary_data = json.loads(glossary_file.read_text(encoding="utf-8"))

    # Load node/edge data for sidebar and cross-references
    nodes_file = project_dir / "data" / "nodes.json"
    edges_file = project_dir / "data" / "edges.json"

    if not nodes_file.exists() or not edges_file.exists():
        print("Error: nodes.json and edges.json required for sidebar", file=sys.stderr)
        sys.exit(1)

    nodes_json = json.loads(nodes_file.read_text(encoding="utf-8"))
    edges_json = json.loads(edges_file.read_text(encoding="utf-8"))["edges"]

    docs_dir = str(project_dir / "docs")
    page_map = build_node_page_map(docs_dir, nodes_json)
    sidebar_tree = build_sidebar_tree(nodes_json)

    generate_glossary_articles(
        project_dir, site_dir, glossary_data,
        nodes_json, edges_json, page_map, sidebar_tree,
        dry_run=dry_run, verbose=verbose,
    )

    generate_glossary_index(
        site_dir, glossary_data,
        nodes_json, edges_json, page_map, sidebar_tree,
        dry_run=dry_run, verbose=verbose,
    )


if __name__ == "__main__":
    main()
