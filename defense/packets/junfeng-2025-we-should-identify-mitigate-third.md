# Evidence Locator Packet: junfeng-2025-we-should-identify-mitigate-third

- **Title**: We Should Identify and Mitigate Third-Party Safety Risks in MCP-Powered Agent Systems
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: position_other
- **Link**: https://arxiv.org/abs/2506.13666
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\junfeng-2025-we-should-identify-mitigate-third\fulltext.txt
- **Character Count**: 77632

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 553:1375]
> Abstract
> 
> The development of large language models (LLMs) has entered in a experience-
> driven era, flagged by the emergence of environment feedback-driven learning via
> reinforcement learning and tool-using agents. This encourages the emergenece
> of model context protocol (MCP), which defines the standard on how should a
> LLM interact with external services, such as API and data. However, as MCP
> becomes the de facto standard for LLM agent systems, it also introduces new safety
> risks. In particular, MCP introduces third-party services, which are not controlled
> by the LLM developers, into the agent systems. These third-party MCP services
> provider are potentially malicious and have the economic incentives to exploit
> vulnerabilities and sabotage user-agent interactions. In this position paper, we
> advocate the research

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 3667:3702]
**First 120 words verbatim** [offsets: 3667:4530]
> Evaluation
> 
> Safeguard MCP Service
> 
> 1. Hybrid Detection
> 2. Rust Graph Propagation
> 3. Rigor and Adaptability
> Balance
> 4. ......
> 
> Benchmark
> 
> Third-Party
> 
> Dataset
> 
> Quantified
> MCP Safety
> 
> Adversarial
> 
> Targeted
> 
> Attak
> 
> Metric
> 
> Cross Service
> 
> Protocol
> 
> MCP-Safe Backbone LLM
> 
> Data Accumulation
> 
> Safe MCP Ecosystem
> 
> 1. Global Standards for
> Service Auditing
> 2. Collaborative Governance
> Networks
> 
> Pretraining
> 
> Convertion
> 
> Fine-tuning
> 
> Annotation
> 
> MCP Safety
> 
> Data for
> MCP Safety
> 
> Aware
> 
> Reforcement
> 
> Synthesis
> 
> Learning
> 
> 3. ......
> 
> Although there are attempts to address the safety issue in tool-using scenarios [92, 15, 20], these
> works are still limited by the fact that these tools are pre-vetted and sanitized, thereby hard to reveal
> the tripartite threat model essential for physical-world deployment. Standing at the dawn of a thriving
> MCP ecosystem and awaring of the
**Section Heading**: `Evaluation` [section offsets: 5086:5161]
**First 120 words verbatim** [offsets: 5086:5878]
> Evaluation
> 
> Scenario
> Metric
> 
> Single-Server
> Multi-Server
> 
> Helpfulness: RAL
> 
> 1. WebShop
> 2. Baby AI
> 3. Sheet
> 4. Academia
> 5. Movie
> 
> 6. Weather
> 7. Sciworld
> 8. Text Craft
> 9. AlfWorld
> 10. ......
> 
> Harmfulness:
> 
> ASR & HR
> 
> Detectability: DR
> 
> ......
> 
> Figure 1: The overall framework of a MCP safe agent system, including: (1) Upper Left: The
> differences between MCP introduced safety risks and traditional LLM safety risks. (2) Right: The
> overall architecture of SAFEMCP. (3) Bottom Left: Outlook for MCP safety.
> 
> proposal half year ago, MCP is supported by various frontier LLMs, such as GPT, Claude, Gemini, and
> Qwen, positioning MCP as the architectural foundation for open, real-world-integrated agent systems.
> 
> To demonstrate the practical implication of this position, we first conduct a series of
**Section Heading**: `Evaluation` [section offsets: 26275:35979]
**First 120 words verbatim** [offsets: 26275:27029]
> Evaluation
> 
> Evaluation tells us how safe the MCP-powered agent system is and towards which direction we should
> improve. Thus, a set of evaluation toolkits is necessary to evaluate the safety of MCP-powered agent
> systems. On top of SAFEMCP, we propose to continually improve the evaluation framework.
> 
> 7
> 
> To alleviate the safety issues brought by MCP, we need to develop more robust LLM serving as the
> agent backbone that is more robust to the attacks. We argue that this is necessary because we can
> hardly have access to the implementation of the third-party MCP-service, which limits the feasibility
> to monitor and filter out malicious services in advance. Thus, we propose to embed safeguards
> directly into backbone LLMs.
> 
> Following the common practice

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 28353:28375]
> (1) Benchmark Dataset.
**Location**: `Evaluation` [offsets: 28376:28472]
> Benchmark datasets establish the testbed for evaluating the safety of MCP-powered agent systems.
**Location**: `Evaluation` [offsets: 28473:28599]
> In particular, as MCP is a relatively newly emerging field, there is a lack of safety benchmarks that
> integrates MCP services.
**Location**: `Evaluation` [offsets: 28600:28883]
> Moreover, to simulate the real-world scenarios, the benchmark should not
> only integrate new adversarial scenarios, but also embed real-world constraints like sensor noise, API
> rate limits, and partial observability, exposing how safety mechanisms degrade under operational
> pressures.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 27262:27427]
> To prevent potential MCP attacks, the
> LLM backbone model should be equipped with the knowledge of which kind of information from
> MCP is an attack and what is benign.
**Location**: `Evaluation` [offsets: 29239:29685]
> We would like to
> nominate a few more dimensions that are worth exploring, such as cascading impact scores that
> measure how a single compromised service propagates errors through dependent tools (e.g., corrupted
> ratio of the workflow); recovery latency thresholds that define maximum tolerable downtime for
> 
> --- PAGE BREAK ---
> 
> 4.4
> Data Accumulation
> 
> During the initial development stage of MCP ecosystem, data scarcity is a significant challenge.

## Block 8: Limitations
**Location**: `Limitations`
**First 120 words verbatim** [offsets: 67745:68669]
> Limitations
> 
> Our work establishes a foundational framework for MCP safety and advocates three critical impera-
> tives for the MCP research community. However, two critical limitations merit discussion:
> 
> • Our current implementation evaluates two baseline defense paradigms, i.e., proactive service
> whitelisting and reactive LLM-based filtering, to probe the lower bounds of MCP safety. While
> these strategies reveal fundamental defense-attack dynamics, they leave unexplored the full potential
> of advanced defense mechanisms. Future iterations of SafeMCP will integrate these sophisticated
> strategies to systematically evaluate performance ceilings under optimal protection scenarios.
> • A second constraint stems from our focus on inherent safety properties of backbone LLMs. That
> is, SAFEMCP currently evaluates agents’ native capabilities without without post-hoc alignment
> training (e.g., tool invocation specialization or

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Evaluation` [offsets: 32270:32636]
> The safety of MCP-powered agent system transcends technical innovation, demanding a socio-
> technical framework where governance, collaboration, and adaptive learning converge. Unlike closed
> AI systems, MCP’s open and extensible nature necessitates a shared responsibility model, uniting
> developers, service providers, regulators, and end-users in safeguarding trust.
