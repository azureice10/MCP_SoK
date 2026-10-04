# Evidence Locator Packet: saeid-2026-game-theoretic-multi-agent-control

- **Title**: Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2606.10322
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\saeid-2026-game-theoretic-multi-agent-control\fulltext.txt
- **Character Count**: 119864

## Block 2: Contribution Sentences
**Location**: `Abstract—Large Language Models (LLMs) engaged in multi-` [offsets: 847:1059]
> To ad-
> dress these limitations, we introduce the Game-Theoretic Secure
> Model Context Protocol (GT-MCP), a controller-driven multi-
> agent solution that treats context management as a closed-loop
> dynamical process.

## Block 3: Method Locator
**Section Heading**: `D. Defenses: Isolation, Hierarchy, and Design-Time Control` [section offsets: 10262:12286]
**First 120 words verbatim** [offsets: 10262:11247]
> D. Defenses: Isolation, Hierarchy, and Design-Time Control
> 
> Several defenses separate trusted instructions from untrusted
> content using instruction hierarchy, isolation, and design-
> time separation principles. Spotlighting marks untrusted
> segments and constrains the model’s attention to them,
> reducing indirect injection transfer into core instructions [19].
> Design-time approaches advocate separating the instruction
> and data channels to reduce the attack surface [20]. Related
> instruction-isolation methods emphasize explicit boundary
> enforcement and controlled merging between trusted state and
> untrusted inflow [21]. System-level design patterns further
> provide practical guidance for preserving provenance, limiting
> authority escalation, and auditing state updates in LLM
> applications [22]. These approaches are valuable for reducing
> immediate instruction override, but they remain primarily
> local: they protect boundaries and validate segments without
> explicitly controlling the
**Section Heading**: `III. Methodology: Game-Theoretic Secure Context` [section offsets: 12286:14834]
**First 120 words verbatim** [offsets: 12286:13200]
> III. Methodology: Game-Theoretic Secure Context
> 
> Control (GT-MCP)
> 
> We propose Game-Theoretic Secure Context Control (GT-
> MCP), a trajectory-level control layer designed to stabilize
> multi-agent LLM reasoning under adversarial contextual pertur-
> bations. GT-MCP models multi-turn interaction as a closed-loop
> context-control process in which accepted outputs influence
> subsequent reasoning states. At interaction turn 𝑡∈{1, . . . ,𝑇},
> the user query is denoted by 𝑞𝑡, and the controller main-
> tains a validated context state 𝑐𝑡. This state contains trusted
> semantic memory, including verified claims, validated sum-
> maries, retrieved evidence, and previously accepted reasoning
> elements. The observed context ˜𝑐𝑡provided to the agents may
> additionally include untrusted inflows Δ𝑐𝑡, such as injected
> prompts, poisoned retrieval passages, manipulated tool outputs,
> and externally supplied contextual fragments:
> 
> ˜𝑐𝑡=
**Section Heading**: `B. Design Rationale` [section offsets: 17663:21178]
**First 120 words verbatim** [offsets: 17663:18548]
> B. Design Rationale
> 
> GT-MCP is motivated by the observation that prompt in-
> jection in multi-turn LLM systems is not only a local input-
> output failure but also a trajectory-level state-transition problem.
> 
> --- PAGE BREAK ---
> 
> Fig. 1: Layered GT-MCP architecture for closed-loop context stabilization. The controller separates validated context from untrusted
> inflows, coordinates heterogeneous LLM agents, scores candidate outputs based on causal consistency, cross-agent agreement, and
> contextual drift, and updates persistent memory only through validated selections.
> 
> In persistent-context applications, a response accepted at turn
> 𝑡may become part of the memory that conditions later
> generations. Therefore, an adversarial fragment that appears
> locally plausible can gradually shift the reasoning trajectory
> if it is repeatedly accepted, summarized, and used as support for
> future
**Section Heading**: `Method` [section offsets: 62852:64791]
**First 120 words verbatim** [offsets: 62852:63784]
> Method
> Description
> 
> Single-agent LLM
> One LLM response is directly accepted
> without multi-agent control
> Majority voting
> Three agents generate responses; output is
> selected by semantic majority agreement
> Prompt filtering
> Candidate
> outputs
> are
> filtered
> using
> surface-level injection detection before up-
> date
> RAG defense
> Retrieved and contextual evidence is sani-
> tized before candidate generation
> No-CCI
> GT-MCP without causal consistency scor-
> ing
> No-AGR
> GT-MCP without cross-agent agreement
> scoring
> No-CDS
> GT-MCP without candidate-specific drift
> monitoring
> No-Heal
> GT-MCP without rollback and quarantine
> recovery
> Full GT-MCP
> Complete controller with CCI, AGR,
> CDS, and self-healing
> 
> TABLE VI: Evaluation metrics.
> 
> Metric
> Definition
> 
> ISR
> Fraction of turns with controller-level ad-
> versarial success
> CDS
> Candidate-specific contextual drift after
> tentative update
> CCI
> Structural support of extracted claims in 𝐺𝑡
> AGR
> Semantic agreement

