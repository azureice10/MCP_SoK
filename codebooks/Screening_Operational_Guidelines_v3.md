# Operational Screening Guidelines and Substitution Test (v3)

**For Corpus Audit & Replication Reviewers.**  
Applies to blinded screening of identified records using only title, abstract, and publication year. This protocol supersedes v2 and operationalizes the PRISMA-ScR inclusion/exclusion criteria for the systematic review on the Security of the Model Context Protocol (MCP).

---

## 0. Reviewer Role & Independence Rules

Reviewers re-screen records **independently and blinded**: deciding `include`, `exclude`, or `borderline` based solely on **title, abstract, and year**. Reviewer decisions are subsequently compared against independent coder records to measure screening reliability. Independence is structural:

1. **Do not inspect prior decisions**, and do not discuss records with any co-reviewer until all decisions are submitted.
2. **Do not solicit recommendations from generative AI tools** or automated agents during screening. Decisions must reflect your own appraisal of the candidate text.
3. **Do not infer target pool compositions.** Target proportions of inclusions/exclusions are unknown and must not bias borderline adjudications.
4. **Do not read full texts during the initial screening round.** Full texts may only be inspected for records marked `borderline` during Stage 2 adjudication (Section 8).
5. **Evaluate each record independently** on its own merits without cross-record comparisons.

Estimated review duration: 3–4 minutes per record.

---

## 1. Data Schema

| Field | Content |
|---|---|
| `record_id`, `title`, `abstract`, `year` | Source bibliographic metadata (read-only) |
| `decision` | Permissible values: `include` · `exclude` · `borderline` · `set_b` |
| `exclusion_code` | Mandatory if `exclude`: `IC1`, `IC2`, `IC3`, `IC4`, `EC1`, `EC2`, `EC3`, `EC5` (blank for other decisions) |
| `note` | Mandatory: specific textual justification per Section 7 |

---

## 2. Eligibility Criteria Summary

**Review Scope:** Research addressing the **security of the Model Context Protocol (MCP)**—the protocol introduced by Anthropic (November 2024) to connect LLM planners with tools and resources via a client-server JSON-RPC architecture.

| Code | Criterion Description |
|---|---|
| **IC1** | Published or deposited between 25 November 2024 and 25 September 2026. |
| **IC2** | Specifically addresses MCP security: attacks, vulnerabilities, threat models, authentication/authorization, defenses, or ecosystem security measurements; or evaluates MCP against another tool paradigm on security grounds. |
| **IC3** | Written in English. |
| **IC4** | Peer-reviewed publication, preprint with empirical/formal evaluation, normative specification, official guidance, or vendor disclosure with reproducible PoC/CVE. |
| **EC1** | MCP serves purely as generic engineering plumbing or domain interface without MCP-specific security claims. |
| **EC2** | Generic LLM agent security without analysis of MCP-specific protocol constructs or architecture. |
| **EC3** | Opinion piece, marketing material, or claim devoid of traceable technical evidence. |
| **EC5** | Acronym collision where "MCP" refers to an unrelated domain (e.g., Medical Countermeasures, Multi-Chip Package, Maximum Clique Problem). |

---

## 3. Sequential Decision Flowchart

Execute gates **in sequential order**; halt at the first gate yielding a definitive decision:

- **G0. Publication Year:**
  - Year < 2024 $\rightarrow$ If conceptually foundational to LLM agent/tool security (e.g., indirect prompt injection, tool safety benchmarks), classify as `set_b`. If unrelated to agents/LLMs, `exclude` under `IC2`. Date alone is insufficient for `set_b`.
  - Year = 2024 $\rightarrow$ Verify date window (post-Nov 25, 2024). Evaluate topic via subsequent gates; if included, flag "check 2024 date" in `note`.
- **G1. Language:** Non-English text $\rightarrow$ `exclude`, `IC3`.
- **G2. Acronym Disambiguation:** Abstract must reference LLMs, AI agents, tools, MCP servers, JSON-RPC, or Anthropic. If "MCP" clearly refers to unrelated hardware or medical programs $\rightarrow$ `exclude`, `EC5`.
- **G3. MCP Mention:** Does the title, abstract, or contribution mention MCP? No $\rightarrow$ `exclude`, `IC2`.
- **G4. Security Contribution:** Is the primary contribution security-related (attacks, defenses, threat modeling, authorization, data exfiltration)? No $\rightarrow$ `exclude`, `EC1`. If yes $\rightarrow$ proceed to G5.
- **G5. The Substitution Test (Section 4):** Apply test and document the outcome.
- **G6. Evidence Traceability:** Does the work contain traceable empirical methods, data, or formal analysis? No $\rightarrow$ `exclude`, `EC3`. If yes $\rightarrow$ `include`.

---

## 4. The Substitution Test Operational Definition

Mental experiment: Replace every mention of "MCP" in the title and abstract with *"a generic API tool-calling framework"*. Then ask: **does the core security claim or finding remain intact?**

