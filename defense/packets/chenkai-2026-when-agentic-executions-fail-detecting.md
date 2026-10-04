# Evidence Locator Packet: chenkai-2026-when-agentic-executions-fail-detecting

- **Title**: When Agentic Executions Fail: Detecting and Localizing Runtime Faults from Telemetry
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: benchmark_measurement
- **Link**: https://arxiv.org/abs/2608.14680
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\chenkai-2026-when-agentic-executions-fail-detecting\fulltext.txt
- **Character Count**: 49527

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 514:650]
> We present
> AgentChaosBench, a benchmark for detecting and localizing run-
> time faults in agentic systems from their execution telemetry.
**Location**: `Introduction` [offsets: 5270:6159]
> We introduce AgentChaosBench, a fault-injection benchmark
> for evaluating the diagnosability of LLM-based agentic systems.1
> 
> We use agent applications derived from AI-NativeBench [15] as ex-
> ecutable workloads and inject faults at multiple boundaries of their
> execution, including tool calls, LLM calls, guardrails, and agent-to-
> agent interactions. Each run is executed with a locally deployed
> 
> 1The experimental code and a sample of the benchmark data are available at https:
> //github.com/kevinzck8k/agentic-fault-diagnosis.
> 
> --- PAGE BREAK ---
> 
> Raw trace
> Langfuse JSON
> 
> Task + fault
> configuration
> 
> Instrumented
> agentic execution
> 
> LLM and instrumented through Langfuse to capture its distributed
> trace, including agent, model, and tool spans and their timing, in-
> puts, outputs, and status metadata. Fault-injection markers and
> labels are removed before diagnosis; the injected fault type

## Block 3: Method Locator
**Section Heading**: `method` [section offsets: 9052:25522]
**First 120 words verbatim** [offsets: 9052:9893]
> method
> fault type
> + location
> 
> case.json
> 
> Figure 1: The AgentChaosBench data-generation and diagnosis pipeline.
> 
> examining how an execution unfolded in addition to what it pro-
> duced.
> 
> AgentChaosBench supports this form of analysis through con-
> trolled fault injection and trace-based diagnosis. We execute five
> heterogeneous agentic systems, inject faults into their model calls,
> tools, guardrails, and inter-agent interactions, and capture the re-
> sulting telemetry as structured traces. A diagnosis method receives
> a trace with all injection markers and fault labels removed, and
> must classify the fault and localize the affected span or compo-
> nent. To make this task both realistic and verifiable, injected faults
> must model plausible operational failures and produce evidence in
> the collected telemetry that grounds their assigned fault

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 25522:30929]
**First 120 words verbatim** [offsets: 25522:26308]
> Evaluation
> 
> We ask whether a diagnosis method can infer a fault’s presence,
> type, and responsible component from sanitized telemetry, and how
> that depends on the fault class and detector capacity. We report a
> first set of LLM baselines, organized around four research questions:
> 
> • RQ1 (Fault-type diagnosis and trace representation). How
> accurately can a detector identify the fault type from a single
> sanitized trace, and how do the structured and raw views affect
> coverage and accuracy?
> • RQ2 (Fault-specific difficulty). How does diagnosability vary
> across fault types and the four fault-model classes?
> 
> • RQ3 (Localization). Beyond naming the fault type, can a de-
> tector reliably identify the responsible component and jointly
> predict its location and fault type?
> • RQ4 (Reference
**Section Heading**: `Results` [section offsets: 30929:38027]
**First 120 words verbatim** [offsets: 30929:31673]
> Results
> 
> Table 3 reports AC@1 and AC@3 on the 250 faulty cases for the
> structured and raw trace representations; a dash indicates that the
> detector could not ingest the raw trace within its context window.
> Table 4 reports per-fault-type top-3 recall on structured traces. Each
> entry is the number of cases whose true fault type appears in the
> detector’s top three, out of 25 cases (5 systems × 5 inputs); the final
> row instead counts no-fault controls correctly recognized as clean.
> RQ1: fault-type diagnosis remains difficult across trace rep-
> resentations. Table 3 shows that fault-type diagnosis from a single
> sanitized trace is difficult. The local Qwen detectors sit at 13.6–
> 19.2% AC@1, barely above the 9% random baseline and essentially

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 28708:28882]
> All baselines run against the corrected AgentChaosBench dataset
> of 275 cases, with directory names and held-out fields excluded
> from the input and greedy decoding throughout.
**Location**: `Results` [offsets: 37750:38023]
> And the faults that matter
> most for trustworthiness, above all a bypassed guardrail and a
> silent context overflow, are exactly the ones single-trace detectors
> miss at every scale, motivating the reference-based and specialized
> methods the benchmark is designed to evaluate.

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 25719:25856]
> We report a
> first set of LLM baselines, organized around four research questions:
> 
> • RQ1 (Fault-type diagnosis and trace representation).
**Location**: `Evaluation` [offsets: 27086:27176]
> 3.2
> Baselines
> 
> Our baselines are general-purpose instruction-tuned LLMs applied
> zero-shot.
**Location**: `Evaluation` [offsets: 27101:27176]
> Our baselines are general-purpose instruction-tuned LLMs applied
> zero-shot.
**Location**: `Evaluation` [offsets: 27705:27816]
> A rule-based detector over the observable signals in
> Table 2 is a natural non-LLM baseline left to future work.
**Location**: `Evaluation` [offsets: 28708:28882]
> All baselines run against the corrected AgentChaosBench dataset
> of 275 cases, with directory names and held-out fields excluded
> from the input and greedy decoding throughout.
**Location**: `Results` [offsets: 31572:31886]
> The local Qwen detectors sit at 13.6–
> 19.2% AC@1, barely above the 9% random baseline and essentially
> 
> Chenkai Zhang, Yiran Li, Yifang Tian, Michalis Bachras, and Hans-Arno Jacobsen
> 
> flat across an order of magnitude of model size; and even DeepSeek-
> v4-pro, a frontier model, reaches only 24.8% AC@1 (34.0% AC@3).

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 29816:30426]
> Performance faults
> A2A Latency
> 10/25
> 10/25
> 12/25
> 13/25
> 7/25
> Tool Latency
> 0/25
> 1/25
> 7/25
> 9/25
> 11/25
> 
> Control and routing faults
> Infinite Loop
> 9/25
> 12/25
> 5/25
> 6/25
> 2/25
> Tool Misroute
> 0/25
> 4/25
> 0/25
> 5/25
> 3/25
> Agent Misroute
> 0/25
> 1/25
> 2/25
> 3/25
> 10/25
> 
> Data and policy faults
> Context Overflow
> 8/25
> 2/25
> 2/25
> 1/25
> 0/25
> Output Corruption
> 3/25
> 3/25
> 0/25
> 5/25
> 4/25
> Guardrail Bypass
> 0/25
> 1/25
> 0/25
> 1/25
> 1/25
> 
> No Fault (recognized)
> 1/25
> 14/25
> 12/25
> 24/25
> 22/25
> 
> exhausts its output budget mid-deliberation; we show in §5 that
> doubling the budget leaves the accuracies unchanged, so they are
> not an artifact of the budget.
**Location**: `Results` [offsets: 32292:32544]
> Recognition of no-fault controls follows a different trend:
> it rises from 4% for Qwen3-1.7B to 96% for Qwen3-14B (and 88%
> for DeepSeek-v4-pro), indicating that scale helps detectors avoid
> false alarms even though fault-type classification remains weak.
**Location**: `Results` [offsets: 35441:35607]
> When Agentic Executions Fail: Detecting and Localizing Runtime Faults from Telemetry
> 
> Table 5: Component-location and type-and-location accuracy
> on structured traces.
**Location**: `Results` [offsets: 36388:36620]
> The largest gains occur for faults defined by
> a deviation from normal behavior: for Qwen3-14B, the reference
> raises Context Overflow recall by 55 points and Tool Latency by
> 35 points, while routing faults improve for some detectors.
**Location**: `Results` [offsets: 36845:37026]
> Guardrail Bypass is un-
> moved or slightly worse (−5 to 0 points): on a benign input the
> reference guard also returns pass, so a forged pass is indistinguish-
> able even side by side.

