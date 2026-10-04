# Evidence Locator Packet: ping-2026-hybrid-analysis-secure-mcp-tool

- **Title**: Hybrid Analysis for Secure MCP Tool Use in LLM Agents
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2607.25297
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\ping-2026-hybrid-analysis-secure-mcp-tool\fulltext.txt
- **Character Count**: 72915

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 858:1066]
> To address these limi-
> tations, we propose MTGuard, a hybrid analysis-based defense
> framework designed to safeguard the use of MCP tools in LLM
> agents by leveraging lifecycle-aware static-dynamic co-analysis.
**Location**: `Introduction` [offsets: 4989:5751]
> we propose a hybrid analysis-based defense
> framework that serves as an MCP tool usage guard for LLM agents,
> termed MTGuard. At a high level, MTGuard is deployed as a sepa-
> rate guard agent that protects the target LLM agent throughout the
> MCP tool invocation process. Instead of treating a tool invocation
> as a static message or treating runtime monitoring as a standalone
> sandboxing mechanism, MTGuard couples both views throughout
> the tool use lifecycle. The static view provides the semantic context
> needed to understand what the tool is supposed to do, whereas
> the dynamic view provides execution evidence about what the tool
> actually does. This combination enables MTGuard to detect attacks
> that are invisible to either view alone, especially tool execution

## Block 3: Method Locator
**Section Heading**: `Methodology` [section offsets: 16614:27355]
**First 120 words verbatim** [offsets: 16614:17424]
> Methodology
> 3.1
> Design overview
> 
> At a high level, MTGuard is a hybrid analysis-based defense frame-
> work that safeguards MCP tool usage by LLM agents through the
> joint analysis of static context and dynamic execution behavior. In
> deployment, MTGuard operates as an external guard agent that in-
> tercepts the MCP tool invocation pipeline of a target LLM agent. As
> illustrated in Figure 1, the framework consists of three components:
> a pre-execution parameter auditor, an in-execution behavioral mon-
> itor, and a post-execution result verifier. The detailed algorithmic
> description of MTGuard can be found in Appendix A.
> 
> 3.2
> Pre-execution parameter auditor
> 
> The pre-execution parameter auditor identifies unsafe or policy-
> violating MCP tool invocations before they are dispatched to the
> tool executor. For each
**Section Heading**: `Implementation details. MTGuard is a hybrid analysis-based` [section offsets: 27391:31679]
**First 120 words verbatim** [offsets: 27391:28197]
> Implementation details. MTGuard is a hybrid analysis-based
> defense framework consisting of three components for securing
> MCP tool usage. We implement a prototype of MTGuard primar-
> ily in Python, with the eBPF tracing programs implemented in C.
> Specifically, we build the main pipeline on top of AgentScope [10].
> For controlled MCP tool execution, we use Docker as an isolated
> sandbox environment, and we employ eBPF [8] to capture the run-
> time behavior of each tool. For text-level policy auditing, MTGuard
> consistently uses DeepSeek-V4-Pro as the backend LLM across all
> experimental settings.
> LLM agents and benchmark tasks. We derive our evaluation
> from two representative domains in MCP-SafetyBench [42]: browser
> automation and financial analysis. For each domain, we implement
> a ReAct-style LLM agent

## Block 4: Evaluation Locator
**Section Heading**: `Experimental results show that MTGuard consistently improves` [section offsets: 8406:10393]
**First 120 words verbatim** [offsets: 8406:9222]
> Experimental results show that MTGuard consistently improves
> the security of MCP tool use in real-world LLM agent applications.
> Compared with existing baselines [7], MTGuard achieves stronger
> defense performance while incurring low runtime overhead. Across
> the evaluated settings, MTGuard detects an average of 48.3% of
> unsafe MCP tool calls, compared with 8.3% for the evaluated base-
> line methods. In the meantime, MTGuard maintains an average
> false positive rate of 3.7%, indicating limited disruption to benign
> tool use and the normal functionality of the target LLM agents. In
> addition, MTGuard introduces only a modest runtime overhead,
> with an average additional latency of about 10 seconds in total
> across the evaluated settings. Our ablation study further demon-
> strates the importance of combining multiple
**Section Heading**: `Experiments` [section offsets: 27355:27391]
**First 120 words verbatim** [offsets: 27355:28173]
> Experiments
> 4.1
> Experimental setup
> 
> Implementation details. MTGuard is a hybrid analysis-based
> defense framework consisting of three components for securing
> MCP tool usage. We implement a prototype of MTGuard primar-
> ily in Python, with the eBPF tracing programs implemented in C.
> Specifically, we build the main pipeline on top of AgentScope [10].
> For controlled MCP tool execution, we use Docker as an isolated
> sandbox environment, and we employ eBPF [8] to capture the run-
> time behavior of each tool. For text-level policy auditing, MTGuard
> consistently uses DeepSeek-V4-Pro as the backend LLM across all
> experimental settings.
> LLM agents and benchmark tasks. We derive our evaluation
> from two representative domains in MCP-SafetyBench [42]: browser
> automation and financial analysis. For each domain, we implement
**Section Heading**: `evaluation suite therefore contains 62 server-side, 26 host-side, and` [section offsets: 31679:46641]
**First 120 words verbatim** [offsets: 31679:32527]
> evaluation suite therefore contains 62 server-side, 26 host-side, and
> 11 user-side cases, for a total of 99 cases spanning 18 fine-grained
> attack categories.
> Baseline methods. We compare MTGuard with two runtime
> defense components provided by Agent-Aegis [7]: Tool Call Gover-
> nance (TCG) and Tool Result Inspection (TRI). Because the released
> Agent-Aegis implementation is written in TypeScript, we imple-
> ment MCP-compatible Python adaptations of the two components
> in our evaluation framework.
> 
> --- PAGE BREAK ---
> 
> KDD’27, August 2027, San Jose, CA, USA
> Ping He, Yuexiang Xie, Yaliang Li, and Shouling Ji
> 
> Table 1: The defense performance of MTGuard and baseline methods against different attack methods on mainstream LLM-based
> agents, measured by DR. DS-V4-Flash denotes DeepSeek-V4-Flash and DS-V4-Pro denotes DeepSeek-V4-Pro.
> 
> Attacks
> Defense

