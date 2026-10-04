# Supplementary Material

**Security of Model Context Protocol in Agentic AI Systems: A Systematization of Knowledge on Threats, Trust Boundaries, and Defense Mechanisms**

This file accompanies the manuscript submitted to *AI and Security Convergence*. Data files, codebooks, packets, and scripts referenced below are available in the replication repository https://github.com/azureice10/MCP_SoK.

---

## Table S1. Search strategy and record identification

### S1.1 Academic sources and per-phase counts

| Phase | Source | Raw records |
|---|---|---|
| Baseline | arXiv (cs.CR, cs.AI, cs.SE, cs.CL) | 200 |
| Baseline | OpenAlex | 200 |
| Baseline | Semantic Scholar | 95 |
| Baseline | **Subtotal (after title and DOI deduplication)** | **495 → 460** |
| Supplementary | IEEE Xplore | 112 |
| Supplementary | Scopus (Elsevier REST API) | 172 |
| Supplementary | ACM Digital Library (via Crossref API) | 13 |
| Supplementary | **Subtotal (after cross-source deduplication)** | **297 → 213** |
| Merge | Overlap of supplementary with baseline pool | 59 (56 confirmed overlaps, a 26.3% cross-index intersection, plus 3 duplicate-cluster reconciliations) |
| Merge | Net new supplementary records | 154 |
| Merge | **Screening pool** | **460 + 154 = 614** |

All queries were run on 25 September 2026. Every query required either the full phrase "Model Context Protocol" or the acronym "MCP" together with an agent or LLM term, to avoid collisions with unrelated uses of the acronym in engineering and medicine.

| Source | Exact query string | Filters / Target Fields |
|---|---|---|
| IEEE Xplore | `("All Metadata":"Model Context Protocol") AND ("All Metadata":security OR "All Metadata":attack OR "All Metadata":vulnerability OR "All Metadata":threat OR "All Metadata":"prompt injection" OR "All Metadata":poisoning OR "All Metadata":authorization)` | All Metadata; Years: 2024–2026 |
| ACM DL (Crossref API) | `[[Title: "model context protocol"] OR [Abstract: "model context protocol"]] AND [[Abstract: security] OR [Abstract: attack*] OR [Abstract: vulnerab*] OR [Abstract: threat*] OR [Abstract: "prompt injection"] OR [Abstract: poisoning] OR [Abstract: authoriz*]]` | Title and Abstract; Publication Date: Post-Nov 1, 2024 |
| Scopus (Elsevier REST API) | `TITLE-ABS-KEY("Model Context Protocol" AND (security OR attack OR vulnerability OR threat OR "prompt injection" OR poisoning OR authorization))` | Title, Abstract, Keywords; Nov 2024 – Sep 2026 |
| arXiv | `all:"Model Context Protocol" OR all:"MCP"` combined with security filters (`security`, `vulnerability`, `attack`, `injection`, `poisoning`) | All fields; Categories: cs.CR, cs.AI, cs.SE, cs.CL; Nov 2024 – Sep 2026 |
| OpenAlex | `default.search:"Model Context Protocol" AND (security OR attack OR vulnerability)` | Title, Abstract, Inverted Index Concepts; Nov 2024 – Sep 2026 |
| Semantic Scholar | `query: "Model Context Protocol security"` | Title, Abstract via REST API; Nov 2024 – Sep 2026 |

Snowballing: backward and forward [25], seed set Hou et al. [2], Song et al. [9], Z. Wang et al. [6], Zhao et al. [7], and X. Li and Gao [3]; iterated until no new eligible record appeared.

### S1.2 Gray literature and vulnerability retrieval

Gray-literature source types: (a) the five security-relevant MCP specification revisions (2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28); (b) the OWASP GenAI Security Project (conceptual framing only, no MCP-specific findings); (c) the NSA Cybersecurity Information Sheet on MCP; (d) vulnerability databases and package registries; (e) vendor disclosures and curated incident indices (Invariant Labs GitHub MCP disclosure; Asana cross-tenant advisory; Zealynx MCP Breach Index).

Vocabulary mismatch: a naive query for the standalone acronym "MCP" across NVD API 2.0 and GitHub Security Advisories (GHSA) returned 98 candidates but only 3 true positives, because advisories identify affected components by package identifiers (for example `mcp-server-git`, `@modelcontextprotocol/server-filesystem`, `fastmcp`) rather than the expansion "Model Context Protocol".

Expanded multi-vector protocol:

