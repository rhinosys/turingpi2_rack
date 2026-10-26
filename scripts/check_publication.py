"""Check the public CAD snapshot, paired docs and local links before publishing."""
from pathlib import Path
import hashlib, json, re
from urllib.parse import unquote
ROOT = Path(__file__).resolve().parents[1]
for item in json.loads((ROOT / 'source-manifest.json').read_text()):
    path = ROOT / item['path']
    assert path.is_file(), path
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], path
english = {p.name for p in (ROOT / 'docs/en').glob('*.md')}
french = {p.name for p in (ROOT / 'docs/fr').glob('*.md')}
assert english == french, (english, french)
for path in (ROOT / 'docs').rglob('*.md'):
    for href in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if href.startswith(('http:', 'https:')):
            prefix = 'https://github.com/rhinosys/turingpi2_rack/blob/main/'
            if href.startswith(prefix):
                assert (ROOT / unquote(href[len(prefix):])).exists(), href
            continue
        href = unquote(href.split('#')[0])
        if href:
            assert (path.parent / href).exists(), (path, href)
for path in ROOT.rglob('*'):
    if '.git' in path.parts or 'site' in path.parts or '.venv' in path.parts:
        continue
    if path.is_file():
        assert path.stat().st_size < 100 * 1024 * 1024, path
print(f'CAD manifest valid; {len(english)} paired documentation pages; local links valid.')