## Block 5: Attack-Set Excerpts
**Location**: `evaluation suite therefore contains 62 server-side, 26 host-side, and` [offsets: 34489:34595]
> Individual tool calls are labeled using the attack-specific evaluator
> associated with each benchmark case.

## Block 6: Baseline Excerpts
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 8534:8655]
> Compared with existing baselines [7], MTGuard achieves stronger
> defense performance while incurring low runtime overhead.
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 8656:8805]
> Across
> the evaluated settings, MTGuard detects an average of 48.3% of
> unsafe MCP tool calls, compared with 8.3% for the evaluated base-
> line methods.
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 9144:9435]
> Our ablation study further demon-
> strates the importance of combining multiple analysis stages: the
> pre-execution-only variant cannot detect attacks whose malicious
> behavior emerges only during host-side execution, whereas the
> complete MTGuard consistently provides the strongest protection.
**Location**: `evaluation suite therefore contains 62 server-side, 26 host-side, and` [offsets: 31837:31854]
> Baseline methods.
**Location**: `evaluation suite therefore contains 62 server-side, 26 host-side, and` [offsets: 32288:32433]
> Table 1: The defense performance of MTGuard and baseline methods against different attack methods on mainstream LLM-based
> agents, measured by DR.
**Location**: `evaluation suite therefore contains 62 server-side, 26 host-side, and` [offsets: 34227:34353]
> For a fair comparison, both baselines are re-
> played over the same tool-call records collected from the executions
> of MTGuard.

## Block 7: Cost Excerpts
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 8534:8655]
> Compared with existing baselines [7], MTGuard achieves stronger
> defense performance while incurring low runtime overhead.
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 8806:8984]
> In the meantime, MTGuard maintains an average
> false positive rate of 3.7%, indicating limited disruption to benign
> tool use and the normal functionality of the target LLM agents.
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 8985:9143]
> In
> addition, MTGuard introduces only a modest runtime overhead,
> with an average additional latency of about 10 seconds in total
> across the evaluated settings.
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 9501:9715]
> • We identify a runtime observability blind spot in existing
> MCP tool-use defenses and propose MTGuard, a hybrid
> defense framework that combines protocol-level contextual
> inspection with dynamic execution analysis.
**Location**: `Experimental results show that MTGuard consistently improves` [offsets: 10223:10389]
> The results show that MT-
> Guard substantially improves the detection of unsafe tool
> calls while maintaining a low false-positive rate and moder-
> ate runtime overhead.
**Location**: `evaluation suite therefore contains 62 server-side, 26 host-side, and` [offsets: 31855:32001]
> We compare MTGuard with two runtime
> defense components provided by Agent-Aegis [7]: Tool Call Gover-
> nance (TCG) and Tool Result Inspection (TRI).

## Block 8: Limitations
**Section Heading**: `Limitations & Future work` [section offsets: 46656:49365]
**First 120 words verbatim** [offsets: 46656:47569]
> Limitations & Future work
> 
> Generality. MTGuard uses MCP as its reference interface be-
> cause MCP standardizes tool schemas, invocation arguments, and
> response messages. Conceptually, the framework may be adapted to
> other tool-use interfaces, including function-calling APIs, LangChain
> tools, local functions, shell commands, and REST API wrappers.
> Such an adaptation would map tool metadata, arguments, execu-
> tion boundaries, and returned values to the corresponding inputs
> of MTGuard. However, this extension requires a well-defined in-
> terception boundary and sufficient control over the tool execution
> environment. Tools executed remotely or on platforms without
> compatible sandboxing and system-level tracing may require ad-
> ditional provider-side instrumentation. Therefore, although the
> 
> DS-V4-Flash
> DS-V4-Pro
> GPT-5.6 Luna
> DS-V4-Flash
> DS-V4-Pro
> GPT-5.6 Luna
> 
> design is not inherently restricted to MCP, our

## Block 9: Adaptivity Hits
**Matched Term**: `Adaptive` | **Location**: `References` [offsets: 57862:58040]
> 2025. AGrail: A Lifelong Agent Guardrail with Effective
> and Adaptive Safety Detection. In ACL, Wanxiang Che, Joyce Nabende, Ekaterina
> Shutova, and Mohammad Taher Pilehvar (Eds.).
