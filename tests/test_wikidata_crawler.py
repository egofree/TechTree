#!/usr/bin/env python3
"""Tests for wikidata-crawler.py — mock-based, no internet access required.

Uses stdlib unittest with pytest runner.  Tests cover:
- Tokenization and scoring (pure functions)
- Search query building
- WikidataClient search_entities / get_entity_data (mock HTTP)
- Apply mode (mock file I/O)
- Stub mode (mock file I/O)
"""

import csv
import importlib.util
import json
import os
import sys
import tempfile
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

# ---------------------------------------------------------------------------
# Module loading — wikidata-crawler.py has a hyphen, so use importlib
# ---------------------------------------------------------------------------

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR = os.path.abspath(os.path.join(_THIS_DIR, "..", "scripts"))
sys.path.insert(0, _SCRIPTS_DIR)

_spec = importlib.util.spec_from_file_location(
    "wikidata_crawler",
    os.path.join(_SCRIPTS_DIR, "wikidata-crawler.py"),
)
wc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wc)

# Now import WikidataClient for client tests (lib/ is on sys.path)
from lib.wikidata_client import WikidataClient  # noqa: E402


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_args(**kwargs):
    """Create a simple namespace object for argparse args."""
    return type("Args", (), kwargs)()


# ===================================================================
# 1. Tokenization
# ===================================================================

class TestTokenize(unittest.TestCase):
    """Tests for tokenize()."""

    def test_tokenize_basic(self):
        self.assertEqual(wc.tokenize("Iron and Steel"), ["iron", "and", "steel"])

    def test_tokenize_empty(self):
        self.assertEqual(wc.tokenize(""), [])

    def test_tokenize_hyphenated(self):
        self.assertEqual(wc.tokenize("water-treatment"), ["water-treatment"])


# ===================================================================
# 2. Scoring
# ===================================================================

class TestScoreNameSimilarity(unittest.TestCase):
    """Tests for score_name_similarity()."""

    def test_exact_match(self):
        self.assertAlmostEqual(wc.score_name_similarity("Copper", "Copper"), 1.0)

    def test_partial_match(self):
        # {"iron","and","steel"} ∩ {"steel"} = 1 of 3
        self.assertAlmostEqual(
            wc.score_name_similarity("Iron and Steel", "steel"), 1 / 3, places=4
        )

    def test_no_match(self):
        self.assertAlmostEqual(wc.score_name_similarity("Glass", "Aluminum"), 0.0)


class TestScoreDescriptionOverlap(unittest.TestCase):
    """Tests for score_description_overlap()."""

    def test_overlap(self):
        # {"alloy","of","iron"} ∩ {"iron","carbon","alloy"} = 2 of 3
        score = wc.score_description_overlap("alloy of iron", "iron carbon alloy")
        self.assertGreater(score, 0.0)
        self.assertAlmostEqual(score, 2 / 3, places=4)

    def test_empty(self):
        self.assertAlmostEqual(wc.score_description_overlap("", "something"), 0.0)


class TestScoreTagMatch(unittest.TestCase):
    """Tests for score_tag_match()."""

    def test_tag_match(self):
        tags = {"material": ["iron"]}
        score = wc.score_tag_match(tags, "iron processing")
        self.assertGreater(score, 0.0)

    def test_tag_match_empty(self):
        self.assertAlmostEqual(wc.score_tag_match({}, "metal processing"), 0.0)


class TestComputeScore(unittest.TestCase):
    """Tests for compute_score() weight arithmetic."""

    def test_weights(self):
        candidate = {"label": "Iron", "description": "iron metal alloy"}
        name_sim = wc.score_name_similarity("Iron", candidate["label"])
        desc_sim = wc.score_description_overlap(
            "alloy of iron", candidate["description"]
        )
        tag_sim = wc.score_tag_match(
            {"material": ["iron"]}, candidate["description"]
        )

        score, reason = wc.compute_score(
            "Iron", "alloy of iron", {"material": ["iron"]}, candidate
        )
        expected = wc.W_NAME * name_sim + wc.W_DESC * desc_sim + wc.W_TAG * tag_sim
        self.assertAlmostEqual(score, round(expected, 4), places=3)
        self.assertIn("name=", reason)

    def test_no_match_components(self):
        score, reason = wc.compute_score(
            "Glass",
            "transparent material",
            {},
            {"label": "Aluminum", "description": "lightweight metal"},
        )
        self.assertAlmostEqual(score, 0.0)
        self.assertEqual(reason, "no_match_components")


# ===================================================================
# 3. Build search query
# ===================================================================

class TestBuildSearchQuery(unittest.TestCase):
    """Tests for build_search_query()."""

    def test_basic(self):
        query = wc.build_search_query({"name": "Iron and Steel"})
        self.assertIn("iron", query)
        self.assertIn("steel", query)

    def test_with_tags(self):
        entity = {"name": "Copper", "tags": {"material": ["metals"]}}
        query = wc.build_search_query(entity)
        self.assertIn("copper", query)
        self.assertIn("metals", query)

    def test_deduplicates(self):
        entity = {"name": "Steel", "tags": {"material": ["steel"]}}
        query = wc.build_search_query(entity)
        self.assertEqual(query.split().count("steel"), 1)


