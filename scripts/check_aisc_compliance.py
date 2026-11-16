#!/usr/bin/env python3
"""Check the AISC submission manuscript against the journal's stated requirements.

Reads manuscript/submission/*.md, references.tsv and (optionally) the built .docx, and reports:
length, reference count, non-academic references, recent-reference share, self-citations,
references per external author, and leftover template placeholders.
Similarity (<=25% overall, <=8% per source) cannot be computed offline and must be checked
with the journal's tool (for example iThenticate or Turnitin).

Usage: python scripts/check_aisc_compliance.py [path/to/manuscript.docx]
"""
import glob
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'manuscript' / 'submission'
OWN = {'hadiprakoso', 'buana', 'kabetta'}


def cited_keys():
    text = ''.join(Path(f).read_text(encoding='utf-8') for f in sorted(glob.glob(str(SRC / '0*_*.md'))))
    keys = []
    for m in re.finditer(r'\[@([^\]]+)\]', text):
        for k in m.group(1).split(';'):
            k = k.strip().lstrip('@')
            if k not in keys:
                keys.append(k)
    return keys


def authors_of(ref):
    head = ref.split(' (', 1)[0]
    found = re.findall(r"([A-Z][^\s,]*(?:[ -][A-Za-zÀ-ɏ'’-]+)*?),\s*((?:[A-Z]\.[ -]?)+)", head)
    if found:
        return [(s.strip().lower(), i.replace(' ', '')) for s, i in found]
    return [(head.strip().lower(), '')]


def main():
    refs = {}
    for ln in (SRC / 'references.tsv').read_text(encoding='utf-8').split('\n'):
        if ln.strip():
            k, flag, text = ln.split('\t', 2)
            refs[k] = (flag == 'NA', text)
    keys = cited_keys()
    missing = [k for k in keys if k not in refs]
    assert not missing, f'unknown keys: {missing}'
    n = len(keys)
    rows = []

    def row(name, value, ok, rule):
        rows.append((name, value, 'PASS' if ok else 'FAIL', rule))

    # length
    words = None
    placeholders = []
    if len(sys.argv) > 1:
        z = zipfile.ZipFile(sys.argv[1])
        d = z.read('word/document.xml').decode('utf-8')
        body = d[d.find('<w:body>'):]
        txt = ' '.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', body))
        words = len(txt.split())
        placeholders = sorted(set(re.findall(r'd month yyyy|yyyy, Vol\. XX\(XX\)|bonviewAISCX+', txt)))
        ref_start = txt.rfind('References')
        row('Manuscript length (words, incl. tables and references)', words, 3500 <= words <= 15000, '3,500 to 15,000')
        row('Main text without references (words)', len(txt[:ref_start].split()), True, 'informational')
    row('References cited', n, n >= 20, 'at least 20')
    na = [k for k in keys if refs[k][0]]
    row('Non-academic references', f'{len(na)} ({", ".join(na)})', len(na) <= 3, 'at most 3')
    years = []
    for k in keys:
        m = re.search(r'\((?:[^)]*?)(\d{4})[a-z]?[,)]', refs[k][1])
        years.append(int(m.group(1)) if m else 0)
    recent = sum(1 for y in years if 2021 <= y <= 2026)
    row('References from 2021 to 2026', f'{recent}/{n} ({100 * recent / n:.1f}%)', recent / n >= 0.60, 'at least 60%')
    own = [k for k in keys if any(a[0] in OWN for a in authors_of(refs[k][1]))]
    row('Self-citations', f'{len(own)} ({100 * len(own) / n:.1f}%)', len(own) <= 3 and len(own) / n <= 0.10, 'at most 3 and 10%')
    cnt = Counter()
    for k in keys:
        for a in set(authors_of(refs[k][1])):
            if a[0] not in OWN:
                cnt[a] += 1
    top = cnt.most_common(4)
    mx = top[0][1] if top else 0
    row('Most-cited external author (surname, initials)', f'{top[0][0][0].title()} {top[0][0][1]}: {mx} refs ({100 * mx / n:.1f}%)',
        mx <= 5 and mx / n <= 0.10, 'at most 5 and 10% per author or group')
    print(f'{"Check":58s} {"Result":44s} {"Status":6s} Rule')
    for name, value, status, rule in rows:
        print(f'{name:58s} {str(value):44s} {status:6s} {rule}')
    print('\nAuthors with 3 or more references:', [(a[0].title() + ' ' + a[1], c) for a, c in cnt.items() if c >= 3])
    print('Uncited keys in references.tsv (not printed):', [k for k in refs if k not in keys])
    if placeholders:
        print('Template placeholders left for the editor:', placeholders)
    print('Similarity (<=25% overall, <=8% per source): not computable offline; run the journal tool before submission.')
    sys.exit(0 if all(r[2] == 'PASS' for r in rows) else 1)


if __name__ == '__main__':
    main()
