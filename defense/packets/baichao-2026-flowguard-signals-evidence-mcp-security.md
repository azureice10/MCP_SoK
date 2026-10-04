# Evidence Locator Packet: baichao-2026-flowguard-signals-evidence-mcp-security

- **Title**: FlowGuard: From Signals to Evidence for MCP Security Detection
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2607.14754
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\baichao-2026-flowguard-signals-evidence-mcp-security\fulltext.txt
- **Character Count**: 107329

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) enables LLM` [offsets: 746:819]
> We present FlowGuard, an evidence-grounded MCP security
> detection system.
**Location**: `Abstract—The Model Context Protocol (MCP) enables LLM` [offsets: 1105:1218]
> We
> evaluate FlowGuard on an executable benchmark containing
> 1,880 MCP cases across five vulnerability categories.

## Block 3: Method Locator
**Section Heading**: `III. METHODOLOGY` [section offsets: 16468:16486]
**First 120 words verbatim** [offsets: 16468:17302]
> III. METHODOLOGY
> 
> A. Challenges and Key Ideas
> 
> Challenge 1: Probes must be both schema-valid and
> attack-effective, but these two goals conflict without backend
> visibility. A useful security probe must satisfy two conflicting
> requirements. It must conform to the tool’s type and format
> constraints, otherwise it will be rejected before reaching the
> backend. At the same time, it must carry a payload capable
> of triggering vulnerability behavior. Without knowledge of
> the backend implementation, constructing such probes is non-
> trivial. We decouple probing into two phases: a reconnaissance
> phase that extracts backend signals using low-impact, schema-
> compliant inputs, followed by a targeted phase that generates
> exploit-oriented probes guided by the inferred backend con-
> text.
> 
> Challenge 2: Parameters with similar schemas can have
**Section Heading**: `B. Category-Specific Design` [section offsets: 40392:45158]
**First 120 words verbatim** [offsets: 40392:41274]
> B. Category-Specific Design
> 
> We construct each category according to where the risk
> appears in the three stages analyzed by FlowGuard. Execution-
> path vulnerabilities model unsafe flows from Tool Invocation
> parameters to backend operations, while semantic risks appear
> 
> --- PAGE BREAK ---
> 
> in Tool Discovery metadata or Response Consumption content.
> Each category includes positive cases and negative or hard-
> negative cases with similar surface semantics.
> 
> Command Injection. Command injection occurs when
> user-controlled input is interpreted as part of an operating-
> system command, allowing an attacker to alter the intended
> command semantics or execute unintended commands. Fol-
> lowing CWE-78 [15], we generate MCP tools whose param-
> eters flow into command-execution patterns. Positive cases
> cover direct shell construction, string concatenation, f-string
> command construction,
**Section Heading**: `Method` [section offsets: 46966:48067]
**First 120 words verbatim** [offsets: 46966:47889]
> Method
> TP
> FP
> TN
> FN
> Error
> Precision
> Recall
> F1
> Accuracy
> 
> DENOMINATORS.
> 
> Credential Leakage
> 
> Tool Poisoning
> 
> Command Injection
> 
> Prompt Injection
> 
> File System Access
> 
> evidence collection mechanisms, whereas Tool Poisoning and
> Prompt Injection are primarily metadata- or response-semantic
> threats. For real-world evaluation, we interact with MCPZoo
> servers through MCPZoo’s provided access interface.
> 
> Baselines. We compare FlowGuard with three representa-
> tive MCP security scanners covering different analysis mech-
> anisms. For static source-code analysis, we use MCPScan,
> which analyzes MCP server implementations to identify po-
> tentially risky behaviors. For metadata-based analysis, we use
> MCP-Scanner, which inspects tool descriptions and related
> metadata for suspicious patterns. For dynamic interaction
> analysis, we use A.I.G (AI Infra Guard), which performs
> runtime probing by generating tool invocations and analyzing
**Section Heading**: `Implementation` [section offsets: 48067:48171]
**First 120 words verbatim** [offsets: 48067:48909]
> Implementation
> and
> Configuration. FlowGuard uses
> Qwen3-235B-A22B-Instruct as the default LLM across all
> experiments. Unless otherwise specified, the timeout for each
> scanning run is set to 900 seconds, and the maximum prob-
> ing budget B is limited to 5 rounds. The probing process
> terminates earlier once sufficient evidence is collected or no
> additional useful signal is observed. For fair comparison, all
> baseline scanners use their default or recommended configu-
> rations under the same LLM and overall timeout constraint.
> 
> Metrics. We evaluate performance using multiple metrics,
> including detection accuracy (Precision, Recall, and F1 score),
> false positive rate, probe validity, average number of probing
> rounds, and overall runtime cost. For real-world MCP servers,
> we additionally perform manual verification of selected find-
> ings to

## Block 4: Evaluation Locator
**Section Heading**: `results. Before Tool Invocation, the agent obtains tool names,` [section offsets: 27782:32880]
**First 120 words verbatim** [offsets: 27782:28701]
> results. Before Tool Invocation, the agent obtains tool names,
> descriptions, and JSON schemas during Tool Discovery, and
> this metadata may directly affect tool selection and argument
> construction. We therefore separate signal identification into
> two categories: metadata-layer signals from Tool Discovery,
> and execution-layer signals from Tool Invocation and Re-
> sponse Consumption.
> 
> Description-Layer Detection. Tool Discovery metadata is
> itself an attack surface. A malicious MCP server can embed
> hidden instructions in tool descriptions or schemas, influencing
> the agent before Tool Invocation. To balance efficiency and
> coverage, we use a three-tier pipeline. First, name-confusion
> detection normalizes tool names by lowercasing, removing
> non-alphanumeric characters, and applying common leet sub-
> stitutions, then compares them against high-risk authoritative
> tool names. Second, fast rule matching applies regular
**Section Heading**: `V. EVALUATION` [section offsets: 45158:46193]
**First 120 words verbatim** [offsets: 45158:46004]
> V. EVALUATION
> 
> We evaluate FlowGuard through the following five research
> questions:
> 
> • RQ1 (Detection Effectiveness): How accurate is Flow-
> Guard in detecting different types of MCP vulnerabilities,
> and can it maintain high coverage while effectively con-
> trolling false positives?
> 
> • RQ2
> (Probe
> Quality
> and
> Efficiency):
> Can
> the
> constraint-aware
> probe
> generation
> strategy
> produce
> schema-compliant inputs while improving probe success
> rate and overall detection efficiency?
> 
> • RQ3 (Runtime Overhead): What is the runtime over-
> head of FlowGuard, and does its time and interaction cost
> meet the requirements of practical deployment?
> 
> • RQ4 (Mechanism Contribution): What are the contribu-
> tions of key components, including semantic risk triage,
> the Recon and Strike probing strategy, and response anal-
> ysis with attribution, to the overall system
**Section Heading**: `A. Experiment Setup` [section offsets: 46193:46214]
**First 120 words verbatim** [offsets: 46193:47070]
> A. Experiment Setup
> 
> Evaluation Targets. We deploy FlowGuard as an active se-
> curity scanner that interacts with target servers strictly through
> the standard MCP protocol. For benchmark evaluation, each
> case is executed as an independent MCP server instance with
> its ground-truth trigger and label hidden from the scanner. RQ1
> reports end-to-end detection results over all five benchmark
> categories. Subsequent mechanism-oriented analyses focus on
> Command Injection, Credential Leakage, and File System
> Access, because they directly exercise FlowGuard’s active
> parameter-level probing, refinement, runtime overhead, and
> 
> --- PAGE BREAK ---
> 
> TABLE II
> DETECTION EFFECTIVENESS ACROSS FIVE MCP VULNERABILITY CATEGORIES. ERROR DENOTES FAILED RUNS AND IS EXCLUDED FROM
> 
> Category
> Method
> TP
> FP
> TN
> FN
> Error
> Precision
> Recall
> F1
> Accuracy
> 
> DENOMINATORS.
> 
> Credential Leakage
> 
> Tool Poisoning
**Section Heading**: `Evaluation Targets. We deploy FlowGuard as an active se-` [section offsets: 46214:46966]
**First 120 words verbatim** [offsets: 46214:47097]
> Evaluation Targets. We deploy FlowGuard as an active se-
> curity scanner that interacts with target servers strictly through
> the standard MCP protocol. For benchmark evaluation, each
> case is executed as an independent MCP server instance with
> its ground-truth trigger and label hidden from the scanner. RQ1
> reports end-to-end detection results over all five benchmark
> categories. Subsequent mechanism-oriented analyses focus on
> Command Injection, Credential Leakage, and File System
> Access, because they directly exercise FlowGuard’s active
> parameter-level probing, refinement, runtime overhead, and
> 
> --- PAGE BREAK ---
> 
> TABLE II
> DETECTION EFFECTIVENESS ACROSS FIVE MCP VULNERABILITY CATEGORIES. ERROR DENOTES FAILED RUNS AND IS EXCLUDED FROM
> 
> Category
> Method
> TP
> FP
> TN
> FN
> Error
> Precision
> Recall
> F1
> Accuracy
> 
> DENOMINATORS.
> 
> Credential Leakage
> 
> Tool Poisoning
> 
> Command Injection
> 
> Prompt

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation Targets. We deploy FlowGuard as an active se-` [offsets: 46365:46515]
> For benchmark evaluation, each
> case is executed as an independent MCP server instance with
> its ground-truth trigger and label hidden from the scanner.
**Location**: `Evaluation Targets. We deploy FlowGuard as an active se-` [offsets: 46516:46592]
> RQ1
> reports end-to-end detection results over all five benchmark
> categories.

