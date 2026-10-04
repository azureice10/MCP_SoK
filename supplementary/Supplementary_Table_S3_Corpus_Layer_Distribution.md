# Supplementary Document S3: Layer Distribution Analysis of the Academic Synthesis Corpus (N = 171)

**Supporting Document for:** *Security of Model Context Protocol in Agentic AI Systems: A Systematization of Knowledge on Threats, Trust Boundaries, and Defense Mechanisms*  
**Date of Audit:** October 2026  
**Corpus Scope:** 171 MCP-Specific Academic and Archival Records (Excluding Set B and External Validation Set E4)

---

## 1. Executive Summary & Distribution Overview

This supplementary document provides transparent audit documentation for the claim presented in **Section 4.3 (Two complementary evidence streams)** of the main manuscript:

> *"In our layer coding of the corpus, 91 of the 171 records (53.2%) focus primarily on Layer A (indirect prompt injection and semantic tool poisoning). In the validation set, no record carries a Layer A class as its only label... Under primary labels, Layer C accounts for 18 of the 22 records (81.8%)."*

### Layer Distribution across Corpus (N = 171)

| Layer | Primary Focus Description | Academic Records (N = 171) | Share (%) |
|:---|:---|:---:|:---:|
| **Layer A** | **Semantic Channel (Prompt Injection, Context Dilation, & Tool Poisoning)** | **91** | **53.2%** |
| **Layer C** | **Transport, Authorization, & Sink Enforcement Flaws** | **70** | **40.9%** |
| **Layer D** | **Cross-Server Composition, Taint Propagation, & Supply Chain** | **8** | **4.7%** |
| **Layer B** | **State, Descriptors, & Temporal Drift / Schema Mutation** | **2** | **1.2%** |
| **Total** | **All Layers (Single Primary Label per Record)** | **171** | **100.0%** |

*(Note: Under multi-label coding where studies evaluate defenses spanning multiple layers, Layer A appears in 59 records [34.5%], Layer B in 31 [18.1%], Layer C in 53 [31.0%], and Layer D in 44 [25.7%]).*

---

## 2. Breakdown of the 91 Layer A Academic Records by Role

The 91 academic records concentrating primarily on Layer A encompass both defensive interventions and offensive/measurement evaluations:

| Role (Peran) | Count | Description / Representative Examples |
|:---|:---:|:---|
| **Primary Defenses (defense_primary)** | **55** | Content inspection, prompt guardrails, TAE attention monitors (e.g., MindGuard, FlowGuard, Beyond Detection, ADR) |
| **Conceptual Proposals (proposal_only, L0)** | **9** | Unimplemented architectures proposing semantic filtering and safe prompt boundaries |
| **Attack Studies (attack)** | **9** | Empirical attack methodologies targeting the model-planner interface (e.g., GAPMA/MPMA, BiasAgent, MCPTox exploits) |
| **Benchmarks & Measurements (benchmark_measurement)** | **8** | Evaluation suites and susceptibility measurements for prompt injection (e.g., MCPTox, ToolSandbox, Invariant prompt suites) |
| **Secondary Defenses (defense_secondary)** | **4** | Broader agent architectures featuring specialized prompt sanitization layers |
| **Surveys & Systematic Reviews (survey_review)** | **4** | Syntheses primarily focused on LLM prompt injection and semantic agent safety |
| **Position & Specification Framing (position_other)** | **2** | Architectural frameworks discussing semantic trust boundaries |
| **Total Layer A Academic Records** | **91** | **53.2% of the synthesis corpus (N = 171)** |

---

## 3. Complete Manifest of the 91 Layer A Academic Records