## Block 8: Limitations
**Section Heading**: `Limitations` [section offsets: 40928:42182]
**First 120 words verbatim** [offsets: 40928:41727]
> Limitations
> 
> The current benchmark uses five systems with five aligned inputs
> per condition; while this yields 275 verified cases and balanced per-
> fault coverage, broader task and input diversity would strengthen
> external validity, and we plan to scale both. Our baselines are zero-
> shot general-purpose LLMs (four local Qwen models and the fron-
> tier DeepSeek-v4-pro) evaluated on both the structured and raw
> trace views; a rule-based non-LLM detector, few-shot prompting,
> and specialized attribution methods remain to be evaluated. Because
> DeepSeek-v4-pro is served through a commercial API, its outputs
> are not reproducible even at temperature 0: a re-run disagrees on
> nearly half (48%) of top-1 predictions, though aggregate accuracy
> is stable to within a point, so we read its per-case results

## Block 9: Adaptivity Hits
**Matched Term**: `white-box` | **Location**: `Related Work` [offsets: 38041:38469]
> Agentic systems and observability. Benchmarks such as Agent-
> Bench established the breadth of tasks LLM agents can solve through
> multi-step environment interaction [11], and AI-native suites like
> AI-NativeBench extend this to white-box systems that combine
> agents with MCP tools and A2A communication [15]. As these
> systems grow into distributed software, operating them reliably
> requires telemetry beyond final-answer checking.
**Matched Term**: `White-Box` | **Location**: `References` [offsets: 48265:48394]
> AI-NativeBench: An Open-
> 
> Source White-Box Agentic Benchmark Suite for AI-Native Systems.
> arXiv
> preprint arXiv:2601.09393 (2026).
