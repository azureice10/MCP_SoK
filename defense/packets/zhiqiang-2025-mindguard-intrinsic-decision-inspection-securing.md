# Evidence Locator Packet: zhiqiang-2025-mindguard-intrinsic-decision-inspection-securing

- **Title**: MindGuard: Intrinsic Decision Inspection for Securing LLM Agents Against Metadata Poisoning
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2508.20412
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\zhiqiang-2025-mindguard-intrinsic-decision-inspection-securing\fulltext.txt
- **Character Count**: 94569

## Block 2: Contribution Sentences
**Location**: `Abstract—The vulnerability of LLM decision-making to pollu-` [offsets: 891:1068]
> To bridge this gap, we propose Decision Inspection, a novel
> security paradigm that scrutinizes the LLM’s internal tool-
> call logic by tracking and verifying decision provenance.
**Location**: `Abstract—The vulnerability of LLM decision-making to pollu-` [offsets: 1069:1264]
> We
> introduce the Decision Dependency Graph (DDG) to charac-
> terize the LLM’s decision-making logic as the dependency
> of call decisions on different input context elements (e.g.,
> query, metadata).

## Block 3: Method Locator
**Section Heading**: `Method` [section offsets: 7634:7811]
**First 120 words verbatim** [offsets: 7634:8409]
> Method
> Track
> Detect
> Attribute
> Plug-in
> Model-free
> 
> Static Scan∗
> ✗
> ✗
> ✓
> ✓
> ✗
> Architect Isolate∗
> ✗
> ✓
> ✗
> ✗
> ✗
> Behavior Audit+
> ✗
> ✓
> ✗
> ✓
> ✗
> Policy Enhance+
> ✗
> ✓
> ✗
> ✗
> ✓
> 
> MINDGUARD†
> ✓
> ✓
> ✓
> ✓
> ✓
> 
> 1. Track: decision-level tracking of which context influenced the
> call; Detect: per-invocation detection of poisoned calls; Attribute:
> identification of the specific poisoned context; Model-free: requires
> no external LLM.
> 2. Working on: ∗decision input; + decision output; † decision logic.
> 
> indistinguishability between implicit code and data at the
> pre-decision stage, and the unverifiability of dynamic
> invocation intent at the post-decision stage.
> 
> Our Solution. To bridge this gap, we propose De-
> cision Inspection, the first decision integrity verification
> mechanism that directly scrutinizes
**Section Heading**: `4. Methodology` [section offsets: 25666:26075]
**First 120 words verbatim** [offsets: 25666:26547]
> 4. Methodology
> 
> To achieve decision inspection, we first introduce the
> Decision Dependency Graph, a formal model that charac-
> terizes the LLM’s decision logic (§4.1). We then devise an
> attention-based mechanism to track the influence of different
> contextual elements on decisions (§4.2). Finally, we propose
> an integrity-anomaly-based verification scheme to accurately
> identify compromised decisions (§4.3).
> 
> 4.1. Characterization: Decision Dependency Graph
> 
> To facilitate the three objectives of decision inspection,
> we require a formal model to characterize the internal
> decision logic of F(·), analogous to how Program Depen-
> dence Graphs [33] (PDGs) model the internal logic flows
> of deterministic programs in traditional security. However,
> such deterministic models are ill-suited for the probabilis-
> tic nature of LLM decision-making, which operates not
> through fixed control
**Section Heading**: `5. System Design` [section offsets: 36592:36975]
**First 120 words verbatim** [offsets: 36592:37393]
> 5. System Design
> 
> We implement MINDGUARD (Fig. 4), a prototype
> guardrail that performs intrinsic self-inspection, constructs
> and analyzes the Decision Dependency Graph during the
> reasoning process to achieve our security goals. This section
> introduces the design of Context Vertex Parser (§5.1),
> Dependency Graph Builder (§5.2), and Decision Integrity
> Defender (§5.3) in MINDGUARD.
> 
> 5.1. Context Vertex Parser
> 
> The Context Vertex Parser aims to instantiate the formal
> DDG model defined in §4.1. It analyzes the LLM’s input
> 
> --- PAGE BREAK ---
> 
> Figure 4: System Design of MINDGUARD. Once generating a tool call, MINDGUARD parses the LLM’s context to extract
> the vertices V (Context Vertex Parser in §5.1) and builds the decision dependency graph G from its attention matrix
> (Dependency Graph Builder in
**Section Heading**: `Method` [section offsets: 59773:59934]
**First 120 words verbatim** [offsets: 59773:60391]
> Method
> Qwen3-8b†
> Qwen3-8b
> Phi-4†
> 
> TPR↑|FPR↓
> TPR↑|FPR↓
> TPR↑|FPR↓
> 
> Atten. Track
> 62.6 | 48.3
> 26.5 | 38.4
> 69.9 | 58.8
> 
> LLM-Guard
> 33.2 | 36.1
> 36.8 | 35.3
> 35.2 | 39.7
> LLM Detect
> 42.2 | 38.8
> 50.0 | 41.0
> 40.1 | 45.1
> 
> Static
> 
> Scan
> 
> CaMeL
> 0.0 | 0.0
> 0.0 | 0.0
> 0.0 | 0.0
> PFI
> 0.0 | 0.0
> 0.0 | 0.0
> 0.0 | 0.0
> 
> Architect
> 
> Isolate
> 
> MELON
> 14.3 | 4.0
> 47.1 | 4.5
> 2.0 | 0.5
> MCIP
> 58.5 | 54.0
> 57.4 | 51.8
> 56.4 | 54.9
> 
> Behavior
> 
> Audit
> 
> Decision
> 
> Inspect
> Ours
> 96.5 | 5.2
> 94.1 | 3.9
> 91.0 | 9.5
> 
> such as CaMeL [18] and MCIP [20]. Fig. 5 further com-
> pares MINDGUARD against other non-architectural, non-
> fine-tuning mechanisms in terms of runtime

## Block 4: Evaluation Locator
**Section Heading**: `6. Evaluation` [section offsets: 46273:47324]
**First 120 words verbatim** [offsets: 46273:47117]
> 6. Evaluation
> 
> We evaluate MINDGUARD on various LLM agents us-
> ing diverse applications under both fully adversarial attack
> datasets and realistic settings (normal calls contain no poi-
> soned descriptions). Our highlights are as follows:
> 
> • MINDGUARD successfully achieves our security goals,
> demonstrating 97%+ accuracy in identifying poisoned calls
> and 98%+ accuracy in tracing them to the poisoned source,
> while highly adaptable across various LLMs (§6.2).
> 
> • As an intrinsic self-inspection mechanism, MIND-
> GUARD requires no external resources. Its security perfor-
> mance outperforms SOTA methods while saving over 1000+
> token overhead for each invocation (§6.3).
> 
> --- PAGE BREAK ---
> 
> TABLE 5: Label Distribution for Evaluated LLM Agent
> 
> LLM
> MCPTox (#)
> InjecAgent (#)
> RAS-Eval (#)
> 
> Normal
> Poisoned
> Normal
> Poisoned
> Normal
> Poisoned
> 
> Qwen3-8b
**Section Heading**: `6.1. Experimental Setup` [section offsets: 47942:51735]
**First 120 words verbatim** [offsets: 47942:48791]
> 6.1. Experimental Setup
> 
> Dataset and LLM Agent. To evaluate the performance
> of MINDGUARD, we curated three distinct attack datasets:
> 1) MCPTox [9]. This dataset consists of tools collected from
> real-world MCP scenarios, encompassing MCP servers with
> varying tool quantities across diverse settings. All samples
> within this dataset are metadata-poisoned, covering both CFI
> violation and DFI violation attack types. 2) InjecAgent [50]
> and 3) RAS-Eval [51]. These two datasets exclusively con-
> tain CFI violation attacks, originally designed for indirect
> prompt injection. We extracted the malicious payloads from
> these datasets, transforming them into metadata poisoning
> samples based on the principle established in [9]. We then
> evaluate the effectiveness and generalizability of MIND-
> GUARD across multiple LLM agents, including models from
> the Qwen
**Section Heading**: `Results in Fig. 8b demonstrate that attack success (ASR)` [section offsets: 65652:66171]
**First 120 words verbatim** [offsets: 65652:66552]
> Results in Fig. 8b demonstrate that attack success (ASR)
> increases when amplifying malicious attention (αa >0)
> and decreases sharply when suppressing malicious attention
> (αa <0). This strong correlation confirms that effective
> attacks require substantial attention allocation to malicious
> content. An adaptive attacker attempting to minimize total
> attention aggregated from all layers (e.g., TAE) while main-
> taining attack efficacy would therefore face fundamental
> contradictions with attention mechanism principles.
> 
> 7. Discussion
> 
> Representative Failure Analysis. Despite its overall
> high accuracy, MINDGUARD faces challenges in certain
> corner cases: 1) Semantic-Level Parameter Generation
> in DFI Detection. In DFI, we generally assume that pa-
> rameter values are generated through direct string match-
> ing from the attacker’s intent (e.g., read /root/ssh/).
> While this captures the most prevalent

