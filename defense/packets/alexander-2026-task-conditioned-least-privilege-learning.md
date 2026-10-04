# Evidence Locator Packet: alexander-2026-task-conditioned-least-privilege-learning

- **Title**: Task-Conditioned Least-Privilege Learning for Executable Terminal and MCP Agents
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2608.18351
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\alexander-2026-task-conditioned-least-privilege-learning\fulltext.txt
- **Character Count**: 48654

## Block 2: Contribution Sentences
**Location**: `Abstract—Tool-using large language-model agents can` [offsets: 689:819]
> We propose a framework
> where each action is audited before execution and again
> from observed effects along six dimensions of risk.
**Location**: `Abstract—Tool-using large language-model agents can` [offsets: 1157:1296]
> We find that after training
> using this framework on Qwen3.5-4B over 1,500 tasks,
> the selected seed reaches 98.48% safe success across 2,896
**Location**: `I. INTRODUCTION` [offsets: 4315:5128]
> we propose to have the model
> learn to exercise least-privilege actions that still provide
> sufficient evidence to finish the task.
> 
> To study this, we define how that least privilege is
> task-relative. We use three different metrics to help judge
> what task specific authority is necessary for tool-using
> agents. These include what capabilities are shown to
> the model, what actions the environment permits, and
> what actual authority and effect happens. The model
> sees a comprehensive tool inventory, while an unseen
> environment broker parses each proposed action, deter-
> ministically calculates its intended authority, assesses its
> 
> --- PAGE BREAK ---
> 
> execution risk, selects the execution mode, and records
> the resulting effects. This structure lets us assign each
> task a sufficient-authority envelope, and penalize

## Block 3: Method Locator
**Section Heading**: `III. METHODOLOGY` [section offsets: 10966:10984]
**First 120 words verbatim** [offsets: 10966:11747]
> III. METHODOLOGY
> 
> A. Task Relative Authority
> 
> For task x, the visible actions are a terminal command,
> an MCP call, a categorical human escalation, and a final
> answer. Their sequence forms τ = (a1, o1, . . . , aT , oT ).
> Each action receives a six-dimensional authority vector
> 
> z(at) = [zwrite, zexec, zexternal,
> 
> zsecret, zscope, zpersistent] ∈[0, 1]6.
> (1)
> 
> The components correspond to state mutation, dynamic
> execution, reaches or exceeds the environment bound-
> ary, unprivileged sensitive-data access, broad and wide
> effects, and state that persists beyond the intended oper-
> ation. The risk vector is the componentwise maximum
> between the pre- and post-action risk assessments. The
> final trajectory risk vector then records the largest value
> reached on each authority dimension
**Section Heading**: `C. Modular Framework Use` [section offsets: 13875:15133]
**First 120 words verbatim** [offsets: 13875:14639]
> C. Modular Framework Use
> 
> The framework’s separation of broker, task schemas,
> post-action verifiers and excess privilege calculation are
> separated to allow for handling tasks that have different
> behavior and needs. Consider a proposal task that only
> asks an agent to read a bug report, bug.txt and suggest
> a patch. Here, a simple read is sufficient while a write
> would be classified as excessive. Pre-action brokers do,
> however, require evidence terms because no mutative
> action is executed by the agent in the correct run. On the
> other hand, a multi-tool cross-service task that requires
> an agent to read from a GitHub-like service using MCP
> tools and copy that information into a separate database
> row requires elevated sufficient privilege envelopes in
> external

## Block 4: Evaluation Locator
**Section Heading**: `evaluation episodes spanning all 500 held-out tasks, com-` [section offsets: 1297:2147]
**First 120 words verbatim** [offsets: 1297:2213]
> evaluation episodes spanning all 500 held-out tasks, com-
> pared with 64.36% for the base policy, and reduces excess-
> authority error events from 4.56% to 0.79%. Further-
> more, external tests show capability retention and prompt-
> directed improvement. A 400 task continuation study also
> found evidence of generalization, reducing excess-authority
> events by 6.99 percentage points while maintaining previous
> capabilities. We conclude learned restraint through least-
> privilege aware post-training is therefore useful as an
> additional control layer for tool-using agents in executable
> terminal and MCP environments, but it does not replace
> permission gates and sandboxing.
> 
> Index Terms—language-model agents, least privilege,
> permission gates, tool use, reinforcement learning, ex-
> ecutable environments, MCP, terminal agents, excess-
> authority errors
> 
> I. INTRODUCTION
> 
> Tool-using agents can successfully complete tasks
**Section Heading**: `evaluation covers ten frontier models like GPT-5.5 and` [section offsets: 7968:10966]
**First 120 words verbatim** [offsets: 7968:8888]
> evaluation covers ten frontier models like GPT-5.5 and
> Claude Opus 4.7 across three domains and finds sub-
> stantial over-privilege. Errors increase under real-world
> conditions such as incomplete requests, convenience-
> oriented wording, and tasks that are not cleanly defined.
> These findings indicate that improved general capability
> does not itself produce reliable authority control or risk
> judgment.
> 
> A contemporaneous study, ToolPrivBench, is the clos-
> est prior post-training comparison [7]. It makes lower-
> and higher-privilege tools independently sufficient, and
> measures whether an agent selects a higher-privilege tool
> initially or escalates after transient lower-tier failures.
> Its privilege-aware post-training method reduces unnec-
> essary higher-privilege selection while retaining general
> tool ability. ToolPrivBench appeared while our experi-
> mental program was already in progress. It informed our
> external
**Section Heading**: `E. Tasks and Evaluation` [section offsets: 17222:20739]
**First 120 words verbatim** [offsets: 17222:17990]
> E. Tasks and Evaluation
> 
> We authored a task catalog of 2000 separate tasks
> as seen in Table I. These are subdivided into 1,500
> training tasks, 300 validation variants that are within
> training families (the within validation set partition),
> and 200 tasks from the families which are not included
> in the training pool (the excluded family validation set
> partition). The 300 within validation tasks are primarily
> to prevent explicit reward hacking and to validate the
> training gains. By contrast, the excluded task families
> are used to test if the learned least-privilege carries to
> new task structures under the same brokered terminal and
> MCP environment. These tasks combined form the total
> validation of 500 tasks. The curriculum covers targeted
> reading, code changes,
**Section Heading**: `IV. EXPERIMENTAL RESULTS AND DISCUSSION` [section offsets: 20739:20780]
**First 120 words verbatim** [offsets: 20739:21487]
> IV. EXPERIMENTAL RESULTS AND DISCUSSION
> 
> A. Internal Results
> 
> Of the three seeds initially trained, we selected the
> most stable, Seed 1 using the routine 206 task evaluation
> set before running the complete 500-task and external
> evaluations. Safe success on the routine task set was
> 85.98%, 97.63%, and 86.29% for seeds 0, 1, and 2,
> respectively. We tested the complete evaluation 500
> validation set with both policies, each receiving the same
> exact system prompt, tool inventory, broker system, and
> deterministic verifiers. Table II compares how the base
> and trained policies act and compare to each other in our
> 500 least-privilege aware task validation set.
> As seen, the trained Seed 1 produces 988 more safe
> episodes than the base policy and 109