## Block 4: Evaluation Locator
**Section Heading**: `results on stability, utility, efficiency, and robustness. Section VI` [section offsets: 7516:7705]
**First 120 words verbatim** [offsets: 7516:8403]
> results on stability, utility, efficiency, and robustness. Section VI
> discusses the findings, Section VII outlines limitations and
> future directions, and Section VIII concludes the paper.
> 
> II. Related Work
> 
> This section reviews prior work along four directions and
> identifies the remaining gap in trajectory-level context control.
> 
> A. Prompt Injection and Context Poisoning
> 
> Prompt injection has evolved from single-turn jailbreaks to-
> ward stateful failures in which injected instructions persist inside
> long-lived contexts, retrieved passages, and tool outputs. Early
> optimization-based jailbreak work shows that short adversarial
> strings can reliably disrupt aligned behavior without modifying
> model weights [14]. More recent studies focus on indirect
> prompt injection, in which attackers embed instructions in exter-
> nal content that later enter the model’s context via retrieval and
**Section Heading**: `evaluation, the controller appends decision metadata to the` [section offsets: 52211:58688]
**First 120 words verbatim** [offsets: 52211:53029]
> evaluation, the controller appends decision metadata to the
> packet:
> 
> 𝑖=1, ˆ𝑖𝑡, Q𝑡+1, 𝑑★
> 
> pkt𝑡, {𝑦𝑖(𝑡)}3
> 
> 𝑖=1, {S𝑖}3
> 
> 𝑖=1, {𝑇𝑖(𝑡)}3
> 
> pkt+
> 
> ,
> (45)
> where S𝑖is the extracted claim set for candidate 𝑦𝑖(𝑡), 𝑇𝑖(𝑡)
> is its trust score, ˆ𝑖𝑡is the selected agent index, Q𝑡+1 is the
> quarantine set, and 𝑑★is the rollback depth if recovery is
> triggered. This packetized interface makes GT-MCP auditable
> and reproducible. It allows the controller to trace which
> fragments entered the observed context, which claims were
> extracted, how trust scores were assigned, which output was
> selected, and whether recovery was activated. Therefore, the
> MCP packet acts as the operational bridge between multi-agent
> generation, causal graph validation, trust aggregation, and self-
> healing recovery.
> 
> 𝑡=
> 
> P. Controller Parameter Calibration
> 
> The
**Section Heading**: `IV. Experimental Setup` [section offsets: 58688:62852]
**First 120 words verbatim** [offsets: 58688:59537]
> IV. Experimental Setup
> 
> We evaluate GT-MCP in a closed-loop multi-turn adversarial
> setting designed to test whether malicious contextual pertur-
> bations can persist across turns, alter the validated context,
> and affect future reasoning. The primary evaluation horizon
> consists of 𝑇= 500 interaction turns per run. Each turn contains
> one user query, one observed context assembly step, three
> candidate LLM responses, one controller selection decision,
> one tentative context update, and, when needed, one self-healing
> recovery decision. To support paired comparisons, all methods
> are evaluated under the same query sequence, attack schedule,
> and random seeds. Unless otherwise stated, each method is
> repeated across 𝑅= 10 independent seeds, yielding 5,000 turn-
> level observations per method. For paired ablation analysis, the
> full GT-MCP pipeline and
**Section Heading**: `V. Experimental Results` [section offsets: 64791:65014]
**First 120 words verbatim** [offsets: 64791:65623]
> V. Experimental Results
> All evaluations are conducted under the full closed-loop GT-
> MCP pipeline described in Section III. All experiments use
> identical seeds across runs to ensure paired comparisons and
> reproducibility.
> 
> A. Context Stability and Drift Behavior
> 
> We first examine whether GT-MCP preserves contextual
> stability across the 𝑇= 500-turn closed-loop evaluation horizon
> 
> --- PAGE BREAK ---
> 
> Fig. 2: Distribution of selected-output contextual drift across
> 500 interaction turns.
> 
> TABLE VII: Drift severity, utility impact, and recovery activa-
> tion.
> 
> Category
> Count Fraction (%) Median Drift Mean Utility Min Utility Heal (%)
> 
> Near-zero drift
> 498
> 99.6
> 0.000
> -0.18
> -2.10
> 0.0
> Nonzero drift
> 2
> 0.4
> 27.63
> -23.46
> -24.93
> 100.0
> 
> defined in Section IV. Contextual drift is measured after the
> controller selects a candidate response

