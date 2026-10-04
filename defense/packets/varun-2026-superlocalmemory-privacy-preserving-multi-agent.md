# Evidence Locator Packet: varun-2026-superlocalmemory-privacy-preserving-multi-agent

- **Title**: SuperLocalMemory: Privacy-Preserving Multi-Agent Memory with Bayesian Trust Defense Against Memory Poisoning
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2603.02240
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\varun-2026-superlocalmemory-privacy-preserving-multi-agent\fulltext.txt
- **Character Count**: 36447

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 575:879]
> We present SuperLocalMemory, a local-first memory system for multi-agent AI
> that defends against OWASP ASI06 memory poisoning through architectural
> isolation and Bayesian trust scoring, while personalizing retrieval through adaptive
> learning-to-rank—all without cloud dependencies or LLM inference calls.
**Location**: `Abstract` [offsets: 3019:3162]
> We present SuperLocalMemory, a local-first memory system that eliminates cloud dependency while
> providing trust-aware multi-agent coordination.
**Location**: `Abstract` [offsets: 3163:3361]
> Our contributions:
> 
> 2
> Threat Model and Motivation
> 
> 2.1
> Memory Poisoning Taxonomy
> 
> OWASP ASI06 defines memory poisoning as persistent corruption of agent memory that influences
> future decisions [21].

