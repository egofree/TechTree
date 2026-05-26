"""JSON manifest management, patch generation/application, checkpoint/rollback
stubs, and node/edge validation for the bootciv tech tree data layer.

Stdlib-only. All file writes use write-to-temp + os.replace for crash safety.
"""

import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

NODE_REQUIRED_FIELDS = [
    "id", "name", "level", "parent", "description",
    "timeline", "outputs", "critical", "early_win", "pinnacle", "tags",
]

EDGE_REQUIRED_FIELDS = ["from", "to", "type", "flow"]

VALID_EDGE_TYPES = {"material", "tool"}

VALID_EDGE_FLOWS = {"primary", "byproduct-reuse", "waste-recovery", "recycling-loop"}

VALID_LIFECYCLE_TAGS = {"waste-source", "waste-sink", "recyclable", "recycled-feedstock", "closed-loop"}

# ---------------------------------------------------------------------------
# Manifest management
# ---------------------------------------------------------------------------


def load_manifest(path):
    """Read a JSON manifest file and return a dict.

    Returns an empty dict if the file does not exist or cannot be parsed.
    """
    p = Path(path)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def save_manifest(path, data):
    """Write a JSON manifest atomically (write-to-temp + rename).

    Ensures crash safety: the destination file is never in a partial state.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    fd, tmp_path = tempfile.mkstemp(
        suffix=".tmp",
        prefix=".manifest_",
        dir=str(p.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        os.replace(tmp_path, str(p))
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


# ---------------------------------------------------------------------------
# Patch generation
# ---------------------------------------------------------------------------


def generate_node_patch(new_nodes, new_edges, existing_nodes_path, existing_edges_path):
    """Compare new data against existing manifests and produce a patch dict.

    The patch shows additions and modifications relative to the current
    data files.  Nodes are matched by ``id``; edges are compared as tuples
    ``(from, to, type)``.

    Args:
        new_nodes: List of node dicts to merge.
        new_edges: List of edge dicts to merge.
        existing_nodes_path: Path to the current nodes.json.
        existing_edges_path: Path to the current edges.json.

    Returns:
        Dict with keys ``nodes_added``, ``nodes_modified``, ``edges_added``.
    """
    existing_data = load_manifest(existing_nodes_path)
    existing_nodes_list = existing_data.get("nodes", [])
    existing_node_map = {n["id"]: n for n in existing_nodes_list if "id" in n}

    existing_edges_data = load_manifest(existing_edges_path)
    existing_edges_list = existing_edges_data.get("edges", [])
    existing_edge_set = {
        (e["from"], e["to"], e["type"], e["flow"])
        for e in existing_edges_list
        if all(k in e for k in EDGE_REQUIRED_FIELDS)
    }

    nodes_added = []
    nodes_modified = []
    for node in new_nodes:
        nid = node.get("id")
        if not nid:
            continue
        if nid not in existing_node_map:
            nodes_added.append(node)
        elif existing_node_map[nid] != node:
            nodes_modified.append(node)

    edges_added = []
    for edge in new_edges:
        key = (edge.get("from"), edge.get("to"), edge.get("type"), edge.get("flow"))
        if all(key) and key not in existing_edge_set:
            edges_added.append(edge)

    return {
        "nodes_added": nodes_added,
        "nodes_modified": nodes_modified,
        "edges_added": edges_added,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


# ---------------------------------------------------------------------------
# Patch application
# ---------------------------------------------------------------------------


def apply_patch(nodes_path, edges_path, patch_path):
    """Atomically apply a patch to nodes.json and edges.json.

    The patch file is a JSON dict with keys ``nodes_added``,
    ``nodes_modified``, and ``edges_added`` (as produced by
    :func:`generate_node_patch`).

    Both data files are written using write-to-temp + rename for crash safety.
    """
    patch = load_manifest(patch_path)
    if not patch:
        print("apply_patch: empty or missing patch file: {}".format(patch_path))
        return

    nodes_data = load_manifest(nodes_path)
    if not nodes_data:
        nodes_data = {"$schema": "bootciv-nodes-v1", "nodes": []}
    nodes_list = nodes_data.get("nodes", [])
    node_map = {n["id"]: n for n in nodes_list if "id" in n}

    edges_data = load_manifest(edges_path)
    if not edges_data:
        edges_data = {"$schema": "bootciv-edges-v1", "edges": []}
    edges_list = edges_data.get("edges", [])
    edge_set = {
        (e["from"], e["to"], e["type"], e["flow"])
        for e in edges_list
        if all(k in e for k in EDGE_REQUIRED_FIELDS)
    }

    for node in patch.get("nodes_added", []):
        nid = node.get("id")
        if nid and nid not in node_map:
            nodes_list.append(node)
            node_map[nid] = node

    for node in patch.get("nodes_modified", []):
        nid = node.get("id")
        if nid and nid in node_map:
            for i, existing in enumerate(nodes_list):
                if existing.get("id") == nid:
                    nodes_list[i] = node
                    node_map[nid] = node
                    break

    for edge in patch.get("edges_added", []):
        key = (edge.get("from"), edge.get("to"), edge.get("type"), edge.get("flow"))
        if all(key) and key not in edge_set:
            edges_list.append(edge)
            edge_set.add(key)

    nodes_data["nodes"] = nodes_list
    edges_data["edges"] = edges_list

    save_manifest(nodes_path, nodes_data)
    save_manifest(edges_path, edges_data)

    print("Patch applied: {} nodes, {} edges".format(len(nodes_list), len(edges_list)))


# ---------------------------------------------------------------------------
# Checkpoint / rollback stubs (full implementation in T14)
# ---------------------------------------------------------------------------


def create_checkpoint(nodes_path, edges_path):
    """Save timestamped backup copies of nodes.json and edges.json.

    Backups are stored in ``data/.backups/<timestamp>/``.

    Args:
        nodes_path: Path to nodes.json.
        edges_path: Path to edges.json.

    Returns:
        Path to the checkpoint directory (string).
    """
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    nodes_p = Path(nodes_path)
    backup_dir = nodes_p.parent / ".backups" / ts
    backup_dir.mkdir(parents=True, exist_ok=True)

    for src_path in (nodes_path, edges_path):
        src = Path(src_path)
        if src.exists():
            shutil.copy2(str(src), str(backup_dir / src.name))

    print("Checkpoint created: {}".format(backup_dir))
    return str(backup_dir)


def rollback(checkpoint_path):
    """Restore nodes.json and edges.json from a checkpoint directory.

    This is a basic stub — T14 extends it with manifest tracking and
    selective rollback.

    Args:
        checkpoint_path: Path to the checkpoint directory (as returned by
            :func:`create_checkpoint`).

    Returns:
        True if restoration succeeded, False otherwise.
    """
    cp = Path(checkpoint_path)
    if not cp.is_dir():
        print("rollback: checkpoint not found: {}".format(checkpoint_path))
        return False

    data_dir = cp.parent.parent
    restored = []
    for json_file in cp.glob("*.json"):
        dest = data_dir / json_file.name
        shutil.copy2(str(json_file), str(dest))
        restored.append(dest.name)

    if restored:
        print("Rollback restored: {}".format(", ".join(sorted(restored))))
        return True
    else:
        print("rollback: no .json files found in checkpoint")
        return False


def pre_crawl_checkpoint():
    """Convenience wrapper: checkpoint the standard data paths.

    Saves ``data/nodes.json`` and ``data/edges.json`` before a crawl run.

    Returns:
        Path to the checkpoint directory (string).
    """
    script_dir = Path(__file__).resolve().parent.parent
    data_dir = script_dir.parent / "data"
    nodes_path = data_dir / "nodes.json"
    edges_path = data_dir / "edges.json"
    return create_checkpoint(str(nodes_path), str(edges_path))


def post_crawl_verify():
    """Run validate.sh programmatically and return success status.

    Executes ``scripts/validate.sh`` via subprocess and captures its output.
    Returns True if all checks pass, False otherwise.

    Returns:
        bool: True if validation succeeded, False otherwise.
    """
    script_dir = Path(__file__).resolve().parent.parent
    validate_path = script_dir / "validate.sh"

    if not validate_path.exists():
        print("post_crawl_verify: validate.sh not found at {}".format(validate_path))
        return False

    try:
        result = subprocess.run(
            ["bash", str(validate_path)],
            capture_output=True,
            text=True,
            timeout=120,
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr, end="")
        if result.returncode == 0:
            print("post_crawl_verify: validation passed")
            return True
        else:
            print("post_crawl_verify: validation failed (exit {})".format(
                result.returncode
            ))
            return False
    except subprocess.TimeoutExpired:
        print("post_crawl_verify: validate.sh timed out")
        return False
    except Exception as exc:
        print("post_crawl_verify: error running validate.sh: {}".format(exc))
        return False


def rollback_on_failure(checkpoint_path):
    """Restore all files from a checkpoint directory, with logging.

    Wrapper around :func:`rollback` that also includes the catalog file
    (e.g. ``plants.json``) if present in the checkpoint.  Provides detailed
    logging of what was restored.

    Args:
        checkpoint_path: Path to the checkpoint directory (as returned by
            :func:`pre_crawl_checkpoint` or :func:`create_checkpoint`).

    Returns:
        True if restoration succeeded, False otherwise.
    """
    cp = Path(checkpoint_path)
    if not cp.is_dir():
        print("rollback_on_failure: checkpoint not found: {}".format(checkpoint_path))
        return False

    data_dir = cp.parent.parent
    restored = []
    for json_file in sorted(cp.glob("*.json")):
        dest = data_dir / json_file.name
        shutil.copy2(str(json_file), str(dest))
        restored.append(dest.name)

    if restored:
        print("rollback_on_failure: restored {} files from {}: {}".format(
            len(restored), cp.name, ", ".join(restored)
        ))
        return True
    else:
        print("rollback_on_failure: no .json files found in checkpoint")
        return False


def list_checkpoints():
    """List available checkpoints in data/.backups/.

    Returns:
        List of dicts with keys ``name`` (timestamp string) and ``path``
        (absolute path string), sorted newest-first.  Empty list if no
        checkpoints exist.
    """
    script_dir = Path(__file__).resolve().parent.parent
    backup_dir = script_dir.parent / "data" / ".backups"

    if not backup_dir.is_dir():
        return []

    checkpoints = []
    for entry in sorted(backup_dir.iterdir(), reverse=True):
        if entry.is_dir():
            file_count = len(list(entry.glob("*.json")))
            checkpoints.append({
                "name": entry.name,
                "path": str(entry),
                "files": file_count,
            })

    return checkpoints


def cleanup_old_checkpoints(keep=5):
    """Remove old checkpoints, keeping only the N most recent.

    Args:
        keep: Number of most recent checkpoints to retain (default 5).

    Returns:
        List of removed checkpoint directory paths (strings).
    """
    checkpoints = list_checkpoints()

    if len(checkpoints) <= keep:
        print("cleanup_old_checkpoints: {} checkpoints found, nothing to remove".format(
            len(checkpoints)
        ))
        return []

    to_remove = checkpoints[keep:]
    removed = []

    for cp in to_remove:
        cp_path = Path(cp["path"])
        try:
            shutil.rmtree(str(cp_path))
            removed.append(cp["path"])
            print("cleanup_old_checkpoints: removed {}".format(cp["name"]))
        except OSError as exc:
            print("cleanup_old_checkpoints: failed to remove {}: {}".format(
                cp["name"], exc
            ))

    print("cleanup_old_checkpoints: kept {}, removed {}".format(
        len(checkpoints) - len(removed), len(removed)
    ))
    return removed


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------


def validate_node(node):
    """Check a single node dict has all required fields.

    Args:
        node: A node dict (as found in nodes.json ``nodes`` array).

    Returns:
        List of error strings. Empty list means the node is valid.
    """
    errors = []

    for field in NODE_REQUIRED_FIELDS:
        if field not in node:
            errors.append("missing required field: {}".format(field))

    nid = node.get("id")
    if nid is not None:
        if not isinstance(nid, str) or not nid:
            errors.append("field 'id' must be a non-empty string")

    level = node.get("level")
    if level is not None and level not in ("domain", "capability", "process"):
        errors.append(
            "field 'level' must be one of domain/capability/process, got: {}".format(
                repr(level)
            )
        )

    outputs = node.get("outputs")
    if outputs is not None and not isinstance(outputs, list):
        errors.append("field 'outputs' must be a list")

    for bool_field in ("critical", "early_win", "pinnacle"):
        val = node.get(bool_field)
        if val is not None and not isinstance(val, bool):
            errors.append("field '{}' must be a boolean".format(bool_field))

    tags = node.get("tags")
    if tags is not None:
        if not isinstance(tags, dict):
            errors.append("field 'tags' must be a dict")
        else:
            for sub in ("material", "capability"):
                if sub in tags and not isinstance(tags[sub], list):
                    errors.append("field 'tags.{}' must be a list".format(sub))

            if "lifecycle" in tags:
                if not isinstance(tags["lifecycle"], list):
                    errors.append("field 'tags.lifecycle' must be a list")
                elif isinstance(tags["lifecycle"], list):
                    for val in tags["lifecycle"]:
                        if val not in VALID_LIFECYCLE_TAGS:
                            errors.append(
                                "tags.lifecycle value '{}' not in controlled vocabulary: {}".format(
                                    val, sorted(VALID_LIFECYCLE_TAGS)
                                )
                            )

    return errors


def validate_edge(edge):
    """Check an edge dict has required fields with valid values.

    Args:
        edge: An edge dict (as found in edges.json ``edges`` array).

    Returns:
        List of error strings. Empty list means the edge is valid.
    """
    errors = []

    for field in EDGE_REQUIRED_FIELDS:
        if field not in edge:
            errors.append("missing required field: {}".format(field))

    edge_type = edge.get("type")
    if edge_type is not None and edge_type not in VALID_EDGE_TYPES:
        errors.append(
            "field 'type' must be one of {}, got: {}".format(
                sorted(VALID_EDGE_TYPES), repr(edge_type)
            )
        )

    edge_flow = edge.get("flow")
    if edge_flow is not None and edge_flow not in VALID_EDGE_FLOWS:
        errors.append(
            "field 'flow' must be one of {}, got: {}".format(
                sorted(VALID_EDGE_FLOWS), repr(edge_flow)
            )
        )

    # 'from' and 'to' must differ (no self-loops).
    from_id = edge.get("from")
    to_id = edge.get("to")
    if from_id is not None and to_id is not None and from_id == to_id:
        errors.append("self-loop detected: 'from' and 'to' are identical ({})".format(from_id))

    return errors