## Block 5: Attack-Set Excerpts
**Location**: `evaluation is organized according to benchmark-inspired attack` [offsets: 102690:102822]
> evaluation is organized according to benchmark-inspired attack
> styles commonly used in prompt-injection and agent-security
> research.
**Location**: `evaluation is organized according to benchmark-inspired attack` [offsets: 103033:103199]
> The goal is not to reproduce
> each benchmark verbatim, but to align the evaluation with
> their dominant threat patterns while preserving the closed-loop
> GT-MCP setting.
**Location**: `evaluation is organized according to benchmark-inspired attack` [offsets: 103752:103936]
> These results support the trajectory-level robust-
> ness of GT-MCP: benchmark-inspired attacks may introduce
> localized instability, but they do not persist as validated context
> updates.
**Location**: `evaluation is organized according to benchmark-inspired attack` [offsets: 106139:106223]
> TABLE XXXIII: Benchmark-inspired adversarial evaluation
> across the 172 attack turns.
**Location**: `evaluation is organized according to benchmark-inspired attack` [offsets: 106225:106483]
> Benchmark Style
> Attack Turns
> High-Drift Events
> 
> PromptInject-style
> 42
> 1
> PoisonedRAG-style
> 48
> 1
> AgentDojo-style
> 34
> 0
> Delayed Trigger
> 24
> 0
> Agreement Mimicry
> 24
> 0
> 
> Total
> 172
> 2
> 
> TABLE XXXIV: Residual vulnerability patterns observed
> during adversarial evaluation.

## Block 6: Baseline Excerpts
**Location**: `IV. Experimental Setup` [offsets: 59479:59644]
> For paired ablation analysis, the
> full GT-MCP pipeline and each ablated variant are evaluated
> using identical seeds and identical adversarial perturbation
> schedules.
**Location**: `IV. Experimental Setup` [offsets: 61483:61573]
> We compare the full GT-MCP
> pipeline against representative baselines and ablated variants.
**Location**: `IV. Experimental Setup` [offsets: 61574:61705]
> The baseline methods include a single-agent LLM, majority
> voting across agents, prompt filtering, and a retrieval-oriented
> defense.
**Location**: `IV. Experimental Setup` [offsets: 61706:61881]
> The ablation variants remove one GT-MCP component
> at a time: causal consistency scoring, cross-agent agreement,
> candidate-specific drift monitoring, and self-healing recovery.
**Location**: `IV. Experimental Setup` [offsets: 62784:62850]
> For ablation
> 
> 12
> 
> TABLE V: Evaluated methods and ablated variants.
**Location**: `G. Baseline Comparison and Comparative Robustness Evalu-` [offsets: 96629:96830]
> Baseline Comparison and Comparative Robustness Evalu-
> ation
> 
> We compare GT-MCP against representative LLM defense
> and orchestration baselines under the same 𝑇= 500-turn
> adversarial evaluation protocol.

