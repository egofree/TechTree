"""Data access layer for TechTree JSON-LD per-entity files.

Reads and writes individual .jsonld files from data/entities/,
data/products/, and data/entities/_edges/.  Stdlib-only — no
rdflib, pyld, or other external dependencies.

Typical usage::

    from lib.tt_data import load_entity, load_all_entities

    entity = load_entity("metals.iron-steel")
    all_caps = load_all_entities(entity_type="Capability")
"""

import json
import os

# ---------------------------------------------------------------------------
# Path constants — derived from module location
# ---------------------------------------------------------------------------

_LIB_DIR = os.path.dirname(os.path.abspath(__file__))
_SCRIPTS_DIR = os.path.dirname(_LIB_DIR)
_PROJECT_DIR = os.path.dirname(_SCRIPTS_DIR)

DATA_DIR = os.path.join(_PROJECT_DIR, "data")
ENTITIES_DIR = os.path.join(DATA_DIR, "entities")
EDGES_DIR = os.path.join(ENTITIES_DIR, "_edges")
PRODUCTS_DIR = os.path.join(DATA_DIR, "products")
CONTEXT_PATH = os.path.join(DATA_DIR, "context.jsonld")

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

_context_cache = None


def _entity_id_to_path(entity_id):
    """Convert an entity ID to its filesystem path.

    Supports three ID formats:

    * Dotted:  ``metals.iron-steel``  -> data/entities/metals/iron-steel.jsonld
    * Slashed: ``metals/iron-steel``  -> data/entities/metals/iron-steel.jsonld
    * Domain:  ``foundations``        -> data/entities/foundations/foundations.jsonld
    """
    if "/" in entity_id:
        # Already path-like: "metals/iron-steel"
        return os.path.join(ENTITIES_DIR, entity_id + ".jsonld")
    if "." in entity_id:
        # Dotted: "metals.iron-steel" -> domain=metals, name=iron-steel
        domain, name = entity_id.split(".", 1)
        return os.path.join(ENTITIES_DIR, domain, name + ".jsonld")
    # Domain-level: "foundations" -> foundations/foundations.jsonld
    return os.path.join(ENTITIES_DIR, entity_id, entity_id + ".jsonld")


def _load_json(path):
    """Load and parse a JSON-LD file.  Returns *None* if not found."""
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def _deterministic_dumps(data):
    """Serialize to deterministic JSON (sorted keys, 2-space indent)."""
    return json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


# ---------------------------------------------------------------------------
# Public API — loading
# ---------------------------------------------------------------------------


def load_context():
    """Load and cache the JSON-LD context from ``data/context.jsonld``.

    Returns the ``@context`` dict.  The result is cached after the first
    successful call.
    """
    global _context_cache
    if _context_cache is None:
        raw = _load_json(CONTEXT_PATH)
        if raw is None:
            raise FileNotFoundError(
                "Context file not found: {}".format(CONTEXT_PATH)
            )
        _context_cache = raw.get("@context", raw)
    return _context_cache


def load_entity(entity_id):
    """Load a single entity by its ID.

    Args:
        entity_id: Accepts dotted (``metals.iron-steel``), slashed
            (``metals/iron-steel``), or bare domain (``foundations``)
            formats.

    Returns:
        Parsed entity dict, or *None* if the file does not exist.
    """
    return _load_json(_entity_id_to_path(entity_id))


def load_all_entities(entity_type=None):
    """Load every entity file, optionally filtered by ``@type`` or ``level``.

    Walks ``data/entities/`` (skipping the ``_edges/`` sub-directory).

    Args:
        entity_type: Optional filter string.  Compared against both the
            entity's ``@type`` value (``"Domain"``, ``"Capability"``,
            ``"Process"``) and its ``level`` field (``"domain"``,
            ``"capability"``, ``"process"``).

    Returns:
        List of entity dicts.
    """
    entities = []
    for dirpath, dirnames, filenames in os.walk(ENTITIES_DIR):
        # Don't descend into _edges
        if "_edges" in dirnames:
            dirnames.remove("_edges")
        for filename in sorted(filenames):
            if not filename.endswith(".jsonld"):
                continue
            entity = _load_json(os.path.join(dirpath, filename))
            if entity is None:
                continue
            if entity_type is not None:
                if entity_type not in (
                    entity.get("@type"),
                    entity.get("level"),
                ):
                    continue
            entities.append(entity)
    return entities


def load_product(product_id):
    """Load a product by its ID.

    Args:
        product_id: Product identifier (e.g. ``"steel"``,
            ``"aluminum_ingots"``).

    Returns:
        Parsed product dict, or *None* if not found.
    """
    return _load_json(os.path.join(PRODUCTS_DIR, product_id + ".jsonld"))


