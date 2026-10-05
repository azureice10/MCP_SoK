# Operational Guidelines for Defense Coding Sheet (v1.1)

Applies to `Defense_Coding_Workbook_v1.3_FROZEN.xlsx` (sheet `Coding`). These guidelines are normative and binding: in case of any discrepancy with recollections or earlier drafts, this document governs. All coded values must be grounded directly in paper full texts, not in titles, abstracts, or automated agent suggestions.

---

## 0. Strict Inviolable Principles

1. **No Guessing.** If text evidence is insufficient, mark `unclear` or leave blank, and document the rationale in the `notes` column.
2. **Code from Method and Evaluation Sections**, not the abstract. The abstract is only sufficient to identify defense role, name, paradigm, and high-level mechanism summary.
3. **No Full Text = No Evaluation Codes.** Set `fulltext_available = no` and leave all columns from `evaluation_type` through `utility_overhead` completely blank.
4. **No Default Values.** Never copy patterns across rows (e.g., blanket `{A1, C1}`). Every taxonomy class must have explicit textual justification from that specific paper.
5. **Formula-Driven Columns (Maturity, Consistency Checks) Must Not Be Edited.** Maturity is computed deterministically by formula.
6. **Hide the Reference `agent_role` Column** before beginning (right-click column, Hide). Determine the role independently from the evidence packet first, and only unhide the reference column afterward for comparison, logging any discrepancy in `notes`.

---

## 1. Pre-Coding Verification (±20 minutes)

1. Open 5 random evidence locator packets in `defense/packets/`. For each packet, copy one quoted excerpt and search for it within `fulltext.txt` of the corresponding paper. The quote must match verbatim, and the section/page locator must be accurate. If any quote fails the verbatim test, halt and re-verify the locator extractor.
2. Verify that each packet includes an Adaptivity hits scan block (which may report `no hits`).
3. Retain a clean, unedited backup of the coding workbook.

---

## 2. Workflow & Triage Priority

| Sequence | Triage Pool (Column `triage`) | Procedure | Target Time / Row |
|---|---|---|---|
| 1 | `kandidat_agent` (80 records) | Full coding per Sections 3–8 | 5–8 min (proposal_only: 2–3 min) |
| 2 | `kandidat_cek_recall` (17 records) | Determine role first. If not a defense, stop. If defense, code fully | 3–8 min |
| 3 | `scan_cepat` (89 records) | Code `role` only from title/abstract. If mitigation is implemented, inspect packet and escalate to candidate | ±1 min |

Save progress every 20 rows. Complete each batch in unified sessions to maintain coding definition consistency.

---

## 3. The `role` Column (Mandatory for ALL Records)

Evaluate sequentially and select the first matching category:

1. Does the paper design, implement, or specify a **mechanism** intended to prevent, detect, or mitigate attacks on MCP-based agent systems? (Scanners, detectors, gateways, proxies, and formal policies qualify as mechanisms).
   - **Yes, and it constitutes the primary contribution** $\rightarrow$ `defense_primary`
   - **Yes, but the primary contribution is an attack, measurement, or survey, and the mitigation is implemented and empirically evaluated** $\rightarrow$ `defense_secondary`
   - **Yes, but it is only proposed, recommended, or sketched without implementation/evaluation** $\rightarrow$ `proposal_only`
2. **No.** Select one:
   - Attack or exploit without evaluated mitigation $\rightarrow$ `attack`
   - Survey, systematic literature review, taxonomy, or threat model $\rightarrow$ `survey_review`
   - Benchmark, dataset, or empirical measurement study $\rightarrow$ `benchmark_measurement`
   - Position paper, conceptual essay, index, or risk score framework without enforcement mechanism $\rightarrow$ `position_other`
   - Other non-defense literature (explain in `notes`) $\rightarrow$ `not_defense`

