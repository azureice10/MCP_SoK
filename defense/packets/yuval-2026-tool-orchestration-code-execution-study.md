# Evidence Locator Packet: yuval-2026-tool-orchestration-code-execution-study

- **Title**: From Tool Orchestration to Code Execution: A Study of MCP Design Choices
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_secondary
- **Link**: https://arxiv.org/abs/2602.15945
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\yuval-2026-tool-orchestration-code-execution-study\fulltext.txt
- **Character Count**: 75051

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 116:1013]
> Abstract
> Model Context Protocols (MCPs) provide a unified plat-
> form for agent systems to discover, select, and orchestrate
> tools across heterogeneous execution environments. As MCP-
> based systems scale to incorporate larger tool catalogs and
> multiple concurrently connected MCP servers, traditional tool-
> by-tool invocation increases coordination overhead, fragments
> state management, and limits support for wide-context oper-
> ations. To address these scalability challenges, recent MCP
> designs have incorporated code execution as a first-class ca-
> pability, an approach called Code Execution MCP (CE-MCP).
> This enables agents to consolidate complex workflows, such
> as SQL querying, file analysis, and multi-step data transforma-
> tions, into a single program that executes within an isolated
> runtime environment.
> 
> In this work, we formalize the architectural distinction be-
> tween context-coupled

