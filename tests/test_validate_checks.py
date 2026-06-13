#!/usr/bin/env python3
"""Tests for quality audit checks (20-24) in scripts/validate.py.

Uses direct Validator instantiation (skipping __init__) with mock data.
Checks 21, 22, 24 are in-memory only — set attributes directly.
Checks 20, 23 are filesystem-dependent — use temp dirs + patch DOCS_DIR.
"""

import importlib.util
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# ---------------------------------------------------------------------------
# Module loading — validate.py is in scripts/, not a package
# ---------------------------------------------------------------------------

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", "scripts"))
sys.path.insert(0, _SCRIPTS_DIR)

_spec = importlib.util.spec_from_file_location(
    "validate", os.path.join(_SCRIPTS_DIR, "validate.py")
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

Validator = mod.Validator
DOCS_DIR_ATTR = "DOCS_DIR"  # global in validate module we patch for fs tests


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_validator(**kwargs):
    """Create a Validator skipping __init__, then set attributes from kwargs."""
    v = Validator.__new__(Validator)
    v.verbose = False
    v.skip = frozenset()
    v.results = []
    v.entities = {}
    v.entity_files = {}
    v.duplicate_entity_ids = []
    v.edges = []
    v.products = []
    v.schemas = {}
    for k, val in kwargs.items():
        setattr(v, k, val)
    return v


def _make_entity(eid, description="A meaningful description with more than 20 characters",
                 outputs=None, tags=None, timeline="Years 5-10", level="capability", **extra):
    """Build a minimal entity dict."""
    entity = {
        "id": eid,
        "description": description,
        "outputs": outputs if outputs is not None else [],
        "tags": tags if tags is not None else {},
        "timeline": timeline,
        "level": level,
    }
    entity.update(extra)
    return entity


def _make_edge(from_id, to_id, edge_type="tool", flow="primary"):
    """Build a minimal edge dict."""
    return {"from": from_id, "to": to_id, "edgeType": edge_type, "flow": flow}


def _make_product(pid, name="Product", source="test.capability"):
    """Build a minimal product dict."""
    return {"@id": pid, "name": name, "source": source}


# ===================================================================
# Check 20: check_entity_doc_sync (filesystem-dependent)
# ===================================================================

class TestCheckEntityDocSync(unittest.TestCase):
    """Tests for Validator.check_entity_doc_sync()."""

    def setUp(self):
        self.maxDiff = None
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _write_doc(self, domain, name, content="# Title\n"):
        """Write a .md file under tmpdir/docs/{domain}/{name}.md."""
        domain_dir = os.path.join(self.tmpdir, domain)
        os.makedirs(domain_dir, exist_ok=True)
        with open(os.path.join(domain_dir, f"{name}.md"), "w") as f:
            f.write(content)

    def _validator_with_docs(self, entities=None, edges=None, products=None):
        """Create validator and patch DOCS_DIR to tmpdir."""
        v = _make_validator(
            entities=entities or {},
            edges=edges or [],
            products=products or [],
        )
        return v

    def test_entity_without_doc_flagged(self):
        """Entity exists in data but no corresponding .md file → flagged."""
        v = self._validator_with_docs(
            entities={"test.capability": _make_entity("test.capability")}
        )
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_entity_doc_sync()
        self.assertTrue(
            any("entity without doc" in e for e in errors),
            f"Expected 'entity without doc' error, got: {errors}",
        )

    def test_doc_without_entity_flagged(self):
        """.md file exists but no corresponding entity → flagged."""
        self._write_doc("test", "capability")
        v = self._validator_with_docs(entities={})
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_entity_doc_sync()
        self.assertTrue(
            any("doc without entity" in e for e in errors),
            f"Expected 'doc without entity' error, got: {errors}",
        )

    def test_synced_entity_doc_passes(self):
        """Entity AND doc both exist → no error."""
        self._write_doc("test", "capability")
        v = self._validator_with_docs(
            entities={"test.capability": _make_entity("test.capability")}
        )
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_entity_doc_sync()
        self.assertEqual(errors, [], f"Expected no errors, got: {errors}")

    def test_domain_level_entity_skipped(self):
        """Domain-level entities are skipped (no doc needed)."""
        v = self._validator_with_docs(
            entities={"test": _make_entity("test", level="domain")}
        )
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_entity_doc_sync()
        self.assertEqual(errors, [], f"Expected no errors for domain entity, got: {errors}")

    def test_index_md_ignored(self):
        """index.md files should be ignored (not treated as entity docs)."""
        # Write index.md only — should NOT trigger "doc without entity"
        index_dir = os.path.join(self.tmpdir, "test")
        os.makedirs(index_dir, exist_ok=True)
        with open(os.path.join(index_dir, "index.md"), "w") as f:
            f.write("# Test Domain\n")
        v = self._validator_with_docs(entities={})
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_entity_doc_sync()
        self.assertEqual(errors, [], f"Expected no errors for index.md, got: {errors}")


# ===================================================================
# Check 21: check_edge_completeness (in-memory only)
# ===================================================================

class TestCheckEdgeCompleteness(unittest.TestCase):
    """Tests for Validator.check_edge_completeness()."""

    def setUp(self):
        self.maxDiff = None

    def test_orphan_entity_detected(self):
        """Entity with no edges at all → flagged as orphan."""
        v = _make_validator(
            entities={"test.orphan": _make_entity("test.orphan")},
            edges=[],
            products=[],
        )
        errors = v.check_edge_completeness()
        self.assertTrue(
            any("orphan entity" in e for e in errors),
            f"Expected orphan error, got: {errors}",
        )

    def test_orphan_excludes_foundations(self):
        """Entity named 'foundations' should NOT be flagged as orphan."""
        v = _make_validator(
            entities={"foundations": _make_entity("foundations")},
            edges=[],
            products=[],
        )
        errors = v.check_edge_completeness()
        orphan_errors = [e for e in errors if "orphan" in e]
        self.assertEqual(
            orphan_errors, [],
            f"Expected no orphan error for foundations, got: {orphan_errors}",
        )

    def test_unused_output_detected(self):
        """Entity outputs a product name that has no matching product @id → flagged."""
        v = _make_validator(
            entities={
                "test.producer": _make_entity("test.producer", outputs=["unknown-product"]),
            },
            edges=[_make_edge("test.consumer", "test.producer")],
            products=[],  # no products → output is unused
        )
        errors = v.check_edge_completeness()
        self.assertTrue(
            any("unused output" in e for e in errors),
            f"Expected unused output error, got: {errors}",
        )

    def test_connected_entity_passes(self):
        """Entity with edges → should NOT be flagged as orphan."""
        v = _make_validator(
            entities={
                "test.capability": _make_entity(
                    "test.capability", outputs=["product1"]
                ),
            },
            edges=[_make_edge("test.capability", "test.other")],
            products=[_make_product("product1")],
        )
        errors = v.check_edge_completeness()
        orphan_errors = [e for e in errors if "orphan" in e]
        self.assertEqual(
            orphan_errors, [],
            f"Expected no orphan error for connected entity, got: {orphan_errors}",
        )

    def test_output_matching_product_passes(self):
        """Entity output that matches a product @id → NOT flagged as unused."""
        v = _make_validator(
            entities={
                "test.producer": _make_entity("test.producer", outputs=["widget"]),
            },
            edges=[_make_edge("test.consumer", "test.producer")],
            products=[_make_product("widget")],
        )
        errors = v.check_edge_completeness()
        unused_errors = [e for e in errors if "unused output" in e]
        self.assertEqual(
            unused_errors, [],
            f"Expected no unused output error, got: {unused_errors}",
        )


# ===================================================================
# Check 22: check_content_quality (in-memory only)
# ===================================================================

class TestCheckContentQuality(unittest.TestCase):
    """Tests for Validator.check_content_quality()."""

    def setUp(self):
        self.maxDiff = None

    def test_short_description_flagged(self):
        """Entity with description < 20 chars → flagged."""
        v = _make_validator(
            entities={"test.short": _make_entity("test.short", description="Too short")},
        )
        errors = v.check_content_quality()
        self.assertTrue(
            any("description too short" in e for e in errors),
            f"Expected short description error, got: {errors}",
        )

    def test_placeholder_text_flagged(self):
        """Entity with TODO/TBD in description → flagged."""
        for placeholder in ("TODO: fill in", "TBD", "FIXME later"):
            v = _make_validator(
                entities={
                    "test.placeholder": _make_entity(
                        "test.placeholder",
                        description=f"A description saying {placeholder} and enough chars",
                    ),
                },
            )
            errors = v.check_content_quality()
            self.assertTrue(
                any("placeholder" in e for e in errors),
                f"Expected placeholder error for '{placeholder}', got: {errors}",
            )

    def test_empty_outputs_flagged(self):
        """Entity with empty outputs array → flagged."""
        v = _make_validator(
            entities={
                "test.empty": _make_entity(
                    "test.empty", outputs=[]
                ),
            },
        )
        errors = v.check_content_quality()
        self.assertTrue(
            any("empty outputs" in e for e in errors),
            f"Expected empty outputs error, got: {errors}",
        )

    def test_good_entity_passes(self):
        """Entity with proper description, outputs, timeline → no errors."""
        v = _make_validator(
            entities={
                "test.good": _make_entity(
                    "test.good",
                    description="A perfectly fine description of a capability",
                    outputs=["widget-a"],
                    timeline="Years 5-10",
                ),
            },
        )
        errors = v.check_content_quality()
        self.assertEqual(errors, [], f"Expected no errors for good entity, got: {errors}")

    def test_no_outputs_not_flagged(self):
        """Entity with outputs=None (key absent) → NOT flagged as empty outputs."""
        v = _make_validator(
            entities={
                "test.nooutputs": {
                    "id": "test.nooutputs",
                    "description": "Entity with no outputs key at all",
                    "tags": {},
                    "timeline": "Years 5-10",
                },
            },
        )
        errors = v.check_content_quality()
        empty_output_errors = [e for e in errors if "empty outputs" in e]
        self.assertEqual(
            empty_output_errors, [],
            f"Expected no empty outputs error when outputs key absent, got: {empty_output_errors}",
        )

    def test_unusual_timeline_flagged(self):
        """Entity with non-matching timeline format → flagged."""
        v = _make_validator(
            entities={
                "test.badtime": _make_entity(
                    "test.badtime",
                    description="A description with enough characters to pass",
                    timeline="whenever we feel like it",
                ),
            },
        )
        errors = v.check_content_quality()
        self.assertTrue(
            any("unusual timeline" in e for e in errors),
            f"Expected unusual timeline error, got: {errors}",
        )


# ===================================================================
# Check 23: check_blockquote_metadata_consistency (filesystem-dependent)
# ===================================================================

class TestCheckBlockquoteMetadataConsistency(unittest.TestCase):
    """Tests for Validator.check_blockquote_metadata_consistency()."""

    def setUp(self):
        self.maxDiff = None
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def _write_doc(self, domain, name, content):
        """Write a .md file under tmpdir/{domain}/{name}.md."""
        domain_dir = os.path.join(self.tmpdir, domain)
        os.makedirs(domain_dir, exist_ok=True)
        with open(os.path.join(domain_dir, f"{name}.md"), "w") as f:
            f.write(content)

    def test_doc_claims_dep_without_edge(self):
        """Doc says 'Dependencies: foo.bar' but no edge from entity to foo.bar → flagged."""
        self._write_doc("test", "capability", (
            "# Capability\n"
            "\n"
            "> **Dependencies**: `test.other`\n"
        ))
        v = _make_validator(
            entities={"test.capability": _make_entity("test.capability")},
            edges=[],  # no edge from test.capability → test.other
        )
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_blockquote_metadata_consistency()
        self.assertTrue(
            any("doc claims dep on" in e for e in errors),
            f"Expected 'doc claims dep on' error, got: {errors}",
        )

    def test_doc_claims_enable_without_edge(self):
        """Doc says 'Enables: baz.qux' but no edge from baz.qux to entity → flagged."""
        self._write_doc("test", "capability", (
            "# Capability\n"
            "\n"
            "> **Enables**: `baz.qux`\n"
        ))
        v = _make_validator(
            entities={"test.capability": _make_entity("test.capability")},
            edges=[],  # no edge at all
        )
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_blockquote_metadata_consistency()
        self.assertTrue(
            any("doc claims enables" in e for e in errors),
            f"Expected 'doc claims enables' error, got: {errors}",
        )

    def test_consistent_metadata_passes(self):
        """Doc Dependencies/Enables match edges exactly → no errors."""
        self._write_doc("test", "capability", (
            "# Capability\n"
            "\n"
            "> **Dependencies**: `test.producer`\n"
            "\n"
            "> **Enables**: `test.consumer`\n"
        ))
        v = _make_validator(
            entities={
                "test.capability": _make_entity("test.capability"),
                "test.producer": _make_entity("test.producer"),
                "test.consumer": _make_entity("test.consumer"),
            },
            edges=[
                # capability depends on producer: edge from capability to producer
                _make_edge("test.capability", "test.producer"),
                # consumer depends on capability: edge from consumer to capability
                _make_edge("test.consumer", "test.capability"),
            ],
        )
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_blockquote_metadata_consistency()
        self.assertEqual(errors, [], f"Expected no errors for consistent metadata, got: {errors}")

    def test_no_docs_dir_passes(self):
        """If docs dir doesn't exist → returns empty errors (no crash)."""
        nonexistent = os.path.join(self.tmpdir, "nonexistent_docs")
        v = _make_validator(entities={}, edges=[])
        with patch.object(mod, DOCS_DIR_ATTR, Path(nonexistent)):
            errors = v.check_blockquote_metadata_consistency()
        self.assertEqual(errors, [])

    def test_index_md_skipped(self):
        """index.md files should be skipped (not checked for metadata)."""
        domain_dir = os.path.join(self.tmpdir, "test")
        os.makedirs(domain_dir, exist_ok=True)
        with open(os.path.join(domain_dir, "index.md"), "w") as f:
            f.write("# Test\n\n> **Dependencies**: `bogus.ref`\n")
        v = _make_validator(
            entities={"test": _make_entity("test", level="domain")},
            edges=[],
        )
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_blockquote_metadata_consistency()
        dep_errors = [e for e in errors if "doc claims dep" in e]
        self.assertEqual(
            dep_errors, [],
            f"Expected no dep errors from index.md, got: {dep_errors}",
        )

    def test_doc_for_unknown_entity_skipped(self):
        """Doc file for entity not in entities dict → skipped (not checked)."""
        self._write_doc("test", "phantom", (
            "# Phantom\n"
            "\n"
            "> **Dependencies**: `bogus.ref`\n"
        ))
        v = _make_validator(entities={}, edges=[])
        with patch.object(mod, DOCS_DIR_ATTR, Path(self.tmpdir)):
            errors = v.check_blockquote_metadata_consistency()
        self.assertEqual(errors, [])


# ===================================================================
# Check 24: check_lifecycle_edge_consistency (in-memory only)
# ===================================================================

class TestCheckLifecycleEdgeConsistency(unittest.TestCase):
    """Tests for Validator.check_lifecycle_edge_consistency()."""

    def setUp(self):
        self.maxDiff = None

    def test_lifecycle_without_circular_edge(self):
        """Entity with lifecycle tag ['recyclable'] but no circular edges → flagged."""
        v = _make_validator(
            entities={
                "test.recycler": _make_entity(
                    "test.recycler",
                    tags={"lifecycle": ["recyclable"]},
                ),
            },
            edges=[_make_edge("test.consumer", "test.recycler", flow="primary")],
        )
        errors = v.check_lifecycle_edge_consistency()
        self.assertTrue(
            any("lifecycle tag" in e and "no circular economy edges" in e for e in errors),
            f"Expected lifecycle inconsistency error, got: {errors}",
        )

    def test_lifecycle_with_circular_edge_passes(self):
        """Entity with lifecycle tag ['recyclable'] AND a recycling-loop edge → passes."""
        v = _make_validator(
            entities={
                "test.recycler": _make_entity(
                    "test.recycler",
                    tags={"lifecycle": ["recyclable"]},
                ),
                "test.consumer": _make_entity("test.consumer"),
            },
            edges=[_make_edge("test.consumer", "test.recycler", flow="recycling-loop")],
        )
        errors = v.check_lifecycle_edge_consistency()
        self.assertEqual(
            errors, [],
            f"Expected no errors for recyclable entity with recycling-loop edge, got: {errors}",
        )

    def test_no_lifecycle_tag_passes(self):
        """Entity without lifecycle tags → no errors (even with no edges)."""
        v = _make_validator(
            entities={
                "test.normal": _make_entity("test.normal"),
            },
            edges=[],
        )
        errors = v.check_lifecycle_edge_consistency()
        self.assertEqual(
            errors, [],
            f"Expected no errors for entity without lifecycle tags, got: {errors}",
        )

    def test_all_circular_tags_detected(self):
        """Each circular tag without a matching edge should be flagged."""
        circular_tags = ["recyclable", "waste-source", "recycled-feedstock", "closed-loop"]
        for tag in circular_tags:
            v = _make_validator(
                entities={
                    f"test.{tag}": _make_entity(
                        f"test.{tag}",
                        tags={"lifecycle": [tag]},
                    ),
                },
                edges=[],
            )
            errors = v.check_lifecycle_edge_consistency()
            self.assertTrue(
                any(f"lifecycle tag '{tag}'" in e for e in errors),
                f"Expected error for tag '{tag}', got: {errors}",
            )

    def test_all_circular_flows_satisfy(self):
        """Each circular flow type should satisfy a lifecycle tag."""
        circular_flows = ["byproduct-reuse", "waste-recovery", "recycling-loop"]
        for flow in circular_flows:
            v = _make_validator(
                entities={
                    "test.recycler": _make_entity(
                        "test.recycler",
                        tags={"lifecycle": ["recyclable"]},
                    ),
                    "test.other": _make_entity("test.other"),
                },
                edges=[_make_edge("test.other", "test.recycler", flow=flow)],
            )
            errors = v.check_lifecycle_edge_consistency()
            self.assertEqual(
                errors, [],
                f"Expected no errors with flow '{flow}', got: {errors}",
            )

    def test_lifecycle_tags_not_list_skipped(self):
        """Entity where lifecycle is not a list → skipped gracefully."""
        v = _make_validator(
            entities={
                "test.bad": _make_entity(
                    "test.bad",
                    tags={"lifecycle": "recyclable"},  # string, not list
                ),
            },
            edges=[],
        )
        errors = v.check_lifecycle_edge_consistency()
        self.assertEqual(
            errors, [],
            f"Expected no crash when lifecycle is not a list, got: {errors}",
        )


if __name__ == "__main__":
    unittest.main()