- Boolean phrase query: `"model context protocol" OR "mcp-server" OR "fastmcp" OR "mcp-remote" OR "mcp inspector"`
- Package-name prefixes across npm, PyPI, and Maven: `mcp-server-*`, `@modelcontextprotocol/*`
- Common Platform Enumeration (CPE) vendor entries
- GHSA GraphQL queries across the npm, PyPI, and Maven ecosystems

Result: 128 raw candidates → 31 after deduplication → 9 excluded (generic dependencies or LLM UI flaws without a protocol binding) → **22 Tier E4 records** (20 CVEs and 2 vendor disclosures). These records form the external validation set of Section 4.3 and are not part of the 614-record academic screening pool or the 171-record synthesis corpus.

Data: `data/screening/prisma_screening_pool_614.csv`, `data/corpus/mcp_sok_corpus_171.csv`, `data/corpus/background_set_b_11.csv`, `data/corpus/corpus_metadata_182.csv`, `data/validation/e4_validation_set_22.csv`.

---

## Table S2. Data extraction form

The extraction schema was verified against the frozen coding workbook (`Lembar_Koding_Pertahanan_v1.3_FROZEN.xlsx`) with standardized permissible value domains:

| Field group | Fields | Allowed Values / Schema |
|---|---|---|
| Bibliographic | `record_id`, `authors`, `year`, `title`, `venue`, `doi_or_url` | Canonical string format `<author>-<year>-<slug>`; Year: 2024–2026 (or historical for Set B); DOI/arXiv string |
| Evidence | `evidence_tier`, `AACODS_appraisal` | Categorical: E1 (Peer-reviewed empirical), E2 (Preprint empirical), E3 (Spec/Standard), E4 (Practitioner disclosure/CVE), E5 (Community framework) |
| Protocol state | `mcp_protocol_version`, `sdk_version`, `host_client_tested` | Spec revision: `2024-11-05`, `2025-03-26`, `2025-06-18`, `2025-11-25`, `2026-07-28`; SDK strings; Tested host/client environment |
| Threat | `threat_layer`, `taxonomy_class_primary`, `taxonomy_class_secondary`, `boundary_crossing`, `attack_vector` | Layer: `A`, `B`, `C`, `D`, `Multi`; Primary & Secondary classes: `A1`–`A3`, `B1`–`B3`, `C1`–`C7`, `D1`–`D3`; Crossings: `U -> L`, `L -> S_i`, `S_i -> L`, `S_i -> X_i`, `S_i -> S_j`, `L -> UI` |
| Defense | `defense_role`, `defense_name`, `paradigma`, `titik_penegakan`, `defense_maturity`, `evaluasi_adaptif`, `jenis_evaluasi` | Role: `primary`, `secondary`, `proposal_only`, `none`; Maturity: `L0` (Conceptual), `L1` (Offline/PoC), `L2` (Testbed), `L3` (Production); Adaptivity: `Yes`, `No`, `N/A`; Evaluation: `author_run`, `independent`, `none` |
| Synthesis | `stated_limitations`, `contradictions`, `supporting_passage` | Verbatim text excerpts (≤25 words) from full-text packets (`defense/packets/`) |

---

## Section S3. Screening calibration, substitution test, and audits

### S3.1 Calibration sample

- Random 20% sample of the 460-record baseline pool (n = 92, random seed 42), screened by two reviewers blind to each other and to automated recommendations, using only title, abstract, and publication year (venue, DOI, and source withheld).
- Three records whose screening had been informed by worked examples in the reviewer protocol were replaced with three freshly drawn records (random seed 343) before computing agreement.
- Raw agreement 85.9% (79/92); Cohen's κ = 0.734 (substantial [29]). κ = 0.798 when two functionally equivalent but differently labeled Set B decisions count as agreement.

### S3.2 Protocol refinements after calibration

1. **Substitution test.** If a record's security claim survives unchanged when "MCP" is replaced by a generic tool-calling framework, the record fails IC2 even where MCP is mentioned. Five records describing generic mechanisms (information-flow control, multi-layer red-teaming, runtime tool-call interception, an agent-skills survey, and metadata-attack detection) were excluded under EC2. Conversely, the test retained studies grounded in MCP's own artifacts (server codebases, registries, logs) even when security is a minority theme, and applied systems that analyze an MCP-specific threat.
2. **Set B scope.** Set B requires conceptual relevance to agent or tool-use security, not merely a pre-window publication date; four pre-2024 records on unrelated topics had been misclassified as background.

