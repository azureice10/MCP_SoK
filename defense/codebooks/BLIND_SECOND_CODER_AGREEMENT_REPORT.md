# Final Report: Blind Second-Coder Coding Sheet & Inter-Coder Agreement Analysis

**Reference Documents:** `Defense_Coding_Guidelines_v1.1.md`  
**Source Workbooks:**
- Coder 1 (Master Corpus): `Lembar_Koding_Pertahanan_v1.3_FROZEN.xlsx` / `Defense_Coding_Workbook_v1.3_FROZEN.xlsx`
- Coder 2 (Blind Sample 38): `Lembar_Koding_KODER2_BLIND.xlsx` / `BLIND_CODER2_Workbook.xlsx`  
**Execution Timestamp:** September 2026  
**Formula Audit Status:** **100% Clean (38/38 rows populated, 0 CHECK / 0 Errors)**

---

## 1. Executive Summary & Coding Protocol

Blind second-coding was conducted completely independently on a **representative random sample of 38 papers** drawn from the final baseline pool. Coder 2 was blind to Coder 1's decisions and automated suggestions, evaluating papers across 4 verified sequential batches:
- **Batch 1 (Rows 2–11, 10 records):** `saeid-2025` through `pei-2026` — Completed & Verified
- **Batch 2 (Rows 12–21, 10 records):** `zhiqiang-2025` through `herman-2025` — Completed & Verified
- **Batch 3 (Rows 22–30, 9 records):** `nicola-2025` through `shiqiang-2025` — Completed & Verified
- **Batch 4 (Rows 31–39, 9 records):** `ping-2026` through `murali-2026` — Completed & Verified

All logical validation constraints (the `consistency_check` formula) were 100% satisfied without discrepancy (`0 CHECK`).

---

## 2. Coder 2 Role Distribution

| Granular Role | Count | Percentage | Binary Classification |
| :--- | :---: | :---: | :--- |
| `defense_primary` | 10 | 26.32% | **Defense Contributions (21 papers / 55.26%)** |
| `defense_secondary` | 4 | 10.53% | |
| `proposal_only` | 7 | 18.42% | |
| `benchmark_measurement` | 5 | 13.16% | **Non-Defense Literature (17 papers / 44.74%)** |
| `survey_review` | 5 | 13.16% | |
| `attack` | 5 | 13.16% | |
| `position_other` | 1 | 2.63% | |
| `not_defense` | 1 | 2.63% | |
| **Total Sample** | **38** | **100.0%** | **38 Papers** |

---

## 3. Statistical Inter-Coder Agreement Results

### A. Paper Role Classification ($N = 38$)

| Evaluated Dimension | Observed Agreement | Cohen's Kappa ($\kappa$) | Standard Interpretation (Landis & Koch, 1977) |
| :--- | :---: | :---: | :--- |
| **Binary Role** (*Defense* vs. *Non-Defense*) | **100.00%** (38/38) | **1.0000** | **Perfect Agreement** |
| **Granular Role** (8 Categories) | **92.11%** (35/38) | **0.9044** | **Almost Perfect Agreement** ($\kappa \ge 0.81$) |

### B. Technical Defense Dimensions on Mutually Agreed Defenses ($N = 21$)

| Coding Dimension | Workbook Variable | Observed Agreement | Cohen's Kappa ($\kappa$) | Agreement Strength |
| :--- | :--- | :---: | :---: | :--- |
| **Maturity Level** | `maturitas (otomatis)` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |
| **Adversary Adaptivity** | `adaptif` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |
| **Evaluation Type** | `jenis_evaluasi` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |
| **LLM in Decision Path** | `llm_dlm_keputusan` | **95.24%** (20/21) | **0.9261** | **Almost Perfect Agreement** |
| **Deployment Status** | `deployment` | **90.48%** (19/21) | **0.8409** | **Almost Perfect Agreement** |
| **Attack Set Origin** | `asal_set_serangan` | **85.71%** (18/21) | **0.7812** | **Substantial Agreement** |
| **Enforcement Point** | `titik_penegakan` | **80.95%** (17/21) | **0.6441** | **Substantial Agreement** |
| **Defense Paradigm** | `paradigma` | **71.43%** (15/21) | **0.6348** | **Substantial Agreement** |
| **Utility / Overhead Metric**| `biaya_utilitas` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |

### C. Multi-Label Set Overlap (*Mean Jaccard Similarity*, $N = 21$)

- **Boundary Crossings (`crossings`, R1–R7):** **0.6786** (*Substantial Overlap*)
- **Attack Classes Claimed (`kelas_diklaim`, A1–D3):** **0.5825** (*Moderate-to-Substantial Overlap*)
- **Attack Classes Evaluated (`kelas_dievaluasi`):** **0.7667** (*High Empirical Overlap*)

---

## 4. Discrepancy Analysis & Methodological Reconciliation

Three papers exhibited granular role disagreements where Coder 1 assigned `defense_primary` while Coder 2 assigned `proposal_only`. All three remained strictly within the defense domain (*100% binary defense agreement*):

1. **`om-2026-chainwatch-kill-chain-aligned-sequential`**
   - *Coder 1:* `defense_primary`
   - *Coder 2:* `proposal_only`
   - *Reconciliation Rationale:* The paper presents a concrete sequential mitigation architecture but lacks empirical quantitative experiments (`evaluation_type = none`). Coder 2 conservatively treated it as a conceptual proposal. Both coders unanimously agreed on maturity level **L0**.
2. **`gamini-2026-mcp-secure-runtime-access-control`**
   - *Coder 1:* `defense_primary`
   - *Coder 2:* `proposal_only`
   - *Reconciliation Rationale:* The full text was behind an access challenge during the second coder's run. Coder 1 coded from the verified technical summary, whereas Coder 2 withheld empirical validation until direct access. Both agreed the paper specifies an access control defense.
3. **`shiqiang-2025-secure-model-context-protocol-large`**
   - *Coder 1:* `defense_primary`
   - *Coder 2:* `proposal_only`
   - *Reconciliation Rationale:* Analogous to Gamini-2026, paywalled archival status led Coder 2 to conservatively code it as a conceptual proposal.

---

## 5. Key Empirical Findings Confirmed Independently

1. **The Adaptive Adversary Deficit:**
   - Both coders independently confirmed that **0 out of 21 evaluated defense systems** evaluated their mitigations against an adaptive adversary intentionally designed to evade the defense ($\kappa = 1.0000$). This corroborates the central finding of Section 6 that published MCP agent defenses are vulnerable to adaptive evasion.
2. **The Independence Deficit:**
   - Zero papers in the sample were independently evaluated by third parties or integrated into external evaluation harnesses (0 Level 2 papers in sample, $\kappa = 1.0000$).
3. **Production Deployment Grounding (Maturity L3):**
   - Both coders corroborated ADR (`chenning-2026-adr-agentic-detection-system-enterprise`) as the sole production-evaluated deployment candidate meeting L3 criteria, grounded in documented production deployment telemetry.