def load_all_products():
    """Load every product from ``data/products/``.

    Returns:
        List of product dicts, sorted by filename.
    """
    products = []
    if not os.path.isdir(PRODUCTS_DIR):
        return products
    for filename in sorted(os.listdir(PRODUCTS_DIR)):
        if not filename.endswith(".jsonld"):
            continue
        product = _load_json(os.path.join(PRODUCTS_DIR, filename))
        if product is not None:
            products.append(product)
    return products


def load_dependencies_for(entity_id):
    """Load all dependency edges referencing *entity_id*.

    Scans every ``.jsonld`` file in ``data/entities/_edges/`` and returns
    those whose ``from`` or ``to`` field equals *entity_id*.

    Args:
        entity_id: Entity ID in dotted format (e.g. ``"metals.aluminum"``).

    Returns:
        List of edge dicts.
    """
    edges = []
    if not os.path.isdir(EDGES_DIR):
        return edges
    for filename in sorted(os.listdir(EDGES_DIR)):
        if not filename.endswith(".jsonld"):
            continue
        edge = _load_json(os.path.join(EDGES_DIR, filename))
        if edge is None:
            continue
        if edge.get("from") == entity_id or edge.get("to") == entity_id:
            edges.append(edge)
    return edges


def get_nodes_by_domain(domain):
    """Load all entities inside a domain directory.

    Args:
        domain: Domain name (e.g. ``"foundations"``, ``"metals"``).

    Returns:
        List of entity dicts from ``data/entities/{domain}/``, sorted by
        filename.
    """
    domain_dir = os.path.join(ENTITIES_DIR, domain)
    entities = []
    if not os.path.isdir(domain_dir):
        return entities
    for filename in sorted(os.listdir(domain_dir)):
        if not filename.endswith(".jsonld"):
            continue
        entity = _load_json(os.path.join(domain_dir, filename))
        if entity is not None:
            entities.append(entity)
    return entities


def get_prerequisites(entity_id, depth=None):
    """Recursively collect prerequisite entities.

    Follows dependency edges: an edge ``from: A, to: B`` means *A*
    depends on *B*.  Starting from *entity_id*, this function collects
    all *B* entities (and their prerequisites, recursively).

    Args:
        entity_id: Entity ID in dotted format.
        depth: Maximum recursion depth.

            * ``None``  — follow the full chain (cycles are detected).
            * ``1``     — only direct prerequisites.
            * ``N``     — recurse up to *N* levels deep.

    Returns:
        List of entity dicts, deduplicated, in discovery order.
    """
    visited = set()
    result = []

    def _recurse(eid, current_depth):
        if eid in visited:
            return
        visited.add(eid)

        if depth is not None and current_depth > depth:
            return

        for edge in load_dependencies_for(eid):
            if edge.get("from") != eid:
                continue
            dep_id = edge.get("to")
            if not dep_id or dep_id in visited:
                continue
            dep_entity = load_entity(dep_id)
            if dep_entity is not None:
                result.append(dep_entity)
                _recurse(dep_id, current_depth + 1)

    _recurse(entity_id, 1)
    return result


# ---------------------------------------------------------------------------
# Public API — writing
# ---------------------------------------------------------------------------


def save_entity(entity, filepath=None):
    """Write an entity dict to disk with deterministic JSON serialization.

    Uses ``sort_keys=True``, 2-space indent, and a trailing newline so
    that repeated saves produce byte-identical output.

    Args:
        entity: Entity dict to persist.
        filepath: Target path.  When *None*, the path is derived from
            the entity's ``id`` (or ``@id``) field via
            :func:`_entity_id_to_path`.
    """
    if filepath is None:
        entity_id = entity.get("id") or entity.get("@id")
        if not entity_id:
            raise ValueError(
                "Entity has no 'id' or '@id' field; provide filepath explicitly"
            )
        filepath = _entity_id_to_path(entity_id)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(_deterministic_dumps(entity))


# ---------------------------------------------------------------------------
# Public API — conversion
# ---------------------------------------------------------------------------


def entity_to_dict(entity):
    """Flatten a JSON-LD entity to a plain dict.

    Strips ``@context`` and renames ``@type`` -> ``type``.
    If the entity uses ``@id`` instead of ``id``, it is renamed to ``id``.

    Args:
        entity: A JSON-LD entity dict.

    Returns:
        A new dict without JSON-LD artifacts.
    """
    result = {}
    for key, value in entity.items():
        if key == "@context":
            continue
        if key == "@type":
            result["type"] = value
        elif key == "@id":
            # Products use @id; entities use id (mapped via context)
            if "id" not in entity:
                result["id"] = value
        else:
            result[key] = value
    return result
