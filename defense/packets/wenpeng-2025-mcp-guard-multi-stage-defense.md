# Evidence Locator Packet: wenpeng-2025-mcp-guard-multi-stage-defense

- **Title**: MCP-Guard: A Multi-Stage Defense-in-Depth Framework for Securing Model Context Protocol in Agentic AI
- **Year**: 2025
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2508.10991
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\wenpeng-2025-mcp-guard-multi-stage-defense\fulltext.txt
- **Character Count**: 49599

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 623:748]
> To counter
> these challenges, we propose MCP-GUARD, a
> robust, layered defense architecture designed
> for LLM–tool interactions.
**Location**: `Abstract` [offsets: 1140:1287]
> To enable rigorous training and eval-
> uation, we introduce MCP-ATTACKBENCH, a
> comprehensive benchmark comprising 70,448
> samples augmented by GPT-4.

## Block 3: Method Locator
**Section Heading**: `1. MCP-GUARD Framework: Propose a three-` [section offsets: 5340:5511]
**First 120 words verbatim** [offsets: 5340:6168]
> 1. MCP-GUARD Framework: Propose a three-
> stage defense (static, neural, LLM arbitration)
> achieving 89.1% F1-score with 51% latency
> reduction vs. standalone LLM defenses.
> 
> 2. MCP-ATTACKBENCH: We will release the
> large-scale MCP-specific benchmark with
> 70,448 samples, covering unique threats for
> future research.
> 
> 2
> Related Work
> 
> MCP security frameworks can be broadly catego-
> rized into three main areas: infrastructure isolation
> and access control (Narajala et al., 2025; Bhatt
> et al., 2025), offline auditing and static inspection
> (Radosevich and Halloran, 2025; Guo et al., 2025),
> and runtime integrity and information flow (Kumar
> et al., 2025; Jing et al., 2025; Wang et al., 2025a).
> As shown in Table 1, existing solutions primar-
> ily focus on pre-execution gatekeeping and offline
> checks, while runtime semantic inspection

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `Abstract` [offsets: 1140:1287]
> To enable rigorous training and eval-
> uation, we introduce MCP-ATTACKBENCH, a
> comprehensive benchmark comprising 70,448
> samples augmented by GPT-4.
**Location**: `Abstract` [offsets: 1288:1494]
> This benchmark
> simulates diverse real-world attack vectors that
> circumvent conventional defenses in the MCP
> paradigm, thereby laying a solid foundation for
> future research on securing LLM-tool ecosys-
> tems.
**Location**: `Introduction` [offsets: 2275:2353]
> MCP-GUARD excels in Runtime Seman-
> tic Integrity with a large-scale benchmark.
**Location**: `2. MCP-ATTACKBENCH: We will release the` [offsets: 5514:5651]
> MCP-ATTACKBENCH: We will release the
> large-scale MCP-specific benchmark with
> 70,448 samples, covering unique threats for
> future research.
**Location**: `Related Work` [offsets: 6836:7089]
> While benchmarks like MCPSecBench
> (Yang et al., 2025) and MCIP-bench (Jing et al.,
> 2025) effectively facilitate offensive red-teaming
> and policy verification, they are primarily designed
> for vulnerability assessment rather than defensive
> model training.
**Location**: `Related Work` [offsets: 7090:7323]
> This creates a critical gap: existing
> datasets lack the scale and semantic diversity re-
> quired to train robust neural detectors, a limitation
> our work addresses by introducing the large-scale
> MCP-ATTACKBENCH for supervision signals.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Introduction` [offsets: 2275:2353]
> MCP-GUARD excels in Runtime Seman-
> tic Integrity with a large-scale benchmark.
**Location**: `Introduction` [offsets: 2355:2375]
> Pre-Ex
> Runtime
> Prot.
**Location**: `III. Protocol & Integrity` [offsets: 3769:4180]
> Recent
> audits reveal sophisticated MCP exploits beyond
> prompt injection: Tool Poisoning embeds malicious
> instructions in tool descriptions to hijack intent
> (e.g., a benign calculator exfiltrating SSH keys)
> 
> 1
> 
> --- PAGE BREAK ---
> 
> (Guo et al., 2025; Radosevich and Halloran, 2025),
> while Shadowing Attacks disguise legitimate tools
> on malicious servers to manipulate control flow un-
> detected (Hou et al., 2025).
**Location**: `III. Protocol & Integrity` [offsets: 4181:4477]
> Current defenses fall
> short: static gateways like MCP Guardian (Kumar
> et al., 2025) rely on regex WAFs effective against
> overt syntax but blind to semantic obfuscation; of-
> fline scanners like McpSafetyScanner (Radosevich
> and Halloran, 2025) offer pre-deployment checks
> but no runtime protection.
**Location**: `III. Protocol & Integrity` [offsets: 4479:4795]
> To bridge this critical gap, we introduce MCP-
> GUARD, a real-time, layered defense framework
> tailored for MCP, featuring a three-stage pipeline
> that balances efficiency with deep semantic analy-
> sis: (1) Stage I (Fail-Fast): A lightweight static
> scanner filters overt syntax violations with sub-
> millisecond latency.
**Location**: `III. Protocol & Integrity` [offsets: 4992:5146]
> (3) Stage III (Intelligent Arbi-
> tration): An LLM arbitrator with a hybrid fallback
> mechanism resolves ambiguous cases while min-
> imizing false positives.

## Block 8: Limitations
**Location**: `Limitations`
**First 120 words verbatim** [offsets: 34838:35694]
> Limitations
> 
> Despite the robust performance of MCP-GUARD,
> several limitations remain inherent to its current
> design and evaluation scope:
> Protocol Dependency and Evolution. Our frame-
> work is tightly coupled with the current specifica-
> tion of the Model Context Protocol. While Stage
> I’s regex patterns are hot-updateable, fundamental
> changes to the MCP transport layer (e.g., a shift
> from JSON-RPC to a binary protocol) would ne-
> cessitate significant re-engineering of the parsing
> logic. Additionally, our evaluation primarily fo-
> cuses on text-based payloads. As MCP evolves to
> support multi-modal data transfer (e.g., image or
> audio buffers), our text-centric embedding models
> (Stage II) may require retraining to detect adversar-
> ial perturbations in non-textual modalities.
> Latency vs. Security Trade-off. Although MCP-
> GUARD achieves a 2.04× speedup

## Block 9: Adaptivity Hits
**Matched Term**: `circumvent` | **Location**: `Abstract` [offsets: 1140:1712]
> To enable rigorous training and eval-
> uation, we introduce MCP-ATTACKBENCH, a
> comprehensive benchmark comprising 70,448
> samples augmented by GPT-4. This benchmark
> simulates diverse real-world attack vectors that
> circumvent conventional defenses in the MCP
> paradigm, thereby laying a solid foundation for
> future research on securing LLM-tool ecosys-
> tems.
> 
> arXiv:2508.10991v4  [cs.CR]  8 Jan 2026
> 
> 1
> Introduction
> 
> The rapid proliferation of Large Language Mod-
> els (LLMs) has necessitated a dual focus on their
> security vulnerabilities and intellectual property
> safeguards.
**Matched Term**: `evade` | **Location**: `Related Work` [offsets: 9388:10161]
> proposed MCIP, which
> enforces “Contextual Integrity” by tracking infor-
> mation flow between public and private contexts
> (Jing et al., 2025), while Wang et al.’s similarly
> named MCPGuard focuses on offline scanning for
> server-side vulnerabilities like path traversal rather
> than real-time prompt filtering (Wang et al., 2025a).
> Bridging these gaps, our framework introduces a
> semantic-aware defense pipeline that transcends
> syntactic WAFs and offline audits; by integrating a
> fine-tuned E5 embedding model (Stage II) with a
> lightweight LLM arbitrator (Stage III), we detect
> subtle adversarial intents in real-time traffic that
> evade traditional regex filters.
> 
> 3
> MCP-Guard
> 
> MCP-GUARD functions as a proxy-based security
> middleware interposed between the MCP Host and
> Server.
**Matched Term**: `evade` | **Location**: `2. Stage II: Semantic Neural Detection (The In-` [offsets: 11269:11700]
> To bridge the semantic gap left by
> regex-based WAFs, this stage utilizes a fine-
> tuned Multilingual E5 embedding model. Un-
> like generic scanners (Guo et al., 2025), our
> model undergoes full-parameter fine-tuning
> on domain-specific MCP threat data, enabling
> it to detect obfuscated payloads (e.g., tool
> poisoning, jailbreaks) that evade syntactic
> rules. It outputs a malicious probability score
> P(y|x) to quantify threat certainty.
**Matched Term**: `evade` | **Location**: `references` [offsets: 13976:14549]
> Stage I effectively filters overt syntactic threats but
> remains blind to semantic adversarial payloads—
> attacks that comply with MCP syntax yet embed
> malicious intent in natural language. Recent audits
> highlight sophisticated vectors such as Retrieval-
> Agent Deception (RADE) (Radosevich and Hallo-
> ran, 2025) and Tool Poisoning (Guo et al., 2025),
> which evade static filters by mimicking legitimate
> 
> invocations. Stage II employs the MCP-GUARD
> Learnable Detector—a fine-tuned E5 embedding
> model that captures latent semantic misalignment
> in complex or obfuscated payloads.
**Matched Term**: `evade` | **Location**: `references` [offsets: 18334:18596]
> In contrast, our architecture employs a condi-
> tional activation mechanism. This stage utilizes a
> lightweight LLM solely as a final symbolic check
> to resolve uncertainties (P(y|x) ≈0.5) that evade
> Stage II’s decision boundary.
> Decoupled Independent Verification.
**Matched Term**: `evade` | **Location**: `Method` [offsets: 32755:33154]
> Full-parameter
> fine-tuning on MCP-ATTACKBENCH overcomes
> the domain misalignment of standard embeddings
> (65.37% accuracy), propelling the F1-score from
> 55.6% (Stage I) to 95.1% (Stage II) with 96.01%
> accuracy (Table 4a). This substantial gain confirms
> the neural component’s critical role in identifying
> complex attacks that evade rigid syntactic filters.
> Speedup
> Against
> LLMs
> Standalone
> (Stage III).
**Matched Term**: `adaptive` | **Location**: `References` [offsets: 42560:42690]
> 2025. Pree: Towards
> harmless and adaptive fingerprint editing in large
> language models via knowledge prefix enhancement.
> Preprint.
