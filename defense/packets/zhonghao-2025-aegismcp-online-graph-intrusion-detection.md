# Evidence Locator Packet: zhonghao-2025-aegismcp-online-graph-intrusion-detection

- **Title**: AegisMCP: Online Graph Intrusion Detection for Tool-Augmented LLMs on Edge Devices
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2510.19462
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\zhonghao-2025-aegismcp-online-graph-intrusion-detection\fulltext.txt
- **Character Count**: 64625

## Block 2: Contribution Sentences
**Location**: `Abstract—In this work, we study security of Model Context` [offsets: 362:423]
> We introduce AegisMCP, a protocol-level intrusion detec-
> tor.
**Location**: `Abstract—In this work, we study security of Model Context` [offsets: 424:1046]
> Our contributions are: (i) a minimal attack suite spanning
> instruction-driven escalation, chain-of-tool exfiltration, malicious
> MCP server registration, and persistence; (ii) NEBULA-Schema
> (Network-Edge Behavioral Learning for Untrusted LLM Agents),
> a reusable protocol-level instrumentation that represents MCP
> activity as a streaming heterogeneous temporal graph over
> agents, MCP servers, tools, devices, remotes, and sessions;
> and (iii) a CPU-only streaming detector that fuses novelty,
> session-DAG structure, and attribute cues for near-real-time edge
> inference, with optional fusion of local prompt-guardrail signals.
**Location**: `I. INTRODUCTION` [offsets: 3715:4594]
> We present AEGISMCP, a practical protocol-level intrusion
> detector for MCP-driven smart homes. AegisMCP instru-
> ments the MCP control plane and minimal network meta-
> data to emit events in a reusable heterogeneous schema
> (NEBULA). It then constructs micro-batched sliding windows
> and performs edge-level anomaly scoring with a lightweight
> GraphSAGE-style model [8] implemented in PyTorch Ge-
> ometric [9], fused with session-DAG features and optional
> prompt-guardrail signals. The system runs CPU-only via
> ONNX Runtime [10], enabling deployment on consumer edge
> hardware.
> 
> A. Design challenges
> 
> AegisMCP addresses three concrete challenges: (i) Seman-
> tic visibility without DPI (Deep packet inspection): capture
> intent and context by modeling the MCP control plane and
> a minimal 5-tuple/SNI(Server Name Indication) view, avoid-
> ing heavyweight packet inspection. (ii) Few labels,

