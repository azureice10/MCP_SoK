# Evidence Locator Packet: suliu-2026-airguard-guarding-agent-actions-runtime

- **Title**: AIRGuard: Guarding Agent Actions with Runtime Authority Control
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2605.28914
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\suliu-2026-airguard-guarding-agent-actions-runtime\fulltext.txt
- **Character Count**: 48736

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 725:832]
> We present
> AIRGuard, a runtime guard that operational-
> izes least privilege as action-time authoriza-
> tion.
**Location**: `Introduction` [offsets: 7775:8627]
> Our contributions are:
> 
> 1. We identify authority confusion as a runtime
> failure mode distinct from jailbreaks, prompt
> injection, and parameter provenance.
> 
> --- PAGE BREAK ---
> 
> 2. We introduce an authority-risk model for
> agent actions: capability mapping, authority
> inheritance, resource and target trust, source
> trust pools, side-effect simulation, tiered en-
> forcement, and sequence audit.
> 
> 3. We report results on AgentTrap (Zhuang et al.,
> 2026) and DTAP-150 (Chen et al., 2026), in-
> cluding security-utility tradeoffs and failure
> analysis that should guide future authority-
> aware defenses.
> 
> 2
> Problem Formulation
> 
> 2.1
> Threat Model
> 
> We study a tool-using agent that receives a task, ob-
> 
> serves content from multiple runtime channels, and
> proposes side-effecting tool actions. Let C denote
> this channel vocabulary, including user-facing text,
> copied

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
**Section Heading**: `3. We report results on AgentTrap (Zhuang et al.,` [section offsets: 8167:20592]
**First 120 words verbatim** [offsets: 8167:8969]
> 3. We report results on AgentTrap (Zhuang et al.,
> 2026) and DTAP-150 (Chen et al., 2026), in-
> cluding security-utility tradeoffs and failure
> analysis that should guide future authority-
> aware defenses.
> 
> 2
> Problem Formulation
> 
> 2.1
> Threat Model
> 
> We study a tool-using agent that receives a task, ob-
> 
> serves content from multiple runtime channels, and
> proposes side-effecting tool actions. Let C denote
> this channel vocabulary, including user-facing text,
> copied instructions, shared documents, webpages,
> retrieved files, tool or MCP outputs, memory en-
> tries, local files, packages, scripts, plugins, skills,
> generated code, and downloaded dependencies. At
> step i, the agent has observed a trajectory prefix
> 
> Hi = {(cj, xj)}j≤i,
> cj ∈C,
> 
> where xj is the content observed from channel cj.
> Let g denote the
**Section Heading**: `Evaluation` [section offsets: 20592:28698]
**First 120 words verbatim** [offsets: 20592:21485]
> Evaluation
> 
> 4.1
> Experiment Setup
> 
> Models. The main AIRGuard runs use Claude
> Haiku 4.5 and Claude Sonnet 4.6 through native
> CLI agent integrations. We additionally report a
> prompt-only ablation with GPT-5.4-mini through
> Codex CLI on DTAP-150. The prompt-only setting
> prepends the AIRGuard policy to the model prompt
> and requests diagnostic decisions, but it does not
> enforce tool calls in code.
> 
> Datasets. We evaluate AIRGuard on two bench-
> marks. AgentTrap contains 141 cases: 91 mali-
> cious authority-confusion attacks and 50 benign
> tasks. The attacks cover data exfiltration, system
> integrity, prompt injection, config poisoning, re-
> source abuse, content-safety bypass, output tamper-
> ing, unauthorized disclosure, code injection, mis-
> information, cross-skill collusion, steganographic
> payloads, supply-chain attacks, MCP abuse, privi-
> lege escalation, and autonomous enrollment.
> 
> DTAP-150

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 20987:20996]
> Datasets.
**Location**: `Evaluation` [offsets: 21656:21713]
> We use a unified security–utility view
> across benchmarks.
**Location**: `Evaluation` [offsets: 23564:23704]
> AIRGuard also preserves more be-
> nign task utility than the external defenses on
> DTAP-150, the benchmark where over-defense is
> most visible.

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 20739:20833]
> We additionally report a
> prompt-only ablation with GPT-5.4-mini through
> Codex CLI on DTAP-150.
**Location**: `Evaluation` [offsets: 22094:22104]
> Baselines.
**Location**: `Evaluation` [offsets: 22380:22493]
> We also include a prompt-only AIRGuard ablation
> 
> on DTAP-150 to separate policy prompting from
> runtime mediation.
**Location**: `Evaluation` [offsets: 22962:23149]
> The same pat-
> tern holds for GPT agents: AIRGuard achieves
> 8.8% ASR with GPT-5.4-mini and 9.9% with GPT-
> 5.3-codex, compared with 18.7% and 26.4% for
> MELON, and 22.0% and 25.3% for ARGUS.
**Location**: `Evaluation` [offsets: 27476:27521]
> Table 2:
> DTAP-150 ablation with GPT-5.4-mini.
**Location**: `Evaluation` [offsets: 28023:28121]
> 4.3
> Ablation and Baselines
> 
> Table 2 asks whether AIRGuard can be reduced
> to a prompt-level policy.

## Block 7: Cost Excerpts
**Location**: `3. We report results on AgentTrap (Zhuang et al.,` [offsets: 8170:8368]
> We report results on AgentTrap (Zhuang et al.,
> 2026) and DTAP-150 (Chen et al., 2026), in-
> cluding security-utility tradeoffs and failure
> analysis that should guide future authority-
> aware defenses.
**Location**: `3. We report results on AgentTrap (Zhuang et al.,` [offsets: 8466:8554]
> serves content from multiple runtime channels, and
> proposes side-effecting tool actions.
**Location**: `3. We report results on AgentTrap (Zhuang et al.,` [offsets: 9536:9681]
> The at-
> tacker’s goal is to influence the agent at runtime
> so that the agent uses its own authorized access
> to perform unauthorized side effects.
**Location**: `3. We report results on AgentTrap (Zhuang et al.,` [offsets: 9682:9802]
> We do not
> model direct compromise of the protected runtime
> policy or out-of-band tool execution that bypasses
> the agent.
**Location**: `3. We report results on AgentTrap (Zhuang et al.,` [offsets: 10031:10124]
> We assume the
> runtime can observe proposed tool calls or wrap
> 
> tool servers before execution.
**Location**: `3. We report results on AgentTrap (Zhuang et al.,` [offsets: 11619:11829]
> The runtime should enforce the following invariant:
> 
> A side-effecting action is legitimate only
> when its target and expected effect are
> justified by the task and policy, not
> merely suggested by runtime context.

## Block 8: Limitations
**Section Heading**: `Limitations` [section offsets: 32844:34096]
**First 120 words verbatim** [offsets: 32844:33643]
> Limitations
> 
> AIRGuard is not a prompt-only defense, so it is
> not automatically portable to every agent frame-
> work. It must observe and mediate proposed ac-
> tions before execution, which requires integration
> with the specific tool runtime, CLI loop, MCP
> proxy, browser controller, or API wrapper used
> by the agent. Frameworks that expose structured
> tool calls can be supported with a normalization
> adapter, but frameworks that hide side effects in-
> side tool servers, execute generated code outside
> the guard, or bypass a pre-action hook require struc-
> tural changes before AIRGuard can enforce its pol-
> icy.
> 
> Ethics Statement
> 
> This work studies attacks in controlled benchmark
> environments and does not provide new operational
> exploit code beyond benchmark tasks already de-
> signed for agent-safety

## Block 9: Adaptivity Hits
no hits
