# MCP_SoK: Replication Package & Supplementary Research Dataset

**Paper Title:** *Security of Model Context Protocol in Agentic AI Systems: A Systematization of Knowledge on Threats, Trust Boundaries, and Defense Mechanisms*  
**Journal:** *AI and Security Convergence* (Bon View Publishing)  
**Authors:** Raden Budiarto Hadiprakoso\*, I Komang Setia Buana, and Herman Kabetta (*Politeknik Siber dan Sandi Negara, Indonesia*)  
**Dataset Freeze Status:** `FROZEN_RECONCILED_PUBLICATION_READY` (`2026-11-14`)

---

## 1. Repository Overview

This repository hosts the complete, deduplicated, and cryptographically checksummed replication package for our Systematization of Knowledge (SoK) on the security of the **Model Context Protocol (MCP)**. The manuscript, its figures, and editorial correspondence are not distributed here while the paper is under journal review. The repository contains:
1. **The Analytical Supplementary Material & Standalone Supplementary Research Dataset** (`supplementary/`)
2. **The Frozen Reconciled Screening, Corpus, Defense, and Vulnerability Datasets** (`data/`)
3. **Screening & Defense Coding Codebooks** (`codebooks/`)
4. **Full-Text Verification & Version-Linkage Provenance** (`evidence/` & `reports/`)
5. **Automated Reproduction & CI Verification Scripts** (`scripts/`, `tests/`, `.github/workflows/verify.yml`)

---

## 2. Directory Structure

```text
MCP_SoK/
├── .github/workflows/verify.yml                           # GitHub Actions CI pipeline
├── CITATION.cff                                           # Citation metadata
├── LICENSE                                                # MIT / CC-BY-4.0 License
├── README.md                                              # Repository documentation
├── requirements.txt                                       # Python dependencies
├── supplementary/
│   ├── MCP_SoK_Supplementary_Material_Revised.md          # Tables S1–S7 & Sections S3, S5, S6
│   └── MCP_SoK_Supplementary_Research_Dataset.md          # Standalone Supplementary Dataset (S-Spec, S-E4, S-Corpus, S-Defenses)
├── data/
│   ├── screening/
│   │   ├── baseline_pool_460.csv                          # Phase 1 baseline pool (460 slots)
│   │   ├── supplementary_pool_213_raw.csv                 # Phase 2 supplementary pool (213 deduplicated -> 154 net new)
│   │   ├── screening_calibration_sample_92.csv            # 20% blind calibration sample (n = 92, kappa = 0.740)
│   │   ├── exclusion_code_reconciliation_worksheet.csv    # 106 reconciled exclusions + version-linkage columns
│   │   ├── prisma_screening_pool_reconciled_frozen.csv    # Frozen screening pool (616 audit rows / 609 unique studies)
│   │   └── screening_pool_reconciled.json                 # Full provenance screening ledger (JSON)
│   ├── corpus/
│   │   ├── mcp_sok_corpus_179_reconciled_frozen.csv       # Primary Reconciled MCP-Specific Corpus (N = 179; Skema A)
│   │   ├── mcp_sok_corpus_170_conservative_frozen.csv     # Conservative Sensitivity Corpus (N = 170; Skema B)
│   │   ├── dataset_s3_frozen_corpus_179.csv               # Enriched S-Corpus inventory (179 records; IDs 072, 085, and 088 retired) with venues & DOIs
│   │   └── background_set_b_11.csv                        # Foundational pre-MCP Background Set B (n = 11)
│   ├── defenses/
│   │   ├── defenses_88_reconciled_frozen.csv              # Primary Reconciled Defense Matrix (n = 88; Skema A)
│   │   ├── defenses_84_reconciled_frozen.csv              # Conservative Sensitivity Defense Matrix (n = 84; Skema B)
│   │   └── dataset_s4_frozen_defenses_88.csv              # Enriched S-Def table (88 records; ID 78 retired) with full metadata
│   └── validation/
│       ├── dataset_s1_mcp_specifications.csv              # Normative MCP Specification Revisions (S-Spec-01..07)
│       └── dataset_s2_e4_cves_and_incidents.csv           # Tier E4 Validation Set (20 CVEs + 4 Practitioner Advisories)
├── codebooks/
│   ├── Screening_Operational_Guidelines_v3.md
│   ├── Screening_Substitution_Test_v3.2.md
│   ├── Section_S3_Screening_Calibration_Audit.md
│   └── Defense_Coding_Guidelines_v1.1.md
├── evidence/
│   ├── four_case_evidence.json
│   ├── duplicate_id_evidence.json
│   └── source_recovery_manifest.json
├── reports/
│   └── LAPORAN_PEMBEKUAN_DAN_PERHITUNGAN_ULANG_FINAL.md
├── manifests/
│   └── freeze_manifest_sha256.json                        # SHA-256 checksums of all frozen repository files
├── scripts/
│   ├── verify_prisma_arithmetic.py
│   ├── verify_defense_maturity.py
│   ├── run_audit_checks.py                                # Public checks; manuscript checks run only with a local manuscript/ copy
│   ├── verify_freeze_hashes.py
│   ├── refactor_local_workspace.py
│   ├── build_aisc_docx.py                                 # Authors' tool: builds the journal .docx (needs local manuscript/submission/ sources)
│   ├── make_figure2_trust_zones.py                         # Authors' tool: redraws Figure 2 (local manuscript/ copy)
│   └── check_aisc_compliance.py                           # Authors' tool: journal-rule checks (needs local manuscript/submission/ sources)
└── tests/
    └── test_reconciliation.py
```

