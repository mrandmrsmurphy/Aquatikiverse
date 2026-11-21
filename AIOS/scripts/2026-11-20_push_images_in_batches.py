#!/usr/bin/env python3
"""Add untracked images to git in ~25 MB batches, commit and push each, pausing between batches."""
import subprocess, sys, time, os
BATCH = 25 * 1024 * 1024
PAUSE = int(sys.argv[1]) if len(sys.argv) > 1 else 600
EXT = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')
def run(*a): return subprocess.run(a, check=True, capture_output=True, text=True).stdout
files = [f for f in run('git', 'ls-files', '-o', '--exclude-standard', '-z').split('\0') if f.lower().endswith(EXT)]
files.sort()
batches, cur, size = [], [], 0
for f in files:
    s = os.path.getsize(f)
    if cur and size + s > BATCH:
        batches.append(cur); cur, size = [], 0
    cur.append(f); size += s
if cur: batches.append(cur)
print(f'{len(files)} images, {len(batches)} batches, pause {PAUSE}s', flush=True)
for i, b in enumerate(batches, 1):
    run('git', 'add', '--', *b)
    run('git', 'commit', '-q', '-m', f'Add images batch {i}/{len(batches)}\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>')
    run('git', 'push', '-q')
    print(f'batch {i}/{len(batches)} pushed ({len(b)} files)', flush=True)
    if i < len(batches): time.sleep(PAUSE)
print('done', flush=True)
