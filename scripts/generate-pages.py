#!/usr/bin/env python3
"""Generate all HTML pages for the bootciv offline browser site.

Called by build-site.sh after directory structure is created.
Uses tt_data.py for entity/edge loading (per-entity JSON-LD files).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib.build_utils import (
    build_node_page_map,
    build_sidebar_tree,
    generate_capability_pages,
    generate_domain_pages,
    generate_home_page,
    generate_search_index,
    load_all_edges,
)
from lib.tt_data import load_all_entities
import yaml


def main():
    if len(sys.argv) < 6:
        print(
            "Usage: generate-pages.py <project_dir> <site_dir> "
            "<mermaid_dir> <verbose> <search_index_only>",
            file=sys.stderr,
        )
        sys.exit(1)

    project_dir = Path(sys.argv[1])
    site_dir = Path(sys.argv[2])
    mermaid_dir = Path(sys.argv[3])
    verbose = sys.argv[4] == "true"
    search_index_only = sys.argv[5] == "true"

    docs_dir = str(project_dir / "docs")
    checklist_file = project_dir / "data" / "checklist.yaml"

    nodes = load_all_entities()
    edges = load_all_edges()
    checklist = yaml.safe_load(checklist_file.read_text(encoding="utf-8"))

    page_map = build_node_page_map(docs_dir, nodes)
    sidebar_tree = build_sidebar_tree(nodes)

    if search_index_only:
        cap_entries = generate_capability_pages(
            docs_dir, str(site_dir), nodes, edges, page_map, sidebar_tree,
        )
        domain_entries = generate_domain_pages(
            str(site_dir), nodes, edges, page_map, sidebar_tree, str(mermaid_dir),
        )
        home_entry = generate_home_page(
            docs_dir, str(site_dir), nodes, edges, checklist,
            page_map, sidebar_tree, str(mermaid_dir),
        )
        all_entries = [home_entry] + domain_entries + cap_entries
        search_js = generate_search_index(all_entries)
        (site_dir / "assets" / "search-index.js").write_text(search_js, encoding="utf-8")
        print("  Generated search index")
        return

    cap_entries = generate_capability_pages(
        docs_dir, str(site_dir), nodes, edges, page_map, sidebar_tree,
    )
    domain_entries = generate_domain_pages(
        str(site_dir), nodes, edges, page_map, sidebar_tree, str(mermaid_dir),
    )
    home_entry = generate_home_page(
        docs_dir, str(site_dir), nodes, edges, checklist,
        page_map, sidebar_tree, str(mermaid_dir),
    )

    all_entries = [home_entry] + domain_entries + cap_entries
    search_js = generate_search_index(all_entries)
    (site_dir / "assets" / "search-index.js").write_text(search_js, encoding="utf-8")
    print("  Generated search index")


if __name__ == "__main__":
    main()