### S3.3 Audit of sole inclusions

- The first reviewer screened the remaining 80% of the baseline pool alone.
- A second reviewer, blind to the first reviewer's decisions, re-screened 137 of the 138 sole inclusions (one had no abstract) from title, abstract, and year.
- After open reconciliation, 37 of 137 (27.0%; Wilson 95% CI 20.3%–35.0%) were excluded, mostly generic agent-security or application papers in which MCP was only a deployment interface (EC1, EC2). One further record was excluded because its full text showed "MCP" did not mean the Model Context Protocol (EC5).
- Post-audit rule (recorded after the fact and applied only to audited records): an attack or defense paper passes only if (a) its threat or mechanism is framed as a weakness or requirement of the MCP ecosystem or architecture; (b) the results supporting its central claim were obtained on real MCP servers, tools, or clients (or, for a design without experiments, its mechanism depends on MCP-specific elements); and (c) its measurements evaluate the claim it advances.

### S3.4 Audit of sole exclusions

- The first reviewer made 182 sole exclusions. None of the 118 off-topic exclusions (IC2) mentions MCP in title or abstract; a keyword scan for tool and agent terms flagged one, and 12 were drawn at random for manual checking.
- The second reviewer, blind to the first reviewer's codes, re-screened these 20 plus the 64 other exclusions (84 in total) and reinstated none.
- Agreement on the exclusion code: 61 of 84 (72.6%), mostly where a record never mentions MCP and could carry IC2 or EC2. Seven records without an abstract were judged from the title.
- Eleven records unresolved from the abstract were checked in full text: two taxonomies of real-world MCP server faults [30, 31] were retained because each grounds its categories in mined MCP codebases, and one proxy architecture was reclassified to include because its controls were built around MCP's client-server model.

### S3.5 Disposition by pool

| Pool | Screened | MCP-specific | Set B | Excluded |
|---|---|---|---|---|
| Baseline | 460 | 148 | 9 | 303 |
| Supplementary | 154 | 23 | 2 | 129 (EC5: 81; EC1: 47; EC2: 1) |
| **Total** | **614** | **171** | **11** | **432** (IC2: 164; EC1: 125; EC2: 56; EC5: 82; EC3: 5; EC4: 0) |

---

## Table S4. E4 validation set: full mapping and adjudication

