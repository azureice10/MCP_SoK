# Addendum A1: Screening Operational Protocol and Substitution Test (v3 → v3.2)

Established by the coordinator after the first follow-up audit. Applies to all subsequent screenings (including exclusion audits) and reported in Section 2.6 as a protocol refinement made after audit. Placed as an addition to Sections 4.2 and 5 of the v3 screening protocol.

---

## A1. Attack or Defense Papers Targeting MCP

A1 is a special case of exclusion criteria P1 and P2 for papers whose primary contribution is attack or defense. Papers pass through A1 only if **A1a, A1b, and A1c are all satisfied**. The substitution sentence (Section 4.4) remains mandatory.

**A1a. Threat framework.** The threat or mechanism is formulated as a weakness or requirement of the MCP ecosystem or architecture, for example:
- Trust in third-party tool providers or MCP servers
- MCP tool description or response channels
- Composition of calls across multiple MCP servers
- MCP configuration, registration, or transport

**A1b. Primary evidence.** **Primary results** supporting the core claim are obtained on real MCP servers, tools, or clients. Results on generic simulation environments may exist but do not count as MCP evidence. Demonstration on real MCP infrastructure that successfully supports MCP-specific claims (e.g., two real MCP clients) suffices, whereas tests on real clients showing attack failed do not. For designs without experiments, the design mechanism itself must depend on MCP-specific elements (e.g., proxy position between client and server, tool definitions, `tools/list`, MCP configuration files).

**A1c. Reported measurements.** The reported metrics must measure the claimed proposition. Passing rates on benign benchmarks do not count as attack evidence (EC3 if no other traceable measurements exist).

**Exclude (EC2) if any of the following apply:**
- Primary results obtained on multi-format benchmark or generic API function calling, where MCP appeared only in additional validation or as one tool format among many
- Authors themselves concluded the vulnerability or mechanism is general for LLM-based agents (e.g., "resides in the model layer," applies to any agent loop)
- Feature or mechanism does not use any MCP structure

---

## Warning About Abstracts

Abstracts often mention MCP more strongly than the paper's content. If A1b cannot be confirmed from the abstract, mark `borderline` and decide from the methods and results sections, not from the word "MCP" in the title or abstract.

---

## Calibrated Examples (Hypothetical)

| # | Summary | Decision |
|:---:|:---|:---|
| A1-1 | Attack modifies response text of a tool; abstract mentions MCP, but primary experiments call API function calling on four models, and validation on real MCP clients shows attack failed | `exclude`, `EC2` (A1b failed) |
| A1-2 | Attack installs malicious MCP tool in the open ecosystem and exploits trust in tool provider; run on several real MCP clients | `include` (A1a and A1b) |
| A1-3 | Tool call traffic detector with generic features (tool name, argument embeddings), trained on multi-format benchmark | `exclude`, `EC2` (mechanism without MCP structure) |
| A1-4 | Proxy design between MCP client and server that detects tool definition changes and cross-server calls; no empirical evaluation yet | `include` (A1a; A1b via MCP-specific mechanism); maturity L0; note "IC4 marginal" |
| A1-5 | Composition attack where agent with access to many MCP services chains legitimate operations; tested on agents using MCP servers | `include` (A1a: cross-service composition) |
| A1-7 | Paper claims composition vulnerability in MCP-based agents, but reported numbers are passing rates on benign benchmark and case study is narrative | `exclude`, `EC3` (A1c failed) |
| A1-6 | General agent defense framework evaluated on three safety benchmarks; MCP mentioned as one plugin | `exclude`, `EC2` |

---

## Full Eligibility Criteria Reference

### Inclusion Criteria (IC)

| ID | Criterion |
|:---:|:---|
| IC1 | Published or posted between 25 November 2024 and 25 September 2026. |
| IC2 | Addresses the security of MCP specifically: attacks, vulnerabilities, threat models, authentication or authorization, defenses, or ecosystem security measurements; or compares MCP with another agent tool-use paradigm on security grounds. |
| IC3 | Written in English. |
| IC4 | Belongs to one of the following types: peer-reviewed paper; preprint with empirical, measurement, or formal method; normative specification; government or standards-body guidance; vulnerability disclosure with CVE identifier or reproducible proof of concept. |

### Exclusion Criteria (EC)

| ID | Criterion |
|:---:|:---|
| EC1 | Uses MCP only as infrastructure for a non-security goal, such as task-capability benchmarking. |
| EC2 | Discusses LLM or agent security without MCP-specific analysis. Foundational pre-release works enter Set B instead. |
| EC3 | Marketing material, opinion pieces without technical evidence, or statistics without a traceable method. |
| EC4 | Full text not accessible. |
| EC5 | Uses "MCP" for an unrelated concept. |

### A1 Special Criterion (for attack/defense papers)

**A1. MCP-specific attack or defense papers** pass IC2 only if:
- **A1a:** Threat mechanism is formulated as a weakness/requirement of MCP ecosystem or architecture
- **A1b:** Primary results are obtained on real MCP servers, tools, or clients
- **A1c:** Metrics measure the claimed proposition (not just benign benchmark performance)

---

## Substitution Test (from v3 Screening Protocol)

The boundary between MCP-specific and generic agent-security work is operationalized as a substitution test: **if a record's security claim survives unchanged when "MCP" is replaced by a generic tool-calling framework, the record fails IC2** even where MCP is mentioned.

Apply this test after checking A1 criteria. Records that pass the substitution test are excluded under EC2.

---

## Evidence Tiers (E1–E5)

| Tier | Evidence Type | Examples |
|:---:|:---|:---|
| E1 | Peer-reviewed empirical, measurement, or formal study | Papers at archival conferences and journals |
| E2 | Preprint with empirical, measurement, or formal method | arXiv papers not yet published at an archival venue |
| E3 | Normative specification or government/standards-body guidance | MCP specification revisions; NSA guidance |
| E4 | Practitioner disclosure with CVE or reproducible PoC | Vendor security advisories; CVE records |
| E5 | Community guidance and consensus frameworks | OWASP projects |

---

## Version History

| Version | Date | Changes |
|:---|:---|:---|
| v3.2 | 2026-XX | Current version; A1 special criterion added post-audit |
| v3.1 | 2026-XX | Set B boundary clarified |
| v3.0 | 2026-XX | Initial v3 protocol |

---

## Document Information

| Field | Value |
|:---|:---|
| Document ID | Addendum A1 |
| Version | v3.2 |
| Status | Active |
| Applies to | All screenings and audits |
| Reported in | Section 2.6 |
