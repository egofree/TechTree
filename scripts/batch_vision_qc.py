#!/usr/bin/env python3
"""Batch vision QC: score every image in docs/images/ via grok CLI.

Uses --prompt-file to avoid ARG_MAX issues, runs N workers in parallel.
"""

import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("ERROR: Pillow required. pip install Pillow")

# ── Config ──────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parent.parent
IMAGES_DIR = PROJECT / "docs" / "images"
IMAGES_JSON = PROJECT / "data" / "images.json"
OUTPUT_FILE = PROJECT / "data" / "vision-audit.json"
GROK_BIN = Path("/home/user/.grok/bin/grok")
MAX_PX = 600
JPEG_QUALITY = 70
MAX_RETRIES = 3
GROK_TIMEOUT = 180  # seconds per image
WORKERS = 2  # parallel grok instances (avoid overloading)
CHECKPOINT_EVERY = 10  # save every N new scores
# ────────────────────────────────────────────────────────────────────────


def load_images_manifest():
    """Load images.json and build filename → node_name mapping."""
    with open(IMAGES_JSON) as f:
        data = json.load(f)
    nodes = data.get("nodes", {})
    # Map: relative path from project root → node_name
    path_to_name = {}
    # Also map by just the filename stem → node_name for fallback
    stem_to_name = {}
    for key, info in nodes.items():
        lp = info.get("local_path", "")
        name = info.get("node_name", key)
        if lp:
            path_to_name[lp] = name
        stem_to_name[key] = name
    return path_to_name, stem_to_name


def derive_article_title(rel_path: str, path_to_name: dict, stem_to_name: dict) -> str:
    """Get article title for an image from images.json or filename."""
    # Try direct lookup by full relative path
    if rel_path in path_to_name:
        return path_to_name[rel_path]

    # Try mapping from filename stem
    # e.g. "agriculture/agriculture_aquaponics.jpg" → "agriculture.aquaponics"
    fname = Path(rel_path).stem  # agriculture_aquaponics
    domain = Path(rel_path).parent.name
    parts = fname.split("_", 1)
    if len(parts) > 1:
        slug = parts[1]
        # Try dotted key: "agriculture.aquaponics"
        dotted = f"{domain}.{slug}"
        if dotted in stem_to_name:
            return stem_to_name[dotted]
        # Try with nested slug: "agriculture.soil-management.vermiculture"
        # Check various key patterns
        for key in stem_to_name:
            if key.endswith(slug) or key.endswith(fname):
                return stem_to_name[key]

    # Fallback: derive from filename
    if len(parts) > 1:
        title = parts[1].replace("-", " ").replace("_", " ").title()
    else:
        title = parts[0].title()
    return title


def resize_to_base64(img_path: Path) -> tuple[str, str]:
    """Resize image to max 600px, return (base64_str, mime_type)."""
    img = Image.open(img_path)
    img = img.convert("RGB")
    w, h = img.size
    if w > MAX_PX or h > MAX_PX:
        if w >= h:
            new_w = MAX_PX
            new_h = int(h * MAX_PX / w)
        else:
            new_h = MAX_PX
            new_w = int(w * MAX_PX / h)
        img = img.resize((new_w, new_h), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, format="JPEG", quality=JPEG_QUALITY)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return b64, "image/jpeg"


def build_prompt_json(b64_data: str, mime: str, article_title: str) -> str:
    """Build the prompt JSON for grok CLI."""
    text_prompt = (
        f"Rate this image 1-10 for relevance to '{article_title}' as an illustration "
        f"in a science/technology reference about bootstrapping industrial civilization. "
        f"Consider: visual impact, topical accuracy, image quality, whether it's a "
        f"diagram/photo/illustration. Respond with ONLY valid JSON, no markdown fences: "
        f'{{"relevance": N, "quality": N, "verdict": "keep"|"replace", "reason": "..."}}'
    )
    payload = {
        "type": "acp",
        "content": [
            {"type": "image", "data": b64_data, "mimeType": mime},
            {"type": "text", "text": text_prompt},
        ],
    }
    return json.dumps(payload)


