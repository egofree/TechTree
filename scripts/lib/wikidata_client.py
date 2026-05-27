"""Wikidata REST API client for entity search and data retrieval.

Stdlib-only. Uses WikiClient for HTTP transport and RateLimiter for
throttling. Wraps the Wikidata MediaWiki API (wbsearchentities,
wbgetentities) to search for entities by label and fetch multilingual
labels, descriptions, and aliases.

Usage:
    from lib.wikidata_client import WikidataClient

    client = WikidataClient()

    # Search for entities
    results = client.search_entities("iron ore")
    for r in results:
        print(r["qid"], r["label"], r["description"])

    # Get multilingual data for a specific entity
    data = client.get_entity_data("Q131814")
    print(data["labels"]["en"])
"""

from lib.wiki_client import WikiClient
from lib.rate_limiter import RateLimiter


# --- Constants ---

WIKIDATA_API_URL = "https://www.wikidata.org/w/api.php"

DEFAULT_USER_AGENT = (
    "BootCivWikidataBot/1.0 "
    "(https://github.com/bootciv; educational CC0 project)"
)

DEFAULT_LANGUAGES = ["en", "es", "fr", "de", "zh"]


# --- Client ---

class WikidataClient:
    """Wikidata REST API client with rate limiting.

    Composes WikiClient for HTTP transport and RateLimiter for
    request throttling. Provides entity search and multilingual
    data retrieval via the Wikidata MediaWiki API.

    Args:
        client: WikiClient instance (created if not provided).
        limiter: RateLimiter instance (created if not provided).
    """

    def __init__(self, client=None, limiter=None):
        self._client = client or WikiClient(
            base_url=WIKIDATA_API_URL,
            user_agent=DEFAULT_USER_AGENT,
        )
        self._limiter = limiter or RateLimiter(requests_per_second=1)

    def search_entities(self, query, language="en", limit=3):
        """Search Wikidata for entities matching a text query.

        Calls the wbsearchentities API to find items whose labels
        or aliases match the given search string.

        Args:
            query: Search string (e.g. "iron ore", "silicon").
            language: Language code for search and results (default "en").
            limit: Maximum number of results to return (default 3).

        Returns:
            List of dicts, each with:
                qid: Wikidata entity ID (e.g. "Q131814")
                label: Entity label in the requested language
                description: Short description, or empty string if none
            Returns empty list on failure or no results.
        """
        self._limiter.wait()

        data = self._client.get_json(params={
            "action": "wbsearchentities",
            "search": query,
            "language": language,
            "limit": limit,
            "type": "item",
            "format": "json",
        })

        if data is None:
            return []

        try:
            results = data.get("search", [])
        except (AttributeError, TypeError):
            return []

        output = []
        for item in results:
            output.append({
                "qid": item.get("id", ""),
                "label": item.get("label", ""),
                "description": item.get("description", ""),
            })

        return output

    def get_entity_data(self, qid, languages=None):
        """Fetch multilingual labels, descriptions, and aliases for an entity.

        Calls the wbgetentities API to retrieve structured data for
        one Wikidata item in multiple languages.

        Args:
            qid: Wikidata entity ID (e.g. "Q131814").
            languages: List of language codes to fetch (default:
                ["en", "es", "fr", "de", "zh"]).

        Returns:
            Dict with structure:
                {
                    "qid": "Q131814",
                    "labels": {"en": "iron ore", "es": "mena de hierro", ...},
                    "descriptions": {"en": "natural mineral...", ...},
                    "aliases": {"en": ["haematite", ...], ...}
                }
            Returns empty dict if entity not found or on failure.
        """
        if languages is None:
            languages = DEFAULT_LANGUAGES

        self._limiter.wait()

        data = self._client.get_json(params={
            "action": "wbgetentities",
            "ids": qid,
            "props": "labels|descriptions|aliases",
            "languages": "|".join(languages),
            "format": "json",
        })

        if data is None:
            return {}

        try:
            entity = data.get("entities", {}).get(qid, {})
        except (AttributeError, TypeError):
            return {}

        if not entity:
            return {}

        # Check for missing/invalid entity (Wikidata returns
        # {"missing": ""} for non-existent entities)
        if "missing" in entity:
            return {}

        return {
            "qid": qid,
            "labels": self._extract_lang_map(entity.get("labels", {})),
            "descriptions": self._extract_lang_map(entity.get("descriptions", {})),
            "aliases": self._extract_aliases(entity.get("aliases", {})),
        }

    @staticmethod
    def _extract_lang_map(lang_map):
        """Extract {lang: value} from a Wikidata language map.

        Wikidata returns labels/descriptions as:
            {"en": {"language": "en", "value": "iron ore"}, ...}
        This flattens to:
            {"en": "iron ore", ...}

        Args:
            lang_map: Dict of language code to {language, value} dicts.

        Returns:
            Simple dict of {lang_code: string_value}.
        """
        result = {}
        for lang, entry in lang_map.items():
            if isinstance(entry, dict) and "value" in entry:
                result[lang] = entry["value"]
        return result

    @staticmethod
    def _extract_aliases(alias_map):
        """Extract {lang: [values]} from a Wikidata alias map.

        Wikidata returns aliases as:
            {"en": [{"language": "en", "value": "haematite"}, ...], ...}
        This flattens to:
            {"en": ["haematite", ...], ...}

        Args:
            alias_map: Dict of language code to list of {language, value} dicts.

        Returns:
            Dict of {lang_code: [string_values]}.
        """
        result = {}
        for lang, entries in alias_map.items():
            if isinstance(entries, list):
                values = []
                for entry in entries:
                    if isinstance(entry, dict) and "value" in entry:
                        values.append(entry["value"])
                if values:
                    result[lang] = values
        return result