## Block 3: Method Locator
**Section Heading**: `architecture` [section offsets: 14279:15031]
**First 120 words verbatim** [offsets: 14279:15079]
> architecture
> 
> Memory Stack
> Coordination (v2.5)
> 
> write
> read
> 
> Adaptive Learning (v2.7)
> 3-layer behavioral analysis · LambdaRank re-ranking
> 
> Layer 4: Pattern Learning
> Beta-Binomial Bayesian · 8 categories
> 
> trust
> 
> Layer 3: Knowledge Graph
> Leiden clustering · TF-IDF key-terms · O(n2)
> 
> Layer 2: Hierarchical Index
> Materialized paths · O(1) parent lookup
> 
> provenance
> 
> Layer 1: Storage Engine
> SQLite + FTS5 + WAL + Write Queue
> 
> memory.db — WAL · single file · zero network
> learning.db — GDPR isolated
> 
> Data flow
> Event / signal flow
> *A2A = architecture specification only
> 
> (JSON array of all modifications with timestamps and agent IDs). This enables forensic isolation of
> all memories from a specific agent and modification history tracing for any memory.
> 
> 5
> Evaluation
> 
> 5.1
> Experimental Setup
> 
> 5
> 
> Event Bus
**Section Heading**: `architecture.` [section offsets: 24851:27352]
**First 120 words verbatim** [offsets: 24851:25834]
> architecture.
> 
> Pattern learning and adaptive ranking. MACLA [8] introduces Beta-Binomial Bayesian confidence
> for multi-agent learning. MemoryBank [31] provides temporal-aware memory architecture. Our
> Layer 4 adapts MACLA’s confidence model for local preference tracking. For retrieval personalization,
> learning-to-rank approaches using gradient boosted trees [12] with LambdaRank objectives [3] are
> well-established in web search but have not been applied to local memory systems. Recent work on
> BM25-to-re-ranker pipelines for personal collections [26] and cold-start mitigation through synthetic
> bootstrapping [13] inform our three-phase adaptive ranking design. Time-weighted sequential pattern
> mining [16] inspires our sliding-window-based workflow pattern detection. To our knowledge,
> SuperLocalMemory is the first system combining fully local, zero-LLM adaptive re-ranking with
> privacy-preserving behavioral learning for personal AI memory.
> 
> Memory architectures. The survey by

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 15031:24097]
**First 120 words verbatim** [offsets: 15031:15916]
> Evaluation
> 
> 5.1
> Experimental Setup
> 
> 5
> 
> Event Bus
> SSE · WebSocket · Webhook
> 
> events
> 
> Trust Scorer
> Bayesian signals · decay
> 
> Agent Registry
> Protocol · counters · trust
> 
> feedback
> 
> & patterns
> 
> Provenance Tracker
> 
> created_by · chain · audit
> 
> Figure 1: SuperLocalMemory architecture. The four-layer memory stack (left) provides progressive
> enhancement; the adaptive learning layer (v2.7) re-ranks search results using three-layer behav-
> ioral analysis. The coordination panel (right, v2.5) handles event broadcasting, trust scoring, and
> provenance tracking, with feedback and learned patterns stored in an isolated learning.db (GDPR-
> friendly, supports Article 17 erasure). All data remains on the user’s machine.
> 
> Defense against sleeper agents. An agent writes normally for N operations (accumulating positive
> signals), then begins injecting contradictory content. The decay factor ensures

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 16141:16293]
> All benchmarks ran on Apple M4 Pro (24GB RAM), macOS 26.2, Python 3.12.12, SQLite 3.51.1,
> scikit-learn 1.8.0, python-igraph 1.0.0, and leidenalg 0.11.0.
**Location**: `Evaluation` [offsets: 18846:18992]
> The
> benchmark data in this paper uses brute-force computation; at 5,000 memories a full build takes 4.6
> minutes, motivating the HNSW optimization.
**Location**: `Evaluation` [offsets: 23364:23399]
> §LongMemEval (different benchmark).

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 15892:16057]
> The decay factor ensures early good behavior
> stabilizes trust, but accumulated negative signals from the poisoning phase gradually overcome
> the established baseline.
**Location**: `Evaluation` [offsets: 17545:17656]
> 5.5
> Layer Ablation Study
> 
> Table 3 reports retrieval quality across five layer configurations at 1,000 memories.
**Location**: `Evaluation` [offsets: 19708:19738]
> Table 3: Layer ablation study.
**Location**: `Evaluation` [offsets: 20258:20488]
> Benign baseline (10 agents)
> 0.945
> —
> 0.000
> Single poisoner (9 benign + 1)
> 0.946
> 0.048
> 0.898
> Sleeper (normal →inject)
> 0.902
> 0.249
> 0.653
> 
> The core FTS5 retrieval achieves MRR 0.90 (first relevant result at rank 1 for 90% of queries).

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 16686:16821]
> Each timing measurement reports the median of 100 runs after 10 warmup iterations, using
> time.perf_counter() for microsecond precision.
**Location**: `Evaluation` [offsets: 16847:16900]
> Table 1 reports search latency across database sizes.
**Location**: `Evaluation` [offsets: 16901:16982]
> For typical personal memory databases (100
> memories), search completes in 10.6ms.
**Location**: `Evaluation` [offsets: 16983:17066]
> Scaling from 100 to 1,000 memories (10× data) increases
> latency 12×—roughly linear.
**Location**: `Evaluation` [offsets: 17067:17247]
> Beyond 1,000, brute-force TF-IDF exhibits superlinear scaling (1.17s
> at 5,000), motivating optional BM25 and HNSW index add-ons included in the distribution but not
> evaluated here.
**Location**: `Evaluation` [offsets: 17393:17501]
> Per-memory cost decreases from 44KB at 100
> memories to 1.4KB at 10,000 as fixed database overhead amortizes.