---

## 3. Summary of Frozen Reconciled Statistics (`2026-11-14`)

| Metric | Primary Reconciled (`Skema A`) | Conservative Sensitivity (`Skema B`) |
| :--- | :---: | :---: |
| **Combined Screening Audit Rows (`Baseline + Supplementary`)** | **616** (`460 + 156`; `156 = 154 initial + 2 restored Tier E1 defenses`) | **616** (`460 + 156`) |
| **Unique Deduplicated Studies Screened** | **609** (`453 + 156`) | **609** (`453 + 156`) |
| **MCP-Specific Synthesis Corpus (`N`)** | **179** (`157 Baseline + 22 Supp`) | **170** (`148 Baseline + 22 Supp`) |
| **Foundational Background Set B** | **11** | **11** |
| **Total Extracted Studies** | **190** | **181** |
| **Unique Excluded Studies (Outside `DUP`)** | **419** (`IC2:149, EC1:124, EC5:84, EC2:55, EC3:5, IC3:2, EC4:0`) | **428** (`IC2:149, EC1:125, EC5:84, EC2:63, EC3:5, IC3:2, EC4:0`) |
| **Version / Cross-Pool Duplicates Merged (`DUP`)** | **7** Baseline rows (`5` version duplicates + `2` cross-pool Set B duplicates) | **7** Baseline rows (`5` + `2`) |
| **Primary Layers (`A / B / C / D`)** | **90 / 3 / 77 / 9** (`50.3% / 1.7% / 43.0% / 5.0%`) | **88 / 2 / 72 / 8** (`51.8% / 1.2% / 42.4% / 4.7%`) |
| **Coded Defenses (`n`: `primary / secondary / proposal`)** | **88** (`67 / 7 / 14`) | **84** (`65 / 7 / 12`) |
| **Defense Maturity (`L0 / L1 / L2 / L3`)** | **17 / 69 / 2 / 0** (`19.3% / 78.4% / 2.3% / 0.0%`) | **15 / 67 / 2 / 0** (`17.9% / 79.8% / 2.4% / 0.0%`) |
| **Mechanism Families (`Policy / Content / Integrity`)** | **39 / 36 / 13** (`44.3% / 40.9% / 14.8%`) | **36 / 35 / 13** (`42.9% / 41.7% / 15.5%`) |
| **Adaptive Evaluations Among Evaluated (`L1+L2`)** | **2 / 71** (`2.8%`) | **2 / 69** (`2.9%`) |

---

## 4. Running Automated Verification Locally

```bash
python scripts/verify_prisma_arithmetic.py
python scripts/verify_defense_maturity.py
python scripts/run_audit_checks.py
python scripts/verify_freeze_hashes.py
python -m unittest discover -s tests -p "test_reconciliation.py"
```
