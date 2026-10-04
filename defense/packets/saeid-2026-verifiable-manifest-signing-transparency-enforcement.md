# Evidence Locator Packet: saeid-2026-verifiable-manifest-signing-transparency-enforcement

- **Title**: Verifiable Manifest Signing and Transparency Enforcement for Secure MCP-Based LLM Pipelines
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2601.23132
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\saeid-2026-verifiable-manifest-signing-transparency-enforcement\fulltext.txt
- **Character Count**: 91852

## Block 2: Contribution Sentences
**Location**: `Abstract—Large Language Models (LLMs) are increasingly` [offsets: 873:958]
> This paper
> introduces a manifest-level enforcement layer for MCP-based
> LLM pipelines.

## Block 3: Method Locator
**Section Heading**: `architecture based on authenticated data structures and zero-` [section offsets: 10677:10911]
**First 120 words verbatim** [offsets: 10677:11675]
> architecture based on authenticated data structures and zero-
> knowledge proofs. Although TAP improves verifiability in
> structured multi-user systems, its applicability to dynamic
> LLM execution and tool orchestration remains limited.
> 
> B. Runtime Attestation and Secure Execution
> 
> Several studies investigate runtime integrity and attestation
> in distributed environments. Su et al. [21] propose contin-
> uous verification mechanisms for cloud workloads, while
> Scanclave [22] leverages enclave-based protection for se-
> cure execution. These approaches improve infrastructure-level
> trust and execution integrity; however, they do not explicitly
> address LLM-specific execution semantics, e.g., adversarial
> prompts, chained tool interactions, probabilistic runtime be-
> havior, and manifest-level policy enforcement. In addition,
> enclave-dependent architectures may introduce scalability and
> deployment constraints in heterogeneous LLM ecosystems.
> 
> C. Adversarial Tool Invocation and Prompt Security
> 
> Other
**Section Heading**: `III. PROPOSED METHODOLOGY` [section offsets: 13621:15793]
**First 120 words verbatim** [offsets: 13621:14516]
> III. PROPOSED METHODOLOGY
> 
> This section presents the proposed manifest-level enforce-
> ment approach for MCP-based, tool-integrated LLM pipelines.
> The approach focuses on a single execution artifact: the MCP
> tool-use manifest. Although digital signatures, runtime veri-
> fication, transparency logs, and audit records are established
> security primitives, their role in this work is to enforce the
> integrity and authorization status of MCP manifests before tool
> execution. Thus, the contribution is not a new cryptographic
> primitive, but an MCP-specific enforcement workflow that
> binds each tool invocation to a canonical, policy-compliant,
> freshness-valid, and verifiable manifest. Rather than modify-
> ing the core MCP interaction model, the proposed approach
> strengthens the execution layer by requiring every tool request
> to pass through manifest-centered authorization. As illustrated
> in Figure
**Section Heading**: `IMPLEMENTATION AND EXPERIMENTAL CONFIGURATION` [section offsets: 37410:42279]
**First 120 words verbatim** [offsets: 37410:38422]
> IMPLEMENTATION AND EXPERIMENTAL CONFIGURATION
> 
> Component
> Configuration
> 
> Hash function
> SHA-256 / specify actual implementation
> Signature scheme
> ECDSA / Ed25519 / specify actual scheme
> Key management
> HSM-backedandHSM-simulated signing module
> Transparency log
> Merkle-tree-based append-only log
> LLM backends
> GPT 5.3, LLaMA-3.5, DeepSeek-V3
> Workload sizes
> 100–50,000 manifest instances
> Prompting setting
> Structured zero-shot prompt
> Prompt template
> Same template applied across all LLM backends
> Temperature
> Specify actual value
> Top-p
> Specify actual value
> Maximum tokens
> Specify actual value
> Repetitions
> Specify number of independent runs
> Random seed
> Specify seed if used
> Execution environment
> CPU/GPU, RAM, OS, Python version
> 
> 5.3,
> tool_id=finance_risk_api,
> requested_scope={read,
> analyze},
> policy_id=POL-03,
> and
> execution_mode=verified_tool_call; and a fresh-
> ness component with timestamp 2026-05-06T14:22:10Z
> and epoch_window=300. This example illustrates how
> Mu, Mm, and τ are separated before hashing and signing,