## Block 3: Method Locator
**Section Heading**: `A. Design challenges` [section offsets: 4287:4958]
**First 120 words verbatim** [offsets: 4287:5172]
> A. Design challenges
> 
> AegisMCP addresses three concrete challenges: (i) Seman-
> tic visibility without DPI (Deep packet inspection): capture
> intent and context by modeling the MCP control plane and
> a minimal 5-tuple/SNI(Server Name Indication) view, avoid-
> ing heavyweight packet inspection. (ii) Few labels, evolving
> catalogs: pretrain on benign traffic with a self-supervised
> objective, then adapt with a thin supervised head and TTL
> (Time-To-Live)-based novelty tracking over (src type, etype,
> dst type) triples. (iii) Edge constraints: micro-batches, type
> embeddings, and ONNX INT8 export keep per-window model
> time sub-second while preserving structure sensitivity.
> 
> B. Contributions
> 
> We make the following contributions:
> 
> 1) NEBULA-Schema and MCP instrumentation A het-
> erogeneous temporal event schema and a JSON-RPC
> proxy plus lightweight network capture that together
> 
> --- PAGE
**Section Heading**: `IV. AEGISMCP SYSTEM DESIGN` [section offsets: 20192:20648]
**First 120 words verbatim** [offsets: 20192:21086]
> IV. AEGISMCP SYSTEM DESIGN
> 
> AegisMCP is a streaming, protocol-level detection system
> that converts MCP control-plane activity and minimal connec-
> tion metadata into heterogeneous temporal graphs and scores
> behavior in near real time. The pipeline has three stages:
> (1) protocol-boundary instrumentation, (2) streaming graph
> construction, and (3) anomaly detection. This section covers
> (1) and (2); the next section details real-time detection and
> fusion.
> 
> A. Design overview
> 
> Agents interact with MCP servers and tools via JSON-RPC.
> AegisMCP instruments this control plane and augments it
> with minimal egress observations (destination, port, bytes)
> to produce NEBULA events. A window builder assembles
> micro-batched, schema-normalized graphs with per-session
> DAG summaries. The detector consumes these graphs to
> produce alerts (next section). We instantiate three attack
> templates (composition,
**Section Heading**: `A. Design overview` [section offsets: 20648:21646]
**First 120 words verbatim** [offsets: 20648:21550]
> A. Design overview
> 
> Agents interact with MCP servers and tools via JSON-RPC.
> AegisMCP instruments this control plane and augments it
> with minimal egress observations (destination, port, bytes)
> to produce NEBULA events. A window builder assembles
> micro-batched, schema-normalized graphs with per-session
> DAG summaries. The detector consumes these graphs to
> produce alerts (next section). We instantiate three attack
> templates (composition, catalog extension, policy-violating
> 
> --- PAGE BREAK ---
> 
> WINDOWED GRAPH
> 
> NEBULA EVENT STREAM
> 
> HETEROGENEOUS
> 
> GRAPH
> 
> remote
> 
> Edge attr: [bytes,
> 
> ports, status, ts,
> 
> agent
> 
> session_id]
> 
> tool
> device
> 
> SESSION DAG
> 
> Tool_A
> 
> invoke
> 
> Action_B
> 
> invoke
> 
> Tool_C
> 
> device control) on the aforementioned MasterMCP, but all
> instrumentation and schema are independent of specific data
> catalog or metadata repository.We exercise the three templates
> from §III; Aegis only relies on
**Section Heading**: `E. Implementation notes` [section offsets: 26301:26667]
**First 120 words verbatim** [offsets: 26301:27179]
> E. Implementation notes
> 
> Control-plane parsing is linear in message size; egress
> observation is filtered to relevant classes of traffic. DuckDB
> queries over Parquet provide sub-second window assembly on
> Intel N150-class hardware via columnar scans and predicate
> pushdown. Typed integer arrays keep memory/CPU footprints
> low and enable fast handoff to the detector.
> 
> F. Transition: real-time anomaly detection
> 
> The next section details real-time detection: novelty over
> (src type, etype, dst type), session-DAG scoring, attribute
> cues, and their fusion; seen-edge filtering for throughput; and
> ONNX CPU-only deployment. We also place the per-edge
> feature construction pseudocode and thresholding policy there.
> 
> V. NEBULA DETECTOR: PROTOCOL-AWARE DETECTION
> 
> AegisMCP’s final stage is a low-overhead detector that
> scores each micro-batch graph on CPU and emits per-edge
> alerts with

## Block 4: Evaluation Locator
**Section Heading**: `VI. EVALUATION` [section offsets: 32424:32764]
**First 120 words verbatim** [offsets: 32424:33282]
> VI. EVALUATION
> 
> We evaluate AEGISMCP along three axes: (1) detection
> accuracy on MCP-specific attacks versus strong baselines, (2)
> timeliness and efficiency on router-class hardware, and (3) the
> contribution of each component via ablations. All experiments
> are reproducible with the repository’s verification scripts and
> artifact bundles.
> 
> A. Experimental Setup
> 
> a) Testbed and pipeline.: A single Intel N150 (4 Cores,
> 16GB RAM) mini-PC runs Home Assistant, Mosquitto, and
> the detector (CPU-only). Device actions (lock, siren, camera
> snapshot/stream) are invoked through the MCP proxy to
> preserve protocol semantics. Collector emits NEBULA events
> (install, invoke, net out); DuckDB queries 10s micro-batches
> with a small lateness watermark; each window serializes a
> compact .npz graph and session-DAG JSON.
> 
> b) Traffic and labels.: We synthesize 24–48h daily
**Section Heading**: `A. Experimental Setup` [section offsets: 32764:34420]
**First 120 words verbatim** [offsets: 32764:33614]
> A. Experimental Setup
> 
> a) Testbed and pipeline.: A single Intel N150 (4 Cores,
> 16GB RAM) mini-PC runs Home Assistant, Mosquitto, and
> the detector (CPU-only). Device actions (lock, siren, camera
> snapshot/stream) are invoked through the MCP proxy to
> preserve protocol semantics. Collector emits NEBULA events
> (install, invoke, net out); DuckDB queries 10s micro-batches
> with a small lateness watermark; each window serializes a
> compact .npz graph and session-DAG JSON.
> 
> b) Traffic and labels.: We synthesize 24–48h daily ac-
> tivity (tens of thousands of sessions) with benign fillers and
> proper invoke→net out ordering. We inject two attack families
> from our MasterMCP-based suite [35]: (i) instruction-driven
> chain exfiltration and (ii) catalog extension with malicious
> registration and persistence (default 10% attack prevalence).
> Weak session labels
**Section Heading**: `results` [section offsets: 41221:41321]
**First 120 words verbatim** [offsets: 41221:42050]
> results
> indicate
> AegisMCP
> is
> deployable
> on
> router-class hardware without impacting other services.
> 
> E. Ablation Study
> 
> We measure the contribution of each component by remov-
> ing it and retraining:
> 
> • No SSL pretraining. AP drops by > 20pp, underscoring
> the importance of learning “normal” structure before
> fine-tuning on scarce labels.
> 
> • No session-DAG features. Precision degrades, particu-
> larly on the exfiltration chain where DAG length and
> install proximity are key disambiguators.
> 
> • No novelty. Recall drops on first-time provider/domain
> edges; fusion compensates partially via attributes but
> misses early egress attempts.
> The combined fusion (edge + DAG + novelty) yields the
> best AP/F1 while controlling FP/h. The ablation figure in the
> artifact bundle (AP bars) visualizes these deltas.
> 
> F. Reproducibility and Checks

