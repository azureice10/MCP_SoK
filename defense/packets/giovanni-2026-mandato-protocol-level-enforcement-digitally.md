# Evidence Locator Packet: giovanni-2026-mandato-protocol-level-enforcement-digitally

- **Title**: Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2608.14074
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\giovanni-2026-mandato-protocol-level-enforcement-digitally\fulltext.txt
- **Character Count**: 26888

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 5438:5478]
> This paper makes four contributions:
> 
> 1.
**Location**: `Abstract` [offsets: 6635:6839]
> This paper 
> contributes the model, the architecture, and the regulatory analysis; empirical results are defined 
> as a falsifiable plan rather than reported, in the spirit of early-stage systems papers[6].

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
**Section Heading**: `Implementation Status and Evaluation Plan` [section offsets: 19446:19497]
**First 120 words verbatim** [offsets: 19446:20454]
> Implementation Status and Evaluation Plan
> 
> Status
> 
> Evaluation plan
> 
> Enforcement overhead
> 
> Selective hash commitments of argument values in log records
> 
> The reference implementation derives from a specification (v0.6) comprising over 170 numbered 
> functional and non-functional requirements (RF-*/RNF-*), an architectural decomposition 
> (ARCH-*), a relational schema of 22+ tables covering mandates, grants, delegation edges, 
> revocations, quota counters, log records, and checkpoints, and 22 use cases (UC-01–UC-22) 
> spanning issuance, attenuation, enforcement, escalation, ratification, revocation-lag behavior, 
> and audit extraction. Delivery is organized on a milestone path M0–M8.5; an end-to-end 
> demonstration configuration (proxy, decision service, oversight console, verifier CLI) 
> corresponds to milestones M5–M6. Six open design points (APERTO-01–06) are tracked publicly 
> in the specification, including the interaction between quota semantics and delegation, and 
> checkpoint-interval policy under
**Section Heading**: `Evaluation plan` [section offsets: 19497:21904]
**First 120 words verbatim** [offsets: 19497:20514]
> Evaluation plan
> 
> Enforcement overhead
> 
> Selective hash commitments of argument values in log records
> 
> The reference implementation derives from a specification (v0.6) comprising over 170 numbered 
> functional and non-functional requirements (RF-*/RNF-*), an architectural decomposition 
> (ARCH-*), a relational schema of 22+ tables covering mandates, grants, delegation edges, 
> revocations, quota counters, log records, and checkpoints, and 22 use cases (UC-01–UC-22) 
> spanning issuance, attenuation, enforcement, escalation, ratification, revocation-lag behavior, 
> and audit extraction. Delivery is organized on a milestone path M0–M8.5; an end-to-end 
> demonstration configuration (proxy, decision service, oversight console, verifier CLI) 
> corresponds to milestones M5–M6. Six open design points (APERTO-01–06) are tracked publicly 
> in the specification, including the interaction between quota semantics and delegation, and 
> checkpoint-interval policy under adversarial suppression. The implementation targets current

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation plan` [offsets: 19514:20081]
> Enforcement overhead
> 
> Selective hash commitments of argument values in log records
> 
> The reference implementation derives from a specification (v0.6) comprising over 170 numbered 
> functional and non-functional requirements (RF-*/RNF-*), an architectural decomposition 
> (ARCH-*), a relational schema of 22+ tables covering mandates, grants, delegation edges, 
> revocations, quota counters, log records, and checkpoints, and 22 use cases (UC-01–UC-22) 
> spanning issuance, attenuation, enforcement, escalation, ratification, revocation-lag behavior, 
> and audit extraction.
**Location**: `Evaluation plan` [offsets: 20716:20890]
> Added latency per tool call, 𝛥𝑡= 𝑡proxied −𝑡direct, reported as p50/p95/p99 under (a) synthetic 
> load across grant set sizes |𝛴| ∈{10, 102, 103} and (b) replayed real traces.
**Location**: `Evaluation plan` [offsets: 20891:20978]
> Acceptance target: 
> p95 overhead ≤ 5% of median tool execution time for auto decisions.
**Location**: `Evaluation plan` [offsets: 21399:21499]
> Median human confirmation latency and abandonment rate on the oversight console in pilot use 
> — Art.

## Block 8: Limitations
**Section Heading**: `Limitations and Future Work` [section offsets: 21904:21933]
**First 120 words verbatim** [offsets: 21904:22713]
> Limitations and Future Work
> 
> Conclusion
> 
> Beyond the empirical gap that Section 6 plans to close, four limitations are structural and worth 
> stating. First, MANDATO bounds authority, not competence: a permitted call can still be a bad idea, 
> and no constraint language substitutes for the judgment obligations that remain with the 
> principal. Second, the legal reading of mandates as acts of delegation is an alignment claim, not 
> settled doctrine; its validation is a matter for legal scholarship and, eventually, case law — we 
> consider the interdisciplinary evaluation of this claim future work in itself. Third, the anchoring 
> scheme is tamper-evident, not tamper-proof, within a checkpoint interval; co-signing and shorter 
> intervals trade cost against exposure, and we plan to characterize that trade-off

## Block 9: Adaptivity Hits
no hits