## Block 5: Attack-Set Excerpts
**Location**: `evaluation covers ten frontier models like GPT-5.5 and` [offsets: 9397:9480]
> General tool-use benchmarks provide capability com-
> parisons and informative tasks.
**Location**: `C. External Evaluation by Independent Benchmarks` [offsets: 24843:25000]
> External Evaluation by Independent Benchmarks
> 
> Table IV shows results on two independent bench-
> marks that were not used to select the training check-
> point.
**Location**: `C. External Evaluation by Independent Benchmarks` [offsets: 25805:25843]
> TABLE IV
> INDEPENDENT BENCHMARK RESULTS
**Location**: `E. Continuation Study Results` [offsets: 28617:28767]
> The original 1,500 seed run performs well with the
> internal validation set but it does not have as marked
> of an improvement in the external benchmark.
**Location**: `E. Continuation Study Results` [offsets: 30392:30536]
> We used
> a held-out validation set of 50 tasks based on the 400
> mixed task set to monitor the results along with the
> standard internal benchmark.
**Location**: `E. Continuation Study Results` [offsets: 30770:30943]
> For other
> external benchmarks such as MetaTool and FORTIS, we
> also did not observe any statistically significant changes
> in overall results, suggesting capability retention.

## Block 6: Baseline Excerpts
**Location**: `E. Tasks and Evaluation` [offsets: 19087:19256]
> For internal checkpoint evaluations and ablation, we
> use a smaller routine evaluation subset of these 500
> tasks containing 206 tasks sampled over 8 generations
> per task.
**Location**: `A. Internal Results` [offsets: 22059:22202]
> On the complete
> 200-task whole-family-heldout partition, seed 1 records
> 1,020/1,020 safe episodes, compared with 689/1,020 for
> the base policy.
**Location**: `A. Internal Results` [offsets: 22203:22298]
> On the unseen-MCP family, seed 1
> records 440/440 safe episodes, compared with 220/440
> for base.
**Location**: `C. External Evaluation by Independent Benchmarks` [offsets: 25450:25609]
> Base
> Seed 1
> Prompt Ablation Results
> 
> 100
> 
> 90
> 
> Safe-success rate (%)
> 
> 80
> 
> 70
> 
> 60
> 
> 50
> 
> Full Prompt
> No Security Add Prompt
> One-line prompt
> 
> Prompt condition
> 
> Fig.
**Location**: `C. External Evaluation by Independent Benchmarks` [offsets: 25657:25770]
> Seed 1 changes by
> 0.24 percentage points across the three prompts, compared with 3.70
> points for the base policy.
**Location**: `Evaluation` [offsets: 26072:26157]
> On MetaTool, seed 1 answers 836 of 1,000 items
> correctly, compared with 819 for base.

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
**Section Heading**: `V. LIMITATIONS AND FUTURE WORK` [section offsets: 37061:40967]
**First 120 words verbatim** [offsets: 37061:37907]
> V. LIMITATIONS AND FUTURE WORK
> There are limitations to the study and we acknowledge
> that the tasks are largely synthetically generated from
> structured families with clear, pre-defined grouping and
> testing patterns. This means that while whole-family
> holdouts and template-group checks reduce construction
> and cross-family dependence, they do not establish per-
> formance on unrestricted production repositories or ser-
> vices. The authority dimensions, weights, and sufficient
> envelopes encode judgments that may not be completely
> correct, though as we have taken measures to reduce
> 
> this by having a detailed risk archive justification section
> for each task. Furthermore, the study only uses one 4B
> model and one adapter family, though previous research
> works suggest representation level similarities between
> large language model families and in

## Block 9: Adaptivity Hits
no hits
