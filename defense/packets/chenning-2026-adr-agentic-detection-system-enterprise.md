# Evidence Locator Packet: chenning-2026-adr-agentic-detection-system-enterprise

- **Title**: ADR: An Agentic Detection System for Enterprise Agentic AI Security
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2605.17380
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\chenning-2026-adr-agentic-detection-system-enterprise\fulltext.txt
- **Character Count**: 67253

## Block 2: Contribution Sentences
**Location**: `ABSTRACT` [offsets: 154:362]
> ABSTRACT
> We present the Agentic AI Detection and Response (ADR) system, the first large-scale, production-proven
> enterprise framework for securing AI agents operating through the Model Context Protocol (MCP).
**Location**: `ABSTRACT` [offsets: 1496:1797]
> To validate the approach and enable community adoption, we introduce ADR-Bench (302 tasks,
> 17 techniques, 133 MCP servers), where ADR achieves zero false positives while detecting 67% of attacks –
> outperforming three state-of-the-art baselines (ALRPHFS, GuardAgent, LlamaFirewall) by 2–4× in F1-score.
**Location**: `INTRODUCTION` [offsets: 5659:6526]
> We introduce ADR-
> Bench (302 tasks, 42 malicious, 260 benign), a bench-
> mark derived from real enterprise telemetry across 133
> MCP servers and 17 attack techniques. It captures the
> complexity, imbalance, and contextual diversity of pro-
> duction environments, enabling rigorous and reproducible
> evaluation of agentic security systems.
> 
> Deployed at UBER for over ten months (§6), ADR has
> demonstrated sustained reliability with growing adoption
> reaching over 7,200 unique hosts. The system detected
> hundreds of credential exposures across 26 categories that
> had been inadvertently shared outside the enterprise net-
> work. These findings informed a shift-left prevention layer
> that achieved 97.2% precision in blocking credential leaks
> (206 detected across 212 unique credentials from hundreds
> of thousands of sessions). Additionally, controlled testing
> through internal

## Block 3: Method Locator
**Section Heading**: `Implementation. ADR uses GPT-4o for triage and Claude` [section offsets: 33541:52496]
**First 120 words verbatim** [offsets: 33541:34346]
> Implementation. ADR uses GPT-4o for triage and Claude
> Sonnet 4 for reasoning, with three MCP servers providing
> enterprise context (§3). Importantly, ADR requires no hy-
> perparameter tuning as the triage and reasoning prompts
> are fixed across all tasks and benchmarks. All detectors are
> evaluated under identical conditions on the same hardware.
> 
> Metrics. For detection accuracy, we measure Precision,
> Recall, F1-score, True Positive (TP) / False Positive (FP)
> counts, and False Positive Rate (FPR). For operational ef-
> ficiency, we measure cost per task ($), mean latency (sec-
> onds), cost per true positive ($), and 95th percentile latency
> (seconds).
> 
> --- PAGE BREAK ---
> 
> ADR: An Agentic Detection System for Enterprise Agentic AI Security
> 
> 5.2
> Overall Performance
> 
> We benchmark ADR against all baselines

