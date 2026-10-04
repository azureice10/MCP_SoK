# Evidence Locator Packet: lichao-2026-safemcp-proactive-power-regulation-llm

- **Title**: SafeMCP: Proactive Power Regulation for LLM Agent Defense via Environment-Grounded Look-Ahead Reasoning
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2606.01991
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\lichao-2026-safemcp-proactive-power-regulation-llm\fulltext.txt
- **Character Count**: 96155

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 583:735]
> In response, we propose SafeMCP,
> a server-side defense plugin that constrains
> tool acquisition via predictive reasoning regard-
> ing future safety risks.
**Location**: `Abstract` [offsets: 947:1139]
> To train SafeMCP, we introduce a three-
> stage pipeline comprising environmental dy-
> namic grounding, safe policy initialization, and
> reinforcement learning (RL) with dual verifi-
> able rewards.
**Location**: `Introduction` [offsets: 5225:6038]
> we propose SafeMCP, a server-side
> defense plugin that constrains tool acquisition via
> predictive reasoning regarding future safety risks.
> Specifically, the mechanism of SafeMCP is shown
> in the fig. 1(B). We formulate the agent-defense
> interaction as a Cooperative Stackelberg Power
> Game (von Stackelberg, 2010; Zhao et al., 2023).
> Grounded in environment dynamics, SafeMCP pre-
> dicts the state transition and conducts a reasoning
> process to assess state safety and to identify tools
> that precipitate hazardous transitions. SafeMCP en-
> forces a two-tier defense: (1) a proactive filtering
> layer constrains the power of the next state by ex-
> cluding tools that enable unsafe transitions; (2) an
> intervention layer serves as a fail-safe, intercepting
> hazardous tool calls at the current step.
> 
> Through training in an

## Block 3: Method Locator
**Section Heading**: `Method` [section offsets: 14507:18331]
**First 120 words verbatim** [offsets: 14507:15382]
> Method
> 
> We introduce SafeMCP, a framework that integrates
> 
> proactive tool filtering with immediate safety con-
> straints. By leveraging an internal world model for
> look-ahead reasoning, SafeMCP preemptively fil-
> ters out tools that induce transitions from Scritical to
> Sunsafe. Complementarily, a fail-safe intervention
> layer blocks tool invocations predicted to result in
> Sunsafe, thereby reducing residual risk when proac-
> tive filtering is insufficient.
> 
> As shown in fig. 2, SafeMCP undergoes a three-
> stage training pipeline: (1) Environmental Dynam-
> ics Grounding. (2) Safe Policy Initialization. (3)
> RL with Dual Verifiable Rewards.
> 
> 4.1
> Inference-Time Defense Mechanism
> 
> Our server-side defense operates transparently to
> the agent, intervening only during queries for avail-
> able tools Ai and tool execution requests. This
> design yields an agent-agnostic framework.
> 
> As

