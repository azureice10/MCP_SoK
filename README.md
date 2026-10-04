# SoK: Security of the Model Context Protocol (MCP)

[![Audit Verification](https://img.shields.io/badge/Audit%20Checks-33%2F33%20Passing-brightgreen.svg)]()
[![PRISMA Closure](https://img.shields.io/badge/PRISMA%20Pool-614%20Records%20Closed-blue.svg)]()
[![Synthesis Corpus](https://img.shields.io/badge/Corpus-171%20Records-blueviolet.svg)]()
[![License: CC BY 4.0 / MIT](https://img.shields.io/badge/License-CC%20BY%204.0%20%7C%20MIT-lightgrey.svg)]()

This repository contains the complete replication package, research datasets, coding workbooks, supplementary materials, and verification scripts for the paper:

> **SoK: Security of the Model Context Protocol (MCP)**  
> *Systematization of Knowledge on AI Agent Communication Boundaries, Threats, and Defenses.*  
> GitHub Repository: [https://github.com/azureice10/MCP_SoK](https://github.com/azureice10/MCP_SoK)

---

## 📁 Repository Structure

```
MCP_SoK/
├── README.md                                  # Repository overview and reproduction guide
├── LICENSE                                    # Open science dual license (CC-BY-4.0 / MIT)
├── requirements.txt                           # Minimal Python dependencies (pandas, openpyxl)
├── .gitignore                                 # Clean version control exclusions
│
├── manuscript/                                # Paper manuscripts and visual figures
│   ├── MCP_SoK_Manuscript_BonView.md          # Full unconstrained manuscript
│   ├── MCP_SoK_Manuscript_BonView_condensed.md# Journal-ready condensed manuscript
│   └── figures/
│       └── figure_1_prisma.md                 # Reconciled PRISMA-ScR flow diagram (Mermaid)
│
├── data/                                      # Research datasets and corpora
│   ├── screening/
│   │   ├── prisma_screening_pool_614.csv      # Complete PRISMA screening pool (614 records)
│   │   ├── prisma_screening_pool_614.xlsx     # Spreadsheet format of screening pool
│   │   ├── baseline_pool_460.csv              # Initial baseline pool (460 records)
│   │   ├── supplementary_pool_213_raw.csv     # Raw supplementary records (IEEE/ACM/Scopus)
│   │   └── screening_calibration_sample_92.csv# 20% dual-coder calibration sample (κ = 0.84)
│   ├── corpus/
│   │   ├── mcp_sok_corpus_171.csv             # MCP-specific synthesis corpus (171 records)
│   │   ├── mcp_sok_corpus_171.xlsx            # Spreadsheet format of synthesis corpus
│   │   ├── background_set_b_11.csv            # Methodological background Set B (11 records)
│   │   ├── background_set_b_11.xlsx           # Spreadsheet format of Set B
│   │   ├── corpus_metadata_182.csv            # Consolidated extracted corpus (182 records)
│   │   └── corpus_metadata_182.xlsx           # Spreadsheet format of extracted corpus
│   └── validation/
│       ├── e4_validation_set_22.csv           # Held-out E4 validation benchmark (22 records)
│       └── Lembar_Koding_E4_CVE_22.xlsx       # Adjudicated coding workbook for E4 benchmark
│
├── supplementary/                             # Supplementary Information files (S1–S6)
│   ├── Table_S1_Query_Strings_Counts.md       # Search query syntax, sources, and hit counts
│   ├── Table_S2_Data_Extraction_Form.md       # Standardized 21-variable extraction schema
│   ├── Supplementary_Table_S3_Corpus_Layer_Distribution.csv # Distribution across 4 layers
│   ├── Supplementary_Table_S3_Corpus_Layer_Distribution.xlsx
│   ├── Supplementary_Table_S3_Corpus_Layer_Distribution.md
│   ├── Section_S3_Screening_Calibration_Audit.md # Calibration protocol and post-hoc audits
│   ├── Table_S4_E4_Validation_Set.md          # Full 22-record E4 benchmark with CVSS & EPSS
│   ├── Section_S5_Defense_Coding_Reliability.md  # Inter-rater reliability & threshold analysis
│   └── Section_S6_ChainWatch_SAMOS_Resolution.md # Granular resolution of ChainWatch vs SAMOS
│
├── defense/                                   # Defense extraction and coding artifacts
│   ├── codebooks/
│   │   ├── Lembar_Koding_Pertahanan_v1.3_FROZEN.xlsx # Master frozen defense coding workbook
│   │   ├── Lembar_Koding_KODER2_BLIND.xlsx    # Independent blind second-coder workbook
│   │   ├── Pedoman_Pengisian_Lembar_Koding_v1.1.md  # Defense coding codebook and guidelines
│   │   └── LAPORAN_KESEPAKATAN_KODER2_BLIND.md# Dual-coding agreement report (κ = 0.87)
│   └── packets/                               # 88 verbatim evidence locator packets (*.md)
│       ├── attique-2025-internet-healthcare.md
│       ├── barboni-2025-defense-mcp.md
│       └── ... (88 total locator packets)
│
└── scripts/                                   # Automated audit and verification scripts
    ├── run_audit_checks.py                    # Master audit asserting 33 manuscript constants
    ├── verify_prisma_arithmetic.py            # Verification of PRISMA pool arithmetic closure
    └── verify_defense_maturity.py             # Verification of defense maturity distributions
```

---

## 🔬 Core Quantitative Findings

1. **Exact PRISMA Arithmetic Closure:**
   - Consolidated Screening Pool: **614 records** ($460\text{ baseline} + 154\text{ supplementary} = 614$).
   - Total Excluded: **432 records** ($303\text{ baseline} + 129\text{ supplementary} = 432$).
   - Total Extracted: **182 records** ($171\text{ MCP-specific synthesis} + 11\text{ Set B background} = 182$).
   - Dual-coder screening calibration: Cohen's $\kappa = 0.84$ ($n = 92$).

2. **16-Class Taxonomy & External Validation Absorption:**
   - 16 classes structured across 4 layers: Semantic ($A_1$–$A_3$), Protocol ($B_1$–$B_3$), Server/Host ($C_1$–$C_7$), Client UI ($D_1$–$D_3$).
   - Tested against a held-out benchmark of **22 Tier E4 records** (20 CVEs + 2 Vendor Disclosures) across **15 distinct disclosure/product clusters**.
   - **Pre-revision absorption:** 17 of 22 (77.3%; 11 of 15 clusters, 73.3%).
   - **Post-revision absorption:** 20 of 22 (90.9%; 13 of 15 clusters, 86.7%), demonstrating decisive coverage gain after accommodating client-side bridge attacks ($C_6$) and multi-tenant authorization scoping failures ($C_7$).

3. **Defense Maturity Gap & The Adaptivity Deficit:**
   - Evaluated across **85 defense proposals**:
     - Level 0 (Conceptual): **15 (17.6%)**
     - Level 1 (Offline / PoC): **68 (80.0%)**
     - Level 2 (Testbed): **2 (2.4%)**
     - Level 3 (Production): **0 (0.0%)**
   - Inter-rater agreement on defense taxonomy and maturity: Cohen's $\kappa = 0.87$.
   - **Adaptive adversary evaluation:** Only **3 of 70 empirical defenses (4.3%)** evaluated their mitigations against an adaptive attacker.

---

## 🚀 Reproduction & Verification Guide

### Prerequisites
- Python 3.10+
- Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Audit Scripts
1. **Master Manuscript & Data Audit (33 Assertions):**
```bash
python scripts/run_audit_checks.py
```
*Expected Output:* `ALL 33 QUANTITATIVE AND STRUCTURAL ASSERTIONS PASSED PERFECTLY!`

2. **PRISMA Arithmetic Verification:**
```bash
python scripts/verify_prisma_arithmetic.py
```
*Expected Output:* `PRISMA ARITHMETIC VERIFICATION PASSED WITH 100% ACCURACY!`

3. **Defense Maturity Verification:**
```bash
python scripts/verify_defense_maturity.py
```
*Expected Output:* `DEFENSE METRICS AND MATURITY VERIFICATION PASSED WITH 100% ACCURACY!`

---

## 📤 Git Deployment Instructions

To push this clean directory to your GitHub repository:

```bash
# 1. Navigate into the MCP_SoK folder
cd c:\Users\raden\Downloads\mcp_sok\MCP_SoK

# 2. Initialize git repository
git init

# 3. Add all clean repository files
git add .

# 4. Create publication commit
git commit -m "feat: complete research artifact package for MCP SoK (BonView & condensed)"

# 5. Link remote repository
git remote add origin https://github.com/azureice10/MCP_SoK.git

# 6. Set main branch and push
git branch -M main
git push -u origin main --force
```

---

## 📜 Citation

```bibtex
@article{mcp_sok_2026,
  title     = {SoK: Security of the Model Context Protocol (MCP)},
  author    = {Authors Anonymous},
  journal   = {Transactions on Software Engineering and Methodology},
  year      = {2026},
  url       = {https://github.com/azureice10/MCP_SoK}
}
```
