#!/usr/bin/env python3
"""Verify PRISMA arithmetic closure and exclusion reconciliation integrity."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_csv(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def main():
    pool_csv = read_csv(ROOT / 'data/screening/prisma_screening_pool_reconciled_frozen.csv')
    pool_json = json.loads((ROOT / 'data/screening/screening_pool_reconciled.json').read_text(encoding='utf-8'))
    ws = read_csv(ROOT / 'data/screening/exclusion_code_reconciliation_worksheet.csv')
    c179 = read_csv(ROOT / 'data/corpus/mcp_sok_corpus_179_reconciled_frozen.csv')
    c170 = read_csv(ROOT / 'data/corpus/mcp_sok_corpus_170_conservative_frozen.csv')
    setb = read_csv(ROOT / 'data/corpus/background_set_b_11.csv')

    assert len(pool_csv) == 616 and len(pool_json) == 616, f"Expected 616 audit rows, got {len(pool_csv)}"
    assert len(ws) == 106, f"Expected 106 worksheet rows, got {len(ws)}"
    assert len(c179) == 179, f"Expected 179 reconciled corpus rows, got {len(c179)}"
    assert len(c170) == 170, f"Expected 170 conservative corpus rows, got {len(c170)}"
    assert len(setb) == 11, f"Expected 11 Set B rows, got {len(setb)}"

    # Verify zero pending rows and exact pool breakdown
    disp = Counter(r['final_decision'] for r in pool_csv)
    assert disp == {'Include': 190, 'Exclude': 419, 'Duplicate': 7}, f"Unexpected dispositions: {disp}"

    pool_disp = Counter((r['source_pool'], r['final_decision'], r['screening_decision']) for r in pool_csv)
    expected_pool_disp = {
        ('Baseline', 'Include', 'Included (Corpus)'): 157,
        ('Baseline', 'Include', 'Included (Set B)'): 9,
        ('Baseline', 'Exclude', 'Excluded'): 287,
        ('Baseline', 'Duplicate', 'Duplicate (Removed Before Synthesis)'): 7,
        ('Supplementary', 'Include', 'Included (Corpus)'): 22,
        ('Supplementary', 'Include', 'Included (Set B)'): 2,
        ('Supplementary', 'Exclude', 'Excluded'): 132,
    }
    assert dict(pool_disp) == expected_pool_disp, f"Pool attribution mismatch: {pool_disp}"

    # Verify calibration kappa from screening_calibration_sample_92.csv
    cal = read_csv(ROOT / 'data/screening/screening_calibration_sample_92.csv')
    assert len(cal) == 92
    r1 = [r['r1_decision'].strip().lower() for r in cal]
    r2 = [r['r2_decision'].strip().lower() for r in cal]
    agree = sum(a == b for a, b in zip(r1, r2))
    assert agree == 79, f"Expected 79/92 agreement, got {agree}"
    cats = set(r1) | set(r2)
    po = agree / 92.0
    pe = sum(r1.count(c) * r2.count(c) for c in cats) / (92.0 * 92.0)
    kappa = (po - pe) / (1.0 - pe)
    assert abs(kappa - 0.7400) < 1e-3, f"Expected literal 4-way kappa ~0.740, got {kappa:.4f}"

    # Verify exclusion codes
    ex_codes = Counter(r['exclusion_reason'] for r in pool_csv if r['final_decision'] == 'Exclude')
    expected_codes = {'IC2': 149, 'EC1': 124, 'EC5': 84, 'EC2': 55, 'EC3': 5, 'IC3': 2}
    assert dict(ex_codes) == expected_codes, f"Unexpected exclusion codes: {ex_codes}"

    # Verify worksheet has all linkage columns populated
    for r in ws:
        assert r['final_decision'] in {'Include', 'Exclude', 'Duplicate'}, f"Invalid worksheet decision: {r}"
        assert r['version_relation_type'], f"Missing version_relation_type: {r['record_id']}"

    print("[OK] PRISMA arithmetic and exclusion reconciliation verified: 616 audit rows (609 unique) -> 179 Corpus + 11 Set B + 419 Excluded + 7 DUP.")

if __name__ == '__main__':
    main()
