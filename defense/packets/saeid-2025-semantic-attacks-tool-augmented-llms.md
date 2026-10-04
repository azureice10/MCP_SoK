# Evidence Locator Packet: saeid-2025-semantic-attacks-tool-augmented-llms

- **Title**: Semantic Attacks on Tool-Augmented LLMs: Securing the Model Context Protocol Against Descriptor-Level Manipulation
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2512.06556
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\saeid-2025-semantic-attacks-tool-augmented-llms\fulltext.txt
- **Character Count**: 85316

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) enables Large` [offsets: 876:1090]
> We propose a layered defense solution
> that integrates descriptor integrity verification, pre-context se-
> mantic vetting with an auxiliary LLM, and lightweight runtime
> guardrails, without requiring model retraining.
**Location**: `Abstract—The Model Context Protocol (MCP) enables Large` [offsets: 1091:1282]
> We evaluate
> GPT-5.3, DeepSeek-V3, and LLaMA-3.5 across eight prompting
> strategies in controlled, adversarial MCP scenarios in which tool
> metadata is manipulated to simulate realistic attacks.
**Location**: `I. INTRODUCTION` [offsets: 6998:8071]
> we introduce a systematic evaluation methodology
> for MCP-integrated LLM systems that isolates descriptor-
> level semantic manipulation under controlled and realistic
> operational constraints, including syntactically valid tools, un-
> changed model parameters, and standard invocation pipelines
> [13], [17]. The methodology incorporates controlled descriptor
> mutation, real-world descriptor corpus analysis, ecosystem-
> level MCP exposure assessment, adversarial stress testing,
> cross-model transferability evaluation, enterprise-oriented de-
> ployment scenarios, extended ablation analysis, prompting-
> strategy analysis, and layered protocol-level defenses com-
> bining descriptor integrity verification, semantic vetting, run-
> time guardrails, and context-aware enforcement across the
> descriptor lifecycle. This design enables reproducible analysis
> of descriptor-driven vulnerabilities without requiring an un-
> realistic compromise of infrastructure. We evaluate GPT-5.3,
> DeepSeek-V3, and LLaMA-3.5 across representative attack
> scenarios (Tool Poisoning, Shadowing, Rug Pull) and

## Block 3: Method Locator
**Section Heading**: `III. METHODOLOGY` [section offsets: 12931:14138]
**First 120 words verbatim** [offsets: 12931:13875]
> III. METHODOLOGY
> 
> This section describes the experimental setup for evaluat-
> ing descriptor-level vulnerabilities in MCP-integrated LLM
> systems. Our approach isolates the interactions among tool
> descriptors, MCP context reasoning behavior, and mitigation
> mechanisms within a controlled MCP environment. Figure 1
> illustrates the end-to-end evaluation pipeline, capturing the
> full lifecycle of a tool-augmented LLM interaction, including
> prompt construction, context assembly, MCP reasoning, tool
> selection, response generation, and metric logging. This design
> enables systematic analysis of how adversarial descriptors
> are introduced, how they propagate through MCP context
> reasoning, and how they impact both execution outcomes and
> operational performance. The setup consists of three main
> components. First, a scenario generator produces controlled
> task prompts, prompting strategies, and adversarial descriptor
> variants. Second, the MCP layer
**Section Heading**: `implementation-specific identifiers while preserving semantic` [section offsets: 46294:47083]
**First 120 words verbatim** [offsets: 46294:47244]
> implementation-specific identifiers while preserving semantic
> structure, action verbs, tool purpose, and contextual qualifiers.
> We categorized risky semantic cues into five groups: user-
> context expansion, sensitive-data reference, authority dele-
> gation, automatic execution phrasing, and ambiguous opti-
> mization language. Table XIV summarizes their distribution.
> These results support the realism of our adversarial descrip-
> tor construction. Phrases such as “improve accuracy, include
> relevant context, automatically verify,” and “prioritize user-
> related information” are not syntactically malicious, but they
> can subtly shift MCP reasoning and tool selection. This
> motivates treating descriptors as active semantic inputs rather
> than passive metadata in tool-augmented LLM systems.
> 
> E. Performance Analysis
> 
> To address RQ2, this section evaluates latency behavior
> across models and prompting strategies, and examines how
> response time interacts

## Block 4: Evaluation Locator
**Section Heading**: `results indicate that tool metadata actively shapes reasoning,` [section offsets: 11178:11328]
**First 120 words verbatim** [offsets: 11178:12165]
> results indicate that tool metadata actively shapes reasoning,
> highlighting a semantic attack surface directly relevant to
> descriptor-level threats.
> 
> C. MCP-Specific Vulnerabilities
> 
> Descriptor-driven attacks are particularly relevant in MCP
> architectures. Radosevich and Halloran [32] identify protocol-
> level
> vulnerabilities
> and
> introduce
> McpSafetyScanner,
> showing that insecure descriptors can lead to credential
> leakage and agent hijacking. Narajala et al. [33] report
> that real-world MCP deployments may remain vulnerable
> to descriptor manipulation and lifecycle inconsistencies.
> Benchmarks such as MCPSecBench [34] demonstrate that
> descriptor
> manipulation
> can
> impact
> tool
> selection
> even
> under permission constraints. MCP-Guard [35] evaluates
> integrity-based defenses, and MCP-Tox [36] demonstrates
> 
> --- PAGE BREAK ---
> 
> that subtle descriptor perturbations can significantly impact
> reasoning without violating schema constraints.
> 
> The literature synthesis reveals three key gaps: 1)
**Section Heading**: `evaluation of descriptor-driven vulnerabilities across different` [section offsets: 23252:23335]
**First 120 words verbatim** [offsets: 23252:24149]
> evaluation of descriptor-driven vulnerabilities across different
> tool categories.
> 
> D. Evaluation
> 
> The evaluation setup characterizes the impact of adversarial
> descriptors on tool selection, MCP context formation, and
> safety outcomes in MCP-integrated LLM systems. We assess
> both hard failures (unsafe invocations) and partial impacts
> (data leakage, intent deviation, and degraded behavior), ad-
> dressing limitations of binary blocked/allowed reporting. For
> example, consider a user request to retrieve public information.
> The model is presented with multiple tools, including a benign
> retrieval tool and a semantically manipulated variant whose
> descriptor emphasizes user-related details. The MCP system
> 
> --- PAGE BREAK ---
> 
> aggregates these descriptors into the context, after which the
> model reasons over the available tools and selects one for
> execution. This process illustrates how descriptor
**Section Heading**: `D. Evaluation` [section offsets: 23335:24422]
**First 120 words verbatim** [offsets: 23335:24210]
> D. Evaluation
> 
> The evaluation setup characterizes the impact of adversarial
> descriptors on tool selection, MCP context formation, and
> safety outcomes in MCP-integrated LLM systems. We assess
> both hard failures (unsafe invocations) and partial impacts
> (data leakage, intent deviation, and degraded behavior), ad-
> dressing limitations of binary blocked/allowed reporting. For
> example, consider a user request to retrieve public information.
> The model is presented with multiple tools, including a benign
> retrieval tool and a semantically manipulated variant whose
> descriptor emphasizes user-related details. The MCP system
> 
> --- PAGE BREAK ---
> 
> aggregates these descriptors into the context, after which the
> model reasons over the available tools and selects one for
> execution. This process illustrates how descriptor semantics
> can impact tool selection and downstream behavior.
**Section Heading**: `Results are stratified by attack type to enable scenario-level` [section offsets: 25464:27754]
**First 120 words verbatim** [offsets: 25464:26206]
> Results are stratified by attack type to enable scenario-level
> analysis. We define an aggregate risk score:
> 
> Rsys = w1ρ + w2ι + w3 ¯Sharm,
> (17)
> 
> where ¯Sharm is the normalized harm score derived from leakage
> and intent deviation. Unless otherwise specified, we use equal
> weights (w1 = w2 = w3) to balance security and behavioral
> impact without introducing bias. We employ a secondary
> language model Lvet to assess the safety of tool usage based
> on the prompt P′, candidate tool τ ∗, and descriptor d∗.
> This verifier operates independently from the primary model
> 
> used for tool selection, allowing separation between decision-
> making and validation. The verifier produces a binary safety
> decision:
> 
> Isafe = Lvet(P′, τ ∗, d∗),
> (18)
> 
> where Isafe

## Block 5: Attack-Set Excerpts
**Location**: `F. Experimental Setup` [offsets: 30518:30646]
> The testbed
> consists of a fixed set of in-house tools to ensure con-
> sistent behavior and full observability across experiments.
**Location**: `F. Experimental Setup` [offsets: 30707:30773]
> TABLE II: Toolset used in the experimental enterprise MCP
> testbed.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `D. Evaluation` [offsets: 23774:23940]
> The model is presented with multiple tools, including a benign
> retrieval tool and a semantically manipulated variant whose
> descriptor emphasizes user-related details.
**Location**: `Results are stratified by attack type to enable scenario-level` [offsets: 27419:27558]
> The goal of the applied mitigation mechanisms is to reduce
> this exposure while preserving normal system behavior un-
> der benign conditions.
**Location**: `Results are stratified by attack type to enable scenario-level` [offsets: 27559:27752]
> To evaluate this trade-off, we report
> changes in malicious selection rate (ρ), unsafe invocation rate
> (ι), aggregated harm score ( ¯Sharm), latency overhead (∆t), and
> false-positive rate (φfp).
**Location**: `E. Evaluation Protocol` [offsets: 27778:27996]
> The evaluation process measures the mapping from a
> transformed prompt and MCP context to the selected tool,
> while recording malicious selection, unsafe invocation, harm
> severity, false positives, and inference latency.
**Location**: `E. Evaluation Protocol` [offsets: 28128:28252]
> The
> MCP context C is then constructed by combining benign and
> adversarial tool descriptors through the registration process.
**Location**: `E. Evaluation Protocol` [offsets: 28561:28825]
> During this process, all relevant metrics are recorded,
> including the malicious selection rate ρ, unsafe invocation
> indicators ι, leakage and intent-related harm scores Sleak,
> Sintent, the false positive rate, latency, and their corresponding
> confidence intervals.

## Block 8: Limitations
**Section Heading**: `limitations.` [section offsets: 40096:40849]
**First 120 words verbatim** [offsets: 40096:41024]
> limitations.
> 
> TABLE IX: Block rates under baseline and adversarial stress
> conditions (Tool Poisoning).
> 
> Model
> Baseline
> Stress-Test
> 
> GPT-5.3
> 0.60
> 0.45
> DeepSeek-V3
> 0.49
> 0.37
> LLaMA-3.5
> 0.42
> 0.30
> 
> Figure 3 shows the relationship between reasoning depth
> and unsafe tool invocation. Deeper reasoning chains amplify
> the propagation of descriptor signals, leading to higher rates of
> unsafe invocations. This result indicates that reasoning depth,
> rather than prompt length alone, strongly impacts vulnerability
> to descriptor-driven manipulation.
> 
> Fig. 3: Impact of reasoning depth on unsafe tool invocation
> across prompting strategies. Deeper reasoning chains amplify
> the propagation of the descriptor signal, increasing exposure
> to descriptor-driven attacks.
> 
> B. Descriptor Mutation Engine
> 
> To address RQ1, we implemented a lightweight descriptor
> mutation engine to systematically generate adversarial tool
> descriptors while preserving

## Block 9: Adaptivity Hits
**Matched Term**: `optimized against` | **Location**: `I. Impact of Prompting Strategies: A Realistic Enterprise Case` [offsets: 63189:63725]
> To address RQ3, we evaluated whether descriptor-level
> attacks generalize across different LLM architectures by con-
> ducting a cross-model transferability analysis. Adversarial
> descriptors were optimized against one source model and
> subsequently evaluated against the remaining target models
> without modification.
> 
> Ti→j = ρj(Dadv
> 
> i
> )
> ρi(Dadv
> 
> i
> ) ,
> (24)
> 
> where Dadv
> 
> i
> denotes descriptors optimized against source
> model i, ρi is the malicious selection rate on the source
> model, and ρj is the malicious selection rate on target model j.
**Matched Term**: `optimized against` | **Location**: `I. Impact of Prompting Strategies: A Realistic Enterprise Case` [offsets: 63544:63824]
> where Dadv
> 
> i
> denotes descriptors optimized against source
> model i, ρi is the malicious selection rate on the source
> model, and ρj is the malicious selection rate on target model j.
> Table XXVI shows that descriptor-level attacks transfer across
> models with moderate effectiveness.
**Matched Term**: `optimized against` | **Location**: `I. Impact of Prompting Strategies: A Realistic Enterprise Case` [offsets: 63825:64345]
> Adversarial descriptors
> generated against LLaMA-3.5 transfer most strongly to GPT-
> 5.3 and DeepSeek-V3, suggesting that descriptors exploit-
> ing weaker semantic filtering can still affect stronger mod-
> els. Transferability is asymmetric: attacks optimized against
> GPT-5.3 transfer less effectively to LLaMA-3.5, likely be-
> cause GPT-5.3-specific adversarial cues interact differently
> with LLaMA-3.5’s safety filtering and reasoning behavior,
> highlighting model-dependent robustness to descriptor-driven
> manipulation.
> 
> V.
**Matched Term**: `adaptive` | **Location**: `3 LLMs × 8 strategies; 1800+ runs;` [offsets: 72400:72863]
> MCP security must address both execu-
> tion behavior and semantic intent. As tool-augmented LLM
> systems become increasingly autonomous, effective security
> approaches should integrate descriptor semantics, reasoning
> dynamics, and orchestration policies, potentially embedding
> descriptor validation, semantic auditing, and adaptive control
> directly into the orchestration layer to support standardized
> evaluation and robust operation in real-world deployments.
> 
> VII.
**Matched Term**: `adaptive` | **Location**: `VIII. FUTURE WORK` [offsets: 75549:75878]
> FUTURE WORK
> 
> Future work should extend evaluation to larger-scale, real-
> world MCP deployments, incorporating adaptive adversarial
> strategies and dynamic validation mechanisms. Investigating
> distributed trust models and alternative provenance verification
> will improve applicability in decentralized and federated en-
> vironments.
