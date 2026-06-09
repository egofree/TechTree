#!/usr/bin/env python3
"""Retry error images from vision audit."""
import json, os, re, subprocess, time, base64, tempfile, sys
from pathlib import Path
from PIL import Image
from io import BytesIO

PROJECT = Path('/home/user/dev/bootciv/tech-tree-bootstrap')
GROK_BIN = '/home/user/.grok/bin/grok'

def save(d):
    results = d['results']
    d['flagged_count'] = sum(1 for v in results.values() if v.get('verdict') == 'replace')
    d['error_count'] = sum(1 for v in results.values() if v.get('verdict') == 'error')
    d['pass_count'] = sum(1 for v in results.values() if v.get('verdict') == 'keep')
    domains = {}
    for k, v in results.items():
        dd = v.get('domain', 'unknown')
        if dd not in domains:
            domains[dd] = {'total': 0, 'keep': 0, 'replace': 0, 'error': 0}
        domains[dd]['total'] += 1
        domains[dd][v.get('verdict', 'error')] += 1
    d['domain_breakdown'] = domains
    with open(PROJECT / 'data/vision-audit.json', 'w') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

with open(PROJECT / 'data/vision-audit.json') as f:
    data = json.load(f)

errors = {k: v for k, v in data['results'].items() if v.get('verdict') == 'error'}
print(f"Retrying {len(errors)} error images...")

fixed = 0
still_errors = 0

for i, (key, val) in enumerate(errors.items()):
    domain = val.get('domain', 'plants')
    fname = val.get('file', key.split('/')[-1])
    img_path = PROJECT / 'docs' / 'images' / domain / fname

    if not img_path.exists():
        print(f"  [{i+1}] MISSING: {img_path}", flush=True)
        still_errors += 1
        continue

    print(f"  [{i+1}/{len(errors)}] {key}...", end='', flush=True)

    success = False
    for attempt in range(3):
        try:
            img = Image.open(img_path).convert('RGB')
            w, h = img.size
            if w > 600 or h > 600:
                if w >= h:
                    nw, nh = 600, int(h * 600 / w)
                else:
                    nh, nw = 600, int(w * 600 / h)
                img = img.resize((nw, nh), Image.LANCZOS)
            buf = BytesIO()
            img.save(buf, format='JPEG', quality=70)
            b64 = base64.b64encode(buf.getvalue()).decode('ascii')

            title = val.get('article_title', fname.replace('_', ' ').replace('.jpg','').replace('.png','').replace('.webp',''))
            prompt = json.dumps({
                'type': 'acp',
                'content': [
                    {'type': 'image', 'data': b64, 'mimeType': 'image/jpeg'},
                    {'type': 'text', 'text': f"Rate this image 1-10 for relevance to '{title}' as an illustration in a science/technology reference about bootstrapping industrial civilization. Consider: visual impact, topical accuracy, image quality. Respond with ONLY valid JSON: {{\"relevance\": N, \"quality\": N, \"verdict\": \"keep\" or \"replace\", \"reason\": \"...\"}}"}
                ]
            })

            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, prefix='grok_retry_') as tf:
                tf.write(prompt)
                tmp = tf.name

            t0 = time.time()
            result = subprocess.run([GROK_BIN, '--prompt-file', tmp], capture_output=True, text=True, timeout=180)
            os.unlink(tmp)
            elapsed = time.time() - t0

            out = result.stdout.strip()
            match = re.search(r'\{[^{}]*"relevance"[^{}]*\}', out, re.DOTALL)
            if match:
                parsed = json.loads(match.group(0))
                rel = int(parsed.get('relevance', 0))
                qual = int(parsed.get('quality', 0))
                verdict = 'keep' if rel >= 5 and qual >= 5 else 'replace'
                reason = parsed.get('reason', 'No reason')

                data['results'][key] = {
                    'file': fname, 'domain': domain, 'article_title': title,
                    'relevance': rel, 'quality': qual, 'verdict': verdict,
                    'reason': reason, 'elapsed_s': round(elapsed, 1)
                }
                fixed += 1
                success = True
                print(f" OK: R={rel} Q={qual} -> {verdict} ({elapsed:.0f}s)", flush=True)
                break
            else:
                raise ValueError(f"No JSON in output: {out[:100]}")
        except Exception as e:
            if attempt < 2:
                time.sleep(5)
            else:
                print(f" FAILED: {str(e)[:80]}", flush=True)
                still_errors += 1

    # Checkpoint every 5 images
    if (i + 1) % 5 == 0:
        save(data)
        print(f"  === checkpoint: {fixed} fixed, {still_errors} failed, {len(errors)-i-1} remaining ===", flush=True)

save(data)
print(f"\nRetry complete: {fixed} fixed, {still_errors} still errors")