## Block 7: Cost Excerpts
**Location**: `results on stability, utility, efficiency, and robustness. Section VI` [offsets: 7516:7574]
> results on stability, utility, efficiency, and robustness.
**Location**: `evaluation, the controller appends decision metadata to the` [offsets: 56456:56650]
> The same evaluation
> logic applies to additional trajectory-level metrics, including
> mean causal consistency, candidate-specific contextual drift,
> recovery frequency, rollback depth, and utility.
**Location**: `IV. Experimental Setup` [offsets: 59645:59703]
> The evaluation contains both benign and adversarial
> turns.
**Location**: `IV. Experimental Setup` [offsets: 59704:59881]
> Out of the 𝑇= 500 turns in each run, 328 turns are benign
> and 172 turns contain adversarial perturbations, corresponding
> to 65.6% benign exposure and 34.4% adversarial exposure.
**Location**: `IV. Experimental Setup` [offsets: 60074:60337]
> Benign interaction
> 328
> 65.6
> Direct prompt injection
> 30
> 6.0
> Retrieval poisoning
> 40
> 8.0
> Tool-output injection
> 30
> 6.0
> Dormant trigger injection
> 22
> 4.4
> Trajectory steering
> 30
> 6.0
> Agreement mimicry
> 20
> 4.0
> 
> Total
> 500
> 100.0
> 
> TABLE IV: Controller and agent configuration.
**Location**: `IV. Experimental Setup` [offsets: 62353:62552]
> We also report contextual drift, causal consistency, cross-agent
> agreement, utility, recovery frequency, rollback depth, quaran-
> tine size, stable-turn percentage, token usage, and latency per
> token.

