"""Unblind the paste test and add up the totals. Run with:
python3 evidence/paste-test/analyse.py evidence/paste-test
"""
import json, sys
from pathlib import Path
folder = Path(sys.argv[1])
mapping = json.loads((folder / "mapping.json").read_text())
scores = json.loads((folder / "scores.json").read_text())
for arm in ("current", "edited", "prompt"):
    cs = [c for c, m in mapping.items() if m["arm"] == arm]
    for c in cs:
        assert scores[c]["scenario"] == mapping[c]["scenario"], c
    right = sum(sum(scores[c]["sort"]) for c in cs)
    total = sum(len(scores[c]["sort"]) for c in cs)
    shape = sum(sum(scores[c]["shape"]) for c in cs) / len(cs)
    print(f'{arm:8} sorted right={right}/{total} mean shape={shape:.2f}/3 failures={sum(scores[c]["F"] for c in cs)}')
