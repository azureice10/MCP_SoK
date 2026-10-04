# Evidence Locator Packet: kiarash-2026-trustworthy-ai-llm-scalability-risk

- **Title**: Trustworthy AI LLM Scalability Risk Index (LSRI): A Cybersecurity Framework Assessing Agentic-AI Security & Software Model Supply Chain Safety Boosting AI-Generated Malware Defense & Explainability Mitigating Emerging Risks of Generative AI
- **Year**: 2026
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: position_other
- **Link**: https://arxiv.org/abs/2602.19021
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\kiarash-2026-trustworthy-ai-llm-scalability-risk\fulltext.txt
- **Character Count**: 72197

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 338:1348]
> Abstract
> 
> 1
> Introduction
> 
> 1
> 
> Mitigating Emerging Risks of Generative AI
> 
> 1Virelya Intelligence Research Labs, San Francisco Bay Area, California
> 2,3Google, Mountain View, California
> 1{ahi@virelya.org, kiarash.ahi@uconn.edu}, 2{varawal@google.com},
> 3{svalizadeh@google.com, saeed.valizadeh@uconn.edu}
> 
> As AI shifts from human-in-the-loop interfaces to autonomous multi-agent systems capable of real-time code
> execution and tool integration through protocols like the Model Context Protocol (MCP), traditional SAST, DAST,
> and legacy AI safety methods fail to detect modern agentic-AI threats. This paper introduces the LLM Scalability
> Risk Index (LSRI), a parametric framework and cybersecurity standard for stress-testing autonomous orchestration
> pipelines. LSRI measures the operational thresholds where load, compounding hallucinations, data poisoning, and
> adversarial prompt injections including jailbreaking and indirect prompt injection cause security boundaries to fail.
> 
> Beyond RLHF and RLAIF, we present
**Location**: `Introduction` [offsets: 1338:2240]
> we present a Verifiable Root of Trust architecture using cryptographic attestation,
> semantic policy enforcement, and continuous runtime verification to secure the AI software supply chain. LSRI
> defends against malicious LoRA adapters, weight tampering, dependency typosquatting, and unsafe model artifacts
> from public registries such as Hugging Face and GitHub. By replacing post-hoc alignment with verifiable runtime
> controls, LSRI provides scalable API defense, safer agentic orchestration under heavy cloud workloads, stronger
> polymorphic malware detection, automated red-teaming, and improved system explainability.
> 
> Oriented alongside NIST AI RMF, OWASP Top 10 for LLMs, and ISO 42001, LSRI establishes a deployable
> compliance baseline for securing generative AI ecosystems including ChatGPT, GPT-4o, Claude 3.5 Sonnet, Copi-
> lot, LLaMA, Gemini, and Bedrock. LSRI also supports capital market risk