## Block 4: Evaluation Locator
**Section Heading**: `evaluation of agentic security systems.` [section offsets: 5953:7826]
**First 120 words verbatim** [offsets: 5953:6848]
> evaluation of agentic security systems.
> 
> Deployed at UBER for over ten months (§6), ADR has
> demonstrated sustained reliability with growing adoption
> reaching over 7,200 unique hosts. The system detected
> hundreds of credential exposures across 26 categories that
> had been inadvertently shared outside the enterprise net-
> work. These findings informed a shift-left prevention layer
> that achieved 97.2% precision in blocking credential leaks
> (206 detected across 212 unique credentials from hundreds
> of thousands of sessions). Additionally, controlled testing
> through internal capture-the-flag exercises and emulation of
> real-world attacks (Agent Flayer) validated ADR’s ability
> to trace multi-stage prompt injection and exfiltration chains.
> To rigorously validate the approach and enable community
> adoption (§5), we introduce ADR-Bench (302 tasks, 42
> malicious, 260 benign) derived from enterprise
**Section Heading**: `EVALUATION` [section offsets: 31591:33541]
**First 120 words verbatim** [offsets: 31591:32433]
> EVALUATION
> 
> 5.1
> Experimental Setup
> 
> Benchmarks. We evaluate on two benchmarks:
> 
> • AgentDojo (Debenedetti et al., 2024) is a public bench-
> mark for prompt injection detection containing 93 tasks
> (38 malicious, 55 benign) with attacks embedded in
> external data (tool outputs, web content, emails). We
> use AgentDojo as an auxiliary public reference focused
> on prompt injection. While AgentSafetyBench (Zhang
> et al., 2024b) has broader coverage, it is not MCP-native,
> so a faithful comparison would require substantial re-
> instrumentation of tasks/tools into an MCP setting.
> • ADR-Bench (§4) is our enterprise threat benchmark con-
> taining 302 agentic tasks covering 17 attack techniques
> across 5 tactical categories. Tasks include 42 malicious
> scenarios (13.9%) and 260 benign operations (86.1%),
> reflecting realistic enterprise class imbalance.

## Block 5: Attack-Set Excerpts
**Location**: `evaluation of agentic security systems.` [offsets: 6477:6691]
> Additionally, controlled testing
> through internal capture-the-flag exercises and emulation of
> real-world attacks (Agent Flayer) validated ADR’s ability
> to trace multi-stage prompt injection and exfiltration chains.
**Location**: `evaluation of agentic security systems.` [offsets: 7440:7590]
> On
> AgentDojo (Debenedetti et al., 2024) (a public prompt injec-
> tion benchmark), ADR detects all attacks with only three
> false alarms out of 93 tasks.
**Location**: `EVALUATION` [offsets: 31627:31638]
> Benchmarks.
**Location**: `EVALUATION` [offsets: 31639:31886]
> We evaluate on two benchmarks:
> 
> • AgentDojo (Debenedetti et al., 2024) is a public bench-
> mark for prompt injection detection containing 93 tasks
> (38 malicious, 55 benign) with attacks embedded in
> external data (tool outputs, web content, emails).
**Location**: `EVALUATION` [offsets: 32162:32304]
> • ADR-Bench (§4) is our enterprise threat benchmark con-
> taining 302 agentic tasks covering 17 attack techniques
> across 5 tactical categories.

## Block 6: Baseline Excerpts
**Location**: `evaluation of agentic security systems.` [offsets: 6908:7073]
> On ADR-
> Bench, ADR achieves zero false positives while detecting
> 67% of attacks, outperforming baselines by 2–4× in F1-
> score while maintaining low latency and cost.
**Location**: `evaluation of agentic security systems.` [offsets: 7203:7439]
> ately prioritize precision for production viability, as the high
> false positive rates of baseline methods (up to 40 FPs out
> of 260 benign tasks) make them unsuitable for deployment
> where false alarms trigger expensive incident response.
**Location**: `EVALUATION` [offsets: 32435:32445]
> Baselines.
**Location**: `EVALUATION` [offsets: 33273:33539]
> For all three baselines, we adapt their open-source imple-
> mentations to ensure fair comparison: LlamaFirewall from
> Meta’s Purple Llama repository (LlamaFirewall, 2025),
> GuardAgent (GuardAgent, 2025) and ALRPHFS (ALR-
> PHFS, 2025) from the authors’ official releases.