### 4.1 Outcome: "Claim Remains Intact" $\rightarrow$ Generic Paper
Preliminary verdict: `exclude`, `EC2` (if security contribution) or `EC1` (if non-security). **Unless** one of the three exceptions in Section 4.2 applies.

Signs of generic papers: MCP is mentioned merely as "one example", "one supported protocol", "a deployment interface", or "plumbing"; attack vectors are described without referencing MCP-specific constructs.

### 4.2 Three Preserved Exceptions ($\rightarrow$ `include`)
- **P1. MCP as an Empirical Study Object:** Data, server codebases, registry catalogs, or telemetry logs originate from real MCP deployments, such that substitution is impossible without losing the empirical corpus.
- **P2. MCP as a Specific Architectural Target:** The addressed vulnerability or defense is formulated around MCP's own protocol constructs (e.g., dynamic tool schemas, transport endpoints, OAuth discovery, tool list change notifications).
- **P3. Comparative Protocol Clause:** The work explicitly compares MCP with at least one alternative agent protocol along security dimensions.
- **Mixed Application Clause:** Domain applications embedding a dedicated MCP threat model or containment sandbox grounded in real MCP security incidents $\rightarrow$ `include` (document MCP-specific section in `note`).

### 4.3 Outcome: "Claim Collapses Without MCP" $\rightarrow$ `include`
The security mechanism depends directly on MCP features (JSON-RPC tool definitions, prompt templates, resource endpoints, client-server trust boundaries).

### 4.4 Mandatory Substitution Sentence
Every record reaching Gate 5 must include a standardized justification in `note`:
> **Substitution:** If MCP is replaced with a generic tool-calling framework, the central claim [remains intact / collapses] because ___. **Exception:** [None / P1 / P2 / P3].

---

## 5. Decision Rules for Common Edge Cases

| Scenario | Decision |
|---|---|
| Attack or vulnerability analysis targeting MCP mechanisms | `include` |
| Defense built specifically around MCP protocol boundaries | `include` |
| Generic multi-agent security framework mentioning MCP as an adapter | `exclude`, `EC2` |
| Domain application using MCP purely for tool plumbing | `exclude`, `EC1` |
| Tool dataset or registry crawler without security evaluation | `exclude`, `EC1` |
| Systematic review, taxonomy, or SoK on MCP security | `include` |
| Multi-agent protocol survey comparing MCP with security metrics | `include` (P3) |
| Position paper devoid of empirical evaluation or formal methods | `exclude`, `EC3` |
| Security advisory (CVE) on MCP server or SDK | `include` (E4 validation set) |

---

## 6. Guidelines for `borderline` Decisions

Use `borderline` only when a specific criterion cannot be adjudicated from the abstract alone (e.g., unclear whether evaluated on real MCP servers vs. synthetic mocks). Explicitly state the unresolved criterion and the question to be resolved by full-text review. If more than 15% of records are marked `borderline`, pause and recalibrate with the screening coordinator.

---

## 7. Stage 2 Full-Text Resolution for `borderline` Records

For records marked `borderline` during Stage 1:
1. Inspect the full text of the methods and evaluation sections.
2. Update decision to `include` or `exclude`.
3. Prefix the updated `note` with `"FT:"` citing the specific section and page number resolving the criterion.

---

## 8. Calibrated Worked Examples

| # | Abstract Summary | Verdict & Rationale |
|:---:|:---|:---|
| 1 | Tool poisoning analysis: hidden instructions in MCP server tool descriptions steer agent planning; evaluated across 12 MCP clients | `include`. Substitution collapses because dynamic MCP tool descriptions provide the injection vector. |
| 2 | Logistics agent using MCP for parcel tracking; adds input regex filter and measures delivery schedule accuracy | `exclude`, `EC1`. Domain functionality; MCP is plumbing; security is not a core contribution. |
| 3 | Access control framework for LLM agents; MCP mentioned in conclusion as one deployment option | `exclude`, `EC2`. Substitution: claim remains intact; no P1/P2/P3. |
| 4 | Security measurement of 5,000 public MCP servers: analyzing authentication rates and exposed endpoints | `include` (P1). Empirical corpus mined from real MCP servers. |
| 5 | Custom MCP proxy addressing local transport hijacking; adds multi-layer execution sandbox | `include` (P2). Mechanism targets MCP client-server transport boundaries. |
| 6 | Dataset of 60,000 MCP server repositories "to facilitate security research"; no vulnerability mining | `exclude`, `EC1`. Downstream benefit only. |
| 7 | Multi-agent protocol comparing adversarial robustness against MCP in empirical experiments | `include` (P3). Comparative protocol evaluation. |
| 8 | 2023 paper on indirect prompt injection benchmarks for tool-augmented LLMs | `set_b`. Foundational background literature on agent tool security. |
| 9 | "MCP" refers to a signal processing chip in biomedical telemetry | `exclude`, `EC5`. Non-protocol acronym collision. |
