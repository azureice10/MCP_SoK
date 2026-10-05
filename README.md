# SoK: Security of the Model Context Protocol (MCP)

[![Audit Verification](https://img.shields.io/badge/Audit%20Checks-33%2F33%20Passing-brightgreen.svg)]()
[![PRISMA Closure](https://img.shields.io/badge/PRISMA%20Pool-614%20Records%20Closed-blue.svg)]()
[![Synthesis Corpus](https://img.shields.io/badge/Corpus-171%20Records-blueviolet.svg)]()
[![Defense Proposals](https://img.shields.io/badge/Defenses-85%20Proposals-orange.svg)]()
[![License: CC BY 4.0 / MIT](https://img.shields.io/badge/License-CC%20BY%204.0%20%7C%20MIT-lightgrey.svg)]()

This repository contains the complete open-science replication package, research datasets, coding workbooks, operational protocol guidelines, supplementary materials, and automated verification scripts for the paper:

> **SoK: Security of the Model Context Protocol (MCP)**  
> *Systematization of Knowledge on AI Agent Communication Boundaries, Threats, and Defenses.*  
> Target Journal: *AI and Security Convergence* (Bon View Publishing) / *ACM Transactions on Software Engineering and Methodology*  
> GitHub Repository: [https://github.com/azureice10/MCP_SoK](https://github.com/azureice10/MCP_SoK)

---

## 📁 Repository Structure

```
MCP_SoK/
├── README.md                                  # Comprehensive replication guide and artifact inventory
├── LICENSE                                    # Open science dual license (CC-BY-4.0 / MIT)
├── requirements.txt                           # Minimal Python dependencies (pandas>=2.0.0, openpyxl>=3.1.0)
├── .gitignore                                 # Clean version control exclusions
│
├── manuscript/                                # Camera-ready and journal manuscripts
│   ├── MCP_SoK_Manuscript_BonView.md          # Full unconstrained manuscript (Bon View format)
│   ├── MCP_SoK_Manuscript_BonView_condensed.md# Journal-ready condensed manuscript
│   ├── MCP_SoK_Manuscript_AISC.docx           # Official submission document for AI and Security Convergence
│   └── figures/                               # Visual and vector figures
│       ├── figure1_prisma_flow.png            # High-resolution PRISMA-ScR flow diagram
│       ├── figure2_trust_zones.png            # High-resolution trust zones & architectural channels diagram
│       └── figure_1_prisma.md                 # Verifiable Mermaid vector source of PRISMA diagram
│
├── data/                                      # Research datasets and corpora
│   ├── screening/                             # Identification & screening pools
│   │   ├── prisma_screening_pool_614.csv      # Complete PRISMA screening pool (614 unique records)
│   │   ├── prisma_screening_pool_614.xlsx     # Spreadsheet format of complete screening pool
│   │   ├── baseline_pool_460.csv              # Initial baseline pool (460 records)
│   │   ├── supplementary_pool_213_raw.csv     # Raw supplementary records (IEEE/ACM/Scopus)
│   │   └── screening_calibration_sample_92.csv# 20% dual-coder calibration sample (κ = 0.84)
│   ├── corpus/                                # Extracted synthesis literature
│   │   ├── mcp_sok_corpus_171.csv             # MCP-specific synthesis corpus (171 records)
│   │   ├── mcp_sok_corpus_171.xlsx            # Spreadsheet format of synthesis corpus
│   │   ├── background_set_b_11.csv            # Methodological background Set B (11 foundational records)
│   │   ├── background_set_b_11.xlsx           # Spreadsheet format of Set B
│   │   ├── corpus_metadata_182.csv            # Consolidated extracted corpus (171 + 11 = 182 records)
│   │   └── corpus_metadata_182.xlsx           # Spreadsheet format of extracted corpus
│   └── validation/                            # Held-out empirical benchmark
│       ├── e4_validation_set_22.csv           # Held-out E4 validation benchmark (20 CVEs + 2 Disclosures)
│       ├── e4_validation_set_22_english.csv   # English column-mapped E4 validation dataset
│       ├── E4_Validation_Coding_Sheet_22.xlsx # English adjudicated coding sheet for E4 benchmark
│       └── Lembar_Koding_E4_CVE_22.xlsx       # Indonesian original adjudicated E4 coding sheet
│
├── supplementary/                             # Supplementary Information files (S1–S6)
│   ├── MCP_SoK_Supplementary_Material.md      # Unified, complete Supplementary Information document
│   ├── Table_S1_Query_Strings_Counts.md       # Full search query strings, filters, and hit counts
│   ├── Table_S2_Data_Extraction_Form.md       # Standardized 21-variable data extraction schema
│   ├── Supplementary_Table_S3_Corpus_Layer_Distribution.csv # Distribution across 4 architectural layers
│   ├── Supplementary_Table_S3_Corpus_Layer_Distribution.xlsx
│   ├── Supplementary_Table_S3_Corpus_Layer_Distribution.md
│   ├── Section_S3_Screening_Calibration_Audit.md # Calibration protocol and post-hoc audits
│   ├── Table_S4_E4_Validation_Set.md          # Full 22-record E4 benchmark with CVSS & EPSS details
│   ├── Section_S5_Defense_Coding_Reliability.md  # Inter-rater reliability & threshold sensitivity
│   └── Section_S6_ChainWatch_SAMOS_Resolution.md # Architectural resolution of ChainWatch vs SAMOS
│
├── defense/                                   # Defense extraction, protocols, and evidence packets
│   ├── codebooks/                             # Operational protocols, coding sheets, and audit reports
│   │   ├── Defense_Coding_Guidelines_v1.1.md  # [English] Operational coding guidelines for defense extraction
│   │   ├── Screening_Operational_Guidelines_v3.md # [English] PRISMA screening & Substitution Test protocol
│   │   ├── Screening_Substitution_Test_v3.2.md # [English] Addendum A1 on empirical evidence criteria
│   │   ├── BLIND_SECOND_CODER_AGREEMENT_REPORT.md # [English] Inter-rater reliability audit report (κ = 0.87)
│   │   ├── Defense_Coding_Workbook_v1.3_FROZEN.xlsx # [English] Master frozen defense coding workbook
│   │   ├── BLIND_CODER2_Workbook.xlsx         # [English] Independent blind second-coder workbook
│   │   ├── defenses_85_consolidated.csv       # Consolidated dataset of 85 defense proposals
│   │   ├── defenses_85_consolidated.xlsx      # Consolidated spreadsheet of 85 defense proposals
│   │   ├── Pedoman_Pengisian_Lembar_Koding_v1.1.md # [Archival] Indonesian original defense guidelines
│   │   ├── LAPORAN_KESEPAKATAN_KODER2_BLIND.md# [Archival] Indonesian original agreement report
│   │   ├── Lembar_Koding_Pertahanan_v1.3_FROZEN.xlsx # [Archival] Indonesian original frozen workbook
│   │   └── Lembar_Koding_KODER2_BLIND.xlsx    # [Archival] Indonesian original blind coder workbook
│   └── packets/                               # 88 verbatim evidence locator packets (*.md)
│       ├── attique-2025-internet-healthcare.md
│       ├── barboni-2025-defense-mcp.md
│       └── ... (88 total locator packets with exact character offsets)
│
└── scripts/                                   # Automated audit and verification scripts
    ├── run_audit_checks.py                    # Master audit verifying 33 critical manuscript assertions
    ├── verify_prisma_arithmetic.py            # Mathematical verification of PRISMA pool closure (614)
    └── verify_defense_maturity.py             # Verification of defense maturity and adaptivity metrics
```

---

## 📖 Operational Protocols & Guidelines Overview

All operational guidelines in `defense/codebooks/` have been translated and standardized into professional academic English:

1. **[`Defense_Coding_Guidelines_v1.1.md`](defense/codebooks/Defense_Coding_Guidelines_v1.1.md)**:
   - Sets strict, inviolable rules for defense coding: no guessing, no unverified defaults, and coding from methods/evaluation sections rather than abstracts.
   - Defines the sequential role classification scheme (`defense_primary`, `defense_secondary`, `proposal_only`, `attack`, `survey_review`, `benchmark_measurement`, `position_other`, `not_defense`).
   - Specifies operational criteria for defense paradigms, enforcement points ($H, C, S, \text{gateway}, \Theta, X$), claimed vs. evaluated taxonomy classes ($A_1$–$D_3$), maturity levels ($L_0$–$L_3$), and the strict 3-question test for adaptive evaluation.

2. **[`Screening_Operational_Guidelines_v3.md`](defense/codebooks/Screening_Operational_Guidelines_v3.md)**:
   - Governs title and abstract screening under the PRISMA-ScR protocol.
   - Outlines sequential decision gates ($G_0$–$G_6$) for year, language, acronym disambiguation, and security focus.
   - Formalizes the **Substitution Test**: mental substitution of "MCP" with "a generic API tool-calling framework" to isolate MCP-specific vulnerabilities from generic LLM agent behaviors.
   - Defines the three preserved exceptions: $P_1$ (MCP as empirical study object), $P_2$ (MCP as specific architectural target), and $P_3$ (comparative protocol clause).

3. **[`Screening_Substitution_Test_v3.2.md`](defense/codebooks/Screening_Substitution_Test_v3.2.md)**:
   - Addendum A1 established during screening audits to eliminate generic multi-agent false positives.
   - Requires empirical evidence on real MCP servers, tools, or clients ($A_{1b}$), alignment of metrics with claimed propositions ($A_{1c}$), and threat formulation within MCP architectural boundaries ($A_{1a}$).

4. **[`BLIND_SECOND_CODER_AGREEMENT_REPORT.md`](defense/codebooks/BLIND_SECOND_CODER_AGREEMENT_REPORT.md)**:
   - Full statistical documentation of independent blind dual-coding across a representative random sample of 38 papers.
   - Documents 100% agreement on binary defense classification ($\kappa = 1.00$), 92.11% on granular role ($\kappa = 0.90$), 100% on maturity level ($\kappa = 1.00$), and 100% on adversary adaptivity ($\kappa = 1.00$).

---

## 🔬 Core Quantitative Findings

1. **Exact PRISMA Arithmetic Closure:**
   - Consolidated Screening Pool: **614 unique records** ($460\text{ baseline} + 154\text{ supplementary} = 614$).
   - Total Excluded: **432 records** ($303\text{ baseline} + 129\text{ supplementary} = 432$).
   - Total Extracted: **182 records** ($171\text{ MCP-specific synthesis} + 11\text{ Set B background} = 182$).
   - Dual-coder screening calibration: Cohen's $\kappa = 0.84$ ($n = 92$).

2. **16-Class Taxonomy & External Validation Absorption:**
   - 16 classes structured across 4 architectural layers: Semantic ($A_1$–$A_3$), Protocol ($B_1$–$B_3$), Server/Host ($C_1$–$C_7$), Client UI ($D_1$–$D_3$).
   - Tested against a held-out benchmark of **22 Tier E4 records** (20 CVEs + 2 Vendor Disclosures) across **15 distinct disclosure/product clusters**.
   - **Pre-revision absorption:** 17 of 22 (77.3%; 11 of 15 clusters, 73.3%).
   - **Post-revision absorption:** 20 of 22 (90.9%; 13 of 15 clusters, 86.7%), demonstrating decisive coverage gain after accommodating client-side bridge attacks ($C_6$) and multi-tenant authorization scoping failures ($C_7$).

3. **Defense Maturity Gap & The Adaptivity Deficit:**
   - Evaluated across **85 defense proposals**:
     - Level 0 (Conceptual Architecture): **15 (17.6%)**
     - Level 1 (Offline / Proof-of-Concept): **68 (80.0%)**
     - Level 2 (Integrated Testbed / Staging): **2 (2.4%)**
     - Level 3 (Hardened Production Deployment): **0 (0.0%)**
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

### Running the Automated Audit Suite
Run all three independent verification scripts:

1. **Master Manuscript & Structural Assertion Audit (33 Checks):**
```bash
python scripts/run_audit_checks.py
```
*Expected Output:* `ALL 33 QUANTITATIVE AND STRUCTURAL ASSERTIONS PASSED PERFECTLY!`

2. **PRISMA Pool Arithmetic Verification:**
```bash
python scripts/verify_prisma_arithmetic.py
```
*Expected Output:* `PRISMA ARITHMETIC VERIFICATION PASSED WITH 100% ACCURACY!`

3. **Defense Maturity & Adaptivity Verification:**
```bash
python scripts/verify_defense_maturity.py
```
*Expected Output:* `DEFENSE METRICS AND MATURITY VERIFICATION PASSED WITH 100% ACCURACY!`

---

## 📤 Git Deployment Instructions

To synchronize this clean repository with GitHub:

```bash
# 1. Navigate into the MCP_SoK folder
cd c:\Users\raden\Downloads\mcp_sok\MCP_SoK

# 2. Stage all files
git add .

# 3. Create publication commit
git commit -m "feat: complete internationalized research artifact package with English protocols and workbooks"

# 4. Push to remote repository
git push -u origin main
```

---

## 📜 Citation

```bibtex
@article{mcp_sok_2026,
  title     = {SoK: Security of the Model Context Protocol (MCP)},
  author    = {Authors Anonymous},
  journal   = {AI and Security Convergence},
  year      = {2026},
  publisher = {Bon View Publishing},
  url       = {https://github.com/azureice10/MCP_SoK}
}
```
