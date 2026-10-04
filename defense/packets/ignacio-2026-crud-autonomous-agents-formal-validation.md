# Evidence Locator Packet: ignacio-2026-crud-autonomous-agents-formal-validation

- **Title**: From CRUD to Autonomous Agents: Formal Validation and Zero-Trust Security for Semantic Gateways in AI-Native Enterprise Systems
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2604.25555
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\ignacio-2026-crud-autonomous-agents-formal-validation\fulltext.txt
- **Character Count**: 61394

## Block 2: Contribution Sentences
**Location**: `abstract` [offsets: 45845:46765]
> abstract
> risk directives into ex-
> ecutable mathematical
> verification
> OWASP GenAI [17]
> Manual red teaming
> Recommends
> least
> privilege
> 
> significant further empirical validation.
> 
> 13
> Related Work Comparison
> 
> Framework
> State Validation
> Agentic
> Authoriza-
> tion
> 
> REST / OpenAPI
> Unit
> &
> integration
> tests
> 
> 14
> Future Work
> 
> 19
> 
> Limitation
> Ad-
> dressed
> 
> Delegates
> to
> loosely
> coupled tools
> 
> Out of scope for tool
> calls
> 
> Replaces
> manual
> red-teaming with au-
> tomated
> continuous
> semantic fuzzing
> AgentGuard [3]
> Online MDP learning
> Probabilistic blocking
> Shifts
> verification
> pre-deployment
> via
> fuzzing, avoiding risky
> runtime reliance
> 
> The explicit limitations identified during the empirical evaluation present clear, actionable av-
> enues for future research.
> 
> To overcome the semantic fuzzer’s inherent inability to bypass highly complex cryptographic
> checks and strict parameter constraints, future iterations of this architecture must

## Block 3: Method Locator
**Section Heading**: `Implementation Stack and Component Mapping` [section offsets: 31167:31413]
**First 120 words verbatim** [offsets: 31167:32150]
> Implementation Stack and Component Mapping
> 
> Paper Component
> File
> Notes
> 
> 8.2
> Test Suite
> 
> 14
> 
> Semantic Firewall
> gateway/firewall.py
> 12
> regex
> injection
> patterns;
> taint-
> aware
> context
> tags
> ([EMAIL_BODY],
> [EXTERNAL])
> Tool Registry
> gateway/registry.py
> 12 MCP-style tools across READ /
> WRITE / CRITICAL tiers
> Semantic Router
> gateway/router.py
> TF-IDF + cosine similarity; fully offline
> Policy Engine
> gateway/policy.py
> OPA-inspired
> RBAC;
> role
> hierarchy;
> BOLA ownership checks
> Audit Ledger
> gateway/audit.py
> SHA-256
> hash-chained,
> append-only;
> SQLite backend
> EPA Graph
> gateway/epa.py
> NetworkX MultiDiGraph; DOT export;
> buggy flag toggles the BOLA edge
> Claude Planner
> gateway/planner.py
> Anthropic API (optional); deterministic
> mock fallback
> Semantic Fuzzer
> fuzzer/semantic_fuzzer.py
> Invariant-based; guided 80% valid / 20%
> adversarial mutation
> FastAPI Gateway
> gateway/main.py
> Endpoints:
> /intent,
> /audit,
> /epa,
> /health
> 
> The poc ships with a comprehensive test suite of 47 automated tests organized

## Block 4: Evaluation Locator
**Section Heading**: `10 Results` [section offsets: 5117:5320]
**First 120 words verbatim** [offsets: 5117:5479]
> 10 Results
> 16
> 10.1 Productivity and Incidental Code Reduction . . . . . . . . . . . . . . . . . . . . .
> 16
> 10.2 Security and Adversarial Resilience . . . . . . . . . . . . . . . . . . . . . . . . . .
> 17
> 10.3 Formal Verification Metrics
> . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
> 17
> 10.4 Performance Analysis . . . . . . . . . . . . . . . . . . .
**Section Heading**: `Results` [section offsets: 36475:43059]
**First 120 words verbatim** [offsets: 36475:37425]
> Results
> 
> 10.1
> Productivity and Incidental Code Reduction
> 
> 16
> 
> The semantic fuzzing campaign was rigorously initialized with a base corpus containing 10,000
> legitimate natural language intents. The fuzzer’s mutation engine then iteratively applied aggres-
> sive adversarial perturbations aligned perfectly with the OWASP LLM01 vulnerability profile [17],
> extreme parameter boundary manipulations engineered to test for authorization bypasses, and
> sophisticated context tainting techniques. The automated campaign ran up to a defined Test
> Limit of 500,000 stochastic interaction sequences.
> 
> The hardware configuration comprised high-performance NVIDIA A100 GPUs.
> The pre-
> inference Semantic Firewall utilized the highly optimized DeBERTa-v3 micro-model. The core
> Chain-of-Thought planning was powered by Llama-3-8B (edge-compute simulation) and GPT-
> 4o (high-capability cloud simulation). All language models were constrained to a temperature
> setting of

## Block 5: Attack-Set Excerpts
**Location**: `Results` [offsets: 41652:41774]
> The full test suite of 47 tests is reproducible in under 2 seconds on commodity
> hardware, with no external API dependency.

## Block 6: Baseline Excerpts
**Location**: `Results` [offsets: 37751:37991]
> When integrating
> a completely new functional sub-domain, the traditional REST baseline required the generation
> of 920 Lines of Code distributed across complex routing logic, Data Transfer Objects, object
> mappers, and heavy controller logic.
**Location**: `Results` [offsets: 40885:40911]
> traditional REST baseline.
**Location**: `Results` [offsets: 40913:41172]
> Dimension
> Metric
> REST Baseline
> Semantic Gateway
> Delta
> 
> 16 days
> 3 days
> 5.3× acceler-
> ation
> Security (BOLA)
> Real-State
> Compro-
> mise
> 
> The proof-of-concept implementation provides independently reproducible evidence for the two
> most critical claims of this paper.

## Block 7: Cost Excerpts
**Location**: `Results` [offsets: 40680:40821]
> These cached responses were dispatched with sub-millisecond latency,
> offering performance comparable to highly optimized key-value databases.
**Location**: `Results` [offsets: 41652:41774]
> The full test suite of 47 tests is reproducible in under 2 seconds on commodity
> hardware, with no external API dependency.

## Block 8: Limitations
**Section Heading**: `12 Threats to Validity` [section offsets: 5643:5670]
**First 120 words verbatim** [offsets: 5643:6521]
> 12 Threats to Validity
> 18
> 
> 13 Related Work Comparison
> 19
> 
> 14 Future Work
> 19
> 
> 15 Conclusion
> 20
> 
> Artifact Availability
> 20
> 
> A Tool Schemas
> 22
> 
> B Policy Rules
> 23
> 
> C Fuzzing Campaign Logs
> 23
> 
> D EPA Graphs
> 24
> 
> 3
> 
> --- PAGE BREAK ---
> 
> The evolution of enterprise software architecture has historically been driven by the imperative
> to manage system complexity through deterministic, highly predictable abstractions. From struc-
> tured monolithic systems to Service-Oriented Architectures and microservices proliferation, the
> underlying engineering paradigm has remained remarkably stable: software design predicated
> on static rules, rigid interface contracts, and entirely predictable execution flows. However, the
> integration of autonomous agentic artificial intelligence systems into enterprise environments pre-
> cipitates the rapid collapse of this structural rigidity. The transition

## Block 9: Adaptivity Hits
no hits
