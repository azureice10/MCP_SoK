# Supplementary Section S3: Screening Calibration, Substitution Test, and Post-Audit Reconciliation

## 1. Dual-Coder Calibration Protocol

To ensure reliability prior to unassisted screening, two reviewers independently screened a 20% random sample ($n = 92$ records) drawn from the 460 baseline pool records. Reviewers independently applied inclusion criteria (IC1: Post-November 2024 timing; IC2: Focus on Model Context Protocol architecture, security, or implementation) and exclusion criteria (EC1–EC5).

- **Calibration Agreement:** Reviewers agreed on 88 of 92 decisions (95.7% raw agreement), yielding Cohen's $\kappa = 0.84$ ($95\%\text{ CI } [0.73, 0.95]$), indicating strong inter-rater reliability.
- **Disagreements:** The 4 discrepant cases involved generic LLM agent security frameworks mentioning tool use without grounding in the JSON-RPC Model Context Protocol specification. Consensus discussions formalized the **Substitution Test** rule.

---

## 2. The Substitution Test Operational Definition

The Substitution Test establishes whether an empirical finding or theoretical defense belongs specifically to the MCP ecosystem:

> **Operational Rule:** An attack or defense paper passes the substitution test if and only if:
> 1. Its threat model or mechanism is framed as a vulnerability, protocol semantic, or requirement of the MCP client-server architecture;
> 2. The empirical results supporting its primary claim were obtained on real MCP servers, tools, or clients (or, for conceptual designs, its formal mechanism depends on MCP-specific protocol constructs such as JSON-RPC methods, resource templates, prompt endpoints, or OAuth 2.0 metadata); and
> 3. Replacing the Model Context Protocol with a generic function-calling API (e.g., OpenAI Tools, ReAct loops) invalidates the technical finding or architectural control.

Works that failed this test—such as generic multi-agent coordination frameworks or benchmark evaluations treating MCP purely as a drop-in transport layer without testing its boundaries—were categorized under **EC1** (application engineering) or **EC2** (generic agent security).

---

## 3. Post-Audit 1: Audit of Single-Coder Inclusions

Following unassisted screening of the remaining 80% baseline pool, an independent post-hoc audit was executed to ensure no drift occurred:
- A second reviewer, blind to the primary coder's inclusions, audited 137 of 138 records included by the single coder (1 record had no retrievable abstract).
- After blind dual-coding and open reconciliation, 37 records (27.0%; Wilson 95% CI: 20.3%–35.0%) were excluded (primarily generic agent security or application papers failing the substitution test under EC1/EC2).
- One additional record was excluded during full-text review when disambiguation revealed "MCP" referred to "Maximum Clique Problem" (EC5).
- Two empirical taxonomy studies (He et al., Owotogbe et al.) were affirmed and retained because their categories were grounded in mined MCP server codebases.

---

## 4. Post-Audit 2: Audit of Single-Coder Exclusions

To verify false-negative exclusion rates:
- The second reviewer audited 84 exclusion decisions (20 randomly selected off-topic exclusions under IC2 and 64 borderline exclusions under EC1/EC2).
- The reviewers agreed on 61 of 84 exclusion codes (72.6%).
- Full-text inspection of 11 borderline exclusions resulted in **0 records reinstated** into the synthesis corpus. One proxy architecture was confirmed for inclusion after verifying its controls operated on the MCP client-server protocol.

---

## 5. Supplementary Search Screening & Arithmetic Closure

During the October 2026 supplementary search phase across IEEE Xplore, ACM DL, and Scopus:
- 154 new deduplicated records were screened directly under the calibrated substitution protocol.
- 129 records were excluded (81 acronym collisions under EC5, 47 domain applications without security analysis under EC1, and 1 generic agent security study under EC2).
- 25 records were included (23 Tier E1 peer-reviewed empirical studies and 2 Set B background papers).
- Combined with the baseline pool, exact arithmetic closure is established across all 614 records:
  $$\text{Total Screened} = 460\text{ (Baseline)} + 154\text{ (Supplementary)} = 614$$
  $$\text{Total Excluded} = 303\text{ (Baseline)} + 129\text{ (Supplementary)} = 432$$
  $$\text{Total Extracted} = 157\text{ (Baseline)} + 25\text{ (Supplementary)} = 182$$
  $$\text{Synthesis Corpus} = 148\text{ (Baseline)} + 23\text{ (Supplementary)} = 171$$
  $$\text{Background Set B} = 9\text{ (Baseline)} + 2\text{ (Supplementary)} = 11$$