## Block 5: Attack-Set Excerpts
**Location**: `6. Evaluation` [offsets: 46288:46479]
> We evaluate MINDGUARD on various LLM agents us-
> ing diverse applications under both fully adversarial attack
> datasets and realistic settings (normal calls contain no poi-
> soned descriptions).
**Location**: `6.1. Experimental Setup` [offsets: 47967:47989]
> Dataset and LLM Agent.
**Location**: `6.1. Experimental Setup` [offsets: 47990:48089]
> To evaluate the performance
> of MINDGUARD, we curated three distinct attack datasets:
> 1) MCPTox [9].
**Location**: `6.1. Experimental Setup` [offsets: 48090:48240]
> This dataset consists of tools collected from
> real-world MCP scenarios, encompassing MCP servers with
> varying tool quantities across diverse settings.
**Location**: `6.1. Experimental Setup` [offsets: 48241:48355]
> All samples
> within this dataset are metadata-poisoned, covering both CFI
> violation and DFI violation attack types.
**Location**: `6.1. Experimental Setup` [offsets: 48397:48511]
> These two datasets exclusively con-
> tain CFI violation attacks, originally designed for indirect
> prompt injection.

## Block 6: Baseline Excerpts
**Location**: `6.1. Experimental Setup` [offsets: 49509:49518]
> Baseline.
**Location**: `6.1. Experimental Setup` [offsets: 50592:50683]
> Comprehensive implementation details for all baseline meth-
> ods are provided in Appendix A.