Clarifications:
- Surveys or SLRs on defense mechanisms are **not** `proposal_only`; use `survey_review`, even if they include "recommended guidelines".
- Attack papers with a single paragraph of unvalidated recommendations ("we suggest...") = `attack`. If experiments demonstrate that the mitigation reduces attack success rates = `defense_secondary`.
- Benchmarks designed to evaluate defenses = `benchmark_measurement`.
- Corpus examples (roles only): Hou et al. (landscape) = `survey_review`; Zhou et al. (remote server authentication) = `benchmark_measurement`; MCPTox = `benchmark_measurement`; MCP-SecLint = `defense_primary`.

For non-defense roles (`attack`, `survey_review`, `benchmark_measurement`, `position_other`, `not_defense`), **leave all subsequent columns blank**; formulas will assign `n/a`.

---

## 4. Defense Identity Columns (Defense Roles Only)

| Column | Coding Rule |
|---|---|
| `fulltext_available` | `yes` if full text is available and locator packet is accessible; otherwise `no` |
| `defense_name` | Canonical name assigned by authors; if unnamed, use `unnamed:<3 keywords>` |
| `mechanism_summary` | At most 2 sentences in own words: what is inspected, where, and what determines allow/deny |

**Papers with Multiple Defense Components:** Create separate rows (copy row, update `defense_name`, keep `record_id` identical) only if components have distinct enforcement points **or** are evaluated separately. Components that always operate in tandem and are evaluated as a single unified system constitute a single row. Comparative baselines inside a paper do not receive separate rows unless the baseline is an existing corpus record.

---

## 5. `paradigm`, `llm_in_decision`, and `enforcement_point`

### 5.1 `llm_in_decision` (Code prior to `paradigm`)

- `yes`: At runtime, the decision to allow, deny, or alert depends on the output of an LLM or ML model (e.g., LLM-as-a-judge, ML classifier, LLM normalizer whose output determines policy verdict).
- `no`: Decisions are governed purely by deterministic rules, cryptography, or OS-level access control mechanisms.
- LLM used **only during setup/offline** (e.g., synthesizing policies that are subsequently enforced without runtime LLM calls) = `no`; note this in `mechanism_summary`.
- Unclear whether LLM is invoked per request = `unclear`.

### 5.2 `paradigm`: Select **ONE** governing the final decision

| Permissible Value | Operational Criterion |
|---|---|
| `content_inspection_static` | Offline or pre-deployment analysis of code, configurations, or manifests |
| `content_inspection_runtime` | Runtime inspection of payloads (descriptions, arguments, results, message traces) via rules, heuristics, ML, or LLMs |
| `human_approval` | Final authorization decision rests on explicit human-in-the-loop consent |
| `isolation_containment` | Restricting blast radius via sandboxes, containers, WASM VMs, or filesystem path confinement |
| `deterministic_policy` | Explicit formal rules (e.g., OPA, Cedar, ABAC) evaluate requests **AND** `llm_in_decision = no` |
| `capability_or_token` | Authority is carried by cryptographic tokens or attenuable capability handles |
| `integrity_provenance` | Signatures, cryptographic hashes, certificate pinning, or remote attestation of manifests/servers |
| `protocol_provision` | Normative protocol specification requirements or protocol extensions |
| `other` | None of the above (provide justification in `notes`) |

Hard Rule: `deterministic_policy` is **forbidden** if `llm_in_decision = yes` (workbook formula will flag `CHECK`). For hybrid architectures, assign the paradigm of the primary decisive component, and describe secondary components in the summary.

### 5.3 `enforcement_point`

Select the primary insertion point:
- `H`: Host runtime
- `C`: Client application
- `S`: Server implementation
- `gateway_proxy`: Inline proxy intermediary between client and server
- `registry`: Tool/server discovery registry during publishing or admission
- `Theta`: Authorization infrastructure (OAuth AS, IdP, STS)
- `X`: External system / API boundary
- `offline_analysis`: Out-of-band / post-hoc auditing pipeline
- `other`: Specify in `notes`

---

## 6. Architectural Crossings & Taxonomy Classes

**`classes_claimed`**: Classes explicitly stated as mitigated in the abstract, introduction, or threat model. Delimit multiple classes with `;`. Do not infer claims from generic security terms. Grounding:

