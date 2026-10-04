# Evidence Locator Packet: mehrdad-2026-trustshiftprobe-characterizing-benchmarking-defending-staged

- **Title**: TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2608.23763
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\mehrdad-2026-trustshiftprobe-characterizing-benchmarking-defending-staged\fulltext.txt
- **Character Count**: 61973

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged as` [offsets: 1534:2317]
> We introduce TrustShiftProbe, an evaluation
> and defense framework with four contributions: (1) a stateful
> temporal threat model of the agent–server lifecycle as a benign
> conditioning phase followed by an adversarial defection at a trust
> horizon; (2) a language-agnostic attack engine that instantiates
> each variant as a compromised MCP server across four produc-
> tion domains; (3) SHIELD, a multi-tier, zero-oracle runtime de-
> fense at the MCP transport boundary that audits server payloads
> against behavioral baselines learned during clean trust windows;
> and (4) a taxonomy of nine TrustShift variants spanning three
> execution mechanisms (structural violation, semantic corruption,
> scope expansion) and three adversarial objectives (disruption,
> exfiltration, and their combination).

## Block 3: Method Locator
**Section Heading**: `V. TRUSTSHIFT FRAMEWORK` [section offsets: 23001:23026]
**First 120 words verbatim** [offsets: 23001:23840]
> V. TRUSTSHIFT FRAMEWORK
> 
> A. Automated Adversarial Task Generation
> 
> Evaluating agents against temporally-staged TrustShift at-
> tacks requires a task set that is both large and structurally
> valid at every point in the taxonomy. Hand-authoring multi-
> hop adversarial scenarios across the mechanism–trigger cells
> of our taxonomy and four application domains does not scale
> and is prone to annotator bias. We therefore synthesize tasks
> with an automated red-teaming pipeline in the spirit of Perez
> et al. [47]: a high-capability generator (the Red LM, GPT-
> 4o) proposes tasks, while three constraints enforce construct
> validity and schema conformance (Figure 2).
> 
> 1) Stage
> 1:
> Schema-Constrained
> Generation:
> Uncon-
> strained generation of adversarial payloads frequently violates
> the JSON-RPC schema and invalidates a run. We condition
> the Red LM

## Block 4: Evaluation Locator
**Section Heading**: `results into its reasoning context via the MCP client layer,` [section offsets: 13072:16314]
**First 120 words verbatim** [offsets: 13072:13841]
> results into its reasoning context via the MCP client layer,
> and eventually produces a final answer. The MCP protocol
> boundary sits between the AUT’s tool-calling layer and the
> server implementation; the AUT, the user goal, and the tool
> schemas are trusted, while the results crossing that boundary
> are not.
> 
> Attacker model. The attacker controls a single MCP server.
> This models three realistic deployment scenarios: (i) a legiti-
> mate server compromised after approval (supply-chain attack);
> (ii) a malicious server masquerading as a useful utility; or
> (iii) a legitimate server silently updated after approval with
> hidden logic [9], [24]. Common to all three is a trust shift:
> a counterparty that is honest at admission time defects later,
> once it has accrued trust.
**Section Heading**: `VI. EVALUATION METHODOLOGY AND CORE METRICS` [section offsets: 26092:28191]
**First 120 words verbatim** [offsets: 26092:26856]
> VI. EVALUATION METHODOLOGY AND CORE METRICS
> 
> We score each session with a short, deterministic pipeline
> rather than a single all-in-one LLM judge (which is prone to
> surface-level bias), combining tool-call telemetry and answer-
> level fact-checking.
> 
> A session is exposed if the agent invoked the targeted
> tool past the trust horizon N and consumed the adversarial
> response; unexposed runs carry no attack and are excluded.
> On the exposed set, ASRi = 1 when the final answer adopts
> the server’s adversarial value and ASRi = 0 when the agent
> 
> --- PAGE BREAK ---
> 
> Fig. 2. Three-stage Red-LM task-generation pipeline. A high-capability generator (Red LM; GPT-4o) proposes tasks under three constraints: Stage 1 restricts
> generation to the domain schema and the M1–M3 ×
**Section Heading**: `VIII. EVALUATION AND RESULT` [section offsets: 34117:34146]
**First 120 words verbatim** [offsets: 34117:34904]
> VIII. EVALUATION AND RESULT
> 
> A. Model Setup
> 
> Models. We evaluate six LLM agents spanning proprietary
> and open-weight families: GPT-5, GPT-4.1, and o4-mini
> (OpenAI), Claude-Opus-4-8 (Anthropic), Grok-4.3 (xAI), and
> Qwen3.5 Flash (Alibaba). Every model is driven through
> the identical ReAct agent loop with the same task pool, tool
> backends, and SHIELD configuration, so differences reflect
> the model rather than the harness. Decoding uses temperature
> 
> Tier 3: Semantic
> 
> 200–800 ms
> ·
> LLM, optional
> 
> 3a
> Task goal + tool arguments
> 
> PASS
> result →agent
> 
> 3b
> Trust-phase exemplar
> reference
> 
> 3c
> LLM plausibility assessment
> 
> 3d
> No ground-truth access
> 
> =
> 0 for reproducibility (top p left at each provider’s
> default of 1.0, max output tokens =
> 4096, step budget
> = 15 tool calls); models that do not
**Section Heading**: `C. Results and Findings` [section offsets: 35991:43674]
**First 120 words verbatim** [offsets: 35991:36718]
> C. Results and Findings
> 
> Table III reports ASR (%) by task domain and Table IV
> by TrustShift attack variant, both before and after SHIELD.
> We analyze the latter per variant and summarize the attack
> performance in Figure 4.
> 
> a) Finding 1: TrustShift subverts every frontier model.:
> No model is robust. The base ASR ranges from 60.2% (GPT-5)
> to 74.1% (GPT-4.1), with an overall mean of 69.5% (Table III).
> Even the most resistant model is deceived on roughly three
> 
> --- PAGE BREAK ---
> 
> TABLE III
> ASR (%) ON TRUSTSHIFTPROBE ACROSS DOMAINS AND ALL TASKS BEFORE AND AFTER DEFENSE (SHIELD). LOWER IS BETTER. EXACT MODEL
> 
> Model
> Location
> Navigation
> 
> Repository
> Management
> 
> GPT-5
> 61.6
> 56.6
> 49.4
> 48.9
> 64.4
> 33.3
> 65.4
> 23.1
> 60.2
> 40.7
> GPT-4.1

## Block 5: Attack-Set Excerpts
**Location**: `results into its reasoning context via the MCP client layer,` [offsets: 16093:16292]
> All exfiltration is realized through a simulated
> sink—a sentinel token and a placeholder destination—so no
> real secret or file is ever accessed, and the benchmark is safe
> to distribute and reproduce.
**Location**: `E. Guarding Against Evaluation-Artifact Leakage` [offsets: 48649:48812]
> A defense evaluated against a benchmark’s own attack
> instrumentation risks reporting a detection rate that reflects
> recognizing the harness rather than the threat.

## Block 6: Baseline Excerpts
**Location**: `VI. EVALUATION METHODOLOGY AND CORE METRICS` [offsets: 27409:27519]
> without defense (Base) and with SHIELD (+SHIELD); the
> reduction ASR−ASR+SHIELD measures defense effectiveness.
**Location**: `C. Results and Findings` [offsets: 40971:41090]
> Large, many-field repository payloads give omission
> and drift attacks more cover and make behavioral baselines
> noisier.
**Location**: `C. Results and Findings` [offsets: 43190:43423]
> Thus, although individual variants such as Tool-Scope
> Escalation have low baseline exposure due to the agents’
> natural refusal rates, the M3 mitigation is significant at the
> family level rather than an artifact of small-sample noise.

## Block 7: Cost Excerpts
**Location**: `results into its reasoning context via the MCP client layer,` [offsets: 13440:13713]
> This models three realistic deployment scenarios: (i) a legiti-
> mate server compromised after approval (supply-chain attack);
> (ii) a malicious server masquerading as a useful utility; or
> (iii) a legitimate server silently updated after approval with
> hidden logic [9], [24].
**Location**: `results into its reasoning context via the MCP client layer,` [offsets: 14195:14373]
> Runtime
> Injection
> 
> Runtime
> 
> turn
> 
> Staging
> 
> Defense
> 
> Activation depends only on elapsed interaction state, not
> on any keyword, argument value, or syntactic pattern in
> the request.
**Location**: `results into its reasoning context via the MCP client layer,` [offsets: 14214:14373]
> Runtime
> 
> turn
> 
> Staging
> 
> Defense
> 
> Activation depends only on elapsed interaction state, not
> on any keyword, argument value, or syntactic pattern in
> the request.
**Location**: `results into its reasoning context via the MCP client layer,` [offsets: 14374:14629]
> During the conditioning phase the server
> is behaviorally indistinguishable from a benign one;
> the setting N=0 recovers the classical always-malicious
> server, and any N>0 evades provisioning-time and static
> vetting, which can only observe the honest phase.
**Location**: `results into its reasoning context via the MCP client layer,` [offsets: 14971:15205]
> The attacker cannot modify
> the AUT’s system prompt, manipulate the user’s initial
> instructions, intercept traffic destined for other benign
> MCP servers, or observe the AUT’s internal hidden rea-
> soning (e.g., chain-of-thought traces).
**Location**: `C. Results and Findings` [offsets: 37095:37293]
> Because a cold, first-call version of the same
> manipulation is far easier to refuse, this level of success is
> direct evidence that the benign trust phase, not the payload, is
> what disarms the agent.

## Block 8: Limitations
**Section Heading**: `Limitations of Existing Benchmarks. Despite the severity of` [section offsets: 5274:7288]
**First 120 words verbatim** [offsets: 5274:6170]
> Limitations of Existing Benchmarks. Despite the severity of
> this threat, current safety-evaluation suites have three limita-
> tions:
> 
> --- PAGE BREAK ---
> 
> 1) Fragmentary Attack Surface Coverage: benchmarks test
> static, single-shot attacks (e.g., SHADE-Arena [2],
> SafeMCP [28]) or stage time-based scenarios as isolated
> scripts with fixed payloads (e.g., MCP-SafetyBench’s
> Rug-Pull [25]), lacking a systematic taxonomy of ex-
> ecution mechanisms.
> 2) Coarse Outcome Granularity: prior suites (e.g., MCP-
> Tox [26], MCIP-Bench [29]) report post-hoc binary
> success, not temporal trajectory divergence, or when the
> agent’s context window becomes compromised.
> 3) Absence of Zero-Oracle Runtime Defenses: they evaluate
> security in isolation without runtime defenses, prevent-
> ing a holistic assessment of how effectively transport-
> layer monitors can detect and mitigate these threats
> during live execution.

## Block 9: Adaptivity Hits
**Matched Term**: `evasion` | **Location**: `Abstract—The Model Context Protocol (MCP) has emerged as` [offsets: 666:1311]
> This openness introduces a
> severe server-side threat we term TrustShift: a compromised MCP
> server behaves benignly during an initial conditioning phase,
> building operational reliance and suppressing agent skepticism,
> before switching to an adversarial payload once an interaction
> threshold is reached. The evasion is temporal, not syntactic:
> benign at deploy time, the server’s defection is invisible to pre-
> deployment static analysis, which sees only the honest phase.
> Switched payloads range from overt structural violations to
> schema-valid manipulations, the latter preserving outer proto-
> col compliance to evade runtime middleware filters.
**Matched Term**: `evade` | **Location**: `Abstract—The Model Context Protocol (MCP) has emerged as` [offsets: 968:1533]
> The evasion is temporal, not syntactic:
> benign at deploy time, the server’s defection is invisible to pre-
> deployment static analysis, which sees only the honest phase.
> Switched payloads range from overt structural violations to
> schema-valid manipulations, the latter preserving outer proto-
> col compliance to evade runtime middleware filters. Crucially,
> TrustShift originates in the server-controlled tool channel, not
> user prompts (unlike indirect prompt injection) or the transport
> (unlike man-in-the-middle): the adversary is the trusted server
> endpoint itself.
**Matched Term**: `evade` | **Location**: `I. INTRODUCTION` [offsets: 3262:4193]
> MCP’s rapid adoption exposes agents
> to an unvetted server-side attack surface [33]: because agents
> dynamically invoke third-party tools without runtime integrity
> verification [24], a compromised server can manipulate an
> agent’s execution trajectory [21]. We term this exploitation
> TrustShift: a compromised MCP server behaves benignly dur-
> ing an initial trust phase, building operational reliance and
> suppressing the agent’s contextual skepticism; upon reaching
> an interaction threshold, it defects, injecting adversarial pay-
> loads that preserve outer application-layer schema compliance
> to evade static middleware filters [9]. TrustShift is distinct on
> two axes: (1) Channel Origin: payloads originate within the
> server-controlled JSON-RPC tool channel, not user prompts
> or network transport; (2) Temporal Staging: the server stays
> benign during deployment testing, defeating pre-execution
> static analysis and manifest scanners.
**Matched Term**: `evasion` | **Location**: `B. Server-Side Attacks on MCP` [offsets: 9940:10615]
> The vulnerability land-
> scape of LLM tool environments was established by Beurer-
> Kellner and Fischer [9], who first characterized static Tool
> Poisoning Attacks (TPA) and shadow tool registration. This
> framework was subsequently extended along static vectors,
> including multi-hop downstream state subversion [19], host-
> level privilege escalation through untrusted terminal bound-
> aries [20], and cross-tool permission containment evasion [22].
> 
> As delineated in Table I, existing evaluations treat tool com-
> promise as a zero-shot, static injection in which the payload
> P is delivered deterministically at t = 1; they neither model
> nor evaluate against TrustShift paradigms.
**Matched Term**: `evade` | **Location**: `A. Taxonomy Structure` [offsets: 17739:18201]
> 1) M1: Structural Violation: Unlike traditional network
> attacks that break JSON syntax, M1 attacks explicitly maintain
> application-layer schema compliance to evade static middle-
> ware security filters. The structural violation occurs entirely at
> the informational layer: while maintaining outer schema va-
> lidity, the compromised server maliciously removes, truncates,
> or nullifies expected internal keys, arrays, or objects to starve
> the agent’s context window.
**Matched Term**: `evade` | **Location**: `A. Taxonomy Structure` [offsets: 22668:23003]
> Objective:
> O1: Disruption
> O2: Exfiltration
> O3: Combined
> 
> • Cross-Tool Lateral Movement: A stateful fragmentation
> attack where the server distributes its exfiltration across
> a prolonged series of agent invocations [49], sequentially
> gathering small pieces of tokens or data to successfully
> evade payload-size security monitors [10].
> 
> V.
**Matched Term**: `adaptive` | **Location**: `X. CONCLUSION AND FUTURE WORK` [offsets: 49756:50419]
> We observe
> that and mechanism-dependent susceptibility, and show that
> SHIELD, our oracle-free transport-layer defense, meaningfully
> reduces deception-style attacks while remaining structurally
> unable to prevent (only detect) pure denial-of-service defec-
> tions: an integrity–availability asymmetry we argue is in-
> herent to any ground-truth-free monitor, not an artifact of
> our implementation. Natural extensions include multi-server
> coordinated attacks, adaptive adversaries that tune their drift
> rate against SHIELD’s own baseline window, and defenses that
> move beyond purely oracle-free detection toward lightweight
> verification. We leave these to future work.
