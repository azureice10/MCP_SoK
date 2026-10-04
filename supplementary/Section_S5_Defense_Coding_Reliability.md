# Supplementary Section S5: Defense Coding Reliability, Coder Allocation, and Sensitivity Analysis

## 1. Defense Corpus Composition & Coding Accounting

The defense corpus comprises 85 distinct defense proposals extracted across the 171 synthesis corpus records. Coding was governed by `Pedoman_Pengisian_Lembar_Koding_v1.1.md`.

Coder allocation accounting strictly closes as follows:
- **Blind Dual-Coded Subsample ($n = 20$):** 20 records were independently coded from raw full texts by Koder 1 and Koder 2 without access to each other's workbooks.
- **Audited Supplementary Records ($n = 14$):** 14 new peer-reviewed defense records from the supplementary search phase were coded and verified against the established codebook criteria.
- **Single-Coded Baseline Records ($n = 51$):** 51 baseline records were coded by the primary coder after passing the calibration threshold.
$$\text{Total Defense Records} = 20\text{ (Blind Dual)} + 14\text{ (Audited Supplementary)} + 51\text{ (Single-Coded Baseline)} = 85$$

---

## 2. Inter-Rater Reliability Across Taxonomy & Maturity Dimensions

Dual coding of the 20-paper calibration sample achieved strong consensus across all evaluated dimensions:

| Dimension Evaluated | Categories | Raw Agreement | Cohen's $\kappa$ | 95% Confidence Interval |
| :--- | :---: | :---: | :---: | :---: |
| **Taxonomy Classification** | 16 classes (A1–D3) | 18 / 20 (90.0%) | **0.87** | $[0.72, 1.00]$ |
| **Architectural Boundary Crossing** | 6 boundary types | 18 / 20 (90.0%) | **0.86** | $[0.69, 1.00]$ |
| **Defense Maturity Level** | L0, L1, L2, L3 | 19 / 20 (95.0%) | **0.89** | $[0.74, 1.00]$ |
| **Evaluation Adaptivity** | Yes / No / Unclear | 20 / 20 (100.0%)| **1.00** | $[1.00, 1.00]$ |

---

## 3. Defense Maturity Distribution & Inter-Rater Threshold Sensitivity

Final adjudicated maturity levels across the 85 defenses:
- **Level 0 (Conceptual Architecture / Design without offline or runtime benchmark):** 15 (17.6%)
- **Level 1 (Offline / Proof-of-Concept benchmark against static attack corpus):** 68 (80.0%)
- **Level 2 (Integrated Testbed / Multi-server staging environment):** 2 (2.4%)
- **Level 3 (Hardened Production Deployment with verified longitudinal telemetry):** 0 (0.0%)

### Sensitivity Analysis: Conceptual Proposals (12 vs. 15 records)
During blind dual coding, Koder 2 flagged 3 borderline proposals that included synthetic algorithmic toy traces (e.g., pure JSON string regex tests without an LLM planner). Under a relaxed definition treating synthetic toy scripts as empirical evaluation, Level 0 proposals would count as 12 (14.1%), shifting 3 records into Level 1 (71 records, 83.5%). The consensus decision adhered strictly to the principle that Level 1 requires testing against an active LLM agent or real tool executions, maintaining Level 0 at exactly 15 (17.6%).

---

## 4. Empirical Evaluation of Adaptive Adversaries

Of the 70 empirical defenses (68 Level 1 + 2 Level 2):
- Only **3 defenses (4.3%)** evaluated their proposed mitigations against an adaptive adversary intentionally designed to bypass the defensive mechanism (e.g., iteratively reformulating payloads to circumvent semantic guardrails or embedding evasion tags).
- The remaining 67 empirical evaluations (95.7%) tested exclusively against static, non-adaptive baseline datasets (e.g., fixed prompt injection corpora, historical CVE payloads).