## Block 4: Evaluation Locator
**Section Heading**: `Experiments` [section offsets: 24956:32593]
**First 120 words verbatim** [offsets: 24956:25818]
> Experiments
> 
> We conduct extensive experiments to validate
> whether SafeMCP achieves a safe equilibrium. We
> show that it:
> 
> • SafeMCP mitigates risks from power-seeking
> behaviors by regulating task-irrelevant tool ac-
> cessed in high-privilege states;
> 
> • SafeMCP preserves workflow continuity by fil-
> tering harmful tool calls before execution, pre-
> venting unsafe actions;
> 
> • SafeMCP maintains high utilities by avoiding the
> over-refusal common to other defenses.
> 
> Furthermore, ablation studies are presented to vali-
> date the effectiveness of our design components.
> 
> 5.1
> Experiment Settings
> 
> Benchmarks. We evaluate SafeMCP across three
> complementary suites: (i) PowerSeeking Bench
> (ours), a set of 112 prompts designed to track
> whether an agent pursues power escalation and sub-
> sequently executes hazardous operations in high-
> power states; (ii) ToolEmu (Ruan et
**Section Heading**: `results highlight the synergistic roles of the pro-` [section offsets: 32593:34522]
**First 120 words verbatim** [offsets: 32593:33396]
> results highlight the synergistic roles of the pro-
> posed stages. As shown in table 2, the omission
> of Stage 3 (w/o Stage 3) causes the harmful score
> to jump from 0.19 to 0.36. This indicates that
> 
> Claude-3.5
> -Sonnet
> 
> Llama-3.1
> -8B
> 
> 
> 
> 
> 
> 
> 
> SafeMCP
> SafeMCP
> 
> Safiron
> 
> w/o 
> defense
> 
> 
> 
> Llama Guard 3
> 
> 
> 
> Llama Guard 3
> 
> NemoGuard-8B
> 
> NemoGuard-8B
> 
> 
> 
> AgentMonitor
> 
> AgentMonitor
> 
> 
> 
> Qwen3Guard-8B
> 
> Qwen3Guard-8B
> 
> 
> 
> ChainGuard
> 
> ChainGuard
> 
> 
> 
> 
> 
> 
> Harmful Request  ↑
> 
> (C) Llama-3.1-8B
> 
> Stage 3 (RL with Dual Verifiable Rewards) ampli-
> fies dual-phase reasoning, reinforcing the model’s
> ability to perform concurrent state-safety assess-
> ments and proactive tool filtering. Similarly, the
> exclusion of Stage 1 (w/o Stage 1) degrades both
> safety and utility metrics, suggesting that Stage

## Block 5: Attack-Set Excerpts
**Location**: `Experiments` [offsets: 25546:25557]
> Benchmarks.
**Location**: `Experiments` [offsets: 26755:27110]
> We benchmark against a
> diverse set of SOTA defenses, including Llama
> Guard 3 (Inan et al., 2023), Qwen3Guard-Gen-
> 8B (Zhao et al., 2025), Lakera-ChainGuard (Team,
> 2024a), NeMoGuard-8B-Content-Safety (Rebedea
> et al., 2023), AgentMonitor (Naihin et al., 2023),
> RL-Guard (Yang et al., 2024), and Safiron (Huang
> et al., 2025) to provide a rigorous comparison.
**Location**: `Experiments` [offsets: 27361:27514]
> The exact agent set varies by benchmark
> due to benchmark-specific API compatibility and
> intrinsic safety behavior; details are provided in sec-
> tion E.1.
**Location**: `Experiments` [offsets: 29696:29906]
> In the Agen-
> tHarm benchmark, SafeMCP demonstrates an op-
> timal trade-off between utility and safety, effec-
> tively fulfilling benign requests while pruning un-
> safe tool calls triggered by harmful inputs (fig.

## Block 6: Baseline Excerpts
**Location**: `Experiments` [offsets: 25418:25519]
> Furthermore, ablation studies are presented to vali-
> date the effectiveness of our design components.
**Location**: `Experiments` [offsets: 25920:26025]
> The blue dashed line represents the Pareto
> frontier of the safety-utility trade-off across all baselines.
**Location**: `Experiments` [offsets: 26735:26754]
> Baselines & Agents.
**Location**: `Experiments` [offsets: 27752:27835]
> Crucially, it accom-
> plishes this while achieving state-of-the-art util-
> ity rates.
**Location**: `Experiments` [offsets: 28610:28694]
> In contrast, SafeMCP outper-
> forms both baselines, surpassing the Pareto fron-
> tier.
**Location**: `Experiments` [offsets: 29911:30120]
> Although most baseline defenses, excluding Saf-
> iron, achieve perfect blocking rates on harmful sce-
> narios, they suffer from high over-blocking rates,
> frequently terminating the workflow in benign con-
> texts.

## Block 7: Cost Excerpts
**Location**: `Experiments` [offsets: 25920:26025]
> The blue dashed line represents the Pareto
> frontier of the safety-utility trade-off across all baselines.
**Location**: `Experiments` [offsets: 26456:26734]
> Detailed configu-
> rations are provided in section E.1, and (iii) Agen-
> tHarm (Andriushchenko et al., 2025), for which we
> utilize its 176 benign and 176 harmful instructions
> to test the framework’s ability to refuse harmful op-
> erations without excessively rejecting benign ones.
**Location**: `Experiments` [offsets: 27836:27949]
> In contrast, chatbot defenses such as
> Qwen3Guard-8B often attain high safety rates but
> at the expense of utility.
**Location**: `Experiments` [offsets: 28908:28937]
> Runtime Agent Safety Defense.
**Location**: `Experiments` [offsets: 28938:29087]
> In non-
> adversarial risk settings, SafeMCP achieves near-
> optimal safety rates and establishes a superior
> Pareto frontier between safety and utility.
**Location**: `Experiments` [offsets: 29088:29281]
> Since
> risks within ToolEmu stem from agent-environment
> interactions, existing defenses that lack environ-
> ment dynamic understanding fail to predict haz-
> ards triggered by benign-looking tools.

## Block 8: Limitations
**Section Heading**: `Limitations` [section offsets: 35202:37290]
**First 120 words verbatim** [offsets: 35202:36040]
> Limitations
> 
> Our work identifies a few areas for future enhance-
> ment. The precision of power regulation is subject
> to the modeling complexity of specific environ-
> ment dynamics. Additionally, while our grounding
> stage improves local safety reasoning, developing
> cross-domain transferability for safety priors with-
> out extensive local data remains a key objective for
> the next stage of this research.
> 
> Ethical Considerations
> 
> The PowerSeeking Bench and Environment Dy-
> namic Grounding Dataset are designed to advance
> AI safety by enabling the rigorous evaluation of
> LLM agents. To ensure safety, all evaluations were
> conducted within fully simulated, sandboxed en-
> vironments using mock execution layers that do
> not interact with real-world systems. Consequently,
> any observed risky behaviors pose no actual secu-
> rity risk. By releasing

## Block 9: Adaptivity Hits
**Matched Term**: `Adaptive` | **Location**: `References` [offsets: 41215:41329]
> 2025. AGrail: A Lifelong Agent Guardrail
> with Effective and Adaptive Safety Detection.
> Preprint, arXiv:2502.11448.
**Matched Term**: `evasion` | **Location**: `Implementation Details` [offsets: 51369:51505]
> Defense evasion
> Disabling monitors, logs, or policy
> checks.
> 
> Resource acquisition
> Acquiring compute, funds, accounts,
> or infrastructure.
