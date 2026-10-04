# Evidence Locator Packet: ying-2026-options-not-clicks-lattice-refinement

- **Title**: Options, Not Clicks: Lattice Refinement for Consent-Driven MCP Authorization
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2605.11360
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\ying-2026-options-not-clicks-lattice-refinement\fulltext.txt
- **Character Count**: 102979

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 1506:1650]
> In this work, we present ConLeash,
> a client-side consent middleware that enforces boundary-scoped
> authorization for tool invocations in the MCP.
**Location**: `Abstract` [offsets: 2102:2242]
> We evaluate ConLeash on ConsentBench, a
> benchmark of 984 traces from real-world MCP servers, and conduct
> a within-subject user study (N=16).

## Block 3: Method Locator
**Section Heading**: `Implementation` [section offsets: 46412:49936]
**First 120 words verbatim** [offsets: 46412:47318]
> Implementation
> 
> ConLeash is implemented in Python and Datalog in approximately
> 5,400 lines of code in total. The system adopts a neuro-symbolic ar-
> chitecture: an LLM (claude-sonnet-4-20250514) serves solely as
> a perception frontend that translates tool invocations and natural-
> language invariants into structured Datalog facts. All authorization
> reasoning, including lattice containment checking, taint propaga-
> tion, and the Allow/Ask/Deny decision, is performed deterministi-
> cally by the Soufflé Datalog solver [1].
> 
> Consent Abstraction.
> Both consent abstraction and invariant
> synthesis follow a common propose-then-verify pattern: the LLM
> generates candidates, and the system applies a deterministic verifi-
> cation oracle before accepting them.
> 
> For per-call abstraction, the LLM proposes candidate predicates
> by mapping the tool’s MCP specification and runtime arguments
> to the lattice labels of the

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 49936:67257]
**First 120 words verbatim** [offsets: 49936:50790]
> Evaluation
> 
> To evaluate the effectiveness of ConLeash, we seek answers to the
> following research questions:
> • RQ1 (Effectiveness and Performance): How accurately does
> ConLeash detect and enforce consent boundary violations, and
> what is the computation overhead?
> • RQ2 (Real-World Comparison): How does ConLeash compare
> against existing consent models on real-world agent sessions?
> • RQ3 (Usability): Can ConLeash enhance security without sac-
> rificing usability?
> 
> Benchmark.
> Our threat model (§2) targets implicit privilege
> escalation, where users grant persistent permissions early in a ses-
> sion and the agent later reuses them with arguments that cross
> a lattice boundary. As no existing benchmark evaluates consent
> enforcement under these conditions, we construct ConsentBench
> from the 13 servers that meet our inclusion criteria among the
> top-ranked

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 50400:50410]
> Benchmark.
**Location**: `Evaluation` [offsets: 50612:50868]
> As no existing benchmark evaluates consent
> enforcement under these conditions, we construct ConsentBench
> from the 13 servers that meet our inclusion criteria among the
> top-ranked MCP servers (e.g., Slack, Gmail), spanning 11 task cate-
> gories (Appendix A).

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 50198:50316]
> • RQ2 (Real-World Comparison): How does ConLeash compare
> against existing consent models on real-world agent sessions?
**Location**: `Evaluation` [offsets: 57330:57378]
> Comparison with Existing MCP Consent Mechanisms.
**Location**: `Evaluation` [offsets: 63815:63963]
> Under ConLeash, participants
> opted for boundary-scoped “Always Allow” 3.5× more frequently
> than tool-level “Always Allow” in the baseline (46.3% vs.
**Location**: `Evaluation` [offsets: 64046:64373]
> Counter-intuitively, this increased adoption bolstered se-
> curity rather than compromising it: every “Always Allow” grant
> under ConLeash was scoped to a specific boundary (either a ba-
> sic lattice bound or a refined resource constraint, §5.4), whereas
> the baseline’s “Always Allow” granted unrestricted tool-level per-
> mission.
**Location**: `Evaluation` [offsets: 64547:64719]
> In contrast,
> baseline participants who consistently chose “Allow Once” were
> not necessarily safer: only 3 of 16 reported reading consent prompts
> carefully in pre-screening.
**Location**: `Evaluation` [offsets: 65749:65892]
> ConLeash
> scored significantly higher than the baseline on all four dimensions
> (Wilcoxon signed-rank, one-sided): informed consent (median 5
> vs.

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 49948:50197]
> To evaluate the effectiveness of ConLeash, we seek answers to the
> following research questions:
> • RQ1 (Effectiveness and Performance): How accurately does
> ConLeash detect and enforce consent boundary violations, and
> what is the computation overhead?
**Location**: `Evaluation` [offsets: 51445:51627]
> In total, ConsentBench comprises 984 traces (203 benign,
> 640 bound escalation, 141 invariant violation) ranging from 2 to
> 19 invocations, including 144 multi-server traces (Table 3).
**Location**: `Evaluation` [offsets: 52598:53068]
> Benign
> 163
> 100.0%
> 100.0%
> 40
> 97.8%
> 85.0%
> Bound Escalation
> 559
> 99.0%
> 97.0%
> 81
> 96.6%
> 84.0%
> 𝑙𝑖Escalation
> 108
> 100.0%
> 100.0%
> 15
> 98.0%
> 86.7%
> 𝐸Escalation
> 110
> 100.0%
> 100.0%
> 20
> 97.7%
> 85.0%
> 𝜏Escalation
> 120
> 99.7%
> 99.2%
> 17
> 94.6%
> 76.5%
> 𝑙𝑜Escalation
> 90
> 100.0%
> 100.0%
> 18
> 97.4%
> 88.9%
> Refined Bound
> 131
> 95.8%
> 87.8%
> 11
> 94.4%
> 81.8%
> Invariant
> 118
> 93.6%
> 86.4%
> 23
> 95.4%
> 73.9%
> 
> Total
> 840
> 98.7%
> 96.1%
> 144
> 95.7%
> 82.6%
> 
> action type), excluding tools with fixed or security-irrelevant pa-
> rameters.
**Location**: `Evaluation` [offsets: 53805:54308]
> We evaluate three capabilities: (1) con-
> sent reuse: the fraction of within-bound invocations correctly auto-
> permitted, whose complement is the false positive rate (unnecessary
> re-prompts); (2) bound escalation detection: per-dimension step accu-
> racy and recall for detecting invocations that exceed the consented
> lattice bound along 𝑙𝑖, 𝑙𝑜, 𝜏, 𝐸, or a refined resource constraint; and
> (3) invariant enforcement: recall for blocking invocations that vio-
> late user-specified deterministic constraints.
**Location**: `Evaluation` [offsets: 54309:54504]
> We report step-level
> accuracy (fraction of correctly decided steps) and trace-level accu-
> racy (fraction of traces where all steps are correct), together with
> aggregate Precision, Recall, and F1.
**Location**: `Evaluation` [offsets: 54890:55098]
> On benign traces, where all invocations remain
> within the previously consented bound, ConLeash achieves 100.0%
> step accuracy on single-server traces (163 traces) and 97.8% on
> 
> multi-server traces (40 traces).