## Block 8: Limitations
**Section Heading**: `VII. Limitations and Future Directions` [section offsets: 111446:111667]
**First 120 words verbatim** [offsets: 111446:112405]
> VII. Limitations and Future Directions
> 
> Although our experiments demonstrate bounded contextual
> drift, stable reasoning manifolds, and incentive-aligned multi-
> agent interaction under the evaluated configuration, several
> limitations remain. First, the studies employ a fixed set of
> LLM agents and architectures; broader model heterogeneity,
> including multimodal and domain-specialized systems, may
> alter the geometry of the reasoning manifold and the efficacy
> of trust-weighted selection. Second, structural grounding and
> cross-agent agreement serve as operational proxies for reasoning
> validity and do not guarantee epistemic correctness when
> the validated context is incomplete and noisy, highlighting
> the need for external verification signals, causal auditing,
> and uncertainty calibration. Third, the threat model assumes
> contextual perturbations with at most one compromised agent;
> more aggressive adversarial scenarios, including coordinated
> multi-agent

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Abstract—Large Language Models (LLMs) engaged in multi-` [offsets: 1305:1863]
> When instability is detected, a rollback-based
> self-healing mechanism restores the validated context, preventing
> propagation of unsupported fragments. Empirical evaluation over
> 500 interaction turns under an adaptive adversarial threat model
> demonstrates that contextual drift remains bounded in 99.6%
> of turns, with recovery required in only 0.4%. The per-turn
> utility is tightly concentrated (median = −0.19, P05 = −0.72, P95
> = 0.30) with severe degradation (< −1) occurring only in 0.4% of
> cases, and no injection attempt succeeds at the controller level.
**Matched Term**: `adaptive` | **Location**: `A. Nikanjam‡ is with the Huawei Distributed Scheduling and Data Engine` [offsets: 5921:6318]
> First,
> context evolution is modeled as a bounded adversarial control
> problem. Second, multi-agent coordination is formulated as a
> repeated Stackelberg interaction between a controller and an
> adaptive adversary. Third, trust-weighted selection combines
> 
> --- PAGE BREAK ---
> 
> structural grounding, semantic agreement, and temporal sta-
> bility to make adversarial deviation strategically unattractive.
**Matched Term**: `adaptive` | **Location**: `A. Nikanjam‡ is with the Huawei Distributed Scheduling and Data Engine` [offsets: 6959:7321]
> • We evaluate GT-MCP across 500 interaction turns under
> an adaptive adversarial threat model, showing bounded
> contextual drift in 99.6% of turns, rare recovery activation
> in 0.4% of turns, zero controller-level injection success,
> stable selected-output win rates above 98%, and predictable
> efficiency scaling.
> The remainder of this paper is organized as follows.
**Matched Term**: `adaptive` | **Location**: `D. Adversarial Game Formulation` [offsets: 23130:23464]
> Adversarial Game Formulation
> 
> GT-MCP formulates prompt injection and context poison-
> ing as a repeated interaction between a controller and an
> adaptive attacker. The attacker may influence the observed
> context through malicious user prompts, poisoned retrieved
> content, manipulated tool outputs, and compromised candidate
> generations.
**Matched Term**: `adaptive` | **Location**: `D. Adversarial Game Formulation` [offsets: 24189:24606]
> where I(·) is the indicator function and ˆ𝑦𝑡is the controller-
> selected output at turn 𝑡. The controller seeks a selection-and-
> recovery policy 𝜋that remains robust under adaptive, history-
> dependent perturbations. This yields the following minimax
> objective:
> 
> J  𝜋, {Δ𝑐𝑡}𝑇
> 
> min
> 
> 𝜋
> max
> {Δ𝑐𝑡}𝑇
> 
> ,
> (11)
> 
> 𝑡=1
> 
> 𝑡=1
> 
> 5
> 
> where 𝜋maps the observed context ˜𝑐𝑡and candidate responses
> {𝑦𝑖(𝑡)}3
> 
> 𝑖=1 to the selected output ˆ𝑦𝑡.
**Matched Term**: `adaptive` | **Location**: `E. Threat Model Details` [offsets: 25230:25747]
> Threat Model Details
> 
> GT-MCP assumes an adaptive adversary that cannot directly
> overwrite the validated context state 𝑐𝑡, but can influence the
> observed context through untrusted perturbations:
> 
> ˜𝑐𝑡= 𝑐𝑡⊕Δ𝑐𝑡,
> (12)
> 
> where Δ𝑐𝑡may include malicious user instructions, poisoned
> retrieved passages, manipulated tool outputs, hidden direc-
> tives embedded in external content, and adversarial candidate
> generations. Only controller-approved outputs ˆ𝑦𝑡can update
> the trusted state through the legitimate update operator U(·).
**Matched Term**: `evasion` | **Location**: `F. Game-Theoretic Formulation of Secure Multi-Agent Inter-` [offsets: 32161:32627]
> Consequently, the controller reduces the expected payoff of
> adversarial deviation by assigning lower trust to candidates that
> lack causal support, contradict high-confidence graph nodes,
> and induce abnormal drift. In operational terms, this means that
> adversarial success requires simultaneous evasion of the causal
> 
> --- PAGE BREAK ---
> 
> consistency, agreement, and drift-monitoring components. This
> formulation establishes the GT-MCP’s incentive-alignment
> principle.
**Matched Term**: `adaptive` | **Location**: `B. Multi-Agent Behavior and Selection Dynamics` [offsets: 73132:73395]
> 5: Trust-score distributions by agent. Differences in dis-
> persion show that the agents contribute distinct structural and
> semantic signals to the controller, enabling context-adaptive
> selection rather than fixed model preference.
> 
> stability, and cost efficiency.
**Matched Term**: `evasion` | **Location**: `F. Game-Theoretic Outcomes` [offsets: 92580:93098]
> The benign and adversarial utility distributions differ primarily
> in localized tail degradation rather than in broad distributional
> displacement. Attacker profitability remains negligible because
> successful long-horizon manipulation requires simultaneous
> evasion of structural grounding, peer-agreement checks, and
> candidate-specific drift control. This supports the incentive-
> alignment interpretation of GT-MCP: adversarial perturbations
> may increase local cost, but they do not create a systematic
> payoff advantage.
**Matched Term**: `adaptive` | **Location**: `G. Baseline Comparison and Comparative Robustness Evalu-` [offsets: 99790:100025]
> --- PAGE BREAK ---
> 
> TABLE XXX: Comparative robustness evaluation under adaptive adversarial interaction. Lower values are better for injection
> success, drift, utility degradation, and latency; higher values are better for stable turns.