## Block 6: Baseline Excerpts
**Location**: `experiments. Unless otherwise specified, the timeout for each` [offsets: 48449:48592]
> For fair comparison, all
> baseline scanners use their default or recommended configu-
> rations under the same LLM and overall timeout constraint.

## Block 7: Cost Excerpts
**Location**: `results. Before Tool Invocation, the agent obtains tool names,` [offsets: 32272:32399]
> For execution-related risks, the system
> classifies a signal as input reflection, normal defense, or
> confirmed runtime evidence.
**Location**: `V. EVALUATION` [offsets: 45243:45439]
> • RQ1 (Detection Effectiveness): How accurate is Flow-
> Guard in detecting different types of MCP vulnerabilities,
> and can it maintain high coverage while effectively con-
> trolling false positives?
**Location**: `V. EVALUATION` [offsets: 45632:45788]
> • RQ3 (Runtime Overhead): What is the runtime over-
> head of FlowGuard, and does its time and interaction cost
> meet the requirements of practical deployment?
**Location**: `V. EVALUATION` [offsets: 46019:46191]
> • RQ5 (Real-World Effectiveness): When applied to real-
> world MCP servers, what risks does FlowGuard report,
> and how many sampled reports contain concrete runtime
> evidence?
**Location**: `Evaluation Targets. We deploy FlowGuard as an active se-` [offsets: 46593:46908]
> Subsequent mechanism-oriented analyses focus on
> Command Injection, Credential Leakage, and File System
> Access, because they directly exercise FlowGuard’s active
> parameter-level probing, refinement, runtime overhead, and
> 
> --- PAGE BREAK ---
> 
> TABLE II
> DETECTION EFFECTIVENESS ACROSS FIVE MCP VULNERABILITY CATEGORIES.
**Location**: `experiments. Unless otherwise specified, the timeout for each` [offsets: 48184:48327]
> Unless otherwise specified, the timeout for each
> scanning run is set to 900 seconds, and the maximum prob-
> ing budget B is limited to 5 rounds.

