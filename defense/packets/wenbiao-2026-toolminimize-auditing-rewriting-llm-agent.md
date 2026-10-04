# Evidence Locator Packet: wenbiao-2026-toolminimize-auditing-rewriting-llm-agent

- **Title**: ToolMinimize: Auditing and Rewriting LLM Agent Tool Calls to Minimize Privacy Exposure
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2608.24957
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\wenbiao-2026-toolminimize-auditing-rewriting-llm-agent\fulltext.txt
- **Character Count**: 56385

## Block 2: Contribution Sentences
**Location**: `Abstract—LLM agents routinely include privacy-sensitive data` [offsets: 877:1145]
> We present
> TOOLMINIMIZE, a middleware that intercepts tool calls and
> rewrites their arguments to the minimum data necessary for tool
> functionality, combining schema-aware necessity analysis with
> four operations: removal, generalization, substitution, and trun-
> cation.
**Location**: `I. INTRODUCTION` [offsets: 5400:6191]
> We present TOOLMINIMIZE, a mid-
> dleware that intercepts LLM agent tool calls before execution,
> classifies PSD in their arguments, computes a quantitative
> privacy cost, and rewrites arguments to the minimum nec-
> essary data. It sits between the agent and the tool without
> changes to the LLM, framework, or tools. Over-sharing is an
> inference-time phenomenon: the helpfulness objective pushes
> the LLM to include all context in tool arguments regardless of
> safety training, and our motivating study confirms that privacy
> prompts still leave 36–76% of calls leaking PSD. Intervention
> therefore must act on the LLM’s output.
> 
> This paper contributes:
> 1) A practical taxonomy of 10 PSD categories grounded in
> GDPR Art. 9 classifications, and a quantitative privacy cost
> metric PC(t, args) combining

## Block 3: Method Locator
**Section Heading**: `IV. SYSTEM DESIGN` [section offsets: 16009:16028]
**First 120 words verbatim** [offsets: 16009:16814]
> IV. SYSTEM DESIGN
> 
> A. Pipeline Overview
> 
> TOOLMINIMIZE intercepts tool calls after LLM generation
> and before execution. When an agent emits a call with name
> t and arguments args, the middleware passes it through four
> stages (Figure 2): Classify (identify PSD items and categorize
> 
> --- PAGE BREAK ---
> 
> Agent
> (t, args)
> Classify
> Score
> Analyze
> Rewrite
> Tool
> (t, args′)
> 
> Pattern+Entity
> 
> PC(t, args)
> Schema+
> Necessity
> 
> Remove/Gen./
> 
> +Semantic
> 
> Sub./Trunc.
> Tool Schema
> 
> Fig. 2.
> TOOLMINIMIZE pipeline. Tool calls are intercepted after LLM
> generation and before execution.
> 
> TABLE II
> PSD TAXONOMY: 10 CATEGORIES WITH CODES, SENSITIVITY LEVELS,
> 
> AND EXAMPLES.
> 
> Code Category
> S
> GDPR
> Examples
> 
> DI
> Direct identifiers
> 4
> Art. 4(1)
> SSN,
> email,
> phone,
> name
> H
> Health
> 4
> Art. 9(1)
> Conditions, medications
> F
> Financial
> 4
> Art. 4(1)
**Section Heading**: `E. Framework Integration` [section offsets: 22693:23207]
**First 120 words verbatim** [offsets: 22693:23628]
> E. Framework Integration
> 
> TOOLMINIMIZE
> integrates
> with
> three
> major
> agent
> frameworks
> through
> thin
> adapter
> layers
> sharing
> a
> common
> ToolMinimizeMiddleware
> core.
> AutoGenToolMinimize wraps registered tool functions
> via a decorator or agent-level patch; MCPToolMinimize
> intercepts tools/call JSON-RPC requests at the MCP
> client
> transport;
> LangChainToolMinimize
> wraps
> BaseTool instances in a proxy. All adapters share the same
> pipeline; our evaluation confirms identical privacy results
> across frameworks (Section V-D).
> 
> V. EVALUATION
> 
> We evaluate TOOLMINIMIZE on a benchmark of 90 re-
> alistic agent scenarios addressing three research questions.
> RQ1: How pervasive is PSD over-sharing? RQ2: How does
> TOOLMINIMIZE compare with existing mitigations? RQ3:
> What is the contribution of each pipeline component?
> 
> A. Experimental Setup
> 
> a) Benchmark.:
> AgentPrivBench
> contains
> 90
> hand-
> curated multi-step scenarios covering healthcare (23), personal
**Section Heading**: `Method` [section offsets: 27759:29915]
**First 120 words verbatim** [offsets: 27759:28528]
> Method
> PER↓
> PCS↓
> TCR↑DMS↑
> Red.↑
> 
> No Mitigation
> 1.000
> 11.68
> 1.00
> 0.0%
> 0.0%
> Prompt (instr.)
> 0.99±.01 9.27±.62
> 1.00
> 20.8% 17.2%
> Prompt (few-shot) 0.98±.01 7.29±.64
> 1.00
> 35.7% 29.8%
> Prompt (system)
> 0.97±.02 6.71±.61
> 1.00
> 40.4% 33.2%
> PII Detection
> 0.717
> 4.29
> 1.00
> 46.1% 27.6%
> PrivacyChecker
> 0.050
> 0.47
> 0.03
> 95.0% 73.2%
> PrivChk-relaxed
> 0.370
> 3.97
> 0.37
> 63.0% 63.9%
> AudAgent (detect)
> 1.000
> 11.68
> 1.00
> 0.0%
> 0.0%
> 
> ToolMinimize
> 0.567
> 0.59
> 1.00 62.3% 73.6%
> 
> achieves PCS = 0.47 at catastrophic utility loss (TCR = 3%);
> relaxing to block only on H + F raises TCR to 37% but PCS
> to 3.97. AudAgent’s blocking mode (our re-implementation)
> acts post-hoc on detected items but does not rewrite argument
> fields.
> 
> TOOLMINIMIZE achieves PCS = 0.59, close to Privacy-
> Checker’s 0.47 but with

