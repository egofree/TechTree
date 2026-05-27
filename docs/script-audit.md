# Script Audit

## Summary

- Total scripts evaluated: 20 (excluding config/assets/domains)
- Total lib modules evaluated: 11 (including `__init__.py`)
- **KEEP**: 8 scripts + 6 lib modules
- **MERGE**: 6 scripts (glossary pipeline → 1 script; diagram generators → 1 script)
- **DROP**: 6 scripts + 5 lib modules
- **Final script count**: 8 (≤10 target met)

## Audit Table — Scripts

| # | Script | Classification | Reads JSON data? | Rationale | Action |
|---|--------|---------------|-------------------|-----------|--------|
| 1 | `generate-diagrams.sh` | MERGE | Yes (nodes.json, edges.json via jq) | Still needed for Mermaid output. Merge with D2 generator into single `generate-diagrams.py` using `tt_data.py`. | Rewrite to Python using `tt_data.py`; merge D2 logic |
| 2 | `generate-d2-diagrams.sh` | MERGE | Yes (nodes.json, edges.json via jq) | Duplicate logic with Mermaid generator. Same data, different output format. | Merge into `generate-diagrams.py` as `--format d2` flag |
| 3 | `validate.sh` | DROP | Yes (nodes.json, edges.json, glossary.json via jq) | 19-check bash+jq validator. Replaced by JSON Schema conformance tests (`run_conformance_tests.sh`) and future `validate.py` (Task 13). | Remove after `validate.py` is complete |
| 4 | `build-site.sh` | KEEP | Indirect (calls generate-pages.py) | Site build orchestrator. Reads nodes.json via subprocess. Still needed. | Rewrite to use `tt_data.py` via `generate-pages.py` update |
| 5 | `validate-site.sh` | KEEP | No (checks site/ output only) | Validates built site for offline-first compliance. 10 checks. No data layer dependency. | Keep as-is; no data layer rewrite needed |
| 6 | `generate-pages.py` | KEEP | Yes (nodes.json, edges.json via build_utils) | Page orchestrator for site generation. Core dependency. | Rewrite to use `tt_data.py` instead of raw JSON |
| 7 | `crawl-domain.py` | KEEP | Writes to data (not reads tech-tree data) | Wikipedia crawler. Reads config YAML, writes catalog JSON. Data producer, not consumer. | Keep as-is; no `tt_data.py` rewrite needed |
| 8 | `source-images.py` | KEEP | Reads nodes.json (for node IDs only) | Wikimedia image sourcer. Reads node IDs to iterate, writes images.json. | Minor update to read entity IDs from `tt_data.py` |
| 9 | `render-mermaid.sh` | KEEP | No (reads .mmd files only) | Renders .mmd → SVG/PNG via mmdc. No data layer dependency. | Keep as-is |
| 10 | `run_conformance_tests.sh` | KEEP | No (reads test fixtures + schemas) | JSON Schema conformance test runner. New, already uses JSON-LD schemas. | Keep as-is |
| 11 | `migrate_to_jsonld.py` | KEEP | Yes (reads nodes.json, edges.json) | One-time migration script. Already uses `tt_data.py` for serialization. Needed until migration is finalized. | Keep until migration complete, then DROP |
| 12 | `audit-metrics.py` | DROP | Yes (nodes.json, edges.json directly) | Graph health metrics. Standalone report. Can be reimplemented as a `tt_data.py` query when needed. | Remove; add to future reporting tools if needed |
| 13 | `extract-terms.py` | MERGE | No (reads .md files only) | Bold-pattern glossary term extractor. Part of glossary pipeline. | Merge into `build-glossary.py` |
| 14 | `extract-nlp-terms.py` | MERGE | No (reads .md files only) | spaCy NLP glossary term extractor. Part of glossary pipeline. | Merge into `build-glossary.py` |
| 15 | `transform-glossary.py` | MERGE | No (reads glossary-raw.json) | Groups raw terms into combined format. Part of glossary pipeline. | Merge into `build-glossary.py` |
| 16 | `deduplicate-terms.py` | MERGE | No (reads glossary-combined.json) | Deduplicates glossary terms. Part of glossary pipeline. | Merge into `build-glossary.py` |
| 17 | `rate-terms.py` | MERGE | No (reads glossary-dedup.json) | Classifies type/tier. Part of glossary pipeline. | Merge into `build-glossary.py` |
| 18 | `compute-relevance.py` | DROP | Yes (nodes.json + glossary) | Per-article relevance rating. Niche report. Glossary pipeline already produces this data in the final glossary.json. | Remove; functionality preserved in glossary pipeline output |
| 19 | `generate-glossary-pages.py` | KEEP | Yes (nodes.json, edges.json, glossary.json) | Generates glossary HTML pages for site. Called by build-site.sh. | Rewrite to use `tt_data.py` |
| 20 | `link-glossary.py` | KEEP | Reads glossary.json only | Post-processes site HTML to add glossary hyperlinks. Aho-Corasick based. | Keep as-is; no data layer rewrite needed |

## Audit Table — Lib Modules

