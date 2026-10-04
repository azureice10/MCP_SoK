# Supplementary Section S6: Technical Resolution of the ChainWatch–SAMOS Contradiction

## 1. The Apparent Literature Contradiction

In Section 8.1 of the manuscript, a significant apparent tension in the empirical literature is highlighted:
- **ChainWatch (Narayan et al., July 2026 [94]):** Explicitly claims in its literature review that through April 2026, *"no published defense addresses multi-step attack chains"* in MCP-based AI agent systems, presenting ChainWatch as the first framework to provide multi-step sequential detection.
- **SAMOS (Ntousakis et al., late 2025 [93]):** Demonstrates empirical containment of multi-step tool-injection attack chains, specifically replicating and mitigating the real-world GitHub MCP incident (Invariant Labs disclosure).

---

## 2. In-Depth Comparative Architectural Analysis

To resolve whether this represents an oversight in ChainWatch's systematic literature review or a fundamental divergence in threat definitions, we conducted a granular comparative analysis of both systems' formal models:

| Technical Dimension | SAMOS (Ntousakis et al. [93]) | ChainWatch (Narayan et al. [94]) |
| :--- | :--- | :--- |
| **Primary Taxonomy Placement** | **Layer C** (Server/Runtime Boundary, Crossing $S_i \rightarrow X_i$) | **Layer A / Layer D** (Semantic & Client Context, Crossing $L \rightarrow S_i$) |
| **Operational Substrate** | Host OS runtime, container namespaces, and system-call interposition | LLM prompt context window, JSON-RPC message logs, and semantic token flows |
| **Threat Model Definition** | Multi-step compromise where a compromised tool invokes auxiliary tools to execute OS commands or exfiltrate private files | Multi-turn prompt drift where an adversary incrementally steers agent planning across turns without individual prompt violations |
| **Mitigation Mechanism** | Deterministic capability sandboxing, filesystem call brokering, and static permission manifests | Hidden Markov Model (HMM) and sequential state-transition anomaly detection on LLM intent sequences |
| **Defense Maturity** | Level 1 (Hardened runtime prototype evaluated on containerized MCP benchmarks) | Level 1 (Detection pipeline evaluated on synthetic multi-turn dialogues) |

---

## 3. Methodological Resolution & Synthesis

The apparent contradiction arises from **differing definitions of "multi-step attack chains" across architectural abstraction layers**:

1. **System-Level vs. Semantic-Level Chains:** SAMOS views a multi-step chain as a cascade of discrete tool-level capabilities terminating in an operating system sink (e.g., Step 1: Read issue $\rightarrow$ Step 2: Inject tool definition $\rightarrow$ Step 3: Shell execution). It stops the chain at the system-call boundary.
2. **Context Drifting Chains:** ChainWatch defines a multi-step attack chain as semantic context accumulation inside the LLM itself, where each individual prompt and tool invocation appears benign in isolation, but their sequential trajectory compromises the planner. SAMOS does not monitor or sanitize the LLM's internal cognitive trajectory.
3. **Synthesis Finding:** ChainWatch did not overlook SAMOS; rather, SAMOS solves a Layer C containment problem, leaving open the Layer A/D multi-turn semantic poisoning problem that ChainWatch targets. Recognizing this architectural divergence eliminates the contradiction and reinforces the necessity of layered, defense-in-depth security across MCP systems.