## Block 8: Limitations
**Section Heading**: `B. Limitations` [section offsets: 69414:70679]
**First 120 words verbatim** [offsets: 69414:70339]
> B. Limitations
> 
> FlowGuard has several limitations. First, as a black-box
> scanner, it cannot directly observe internal control flow or
> hidden backend logic, and may therefore miss vulnerabili-
> ties that depend on specific application states, authentication
> contexts, or complex multi-step interactions. Second, active
> probing introduces an inherent trade-off between coverage and
> operational safety. Although FlowGuard uses low-side-effect
> 
> probes, testing tools that interact with real files, databases,
> networks, or external services may still trigger unintended be-
> haviors. Third, FlowGuard’s semantic triage, probe generation,
> and response attribution depend partly on the capabilities of
> the underlying LLM. Future advances in language models may
> further improve FlowGuard’s performance. Finally, the current
> prototype focuses on non-adaptive, runtime-visible evidence
> from standard MCP interactions. It does not address

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `C. Threat Model` [offsets: 14887:15385]
> Our analysis treats server-provided metadata, execu-
> tion behavior, and returned content as untrusted observations
> during Tool Discovery, Tool Invocation, and Response Con-
> sumption. During a scan, we assume the server does not try
> to recognize FlowGuard, hide evidence only from the scanner,
> or change behavior only to evade probing. Servers that adapt
> to the scanner, delay malicious behavior across sessions, or
> behave differently for benign-looking clients are outside our
> current threat model.
**Matched Term**: `white-box` | **Location**: `C. Threat Model` [offsets: 16043:16472]
> We do not consider
> scenarios in which the host application, embedded MCP client,
> or FlowGuard execution environment is already compromised.
> We also exclude vulnerabilities that require white-box code
> analysis, local system privileges, adaptive probe evasion, long-
> term cross-session behavior, or attacks that bypass MCP
> tool interaction entirely, such as standalone social-engineering
> attacks unrelated to tool invocation.
> 
> III.
**Matched Term**: `adaptive` | **Location**: `B. Limitations` [offsets: 70127:70554]
> Future advances in language models may
> further improve FlowGuard’s performance. Finally, the current
> prototype focuses on non-adaptive, runtime-visible evidence
> from standard MCP interactions. It does not address servers
> that recognize the scanner and hide evidence, long-term or
> cross-session behavior, ecosystem-level supply-chain risks, or
> client-policy attacks that do not produce observable evidence
> within a bounded scan.
**Matched Term**: `adaptive` | **Location**: `C. J. Maddison, and T. Hashimoto, “Identifying the risks of LM` [offsets: 86583:86721]
> Wang, and Q. Wen, “MCPShield: A security cognition
> layer for adaptive trust calibration in model context protocol agents,”
> 2026. [Online].