# ===================================================================
# 4. Client tests (mock HTTP)
# ===================================================================

class TestSearchEntities(unittest.TestCase):
    """Tests for WikidataClient.search_entities() via mock get_json."""

    @staticmethod
    def _make_client(return_value):
        mock_http = MagicMock()
        mock_http.get_json.return_value = return_value
        mock_limiter = MagicMock()
        return WikidataClient(client=mock_http, limiter=mock_limiter)

    def test_success(self):
        resp = {
            "search": [
                {"id": "Q131814", "label": "iron ore", "description": "natural mineral"},
                {"id": "Q535", "label": "steel", "description": "alloy of iron"},
            ]
        }
        client = self._make_client(resp)
        results = client.search_entities("iron ore")
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["qid"], "Q131814")
        self.assertEqual(results[0]["label"], "iron ore")
        self.assertEqual(results[1]["qid"], "Q535")

    def test_empty(self):
        client = self._make_client({"search": []})
        self.assertEqual(client.search_entities("nonexistent"), [])

    def test_none_response(self):
        client = self._make_client(None)
        self.assertEqual(client.search_entities("anything"), [])


class TestGetEntityData(unittest.TestCase):
    """Tests for WikidataClient.get_entity_data() via mock get_json."""

    @staticmethod
    def _make_client(return_value):
        mock_http = MagicMock()
        mock_http.get_json.return_value = return_value
        mock_limiter = MagicMock()
        return WikidataClient(client=mock_http, limiter=mock_limiter)

    def test_success(self):
        resp = {
            "entities": {
                "Q131814": {
                    "labels": {
                        "en": {"language": "en", "value": "iron ore"},
                        "es": {"language": "es", "value": "mena de hierro"},
                    },
                    "descriptions": {
                        "en": {
                            "language": "en",
                            "value": "natural mineral form of iron",
                        },
                        "es": {
                            "language": "es",
                            "value": "mineral natural de hierro",
                        },
                    },
                    "aliases": {
                        "en": [{"language": "en", "value": "haematite"}],
                    },
                }
            }
        }
        client = self._make_client(resp)
        data = client.get_entity_data("Q131814")
        self.assertIn("labels", data)
        self.assertEqual(data["labels"]["en"], "iron ore")
        self.assertEqual(data["labels"]["es"], "mena de hierro")
        self.assertEqual(data["descriptions"]["en"], "natural mineral form of iron")
        self.assertIn("haematite", data["aliases"]["en"])

    def test_missing(self):
        resp = {"entities": {"Q99999": {"missing": ""}}}
        client = self._make_client(resp)
        self.assertEqual(client.get_entity_data("Q99999"), {})

    def test_none_response(self):
        client = self._make_client(None)
        self.assertEqual(client.get_entity_data("Q99999"), {})


# ===================================================================
# 5. Apply tests (mock file I/O)
# ===================================================================