## Block 3: Method Locator
**Section Heading**: `A Standard Cybersecurity Framework for Assessing` [section offsets: 71:338]
**First 120 words verbatim** [offsets: 71:1083]
> A Standard Cybersecurity Framework for Assessing
> Agentic-AI Security and Software Model Supply Chain Safety,
> Boosting AI-Generated Malware Defense and Explainability for
> 
> Kiarash Ahi1, Vaibhav Agrawal2, and Saeed Valizadeh3
> 
> arXiv:2602.19021v2  [cs.CR]  20 Jul 2026
> 
> Abstract
> 
> 1
> Introduction
> 
> 1
> 
> Mitigating Emerging Risks of Generative AI
> 
> 1Virelya Intelligence Research Labs, San Francisco Bay Area, California
> 2,3Google, Mountain View, California
> 1{ahi@virelya.org, kiarash.ahi@uconn.edu}, 2{varawal@google.com},
> 3{svalizadeh@google.com, saeed.valizadeh@uconn.edu}
> 
> As AI shifts from human-in-the-loop interfaces to autonomous multi-agent systems capable of real-time code
> execution and tool integration through protocols like the Model Context Protocol (MCP), traditional SAST, DAST,
> and legacy AI safety methods fail to detect modern agentic-AI threats. This paper introduces the LLM Scalability
> Risk Index (LSRI), a parametric framework and cybersecurity standard for stress-testing autonomous orchestration
**Section Heading**: `Methodology` [section offsets: 5276:5291]
**First 120 words verbatim** [offsets: 5276:6148]
> Methodology
> 
> 3
> Background and Literature Review
> 
> 3.1
> Evolution and Capabilities of LLMs
> 
> 2
> 
> This paper employs a multi-pronged methodology combining empirical analysis, literature synthesis, and policy eval-
> uation:
> 
> • Literature Survey: We analyzed 80 peer-reviewed papers, policy documents, and technical reports published
> between 2018–2025, focusing on dual-use LLMs, adversarial robustness, and AI governance.
> 
> • Threat Categorization: Attack vectors were organized using a structured adversarial taxonomy derived from
> [17], [18], [20], and cross-referenced with OWASP’s LLM Top 10 and NIST AI RMF 1.0.
> 
> • Policy Maturity Matrix: Governance frameworks were scored based on enforcement level, coverage of LLM-
> specific risks, and implementation transparency, weighted equally across five pillars.
> 
> • LSRI Design: The LLM Scalability Risk Index (LSRI) was developed as a
**Section Heading**: `Method` [section offsets: 33792:55196]
**First 120 words verbatim** [offsets: 33792:34705]
> Method
> Recall (Zero-Day)
> Avg Latency (ms)
> False Positives
> Interpretability
> 
> Static Analyzers
> 62%
> 80
> 11%
> Limited
> LLM + Symbolic Hybrid
> 88%
> 105
> 13%
> Moderate (SHAP)
> LLM + Graph-Based
> 91%
> 96
> 12%
> High (CySecBench)
> 
> • Code scanning at every commit, flagging insecure patterns and suggesting remediations in real time.
> 
> • Analyzing dependency trees to identify vulnerable or outdated libraries before code reaches production.
> 
> Prominent platforms have already begun integrating these capabilities. GitLab’s Auto DevSecOps system employs
> GPT-based models for dynamic scanning and compliance-as-code enforcement. Similarly, Microsoft’s Azure DevOps,
> in collaboration with OpenAI, leverages LLMs for predictive vulnerability scoring, contextual remediation advice, and
> automated security testing.
> 
> These integrations shift security from a reactive checkpoint to a proactive, continuous layer—built directly into the
> tooling

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `Introduction` [offsets: 3523:3837]
> We explore their dual-use nature, recent industry and academic advances, and how both defenders and
> adversaries leverage these models for tasks such as code generation, malware design, zero-day detection, and De-
> vSecOps, supported by architectural comparisons, benchmark studies, and cross-industry case examples.
**Location**: `Introduction` [offsets: 4013:4205]
> To guide the reader, the paper is structured as follows:
> Methodology in Brief—We analyzed 80 peer-reviewed papers and industry datasets, built a Policy Maturity Matrix,
> and supply-chain risks.
**Location**: `Background and Literature Review` [offsets: 11095:11285]
> Benchmarks such as PINT and recent tools have emerged to systematically test defenses against prompt injection and
> jailbreak attacks, measuring both false positives and false negatives [69].
**Location**: `LLM Technology` [offsets: 28242:28516]
> Benchmarking & Evaluation: CySecBench (Security Benchmarks)
> 
> Training & Education: CyberMentor (Explainable Guidance)
> 
> Governance & Compliance: CKC, AI Model Cards (Ethical Auditing)
> 
> Figure 1: Categorization of explainability tools used in LLM-driven cybersecurity systems.
**Location**: `Method` [offsets: 35054:35318]
> • Structured red teaming to stress-test model behavior against adversarial use cases,
> 
> • Staged release strategies to control the dissemination of high-risk capabilities, and
> 
> • Model Watermarking to allow for the traceability of content generated by a model [46].
**Location**: `Method` [offsets: 37692:37769]
> • Centralized auditing repositories to detect and flag unsafe usage patterns.