## Block 7: Cost Excerpts
**Location**: `evaluation of agentic security systems.` [offsets: 6279:6476]
> These findings informed a shift-left prevention layer
> that achieved 97.2% precision in blocking credential leaks
> (206 detected across 212 unique credentials from hundreds
> of thousands of sessions).
**Location**: `evaluation of agentic security systems.` [offsets: 6692:6907]
> To rigorously validate the approach and enable community
> adoption (§5), we introduce ADR-Bench (302 tasks, 42
> malicious, 260 benign) derived from enterprise telemetry
> across 133 MCP servers and 17 attack techniques.
**Location**: `evaluation of agentic security systems.` [offsets: 6908:7073]
> On ADR-
> Bench, ADR achieves zero false positives while detecting
> 67% of attacks, outperforming baselines by 2–4× in F1-
> score while maintaining low latency and cost.
**Location**: `evaluation of agentic security systems.` [offsets: 7203:7439]
> ately prioritize precision for production viability, as the high
> false positive rates of baseline methods (up to 40 FPs out
> of 260 benign tasks) make them unsuitable for deployment
> where false alarms trigger expensive incident response.
**Location**: `evaluation of agentic security systems.` [offsets: 7440:7590]
> On
> AgentDojo (Debenedetti et al., 2024) (a public prompt injec-
> tion benchmark), ADR detects all attacks with only three
> false alarms out of 93 tasks.
**Location**: `EVALUATION` [offsets: 31671:31886]
> • AgentDojo (Debenedetti et al., 2024) is a public bench-
> mark for prompt injection detection containing 93 tasks
> (38 malicious, 55 benign) with attacks embedded in
> external data (tool outputs, web content, emails).