## Block 5: Attack-Set Excerpts
**Location**: `A. Experimental Setup` [offsets: 32787:32921]
> a) Testbed and pipeline.: A single Intel N150 (4 Cores,
> 16GB RAM) mini-PC runs Home Assistant, Mosquitto, and
> the detector (CPU-only).

## Block 6: Baseline Excerpts
**Location**: `VI. EVALUATION` [offsets: 32440:32664]
> We evaluate AEGISMCP along three axes: (1) detection
> accuracy on MCP-specific attacks versus strong baselines, (2)
> timeliness and efficiency on router-class hardware, and (3) the
> contribution of each component via ablations.
**Location**: `A. Experimental Setup` [offsets: 33893:34002]
> c) Baselines and our models: Traffic-only GBT: gradi-
> ent boosting over NetFlow-like features (XGBoost [42]).
**Location**: `A. Experimental Setup` [offsets: 34096:34183]
> GCN / R-GCN: standard graph baselines (homogeneous
> GCN [44] and relational R-GCN [39]).

## Block 7: Cost Excerpts
**Location**: `A. Experimental Setup` [offsets: 33041:33230]
> Collector emits NEBULA events
> (install, invoke, net out); DuckDB queries 10s micro-batches
> with a small lateness watermark; each window serializes a
> compact .npz graph and session-DAG JSON.
**Location**: `A. Experimental Setup` [offsets: 33232:33381]
> b) Traffic and labels.: We synthesize 24–48h daily ac-
> tivity (tens of thousands of sessions) with benign fillers and
> proper invoke→net out ordering.