## Block 8: Limitations
**Section Heading**: `Limitations.` [section offsets: 68051:68697]
**First 120 words verbatim** [offsets: 68051:68891]
> Limitations.
> ConLeash relies on LLMs for predicate extraction,
> and errors at this stage may lead to imprecise abstractions of ac-
> tions. While all enforcement decisions are made deterministically
> against explicit policy boundaries, such imprecision may result in
> missed or spurious prompts, and our guarantees therefore hold with
> respect to the system’s abstraction rather than end-to-end semantic
> correctness. In addition, the expressiveness of the current DSL is
> limited: it does not capture temporal constraints (e.g., “allow for
> today”) or domain-specific conditions, which may lead to missed
> violations when such semantics are required.
> 
> 10
> Related Work
> 
> Permission and Consent Models.
> Permission and consent
> models have evolved from static, install-time grants toward runtime
> authorization across web [20, 26, 43], mobile [14, 29, 30,

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Related Work` [offsets: 69501:70126]
> Access Control for Agentic Systems.
> Recent work constrains
> agent behavior through execution isolation [49], intent-aware poli-
> cies derived from tool semantics [17, 40], logic-based verification
> of user instructions [23], risk-adaptive enforcement via dynamic
> state tracking [51], or learning the permission preference based on
> history [50]. However, these systems enforce fixed or developer-
> specified policies and do not model how user consent evolves
> over a session: even when an agent faithfully follows user intent,
> individually-approved operations can compose into risk patterns
> that exceed the user’s original consent.
