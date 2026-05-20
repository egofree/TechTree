"""SPARQL client for Wikidata structured data queries.

Stdlib-only. Uses WikiClient for HTTP transport and RateLimiter for
throttling. Provides pagination via LIMIT/OFFSET and transforms raw
SPARQL JSON bindings into simple flat dicts suitable for catalog output.

Usage:
    from lib.wiki_client import WikiClient
    from lib.rate_limiter import RateLimiter
    from lib.sparql_client import SparqlClient

    client = SparqlClient()
    for batch in client.get_plant_species(limit=50):
        for species in batch:
            print(species["scientific_name"])
"""

from lib.wiki_client import WikiClient
from lib.rate_limiter import RateLimiter


# --- Constants ---

WIKIDATA_ENDPOINT = "https://query.wikidata.org/sparql"

WIKIDATA_URI_PREFIX = "http://www.wikidata.org/entity/"

DEFAULT_LIMIT = 100

DEFAULT_TIMEOUT = 60


# --- Helpers ---

def _strip_wikidata_uri(value):
    """Extract Q-id from a full Wikidata URI.

    Args:
        value: String, either a full URI like
            "http://www.wikidata.org/entity/Q123" or already a bare Q-id.

    Returns:
        Short Q-id string (e.g. "Q123"), or the original value unchanged.
    """
    if value and value.startswith(WIKIDATA_URI_PREFIX):
        return value[len(WIKIDATA_URI_PREFIX):]
    return value


# --- Client ---