## Block 8: Limitations
**Section Heading**: `VII. DISCUSSION AND LIMITATIONS` [section offsets: 42636:42668]
**First 120 words verbatim** [offsets: 42636:43508]
> VII. DISCUSSION AND LIMITATIONS
> A. Implications
> 
> a) Behavior over payloads: By instrumenting MCP and
> recording only control-plane semantics plus minimal con-
> nection metadata (destination/port; hostname when available),
> 
> --- PAGE BREAK ---
> 
> Model
> Samples
> Duration (s)
> Avg Power (W)
> P95 Power (W)
> Total Energy (J)
> 
> GCN
> 18.000
> 4.430
> 22.250
> 25.560
> 98.790
> GraphSAGE
> 4.000
> 0.920
> 23.370
> 24.130
> 21.480
> Lite
> 6.000
> 1.290
> 22.370
> 24.260
> 30.030
> R-GCN
> 18.000
> 4.320
> 22.290
> 24.310
> 96.440
> Rules
> 3.000
> 0.530
> 21.270
> 22.720
> 11.940
> Seq GRU
> 21.000
> 5.050
> 21.750
> 23.240
> 110.180
> Traffic XGB
> 6.000
> 1.470
> 22.770
> 23.390
> 33.430
> 
> AegisMCP attains high-fidelity visibility without decrypting
> traffic or modifying agents/tools. NEBULA’s normalization
> (fixed node/edge types with provider as an attribute) avoids
> type explosion and supports cross-catalog generalization.
> 
> b) Structure matters: Gains over

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `A. Threat Model` [offsets: 16558:17154]
> e) Adversary model: A gray-box user/content source can
> introduce legitimate tool invocations through natural-language
> inputs (directly or via untrusted web/email/calendar/pages) [6],
> [7]. They may: (i) chain benign tools to stage, obfuscate, and
> egress data; (ii) request installation/registration of additional
> MCP servers if allowed by policy; (iii) choose novel egress
> endpoints; (iv) add benign filler calls and time gaps to evade
> naive heuristics; (v) paraphrase/translate prompts to degrade
> text-only guardrails. They cannot interfere with the collector
> or OS, nor escalate host privileges.
**Matched Term**: `evasion` | **Location**: `B. Attack Suite (Templates and Instantiation)` [offsets: 18310:18670]
> We use three parameterized templates to exercise com-
> position, extension, and impact. Each supports benign filler,
> randomized delays, and destination churn (domain/port/IP)
> for evasion variants. We instantiate these templates on a
> production-grade MCP penetration test stack (MasterMCP
> [35]) with a local egress sink and a fake MCP server for
> reproducibility.
**Matched Term**: `Evasion` | **Location**: `B. Attack Suite (Templates and Instantiation)` [offsets: 19779:20190]
> d) Evasion parameters:
> All templates support filler
> steps, randomized inter-step delays, endpoint churn, and
> prompt paraphrase/translation to stress text-only guards while
> preserving protocol behavior.
> 
> We next present the system design: how AegisMCP in-
> struments MCP to emit NEBULA events, builds streaming
> heterogeneous graphs, and fuses novelty, with attribute signals
> for CPU-only near-real-time detection.
**Matched Term**: `Evasion` | **Location**: `C. Robustness, Evasion, and Mitigations` [offsets: 48185:48498]
> C. Robustness, Evasion, and Mitigations
> 
> a) Slow-roll and cross-window attacks: Adversaries may
> distribute steps across windows/sessions. Session-DAG fea-
> tures already aggregate within windows; extending fusion with
> short window sequences or a lightweight temporal head would
> better capture slow-roll strategies.
**Matched Term**: `evasion` | **Location**: `C. Robustness, Evasion, and Mitigations` [offsets: 49301:49615]
> e) Adversarial ML: Graph poisoning/evasion (e.g., ad-
> versarial edges) could bias embeddings or suppress scores.
> Robust training (edge-dropout, adversarial negatives), conser-
> vative novelty weighting, and guardrail escalators for high-risk
> motifs (e.g., install then egress to a new domain) reduce
> susceptibility.
**Matched Term**: `adaptive` | **Location**: `D. Limitations and Threats to Validity` [offsets: 50561:50766]
> Heavier
> temporal
> GNNs
> (e.g.,
> TGNs) may improve long-horizon recall at higher cost.
> Our hybrid “Lite-F + GraphSAGE” design is a practical
> compromise;
> adaptive
> routing
> could
> allocate
> compute
> dynamically.
> 
> E.
