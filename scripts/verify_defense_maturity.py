#!/usr/bin/env python3
"""Verify defense maturity, mechanism families, and Table 14 coverage statistics."""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_csv(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def main():
    c179 = read_csv(ROOT / 'data/corpus/mcp_sok_corpus_179_reconciled_frozen.csv')
    d88 = read_csv(ROOT / 'data/defenses/defenses_88_reconciled_frozen.csv')
    d84 = read_csv(ROOT / 'data/defenses/defenses_84_reconciled_frozen.csv')

    assert len(d88) == 88, f"Expected 88 defenses, got {len(d88)}"
    assert len(d84) == 84, f"Expected 84 conservative defenses, got {len(d84)}"

    # Check 100% synchronization between corpus defense roles and defense table
    corpus_def_ids = {r['record_id'] for r in c179 if r['peran'] in {'defense_primary', 'defense_secondary', 'proposal_only'}}
    d88_ids = {r['record_id'] for r in d88}
    assert corpus_def_ids == d88_ids, "Mismatch between corpus defense IDs and defenses_88_reconciled_frozen.csv"

    mat88 = Counter(r['maturity_level'] for r in d88)
    assert dict(mat88) == {'L0': 17, 'L1': 69, 'L2': 2}, f"Unexpected maturity distribution (n=88): {mat88}"

    mat84 = Counter(r['maturity_level'] for r in d84)
    assert dict(mat84) == {'L0': 15, 'L1': 67, 'L2': 2}, f"Unexpected maturity distribution (n=84): {mat84}"

    roles89 = Counter(r['defense_role'] for r in d88)
    assert dict(roles89) == {'defense_primary': 67, 'defense_secondary': 7, 'proposal_only': 14}, f"Unexpected roles: {roles89}"

    adapt89 = sum(1 for r in d88 if r['maturity_level'] in {'L1', 'L2'} and r['adaptive_evaluation'] == 'Yes')
    assert adapt89 == 2, f"Expected 2 adaptive evaluations (MindGuard, Delegation Broker), got {adapt89}"
    adapt85 = sum(1 for r in d84 if r['maturity_level'] in {'L1', 'L2'} and r['adaptive_evaluation'] == 'Yes')
    assert adapt85 == 2, f"Expected 2 adaptive evaluations in conservative set, got {adapt85}"

    # Verify Table 14 evaluated-class counts (manuscript Section 6.4)
    import re as _re
    def _eval_counts(rows):
        c = Counter()
        for r in rows:
            for x in _re.split(r'[;,]\s*', r['classes_evaluated']):
                if x and not x.startswith('OUT_OF_TAXONOMY'):
                    c[x] += 1
        return dict(c)
    exp89 = {'A1': 23, 'A2': 32, 'A3': 6, 'B1': 12, 'B2': 7, 'B3': 2, 'C1': 16, 'C2': 7, 'C3': 13, 'C5': 29, 'D1': 20, 'D2': 7, 'D3': 8}
    exp85 = {'A1': 22, 'A2': 31, 'A3': 6, 'B1': 11, 'B2': 6, 'B3': 2, 'C1': 16, 'C2': 7, 'C3': 13, 'C5': 28, 'D1': 20, 'D2': 7, 'D3': 8}
    assert _eval_counts(d88) == exp89, f"Table 14 (n=89) mismatch: {_eval_counts(d88)}"
    assert _eval_counts(d84) == exp85, f"Table 14 (n=85) mismatch: {_eval_counts(d84)}"

    # Verify public repository counts (Open-Source Prototype)
    repo89 = sum(1 for r in d88 if r['deployment_status'] == 'Open-Source Prototype')
    repo85 = sum(1 for r in d84 if r['deployment_status'] == 'Open-Source Prototype')
    assert repo89 == 15 and repo85 == 13, f"Expected public repos 15/89 and 13/85, got {repo89}/89 and {repo85}/85"

    # Verify utility_overhead breakdown among evaluated defenses (L1+L2)
    import re
    eval89 = [r['utility_overhead'] for r in d88 if r['maturity_level'] in {'L1', 'L2'}]
    q89 = sum(1 for v in eval89 if v != 'not_reported' and re.search(r'\d', v))
    ql89 = sum(1 for v in eval89 if v != 'not_reported' and not re.search(r'\d', v))
    nr89 = sum(1 for v in eval89 if v == 'not_reported')
    assert (q89, ql89, nr89) == (51, 7, 13), f"Expected overhead (51, 7, 13) on n=71, got {(q89, ql89, nr89)}"

    eval85 = [r['utility_overhead'] for r in d84 if r['maturity_level'] in {'L1', 'L2'}]
    q85 = sum(1 for v in eval85 if v != 'not_reported' and re.search(r'\d', v))
    ql85 = sum(1 for v in eval85 if v != 'not_reported' and not re.search(r'\d', v))
    nr85 = sum(1 for v in eval85 if v == 'not_reported')
    assert (q85, ql85, nr85) == (50, 7, 12), f"Expected overhead (50, 7, 12) on n=69, got {(q85, ql85, nr85)}"

    print("[OK] Defense maturity & corpus synchronization verified: n=88 (L0=17, L1=69, L2=2, L3=0; Adaptive=2/71) & n=84 (L0=15, L1=67, L2=2; Adaptive=2/69).")

if __name__ == '__main__':
    main()