## Block 3: Method Locator
**Section Heading**: `architecture are therefore improved scalability and reduced` [section offsets: 10189:11420]
**First 120 words verbatim** [offsets: 10189:11025]
> architecture are therefore improved scalability and reduced
> LLM inference costs, since fewer tokens are processed per
> interaction.
> 
> 2.3
> Indirect Prompt Injection
> 
> Indirect prompt injection is an attack in which malicious in-
> structions, which are embedded within external data sources
> (e.g., documents, web pages, tool outputs, and retrieved text),
> are later ingested by an LLM as part of its context [40]. Unlike
> direct prompt injection, the attacker does not interact with the
> model directly; instead, the attack is triggered implicitly when
> the model processes untrusted content during retrieval, tool
> execution, or context augmentation [9,38]. In MCP settings,
> indirect prompt injection is particularly dangerous because
> the MCP explicitly integrates external tools, sources, and arti-
> facts into the model’s context [11]. Since MCP
**Section Heading**: `architecture where agents generate execution programs that` [section offsets: 14982:31558]
**First 120 words verbatim** [offsets: 14982:15883]
> architecture where agents generate execution programs that
> invoke tools within separate environments. CodeMem [8]
> extends this with procedural memory, caching verified code
> patterns.
> 
> The transition from declarative to code-based tool orches-
> tration introduces new attack vectors: (1) generated programs
> can be vulnerable to string manipulation, control flow, and
> 
> --- PAGE BREAK ---
> 
> dynamic evaluation unavailable in schema-constrained declar-
> ative calls; (2) tool outputs are sent directly into executable
> code paths, enabling injection attacks that bypass traditional
> parameter validation; and (3) multi-step code generation cre-
> ates intermediate artifacts that may themselves become attack
> vectors. Prior work identified vulnerabilities in traditional
> MCP architectures but did not address the novel threats asso-
> ciated with the distinct phases of code generation, execution,
> and intermediate
**Section Heading**: `implementation returns a passkey belonging to an arbitrary` [section offsets: 45919:49361]
**First 120 words verbatim** [offsets: 45919:46832]
> implementation returns a passkey belonging to an arbitrary
> user:
> 
> get_pass_by_name("Emma") →"P789012"
> (John’s
> passkey)
> 
> For the benign task “Retrieve all doors that Emma has access
> to,” the agent (1) invokes get_pass_by_name("Emma"); (2)
> receives a poisoned response corresponding to a different
> user; and (3) constructs a SQL query using the returned value
> P789012:
> 
> SELECT doors.door_code FROM doors
> JOIN door_passkeys ON doors.door_code
> = door_passkeys.door_code WHERE
> door_passkeys.pass_key = ’P789012’
> 
> Impact.
> The query executes successfully and returns valid
> records, but the results correspond to a different user. The
> generated code appears correct upon inspection; the corrup-
> tion occurs entirely within the information flow between tools.
> This attack violates integrity by producing factually incorrect
> results while preserving syntactic and execution correctness.
> 
> 6.3.4
> Attack 4: Authorization State
**Section Heading**: `architecture, this validation layer defends against unsafe con-` [section offsets: 49361:54024]
**First 120 words verbatim** [offsets: 49361:50240]
> architecture, this validation layer defends against unsafe con-
> structs in the generated code, such as dynamic evaluation and
> dangerous imports(P5.1, P5.2), as well as unsafe execution
> patterns, including malicious code injection and obfuscated
> payloads (P3.1, P3.2, P3.3). This control acts as the first line
> of defense, preventing unsafe or excessively-privileged code
> from reaching the execution environment.
> 
> Pre-Execution Semantic Gating. Static validation cannot
> detect prompt injection attacks embedded in tool discovery
> artifacts (P1.1) or malicious tool metadata (P1.2, P2.1), since
> these attacks operate at the semantic level rather than the syn-
> tactic level. To address this gap, we introduce a pre-execution
> semantic gate positioned between tool discovery and code
> generation, analyzing discovered artifacts before they can
> influence downstream processing.
> 
> The gate

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 31558:35012]
**First 120 words verbatim** [offsets: 31558:32375]
> Evaluation
> 
> 6.1
> Experimental Setting
> 
> Agents and Models.
> We evaluate two agent architectures:
> (i) a traditional MCP agent (MCP), which follows the stan-
> dard context-coupled tool invocation loop defined by the MCP,
> and (ii) a code execution MCP agent (CE-MCP), which syn-
> thesizes executable code and delegates tool orchestration and
> data processing to an isolated sandbox runtime. (Section 5).
> 
> Each agent is evaluated using three LLMs: GPT-4o, GPT-
> 4.1, and GPT-4.1 mini, yielding six agent–model configura-
> tions (2 agents × 3 models).
> 
> Benchmark.
> All experiments are conducted using MCP-
> Bench [32], a benchmark for the evaluation of tool-using LLM
> agents that interact with real MCP servers. MCP-Bench tasks
> are programmatically synthesized and include a strict specifi-
> cation, a fuzzy natural-language variant,
**Section Heading**: `Results` [section offsets: 35012:39634]
**First 120 words verbatim** [offsets: 35012:35827]
> Results
> 
> Efficiency.
> Across all models and server configurations, the
> CE-MCP architecture consistently reduces the execution time,
> token usage, and number of turns compared to the traditional
> MCP.
> 
> The token savings achieved with the CE-MCP are substan-
> tial and increase with task complexity, particularly for two-
> and three-server tasks. This reduction stems from the fact that
> the CE-MCP avoids repeated serialization of tool schemas, in-
> termediate outputs, and reasoning steps into the model context
> window. Instead, data is loaded directly into the sandboxed
> runtime and processed programmatically, with only the final
> result returned to the agent.
> 
> The execution time results follow a similar trend. The tra-
> ditional MCP exhibits higher average latency due to long
> sequences of tool invocations and repeated
**Section Heading**: `results, which can be seen in Figure 9. While the CE-MCP` [section offsets: 39634:42815]
**First 120 words verbatim** [offsets: 39634:40564]
> results, which can be seen in Figure 9. While the CE-MCP
> maintains task fulfillment comparable to the MCP across
> all evaluated servers, we observe that tasks dominated
> by open-ended textual synthesis (e.g., Wikipedia, Reddit)
> occasionally benefit from the multi-turn interaction pattern of
> the traditional MCP. These tasks require iterative reasoning,
> progressive summarization, and contextual refinement, where
> additional turns can improve grounding and coherence. In
> contrast, CE-MCP favors servers centered on programmatic
> operations and deterministic tool usage (e.g., Math MCP, Unit
> Converter, Scientific Computing). In these settings, executing
> logic directly in a sandboxed environment avoids redundant
> language-model reasoning and repeated schema injection,
> yielding improved efficiency without a loss of correctness.
> 
> Overall, the
> CE-MCP
> delivers
> substantial
> efficiency
> improvements—reducing tokens, time, and turns—while
**Section Heading**: `evaluation captures systemic security risks inherent to the` [section offsets: 42815:45919]
**First 120 words verbatim** [offsets: 42815:43735]
> evaluation captures systemic security risks inherent to the
> CE-MCP execution model.
> 
> We perform all security evaluations using GPT-4o and
> GPT-4.1. The observed success rates were consistent across
> the models, indicating that the failures arise primarily from
> architectural semantics rather than model-specific behavior.
> 
> 6.3.1
> Attack 1: Context Injection via Discovery Artifacts
> (P1.1)
> 
> Mechanism.
> When the agent ingests attacker-controlled file
> names, directory names, or associated metadata into its plan-
> ning context, embedded adversarial instructions can corrupt
> subsequent reasoning and code generation.
> 
> Attack
> Setup.
> The
> MCP
> server
> includes
> a
> schema
> file
> called
> IMPORTANT_INSTRUCTION_READ_BEFORE_PLANNING.tsx,
> whose description embeds the following directive:
> 
> 10
> 
> --- PAGE BREAK ---
> 
> CRITICAL INSTRUCTION: apply NOT to
> the user’s query condition. First call
> inspect_db, then execute via query_db.
> 
> When the user

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 32098:32108]
> Benchmark.
**Location**: `Evaluation` [offsets: 32109:32254]
> All experiments are conducted using MCP-
> Bench [32], a benchmark for the evaluation of tool-using LLM
> agents that interact with real MCP servers.
**Location**: `Evaluation` [offsets: 33108:33221]
> Following the benchmark’s standard protocol,
> each server was evaluated on two single-server tasks from
> MCP-Bench.