| Class | Attack Mechanism Targeted | Trust Boundary Crossing |
|---|---|---|
| A1 | Malicious instructions embedded in tool descriptions or JSON schemas | R2 ($S_i \rightarrow L$) |
| A2 | Indirect prompt injection via tool invocation results or dynamic resources | R2 ($S_i \rightarrow L$) |
| A3 | Tool selection confusion / misdirection from conflicting descriptions | R2 ($S_i \rightarrow L$) |
| B1 | Post-approval descriptor tampering (rug-pull mutations) | R7 (Dynamic registry updates) |
| B2 | Registry metadata drift and tool shadowing over time | R7 ($S_i \leftrightarrow \text{Registry}$) |
| B3 | Planner hallucination/confusion under mutating schemas | R7 ($S_i \leftrightarrow L$) |
| C1 | Confused deputy exploitation across authenticated tools | R3 ($L \rightarrow S_i$) |
| C2 | Caller identity confusion (cross-user authorization leakage) | R3 ($L \rightarrow S_i$) |
| C3 | Transport authorization failure (DNS rebinding, missing CORS/Host checks) | R4 ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) |
| C4 | Intent inversion through crafted invocation traces | R3 ($L \rightarrow S_i$) |
| C5 | Sink policy violation (path traversal, command injection in tool handler) | R5 ($S_i \rightarrow X_i$) |
| C6 | Client bridge exploitation (unsafe URI handlers, local command execution) | R5/R4 ($S_i / \Theta \rightarrow C$) |
| C7 | Authorization scoping failure (cross-tenant metadata/data leakage) | R5 ($S_i \rightarrow X_i$) |
| D1 | Multi-server cross-tool invocation chains and exfiltration | R6 ($S_i \rightarrow S_j$) |
| D2 | Multi-turn guardrail evasion and stateful goal drift | R6 ($L \rightarrow S_i$) |
| D3 | Supply chain malware propagation via cloned or poisoned packages | Pre-session admission |

Classes outside the taxonomy (e.g., pure DoS or algorithmic complexity): record `OUT_OF_TAXONOMY:<description>` **without** including class code strings inside the description.

**`crossings`**: Architectural boundary crossings (R1–R7) whose security properties are actively enforced.

**`classes_evaluated`**: Classes evaluated through **empirical experiments or formal case studies with reported results**. Must be a strict subset of `classes_claimed`. Unverified claims are excluded.

---

## 7. Evaluation Methodology (Full Text Only)

### 7.1 `evaluation_type`

| Permissible Value | Operational Definition |
|---|---|
| `none` | No empirical experiments, quantitative metrics, or formal case studies |
| `author_run` | Evaluated solely by original authors |
| `author_run+independent` | Evaluated by authors and corroborated by an independent corpus paper |
| `independent_only` | Evaluated solely by third-party papers in the corpus |
| `deployment_measurement` | Observational measurement study in real production deployments (maturity left blank; reported in Section 5) |

Independent evaluation requires: (a) independent paper belongs to the 171 synthesis corpus; (b) it executes empirical benchmarks against the defense; (c) passing citations do not qualify. Candidate sources: `independent_eval_candidates.csv`. Record evaluator `record_id` in `independent_evaluator`.

### 7.2 `attack_set_origin`

- `authors_own`: Custom synthetic datasets or prompt suites crafted by authors.
- `third_party_public`: Standard public benchmarks (e.g., InjecAgent, BIPIA, ToolBench; cite name in `notes`).
- `mixed`: Combination of author-created and public benchmark suites.
- `none`: Applicable when `evaluation_type = none`.

### 7.3 `adaptive_evaluation` (Strict Verification)

Answer three mandatory questions using the evidence packet:
1. Does the evaluation feature an adversary **specifically constructed or optimized to evade the proposed defense mechanism** with knowledge of its detection heuristics (white-box, defense-aware, iterative reformulation)?
2. Does the text evaluate attacks specifically targeting **this defense**, rather than static baselines?
3. Can a supporting passage (at most 25 words) be quoted verbatim?