class SparqlClient:
    """SPARQL query client for Wikidata.

    Wraps WikiClient for HTTP and RateLimiter for throttling.
    All queries include LIMIT/OFFSET to avoid timeout.

    Args:
        endpoint: SPARQL endpoint URL.
        client: WikiClient instance for HTTP transport.
        limiter: RateLimiter instance for request throttling.
    """

    def __init__(self, endpoint=None, client=None, limiter=None):
        self.endpoint = endpoint or WIKIDATA_ENDPOINT
        self.client = client or WikiClient()
        self.limiter = limiter or RateLimiter(requests_per_second=1)

    def sparql_query(self, query, limit=DEFAULT_LIMIT, offset=0):
        """Execute a SPARQL query with automatic pagination parameters.

        Appends LIMIT and OFFSET clauses if not already present in the
        query string. Blocks on the rate limiter before each request.

        Args:
            query: SPARQL query string (SELECT ... WHERE { ... }).
            limit: Maximum number of results to return.
            offset: Number of results to skip.

        Returns:
            List of dicts (one per result row), or empty list on failure.
        """
        padded = query.rstrip().rstrip(";")
        if "LIMIT" not in padded.upper().split("}")[-1]:
            padded += "\nLIMIT {}".format(limit)
        if offset > 0 and "OFFSET" not in padded.upper().split("}")[-1]:
            padded += "\nOFFSET {}".format(offset)

        self.limiter.wait()

        data = self.client.get_json(
            url=self.endpoint,
            params={"query": padded, "format": "json"},
        )

        if data is None:
            print("    SPARQL query returned no data (timeout or error)")
            return []

        try:
            bindings = data["results"]["bindings"]
        except (KeyError, TypeError):
            print("    SPARQL response missing expected structure")
            return []

        return self._simplify_bindings(bindings)

    def get_plant_species(self, limit=DEFAULT_LIMIT, offset=0, config=None):
        """Query Wikidata for plant species (taxa under Plantae).

        Finds items that are instances of taxon (Q16521) with a parent
        taxon chain reaching Plantae (Q15978631). Extracts scientific
        name, label, family, and image URL.

        Args:
            limit: Maximum number of results per page.
            offset: Number of results to skip.
            config: Optional dict with source configuration (e.g. from
                plants.yaml). Currently unused but reserved for filters.

        Returns:
            List of dicts in catalog format:
                {wikidata_id, scientific_name, label, family, image, source}
        """
        query = (
            "SELECT ?item ?itemLabel ?scientificName ?family ?familyLabel ?image\n"
            "WHERE {\n"
            "  ?item wdt:P31 wd:Q16521 .\n"
            "  ?item wdt:P225 ?scientificName .\n"
            "  ?item wdt:P171+ wd:Q15978631 .\n"
            "  OPTIONAL { ?item wdt:P171 ?family .\n"
            "             ?family wdt:P105 wd:Q35509 . }\n"
            "  OPTIONAL { ?item wdt:P18 ?image . }\n"
            "  SERVICE wikibase:label {\n"
            "    bd:serviceParam wikibase:language \"en\" .\n"
            "  }\n"
            "}"
        )

        rows = self.sparql_query(query, limit=limit, offset=offset)
        results = []
        seen = set()

        for row in rows:
            qid = row.get("item", "")
            if not qid or qid in seen:
                continue
            seen.add(qid)

            results.append({
                "wikidata_id": qid,
                "scientific_name": row.get("scientificName", ""),
                "label": row.get("itemLabel", ""),
                "family": row.get("familyLabel", ""),
                "image": row.get("image", ""),
                "source": "wikidata",
            })

        return results

    def get_species_details(self, wikidata_id):
        """Query detailed properties for a single species.

        Fetches taxonomic classification, common names, image, description,
        and functional properties (edible, medicinal, fiber, etc.).

        Args:
            wikidata_id: Wikidata Q-id (e.g. "Q12345" or full URI).

        Returns:
            Dict with detailed species information, or empty dict on failure.
        """
        qid = _strip_wikidata_uri(wikidata_id)

        query = (
            "SELECT ?item ?itemLabel ?itemDescription\n"
            "  ?scientificName ?parentTaxon ?parentTaxonLabel\n"
            "  ?taxonRank ?taxonRankLabel\n"
            "  ?image ?commonName\n"
            "WHERE {{\n"
            "  BIND(wd:{qid} AS ?item)\n"
            "  OPTIONAL {{ ?item wdt:P225 ?scientificName . }}\n"
            "  OPTIONAL {{ ?item wdt:P171 ?parentTaxon . }}\n"
            "  OPTIONAL {{ ?item wdt:P105 ?taxonRank . }}\n"
            "  OPTIONAL {{ ?item wdt:P18 ?image . }}\n"
            "  OPTIONAL {{ ?item skos:altLabel ?commonName .\n"
            "    FILTER(LANG(?commonName) = \"en\") }}\n"
            "  SERVICE wikibase:label {{\n"
            "    bd:serviceParam wikibase:language \"en\" .\n"
            "  }}\n"
            "}}"
        ).format(qid=qid)

        rows = self.sparql_query(query, limit=1, offset=0)

        if not rows:
            return {}

        row = rows[0]
        return {
            "wikidata_id": qid,
            "label": row.get("itemLabel", ""),
            "description": row.get("itemDescription", ""),
            "scientific_name": row.get("scientificName", ""),
            "parent_taxon": row.get("parentTaxon", ""),
            "parent_taxon_label": row.get("parentTaxonLabel", ""),
            "taxon_rank": row.get("taxonRankLabel", ""),
            "image": row.get("image", ""),
            "common_name": row.get("commonName", ""),
        }

    def _simplify_bindings(self, bindings):
        """Flatten SPARQL JSON bindings into simple string dicts.

        SPARQL results come as:
            {"varName": {"type": "uri", "value": "http://..."}}
        This strips them down to:
            {"varName": "Q123"}

        URI values are shortened from full Wikidata URIs to Q-ids.
        Blank-node and literal types are extracted as plain strings.

        Args:
            bindings: List of binding dicts from SPARQL JSON results.

        Returns:
            List of flat dicts with string values only.
        """
        results = []

        for binding in bindings:
            row = {}
            for key, cell in binding.items():
                value = cell.get("value", "")
                if cell.get("type") == "uri":
                    value = _strip_wikidata_uri(value)
                row[key] = value
            results.append(row)

        return results
