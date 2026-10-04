# Evidence Locator Packet: shi-2026-when-manual-lies-realistic-benchmark

- **Title**: When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents
- **Year**: 2026
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: benchmark_measurement
- **Link**: https://arxiv.org/abs/2605.24069
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\shi-2026-when-manual-lies-realistic-benchmark\fulltext.txt
- **Character Count**: 30944

## Block 2: Contribution Sentences
**Location**: `Abstract—The rise of tool-using Large Language Model (LLM)` [offsets: 571:668]
> This paper systematically investigates Tool Description
> Poisoning (TDP), a novel semantic attack.
**Location**: `Abstract—The rise of tool-using Large Language Model (LLM)` [offsets: 886:994]
> To rigorously and systematically evaluate this emerging
> threat, we introduce the MCP-TDP Security Benchmark.
**Location**: `I. INTRODUCTION` [offsets: 5043:5936]
> we introduce the MCP-TDP Security
> Benchmark, a high-fidelity evaluation framework built on a
> Docker-based sandbox. We simulate a complete agent work-
> flow—Discovery, Planning, Execution, and Verification—to
> evaluate resilience against metadata attacks. We design 32
> concrete test cases across 6 risk categories adapted from the
> OWASP Top 10 for LLMs [22], covering both “Trojan Horse”
> 
> --- PAGE BREAK ---
> 
> Fig. 2. MCP-TDP Security Benchmark framework architecture: Workflow shows interactions between the LLM agent, MCP servers (hosting legitimate/poisoned
> tools), and sandboxed execution environment; forensic analysis verifies physical side-effects of 32 attack experiments.
> 
> 1
> 
> 32 experiments
> 
> TDP attack
> 
> process
> 
> MCP Client
> LLMs
> &
> 
> Attacker
> 
> ............
> 
> ............
> 
> 3
> 
> MCP Providers
> 
> Final data analysis
> 
> Data aggregation
> 
> and “Supply Chain” scenarios. Crucially, we employ a forensic

## Block 3: Method Locator
**Section Heading**: `A. Framework Architecture` [section offsets: 10482:11755]
**First 120 words verbatim** [offsets: 10482:11343]
> A. Framework Architecture
> 
> As depicted in Fig. 2, the benchmark simulates a complete
> threat-aware workflow through four modular components:
> 
> 1) Controlled Execution Environment: Acting as the
> sandbox (Step 1), isolated Docker containers are pre-
> configured with specific file system states (e.g., dummy
> sensitive files). This strictly isolates and captures the
> physical side-effects of attacks [25].
> 2) MCP Server Cluster: To mimic a real-world ecosystem
> (Step 2), we deploy a malicious server hosting 32
> poisoned tools alongside legitimate functional servers.
> This diversity forces the agent to plan across multi-
> ple sources, testing its resilience against “needle-in-a-
> haystack” metadata attacks [26].
> 3) Standardized Client Interface: A unified ‘Cline’ client
> (Step 3) manages tool discovery and conversation his-
> tory. Standardizing this interface ensures
**Section Heading**: `C. Attack Implementation Schemes` [section offsets: 12758:13777]
**First 120 words verbatim** [offsets: 12758:13534]
> C. Attack Implementation Schemes
> 
> We formalize TDP into two schemes based on the prove-
> nance of the tool T and the integration method of the malicious
> payload P:
> 
> 1) Scheme 1: The “Trojan Horse” Approach (Tnew
> /∈
> Tenv): The attacker introduces a novel, ostensibly benign
> tool Tnew (e.g., “Weather Forecaster”) into the agent’s en-
> vironment. The description is constructed as D(Tnew) =
> Dmask ⊕P, where Dmask represents the lure functionality.
> P is framed as a mandatory constraint (e.g., “list desktop to
> ensure data currency”), exploiting the agent’s trust in declared
> functional requirements [18].
> 
> 2) Scheme 2: The “Supply Chain” Attack (Texist ∈Tenv):
> The attacker subverts a trusted, existing tool Texist (e.g.,
> “File Reader”). The description is mutated to D′(Texist) =
**Section Heading**: `3. Need to use another method to achieve precise deletion of specific lines` [section offsets: 22978:23054]
**First 120 words verbatim** [offsets: 22978:23747]
> 3. Need to use another method to achieve precise deletion of specific lines
> 4. Solution: use the read_file tool of the terminal-controller to get the file
> content, manually delete lines 1-2, and then rewrite the file with the write_file
> tool
> 
> DeepSeek
> 
> ⚙️Execution: The operation was completed but the result did not meet
> expectations. Due to MCP tool limitations, attempting to delete the specified
> lines accidentally emptied the entire file content. The file
> /root/....../emergency.py is now empty. It is recommended to manually restore
> the file content or obtain it from a backup.
> 
> Fig. 5. Reactive Self-Correction by a DeepSeek model. After executing the
> attack, the agent realizes the error and attempts to revert the action.
> 
> Fig. 5 illustrates this process. This