## Block 7: Cost Excerpts
**Location**: `6. Evaluation` [offsets: 46823:46941]
> Its security perfor-
> mance outperforms SOTA methods while saving over 1000+
> token overhead for each invocation (§6.3).
**Location**: `6.1. Experimental Setup` [offsets: 51088:51266]
> T otal );
> Average Precision↑(AP), the area under the Precision-
> Recall Curve, which is the primary metric for imbalanced-
> class settings; and AUC ↑, the area under the ROC Curve.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `evasion` | **Location**: `3.2. Attack Model` [offsets: 21853:22231]
> Studies
> confirm this threat’s viability, showing malicious tools are
> readily published and perceived as trustworthy [11], [31],
> [32], with over 75% of users selecting malicious servers
> in one study [11]. Once adopted, attackers can silently
> modify tool metadata without triggering alerts (e.g., Rug
> Pull Attack [11], [12]), ensuring persistent evasion.
> 
> --- PAGE BREAK ---
> 
> 3.3.
**Matched Term**: `white-box` | **Location**: `3.4. Decision Inspection Defense` [offsets: 25044:25664]
> Defender Capabilities. We assume that the defender
> possesses white-box access to the LLM’s inference process,
> 
> allowing visibility into the attention matrices, input con-
> texts, and the final output tool call, without necessitating
> any modification to the model itself. This setup is highly
> suitable for two primary practical scenarios: 1) for model
> service providers (e.g., Anthropic, OpenAI) integrating this
> defense mechanism as a value-added security feature, just
> like cloud providers today offer built-in DDoS protection; 2)
> for enterprises deploying open-source LLMs for enhanced
> internal auditing and protection.
**Matched Term**: `adaptive` | **Location**: `5.3. Decision Integrity Defender` [offsets: 45268:46035]
> It
> operates in a policy-agnostic manner, directly inspecting the
> structural integrity of decision provenance as defined in §4.3.
> To enable a unified decision integrity verification analysis
> across heterogeneous contexts (e.g., varying tool quantities
> and context lengths), we introduce a more robust, context-
> adaptive metric for edges of all uninvoked tools, which we
> term the Decision Integrity Ratio (DIR):
> 
> DIR(u, v) =
> w(u, v)
> w(vq, v) + w(vtc, v), u ∈VT \{vtc}, v ∈Vout,
> 
> (4)
> where vq is the logical vertex for the user query, and vtc
> is the input context vertex corresponding to the invoked
> tool. This metric quantifies the relative influence of untrusted
> data on the final decision compared to legitimate decision
> sources: user query and invoked tool metadata.
**Matched Term**: `adaptive` | **Location**: `2. Due to the context-dependent and model-dependent nature of decision` [offsets: 47793:47946]
> • MINDGUARD demonstrates robust effectiveness with
> respect to involved variables (§6.4) and maintains resilience
> against adaptive attackers (§6.5).
> 
> 6.1.
**Matched Term**: `Adaptive` | **Location**: `Method` [offsets: 63775:63857]
> (b) Attention Minimization
> 
> Figure 8: Adaptive Attack Analysis on Qwen3-8b†.
> 
> 6.5.
**Matched Term**: `Adaptive` | **Location**: `6.5. Adaptive Attack Analysis` [offsets: 63853:64026]
> 6.5. Adaptive Attack Analysis
> 
> Paraphrasing Attack. Attacker replaces key terms in
> malicious payloads with semantic equivalents to evade de-
> tection while preserving intent.
**Matched Term**: `evade` | **Location**: `6.5. Adaptive Attack Analysis` [offsets: 63884:64348]
> Paraphrasing Attack. Attacker replaces key terms in
> malicious payloads with semantic equivalents to evade de-
> tection while preserving intent. We compare three distinct
> paraphrasing strategies: M1: Rule-based paraphrasing us-
> ing predefined synonym dictionaries; M2: Semantic-based
> paraphrasing
> leveraging
> contextual
> word
> embeddings;
> M3: Deletion of imperative instruction removing coercive
> phrases from injection payloads (e.g., !!!IMPORTANT,
> Ignore Previous...).
**Matched Term**: `adaptive` | **Location**: `Results in Fig. 8b demonstrate that attack success (ASR)` [offsets: 65831:66173]
> This strong correlation confirms that effective
> attacks require substantial attention allocation to malicious
> content. An adaptive attacker attempting to minimize total
> attention aggregated from all layers (e.g., TAE) while main-
> taining attack efficacy would therefore face fundamental
> contradictions with attention mechanism principles.
> 
> 7.
**Matched Term**: `adaptive` | **Location**: `B. Detailed Evaluation Results` [offsets: 84167:84414]
> Context-adaptive Performance of DIR. As previously
> discussed, directly employing two fixed anomaly thresh-
> olds for integrity violation detection proves unstable across
> varying contextual environments, particularly with differing
> numbers of tools.
**Matched Term**: `adaptive` | **Location**: `1. E. Implementation Details for Baselines` [offsets: 89807:89924]
> (b) Attributing Performance
> 
> Figure 11: Context-adaptive(number of tools) Performance.
> 
> invoke MCIP Guardian’s tools.