| # | Record Identifier (`record_id`) | Title | Year | Tier | Role (`peran`) | Claimed / Evaluated Classes |
|:---:|:---|:---|:---:|:---:|:---|:---|
| 1 | `addressing-security-gaps-2025` | Addressing Security Gaps in MCP: Design of a Resilient Reference Architecture | 2025 | E1 | proposal_only | A1;C3;D3 / nan |
| 2 | `aditi-2025-model-context-protocol-vision-systems` | Model Context Protocol for Vision Systems: Audit, Security, and Protocol Extensions | 2025 | E2 | proposal_only | A3;B3;C5 / nan |
| 3 | `agentic-security-validation-2026` | Agentic Security Validation Framework for Retrieval-Augmented and Tool-Enabled Large Language Model Systems | 2026 | E1 | defense_primary | A1;A2;D1;D2 / A1;A2 |
| 4 | `alfonso-2026-mcp-seclint-open-source-static` | MCP-SecLint: An Open-Source Static Analyzer for Detecting Vulnerabilities in LLM Tool Integrations | 2026 | E1 | defense_primary | C5;C3 / C5;C3 |
| 5 | `alfredo-2026-attested-tool-server-admission-security` | Attested Tool-Server Admission: A Security Extension to the Model Context Protocol | 2026 | E2 | defense_primary | B1;B2 / B1;B2 |
| 6 | `anthropic-2024-model-context-protocol-specification-architecture` | Model Context Protocol Specification (Architecture & Security) | 2024 | E3 | position_other | nan / nan |
| 7 | `arash-2025-mcp-bridge-lightweight-llm-agnostic` | MCP Bridge: A Lightweight, LLM-Agnostic RESTful Proxy for Model Context Protocol Servers | 2025 | E2 | position_other | nan / nan |
| 8 | `attestation-aware-authorization-for-2026` | Entitlement-Aware Authorization for MCP-Based AI Search and Chat Systems | 2026 | E1 | defense_primary | C1;C2;C3 / C1;C2;C3 |
| 9 | `auditing-mitigating-and-2026` | Auditing, Mitigating, and Ensuring Accountability for Poisoning Attacks in Multi-modal Agent Systems Using MCP Servers | 2026 | E1 | survey_review | nan / nan |
| 10 | `baichao-2026-flowguard-signals-evidence-mcp-security` | FlowGuard: From Signals to Evidence for MCP Security Detection | 2026 | E2 | defense_primary | A1;A2;C3;C5 / A1;A2;C3;C5 |
| 11 | `beyond-detection-autonomous-2026` | Beyond Detection: Autonomous Anomaly Remediation for MCP Against Tool Poisoning Attacks | 2026 | E1 | defense_primary | A1;A2 / A1;A2 |
| 12 | `beyond-the-protocol-unveiling-2026` | Beyond the Protocol: Unveiling Attack Vectors in the Model Context Protocol (MCP) Ecosystem | 2026 | E1 | attack | nan / nan |
| 13 | `biasagent-exploiting-agent-2026` | BiasAgent: Exploiting Agent Bias for Preference Manipulation Attacks on Model Context Protocol | 2026 | E1 | attack | nan / nan |
| 14 | `bin-2025-mcpguard-automatically-detecting-vulnerabilities-mcp` | MCPGuard : Automatically Detecting Vulnerabilities in MCP Servers | 2025 | E2 | survey_review | nan / nan |
| 15 | `biwei-2025-mcp-not-stand-misuse-cryptography` | "MCP Does Not Stand for Misuse Cryptography Protocol": Uncovering Cryptographic Misuse in Model Context Protocol at Scale | 2025 | E2 | defense_primary | C3;C5 / C3;C5 |
| 16 | `charoes-2026-ai-assisted-development-tools-immune` | Are AI-assisted Development Tools Immune to Prompt Injection? | 2026 | E2 | attack | nan / nan |
| 17 | `charoes-2026-auditing-mcp-servers-privileged-tool` | Auditing MCP Servers for Over-Privileged Tool Capabilities | 2026 | E2 | defense_primary | C5 / C5 |
| 18 | `charoes-2026-model-context-protocol-threat-modeling` | Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning | 2026 | E1 | survey_review | nan / nan |
| 19 | `chenkai-2026-when-agentic-executions-fail-detecting` | When Agentic Executions Fail: Detecting and Localizing Runtime Faults from Telemetry | 2026 | E2 | benchmark_measurement | nan / nan |
| 20 | `chenning-2026-adr-agentic-detection-system-enterprise` | ADR: An Agentic Detection System for Enterprise Agentic AI Security | 2026 | E2 | defense_primary | A1;A2;A3;B1;B2;C1;C2;C5;D1;D2;D3;OUT_OF_TAXONOMY:resource_abuse / A1;A2;C1;C5;D1;D2;D3;OUT_OF_TAXONOMY:resource_abuse |
| 21 | `christoph-2025-agentbound-securing-execution-boundaries-ai` | AgentBound: Securing Execution Boundaries of AI Agents | 2025 | E1 | defense_primary | B1;C5;D1 / C5;D1 |
| 22 | `defense-against-retrieval-2026` | Defense Against Retrieval Injection Attacks in MCP-based LLM Agents | 2026 | E1 | defense_primary | A2 / A2 |
| 23 | `dongsen-2025-mcp-security-bench-msb-benchmarking` | MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents | 2025 | E2 | benchmark_measurement | nan / nan |
| 24 | `dongxu-2026-device-context-protocol-compact-safety` | Device Context Protocol: A Compact, Safety-First Architecture for LLM-Driven Control of Constrained Devices | 2026 | E2 | defense_primary | A2;C5 / A2;C5 |
| 25 | `empirical-study-privilege-2026` | An Empirical Study of Privilege Usage in Large Language Model MCP Servers | 2026 | E1 | benchmark_measurement | nan / nan |
| 26 | `fatemeh-2026-federated-mcp-gateway-enforceable-isolation` | A Federated MCP Gateway: Enforceable Isolation and Measuring Residual Semantic Attacks | 2026 | E1 | defense_primary | A2;D1;D2;OUT_OF_TAXONOMY:resource_abuse / A2;D1;D2;OUT_OF_TAXONOMY:resource_abuse |
| 27 | `gabriela-2025-security-posture-evaluation-model-context` | Security Posture Evaluation of Model Context Protocol Servers Against Prompt Injection | 2025 | E1 | benchmark_measurement | nan / nan |
| 28 | `gamini-2026-mcp-secure-runtime-access-control` | MCP-Secure: A Runtime Access Control Layer for Privilege-Aware LLM Agent Tooling | 2026 | E1 | defense_primary | C1;C5 / C1;C5 |
| 29 | `gautam-2026-registry-descriptions-go-stale-unevenly` | Registry Descriptions Go Stale Unevenly: An 89-Day Measurement of Model Context Protocol Drift, and Why Drift-Ranked Re-Auditing Under-Covers It | 2026 | E2 | benchmark_measurement | nan / nan |
| 30 | `genreachai-agentic-generative-2026` | GenReachAI: An Agentic Generative AI Framework for Automated Reachability Analysis of Enterprise Software Vulnerabilities | 2026 | E1 | defense_primary | D3 / D3 |
| 31 | `giovanni-2026-mandato-protocol-level-enforcement-digitally` | Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails | 2026 | E2 | proposal_only | C1;C2;C3 / nan |
| 32 | `governed-agentic-cloud-2026` | Governed Agentic Cloud Data Pipelines with MCP Gateways | 2026 | E1 | defense_primary | A3;B3;C5 / A3;B3;C5 |
| 33 | `gowthaman-2026-measuring-defenders-layer-aware-framework` | Measuring the Defenders: A Layer-Aware, Framework-Mapped Benchmark for Model Context Protocol Security Proxies | 2026 | E2 | benchmark_measurement | nan / nan |
| 34 | `grigoris-2025-securing-mcp-based-agent-workflows` | Securing MCP-based Agent Workflows | 2025 | E1 | defense_primary | A2;D1;D2 / A2;D1;D2 |
| 35 | `guanlin-2025-zero-knowledge-audit-internet-agents` | Zero-Knowledge Audit for Internet of Agents: Privacy-Preserving Communication Verification with Model Context Protocol | 2025 | E2 | defense_primary | C3;D1 / C3;D1 |
| 36 | `guarding-the-gateway-2026` | Guarding the Gateway: Securing MCP-Mediated RAG Pipelines Against Injection with the Guru Framework | 2026 | E1 | defense_primary | A1;A2;C5 / A1;A2;C5 |
| 37 | `haoran-2025-quantifying-conversation-drift-mcp-via` | Quantifying Conversation Drift in MCP via Latent Polytope | 2025 | E2 | defense_primary | A2;D2 / A2;D2 |
| 38 | `herman-2025-securing-model-context-protocol-mcp` | Securing the Model Context Protocol (MCP): Risks, Controls, and Governance | 2025 | E2 | proposal_only | A1;A2;A3;B1;B2;C3;D3 / nan |
| 39 | `huihao-2025-mcip-protecting-mcp-safety-via` | MCIP: Protecting MCP Safety via Model Contextual Integrity Protocol | 2025 | E1 | defense_primary | A1;A2;C5;D1 / A1;A2;C5;D1 |
| 40 | `ignacio-2026-crud-autonomous-agents-formal-validation` | From CRUD to Autonomous Agents: Formal Validation and Zero-Trust Security for Semantic Gateways in AI-Native Enterprise Systems | 2026 | E2 | defense_primary | C1;C2;C5 / C1;C2;C5 |
| 41 | `jaehyun-2025-preserving-onem2m-security-semantics-llm` | Preserving oneM2M Security Semantics in LLM-IoT Integration with Model Context Protocol | 2025 | E1 | defense_primary | C1;C3;OUT_OF_TAXONOMY:resource_abuse / C1;C3;OUT_OF_TAXONOMY:resource_abuse |
| 42 | `jinwoo-2026-beyond-tool-poisoning-attack-surfaces` | Beyond Tool Poisoning: Attack Surfaces of Malicious Remote MCP Servers Across LLM Platforms | 2026 | E1 | attack | nan / nan |
| 43 | `john-2026-mcp-safety-audit-llms-model` | MCP safety audit: LLMs with the model context protocol allow major security exploits | 2026 | E2 | defense_secondary | A1;A2;C5;D1;D3 / A2;C5;D1 |
| 44 | `l-2025-mcp-security-notification-tool-poisoning` | MCP Security Notification: Tool Poisoning Attacks | 2025 | E4 | attack | nan / nan |
| 45 | `liwei-2026-sharelock-stealthy-multi-tool-threshold` | ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP | 2026 | E2 | attack | nan / nan |
| 46 | `manish-2025-etdi-mitigating-tool-squatting-rug` | ETDI: Mitigating Tool Squatting and Rug Pull Attacks in Model Context Protocol (MCP) by using OAuth-Enhanced Tool Definitions and Policy-Based Access Control | 2025 | E1 | defense_primary | A1;B1 / nan |
| 47 | `mcpdriven-realtime-security-2026` | MCP-driven real-time security monitoring: A hybrid LLM and behavior-aware framework for temporal attack detection and severity assessment | 2026 | E1 | defense_primary | A1;C1;D1;D2 / A1;C1;D1;D2 |
| 48 | `mohammad-2026-formal-security-framework-model-context` | A Formal Security Framework for Model Context Protocol-Based Tool Access inAgentic AI Systems | 2026 | E2 | defense_primary | A1;A2;C1;C3;D3 / A2;C1;C3 |
| 49 | `n-2025-breaking-protocol-security-analysis-model` | Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents | 2025 | E1 | defense_secondary | A2;C3;C5;D1 / A2;D1 |
| 50 | `nirajan-2026-formal-security-framework-mcp-based` | A Formal Security Framework for MCP-Based AI Agents: Threat Taxonomy, Verification Models, and Defense Mechanisms | 2026 | E2 | proposal_only | A1;A2;B1;B2;C1;C3;C5;D1;D3 / nan |
| 51 | `om-2025-comprehensive-security-framework-model-context` | A Comprehensive Security Framework for the Model Context Protocol (MCP) in Multi-Agent AI Systems | 2025 | E1 | defense_primary | A1;A2;B1;B2;C1;C2;D1 / nan |
| 52 | `panduranga-2026-delegation-trust-empirical-gap-analysis` | Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems | 2026 | E2 | defense_secondary | A1;A3;B2;C1;C3 / C1;C3 |
| 53 | `parya-2026-mcp-scanner-detecting-security-risks` | MCP-Scanner: Detecting Security Risks in Model Context Protocol Systems | 2026 | E1 | defense_primary | A1;A2;B2;C1;D3 / A1;A2;D3 |
| 54 | `pek-2026-cascade-component-ablation-corpus-audit` | CASCADE: A Component Ablation and Corpus Audit of a Layered Local Defense for MCP-Based Systems | 2026 | E2 | defense_primary | A1;A2 / A1;A2 |
| 55 | `pengyu-2026-viper-mcp-detecting-exploiting-taint` | VIPER-MCP: Detecting and Exploiting Taint-Style Vulnerabilities in Model Context Protocol Servers | 2026 | E2 | defense_primary | A2;C5;D1 / A2;C5;D1 |
| 56 | `ping-2026-hybrid-analysis-secure-mcp-tool` | Hybrid Analysis for Secure MCP Tool Use in LLM Agents | 2026 | E2 | defense_primary | A1;A2;C5 / A1;A2;C5 |
| 57 | `rodrigo-2026-design-security-framework-multi-agent` | Design of a Security Framework for Multi-Agent Systems Based on Model Context Protocol in SOC Environments | 2026 | E1 | defense_primary | A1;A2;A3;B2;D3 / A1;A2;B2 |
| 58 | `rohit-2024-model-context-protocol-mcp-security` | Model Context Protocol (MCP) Security and Tenancy Boundaries | 2024 | E1 | defense_primary | A2;C2;C3;D1 / A2;C2;D1 |
| 59 | `ruiqi-2026-mcp-itp-automated-framework-implicit` | MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP | 2026 | E2 | attack | nan / nan |
| 60 | `s-2025-zero-trust-security-frameworks-model` | Zero-Trust Security Frameworks for Model Context Protocol (MCP) Server Communications | 2025 | E1 | proposal_only | A1;A2;A3;B1;B2;C3;D3 / nan |
| 61 | `saeid-2025-semantic-attacks-tool-augmented-llms` | Semantic Attacks on Tool-Augmented LLMs: Securing the Model Context Protocol Against Descriptor-Level Manipulation | 2025 | E2 | defense_primary | A1;A3;B1 / A1;A3;B1 |
| 62 | `saeid-2026-game-theoretic-multi-agent-control` | Game-Theoretic Multi-Agent Control for Robust Contextual Reasoning in LLMs | 2026 | E2 | defense_primary | A2;D2 / A2;D2 |
| 63 | `saeid-2026-verifiable-manifest-signing-transparency-enforcement` | Verifiable Manifest Signing and Transparency Enforcement for Secure MCP-Based LLM Pipelines | 2026 | E2 | defense_primary | A1;B1;D3 / A1;B1;D3 |
| 64 | `samuel-2026-secure-sandbox-environment-orchestrating-medical` | A Secure Sandbox Environment for Orchestrating Medical AI Agents Using Model Context Protocols and Role-Based Access Control. | 2026 | E2 | defense_primary | A2;D1;C3 / A2;C3;D1 |
| 65 | `secure-mcp-based-toolaugmented-2026` | Secure MCP-Based Tool-Augmented RAG for Industrial IoT Diagnostics Under Indirect Prompt Injection, Retrieval Poisoning, and Modality Outages | 2026 | E1 | defense_primary | A1;A2;C5 / A1;A2;C5 |
| 66 | `shi-2026-when-manual-lies-realistic-benchmark` | When the Manual Lies: A Realistic Benchmark to Evaluate MCP Poisoning Attacks for LLM Agents | 2026 | E1 | benchmark_measurement | nan / nan |
| 67 | `shiqiang-2025-secure-model-context-protocol-large` | Secure Model Context Protocol for Large Language Models with Dual Signatures | 2025 | E1 | defense_primary | A1;B1;D3 / A1;B1;D3 |
| 68 | `sonu-2025-mcp-guardian-security-first-layer` | MCP Guardian: A Security-First Layer for Safeguarding MCP-Based AI System | 2025 | E2 | defense_primary | A2;C3;C5;OUT_OF_TAXONOMY:resource_abuse / A2;C3;C5;OUT_OF_TAXONOMY:resource_abuse |
| 69 | `sunil-2026-zero-trust-supply-chain-security` | A Zero-Trust Supply Chain Security Framework for Model Context Protocol-based AI Systems | 2026 | E1 | defense_primary | A1;D1;D3 / A1;D1;D3 |
| 70 | `suraj-2026-gateway-architecture-enterprise-mcp-authentication` | A Gateway Architecture for Enterprise MCP Authentication: Unifying Heterogeneous Auth, Identity Delegation, and the User / Non-User Persona Problem | 2026 | E2 | proposal_only | C1;C3;A3 / nan |
| 71 | `survey-model-context-2026` | A survey on model context protocol for embodied intelligence and robotic Internet of things：from semantic control to real-time security assurance | 2026 | E1 | survey_review | nan / nan |
| 72 | `theophilus-2026-systematic-security-analysis-model-context` | A Systematic Security Analysis of Model Context Protocol: Vulnerabilities, Exploits, and Mitigations | 2026 | E1 | defense_secondary | A2;C1;C5;D1;OUT_OF_TAXONOMY:resource_abuse / A2;C1;C5;D1;OUT_OF_TAXONOMY:resource_abuse |
| 73 | `ting-2026-tool-connection-execution-control-benchmarking` | From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes | 2026 | E2 | defense_primary | A1;C1;C5;D1 / A1;C1;C5;D1 |
| 74 | `tobias-2026-machine-learning-based-detection-mcp` | Machine Learning-Based Detection of MCP Attacks | 2026 | E2 | defense_primary | A1;B1 / A1 |
| 75 | `vineeth-2026-enterprise-grade-security-model-context` | Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies | 2026 | E1 | proposal_only | A1;A2;A3;B1;B2;C3;D3 / nan |
| 76 | `wenpeng-2025-mcp-guard-multi-stage-defense` | MCP-Guard: A Multi-Stage Defense-in-Depth Framework for Securing Model Context Protocol in Agentic AI | 2025 | E1 | defense_primary | A1;A2;B1;B2;D1 / A1;A2;B1;B2 |
| 77 | `wonbae-2026-securemcp-policy-enforced-llm-data` | SecureMCP: A Policy-Enforced LLM Data Access Framework for AIoT Systems via Model Context Protocol | 2026 | E2 | defense_primary | B1;C1;C2;A2 / B1;C1;C2;A2 |
| 78 | `xinyi-2026-smcp-secure-model-context-protocol` | SMCP: Secure Model Context Protocol | 2026 | E2 | proposal_only | A1;B1;C1;C3;D3 / nan |
| 79 | `xinyi-2026-unsafe-flow-uncovering-bidirectional-data` | Unsafe by Flow: Uncovering Bidirectional Data-Flow Risks in MCP Ecosystem | 2026 | E2 | defense_primary | A2;C5;D1 / A2;C5;D1 |
| 80 | `yang-2026-mitigating-taint-style-vulnerabilities-mcp` | Mitigating Taint-Style Vulnerabilities in MCP Servers via Security-Aware Tool Descriptions | 2026 | E2 | defense_primary | A1;B1;C5 / B1;C5 |
| 81 | `yiheng-2026-component-manipulation-system-compromise-understanding` | From Component Manipulation to System Compromise: Understanding and Detecting Malicious MCP Servers | 2026 | E2 | defense_primary | A1;A3;B3;D3 / A1;A3;B3 |
| 82 | `ying-2026-options-not-clicks-lattice-refinement` | Options, Not Clicks: Lattice Refinement for Consent-Driven MCP Authorization | 2026 | E2 | defense_primary | C1;A2;B2 / C1;A2 |
| 83 | `zehua-2026-no-box-vulnerability-analysis-description` | No-Box Vulnerability Analysis: Description-only Detection of Indirect Prompt Injection Vulnerabilities in MCP Servers | 2026 | E2 | defense_primary | B2 / B2 |
| 84 | `zheng-2026-mpma-preference-manipulation-attack-model` | MPMA: Preference Manipulation Attack Against Model Context Protocol | 2026 | E1 | attack | nan / nan |
| 85 | `zhenhong-2026-mcpshield-security-cognition-layer-adaptive` | MCPShield: A Security Cognition Layer for Adaptive Trust Calibration in Model Context Protocol Agents | 2026 | E2 | defense_primary | A1;A3;B1;B2;D3 / A1;A3;B1;B2;D3 |
| 86 | `zhiqiang-2025-mcptox-benchmark-tool-poisoning-attack` | MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers | 2025 | E1 | benchmark_measurement | nan / nan |
| 87 | `zhiqiang-2025-mindguard-intrinsic-decision-inspection-securing` | MindGuard: Intrinsic Decision Inspection for Securing LLM Agents Against Metadata Poisoning | 2025 | E2 | defense_primary | A1;B3;B1 / A1 |
| 88 | `zhiyang-2026-acle-mcp-attested-capability-leases` | ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use | 2026 | E2 | defense_primary | A3;C1;C3;D3 / A3;C1;C3;D3 |
| 89 | `zhiyuan-2026-confused-deputy-attack-model-context` | Confused Deputy Attack Against Model Context Protocol | 2026 | E1 | attack | A1;A3 / A1;A3 |
| 90 | `zhonghao-2025-aegismcp-online-graph-intrusion-detection` | AegisMCP: Online Graph Intrusion Detection for Tool-Augmented LLMs on Edge Devices | 2025 | E2 | defense_primary | A2;A3;B1;D3 / A2;A3;D3 |
| 91 | `zhuoran-2026-mcp-sandboxscan-wasm-based-secure` | MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools | 2026 | E2 | defense_primary | A2;D1;D3 / A2;D1 |

---

## 4. Methodological Reconciliation: Academic Focus vs. Operational Vulnerabilities

The contrast documented between the academic corpus ($N = 171$) and the empirical validation benchmark ($n = 22$) reflects **two complementary evidence streams**, rather than an empirical contradiction:

1. **Academic Concentration on Stochastic Semantic Vulnerabilities:**  
   Over 53% of academic papers (91/171) focus on Layer A because the core scientific novelty of LLM-based agent systems lies in natural-language tool orchestration and the model's susceptibility to adversarial prompt steering (e.g., indirect prompt injection and semantic tool poisoning).

2. **Ascertainment Bias in Operational CVE Registries:**  
   In contrast, CVE Numbering Authorities (CNAs) exclusively assign CVEs to deterministic software vulnerabilities with identifiable, patchable source-code defects (such as path traversal, command injection, and DNS rebinding in Layer C). Model-level susceptibility to adversarial natural-language instructions is rarely registered as a product CVE.

3. **Complementary Value:**  
   Reading both streams together provides a complete view of MCP security: academic literature illuminates the emerging semantic threats unique to LLM planners (Layer A), while real-world disclosures expose the traditional software engineering and transport vulnerabilities that compromise MCP hosts and servers in practice (Layer C).
