# Supplementary Section S3: Screening Calibration, Substitution Test, and Post-Audit Reconciliation

## 1. Dual-Coder Calibration Protocol

To establish inter-rater reliability prior to unassisted screening, two reviewers, blind to each other's decisions and to any automated recommendation, independently screened a random 20% calibration sample ($n = 92$, random seed 42) drawn from the 460-record baseline pool. Reviewers evaluated records using only title, abstract, and publication year; venue, DOI, and source were withheld to prevent prestige bias. Three records whose screening had been informed by worked examples in the reviewer protocol were replaced with three freshly drawn records (random seed 343) before computing agreement.

- **Calibration Agreement:** Reviewers agreed on **79 of 92 decisions (85.9% raw agreement)**, yielding **Cohen's $\kappa = 0.740$** on the four decision labels, which indicates substantial agreement ([Landis & Koch, 1977](https://doi.org/10.2307/2529310)). Cohen's $\kappa$ rises to **$0.803$** (82/92) when the three functionally equivalent but differently labeled Set B decisions count as agreement; under binary include/exclude grouping, $\kappa = 0.800$ (83/92).
- **Protocol Refinements:** Disagreements were reconciled in open discussion and produced two protocol refinements:
  1. **The Substitution Test:** Operationalized MCP specificity under inclusion criterion IC2.
  2. **Set B Scope Restriction:** Restricted Set B strictly to pre-release work conceptually relevant to LLM agent or tool-use security (such as indirect prompt injection [Greshake et al., 2023](https://doi.org/10.1145/3605764.3623985) and dynamic agent security benchmarks [AgentDojo, Debenedetti et al., 2024]), rather than merely any pre-window publication date, after four pre-2024 records on unrelated topics had been misclassified as background.

## 2. The Substitution Test Operational Definition

The Substitution Test operationalizes the boundary between MCP-specific security research and generic LLM agent security:

> **Operational Rule (IC2 Substitution Test):** If a record's security claim survives unchanged when "Model Context Protocol" ("MCP") is replaced by a generic tool-calling framework, the record fails **IC2** (and is excluded under **EC2**), even where MCP is explicitly mentioned in the title or abstract.

On this basis, five records describing generic mechanisms (information-flow control, multi-layer red-teaming, runtime tool-call interception, an agent-skills survey, and metadata-attack detection) were excluded under **EC2**. Conversely, the test retained studies grounded in MCP's own artifacts (server codebases, public registries, or protocol logs) even when security is a minority theme, as well as applied systems that analyze an MCP-specific threat.

Following the sole-inclusion audit (Subsection 3), the criteria for attack and defense papers were recorded as an explicit three-part rule (applied to audited records and all supplementary candidates):
1. **Threat or Mechanism Framing:** The threat or defensive mechanism must be framed as a weakness or requirement of the MCP ecosystem or client-server architecture;
2. **Primary Empirical Grounding:** The central results supporting the claim must come from real MCP servers, tools, or clients (or, for conceptual designs without experiments, the formal mechanism must depend on MCP-specific elements such as JSON-RPC 2.0 methods, `tools/list`, resource templates, or OAuth 2.1 metadata); and
3. **Measurement Alignment:** The reported measurements must directly evaluate the security claim advanced.

## 3. Audit 1: Blind Re-Screening of Single-Coder Sole Inclusions

One reviewer screened the remaining 80% of the baseline pool alone, and subsequently applied the calibrated protocol to the 154 supplementary records. Because agreement on the calibration sample did not guarantee that a single reviewer would apply the substitution test without drift, a post-hoc audit was conducted:

- A second reviewer, blind to the first reviewer's decisions, re-screened **137 of the 138 records** that the first reviewer had included alone in the baseline pool (one record lacked a retrievable abstract) from title, abstract, and publication year.
- After open reconciliation, **37 of the 137 records (27.0%; Wilson 95% confidence interval: 20.3%–35.0%)** were excluded—predominantly generic agent-security or application papers in which MCP served solely as a deployment interface (**EC1**, **EC2**).
- One additional record from the adjudicated batch was excluded during full-text inspection because disambiguation revealed that "MCP" did not refer to the Model Context Protocol (**EC5**).
- Every candidate inclusion from the 154-record supplementary pool underwent full dual-reviewer screening and verification.

## 4. Audit 2: Blind Re-Screening of Single-Coder Sole Exclusions

To test for false-negative exclusions among the **182 sole exclusions** made by the first reviewer in the baseline pool:

- None of the 118 off-topic exclusions (**IC2**) mentioned MCP in the title or abstract; a keyword scan for tool and agent terms flagged 1 record, and 19 additional records (including 12 drawn at random) were selected for manual checking alongside the 64 non-IC2 exclusions (**84 at-risk exclusions in total**).
- The second reviewer, blind to the first reviewer's exclusion codes, re-screened all **84 records** (7 records without an abstract were judged from the title) and **reinstated 0 records** into the synthesis corpus.
- **Exclusion Code Agreement:** The two reviewers agreed on the exact exclusion code for **61 of the 84 records (72.6%)**, with disagreements occurring primarily where a record never mentioned MCP and could plausibly be coded under either **IC2** or **EC2**.
- **Full-Text Resolution of Borderline Cases:** Eleven records that could not be resolved from the abstract alone were inspected in full text. Two empirical taxonomies of real-world MCP software and runtime faults ([Owotogbe et al., 2026](https://doi.org/10.48550/arXiv.2606.05339); [Taraghi et al., 2026](https://doi.org/10.48550/arXiv.2603.05637)) were retained because each grounded its fault categories in mined MCP server codebases, and one proxy architecture was reclassified for inclusion because its controls were built specifically around MCP's client-server model.

## 5. Disposition by Pool and Exact PRISMA Arithmetic Closure

All queries across the six bibliographic databases (arXiv, OpenAlex, Semantic Scholar, IEEE Xplore, Scopus, and ACM Digital Library) and gray-literature sources were executed on **25 September 2026**. Combining the baseline pool (460 unique records) and the supplementary pool (154 net new unique records after removing 59 overlaps with the baseline pool) yields exact arithmetic closure across all **614 screened records**:

| Pool | Screened | MCP-Specific Corpus | Background Set B | Total Extracted | Excluded | Exclusion Breakdown |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Pool** | 460 | 148 | 9 | 157 | 303 | IC2, EC1, EC2, EC3, EC5 |
| **Supplementary Pool** | 154 | 23 | 2 | 25 | 129 | EC5: 81; EC1: 47; EC2: 1 |
| **Consolidated Total** | **614** | **171** | **11** | **182** | **432** | **IC2: 164; EC1: 125; EC2: 56; EC5: 82; EC3: 5; EC4: 0** |

$$\text{Total Screened} = 460\text{ (Baseline)} + 154\text{ (Supplementary)} = 614$$
$$\text{Total Excluded} = 303\text{ (Baseline)} + 129\text{ (Supplementary)} = 432$$
$$\text{Total Extracted} = 157\text{ (Baseline)} + 25\text{ (Supplementary)} = 182$$
$$\text{MCP-Specific Synthesis Corpus} = 148\text{ (Baseline)} + 23\text{ (Supplementary)} = 171$$
$$\text{Background Set B} = 9\text{ (Baseline)} + 2\text{ (Supplementary)} = 11$$

*Note:* The 22-record Tier E4 validation set (20 CVEs and 2 vendor incident disclosures) was retrieved and screened separately (128 raw candidates $\rightarrow$ 31 deduplicated $\rightarrow$ 9 excluded for lacking an MCP protocol binding $\rightarrow$ 22 Tier E4 records) and lies outside the 614-record academic screening pool and the 182 extracted records.