## Block 4: Evaluation Locator
**Section Heading**: `experiments across healthcare, financial, RAG, and multi-agent` [section offsets: 1936:2370]
**First 120 words verbatim** [offsets: 1936:2933]
> experiments across healthcare, financial, RAG, and multi-agent
> scenarios show that manifest-level cryptographic enforcement can
> provide low-overhead, traceable, and auditable execution control
> for heterogeneous LLM-tool pipelines.
> 
> arXiv:2601.23132v2  [cs.CR]  24 Jun 2026
> 
> Index Terms—Model Context Protocols (MCPs), Scalability,
> Statistical Validation, Security Analysis, Transparency Logs,
> Verification Frameworks, Trustworthy AI
> 
> I. INTRODUCTION
> 
> Large Language Models (LLMs) are increasingly integrated
> into tool-driven environments, including healthcare analyt-
> ics, financial systems, and autonomous decision-support plat-
> forms [1]–[3]. In these settings, LLMs no longer operate as
> isolated conversational systems; instead, they interact with ex-
> ternal tools, APIs, databases, retrieval engines, and execution
> services [4], [5]. Consequently, the reliability and security
> of the execution pipeline become as critical as the model’s
> reasoning capability. A correct model response may still
**Section Heading**: `IV. EXPERIMENTAL SETUP` [section offsets: 34276:34449]
**First 120 words verbatim** [offsets: 34276:35185]
> IV. EXPERIMENTAL SETUP
> 
> The proposed solution is evaluated in terms of scalability,
> execution overhead, verification correctness, transparency log-
> ging, and auditability.
> 
> A. Experimental Evaluation
> 
> The experimental evaluation assesses the proposed solution
> in terms of scalability, verification stability, transparency-
> log behavior, prompt-to-manifest transformation, violation en-
> forcement, and auditability under increasing workload. The
> evaluation focuses on the manifest-execution layer, where
> LLM-generated tool requests are treated as manifest candi-
> dates rather than executable commands. Execution is permitted
> only after policy validation, signing, verification, transparency
> logging, and audit export. The workload model is defined as:
> 
> W = {w1, w2, . . . , wn},
> 
> wi ∈{100, 500, 1000, 5000, 10000, 20000, 50000}.
> (44)
> 
> Each workload size wi represents an independent batch
> of manifest instances
**Section Heading**: `A. Experimental Evaluation` [section offsets: 34449:34721]
**First 120 words verbatim** [offsets: 34449:35361]
> A. Experimental Evaluation
> 
> The experimental evaluation assesses the proposed solution
> in terms of scalability, verification stability, transparency-
> log behavior, prompt-to-manifest transformation, violation en-
> forcement, and auditability under increasing workload. The
> evaluation focuses on the manifest-execution layer, where
> LLM-generated tool requests are treated as manifest candi-
> dates rather than executable commands. Execution is permitted
> only after policy validation, signing, verification, transparency
> logging, and audit export. The workload model is defined as:
> 
> W = {w1, w2, . . . , wn},
> 
> wi ∈{100, 500, 1000, 5000, 10000, 20000, 50000}.
> (44)
> 
> Each workload size wi represents an independent batch
> of manifest instances processed through the full execution
> pipeline in Algorithms 1-3. The workloads are synthetic
> and application-independent to isolate scalability, runtime
> overhead, verification
**Section Heading**: `evaluation focuses on the manifest-execution layer, where` [section offsets: 34721:37410]
**First 120 words verbatim** [offsets: 34721:35604]
> evaluation focuses on the manifest-execution layer, where
> LLM-generated tool requests are treated as manifest candi-
> dates rather than executable commands. Execution is permitted
> only after policy validation, signing, verification, transparency
> logging, and audit export. The workload model is defined as:
> 
> W = {w1, w2, . . . , wn},
> 
> wi ∈{100, 500, 1000, 5000, 10000, 20000, 50000}.
> (44)
> 
> Each workload size wi represents an independent batch
> of manifest instances processed through the full execution
> pipeline in Algorithms 1-3. The workloads are synthetic
> and application-independent to isolate scalability, runtime
> overhead, verification consistency, logging behavior, and
> latency stability; real-world MCP deployments are therefore
> treated as validation and discussed as limitations. Because the
> proposed solution targets LLM-assisted tool invocation, each
> experiment begins with

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
**Location**: `evaluation was not only to measure computational scalability` [offsets: 53583:53712]
> In contrast
> to baseline MCP execution pipelines, execution requests were
> not forwarded directly to tools after prompt generation.

## Block 7: Cost Excerpts
**Location**: `experiments across healthcare, financial, RAG, and multi-agent` [offsets: 1936:2166]
> experiments across healthcare, financial, RAG, and multi-agent
> scenarios show that manifest-level cryptographic enforcement can
> provide low-overhead, traceable, and auditable execution control
> for heterogeneous LLM-tool pipelines.
**Location**: `IV. EXPERIMENTAL SETUP` [offsets: 34300:34447]
> The proposed solution is evaluated in terms of scalability,
> execution overhead, verification correctness, transparency log-
> ging, and auditability.
**Location**: `evaluation focuses on the manifest-execution layer, where` [offsets: 35251:35508]
> The workloads are synthetic
> and application-independent to isolate scalability, runtime
> overhead, verification consistency, logging behavior, and
> latency stability; real-world MCP deployments are therefore
> treated as validation and discussed as limitations.
**Location**: `Evaluation Focus` [offsets: 48922:49122]
> Predicted
> and observed execution behavior also remained consistent,
> with anomaly rates below 2%, supporting runtime monitoring
> of abnormal delays, throttling effects, and resource-exhaustion
> symptoms.
**Location**: `Evaluation Focus` [offsets: 49123:49266]
> Moreover, verification latency, output-size behav-
> ior, and execution overhead remained bounded and predictable
> across the evaluated workloads.
**Location**: `evaluation,` [offsets: 50327:50364]
> Execution time per LLM across scales.

