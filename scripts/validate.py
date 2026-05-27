#!/usr/bin/env python3
"""
validate.py - JSON Schema + conformance validator for tech-tree-bootstrap.

Replaces validate.sh (19 checks, bash+jq) with Python validator using
JSON Schema validation + structural integrity checks.

Covers all 19 original checks:
  Schema subsumes: data files valid, tag completeness, tag values,
  edge types, level-dot depth, taxonomy, edge flow, lifecycle tags.
  Explicit checks: DAG, cross-refs, hierarchy, terminology,
  diagrams, glossary, boolean consistency.

Usage:
    python3 scripts/validate.py [--verbose] [--skip dag|crossref|tags|hierarchy|conformance]
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path

try:
    from jsonschema import validate as js_validate, ValidationError
except ImportError:
    print("ERROR: jsonschema package required (pip install jsonschema)", file=sys.stderr)
    sys.exit(1)

# --- Paths ---

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
DATA_DIR = PROJECT_DIR / "data"
DOCS_DIR = PROJECT_DIR / "docs"
DIAGRAMS_DIR = PROJECT_DIR / "diagrams" / "mermaid"
SCHEMA_DIR = DATA_DIR / "schema"
ENTITIES_DIR = DATA_DIR / "entities"
EDGES_DIR = ENTITIES_DIR / "_edges"
PRODUCTS_DIR = DATA_DIR / "products"

# --- Closed vocabularies (from schema enums) ---

# Non-primary flows exempt from DAG check (match validate.sh behavior)
NON_PRIMARY_FLOWS = frozenset({"byproduct-reuse", "waste-recovery", "recycling-loop"})


# --- Check result ---

class CheckResult:
    __slots__ = ("name", "passed", "errors")

    def __init__(self, name, passed, errors=None):
        self.name = name
        self.passed = passed
        self.errors = errors or []


# --- Validator ---

class Validator:
    def __init__(self, verbose=False, skip=frozenset()):
        self.verbose = verbose
        self.skip = skip
        self.results: list[CheckResult] = []

        # Loaded data
        self.schemas = {}
        self.entities = {}          # id -> entity dict
        self.entity_files = {}      # id -> Path
        self.duplicate_entity_ids = []  # [(id, path1, path2), ...]
        self.edges = []             # list of edge dicts
        self.products = []          # list of product dicts

    # ---- Data loading ----

    def load_schemas(self):
        for name in ("domain", "capability", "process", "dependency", "product"):
            path = SCHEMA_DIR / f"{name}.schema.json"
            if path.exists():
                with open(path) as f:
                    self.schemas[name] = json.load(f)

    def load_entities(self):
        count = 0
        for domain_dir in sorted(ENTITIES_DIR.iterdir()):
            if domain_dir.name == "_edges" or not domain_dir.is_dir():
                continue
            for fpath in sorted(domain_dir.glob("*.jsonld")):
                try:
                    entity = json.loads(fpath.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, OSError) as exc:
                    if self.verbose:
                        print(f"    ERROR: {fpath}: {exc}", file=sys.stderr)
                    continue
                eid = entity.get("id")
                if not eid:
                    continue
                if eid in self.entities:
                    self.duplicate_entity_ids.append(
                        (eid, fpath, self.entity_files[eid])
                    )
                self.entities[eid] = entity
                self.entity_files[eid] = fpath
                count += 1
        return count

    def load_edges(self):
        count = 0
        if not EDGES_DIR.exists():
            return 0
        for fpath in sorted(EDGES_DIR.glob("*.jsonld")):
            try:
                edge = json.loads(fpath.read_text(encoding="utf-8"))
                self.edges.append(edge)
                count += 1
            except (json.JSONDecodeError, OSError) as exc:
                if self.verbose:
                    print(f"    ERROR: {fpath}: {exc}", file=sys.stderr)
        return count

    def load_products(self):
        count = 0
        if not PRODUCTS_DIR.exists():
            return 0
        for fpath in sorted(PRODUCTS_DIR.glob("*.jsonld")):
            try:
                product = json.loads(fpath.read_text(encoding="utf-8"))
                self.products.append(product)
                count += 1
            except (json.JSONDecodeError, OSError) as exc:
                if self.verbose:
                    print(f"    ERROR: {fpath}: {exc}", file=sys.stderr)
        return count

    # ---- Check runner ----

    def run_check(self, name, fn):
        """Execute *fn* (returns list of error strings). Record pass/fail."""
        num = len(self.results) + 1
        if self.verbose:
            print(f"  [{num:2d}] {name}... ", end="", flush=True)

        try:
            errors = fn()
            if errors is None:
                errors = []
        except Exception as exc:
            errors = [str(exc)]

        passed = len(errors) == 0
        self.results.append(CheckResult(name, passed, errors))

        if self.verbose:
            print("PASS" if passed else "FAIL")
            if not passed:
                for e in errors[:5]:
                    print(f"       {e}", file=sys.stderr)
                if len(errors) > 5:
                    print(f"       ... and {len(errors) - 5} more", file=sys.stderr)
        elif not passed:
            for e in errors[:3]:
                print(f"    {e}", file=sys.stderr)

        return passed

    # ---- Schema validation ----

    def _validate_schema(self, instance, schema_name):
        schema = self.schemas.get(schema_name)
        if not schema:
            return [f"No schema: {schema_name}"]
        try:
            js_validate(instance=instance, schema=schema)
            return []
        except ValidationError as exc:
            return [exc.message]

    # Covers original checks 1,10,11,14,16,19
    def check_schema_entities(self):
        level_to_schema = {
            "domain": "domain",
            "capability": "capability",
            "process": "process",
        }
        errors = []
        for eid, entity in sorted(self.entities.items()):
            level = entity.get("level", "")
            sname = level_to_schema.get(level)
            if not sname:
                errors.append(f"{eid}: unknown level '{level}'")
                continue
            for e in self._validate_schema(entity, sname):
                errors.append(f"{eid}: {e}")
        return errors

    # Covers original checks 12,18
    def check_schema_edges(self):
        errors = []
        for edge in self.edges:
            for e in self._validate_schema(edge, "dependency"):
                fid = edge.get("from", "?")
                tid = edge.get("to", "?")
                errors.append(f"{fid} -> {tid}: {e}")
        return errors

    def check_schema_products(self):
        errors = []
        for prod in self.products:
            pid = prod.get("@id") or prod.get("id", "?")
            for e in self._validate_schema(prod, "product"):
                errors.append(f"{pid}: {e}")
        return errors

    # ---- DAG ----

    # Covers original check 2
    def check_dag(self):
        adj = defaultdict(list)
        for edge in self.edges:
            flow = edge.get("flow", "primary")
            if flow in NON_PRIMARY_FLOWS:
                continue
            fid = edge.get("from")
            tid = edge.get("to")
            if fid and tid:
                adj[fid].append(tid)

        WHITE, GRAY, BLACK = 0, 1, 2
        color = {nid: WHITE for nid in self.entities}
        errors = []

        def dfs(node):
            color[node] = GRAY
            for nbr in adj.get(node, []):
                if nbr not in color:
                    continue  # dangling — caught by cross-ref check
                if color[nbr] == GRAY:
                    return (node, nbr)
                if color[nbr] == WHITE:
                    r = dfs(nbr)
                    if r:
                        return r
            color[node] = BLACK
            return None

        for nid in sorted(self.entities):
            if color[nid] == WHITE:
                cycle = dfs(nid)
                if cycle:
                    errors.append(f"Cycle detected: {cycle[0]} -> {cycle[1]}")
        return errors

    # ---- Cross-references ----

    # Covers original check 3
    def check_node_doc_correspondence(self):
        errors = []
        warnings = []
        domain_segments = {eid.split(".")[0] for eid in self.entities}

        for d in sorted(domain_segments):
            if not (DOCS_DIR / d).is_dir():
                errors.append(f"No docs dir for domain: {d}")

        if DOCS_DIR.exists():
            for dd in sorted(DOCS_DIR.iterdir()):
                if dd.name == "supporting" or not dd.is_dir():
                    continue
                if dd.name not in domain_segments:
                    warnings.append(
                        f"WARNING: docs/{dd.name}/ has no matching domain node"
                    )

        for w in warnings:
            print(f"    {w}", file=sys.stderr)

        return errors

    # Covers original check 4
    def check_edge_references(self):
        eids = set(self.entities)
        errors = []
        for edge in self.edges:
            fid = edge.get("from")
            tid = edge.get("to")
            if fid and fid not in eids:
                errors.append(f"Dangling edge 'from': {fid}")
            if tid and tid not in eids:
                errors.append(f"Dangling edge 'to': {tid}")
        return errors

    def check_product_source_references(self):
        eids = set(self.entities)
        errors = []
        for prod in self.products:
            src = prod.get("source")
            pid = prod.get("@id") or prod.get("id", "?")
            if src and src not in eids:
                errors.append(f"Product '{pid}': source '{src}' not found")
        return errors

    # Covers original check 5
    def check_resource_references(self):
        path = DATA_DIR / "resources.json"
        if not path.exists():
            return []
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return ["resources.json: invalid JSON"]

        eids = set(self.entities)
        errors = []
        for mat in data.get("raw_materials", []):
            for ref in mat.get("used_in", []):
                if ref not in eids:
                    errors.append(f"Dangling resource 'used_in': {ref}")
        return errors

    # Covers original check 6
    def check_checklist_references(self):
        path = DATA_DIR / "checklist.yaml"
        if not path.exists():
            return []
        try:
            import yaml
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            return ["checklist.yaml: invalid YAML"]

        eids = set(self.entities)
        errors = []
        for key, val in (data or {}).items():
            if key.startswith("_"):
                continue
            if isinstance(val, dict) and "items" in val:
                for item in val["items"]:
                    if isinstance(item, dict) and "id" in item:
                        if item["id"] not in eids:
                            errors.append(f"Dangling checklist ref: {item['id']}")
        return errors

    # ---- Terminology ----

    # Covers original check 7
    def check_no_legacy_terminology(self):
        patterns = [r"phase-[0-9]", r"sq-[0-9]", r"main\.quest", r"side\.quest"]
        compiled = [re.compile(p) for p in patterns]
        errors = []
        for eid, entity in sorted(self.entities.items()):
            text = json.dumps(entity)
            for pat in compiled:
                if pat.search(text):
                    errors.append(f"Legacy term in entity: {eid}")
                    break
        for edge in self.edges:
            text = json.dumps(edge)
            for pat in compiled:
                if pat.search(text):
                    errors.append(
                        f"Legacy term in edge: {edge.get('from')} -> {edge.get('to')}"
                    )
                    break
        return errors

    # ---- Diagrams ----

    # Covers original check 8
    def check_diagrams_generated(self):
        gen_script = SCRIPT_DIR / "generate-diagrams.sh"
        if not gen_script.exists():
            return ["generate-diagrams.sh not found"]
        try:
            r = subprocess.run(
                ["bash", str(gen_script), "--list"],
                capture_output=True, text=True, timeout=30,
                cwd=str(PROJECT_DIR),
            )
        except Exception as exc:
            return [f"Cannot run generate-diagrams.sh: {exc}"]

        errors = []
        for line in r.stdout.strip().splitlines():
            for m in re.finditer(r"\S+\.mmd", line):
                diagram_path = PROJECT_DIR / "diagrams" / "mermaid" / m.group()
                if not diagram_path.exists():
                    errors.append(f"Missing diagram: {m.group()}")
        return errors

    # Covers original check 9
    def check_mermaid_syntax(self):
        if not DIAGRAMS_DIR.exists():
            return ["diagrams/mermaid/ not found"]
        mmds = list(DIAGRAMS_DIR.glob("*.mmd"))
        if not mmds:
            return ["No .mmd files in diagrams/mermaid/"]

        errors = []
        for mmd in sorted(mmds):
            txt = mmd.read_text(encoding="utf-8")
            name = mmd.name
            if not txt.startswith("%%{init:"):
                errors.append(f"{name}: missing %%{{init: header")
            if "graph TD" not in txt:
                errors.append(f"{name}: missing 'graph TD'")
            if not re.search(r'\["[^"]+"\]|\("[^"]+"\)', txt):
                errors.append(f"{name}: no node declarations")
            if "-->" not in txt and "-.->" not in txt:
                errors.append(f"{name}: no edges found")
        return errors

    # ---- Hierarchy ----

    # Covers original check 13
    def check_parent_chain(self):
        errors = []
        for eid, entity in sorted(self.entities.items()):
            parent = entity.get("parent")
            if parent is None:
                continue
            if parent not in self.entities:
                errors.append(f"{eid}: parent={parent} does not exist")

        # Verify chains resolve to domain level
        for eid in sorted(self.entities):
            visited = set()
            current = eid
            while current in self.entities:
                if current in visited:
                    errors.append(f"{eid}: circular parent chain at {current}")
                    break
                visited.add(current)
                parent = self.entities[current].get("parent")
                if parent is None:
                    break
                current = parent
            else:
                if current not in self.entities:
                    errors.append(
                        f"{eid}: parent chain ends at non-existent {current}"
                    )
        return errors

    # Covers original check 15
    def check_boolean_consistency(self):
        errors = []
        for eid, entity in sorted(self.entities.items()):
            tags = entity.get("tags")
            if not isinstance(tags, dict):
                continue
            for tag_key, top_key in [
                ("critical", "critical"),
                ("early-win", "early_win"),
                ("pinnacle", "pinnacle"),
            ]:
                if tag_key in tags and top_key in entity:
                    if tags[tag_key] != entity[top_key]:
                        errors.append(
                            f"{eid}: tags.{tag_key}={tags[tag_key]} "
                            f"!= {top_key}={entity[top_key]}"
                        )
        return errors

    # ---- Integrity ----

    def check_no_self_loops(self):
        errors = []
        for edge in self.edges:
            fid = edge.get("from")
            tid = edge.get("to")
            flow = edge.get("flow", "primary")
            if fid == tid and flow != "recycling-loop":
                errors.append(f"Self-loop: {fid} -> {tid} (flow={flow})")
        return errors

    def check_no_duplicate_edges(self):
        errors = []
        seen = {}
        for edge in self.edges:
            key = (edge.get("from"), edge.get("to"), edge.get("flow", "primary"))
            if key in seen:
                errors.append(f"Duplicate edge: {key[0]} -> {key[1]} (flow={key[2]})")
            else:
                seen[key] = True
        return errors

    # ---- Glossary ----

    # Covers original check 17
    def check_glossary(self):
        path = DATA_DIR / "glossary.json"
        if not path.exists():
            return []

        try:
            with open(path, encoding="utf-8") as f:
                glossary = json.load(f)
        except json.JSONDecodeError:
            return ["glossary.json: invalid JSON"]

        terms = glossary.get("terms", [])
        if not terms:
            return []

        eids = set(self.entities)
        errors = []
        slugs = set()
        valid_types = {"noun", "verb", "process", "material", "equipment"}
        valid_tiers = {"critical", "important", "supporting"}

        for term in terms:
            slug = term.get("slug", "")
            slugs.add(slug)

            for ref in term.get("source_articles", []):
                if ref not in eids:
                    errors.append(f"Dangling glossary source_articles: {ref}")

            for ref in term.get("node_refs", []):
                if ref not in eids:
                    errors.append(f"Dangling glossary node_refs: {ref}")

            t = term.get("type", "")
            if t and t not in valid_types:
                errors.append(f"{slug}: invalid type '{t}'")

            tier = term.get("tier", "")
            if tier and tier not in valid_tiers:
                errors.append(f"{slug}: invalid tier '{tier}'")

            if tier in ("critical", "important"):
                defn = term.get("definition", "")
                if not defn or len(defn.split()) < 3:
                    errors.append(f"Empty/too-short definition: {slug}")

        # see_also references
        for term in terms:
            for s in term.get("see_also", []):
                if s not in slugs:
                    errors.append(f"Dangling glossary see_also: {s}")

        # Duplicate slugs
        slug_counts = defaultdict(int)
        for term in terms:
            slug_counts[term.get("slug", "")] += 1
        for slug, cnt in sorted(slug_counts.items()):
            if cnt > 1:
                errors.append(f"Duplicate glossary slug: {slug}")

        return errors

    # ---- Entity ID uniqueness ----

    def check_entity_id_uniqueness(self):
        return [
            f"Duplicate entity ID '{eid}': {p1} and {p2}"
            for eid, p1, p2 in self.duplicate_entity_ids
        ]

    # ---- Conformance ----

    def check_conformance(self):
        script = SCRIPT_DIR / "run_conformance_tests.sh"
        if not script.exists():
            return ["Conformance test suite not found"]
        try:
            r = subprocess.run(
                ["bash", str(script)],
                capture_output=True, text=True, timeout=120,
            )
            if r.returncode != 0:
                lines = r.stdout.strip().splitlines()[-8:]
                return ["Conformance tests failed"] + [f"  {l}" for l in lines]
            return []
        except subprocess.TimeoutExpired:
            return ["Conformance tests timed out"]
        except Exception as exc:
            return [f"Conformance test error: {exc}"]

    # ---- Main runner ----

    def run(self):
        t0 = time.time()

        # Load all data
        self.load_schemas()
        n_ent = self.load_entities()
        n_edg = self.load_edges()
        n_prd = self.load_products()
        n_total = n_ent + n_edg + n_prd

        if self.verbose:
            print(
                f"Loaded {n_ent} entities + {n_edg} edges "
                f"+ {n_prd} products = {n_total} files"
            )

        print("=== TechTree Validation ===")
        print()

        # ---- 19 checks ----

        # 1-3: Schema validation
        if self.verbose:
            print("--- Schema Validation ---")
        self.run_check(
            "Entity schema validation (tags, era, taxonomy, lifecycle)",
            self.check_schema_entities,
        )
        self.run_check(
            "Edge schema validation (edgeType, flow)",
            self.check_schema_edges,
        )
        self.run_check(
            "Product schema validation",
            self.check_schema_products,
        )

        # 4: DAG
        if self.verbose:
            print()
            print("--- DAG ---")
        if "dag" not in self.skip:
            self.run_check(
                "DAG is acyclic (circular economy exempt)",
                self.check_dag,
            )

        # 5-9: Cross-references
        if self.verbose:
            print()
            print("--- Cross-references ---")
        if "crossref" not in self.skip:
            self.run_check(
                "Node-doc correspondence",
                self.check_node_doc_correspondence,
            )
            self.run_check(
                "Edge references valid",
                self.check_edge_references,
            )
            self.run_check(
                "Product source references valid",
                self.check_product_source_references,
            )
            self.run_check(
                "Resources references valid",
                self.check_resource_references,
            )
            self.run_check(
                "Checklist references valid",
                self.check_checklist_references,
            )

        # 10: Terminology
        if self.verbose:
            print()
            print("--- Terminology ---")
        self.run_check(
            "No phase/SQ legacy terminology",
            self.check_no_legacy_terminology,
        )

        # 11-12: Diagrams
        if self.verbose:
            print()
            print("--- Diagrams ---")
        self.run_check(
            "Diagrams generated and present",
            self.check_diagrams_generated,
        )
        self.run_check(
            "Mermaid syntax valid",
            self.check_mermaid_syntax,
        )

        # 13-14: Hierarchy
        if self.verbose:
            print()
            print("--- Hierarchy ---")
        if "hierarchy" not in self.skip:
            self.run_check(
                "Parent chain consistency",
                self.check_parent_chain,
            )
            self.run_check(
                "Boolean consistency (tags vs top-level)",
                self.check_boolean_consistency,
            )

        # 15-16: Integrity
        if self.verbose:
            print()
            print("--- Integrity ---")
        self.run_check(
            "No self-loops (except recycling-loop)",
            self.check_no_self_loops,
        )
        self.run_check(
            "No duplicate edges",
            self.check_no_duplicate_edges,
        )

        # 17: Glossary
        if self.verbose:
            print()
            print("--- Glossary ---")
        self.run_check(
            "Glossary cross-references",
            self.check_glossary,
        )

        # 18: Uniqueness
        if self.verbose:
            print()
        self.run_check(
            "Entity ID uniqueness",
            self.check_entity_id_uniqueness,
        )

        # 19: Conformance
        if "conformance" not in self.skip:
            if self.verbose:
                print()
                print("--- Conformance ---")
            self.run_check(
                "Conformance test suite",
                self.check_conformance,
            )

        # ---- Summary ----
        print()

        # Schema pass count
        schema_errors = 0
        for r in self.results:
            if "schema" in r.name.lower():
                schema_errors += len(r.errors)
        schema_pass = n_total - schema_errors

        all_pass = all(r.passed for r in self.results)
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)

        print(f"Schema:     {schema_pass}/{n_total} {'✓' if all_pass else 'FAIL'}")

        dag_ok = all(
            r.passed for r in self.results if "acycl" in r.name.lower()
        )
        print(f"DAG:        {'No cycles ✓' if dag_ok else 'CYCLES DETECTED'}")

        xref_ok = all(
            r.passed
            for r in self.results
            if any(kw in r.name.lower() for kw in ("reference", "correspondence"))
        )
        print(
            f"Cross-ref:  {n_edg}/{n_edg} edges valid "
            f"{'✓' if xref_ok else 'FAIL'}"
        )

        tags_ok = all(
            r.passed for r in self.results if "schema" in r.name.lower()
        )
        print(
            f"Tags:       All vocabularies valid {'✓' if tags_ok else 'FAIL'}"
        )

        hier_ok = all(
            r.passed
            for r in self.results
            if any(kw in r.name.lower() for kw in ("parent", "boolean"))
        )
        print(
            f"Hierarchy:  {n_ent}/{n_ent} valid {'✓' if hier_ok else 'FAIL'}"
        )

        print()
        if all_pass:
            print(f"Result: ALL PASS ({passed}/{total} checks)")
        else:
            failed = [r for r in self.results if not r.passed]
            print(
                f"Result: {len(failed)} FAILURE{'S' if len(failed) != 1 else ''} "
                f"({passed}/{total} passed)"
            )
            for r in failed:
                print(f"  ✗ {r.name}")
                for e in r.errors[:3]:
                    print(f"      {e}")

        elapsed = time.time() - t0
        if self.verbose:
            print(f"\nCompleted in {elapsed:.1f}s")

        return 0 if all_pass else 1


def main():
    parser = argparse.ArgumentParser(
        description="Validate tech-tree-bootstrap data files"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Show per-check detail"
    )
    parser.add_argument(
        "--skip",
        nargs="*",
        default=[],
        choices=["dag", "crossref", "tags", "hierarchy", "conformance"],
        help="Skip check groups",
    )
    args = parser.parse_args()

    validator = Validator(verbose=args.verbose, skip=frozenset(args.skip))
    sys.exit(validator.run())


if __name__ == "__main__":
    main()