## Block 6: Baseline Excerpts
**Location**: `Introduction` [offsets: 1959:2201]
> Oriented alongside NIST AI RMF, OWASP Top 10 for LLMs, and ISO 42001, LSRI establishes a deployable
> compliance baseline for securing generative AI ecosystems including ChatGPT, GPT-4o, Claude 3.5 Sonnet, Copi-
> lot, LLaMA, Gemini, and Bedrock.
**Location**: `Background and Literature Review` [offsets: 6377:6651]
> • Supply-Chain Analysis and Systems Synthesis: We analyzed prior work on model integrity, data poison-
> ing, weight tampering, and agentic vulnerabilities to define the LLM supply chain as a lifecycle-spanning sys-
> tem covering build-time artifacts and run-time dependencies.
**Location**: `LLM Technology` [offsets: 20714:20898]
> Note: For the purposes of this study, we utilize a baseline where wi = 1
> 
> m
> Y
> 
> Φ =
> 
> j=1
> 
> Where:
> 
> 4.5.1
> Risk Mapping Functions (fi)
> 
> fsig(x) =
> 1
> 
> fexp(x) = e−x
> 
> (
> 
> fstep(x) =
> 
> 6
> 
> n
> X
> 
> !
**Location**: `LLM Technology` [offsets: 21863:22010]
> Throughput values exceeding λ asymptotically reduce risk toward zero, reflecting diminishing marginal scalability
> risk beyond industrial baselines.
**Location**: `LLM Technology` [offsets: 24368:24533]
> Throughput x is measured as sustained inference requests per day, normalized against an industrial baseline λ
> representing large-scale app-store or CI/CD deployment.
**Location**: `LLM Technology` [offsets: 24679:24959]
> While Table 3 provides baseline parameters for a high-throughput mobile ecosystem,
> the framework is designed for Sensitivity Analysis, allowing architects to stress-test how specific metric fluctuations
> (e.g., a 20% increase in latency) impact the overall deployment risk profile.

## Block 7: Cost Excerpts
**Location**: `Introduction` [offsets: 1315:1526]
> Beyond RLHF and RLAIF, we present a Verifiable Root of Trust architecture using cryptographic attestation,
> semantic policy enforcement, and continuous runtime verification to secure the AI software supply chain.
**Location**: `Introduction` [offsets: 1700:1957]
> By replacing post-hoc alignment with verifiable runtime
> controls, LSRI provides scalable API defense, safer agentic orchestration under heavy cloud workloads, stronger
> polymorphic malware detection, automated red-teaming, and improved system explainability.
**Location**: `Background and Literature Review` [offsets: 10280:10380]
> have
> demonstrated that these frameworks preserve privacy while maintaining model utility [13], [14].
**Location**: `Background and Literature Review` [offsets: 11095:11285]
> Benchmarks such as PINT and recent tools have emerged to systematically test defenses against prompt injection and
> jailbreak attacks, measuring both false positives and false negatives [69].
**Location**: `LLM Technology` [offsets: 18367:18501]
> Real-world deployment requires low-latency inference, cost-effective
> infrastructure, and high throughput across diverse architectures.
**Location**: `LLM Technology` [offsets: 18502:18756]
> For instance, scanning millions of apps in the Google
> Play or Apple App Store for malware necessitates robust resource allocation and distributed serving to ensure infer-
> ences complete within milliseconds while remaining resilient to adversarial inputs.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Introduction` [offsets: 4793:5689]
> It outlines a roadmap for establishing a “verifiable root of trust” through cryptographic attestation
> and semantic policy enforcement. Section VI concludes the paper by summarizing our primary two contributions, and
> finally, Section VII discusses the policy and practice implications for stakeholders navigating the rising complexity
> of LLM-powered cybersecurity ecosystems and proposing a governance roadmap rooted in explainability, federated
> learning, and adaptive resilience.
> 
> 2
> Methodology
> 
> 3
> Background and Literature Review
> 
> 3.1
> Evolution and Capabilities of LLMs
> 
> 2
> 
> This paper employs a multi-pronged methodology combining empirical analysis, literature synthesis, and policy eval-
> uation:
> 
> • Literature Survey: We analyzed 80 peer-reviewed papers, policy documents, and technical reports published
> between 2018–2025, focusing on dual-use LLMs, adversarial robustness, and AI governance.
**Matched Term**: `evade` | **Location**: `Background and Literature Review` [offsets: 14109:14513]
> Security researchers report that these “dark LLMs” are increasingly optimized to evade endpoint detection and
> static analysis through polymorphic payloads and context-aware generation [65]–[66]. Simultaneously, deepfake mul-
> timedia amplifies social engineering; for instance, a Ferrari executive was targeted by a CEO voice-clone, which failed
> only when the AI could not answer a specific question [67].
**Matched Term**: `Evasion` | **Location**: `Method` [offsets: 38933:39224]
> • Model Evasion and Robustness: Continuously evaluating and hardening defensive LLMs against adversarial
> evasion techniques specifically designed to bypass AI-based detection [8], [17]. Fine-tuned LLM models with a
> labeled dataset can be used to detect against prompt injection attacks [53].
**Matched Term**: `evasion` | **Location**: `Method` [offsets: 40174:40516]
> --- PAGE BREAK ---
> 
> While all these risks manifest across multiple layers from prompt injection and adversarial evasion to governance
> and compliance failures, many of them ultimately trace back to weaknesses in how LLMs are built and distributed.
> The LLM supply chain from data collection to model release is a critical vector for compromise.
**Matched Term**: `evade` | **Location**: `Method` [offsets: 40517:40814]
> Attackers can
> inject poisoned samples during pre-training, introduce malicious fine-tuning data, or distribute backdoored weights
> via public repositories. Recent research shows minor dataset manipulations can induce persistent “logic bombs” that
> evade traditional red-teaming [61].
> 
> Tram`er et al.
**Matched Term**: `evasion` | **Location**: `Method` [offsets: 52620:52988]
> 1. From Adversarial ML to Cyber Threat Inflation: Traditional adversarial machine learning has largely fo-
> cused on perturbation-based attacks and evasion of fixed classifiers under bounded threat models. These frame-
> works assume that adversarial effort scales linearly with attack complexity and that model misuse requires
> 
> --- PAGE BREAK ---
> 
> significant expertise.
**Matched Term**: `evasion` | **Location**: `Method` [offsets: 52989:53542]
> LLMs invalidate these assumptions by enabling the low-cost, automated generation of
> polymorphic malware, exploits, and social-engineering artifacts. As a result, the dominant challenge is no
> longer isolated evasion, but cyber threat inflation, where the marginal cost of producing diverse and adaptive
> attacks approaches zero. Addressing this shift requires research agendas that emphasize systemic resilience,
> rate-limiting of attack generation, and defenses robust to continuously evolving threat distributions rather than
> static adversarial examples.
**Matched Term**: `Adaptive` | **Location**: `Method` [offsets: 54417:54800]
> 3. From Static Robustness to Adaptive Resilience: Conventional cyber defenses rely heavily on static signatures,
> fixed rule sets, and periodic retraining cycles, reflecting an assumption that threat evolution is incremental
> and observable. LLM-enabled attackers undermine this model by rapidly generating novel attack variants and
> adapting behaviors in response to deployed defenses.
**Matched Term**: `adaptive` | **Location**: `Method` [offsets: 54801:55434]
> Similarly, LLM-based defensive systems may themselves
> evolve through continual learning, fine-tuning, or agentic feedback loops. These dynamics require a move
> toward adaptive and lifelong robustness, where defensive mechanisms continuously update their detection logic,
> threat models, and trust assumptions in response to both environmental changes and emergent supply-chain
> vulnerabilities.
> 
> 6
> Conclusion and Research Implications
> 
> 6.1
> Design Constraints for Feasible AI Governance
> 
> 16
> 
> The integration of large language models into cybersecurity represents a structural shift in both the threat landscape
> and the defensive toolkit.
**Matched Term**: `Adaptive` | **Location**: `Conclusion and Research Implications` [offsets: 58591:58914]
> Adaptivity: Static compliance checklists cannot keep pace with agentic threat evolution. Effective governance
> must support Adaptive Enforcement, where trust assumptions—quantified via parametric models like the LSRI
> (Eq. 1), evolve in response to real-time telemetry such as latency shifts or supply-chain integrity alerts.