class TestRunApply(unittest.TestCase):
    """Tests for run_apply() with mocked load_entity / save_entity."""

    def _write_tsv(self, rows):
        """Write TSV rows (with header) to a temp file; return path."""
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".tsv", delete=False, encoding="utf-8", newline=""
        )
        writer = csv.DictWriter(tmp, fieldnames=wc.TSV_COLUMNS, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
        tmp.close()
        self.addCleanup(os.unlink, tmp.name)
        return tmp.name

    # ---- tests ----

    def test_apply_approved_row(self):
        tsv_path = self._write_tsv(
            [
                {
                    "entity_id": "metals.iron-steel",
                    "entity_name": "Iron and Steel",
                    "domain": "metals",
                    "candidate_qid": "Q131814",
                    "candidate_label": "iron ore",
                    "candidate_description": "natural mineral",
                    "confidence_score": "0.8500",
                    "match_reason": "name=1.00",
                    "status": "approved",
                }
            ]
        )
        mock_entity = {"id": "metals.iron-steel", "name": "Iron and Steel"}
        args = _make_args(tsv_path=tsv_path, dry_run=False)

        with patch.object(wc, "load_entity", return_value=mock_entity), patch.object(
            wc, "save_entity"
        ) as mock_save:
            wc.run_apply(args)
            mock_save.assert_called_once()
            saved = mock_save.call_args[0][0]
            self.assertEqual(saved["wikidataId"], "Q131814")

    def test_skips_rejected(self):
        tsv_path = self._write_tsv(
            [
                {
                    "entity_id": "metals.iron-steel",
                    "entity_name": "Iron and Steel",
                    "domain": "metals",
                    "candidate_qid": "Q131814",
                    "candidate_label": "iron ore",
                    "candidate_description": "",
                    "confidence_score": "0.5",
                    "match_reason": "",
                    "status": "rejected",
                }
            ]
        )
        args = _make_args(tsv_path=tsv_path, dry_run=False)

        with patch.object(wc, "load_entity"), patch.object(
            wc, "save_entity"
        ) as mock_save:
            wc.run_apply(args)
            mock_save.assert_not_called()

    def test_skips_pending(self):
        tsv_path = self._write_tsv(
            [
                {
                    "entity_id": "metals.iron-steel",
                    "entity_name": "Iron and Steel",
                    "domain": "metals",
                    "candidate_qid": "Q131814",
                    "candidate_label": "iron ore",
                    "candidate_description": "",
                    "confidence_score": "0.5",
                    "match_reason": "",
                    "status": "pending",
                }
            ]
        )
        args = _make_args(tsv_path=tsv_path, dry_run=False)

        with patch.object(wc, "load_entity"), patch.object(
            wc, "save_entity"
        ) as mock_save:
            wc.run_apply(args)
            mock_save.assert_not_called()

    def test_preserves_existing(self):
        tsv_path = self._write_tsv(
            [
                {
                    "entity_id": "metals.iron-steel",
                    "entity_name": "Iron and Steel",
                    "domain": "metals",
                    "candidate_qid": "Q999999",
                    "candidate_label": "iron ore",
                    "candidate_description": "",
                    "confidence_score": "0.9",
                    "match_reason": "",
                    "status": "approved",
                }
            ]
        )
        mock_entity = {
            "id": "metals.iron-steel",
            "name": "Iron and Steel",
            "wikidataId": "Q131814",
        }
        args = _make_args(tsv_path=tsv_path, dry_run=False)

        with patch.object(wc, "load_entity", return_value=mock_entity), patch.object(
            wc, "save_entity"
        ) as mock_save:
            wc.run_apply(args)
            mock_save.assert_not_called()

    def test_validates_qid(self):
        tsv_path = self._write_tsv(
            [
                {
                    "entity_id": "metals.iron-steel",
                    "entity_name": "Iron and Steel",
                    "domain": "metals",
                    "candidate_qid": "INVALID",
                    "candidate_label": "iron ore",
                    "candidate_description": "",
                    "confidence_score": "0.9",
                    "match_reason": "",
                    "status": "approved",
                }
            ]
        )
        args = _make_args(tsv_path=tsv_path, dry_run=False)

        with patch.object(wc, "load_entity"), patch.object(
            wc, "save_entity"
        ) as mock_save, patch("sys.stderr", new_callable=StringIO):
            wc.run_apply(args)
            mock_save.assert_not_called()


# ===================================================================
# 6. Stub tests (mock file I/O)
# ===================================================================

class TestRunStub(unittest.TestCase):
    """Tests for run_stub() with mocked load_entity / save_entity."""

    def setUp(self):
        self._orig_enrichment_path = wc.ENRICHMENT_PATH

    def tearDown(self):
        wc.ENRICHMENT_PATH = self._orig_enrichment_path

    def _make_cache(self, entities):
        """Write a temp enrichment cache; return path."""
        cache = {
            "version": "1.0",
            "generated_at": "2026-01-01T00:00:00Z",
            "languages": ["en", "es"],
            "entities": entities,
        }
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        )
        json.dump(cache, tmp)
        tmp.close()
        self.addCleanup(os.unlink, tmp.name)
        return tmp.name

    # ---- tests ----

    def test_fills_description(self):
        cache_path = self._make_cache(
            {
                "metals.iron-steel": {
                    "wikidataId": "Q131814",
                    "name": "Iron and Steel",
                    "descriptions": {"en": "alloy of iron and carbon"},
                    "labels": {"en": "Iron and Steel"},
                    "aliases": {},
                }
            }
        )
        wc.ENRICHMENT_PATH = cache_path
        mock_entity = {"id": "metals.iron-steel", "name": "Iron and Steel"}
        args = _make_args(entity="metals.iron-steel", dry_run=False)

        with patch.object(wc, "load_entity", return_value=mock_entity), patch.object(
            wc, "save_entity"
        ) as mock_save:
            wc.run_stub(args)
            mock_save.assert_called_once()
            saved = mock_save.call_args[0][0]
            self.assertEqual(saved["description"], "alloy of iron and carbon")

    def test_skips_existing_description(self):
        cache_path = self._make_cache(
            {
                "metals.iron-steel": {
                    "wikidataId": "Q131814",
                    "name": "Iron and Steel",
                    "descriptions": {"en": "alloy of iron and carbon"},
                    "labels": {},
                    "aliases": {},
                }
            }
        )
        wc.ENRICHMENT_PATH = cache_path
        mock_entity = {
            "id": "metals.iron-steel",
            "name": "Iron and Steel",
            "description": "existing description",
        }
        args = _make_args(entity="metals.iron-steel", dry_run=False)

        with patch.object(wc, "load_entity", return_value=mock_entity), patch.object(
            wc, "save_entity"
        ) as mock_save:
            wc.run_stub(args)
            mock_save.assert_not_called()

    def test_entity_not_in_cache(self):
        cache_path = self._make_cache({})
        wc.ENRICHMENT_PATH = cache_path
        args = _make_args(entity="metals.iron-steel", dry_run=False)

        with patch.object(wc, "load_entity"), patch.object(
            wc, "save_entity"
        ) as mock_save, patch("sys.stderr", new_callable=StringIO):
            wc.run_stub(args)
            mock_save.assert_not_called()


if __name__ == "__main__":
    unittest.main()
