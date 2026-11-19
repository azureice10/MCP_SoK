# MCP_SoK: Replication Package and Supplementary Research Dataset

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24362766.svg)](https://doi.org/10.5281/zenodo.24362766)

**Paper title:** *Security of the Model Context Protocol in Agentic AI Systems: A Systematization of Knowledge on Threats, Trust Boundaries, and Defense Mechanisms*  
**Journal:** *AI and Security Convergence* (Bon View Publishing), manuscript under review  
**Authors:** Raden Budiarto Hadiprakoso\*, I Komang Setia Buana, and Herman Kabetta (*Politeknik Siber dan Sandi Negara, Indonesia*)

> **Current version: v2 (19 November 2026).** The revised manuscript reports an update search (16 November 2026) and a temporal coverage test of the taxonomy. Its data are in [`v2/`](v2/README.md): 215 corpus studies, 112 defense records, and 256 screened advisories, with SHA-256 checksums and a verification script (`python v2/verify.py`). The manuscript cites the Zenodo archive of release `v2.0.2`, DOI [10.5281/zenodo.24362766](https://doi.org/10.5281/zenodo.24362766) (all versions: [10.5281/zenodo.24362765](https://doi.org/10.5281/zenodo.24362765)). Its `v2/` data are identical to commit [`64bb5a1`](https://github.com/azureice10/MCP_SoK/tree/64bb5a12b8898aba6685dedc75cf03bf68add0cf/v2) (tag `v2.0`).
>
> Everything outside `v2/` is the **v1 replication package of the original search** (frozen 14 November 2026: 179 corpus studies, 88 defense records). It remains the record of the original screening, coding, and audits that v2 builds on.

The manuscript, its figures, and editorial correspondence are not distributed in the current repository tree while the paper is under journal review.

---

## 1. Versions

| Version | Date | Scope | Location |
| :--- | :--- | :--- | :--- |
| **v2** | 19 November 2026 | Original search plus update search; 215 corpus studies (199 conservative), 112 defense records (102 conservative), 256 screened advisories for the temporal coverage test | [`v2/`](v2/README.md) |
| v1 | 14 November 2026 (frozen) | Original search; 179 corpus studies (170 conservative), 88 defense records (84 conservative), 22-record E4 validation set | `supplementary/`, `data/`, `codebooks/`, `evidence/`, `reports/`, `manifests/` |

One v1 corpus record (`S-Corpus-030` / `S-Def-47`) was excluded under IC1 in v2 because its publisher lists 30 March 2024, before the review window. The v1 files are kept unchanged as the frozen record of the original search.

---

## 2. Directory Structure

```text
MCP_SoK/
├── .github/workflows/verify.yml                           # GitHub Actions CI (v1 checks and v2 verification)
├── CITATION.cff                                           # Citation metadata
├── LICENSE                                                # MIT License (code and scripts)
├── LICENSE-DATA                                           # CC BY 4.0 (datasets and documentation)
├── README.md                                              # This file
├── requirements.txt                                       # Python dependencies of the v1 scripts
├── v2/                                                    # Current version (19 November 2026)
│   ├── README.md                                          # Contents, coding conventions, and headline results
│   ├── SHA256SUMS                                         # Checksums of the three v2 CSV files
│   ├── verify.py                                          # Standard-library verification of the v2 counts
│   └── data/
│       ├── dataset_s3_corpus_215_v2.csv                   # 215 MCP-specific studies (199 conservative)
│       ├── dataset_s4_defenses_112_v2.csv                 # 112 defense records (102 conservative)
│       └── dataset_temporal_E4_256.csv                    # 256 screened advisories (216 eligible)
├── supplementary/                                         # v1 supplementary files
│   ├── MCP_SoK_Supplementary_Material_Revised.md          # v1 Tables S1–S7 & Sections S3, S5, S6
│   └── MCP_SoK_Supplementary_Research_Dataset.md          # v1 Supplementary Dataset (S-Spec, S-E4, S-Corpus, S-Defenses)
├── data/                                                  # v1 frozen datasets
│   ├── screening/
│   │   ├── baseline_pool_460.csv                          # Phase 1 baseline pool (460 slots)
│   │   ├── supplementary_pool_213_raw.csv                 # Phase 2 supplementary pool (213 deduplicated -> 154 net new)
│   │   ├── screening_calibration_sample_92.csv            # 20% blind calibration sample (n = 92, kappa = 0.740)
│   │   ├── exclusion_code_reconciliation_worksheet.csv    # 106 reconciled exclusions + version-linkage columns
│   │   ├── prisma_screening_pool_reconciled_frozen.csv    # Frozen screening pool (616 audit rows / 609 unique studies)
│   │   └── screening_pool_reconciled.json                 # Full provenance screening ledger (JSON)
│   ├── corpus/
│   │   ├── mcp_sok_corpus_179_reconciled_frozen.csv       # Primary reconciled MCP-specific corpus (N = 179; Scheme A)
│   │   ├── mcp_sok_corpus_170_conservative_frozen.csv     # Conservative sensitivity corpus (N = 170; Scheme B)
│   │   ├── dataset_s3_frozen_corpus_179.csv               # Enriched S-Corpus inventory (179 records; IDs 072, 085, and 088 retired) with venues & DOIs
│   │   └── background_set_b_11.csv                        # Foundational pre-MCP Background Set B (n = 11)
│   ├── defenses/
│   │   ├── defenses_88_reconciled_frozen.csv              # Primary reconciled defense matrix (n = 88; Scheme A)
│   │   ├── defenses_84_reconciled_frozen.csv              # Conservative sensitivity defense matrix (n = 84; Scheme B)
│   │   └── dataset_s4_frozen_defenses_88.csv              # Enriched S-Def table (88 records; ID 78 retired) with full metadata
│   └── validation/
│       ├── dataset_s1_mcp_specifications.csv              # Normative MCP specification revisions (S-Spec-01..07)
│       └── dataset_s2_e4_cves_and_incidents.csv           # Tier E4 validation set (20 CVEs + 4 practitioner advisories)
├── codebooks/
│   ├── Screening_Operational_Guidelines_v3.md
│   ├── Screening_Substitution_Test_v3.2.md
│   ├── Section_S3_Screening_Calibration_Audit.md
│   └── Defense_Coding_Guidelines_v1.1.md
├── evidence/
│   ├── four_case_evidence.json
│   ├── duplicate_id_evidence.json
│   └── source_recovery_manifest.json                      # Recovered sources; the PDFs themselves are not distributed
├── reports/
│   └── LAPORAN_PEMBEKUAN_DAN_PERHITUNGAN_ULANG_FINAL.md   # v1 freeze and recomputation report (in Indonesian)
├── manifests/
│   └── freeze_manifest_sha256.json                        # SHA-256 checksums of the v1 frozen files, with dated amendments
├── scripts/
│   ├── verify_prisma_arithmetic.py
│   ├── verify_defense_maturity.py
│   ├── run_audit_checks.py                                # Public checks; manuscript checks run only with a local manuscript/ copy
│   ├── verify_freeze_hashes.py
│   ├── refactor_local_workspace.py                        # Authors' tool: archives a local working folder before release
│   ├── build_aisc_docx.py                                 # Authors' tool: builds the journal .docx (needs local manuscript/submission/ sources)
│   ├── make_figure2_trust_zones.py                        # Authors' tool: redraws Figure 2 (local manuscript/ copy)
│   └── check_aisc_compliance.py                           # Authors' tool: journal-rule checks (needs local manuscript/submission/ sources)
└── tests/
    └── test_reconciliation.py
```

---

## 3. Summary Statistics

### 3.1 v2 (19 November 2026)

| Metric | Full corpus | Conservative sensitivity set |
| :--- | :---: | :---: |
| **Records screened** | **916** unique (609 original search + 307 update search) | **916** |
| **MCP-specific synthesis corpus** | **215** (178 retained + 37 new) | **199** |
| **Evidence tiers (`E1 / E2 / E3 / E4`)** | **91 / 119 / 1 / 4** | **85 / 109 / 1 / 4** |
| **Primary layers (`A / B / C / D`)** | **99 / 3 / 99 / 14** | **96 / 2 / 89 / 12** |
| **Defense records (`primary / secondary / proposal`)** | **112** (`83 / 12 / 17`) | **102** (`79 / 10 / 13`) |
| **Defense maturity (`L0 / L1 / L2 / L3`)** | **20 / 90 / 2 / 0** | **16 / 84 / 2 / 0** |
| **Adaptive evaluations among evaluated defenses** | **6 / 92** (6.5%) | **6 / 86** (7.0%) |
| **Temporal coverage test** | **256** screened, **216** eligible: 136 fit a class as written, 53 with an extension, 27 residue | – |

### 3.2 v1, original search (frozen 14 November 2026)

| Metric | Primary Reconciled (`Scheme A`) | Conservative Sensitivity (`Scheme B`) |
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
python v2/verify.py                       # v2: checksums, joins, counts, advisory dates, cluster coverage
python scripts/verify_prisma_arithmetic.py
python scripts/verify_defense_maturity.py
python scripts/run_audit_checks.py
python scripts/verify_freeze_hashes.py
python -m unittest discover -s tests -p "test_reconciliation.py"
```

`v2/verify.py` needs only the Python standard library; the v1 scripts need the packages in `requirements.txt`.

---

## 5. License and Citation

- **Code and scripts** (`scripts/`, `tests/`, `v2/verify.py`, `.github/`): MIT License, see [`LICENSE`](LICENSE).
- **Datasets and documentation** (`data/`, `v2/data/`, `supplementary/`, `codebooks/`, `evidence/`, `reports/`, and the README files): Creative Commons Attribution 4.0 International, see [`LICENSE-DATA`](LICENSE-DATA).

Please cite the paper and this repository using [`CITATION.cff`](CITATION.cff).
