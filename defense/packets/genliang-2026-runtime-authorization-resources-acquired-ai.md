# Evidence Locator Packet: genliang-2026-runtime-authorization-resources-acquired-ai

- **Title**: Runtime Authorization for Resources Acquired by AI Agents
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2609.14744
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\genliang-2026-runtime-authorization-resources-acquired-ai\fulltext.txt
- **Character Count**: 184834

## Block 2: Contribution Sentences
**Location**: `Abstract-Conference.html` [offsets: 182613:183547]
> Abstract-Conference.html
> [40] Jerome H. Saltzer and Michael D. Schroeder. 1975. The Protection of Information in Computer Systems. Proc. IEEE 63,
> 
> 9 (1975), 1278–1308. doi:10.1109/PROC.1975.9939
> [41] Reshabh K. Sharma, Linxi Jiang, Shuo Chen, and Zhiqiang Lin. 2026. Beyond OAuth: Task-Scoped Authorization for
> 
> AI Agents via Natural Language Slices. arXiv:2603.17170 [cs.CR] doi:10.48550/arXiv.2603.17170
> [42] Uchi Uchibeke. 2026. Before the Tool Call: Deterministic Pre-Action Authorization for Autonomous AI Agents.
> 
> arXiv:2603.20953 [cs.CR] doi:10.48550/arXiv.2603.20953
> [43] Universal Commerce Protocol Contributors. 2026.
> Universal Commerce Protocol.
> Protocol specifi-
> cation and schema repository.
> https : / / github . com / Universal - Commerce - Protocol / ucp / tree /
> 8e600b0588c72d3bf23498bd403ef915cb6b1559 Accessed 2026-09-11.
> [44] Mengting Wu, Lin Wang, Yong Zhang, and Jiang Deng. 2026. From Intent to Execution Grant:
**Location**: `Introduction` [offsets: 5887:6777]
> We present a reference architecture for provenance-bounded activation. Its acquisition envelope is a
> downward-closed relational predicate over a normalized typed hypergraph. Each active hyperedge
> may combine multiple inputs and produces one ordinal-indexed output; a multi-output acquisition
> is represented by distinct, independently admitted singleton-output edges. Nodes represent root
> grants, source-resource references, quarantined resources, and active semantic capabilities. The
> predicate can express correlated limits that componentwise checks lose: one beneficiary may hold
> a read capability or a publish capability but not both; one canonical control root may create at most
> one active descendant; or a credential may be valid only for a particular data domain, provider
> profile, purpose, and delegation depth. All grants sharing an issuer, canonical control root, and
> policy epoch

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation Results` [section offsets: 108603:128363]
**First 120 words verbatim** [offsets: 108603:109633]
> Evaluation Results
> 
> 8.1
> Semantic separation and independent reconstruction
> The reference execution and checker agreed on every fixture. The 40 unsafe traces divide evenly
> across eight transformation families and five resource classes. Twenty-five reject during activa-
> tion, five during delivery, and ten during effect commit. Six stable codes account for every rejec-
> tion: 15 RELATIONAL_ENVELOPE_VIOLATION outcomes and five each for OUTPUT_ASSOCIATION_
> CONFLICT, OUTPUT_OUTSIDE_RELATIONAL_CLAUSE, INVALID_AUTHORITY_TRANSITION, EFFECT_
> COMMIT_RACE, and EFFECT_PERMIT_BINDING_MISMATCH.
> 
> The checker rejected 89/89 additional trace-tampering tests. Field-complete subsets mutate the
> 23 acquisition-permit, 25 activation-permit, 16 effect-permit, and ten effect-receipt top-level fields
> independently while retaining the corresponding identifier and rehashing the trace. The remaining
> 15 cover hash-bound and semantic payloads, required ledger rows, the outbox provider key, logical-
> time discipline, source-only predecessor typing,

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation Results` [offsets: 120802:121007]
> 8.4
> Cost and repeatability
> The policy-kernel benchmark executes 20 warm-up and 200 measured rounds over the fixed 60-
> fixture order, yielding 12,000 complete traces on an Apple M4 Max with Node.js 24.18.0.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation Results` [offsets: 109918:110041]
> All 20 benign traces prepared one exact single-use effect permit, consumed its slot, and produced
> one inert effect receipt.
**Location**: `Evaluation Results` [offsets: 113187:113387]
> 8.3
> Runtime, crash, and resource evidence
> 
> 8.2
> Protocol and public-source closure
> The dedicated AP2 profile freezes four primary and five referenced v0.2 JSON schemas at one
> immutable upstream commit.
**Location**: `Evaluation Results` [offsets: 115395:115579]
> The 48
> negative replays cover unregistered boundaries, servers, transports, and tools; missing or unknown
> fields; runtime/profile mismatch; invalid arguments; and correlation mismatch.
**Location**: `Evaluation Results` [offsets: 115601:115743]
> Runtime Authorization for Acquired Resources
> 37
> 
> The frozen upstream experiment executed nine cases three times through each client component.
**Location**: `Evaluation Results` [offsets: 119649:119824]
> Both benign
> paths exited with status zero, 12 cases reached real Docker quarantine, and four authorized first
> starts reached effect-permit commit and broker-mediated dispatch.
**Location**: `Evaluation Results` [offsets: 119904:120274]
> For each runtime, an unregistered tool, missing
> sidecar context, and altered capture binding rejected before resource creation; missing permit,
> effect drift, stale epoch, and post-certificate configuration drift rejected before start dispatch; and
> 
> --- PAGE BREAK ---
> 
> 38
> Zhu and Wang
> 
> certificate replay rejected without a second request after one authorized first use.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `evasion` | **Location**: `Header / Abstract` [offsets: 1211:1633]
> Under explicit assumptions, we prove eight safety properties covering quarantine, backing, non-
> amplification, split non-evasion, crash/retry, refunds, epochs, and effect confinement. Across five resource
> classes, reference semantics accepted 20/20 benign traces and rejected 40/40 registered unsafe traces over 810
> events; an independent checker agreed on 60 base and 40 refinement traces and rejected 89/89 tamper tests.
**Matched Term**: `evasion` | **Location**: `Introduction` [offsets: 9408:10092]
> This paper makes five contributions:
> 
> acquisition non-amplification, split non-evasion, crash-safe at-most-once activation, refund
> non-resurrection, epoch non-inheritance, and end-to-end resource-to-effect confinement.
> (5) It evaluates the separation with 60 five-class base fixtures over 810 events, 40 implementation-
> 
> refinement traces, a checker that rejects all 89 registered tamper tests, two separate agent-
> runtime mappings, AP2 and external-source profiles, 15 activation and five effect crash cuts,
> the complete 32-schedule registered five-bit replay domain, 32 effect replays, 192 receipt sub-
> stitutions, local kernel timing, and a 20-case network-disabled container gate.
**Matched Term**: `evasion` | **Location**: `Background and Problem Separation` [offsets: 61276:61575]
> Theorem 4 (Split non-evasion). Under A1, A4–A6, A8, and A11, fix a reachable refresh-closed
> state 𝑠, and let two acquisition plans differ only in order partition, retry or grant identifier, surface
> alias, independent-event order, or allocation among descendants whose roots share authority domain 𝜌.
**Matched Term**: `evasion` | **Location**: `Background and Problem Separation` [offsets: 74415:74746]
> For multi-output acquisitions, each ordinal has its own activation slot and is admitted against the
> current aggregate. Safe prefixes may activate while the first violating output remains quarantined;
> this is the operational meaning of split non-evasion.
> 
> Algorithm 4 validates the complete current path, not only the opaque handle.
**Matched Term**: `evasion` | **Location**: `Related Work` [offsets: 138820:139102]
> If the provider can create a raw
> credential directly in an agent-controlled channel, quarantine is not complete. If aliases cannot be
> resolved, split non-evasion is not available. If terminal state cannot be queried after a timeout, the
> output remains indeterminate and quarantined.
**Matched Term**: `evasion` | **Location**: `Conclusion` [offsets: 141585:142542]
> It represents actual provider outputs in a typed acquisition hypergraph, evaluates a relational
> downward-closed envelope over canonical identities and aggregates, keeps returned resources in
> quarantine, commits each finite-range output ordinal into at most one slot-unique active record,
> revalidates the exact row and currentness before publishing its opaque handle, preserves capability
> occupancy across refunds, and rechecks current lineage before issuing a single-use effect permit
> that is atomically consumed at effect commit. The resulting theorems cover backed authority,
> non-amplification, split non-evasion, crash safety, freshness, and end-to-end effect confinement
> within a registered decidable profile.
> 
> The executable evidence realizes that profile across five resource classes: 20 benign traces com-
> plete and 40 strict unsafe traces reject over 810 events, with the latter divided among 25 activation,
> five delivery, and ten effect rejections.
**Matched Term**: `evasion` | **Location**: `Conclusion` [offsets: 167530:167846]
> The
> commit guard therefore rejects 𝑒𝑗, contradicting successful full activation. A safe prefix may remain
> active, which is consistent with non-evasion. If an accepted time, epoch, grant-currentness, fence,
> or destruction transition intervenes, it advances the domain revision and atomically refreshes
> the projection.