## Block 4: Evaluation Locator
**Section Heading**: `V. EVALUATION` [section offsets: 23207:23494]
**First 120 words verbatim** [offsets: 23207:24059]
> V. EVALUATION
> 
> We evaluate TOOLMINIMIZE on a benchmark of 90 re-
> alistic agent scenarios addressing three research questions.
> RQ1: How pervasive is PSD over-sharing? RQ2: How does
> TOOLMINIMIZE compare with existing mitigations? RQ3:
> What is the contribution of each pipeline component?
> 
> A. Experimental Setup
> 
> a) Benchmark.:
> AgentPrivBench
> contains
> 90
> hand-
> curated multi-step scenarios covering healthcare (23), personal
> (19), finance (18), workplace (14), travel (12), and legal (4).
> Each scenario specifies a user request, tool calls, and ground-
> truth annotations of necessary vs. unnecessary PSD. Scenarios
> partition into tool_call (Stage C, 60 scenarios, 73 tool calls),
> cross_agent (Stage E, 15), and reasoning (Stage R, 15).
> Annotations follow a written rubric (GDPR Art. 9 tiers, per-
> tool minimum-necessary analysis). We addressed annotation-
**Section Heading**: `A. Experimental Setup` [section offsets: 23494:26223]
**First 120 words verbatim** [offsets: 23494:24334]
> A. Experimental Setup
> 
> a) Benchmark.:
> AgentPrivBench
> contains
> 90
> hand-
> curated multi-step scenarios covering healthcare (23), personal
> (19), finance (18), workplace (14), travel (12), and legal (4).
> Each scenario specifies a user request, tool calls, and ground-
> truth annotations of necessary vs. unnecessary PSD. Scenarios
> partition into tool_call (Stage C, 60 scenarios, 73 tool calls),
> cross_agent (Stage E, 15), and reasoning (Stage R, 15).
> Annotations follow a written rubric (GDPR Art. 9 tiers, per-
> tool minimum-necessary analysis). We addressed annotation-
> circularity concerns with two independent checks. (i) GPT-4o
> and Claude independently annotated 35 calls; both detect more
> PSD than our labels (5.3/7.6 vs. 3.4 items) at high correla-
> tion (ρ=0.63, 0.79; p<0.001), i.e., our labels are conservative
> rather than inflated. (ii)

## Block 5: Attack-Set Excerpts
**Location**: `V. EVALUATION` [offsets: 23222:23332]
> We evaluate TOOLMINIMIZE on a benchmark of 90 re-
> alistic agent scenarios addressing three research questions.
**Location**: `A. Experimental Setup` [offsets: 23517:23692]
> a) Benchmark.:
> AgentPrivBench
> contains
> 90
> hand-
> curated multi-step scenarios covering healthcare (23), personal
> (19), finance (18), workplace (14), travel (12), and legal (4).

## Block 6: Baseline Excerpts
**Location**: `A. Experimental Setup` [offsets: 24921:25508]
> c) Baselines.:
> Nine
> methods:
> No
> Mitigation;
> three
> Prompt strategies (instruction p=0.20, few-shot p=0.35, sys-
> tem p=0.40, calibrated from [22], [23]); PII Detection
> (Presidio-style regex + named-entity recognition (NER)); Pri-
> vacyChecker [4] (contextual-integrity (CI) gating that blocks
> any call carrying critical PSD to third-party tools; since 97%
> of scenarios contain critical PSD, TCR = 3% by design);
> PrivacyChecker-relaxed (blocks only on H + F, not DI;
> TCR = 37%); AudAgent [3] (re-implementation of its blocking
> mode); and TOOLMINIMIZE (rule-based backends, no LLM
> inference).

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
**Section Heading**: `D. Limitations, Error Analysis, and Future Work` [section offsets: 42178:43422]
**First 120 words verbatim** [offsets: 42178:43019]
> D. Limitations, Error Analysis, and Future Work
> 
> a) Limitations.: Simulated vs. live: live validation on
> 307 tool calls shows no significant difference (Mann-Whitney
> p=0.085; TOST p<0.001 at ∆=1.0, not at ∆=0.25). TCR
> scope: schema-validity, not end-to-end (80%; 4/20 maps fail-
> ures from missing annotations; external TCR drops to 60%).
> Ecological validity: the 99.7% baseline PER reflects a privacy-
> critical corpus; general use is lower. User agency: TOOLMIN-
> IMIZE decides unilaterally; classifier targets US formats; gen-
> eralization may signal concealment. Defense: 1/10 encodings
> (field splitting) still evades; 10 categories cover GDPR Art. 9
> but not all special categories. False positives: on benign inputs
> detection fires on 20% and rewriting on 10% (Section V-D)—
> an over-cautious bias, mitigated by fail-prompt confirmation,
> the

## Block 9: Adaptivity Hits
**Matched Term**: `Adaptive` | **Location**: `D. Limitations, Error Analysis, and Future Work` [offsets: 43211:43426]
> b) Future work.: Adaptive NER backend for latency;
> session-level budgets [16]; CaMeL integration for joint
> confidentiality–integrity [8]; user-controlled minimization with
> preview UI; multimodal PSD detection.
> 
> VII.