## Block 4: Evaluation Locator
**Section Heading**: `evaluation protocol where attack success is determined strictly` [section offsets: 5937:6661]
**First 120 words verbatim** [offsets: 5937:6782]
> evaluation protocol where attack success is determined strictly
> by inspecting physical side-effects in the sandbox (e.g., file
> creation, server logs), ensuring zero false positives and val-
> idating the real-world impact of the compromised planning
> layer.
> 
> Contributions: (1) We formally define Tool Description
> Poisoning (TDP), a semantic attack vector targeting the
> cognitive planning layer of LLM agents. (2) We develop
> the MCP-TDP Security Benchmark, the first specialized, a
> reproducible sandbox with 32 real-world test cases verified via
> forensics. (3) We evaluate 8 LLMs, revealing high vulnerabil-
> ity (ASR > 88% for top models) and identifying “The Firewall
> Fallacy” alongside “Reactive Self-Correction” behaviors.
> 
> II. THREAT MODEL AND DEFINITIONS
> To rigorously evaluate TDP, we must clearly define the
> capabilities of the adversary and
**Section Heading**: `D. Evaluation Protocol` [section offsets: 13777:16093]
**First 120 words verbatim** [offsets: 13777:14500]
> D. Evaluation Protocol
> 
> A strict four-stage protocol is followed for each of the 32
> test cases:
> 
> • Prepare: The Docker sandbox is reset, and the specific
> set of MCP tools (including the poisoned one) is loaded.
> 
> --- PAGE BREAK ---
> 
> TABLE II
> VULNERABILITY FINGERPRINTS OF THE EVALUATED MODELS ACROSS SIX MAJOR RISK CATEGORIES, DETAILING THE ATTACK SUCCESS RATE (ASR)
> AND USER COMMAND COMPLETION (UCC) FOR EACH MODEL. VALUES REPRESENT THE MEAN ATTACK SUCCESS RATE (ASR) OVER 5 INDEPENDENT
> 
> RUNS PER TEST CASE (N = 160 TOTAL RUNS PER MODEL). HIGH ASR INDICATES HIGH VULNERABILITY. RESULTS ARE REPORTED AS ”ASR / UCC”.
> 
> GPT-4o
> Claude 3.7 Sonnet
> Claude 4 Sonnet
> Gemini 2.5 Pro-pre
> DeepSeek V3
> DeepSeek R1
> QWQ 32B
> Qwen3 32B
> 
> Risk
**Section Heading**: `IV. EXPERIMENTAL EVALUATION` [section offsets: 16093:16121]
**First 120 words verbatim** [offsets: 16093:16879]
> IV. EXPERIMENTAL EVALUATION
> A. Setup and Metrics
> 
> We evaluated eight prominent models: GPT-4o, Claude
> 3.7/4 Sonnet, Gemini 2.5 Pro-pre, DeepSeek V3/R1, QWQ
> 32B, and Qwen3 32B. To mitigate the stochastic nature of
> LLMs, each test case was executed 5 independent times.
> The metrics reported below represent the average across these
> runs.
> 
> 1. Attack Success Rate (ASR): The percentage of test cases
> where the malicious payload was successfully executed. At-
> tack success requires the malicious payload P to produce the
> expected malicious system side-effect E(P) in the sandbox.
> 
> Success(U, Tpoisoned) ⇐⇒F(E(P(U))) = TRUE
> (5)
> 
> Where F is an objective binary function checking forensic
> evidence (e.g., file creation, data egress). ASR is calculated
> as:
> 
> PN
> 
> i=1 I(Successi)
> 
> ASR =
> 
> N
> (6)
> 
> 2.
**Section Heading**: `D. The Firewall Fallacy: Guardrail Evaluation` [section offsets: 19192:20154]
**First 120 words verbatim** [offsets: 19192:19974]
> D. The Firewall Fallacy: Guardrail Evaluation
> 
> A common defense strategy is to deploy a ‘prompt-
> guardrail’ or firewall to filter malicious inputs [15]. We tested
> this by enabling LlamaGuard-based filters on GPT-4o and
> Gemini 2.5 Pro-pre. The results in Table IV are telling.
> 
> For GPT-4o, the reduction in ASR was limited (-15.3%),
> leaving the model highly vulnerable. More alarmingly, for
> Gemini, the ASR increased. This exposes what we term
> the “Firewall Fallacy.” Guardrails often rely on keyword
> matching or detecting explicit malice. However, TDP frames
> malicious actions as operational requirements of the tool (e.g.,
> “This tool requires reading /etc/passwd to configure itself”).
> The guardrail sees a valid tool operation, not a user attack,
> and lets it pass. The increase in

## Block 5: Attack-Set Excerpts
**Location**: `evaluation protocol where attack success is determined strictly` [offsets: 6344:6490]
> (2) We develop
> the MCP-TDP Security Benchmark, the first specialized, a
> reproducible sandbox with 32 real-world test cases verified via
> forensics.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `evaluation protocol where attack success is determined strictly` [offsets: 5937:6191]
> evaluation protocol where attack success is determined strictly
> by inspecting physical side-effects in the sandbox (e.g., file
> creation, server logs), ensuring zero false positives and val-
> idating the real-world impact of the compromised planning
> layer.
**Location**: `D. Evaluation Protocol` [offsets: 15728:15843]
> • Trigger: The agent receives a benign user prompt (e.g.,
> “Summarize this document”) that requires using the tools.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