def call_grok(prompt_json: str) -> dict:
    """Call grok CLI with --prompt-file, return parsed response."""
    # Write to temp file to avoid ARG_MAX
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False,
                                     prefix="grok_qc_") as tf:
        tf.write(prompt_json)
        tmp_path = tf.name

    try:
        result = subprocess.run(
            [str(GROK_BIN), "--prompt-file", tmp_path],
            capture_output=True,
            text=True,
            timeout=GROK_TIMEOUT,
        )
    finally:
        os.unlink(tmp_path)

    output = result.stdout.strip()
    if not output:
        raise RuntimeError(f"grok returned empty stdout. stderr: {result.stderr[:500]}")

    # Try to extract JSON from output
    match = re.search(r'\{[^{}]*"relevance"[^{}]*\}', output, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    # Try parsing whole output
    return json.loads(output)


def score_image(img_path: Path, path_to_name: dict, stem_to_name: dict) -> dict:
    """Score a single image, return result dict."""
    rel = str(img_path.relative_to(PROJECT))
    domain = img_path.parent.name
    article_title = derive_article_title(rel, path_to_name, stem_to_name)
    fname = img_path.name

    t0 = time.time()
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            b64, mime = resize_to_base64(img_path)
            prompt_json = build_prompt_json(b64, mime, article_title)
            response = call_grok(prompt_json)
            elapsed = round(time.time() - t0, 1)

            relevance = int(response.get("relevance", 0))
            quality = int(response.get("quality", 0))
            reason = response.get("reason", "No reason provided")

            # Apply threshold logic
            if relevance < 5 or quality < 5:
                verdict = "replace"
            else:
                verdict = "keep"

            return {
                "file": fname,
                "domain": domain,
                "article_title": article_title,
                "relevance": relevance,
                "quality": quality,
                "verdict": verdict,
                "reason": reason,
                "elapsed_s": elapsed,
            }
        except Exception as e:
            if attempt < MAX_RETRIES:
                time.sleep(2 * attempt)
                continue
            elapsed = round(time.time() - t0, 1)
            return {
                "file": fname,
                "domain": domain,
                "article_title": article_title,
                "relevance": 0,
                "quality": 0,
                "verdict": "error",
                "reason": f"Error after {MAX_RETRIES} attempts: {e}",
                "elapsed_s": elapsed,
            }


def collect_images() -> list[Path]:
    """Collect all image files from docs/images/."""
    extensions = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg", ".bmp", ".tiff"}
    images = []
    for root, dirs, files in os.walk(IMAGES_DIR):
        for f in sorted(files):
            if Path(f).suffix.lower() in extensions:
                images.append(Path(root) / f)
    return sorted(images)


def save_results(results: dict, total_count: int):
    """Save results to vision-audit.json."""
    flagged = sum(1 for v in results.values() if v.get("verdict") == "replace")
    error_count = sum(1 for v in results.values() if v.get("verdict") == "error")

    # Per-domain breakdown
    domains = {}
    for k, v in results.items():
        d = v.get("domain", "unknown")
        if d not in domains:
            domains[d] = {"total": 0, "keep": 0, "replace": 0, "error": 0}
        domains[d]["total"] += 1
        domains[d][v.get("verdict", "error")] += 1

    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "total": len(results),
        "flagged_count": flagged,
        "error_count": error_count,
        "pass_count": len(results) - flagged - error_count,
        "coverage_pct": round(len(results) / total_count * 100, 1) if total_count else 0,
        "domain_breakdown": domains,
        "results": results,
    }

    # Preserve replacements from prior audit if present
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            old = json.load(f)
        if "replacements" in old:
            output["replacements"] = old["replacements"]
        if "replacement_count" in old:
            output["replacement_count"] = old["replacement_count"]

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


def main():
    print(f"Loading images.json manifest...")
    path_to_name, stem_to_name = load_images_manifest()
    print(f"  {len(path_to_name)} path mappings, {len(stem_to_name)} stem mappings")

    images = collect_images()
    print(f"Found {len(images)} images to score")
    print(f"Using {WORKERS} parallel workers, timeout {GROK_TIMEOUT}s per image")

    # Load existing results if any (to skip already-scored images)
    existing = {}
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            old = json.load(f)
        old_results = old.get("results", {})
        for k, v in old_results.items():
            existing[f"{v.get('domain', k.split('/')[0])}/{v.get('file', k)}"] = v
        print(f"  {len(existing)} existing results to preserve")

    # Separate into todo (need scoring) and preserved
    todo_images = []
    results = {}
    skipped = 0
    for img_path in images:
        domain = img_path.parent.name
        fname = img_path.name
        key = f"{domain}/{fname}"
        if key in existing:
            results[key] = existing[key]
            skipped += 1
        else:
            todo_images.append(img_path)

    print(f"  {len(todo_images)} images to score, {skipped} preserved from prior runs")
    if not todo_images:
        print("Nothing to do!")
        save_results(results, len(images))
        return

    # Score in parallel
    scored = 0
    errors = 0
    lock = __import__('threading').Lock()

    def worker(img_path):
        return img_path, score_image(img_path, path_to_name, stem_to_name)

    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        futures = {executor.submit(worker, img): img for img in todo_images}

        for future in as_completed(futures):
            img_path, result = future.result()
            domain = img_path.parent.name
            fname = img_path.name
            key = f"{domain}/{fname}"
            results[key] = result

            with lock:
                scored += 1
                if result["verdict"] == "error":
                    errors += 1
                    print(f"  [{scored}/{len(todo_images)}] ERROR {key}: {result['reason'][:80]}")
                else:
                    print(f"  [{scored}/{len(todo_images)}] {key}: R={result['relevance']} Q={result['quality']} → {result['verdict']}")

                # Checkpoint
                if scored % CHECKPOINT_EVERY == 0:
                    save_results(results, len(images))
                    print(f"  === checkpoint: {scored} scored, {skipped} preserved, {errors} errors ===")

    # Final save
    save_results(results, len(images))
    print(f"\nDone! Scored: {scored}, Preserved: {skipped}, Errors: {errors}, Total: {len(results)}")


def save_results(results: dict, total_count: int):
    """Save results to vision-audit.json."""
    flagged = sum(1 for v in results.values() if v.get("verdict") == "replace")
    error_count = sum(1 for v in results.values() if v.get("verdict") == "error")

    # Per-domain breakdown
    domains = {}
    for k, v in results.items():
        d = v.get("domain", "unknown")
        if d not in domains:
            domains[d] = {"total": 0, "keep": 0, "replace": 0, "error": 0}
        domains[d]["total"] += 1
        domains[d][v.get("verdict", "error")] += 1

    output = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "total": len(results),
        "flagged_count": flagged,
        "error_count": error_count,
        "pass_count": len(results) - flagged - error_count,
        "coverage_pct": round(len(results) / total_count * 100, 1) if total_count else 0,
        "domain_breakdown": domains,
        "results": results,
    }

    # Preserve replacements from prior audit if present
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            old = json.load(f)
        if "replacements" in old:
            output["replacements"] = old["replacements"]
        if "replacement_count" in old:
            output["replacement_count"] = old["replacement_count"]

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