## Block 8: Limitations
**Section Heading**: `Limitations of Existing Benchmarks` [section offsets: 26924:31591]
**First 120 words verbatim** [offsets: 26924:27757]
> Limitations of Existing Benchmarks
> 
> Most existing agent benchmarks cover only a small subset
> of agentic threats or lack MCP context. Table 1 shows
> that prior work covers only 3–6 of the 17 techniques, while
> ADR-Bench covers all 17 techniques across all five tactics.
> This comprehensive coverage with MCP context is essential
> for evaluating enterprise-ready detectors.
> 
> 4.3
> Our Benchmark: Composition and Ease of Use
> 
> To address these gaps, ADR-Bench reproduces real-world
> attacks from three sources: (i) attack scenarios adapted
> 
> No
> –
> 
> from existing benchmarks (e.g., MCP-Artifact (Song et al.,
> 2025), RAS-Eval (Fu et al., 2025)); (ii) publicly reported
> security incidents and research disclosures; and (iii) inter-
> nal threat intelligence from UBER’s deployment. We faith-
> fully recreate patterns including indirect prompt injection

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Background: Model Context Protocol (MCP) and` [offsets: 8259:8744]
> It addresses a key limitation of large language mod-
> els (LLMs) – their reliance on static pretraining data – by
> enabling standardized, dynamic access to real-time tools
> and environments. This transforms LLMs from isolated
> reasoning engines into adaptive, context-aware systems.
> 
> In a typical workflow (Figure 2), an MCP host (e.g., Cur-
> sor, Claude CLI) interacts with one or more remote MCP
> servers, each exposing modular capabilities such as file I/O,
> API calls, or database access.
**Matched Term**: `red team` | **Location**: `Background: Model Context Protocol (MCP) and` [offsets: 13476:13957]
> This includes examining source code, consulting threat in-
> telligence, and verifying policy compliance. The Offline
> Explorer (§3.2) functions like an internal red team, system-
> atically generating and testing attack scenarios in sandboxed
> environments during pre-deployment validation. Successful
> attacks discovered by the Explorer are curated into a threat
> intelligence repository that feeds back into Tier 2, strength-
> ening the detector’s robustness across diverse attack types.
**Matched Term**: `adaptive` | **Location**: `Background: Model Context Protocol (MCP) and` [offsets: 13762:14138]
> Successful
> attacks discovered by the Explorer are curated into a threat
> intelligence repository that feeds back into Tier 2, strength-
> ening the detector’s robustness across diverse attack types.
> This human-inspired design makes the system adaptive and
> operationally grounded.
> 
> --- PAGE BREAK ---
> 
> ADR: An Agentic Detection System for Enterprise Agentic AI Security
> 
> Figure 4.
**Matched Term**: `evasion` | **Location**: `Background: Model Context Protocol (MCP) and` [offsets: 20993:21568]
> To
> strengthen detection robustness across diverse attack types,
> the Offline Explorer systematically generates and tests at-
> tack variants through three collaborative agents: The Red-
> Teaming Agent proposes realistic attack variants by mutat-
> ing parameters and combining techniques from a seed set
> of known attacks. The Eval Agent executes these candi-
> dates in sandboxed (isolated) environments, measuring both
> attack success and detection evasion. The Threat Intelli-
> gence Agent curates high-value discoveries and publishes
> them to the threat repository for use by Tier 2.
**Matched Term**: `red team` | **Location**: `Background: Model Context Protocol (MCP) and` [offsets: 25987:26294]
> Yes
> 
> along with conversations with red team experts. This syn-
> thesis yields a practical five-tactic, 17-technique threat
> framework tailored to MCP-driven agentic systems (Ap-
> pendix A.1), where tactics describe the adversary’s goal
> (the “why”) and techniques describe specific attack meth-
> ods (the “how”).
**Matched Term**: `adaptive` | **Location**: `Implementation. ADR uses GPT-4o for triage and Claude` [offsets: 50602:50912]
> 2025-10-28
> 
> academia, GuardAgent (Xiang et al., 2024) and AGrail (Luo
> et al., 2025) generate adaptive safety checks and executable
> code to validate agent actions against security requirements.
> ShieldAgent (Chen et al., 2025) structures policy documents
> into verifiable rule circuits to shield protected agents.
**Matched Term**: `adaptive` | **Location**: `CONCLUSION` [offsets: 53640:54039]
> We release ADR-Bench, the ADR Sensor, and the detec-
> tion framework to support reproducibility and community
> adoption. Looking ahead, we see opportunities in extend-
> ing ADR to multi-agent coordination protocols, adaptive
> real-time prevention at the MCP gateway layer, and tighter
> integration with evolving MCP standards to further close
> the gap between detection and response.
> 
> REFERENCES
> 
> ALRPHFS.
**Matched Term**: `adaptive` | **Location**: `REFERENCES` [offsets: 59498:59630]
> and Xiao, C. Agrail: A lifelong agent guardrail with
> effective and adaptive safety detection. arXiv preprint
> arXiv:2502.11448, 2025.
**Matched Term**: `evade` | **Location**: `REFERENCES` [offsets: 65925:67253]
> Security Control By-
> pass
> 
> Adversaries evade detection and circum-
> vent security mechanisms by deploying ma-
> licious tools, manipulating tool resolution,
> or coordinating multiple agents
> 
> Reasoning & Data
> Manipulation
> 
> Adversaries corrupt data sources or manipu-
> late an agent’s reasoning processes to com-
> promise decision integrity and degrade long-
> term reliability
> 
> Operational Impact
> Adversaries disrupt availability and degrade
> business operations by exhausting system
> resources or overwhelming the agent’s infer-
> ence capacity
> 
> 6 techniques: Insecure Supply Chain (JFrog Secu-
> rity Research, 2025), Indirect Prompt Injection (Zen-
> ity Labs, 2025), Control-Flow Hijacking (Invariant
> Labs, 2025c), Code Interpreter Abuse (CyberArk,
> 2025), Insecure Output Handling, Tool Rug Pull (In-
> variant Labs, 2025b)
> 
> 2 techniques: Exploitation of Excessive Tool Per-
> missions (Invariant Labs, 2025a;d), Agent Identity
> Spoofing
> 
> 3 techniques: Tool Shadowing (Microsoft Defender,
> 2025; CyberArk, 2025), Tool Hallucination Manipu-
> lation, Malicious Agent Collusion (Solo.io, 2025)
> 
> 4 techniques: Unvetted MCP Server Connection,
> Semantic Data Poisoning, Long-Term Goal Hijack-
> ing (Hubinger et al., 2024), Temporal Data Attack
> 
> 2 techniques: Agent-Facilitated Resource Exhaus-
> tion (OWASP Foundation, 2025), Model-Layer De-
> nial of Service