## Block 8: Limitations
**Section Heading**: `Limitations and Future Work` [section offsets: 27352:27590]
**First 120 words verbatim** [offsets: 27352:28234]
> Limitations and Future Work
> 
> Trust-weighted ranking. Trust enforcement blocks agents below 0.3, but trust scores do not yet
> influence the re-ranker’s feature vector. Integrating trust as a ranking signal would enable soft
> degradation.
> 
> 8
> Conclusion
> 
> Acknowledgments
> 
> The author used AI writing tools for manuscript preparation. All technical contributions, system
> design, implementation, and experimental evaluation are the sole work of the author.
> 
> 9
> 
> Security. The OWASP Top 10 for Agentic AI [21] identifies memory poisoning (ASI06) as a critical
> threat. Analysis of MCP security [10] reveals tool-level attack vectors. Work on agent privacy [20]
> distinguishes memorization from genuine privacy threats. To our knowledge, SuperLocalMemory
> is the first system combining local-first architecture with trust scoring specifically targeting ASI06
> defense.
> 
> Learning requires sustained

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Abstract` [offsets: 565:1126]
> Abstract
> 
> We present SuperLocalMemory, a local-first memory system for multi-agent AI
> that defends against OWASP ASI06 memory poisoning through architectural
> isolation and Bayesian trust scoring, while personalizing retrieval through adaptive
> learning-to-rank—all without cloud dependencies or LLM inference calls. As AI
> agents increasingly rely on persistent memory, cloud-based memory systems create
> centralized attack surfaces where poisoned memories propagate across sessions and
> users—a threat demonstrated in documented attacks against production systems.
**Matched Term**: `adaptive` | **Location**: `Abstract` [offsets: 880:1795]
> As AI
> agents increasingly rely on persistent memory, cloud-based memory systems create
> centralized attack surfaces where poisoned memories propagate across sessions and
> users—a threat demonstrated in documented attacks against production systems.
> Our architecture combines SQLite-backed storage with FTS5 full-text search,
> Leiden-based knowledge graph clustering, an event-driven coordination layer
> with per-agent provenance, and an adaptive re-ranking framework that learns
> user preferences through three-layer behavioral analysis (cross-project technology
> preferences, project context detection, and workflow pattern mining). Evaluation
> across seven benchmark dimensions demonstrates 10.6ms median search latency,
> zero concurrency errors under 10 simultaneous agents, trust separation (gap =
> 0.90) with 72% trust degradation for sleeper attacks, and 104% improvement
> in NDCG@5 when adaptive re-ranking is enabled.
**Matched Term**: `adaptive` | **Location**: `Abstract` [offsets: 1127:1917]
> Our architecture combines SQLite-backed storage with FTS5 full-text search,
> Leiden-based knowledge graph clustering, an event-driven coordination layer
> with per-agent provenance, and an adaptive re-ranking framework that learns
> user preferences through three-layer behavioral analysis (cross-project technology
> preferences, project context detection, and workflow pattern mining). Evaluation
> across seven benchmark dimensions demonstrates 10.6ms median search latency,
> zero concurrency errors under 10 simultaneous agents, trust separation (gap =
> 0.90) with 72% trust degradation for sleeper attacks, and 104% improvement
> in NDCG@5 when adaptive re-ranking is enabled. Behavioral data is isolated
> in a separate database supporting GDPR Article 17 erasure requests via one-
> command deletion.
**Matched Term**: `adaptive` | **Location**: `Abstract` [offsets: 5328:5622]
> 3. A zero-LLM adaptive learning-to-rank framework that mines user preferences across three
> behavioral layers with privacy-preserving behavioral learning and re-ranks retrieval results,
> achieving 104% NDCG@5 improvement over the base search pipeline—without requiring
> any LLM inference calls.
> 4.
**Matched Term**: `Adaptive` | **Location**: `A SQLite-backed event log with 200-event in-memory buffer broadcasts events` [offsets: 10288:10490]
> --- PAGE BREAK ---
> 
> Adaptive re-ranking. A three-phase progression ensures zero degradation risk [26]: Phase 0
> (baseline): fewer than 20 feedback signals—results returned unchanged (pure v2.5 behavior).
**Matched Term**: `Adaptive` | **Location**: `A SQLite-backed event log with 200-event in-memory buffer broadcasts events` [offsets: 11065:11507]
> 3.3
> Adaptive Learning Layer
> 
> Added in v2.7, the adaptive learning layer addresses the layer differentiation limitation identified
> in our initial evaluation (Section 5.5): while layers 3–4 provide structural enrichment, they did not
> originally improve search ranking. The adaptive layer sits between the search pipeline and result
> delivery, re-ranking candidates based on learned user preferences—entirely locally, without LLM
> inference calls.
**Matched Term**: `adaptive` | **Location**: `A SQLite-backed event log with 200-event in-memory buffer broadcasts events` [offsets: 11094:11661]
> Added in v2.7, the adaptive learning layer addresses the layer differentiation limitation identified
> in our initial evaluation (Section 5.5): while layers 3–4 provide structural enrichment, they did not
> originally improve search ranking. The adaptive layer sits between the search pipeline and result
> delivery, re-ranking candidates based on learned user preferences—entirely locally, without LLM
> inference calls.
> 
> 4
> Trust Scoring Framework
> 
> The trust defense framework addresses OWASP ASI06 through per-agent behavioral monitoring and
> per-memory provenance tracking.
**Matched Term**: `Adaptive` | **Location**: `architecture` [offsets: 14327:15027]
> write
> read
> 
> Adaptive Learning (v2.7)
> 3-layer behavioral analysis · LambdaRank re-ranking
> 
> Layer 4: Pattern Learning
> Beta-Binomial Bayesian · 8 categories
> 
> trust
> 
> Layer 3: Knowledge Graph
> Leiden clustering · TF-IDF key-terms · O(n2)
> 
> Layer 2: Hierarchical Index
> Materialized paths · O(1) parent lookup
> 
> provenance
> 
> Layer 1: Storage Engine
> SQLite + FTS5 + WAL + Write Queue
> 
> memory.db — WAL · single file · zero network
> learning.db — GDPR isolated
> 
> Data flow
> Event / signal flow
> *A2A = architecture specification only
> 
> (JSON array of all modifications with timestamps and agent IDs). This enables forensic isolation of
> all memories from a specific agent and modification history tracing for any memory.
**Matched Term**: `adaptive` | **Location**: `Evaluation` [offsets: 15268:15698]
> Figure 1: SuperLocalMemory architecture. The four-layer memory stack (left) provides progressive
> enhancement; the adaptive learning layer (v2.7) re-ranks search results using three-layer behav-
> ioral analysis. The coordination panel (right, v2.5) handles event broadcasting, trust scoring, and
> provenance tracking, with feedback and learned patterns stored in an isolated learning.db (GDPR-
> friendly, supports Article 17 erasure).
**Matched Term**: `Adaptive` | **Location**: `Evaluation` [offsets: 19903:20638]
> Configuration
> MRR
> NDCG@5
> NDCG@10
> Latency (ms)
> 
> FTS5 only
> 0.90
> 0.441
> 0.466
> 130.0
> + TF-IDF reranking
> 0.90
> 0.441
> 0.466
> 122.3
> + Graph clusters
> 0.90
> 0.441
> 0.466
> 132.7
> Full system (all layers)
> 0.90
> 0.441
> 0.466
> 122.7
> + Adaptive ranker
> 0.90
> 0.900
> 0.728
> 153.1
> 
> Scenario
> Benign Trust
> Malicious Trust
> Gap
> 
> 5.6
> Trust Defense Evaluation
> 
> 5.7
> Pilot User Evaluation
> 
> 7
> 
> Benign baseline (10 agents)
> 0.945
> —
> 0.000
> Single poisoner (9 benign + 1)
> 0.946
> 0.048
> 0.898
> Sleeper (normal →inject)
> 0.902
> 0.249
> 0.653
> 
> The core FTS5 retrieval achieves MRR 0.90 (first relevant result at rank 1 for 90% of queries). Layers
> 3–4 maintain but do not improve MRR—the Graph and Pattern layers provide structural enrichment
> but do not modify the search ranking algorithm.
**Matched Term**: `adaptive` | **Location**: `Evaluation` [offsets: 20972:21214]
> The adaptive learning layer (Section 3.3) addresses this directly. With rule-based re-ranking (20+
> feedback signals), NDCG@5 improves from 0.441 to 0.900 (+104%) and NDCG@10 from 0.466 to
> 0.728 (+56%), while adding only 20ms latency overhead.
**Matched Term**: `adaptive` | **Location**: `Evaluation` [offsets: 21039:21379]
> With rule-based re-ranking (20+
> feedback signals), NDCG@5 improves from 0.441 to 0.900 (+104%) and NDCG@10 from 0.466 to
> 0.728 (+56%), while adding only 20ms latency overhead. MRR is maintained at 0.90—the adaptive
> layer does not degrade topic-level accuracy while substantially improving within-topic ranking.
> 
> Evaluation circularity note.
**Matched Term**: `adaptive` | **Location**: `Evaluation` [offsets: 21351:21686]
> Evaluation circularity note. We acknowledge that the graded relevance labels used for NDCG
> computation are derived from the system’s own importance scores, which the adaptive ranker includes
> as one of nine features. This creates a circularity where the ranker is partially evaluated on its ability
> to predict a signal it has access to.
**Matched Term**: `adaptive` | **Location**: `Evaluation` [offsets: 23427:23802]
> Table 5 compares SuperLocalMemory with published memory systems. SuperLocalMemory re-
> mains the only system combining zero-dependency local-first architecture, Bayesian trust scoring,
> and adaptive local learning without LLM inference. Mem0 [4] now offers local deployment via
> OpenMemory MCP (requiring Docker, PostgreSQL, Qdrant); Zep deprecated its community edition
> (2025).
**Matched Term**: `adaptive` | **Location**: `architecture.` [offsets: 24866:24985]
> Pattern learning and adaptive ranking. MACLA [8] introduces Beta-Binomial Bayesian confidence
> for multi-agent learning.
**Matched Term**: `adaptive` | **Location**: `architecture.` [offsets: 25122:25622]
> For retrieval personalization,
> learning-to-rank approaches using gradient boosted trees [12] with LambdaRank objectives [3] are
> well-established in web search but have not been applied to local memory systems. Recent work on
> BM25-to-re-ranker pipelines for personal collections [26] and cold-start mitigation through synthetic
> bootstrapping [13] inform our three-phase adaptive ranking design. Time-weighted sequential pattern
> mining [16] inspires our sliding-window-based workflow pattern detection.
**Matched Term**: `adaptive` | **Location**: `architecture.` [offsets: 25516:25820]
> Time-weighted sequential pattern
> mining [16] inspires our sliding-window-based workflow pattern detection. To our knowledge,
> SuperLocalMemory is the first system combining fully local, zero-LLM adaptive re-ranking with
> privacy-preserving behavioral learning for personal AI memory.
> 
> Memory architectures.
**Matched Term**: `adaptive` | **Location**: `Conclusion` [offsets: 28207:28491]
> Learning requires sustained usage. The adaptive re-ranking requires 20+ feedback signals for
> rule-based phase and 200+ across 50+ unique queries for ML personalization. Synthetic bootstrap
> mitigates ML cold-start but cannot substitute for genuine behavioral signals in earlier phases.
**Matched Term**: `adaptive` | **Location**: `Conclusion` [offsets: 28883:29038]
> No formal user study has been conducted. Controlled evaluation of whether
> adaptive ranking improves real developer workflows is needed.
> 
> Future directions.
**Matched Term**: `adaptive` | **Location**: `Conclusion` [offsets: 29732:30264]
> We presented SuperLocalMemory, demonstrating that local-first architecture provides effective
> defense against OWASP ASI06 memory poisoning by eliminating the cloud-based attack surfaces
> that current systems depend on, while adaptive learning personalizes retrieval without requiring
> cloud services or LLM inference. Our Bayesian trust framework using Beta-Binomial posterior
> inference achieves trust separation (gap = 0.90) between benign and malicious agents with 72% trust
> degradation for sleeper attacks and zero false positives.
**Matched Term**: `adaptive` | **Location**: `Conclusion` [offsets: 30048:30566]
> Our Bayesian trust framework using Beta-Binomial posterior
> inference achieves trust separation (gap = 0.90) between benign and malicious agents with 72% trust
> degradation for sleeper attacks and zero false positives. The adaptive learning-to-rank framework
> addresses the layer differentiation limitation through three-layer behavioral analysis and re-ranking,
> achieving 104% NDCG@5 improvement while adding only 20ms latency overhead. Behavioral data
> is architecturally isolated with GDPR-friendly one-command erasure.