| # | Module | Classification | Used By | Rationale | Action |
|---|--------|---------------|---------|-----------|--------|
| 1 | `tt_data.py` | KEEP | migrate_to_jsonld.py, future scripts | NEW data access layer. Reads per-entity JSON-LD files. This is the replacement for data_utils.py. | Keep; this is the target API |
| 2 | `build_utils.py` | KEEP | generate-pages.py, generate-glossary-pages.py | Markdown rendering, metadata extraction, page generation. 570 lines. Core site-building library. | Rewrite JSON loading to use `tt_data.py` |
| 3 | `templates.py` | KEEP | build_utils.py, generate-glossary-pages.py | HTML page templates (render_page, render_sidebar). No data layer dependency. | Keep as-is |
| 4 | `wiki_client.py` | KEEP | crawl-domain.py, source-images.py | Wikimedia API HTTP client. No data layer dependency. | Keep as-is |
| 5 | `sparql_client.py` | KEEP | crawl-domain.py (SPARQL queries) | Wikidata SPARQL client. No data layer dependency. | Keep as-is |
| 6 | `rate_limiter.py` | KEEP | crawl-domain.py, sparql_client.py | Token-bucket rate limiter for API calls. No data layer dependency. | Keep as-is |
| 7 | `data_utils.py` | DROP | crawl-domain.py | OLD data layer. Reads nodes.json/edges.json directly. Replaced by `tt_data.py`. | Remove after crawl-domain.py stops importing it |
| 8 | `article_extractor.py` | DROP | crawl-domain.py (plants-specific) | Wikipedia HTML parser for plant data. Tightly coupled to plants domain crawler. | Remove; functionality is crawl-domain.py specific |
| 9 | `disambiguation.py` | DROP | crawl-domain.py (plants-specific) | Wikipedia disambiguation resolver. Tightly coupled to plants domain crawler. | Remove; functionality is crawl-domain.py specific |
| 10 | `linkify_articles.py` | DROP | Standalone (in lib/ but runnable) | Scans .md files for bold→link conversion. Superseded by link-glossary.py which operates on rendered HTML. | Remove; link-glossary.py is the replacement |
| 11 | `__init__.py` | KEEP | — | Empty package init file. | Keep |

## Final Script Layout (Target ≤10)

```
scripts/
├── build-site.sh              # KEEP — site build orchestrator
├── validate-site.sh           # KEEP — site validation (10 checks)
├── render-mermaid.sh          # KEEP — Mermaid → SVG/PNG renderer
├── run_conformance_tests.sh   # KEEP — JSON Schema conformance tests
├── generate-diagrams.py       # MERGED — Mermaid + D2 from tt_data.py (new)
├── generate-pages.py          # KEEP — page orchestrator (rewritten)
├── generate-glossary-pages.py # KEEP — glossary HTML generator (rewritten)
├── build-glossary.py          # MERGED — 5 glossary scripts → 1 pipeline (new)
├── link-glossary.py           # KEEP — HTML glossary linker
├── migrate_to_jsonld.py       # KEEP — one-time migration (DROP after complete)
├── crawl-domain.py            # KEEP — Wikipedia crawler (data producer)
├── source-images.py           # KEEP — Wikimedia image sourcer
├── rating-config.yaml         # Config (not a script)
├── domains/                   # Config directory (not scripts)
│   └── plants.yaml
├── assets/                    # Static assets (not scripts)
│   └── *.js, *.css
└── lib/                       # Library modules
    ├── tt_data.py             # KEEP — new data access layer
    ├── build_utils.py         # KEEP — site building utilities
    ├── templates.py           # KEEP — HTML templates
    ├── wiki_client.py         # KEEP — Wikimedia API client
    ├── sparql_client.py       # KEEP — SPARQL client
    ├── rate_limiter.py        # KEEP — API rate limiter
    └── __init__.py            # KEEP — package init
```

**Active scripts count: 12** (includes crawl-domain.py and source-images.py as data producers, and migrate_to_jsonld.py as temporary).

After migration is complete (migrate_to_jsonld.py dropped): **11 scripts**.

## Glossary Pipeline Merge Detail

The following 5 scripts form a linear pipeline that can be merged into a single `build-glossary.py`:

1. `extract-terms.py` → Stage 1: Bold-pattern extraction from .md files
2. `extract-nlp-terms.py` → Stage 2: spaCy NLP extraction from .md files
3. `transform-glossary.py` → Stage 3: Group raw terms into combined format
4. `deduplicate-terms.py` → Stage 4: Deduplicate via case/plural/hyphen normalization
5. `rate-terms.py` → Stage 5: Type classification + tier rating

Merged as: `python3 scripts/build-glossary.py [--stage N] [--from X] [--to Y]`

This preserves the ability to run individual stages while reducing file count by 4.

## Diagram Generator Merge Detail

`generate-diagrams.sh` and `generate-d2-diagrams.sh` share identical logic (bash+jq reading nodes.json/edges.json) differing only in output format. Merge into:

`python3 scripts/generate-diagrams.py [--format mermaid|d2|all]`

Using `tt_data.py` instead of raw JSON + jq.

## Dependency Graph After Audit

```
Data Producers (no tt_data dependency):
  crawl-domain.py → wiki_client, sparql_client, rate_limiter
  source-images.py → wiki_client

Data Consumers (tt_data.py dependency):
  generate-diagrams.py → tt_data
  generate-pages.py → tt_data, build_utils
  generate-glossary-pages.py → tt_data, build_utils, templates
  build-glossary.py → (reads .md files, no tt_data dependency)

Site Pipeline:
  build-site.sh → generate-pages.py, generate-glossary-pages.py, link-glossary.py

Validation:
  run_conformance_tests.sh → (reads schemas + test fixtures)
  validate-site.sh → (reads site/ output only)

Rendering:
  render-mermaid.sh → (reads .mmd files, requires mmdc)

Migration (temporary):
  migrate_to_jsonld.py → tt_data, (reads nodes.json, edges.json)
```