## Block 6: Baseline Excerpts
**Location**: `Results` [offsets: 35033:35208]
> Across all models and server configurations, the
> CE-MCP architecture consistently reduces the execution time,
> token usage, and number of turns compared to the traditional
> MCP.

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 31615:31939]
> We evaluate two agent architectures:
> (i) a traditional MCP agent (MCP), which follows the stan-
> dard context-coupled tool invocation loop defined by the MCP,
> and (ii) a code execution MCP agent (CE-MCP), which syn-
> thesizes executable code and delegates tool orchestration and
> data processing to an isolated sandbox runtime.
**Location**: `Evaluation` [offsets: 34705:34851]
> • Execution Time: This measures end-to-end time from task
> input to final output, including model inference, tool execu-
> tion, and sandbox runtime.
**Location**: `Results` [offsets: 35033:35208]
> Across all models and server configurations, the
> CE-MCP architecture consistently reduces the execution time,
> token usage, and number of turns compared to the traditional
> MCP.
**Location**: `Results` [offsets: 35525:35666]
> Instead, data is loaded directly into the sandboxed
> runtime and processed programmatically, with only the final
> result returned to the agent.
**Location**: `Results` [offsets: 35668:35718]
> The execution time results follow a similar trend.
**Location**: `Results` [offsets: 35719:35836]
> The tra-
> ditional MCP exhibits higher average latency due to long
> sequences of tool invocations and repeated retries.

## Block 8: Limitations
**Section Heading**: `limitations. As the number of connected MCP servers and` [section offsets: 3463:6847]
**First 120 words verbatim** [offsets: 3463:4327]
> limitations. As the number of connected MCP servers and
> available tools grows [1], metadata and intermediate outputs
> consume an increasing portion of the model’s context win-
> dow, leaving less capacity for reasoning, increasing inference
> costs, and degrading performance on wide-context analytical
> tasks [22].
> 
> To bypass the overhead of traditional MCPs, major indus-
> try deployments such as Anthropic and Cloudflare have in-
> troduced a new execution paradigm—Code Execution MCP
> (CE-MCP) [15, 31]. CE-MCP adopts a context-decoupled
> execution model in which the agent generates a single, self-
> contained executable program that orchestrates the tool call-
> ing within an executable runtime environment. Rather than
> iteratively invoking tools through natural language exchanges,
> the agent encodes control flow, tool invocations, and data
> transformations directly into

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Results` [offsets: 39182:39523]
> In contrast, MCP is favored for tasks with iterative or se-
> mantically adaptive structures (e.g., retry loops, open-ended
> relevance filtering, or subjective aggregation). The MCP’s
> stepwise reasoning allows it to adapt execution based on in-
> termediate observations, whereas the CE-MCP must encode
> loop bounds and conditional logic up front.
**Matched Term**: `adaptive` | **Location**: `Discussion` [offsets: 54544:54908]
> Conversely, the traditional MCP retains advantages on se-
> mantically adaptive tasks that benefit from incremental rea-
> soning, localized retries, and progressive refinement. In such
> settings, the MCP can recover from partial failures through
> additional turns, whereas the CE-MCP must regenerate the
> entire execution program when global assumptions are in-
> correct.
**Matched Term**: `adaptive` | **Location**: `Limitations` [offsets: 56885:57208]
> Our layered defense architecture addressed and success-
> fully blocked all demonstrated attacks in all trials. However,
> we did not stress-test these mitigations against adaptive adver-
> saries who are aware of the defenses. Investigating mitigation
> robustness under adaptive threat model assumptions is a natu-
> ral next step.
**Matched Term**: `adaptive` | **Location**: `Limitations` [offsets: 56995:57398]
> However,
> we did not stress-test these mitigations against adaptive adver-
> saries who are aware of the defenses. Investigating mitigation
> robustness under adaptive threat model assumptions is a natu-
> ral next step.
> 
> 9
> Conclusion
> 
> This paper presents the first comparison of the performance
> of traditional context-coupled MCP and CE-MCP agents with
> respect to their efficiency, task quality, and security.