## Block 8: Limitations
**Section Heading**: `Limitations` [section offsets: 74949:77886]
**First 120 words verbatim** [offsets: 74949:75950]
> Limitations
> 
> No cryptographic verifica-
> tion and auditability
> Chernyshev
> et
> al.
> (2023) [40]
> 
> Reactive only; no runtime
> enforcement
> Duddu et al. (2024) [41]
> Verifiable ML attestations
> Hardware-assisted
> integrity guarantees
> 
> Claude MCP
> Native
> MCP-
> compatible
> manifest
> structure
> 
> LangChain Agents
> Custom
> manifest
> adapter required
> 
> AutoGen
> Custom
> multi-agent
> manifest
> wrapper
> required
> 
> OpenRouter Routing
> Partial through routing
> metadata
> 
> Cruciani
> &
> Verdecchia
> (2025) [39]
> 
> Energy-efficient LLM se-
> lection
> 
> Sustainability-oriented
> optimization
> 
> LLM forensic analysis
> Retrospective trace recon-
> struction
> 
> This Work
> Secure and auditable LLM
> execution pipeline
> 
> randomized scheduling may therefore help reduce regular tim-
> ing patterns and workload bursts without affecting verification
> correctness and auditability. Transparency logging and audit
> validation remained computationally practical at larger scales.
> The Merkle-based logging structure preserved compact proof
> generation and bounded verification

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `M. A. Hamdaqa is with the SæT Laboratory, Polytechnique Montr´eal,` [offsets: 8257:8882]
> Experimental findings demonstrate
> near-linear scalability (R2 = 0.998), stable verification behav-
> ior as workload size increases, effective rejection of malformed
> and policy-violating manifests, and balanced utilization across
> the evaluated LLMs. The results also reveal deployment-level
> considerations, e.g., key allocation imbalance, which motivate
> adaptive key management and rotation strategies in future
> MCP-based execution systems.
> 
> • We introduce a manifest-level enforcement approach for
> MCP-based LLM tool pipelines that treats each tool-use
> manifest as a first-class security object before execution
> authorization.
**Matched Term**: `adaptive` | **Location**: `E. Key Usage, Log Growth, and Timestamp Distribution` [offsets: 60028:60570]
> A chi-square test confirms significant deviation
> across workload scales (Table XIII; χ2(6, N = 55000) =
> 312.7, p < 0.001), indicating that key allocation diverges
> from a uniform distribution.
> The low-key fairness score
> (K = 0.42) indicates a growing concentration of signing
> keys during high-volume execution, creating a deployment-
> level risk that motivates adaptive key rotation, quota balancing,
> and workload-aware key selection. In contrast, transparency-
> log growth remained stable and nearly linear in the log–
> 
> --- PAGE BREAK ---
> 
> Fig.
**Matched Term**: `adaptive` | **Location**: `VII. DISCUSSION` [offsets: 73689:74154]
> Revocation-related synchronization delays were a major
> source of verification failures, especially for dev-k2. Al-
> though verification success remained statistically stable (Ps ≈
> 0.8), the results show that distributed key synchronization,
> revocation propagation, adaptive key rotation, and workload-
> aware key selection are important for large-scale reliability.
> Another key finding is that balanced LLM utilization does not
> imply balanced signing-key utilization.
**Matched Term**: `adaptive` | **Location**: `A. Internal Validity` [offsets: 78304:78926]
> Internal validity concerns whether the observed results re-
> flect the behavior of the proposed solution rather than artifacts
> of the experimental setup. The main limitation is the reliance
> on synthetic, scale-based workloads, which enable controlled
> evaluation but may not fully capture bursty, adaptive, and
> adversarial traffic patterns in production environments. To mit-
> igate this risk, the evaluation used repeated execution rounds,
> randomized workload sampling, and multiple statistical val-
> idation procedures; however, future work should include ad-
> versarial traffic generation and stochastic workload simulation.
**Matched Term**: `adaptive` | **Location**: `IX. FUTURE WORK` [offsets: 81454:82044]
> Future work will extend the proposed solution toward real-
> world MCP deployments, multi-cloud infrastructures, and het-
> erogeneous LLM execution environments. Additional studies
> should investigate adaptive key management, workload-aware
> key rotation, dynamic orchestration policies, and revocation
> synchronization to reduce signing-key concentration and im-
> prove deployment-level reliability. Further research should
> also evaluate broader adversarial scenarios, including insider
> threats, compromised components, replay behavior, adversarial
> traffic bursts, and timing-correlation attacks.
**Matched Term**: `adaptive` | **Location**: `X. CONCLUSION` [offsets: 83069:83720]
> At the same time, the results identified important
> deployment-level considerations, including signing-key con-
> centration, revocation-synchronization delays, and timestamp
> variability under higher workloads. These findings indicate
> that balanced model utilization does not automatically guar-
> antee balanced key usage, and that adaptive key-management
> and scheduling policies are necessary for large-scale deploy-
> ment. Overall, the proposed solution provides a scalable and
> transparent execution-layer foundation for trustworthy MCP-
> based LLM pipelines, while motivating further validation in
> real-world, adversarial, and heterogeneous environments.