| Record | Component and crossing | CVSS rating (authority) | Class | Mechanism and coding notes |
|---|---|---|---|---|
| CVE-2025-47274 | ToolHive deployment utility (zone H) | v4.0 2.4 Low (CNA: GitHub); v3.1 7.8 (NVD) | Residue | Plaintext API tokens and credentials stored in local run-configuration files; no Table 6 crossing traversed. |
| CVE-2025-53109 | Filesystem server (Sᵢ → Xᵢ) | v4.0 7.3 High (GitHub) | C5 | Symlink traversal bypasses directory confinement, enabling arbitrary file read and write. |
| CVE-2025-53110 | Filesystem server (Sᵢ → Xᵢ) | v4.0 7.3 High (GitHub) | C5 | Naive prefix matching allows `/sandbox_private` when `/sandbox` is approved. |
| CVE-2025-68143 | Git server (Sᵢ → Xᵢ) | v4.0 6.5 Medium (GitHub) | C5 | `git_init` accepts arbitrary paths, initializing repositories anywhere on the host. |
| CVE-2025-68144 | Git server (Sᵢ → Xᵢ) | v4.0 6.3 Medium (GitHub) | C5 | Argument injection in `git_diff` and `git_checkout`. |
| CVE-2025-68145 | Git server (Sᵢ → Xᵢ) | v4.0 6.4 Medium (GitHub) | C5 | Traversal bypassing the `--repository` restriction. |
| CVE-2026-27735 | Git server (Sᵢ → Xᵢ) | v4.0 6.4 Medium (GitHub) | C5 | Path traversal in `git_add` stages files outside the repository. |
| CVE-2025-53967 | Framelink Figma server (Sᵢ → Xᵢ) | v3.1 7.5 High (GitHub/NVD) | C5 | Shell metacharacters in `fetchWithRetry` (invoking `curl`) yield remote command execution. |
| CVE-2026-0755 | gemini-mcp-tool (Sᵢ → Xᵢ) | v3.1 9.8 Critical (GitHub) | C5 | OS command injection in `execAsync` and CLI parsing; local file read via `@file` parameters. |
| CVE-2026-39884 | mcp-server-kubernetes (Sᵢ → Xᵢ) | v3.1 8.3 High (GitHub) | C5 | Flag injection into `kubectl` through `port_forward`, leading to remote code execution. |
| CVE-2025-65513 | fetch-mcp-server (Sᵢ → Xᵢ) | v4.0 6.3 Medium (GitHub) | C5 | SSRF via private-IP validation bypass. |
| CVE-2026-32871 | FastMCP OpenAPI provider (Sᵢ → Xᵢ) | v4.0 10.0 Critical (GitHub) | C5 | SSRF and path traversal in `RequestDirector._build_url()`. |
| CVE-2026-35568 | MCP Java SDK (C ↔ Θ, Sᵢ ↔ Θ) | v4.0 7.6 High (GitHub) | C3 | Missing Host and Origin validation on HTTP/SSE endpoints enables DNS rebinding. |
| CVE-2025-66414 | MCP TypeScript SDK (C ↔ Θ, Sᵢ ↔ Θ) | v4.0 7.6 High (GitHub) | C3 | DNS rebinding through missing Host header validation on localhost-bound servers. |
| CVE-2025-66416 | MCP Python SDK (C ↔ Θ, Sᵢ ↔ Θ) | v4.0 7.6 High (GitHub) | C3 | DNS rebinding through missing Host and Origin verification. |
| CVE-2025-49596 | MCP Inspector (C ↔ Θ, Sᵢ ↔ Θ) | v4.0 9.4 Critical (GitHub) | C3 | Unauthenticated local proxy without CORS or token validation; web pages can issue tool calls. |
| CVE-2025-6514 | mcp-remote client proxy (Sᵢ / Θ → C) | v3.1 9.6 Critical (JFrog) | C6 (added) | Untrusted `authorization_endpoint` URLs with shell metacharacters passed to `open`/`exec` during OAuth discovery. |
| CVE-2025-54135 | Cursor IDE, "CurXecute" (Sᵢ / Θ → C) | v3.1 8.5 High (GitHub); 9.8 (NVD) | C6 (added); A2 secondary | Auto-execution of unsanitized launch commands in `.cursor/mcp.json`; the write can be triggered by prompt injection from repository content. |
| CVE-2025-54136 | Cursor IDE, "MCPoison" (descriptor over time) | v3.1 7.2 High (GitHub); 8.8 (NVD) | B1 (extended) | Modified `.cursor/mcp.json` executed without re-verifying consent or integrity. |
| CVE-2026-0621 | MCP TypeScript SDK (C ↔ Sᵢ) | v4.0 8.7 High (GitHub) | Residue | ReDoS in `UriTemplate` expansion; availability defect, no trust boundary traversed. |
| Asana MCP disclosure | Multi-tenant server (Sᵢ → Xᵢ) | High (vendor advisory; corroborated by Zealynx) | C7 (added); C5 secondary | Tenant segregation flaw returned task metadata across corporate tenants. |
| Invariant Labs disclosure | GitHub server (Sᵢ → L → Sᵢ) | High (vendor disclosure) | A2; C1, D1 secondary | Injected issue (A2) leads the planner to read a private repository (C1) and publish it in a public pull request (D1). |

### S4.1 Adjudication notes

- **CVE-2025-6514 and CVE-2025-54135 (C6).** Initial coding debated whether `mcp-remote` was a transport-authorization flaw (C3). `mcp-remote` acts as a client-side stdio-to-HTTP proxy; on connecting to an untrusted server it performs OAuth discovery (RFC 8414), and a malicious endpoint supplies an `authorization_endpoint` URL containing shell metacharacters that is passed to OS utilities to launch the browser. This is a client-side sink failure, not an authorization failure, so C6 and the Sᵢ / Θ → C crossing were defined. CurXecute fits C6 as auto-execution of unsanitized workspace configuration, with A2 secondary.
- **CVE-2025-54136 (B1).** Cursor cached and executed tool configurations from `.cursor/mcp.json` without re-verifying consent on repository updates. B1 was extended from runtime `notifications/tools/list_changed` to post-approval mutation of descriptors and launch configurations.
- **Asana (C7, C5 secondary).** Initial coding stretched C2, but C2 lies on L → Sᵢ where the planner acts as deputy. The Asana failure lies in backend tenant scoping on Sᵢ → Xᵢ; C7 was defined to avoid conflation. Both sources were appraised under AACODS.
- **CVE-2026-0621 (residue).** Availability lies inside the review scope, but the taxonomy has no availability class; recorded as residue and treated, with the seven resource-abuse defenses, as evidence for gap 5.