- All three answered Yes $\rightarrow$ `yes`, and record excerpt in `adaptive_quote`.
- Static benchmark suites, unadapted prompt variations, or "unseen" attacks $\rightarrow$ `no`.
- Ambiguous after reviewing full text $\rightarrow$ `unclear` and document checked sections in `notes`.
- `evaluation_type = none` $\rightarrow$ mandatory `n/a_without_evaluation`.

### 7.4 `evidence_location` & `utility_overhead`

- `evidence_location`: Mandatory for all evaluated entries (e.g., `Sec 5.2; Table 3; p. 8`).
- `utility_overhead`: Quantitative metrics reported (e.g., `latency +5 ms (Table 4)`); if checked and unmentioned, record `not_reported`.

---

## 8. Deployment Status & Level 3 Criteria

- `none`: Default setting.
- `prototype_open_source`: Publicly available repository or code artifacts.
- `production_public_evidence`: Verified documentation or release notes showing integration in production software.
- `spec_normative`: Mandatory (MUST/SHOULD) clauses in official specification revisions.

---

## 9. Formula-Driven Columns & Consistency Validations

`maturity` is computed deterministically:
- **L3**: `deployment = spec_normative` OR `production_public_evidence`
- **L2**: `evaluation_type` includes independent evaluation (`author_run+independent`, `independent_only`)
- **L1**: `evaluation_type = author_run`
- **L0**: `evaluation_type = none`
- `n/a`: Non-defense roles

`consistency_check`: Must be completely blank for a valid row. Consistency alerts:

| Validation Error Flag | Remediation |
|---|---|
| `deterministic_policy with LLM/ML in decision` | Change paradigm or update `llm_in_decision` |
| `adaptive=yes requires verbatim quote` | Insert verified excerpt, or change to `no` |
| `without evaluation, adaptive must be n/a` | Set to `n/a_without_evaluation` |
| `missing evaluated_classes or evidence_location` | Fill in details from evaluation section |
| `without full text, evaluation columns must be blank` | Clear evaluation columns or verify full-text status |

---

## 10. Calibrated Worked Examples

| # | Scenario Description | Canonical Coding Verdict |
|---|---|---|
| 1 | Host-level subprocess sandbox for server tool execution; evaluated on 20 custom path traversal payloads; no adaptive attack formulation | `defense_primary`; `isolation_containment`; `llm=no`; `H`; R5; claimed: C5; evaluated: C5; `author_run`; `authors_own`; `adaptive=no`; `prototype_open_source`; Maturity: **L1** |
| 2 | LLM-as-a-judge inspecting tool definitions; author-evaluated on public benchmark; independently evaluated by another corpus paper | `content_inspection_runtime`; `llm=yes`; `author_run+independent`; `third_party_public`; Maturity: **L2** |
| 3 | OPA policy engine with administrator rules; evaluated across 30 tasks | `deterministic_policy`; `llm=no`; `author_run`; Maturity: **L1** |
| 4 | Gateway where LLM assigns risk scores, followed by threshold policy | `content_inspection_runtime`; `llm=yes` (not deterministic); Maturity: **L1** |
| 5 | Attack paper containing a short paragraph of mitigation suggestions without experiments | `attack`; all other columns blank (`n/a`) |
| 6 | Attack paper introducing a detector evaluated to reduce ASR from 90% to 10% | `defense_secondary`; fully coded per defense protocol |
| 7 | Authors design an adaptive search algorithm specifically to bypass their detector | `adaptive=yes`; record quote in `adaptive_quote` |
| 8 | Systematic review of defense taxonomies | `survey_review`; all other columns blank (`n/a`) |

---

## 11. Completion Checklist Prior to Freezing

- [ ] Sheet `Summary`: "Rows with Validation Errors" = 0.
- [ ] Total categorized records matches corpus size (186 total, 171 synthesis corpus).
- [ ] All evaluated entries possess valid `evidence_location` and `classes_evaluated`.
- [ ] All `adaptive = yes` rows contain verbatim quotes verified against full texts.
- [ ] Incomplete full-text records flagged for institutional access requests.
- [ ] File checksum computed and recorded prior to statistical synthesis.
