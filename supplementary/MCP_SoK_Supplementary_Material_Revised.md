# Supplementary Material

**Security of Model Context Protocol in Agentic AI Systems: A Systematization of Knowledge on Threats, Trust Boundaries, and Defense Mechanisms**

**Authors:** Raden Budiarto Hadiprakoso\*, I Komang Setia Buana, and Herman Kabetta  
**Affiliation:** Cryptographic Engineering, Politeknik Siber dan Sandi Negara, Indonesia  

This file accompanies the revised manuscript submitted to *AI and Security Convergence* alongside the standalone **Supplementary Research Dataset** (`MCP_SoK_Supplementary_Research_Dataset.md`). Data files, codebooks, evidence locator packets, SHA-256 freeze manifests, and verification scripts referenced below are openly available in the replication repository: [https://github.com/azureice10/MCP_SoK](https://github.com/azureice10/MCP_SoK).

## Table S1. Search strategy and record identification

### S1.1 Academic sources and per-phase counts

| Phase | Source | Raw records |
| :--- | :--- | :---: |
| Baseline | arXiv (`cs.CR`, `cs.AI`, `cs.SE`, `cs.CL`) | 200 |
| Baseline | OpenAlex | 200 |
| Baseline | Semantic Scholar | 95 |
| Baseline | **Subtotal (after initial title/DOI deduplication; 7 duplicate rows merged during full-text reconciliation)** | **495 $\to$ 460 rows (453 unique)** |
| Supplementary | IEEE Xplore | 112 |
| Supplementary | Scopus (Elsevier REST API) | 172 |
| Supplementary | ACM Digital Library (via Crossref API) | 13 |
| Supplementary | **Subtotal (after cross-source deduplication)** | **297 $\to$ 213** |
| Merge | Overlap of supplementary with baseline pool | 59 (56 confirmed overlaps, a 26.3% cross-index intersection, plus 3 duplicate-cluster reconciliations) |
| Merge | Net supplementary rows | 156 (154 initial additions + 2 restored Tier E1 defense studies \[19, 59\]) |
| Merge | **Combined screening ledger** | **460 + 156 = 616 audit rows (609 unique deduplicated studies after 7 baseline `DUP` merges)** |

All queries were run on 25 September 2026. Every query required either the full phrase `"Model Context Protocol"` or the acronym `"MCP"` together with an agent or LLM term, to avoid collisions with unrelated uses of the acronym in engineering and medicine.

| Source | Exact query string | Filters / Target Fields |
| :--- | :--- | :--- |
| IEEE Xplore | `("All Metadata":"Model Context Protocol") AND ("All Metadata":security OR "All Metadata":attack OR "All Metadata":vulnerability OR "All Metadata":threat OR "All Metadata":"prompt injection" OR "All Metadata":poisoning OR "All Metadata":authorization)` | All Metadata; Years: 2024–2026 |
| ACM DL (Crossref API) | `[[Title: "model context protocol"] OR [Abstract: "model context protocol"]] AND [[Abstract: security] OR [Abstract: attack*] OR [Abstract: vulnerab*] OR [Abstract: threat*] OR [Abstract: "prompt injection"] OR [Abstract: poisoning] OR [Abstract: authoriz*]]` | Title and Abstract; Publication Date: Post-Nov 1, 2024 |
| Scopus (Elsevier REST API) | `TITLE-ABS-KEY("Model Context Protocol" AND (security OR attack OR vulnerability OR threat OR "prompt injection" OR poisoning OR authorization))` | Title, Abstract, Keywords; Nov 2024 – Sep 2026 |
| arXiv | `all:"Model Context Protocol" OR all:"MCP"` combined with security filters (`security`, `vulnerability`, `attack`, `injection`, `poisoning`) | All fields; Categories: `cs.CR`, `cs.AI`, `cs.SE`, `cs.CL`; Nov 2024 – Sep 2026 |
| OpenAlex | `default.search:"Model Context Protocol" AND (security OR attack OR vulnerability)` | Title, Abstract, Inverted Index Concepts; Nov 2024 – Sep 2026 |
| Semantic Scholar | `query: "Model Context Protocol security"` | Title, Abstract via REST API; Nov 2024 – Sep 2026 |

Snowballing: backward and forward \[25\], seed set Hou et al. \[2\], X. Li and Gao \[3\], Z. Wang et al. \[5\], Zhao et al. \[6\], and Song et al. \[8\]; iterated until no new eligible record appeared.

### S1.2 Gray literature and vulnerability retrieval

Gray-literature source types: (a) the five security-relevant MCP specification revisions (2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28 \[12\]; `Supplementary Dataset S-Spec: S-Spec-01`–`S-Spec-05`); (b) the OWASP GenAI Security Project (conceptual framing only, no MCP-specific findings); (c) the NSA Cybersecurity Information Sheet on MCP \[24\]; (d) vulnerability databases and package registries; (e) vendor disclosures and curated incident indices (Invariant Labs GitHub MCP disclosure `S-E4-22`; Asana cross-tenant advisory `S-E4-21`; Zealynx MCP Breach Index `S-E4-24`).

Vocabulary mismatch: a naive query for the standalone acronym `"MCP"` across NVD API 2.0 and GitHub Security Advisories (GHSA) returned 98 candidates but only 3 true positives, because advisories identify affected components by package identifiers (for example `mcp-server-git`, `@modelcontextprotocol/server-filesystem`, `fastmcp`) rather than the expansion `"Model Context Protocol"`.

Expanded multi-vector protocol:
- Boolean phrase query: `"model context protocol" OR "mcp-server" OR "fastmcp" OR "mcp-remote" OR "mcp inspector"`
- Package-name prefixes across npm, PyPI, and Maven: `mcp-server-*`, `@modelcontextprotocol/*`
- Common Platform Enumeration (CPE) vendor entries
- GHSA GraphQL queries across the npm, PyPI, and Maven ecosystems

Result: 128 raw candidates $\to$ 31 after deduplication $\to$ 9 excluded (generic dependencies or LLM UI flaws without a protocol binding) $\to$ **22 Tier E4 records** (20 CVEs and 2 vendor disclosures; `Supplementary Dataset S-E4: S-E4-01`–`S-E4-22`). These records form the external validation set of Section 4.3 and are evaluated independently of the 179-record synthesis corpus.

Data files: `prisma_screening_pool_reconciled_frozen.csv`, `screening_pool_reconciled.json`, `exclusion_code_reconciliation_worksheet.csv`, `mcp_sok_corpus_179_reconciled_frozen.csv`, `mcp_sok_corpus_170_conservative_frozen.csv`, `defenses_88_reconciled_frozen.csv`, `defenses_84_reconciled_frozen.csv`, and `MCP_SoK_Supplementary_Research_Dataset.md`.

## Table S2. Data extraction form

The extraction schema was verified against the frozen coding dataset (`defenses_88_reconciled_frozen.csv` and `screening_pool_reconciled.json`) with standardized permissible value domains:

| Field group | Fields | Allowed Values / Schema |
| :--- | :--- | :--- |
| Bibliographic & Version Linkage | `record_id`, `authors`, `year`, `title`, `venue`, `doi_or_url`, `version_relation_type`, `canonical_corpus_id`, `canonical_published_doi_or_url` | Canonical string format `<author>-<year>-<slug>`; Year: 2024–2026 (or historical for Set B); Version linkage: `none`, `preprint_to_published_duplicate`, `author_slug_duplicate_of_corpus_record`, `cross_pool_duplicate_of_set_b` |
| Evidence | `evidence_tier`, `AACODS_appraisal` | Categorical: E1 (Peer-reviewed empirical), E2 (Preprint empirical), E3 (Spec/Standard), E4 (Practitioner disclosure/CVE), E5 (Community framework) |
| Protocol state | `mcp_protocol_version`, `sdk_version`, `host_client_tested` | Spec revision: `2024-11-05`, `2025-03-26`, `2025-06-18`, `2025-11-25`, `2026-07-28`, `Unspecified`; SDK strings; Tested host/client environment |
| Threat & boundary | `threat_layer`, `taxonomy_class_primary`, `taxonomy_class_secondary`, `boundary_crossing`, `attack_vector` | Layer (Table 10): `A` (Semantic channel), `B` (Descriptor integrity over time), `C` (Identity, authorization, & sinks), `D` (Composition across servers), `Multi`, `None`; Classes: `A1`–`A3`, `B1`–`B3`, `C1`–`C7`, `D1`–`D3`; Crossings (Table 6): `U -> H`, `S_i -> L`, `L -> S_i`, `C <-> Theta, S_i <-> Theta`, `S_i -> X_i`, `Composition (S_1...S_k)`, `Descriptor (t_1 vs t_0)`, `S_i / Theta -> C` |
| Defense | `defense_role`, `defense_name`, `defense_paradigm`, `enforcement_point`, `maturity_level`, `adaptive_evaluation`, `evaluation_type` | Role: `defense_primary`, `defense_secondary`, `proposal_only`, `none` (or non-defense category); Maturity: `L0` (Conceptual), `L1` (Author-evaluated prototype), `L2` (Independently evaluated), `L3` (Deployed control); Adaptivity: `Yes`, `No`, `N/A`; Evaluation: `author_run`, `independent`, `none` |
| Synthesis | `stated_limitations`, `contradictions`, `supporting_passage` | Verbatim text excerpts (not length-capped) from full-text packets |

## Section S3. Screening calibration, substitution test, and full-text reconciliation audits

### S3.1 Calibration sample

- Random 20% sample of the 460-record baseline pool ($n = 92$, random seed 42), screened by two reviewers blind to each other and to automated recommendations, using only title, abstract, and publication year (venue, DOI, and source withheld).
- Three records whose screening had been informed by worked examples in the reviewer protocol were replaced with three freshly drawn records (random seed 343) before computing agreement.
- Raw agreement 85.9% (79/92); Cohen's $\kappa = 0.740$ on the literal four-category worksheet labels (`include`, `exclude`, `set_b`, `borderline`; $\kappa = 0.800$, 83/92, under binary include/exclude grouping with Set B and borderline counted as include; substantial \[26\]). $\kappa = 0.803$ (82/92, 89.1%; binary grouping unchanged at $\kappa = 0.800$) when the three functionally equivalent Set B decisions are aligned. Values recomputed from `data/screening/screening_calibration_sample_92.csv`.

### S3.2 Protocol refinements after calibration

1. **Substitution test.** If a record's security claim survives unchanged when `"MCP"` is replaced by a generic tool-calling framework, the record fails IC2 even where MCP is mentioned. Five records describing generic mechanisms (information-flow control, multi-layer red-teaming, runtime tool-call interception, an agent-skills survey, and metadata-attack detection) were excluded under EC2. Conversely, the test retained studies grounded in MCP's own artifacts (server codebases, registries, logs) even when security is a minority theme, and applied systems that analyze an MCP-specific threat.
2. **Comparative protocol studies (P3 rule).** Studies comparing MCP with emerging peer protocols (such as A2A, ACP, Agora, or ANP) are retained under IC2 if and only if they provide substantive architectural, threat-model, or security-mechanism analysis of MCP's own primitives or trust boundaries (reinstating 9 full-text-verified protocol and comparative P3 records in the 179-record primary reconciled corpus, while reporting the 170-record strict conservative sensitivity set in parallel).
3. **Set B scope.** Set B requires conceptual relevance to agent or tool-use security, not merely a pre-window publication date; four pre-2024 records on unrelated topics had been misclassified as background.

### S3.3 Audit of sole inclusions

- The first reviewer screened the remaining 80% of the baseline pool alone.
- A second reviewer, blind to the first reviewer's decisions, re-screened 137 of the 138 sole inclusions (one had no abstract) from title, abstract, and year.
- After open reconciliation, 37 of 137 (27.0%; Wilson 95% CI 20.3%–35.0%) were excluded, mostly generic agent-security or application papers in which MCP was only a deployment interface (EC1, EC2). One further record was excluded because its full text showed `"MCP"` did not mean the Model Context Protocol (EC5).
- Post-audit rule (recorded after the fact and applied to audited records and all supplementary candidates): an attack or defense paper passes only if (a) its threat or mechanism is framed as a weakness or requirement of the MCP ecosystem or architecture; (b) the results supporting its central claim were obtained on real MCP servers, tools, or clients (or, for a design without experiments, its mechanism depends on MCP-specific elements); and (c) its measurements evaluate the claim it advances.

### S3.4 Audit of exclusions and version-duplicate reconciliation (`exclusion_code_reconciliation_worksheet.csv`)

- All 106 records in the exclusion reconciliation worksheet (`8` Priority P1 records, `7` Priority P2 duplicate candidates, and `91` Priority P3 exclusions) underwent full-text and metadata verification.
- **Version-duplicate reconciliation (`7 DUP` records):** Five within-baseline records were verified as preprint or author-slug duplicates of canonical corpus studies and merged (`brandon-2025` $\to$ `john-2026` \[48\]; `narek-2026-breaking` $\to$ `n-2025` \[15\]; `tiwari-2025` $\to$ `aditi-2025`; `xiaofan-2025-toward` $\to$ `xiaofan-2025-first-look` \[3\]; `zi-2025` $\to$ `zheng-2026` \[38\]), and two baseline exclusion-worksheet rows (`zehang-2024` [`row-0442`] and `zhaorun-2024` [`row-0449`]) were verified as cross-pool exact-ID duplicates of Set B records already retained in the supplementary pool (`row-0613` and `row-0614`), while the two missing Supplementary Tier E1 defenses (`Jang & Lee` \[19\] and `Bhosle` \[59\]) were restored (`row-0615` and `row-0616`). Two non-duplicate companion works (`narek-2026-prompt` and `xiaofan-2025-mcp-guard`) were verified as distinct studies and retained in the synthesis corpus.
- Eleven borderline records unresolved from the abstract were checked in full text: two taxonomies of real-world MCP server faults (`Taraghi et al.` \[27\] and `Owotogbe et al.`, `S-Preprint-04`) were retained because each grounds its categories in mined MCP codebases, and nine MCP protocol/comparative security studies (`red-team-prompt-injection-2026`, `shanshan-2026`, `mohan-2026`, `christopher-2025`, `haoyu-2025`, `xinyi-2025`, `abhishek-2025`, `yingxuan-2025`, and `ken-2025`) were reinstated in the 179-record primary reconciled corpus (and tracked separately in the 170-record conservative sensitivity analysis).
- **Language (IC3) reconciliation (2 records):** `survey-model-context-2026` and `empirical-study-privilege-2026` were included at abstract screening on the strength of English titles and abstracts, but their main text is not in English (Chinese-language journal articles). Both were excluded under IC3 at full-text reconciliation (`final_decision = Exclude`, `exclusion_reason = IC3`, `review_status = frozen_ic3_exclusion_2026-11-14`); neither is a defense record, so the defense matrices are unchanged. Their identifiers `S-Corpus-072` and `S-Corpus-085` are retired and not reassigned.
- **Substitution-test (IC2) reconciliation (1 record):** `genreachai-agentic-generative-2026` (a software-composition vulnerability-reachability tool that uses MCP servers only as a data connector) was coded as a `defense_primary` L1 record with claimed and evaluated class D3. Full-text inspection showed that it addresses open-source supply-chain vulnerability triage (Log4Shell, React2Shell; 500 production microservices), not MCP security or MCP tool cloning, and that its claim survives unchanged when MCP is replaced by a generic connector. It was excluded under IC2 (`review_status = frozen_ic2_exclusion_2026-11-14`), which removes one defense record (`S-Def-78`) from the matrices (89 to 88; conservative 85 to 84). Its identifiers `S-Corpus-088` and `S-Def-78` are retired and not reassigned.

### S3.5 Disposition by pool (Full Reconciled Skema A and Conservative Sensitivity Skema B)

| Pool | Audit Rows (Unique Studies) | MCP-Specific Corpus (Skema A \[Skema B\]) | Set B Background | Unique Exclusions (Skema A \[Skema B\]) | Version / Cross-Pool Duplicates (`DUP`) |
| :--- | :---: | :---: | :---: | :--- | :---: |
| Baseline | 460 (453 unique) | **157** \[148\] | **9** | **287** \[296\] (IC2: 148; EC1: 77 \[78\]; EC2: 54 \[62\]; EC3: 5; EC5: 3) | **7** (`5` version `DUP` + `2` cross-pool Set B `DUP`) |
| Supplementary | 156 (156 unique) | **22** \[22\] | **2** | **132** \[132\] (EC5: 81; EC1: 47; EC2: 1; IC2: 1; IC3: 2) | **0** |
| **Total** | **616 rows (609 unique)** | **179** \[170\] | **11** | **419** \[428\] (IC2: 149; EC1: 124 \[125\]; EC5: 84; EC2: 55 \[63\]; EC3: 5; IC3: 2; EC4: 0) | **7** (`616 - 7 = 609` unique studies) |

## Table S4. E4 validation set: full mapping and adjudication (`Supplementary Dataset S-E4`)

| Dataset ID & Record | Component and crossing | CVSS rating (authority) | Class | Mechanism and coding notes |
| :--- | :--- | :--- | :---: | :--- |
| `S-E4-01`: CVE-2025-47274 \[41\] | ToolHive deployment utility (zone H) | v4.0 2.4 Low (CNA: GitHub); v3.1 7.8 (NVD) | Residue | Plaintext API tokens and credentials stored in local run-configuration files; no Table 6 crossing traversed. |
| `S-E4-02`: CVE-2025-53109 \[41\] | Filesystem server ($S_i \to X_i$) | v4.0 7.3 High (GitHub) | C5 | Symlink traversal bypasses directory confinement, enabling arbitrary file read and write. |
| `S-E4-03`: CVE-2025-53110 \[41\] | Filesystem server ($S_i \to X_i$) | v4.0 7.3 High (GitHub) | C5 | Naive prefix matching allows `/sandbox_private` when `/sandbox` is approved. |
| `S-E4-04`: CVE-2025-68143 \[41\] | Git server ($S_i \to X_i$) | v4.0 6.5 Medium (GitHub) | C5 | `git_init` accepts arbitrary paths, initializing repositories anywhere on the host. |
| `S-E4-05`: CVE-2025-68144 \[41\] | Git server ($S_i \to X_i$) | v4.0 6.3 Medium (GitHub) | C5 | Argument injection in `git_diff` and `git_checkout`. |
| `S-E4-06`: CVE-2025-68145 \[41\] | Git server ($S_i \to X_i$) | v4.0 6.4 Medium (GitHub) | C5 | Traversal bypassing the `--repository` restriction. |
| `S-E4-07`: CVE-2026-27735 \[41\] | Git server ($S_i \to X_i$) | v4.0 6.4 Medium (GitHub) | C5 | Path traversal in `git_add` stages files outside the repository. |
| `S-E4-08`: CVE-2025-53967 \[41\] | Framelink Figma server ($S_i \to X_i$) | v3.1 7.5 High (GitHub/NVD) | C5 | Shell metacharacters in `fetchWithRetry` (invoking `curl`) yield remote command execution. |
| `S-E4-09`: CVE-2026-0755 \[41\] | gemini-mcp-tool ($S_i \to X_i$) | v3.1 9.8 Critical (GitHub) | C5 | OS command injection in `execAsync` and CLI parsing; local file read via `@file` parameters. |
| `S-E4-10`: CVE-2026-39884 \[41\] | mcp-server-kubernetes ($S_i \to X_i$) | v3.1 8.3 High (GitHub) | C5 | Flag injection into `kubectl` through `port_forward`, leading to remote code execution. |
| `S-E4-11`: CVE-2025-65513 \[41\] | fetch-mcp-server ($S_i \to X_i$) | v4.0 6.3 Medium (GitHub) | C5 | SSRF via private-IP validation bypass. |
| `S-E4-12`: CVE-2026-32871 \[41\] | FastMCP OpenAPI provider ($S_i \to X_i$) | v4.0 10.0 Critical (GitHub) | C5 | SSRF and path traversal in `RequestDirector._build_url()`. |
| `S-E4-13`: CVE-2026-35568 \[41\] | MCP Java SDK ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | v4.0 7.6 High (GitHub) | C3 | Missing Host and Origin validation on HTTP/SSE endpoints enables DNS rebinding. |
| `S-E4-14`: CVE-2025-66414 \[41\] | MCP TypeScript SDK ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | v4.0 7.6 High (GitHub) | C3 | DNS rebinding through missing Host header validation on localhost-bound servers. |
| `S-E4-15`: CVE-2025-66416 \[41\] | MCP Python SDK ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | v4.0 7.6 High (GitHub) | C3 | DNS rebinding through missing Host and Origin verification. |
| `S-E4-16`: CVE-2025-49596 \[41\] | MCP Inspector ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | v4.0 9.4 Critical (GitHub) | C3 | Unauthenticated local proxy without CORS or token validation; web pages can issue tool calls. |
| `S-E4-17`: CVE-2025-6514 \[41\] | mcp-remote client proxy ($S_i / \Theta \to C$) | v3.1 9.6 Critical (JFrog) | C6 (added) | Untrusted `authorization_endpoint` URLs with shell metacharacters passed to `open`/`exec` during OAuth discovery. |
| `S-E4-18`: CVE-2025-54135 \[41\] | Cursor IDE, "CurXecute" ($S_i / \Theta \to C$) | v3.1 8.5 High (GitHub); 9.8 (NVD) | C6 (added); A2 secondary | Auto-execution of unsanitized launch commands in `.cursor/mcp.json`; the write can be triggered by prompt injection from repository content. |
| `S-E4-19`: CVE-2025-54136 \[41\] | Cursor IDE, "MCPoison" (descriptor over time) | v3.1 7.2 High (GitHub); 8.8 (NVD) | B1 (extended) | Modified `.cursor/mcp.json` executed without re-verifying consent or integrity. |
| `S-E4-20`: CVE-2026-0621 \[41\] | MCP TypeScript SDK ($C \leftrightarrow S_i$) | v4.0 8.7 High (GitHub) | Residue | ReDoS in `UriTemplate` expansion; availability defect, no trust boundary traversed. |
| `S-E4-21`: Asana MCP disclosure \[53\] | Multi-tenant server ($S_i \to X_i$) | High (vendor advisory; corroborated by `S-E4-24`) | C7 (added); C5 secondary | Tenant segregation flaw returned task metadata across corporate tenants. |
| `S-E4-22`: Invariant Labs disclosure \[58\] | GitHub server ($S_i \to L \to S_i$) | High (vendor disclosure) | A2; C1, D1 secondary | Injected issue (A2) leads the planner to read a private repository (C1) and publish it in a public pull request (D1). |

### S4.1 Adjudication notes

- **CVE-2025-6514 and CVE-2025-54135 (C6).** Initial coding debated whether `mcp-remote` (`S-E4-17`) was a transport-authorization flaw (C3). `mcp-remote` acts as a client-side stdio-to-HTTP proxy; on connecting to an untrusted server it performs OAuth discovery (RFC 8414 \[42\]), and a malicious endpoint supplies an `authorization_endpoint` URL containing shell metacharacters that is passed to OS utilities to launch the browser. This is a client-side sink failure, not an authorization failure, so C6 and the $S_i / \Theta \to C$ crossing were defined. CurXecute (`S-E4-18`) fits C6 as auto-execution of unsanitized workspace configuration, with A2 secondary.
- **CVE-2025-54136 (B1).** Cursor cached and executed tool configurations from `.cursor/mcp.json` without re-verifying consent on repository updates (`S-E4-19`). B1 was extended from runtime `notifications/tools/list_changed` to post-approval mutation of descriptors and launch configurations.
- **Asana (C7, C5 secondary).** Initial coding stretched C2, but C2 lies on $L \to S_i$ where the planner acts as deputy. The Asana failure (`S-E4-21`) lies in backend tenant scoping on $S_i \to X_i$; C7 was defined to avoid conflation. Both practitioner sources (`S-E4-21` and `S-E4-24`) were appraised under AACODS \[29\].
- **CVE-2026-0621 (residue).** Availability lies inside the review scope, but the taxonomy has no availability class; recorded as residue (`S-E4-20`) and treated, with the eight resource-abuse defenses (seven conservative), as evidence for gap 5.

### S4.2 Clustering and ecosystem concentration

- Shared product or root cause: four CVEs concern the Git reference server, two the Filesystem server, two Cursor, and three the same DNS-rebinding defect in three SDKs; 15 clusters in total. Cluster-level absorption: 11/15 (73.3%; 48.0%–89.1%) before revision and 13/15 (86.7%; 62.1%–96.3%) after.
- Language ecosystems of the 20 CVEs: TypeScript/Node.js (10), Python (9), Java (1). Go, Rust, and C# implementations had no public NVD or GHSA disclosures at the cut-off date.

## Section S5. Defense coding reliability, unit-of-analysis reconciliation, and supporting detail

- **Second-coder sample ($n = 38$):** the four strongest-claim records (two graded L2, two flagged adaptive), 16 random defense records, 18 random non-defense records. Coding was frozen and checksummed before comparison. All supplementary and reopened defense records were independently audited (`20` blind dual-coded + `17` audited supplementary/reopened + `51` single-coded baseline = `88` reconciled defenses; `84` under the conservative sensitivity threshold).
- **Defense vs. non-defense:** 37/38 (97.4%; $\kappa = 0.95$). Eight-way role: 31/38 (81.6%; $\kappa = 0.78$); five of the seven role disagreements fell between a designed defense and a mere proposal.
- **On the 20 defense records both coded:** evaluation type 80%; maturity 75%; primary mechanism 60% (80% when nine mechanisms are grouped into mechanism families); evaluated-class sets matched exactly for 6/20 (mean Jaccard 0.58).
- **Full-text verification resolutions (`Jalendar/ZPAA`, `Armstrong/Astral`, and `Bhosle/Attested Policy Brokerage`):**
  1. `Jalendar et al.` (`S-Def-16`, `jalendar-2025-zero-trust-proof-gated-agent`, Authorea DOI `10.22541/au.175761889.90929465/v1`): Full-text inspection (`MCP_097_jalendar_zpaa.pdf`, 5 pp.) resolved the conflict between earlier coding sheets by confirming that the paper presents a purely conceptual architecture with target latency budgets (`<10 ms`) and no implementation or adversarial experiments; confirmed at **L0** (`proposal_only`, `classes_evaluated` empty).
  2. `Armstrong et al.` (`S-Def-23`, `samuel-2026-secure-sandbox-environment-orchestrating-medical`, *AMIA Joint Summits 2026*, PMC13274365): Full-text inspection (`MCP_033_samuel_astral.pdf`) resolved the earlier sheet discrepancy by confirming that the Astral containerized MCP sandbox argues analytically (a theoretical tool-poisoning scenario under its attenuated delegation tokens) that it neutralizes tool poisoning and evaluates clinical-workflow utility and transport performance, but executes no adversarial attack; confirmed at **L0** (`proposal_only`, `classes_evaluated` empty) while upgrading its bibliographic evidence tier from `E2` to **E1**.
  3. `Bhosle` \[59\] (`S-Def-85`, `attested-policy-brokerage-2026`, *IEEE CIACON 2026*): Full-text inspection of the IEEE PDF (CIACON 2026, pp. 1–6) found a single-host proof of concept with primitive latency measurements (0.113 ms median cache-hit allow, 0.167 ms broker decision, 0.120 ms re-attestation, 0.491/0.798 ms quorum commit), a distributed production-profile latency evaluation (p95 1.54–6.89 ms at 50k–500k requests/s), and one replayed CVE-2025-68144-style argument-injection trace that the PEP validator rejected. There is no adversarial trial set and no breach-rate table (Table II is a qualitative threat-coverage mapping). Coded as `defense_primary` at **L1** (`author_run`; `classes_claimed: C1;C2;C3;C5`; `classes_evaluated: C5`).
- **Unit-of-analysis resolution for `Hierarchical Approaches` (`Jang & Lee` \[19\], `S-Def-84`):** Full-text inspection established that the paper presents two distinct analytical units: (1) an overarching framework of four defense strategies derived from a tripartite threat classification (*MCP-Specific Defense Strategy* with 11 countermeasures, *LLM Inherent Defense Strategy* with 3 countermeasures, *Cyber Security Inherent Strategy*, and *MCP Firewall* technology) that is largely conceptual (**L0**), and (2) a defensive experiment (Section VI, pp. 77160–77162) that applies a packet-filtering countermeasure and the MCP Firewall's detection decision to a DNS-poisoning attack on a tool-calling MCP deployment (**L1**, `author_run`, `content_inspection_runtime`). Following the codebook rule to grade the highest empirically verified component while separating claimed from evaluated classes, `hierarchical-approaches-for-2026` is coded as `defense_secondary`, maturity **L1**, `classes_claimed: A1;A2;C1;C3;C5;D1;OUT_OF_TAXONOMY:dns_poisoning`, and `classes_evaluated: A2;C5;OUT_OF_TAXONOMY:dns_poisoning`.
- **Role and maturity breakdown (`n = 88` Reconciled \[and `n = 84` Conservative\]):** `67` \[65\] `defense_primary`, `7` \[7\] `defense_secondary`, and `14` \[12\] `proposal_only` by role, reconciling to **17 L0 (19.3%)** \[15 L0 (17.9%)\], **69 L1 (78.4%)** \[67 L1 (79.8%)\], **2 L2 (2.3%)** \[2 L2 (2.4%)\], and **0 L3 (0.0%)** once 3 toy-script designs without an active LLM planner or live MCP tool execution are graded L0 under the strict codebook threshold.
- **Adaptive flag:** requires an attack built specifically against the defense's own mechanism (**2 of 71 evaluated defenses \[2.8%\]**; 2 of 69 \[2.9%\] conservative: MindGuard `S-Preprint-13` and Delegation Broker `S-Preprint-14`). ARGUS \[51\] was reclassified as non-adaptive during the 2026-11-14 full-text cross-check: it is an offensive red-team scanner whose adaptive payload generation targets the systems it tests, not an attack constructed against ARGUS itself.
- **Overhead reporting among 71 evaluated defenses (69 conservative):** quantitative **51 (71.8%)** \[50 (72.5%)\], qualitative **7 (9.9%)** \[7 (10.1%)\], not reported **13 (18.3%)** \[12 (17.4%)\]. Public open-source repository (`Open-Source Prototype`): **15 of 88 (17.0%)** \[13 of 84 (15.5%)\].
- **ADR \[50\]:** reports more than ten months of operation on over 7,200 hosts, processing over 10,000 agent sessions per day; graded L1 because the deployment is internal to the authors' employer and unconfirmed by a third party.

## Section S6. Analysis of the ChainWatch–SAMOS contradiction

ChainWatch (`Supplementary Dataset S-Preprint-16`) states that a review of MCP literature up to April 2026 found no published defense against multi-step attack chains, yet its primary illustrative scenario (S2) is the Invariant Labs GitHub incident (`S-E4-22`) that SAMOS \[58\], published at the ACM SOSP 2025 workshops in October 2025, evaluated and blocked.

Two grounds resolve the contradiction. First, ChainWatch's survey of existing defenses (its Section II.C) covers only per-invocation content filters (MCPShield, MCPGuard, MindGuard) and omits systems-level information-flow control (IFC) gateways, which lets it overstate the novelty of a design that reports no experiment (graded L0). Second, the two works pursue different mechanisms. ChainWatch targets unannotated sequential anomaly detection, using a hidden Markov model with Viterbi decoding over 20-dimensional feature vectors to identify kill-chain progression across otherwise benign calls. SAMOS \[58\] enforces deterministic, policy-driven IFC over session taint state at an inline gateway, using developer-supplied annotations (`read_confidentiality`, `write_confidentiality`, and capability flags per SEP-1075/1076). ChainWatch may therefore be the first design attempting unannotated sequential detection, but SAMOS had demonstrated empirical multi-step mitigation by structural IFC about six months earlier.

Stated limitations of the two works: ChainWatch requires labelled traces from real MCP sessions and expects false positives on legitimate multi-service workflows; SAMOS was evaluated on one scenario by its authors without an adaptive adversary.

## Table S7. Primary-layer assignment of the synthesis corpus (*N* = 179 Reconciled / *N* = 170 Conservative)

Record-by-record primary-layer assignment of the 179 MCP-specific synthesis corpus records (and 170 conservative sensitivity records) is provided in `Supplementary Dataset S-Corpus` (`MCP_SoK_Supplementary_Research_Dataset.md` and `mcp_sok_corpus_179_reconciled_frozen.csv`), supporting the layer shares reported in Sections 4.3 and 9.1 of the main manuscript:

| Primary layer | Reconciled Corpus (*N* = 179) | Share (*N* = 179) | Conservative Corpus (*N* = 170) | Share (*N* = 170) |
| :--- | :---: | :---: | :---: | :---: |
| **A. Semantic channel (`A1–A3`)** | **90** | **50.3%** | 88 | 51.8% |
| **B. Descriptor integrity over time (`B1–B3`)** | **3** | **1.7%** | 2 | 1.2% |
| **C. Identity, authorization, and sinks (`C1–C7`)** | **77** | **43.0%** | 72 | 42.4% |
| **D. Composition across servers (`D1–D3`)** | **9** | **5.0%** | 8 | 4.7% |
| **Total MCP-Specific Synthesis Corpus** | **179** | **100.0%** | **170** | **100.0%** |

## Note on citations

Bracketed numbers `\[1\]`–`\[60\]` refer to the peer-reviewed reference list of the long-form revised manuscript draft (`MCP_SoK_Manuscript_Revised_AISC.md`; not distributed in this repository while the paper is under journal review, available from the authors on request), while persistent identifiers (`S-Spec-01`–`S-Spec-07`, `S-E4-01`–`S-E4-24`, `S-Preprint-01`–`S-Preprint-18`, `S-Corpus-001`–`S-Corpus-182` [179 active records; `S-Corpus-072`, `S-Corpus-085`, and `S-Corpus-088` retired], and `S-Def-01`–`S-Def-89` [88 active records; `S-Def-78` retired]) refer to the standalone **Supplementary Research Dataset** (`MCP_SoK_Supplementary_Research_Dataset.md`).