### S4.2 Clustering and ecosystem concentration

- Shared product or root cause: four CVEs concern the Git reference server, two the Filesystem server, two Cursor, and three the same DNS-rebinding defect in three SDKs; 15 clusters in total. Cluster-level absorption: 11/15 (73.3%; 48.0%–89.1%) before revision and 13/15 (86.7%; 62.1%–96.3%) after.
- Language ecosystems of the 20 CVEs: TypeScript/Node.js (10), Python (9), Java (1). Go, Rust, and C# implementations had no public NVD or GHSA disclosures at the cut-off date.

---

## Section S5. Defense coding reliability and supporting detail

- Second-coder sample (n = 38): the four strongest-claim records (two graded L2, two flagged adaptive), 16 random defense records, 18 random non-defense records. Coding was frozen and checksummed before comparison.
- Defense vs. non-defense: 37/38 (97.4%; κ = 0.95). Eight-way role: 31/38 (81.6%; κ = 0.78); five of the seven role disagreements fell between a designed defense and a mere proposal.
- On the 20 defense records both coded: evaluation type 80%; maturity 75%; primary mechanism 60% (80% when nine mechanisms are grouped into four families); evaluated-class sets matched exactly for 6/20 (mean Jaccard 0.58); the coders disagreed on both adaptive-flag records.
- Role breakdown: 67 designed or implemented defenses, 6 secondary, and 12 conceptual proposals under relaxed thresholding (reconciled to exactly 15 records graded L0 in Section 6.2 and the frozen master coding sheet under the strict requirement of an active LLM planner or live tool execution; the 12 vs. 15 sensitivity analysis is detailed in Section S5).
- Definitions tightened after reconciliation: class C1 and the policy mechanism family.
- Adaptive flag: requires an attack built against the defense's own mechanism; fixed suites of paraphrased or obfuscated inputs, and benchmarks designed against other defenses, do not qualify.
- Overhead reporting among 70 evaluated defenses: numeric 52 (74.3%), qualitative 7, none 11. Public repository: 14 of 85 (16.5%).
- ADR [82] reports more than ten months of operation on over 7,200 hosts, processing over 10,000 agent sessions per day; graded L1 because the deployment is internal to the authors' employer and unconfirmed by a third party.
- Additional author-evaluated proposals: MCPFixGen [89] combines multi-checkpoint rollback with attention masking; TFA [90] applies information-flow analysis over a product lattice; SecuAudit [91] binds access policies to metadata using Shamir's secret sharing and supervised hashing with challenge-response auditing; Sentinel-Net [92] combines rule pre-filtering with a temporal dilated CNN-LSTM.
- Evidence passages (at most 25 words) supporting each disputed code: `packets/` directory.

---

## Section S6. Analysis of the ChainWatch–SAMOS contradiction

ChainWatch [94] states that a review of MCP literature up to April 2026 found no published defense against multi-step attack chains, yet its primary illustrative scenario (S2) is the Invariant Labs GitHub incident that SAMOS [93], published at the ACM SOSP 2025 workshops in October 2025, evaluated and blocked.

Two grounds resolve the contradiction. First, ChainWatch's survey of existing defenses (its Section II.C) covers only per-invocation content filters (MCPShield, MCPGuard, MindGuard) and omits systems-level information-flow control (IFC) gateways, which lets it overstate the novelty of a design that reports no experiment (graded L0). Second, the two works pursue different mechanisms. ChainWatch targets unannotated sequential anomaly detection, using a hidden Markov model with Viterbi decoding over 20-dimensional feature vectors to identify kill-chain progression across otherwise benign calls. SAMOS enforces deterministic, policy-driven IFC over session taint state at an inline gateway, using developer-supplied annotations (`read_confidentiality`, `write_confidentiality`, and capability flags per SEP-1075/1076). ChainWatch may therefore be the first design attempting unannotated sequential detection, but SAMOS had demonstrated empirical multi-step mitigation by structural IFC about six months earlier.

Stated limitations of the two works: ChainWatch requires labelled traces from real MCP sessions and expects false positives on legitimate multi-service workflows; SAMOS was evaluated on one scenario by its authors without an adaptive adversary.

---

## Note on citations

Bracketed numbers refer to the reference list of the main manuscript; this supplement cites no additional sources.
