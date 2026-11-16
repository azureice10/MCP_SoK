import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TestFrozenReconciliationPackage(unittest.TestCase):
    def setUp(self):
        with (ROOT / 'data/screening/exclusion_code_reconciliation_worksheet.csv').open(encoding='utf-8-sig') as f:
            self.ws = list(csv.DictReader(f))
        with (ROOT / 'data/defenses/defenses_88_reconciled_frozen.csv').open(encoding='utf-8-sig') as f:
            self.d88 = {r['record_id']: r for r in csv.DictReader(f)}
        self.pool_json = json.loads((ROOT / 'data/screening/screening_pool_reconciled.json').read_text(encoding='utf-8'))

    def test_no_pending_decisions(self):
        for r in self.pool_json:
            self.assertIn(r['final_decision'], {'Include', 'Exclude', 'Duplicate'})
            if r['final_decision'] == 'Include':
                self.assertEqual(r.get('exclusion_reason', ''), '')
            elif r['final_decision'] == 'Duplicate':
                self.assertEqual(r.get('exclusion_reason', ''), 'DUP')

    def test_worksheet_version_linkage_columns(self):
        self.assertEqual(len(self.ws), 106)
        dups = [r for r in self.ws if r['final_decision'] == 'Duplicate']
        self.assertEqual(len(dups), 7)
        for d in dups:
            self.assertTrue(d['canonical_corpus_id'])
            self.assertTrue(d['canonical_published_doi_or_url'])

    def test_priority_defense_resolutions(self):
        # 1. Hierarchical Approaches: unit of analysis separated (L1 secondary for MCP Firewall component)
        ha = self.d88['hierarchical-approaches-for-2026']
        self.assertEqual(ha['defense_role'], 'defense_secondary')
        self.assertEqual(ha['maturity_level'], 'L1')
        self.assertEqual(ha['classes_evaluated'], 'A2;C5;OUT_OF_TAXONOMY:dns_poisoning')

        # 2. Attested Policy Brokerage: L1 primary
        apb = self.d88['attested-policy-brokerage-2026']
        self.assertEqual(apb['defense_role'], 'defense_primary')
        self.assertEqual(apb['maturity_level'], 'L1')
        self.assertEqual(apb['classes_evaluated'], 'C5')

        # 3. Jalendar/ZPAA & Samuel/Astral confirmed L0 after full-text verification of PDFs
        zpaa = self.d88['jalendar-2025-zero-trust-proof-gated-agent']
        self.assertEqual(zpaa['maturity_level'], 'L0')
        astral = self.d88['samuel-2026-secure-sandbox-environment-orchestrating-medical']
        self.assertEqual(astral['maturity_level'], 'L0')
        self.assertEqual(astral['evidence_tier'], 'E1')

if __name__ == '__main__':
    unittest.main()
