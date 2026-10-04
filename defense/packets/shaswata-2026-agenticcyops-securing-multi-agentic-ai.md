# Evidence Locator Packet: shaswata-2026-agenticcyops-securing-multi-agentic-ai

- **Title**: AgenticCyOps: Securing Multi-Agentic AI Integration in Enterprise Cyber Operations
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: proposal_only
- **Link**: https://arxiv.org/abs/2603.09134
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\shaswata-2026-agenticcyops-securing-multi-agentic-ai\fulltext.txt
- **Character Count**: 99388

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 539:889]
> We introduce AgenticCyOps (Securing
> Multi-Agentic AI Integration in Enterprise Cyber Operations), a frame-
> work built on a systematic decomposition of attack surfaces across
> component, coordination, and protocol layers, revealing that docu-
> mented vectors consistently trace back to two integration surfaces:
> tool orchestration and memory management.
**Location**: `Introduction` [offsets: 6748:7655]
> This paper makes the
> following contributions:
> 
> • Attack Surface Decomposition. A systematic analysis of
> MAS threats across component, coordination, and protocol
> layers, identifying that documented vectors converge on
> tool and memory integration surfaces (Table 1).
> • Defensive Design Framework. Five security principles
> derived from the decomposition, where each documented
> vector is addressed by at least two complementary princi-
> ples grounded in compliance mandates (Table 2).
> • CyberOps Application and Evaluation. An agentic SOAR
> architecture with phase-scoped agents, consensus-validated
> execution, and organizational memory, evaluated through
> coverage analysis (Table 3), attack path tracing (Table 4),
> and trust boundary assessment (Table 5) demonstrating a
> minimum of 72% reduction in exploitable boundaries.
> 
> We organize the paper using a What–Why–How–Next progression:
> agentic AI fundamentals and

## Block 3: Method Locator
**Section Heading**: `architecture with phase-scoped agents, consensus-validated` [section offsets: 7283:36830]
**First 120 words verbatim** [offsets: 7283:8193]
> architecture with phase-scoped agents, consensus-validated
> execution, and organizational memory, evaluated through
> coverage analysis (Table 3), attack path tracing (Table 4),
> and trust boundary assessment (Table 5) demonstrating a
> minimum of 72% reduction in exploitable boundaries.
> 
> We organize the paper using a What–Why–How–Next progression:
> agentic AI fundamentals and attack surfaces (§2), defensive prin-
> ciples (§3), MAS-integrated CyberOps framework with coverage,
> attack path, and trust boundary evaluation (§4), and trade-offs with
> open challenges (§5), before concluding. The appendix provides a
> list of acronyms, a categorized summary of the literature underpin-
> ning our research foundation, and full boundary enumeration.
> 
> 2
> Agentic AI and Attack Surfaces (The What)
> 
> Agentic AI refers to autonomous systems that exhibit goal-directed
> behavior through planning, decision-making, and action within
**Section Heading**: `architecture by mapping directly to the security surfaces while` [section offsets: 36830:36937]
**First 120 words verbatim** [offsets: 36830:37739]
> architecture by mapping directly to the security surfaces while
> adhering to the defenses (Table 2).
> 
> 4.2.1
> Architecture Overview. For agentic CyberOps, we employ a
> vertical architecture following the SOC lifecycle, which is inherently
> sequential and phase-dependent. This necessitates an orchestra-
> tor that maintains a global incident state and facilitates handoffs
> between phases. Furthermore, horizontal topologies amplify the
> coordination-level threats from peer-to-peer sharing (Table 1), and
> allow direct pathways for lateral compromise without traversing
> any central checkpoint [9], whereas a centralized Host serves as a
> unified trust anchor through which all authorization, capability en-
> forcement, and audit logging are structurally channeled. Concretely,
> the SOAR functions as the Host, coordinating four phase-scoped
> Client-Servers (Monitor, Analyze, Admin, Report) mirroring the
> SOC lifecycle (§
**Section Heading**: `Architecture Overview. For agentic CyberOps, we employ a` [section offsets: 36937:46645]
**First 120 words verbatim** [offsets: 36937:37868]
> Architecture Overview. For agentic CyberOps, we employ a
> vertical architecture following the SOC lifecycle, which is inherently
> sequential and phase-dependent. This necessitates an orchestra-
> tor that maintains a global incident state and facilitates handoffs
> between phases. Furthermore, horizontal topologies amplify the
> coordination-level threats from peer-to-peer sharing (Table 1), and
> allow direct pathways for lateral compromise without traversing
> any central checkpoint [9], whereas a centralized Host serves as a
> unified trust anchor through which all authorization, capability en-
> forcement, and audit logging are structurally channeled. Concretely,
> the SOAR functions as the Host, coordinating four phase-scoped
> Client-Servers (Monitor, Analyze, Admin, Report) mirroring the
> SOC lifecycle (§ 4). This hierarchical delegation enables the injection
> of validator and consensus policy mechanisms while maintaining
> end-to-end
**Section Heading**: `architecture (Figure 4) and identify where AgenticCyOps’s prin-` [section offsets: 46645:48209]
**First 120 words verbatim** [offsets: 46645:47534]
> architecture (Figure 4) and identify where AgenticCyOps’s prin-
> ciples intercept them. Table 4 summarizes each chain with and
> without AgenticCyOps enforcement. In three of four scenarios (AP-
> 1, AP-2, AP-3), AgenticCyOps intercepts the chain within the first
> two steps, preventing escalation to exploitation. Each interception
> involves at least two principles acting at different layers, confirming
> defense-in-depth. AP-4 exposes a known boundary: AgenticCyOps
> constrains exfiltration scope and outbound schema but cannot en-
> force validation on receiving organizations’ ingestion pipelines.
> 
> 4.3.3
> Trust Boundary Reduction. A trust boundary exists wherever
> one component accepts input from another without independent
> verification. In a flat MAS deployment where all agents share un-
> restricted access to all tools and memory, exploitable boundaries
> grow combinatorially. Table 5 compares

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 18764:18892]
> For example,
> an agent authorized to query data repositories should not possess
> execution privileges on administrative functions.
**Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 41213:41370]
> Operational memory,
> comprising threat repositories, CMDB, SIEM data, and numerous
> sources, is accessed via an independent agent exclusively through
> gateways.
**Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 41421:41659]
> For
> synchronization (§3.2.1), write operations, such as updating detec-
> tion rules, AARs, or policy repositories, route through the Report
> Server’s Improvement Loop, providing a single auditable write path
> that prevents unverified agents.
**Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 41660:41767]
> Versioned repositories and append-
> only structures maintain provenance throughout the incident life-
> cycle.
**Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 44004:44321]
> Threat
> Repositories
> 
> Validation
> 
> I/O
> 
> EDR/NDR Sensor
> 
> Loop
> 
> Threat
> Analysis
> Frameworks
> 
> ITSM/Ticketing
> 
> LLM
> 
> Monitoring & Triage
> 
> Tools
> 
> Code
> Repository
> 
> MCP 
> Servers
> 
> Sandbox
> 
> Local
> Threat
> Repository
> 
> (Child 
> Tasks)
> 
> SIEM Search
> 
> I/O
> 
> RCA
> Loop
> 
> CMDB/
> 
> Code Analyzer
> 
> Asset 
> Inventory
> 
> Investigation
> 
> LLM
> 
> Tools
> 
> Mem.
**Location**: `Discussion (The Next)` [offsets: 49231:49449]
> Our evaluation relies on structural analysis rather than adversarial
> simulation, and runtime overhead remains unmeasured; the field
> also lacks standardized datasets and benchmarks for multi-agent se-
> curity evaluation.

## Block 6: Baseline Excerpts
**Location**: `Abstract` [offsets: 1486:1896]
> Coverage analysis,
> attack path tracing, and trust boundary assessment confirm that the
> design addresses the documented attack vectors with defense-in-
> depth, intercepts three of four representative attack chains within
> the first two steps, and reduces exploitable trust boundaries by a
> minimum of 72% compared to a flat MAS, positioning AgenticCy-
> Ops as a foundation for securing enterprise-grade integration.
**Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 17607:17857]
> Although protocols such as MCP and OAuth-
> based access delegation provide baseline access control, they are
> insufficient against tool hijacking [52] via identity forgery or tool im-
> personation [38], which redirect invocations to malicious endpoints.
**Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 39706:39788]
> A Validation
> Loop verifies triage conclusions against baselines before escalation.
**Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 40772:41006]
> For im-
> provement, agents propose updates to detection rules, playbooks,
> and compliance mappings; an Improvement Loop audits each pro-
> posal against policy and historical baselines before committing
> to organizational memory (§ 3.2.1).
**Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 42428:42741]
> To assess AgenticCyOps’s defensive coverage, we present three
> complementary analyses: a coverage matrix quantifying principle-
> to-vector mappings, an attack path analysis tracing multi-step
> chains through the architecture, and a trust boundary reduction
> comparing exploitable surfaces against a flat MAS baseline.
**Location**: `architecture (Figure 4) and identify where AgenticCyOps’s prin-` [offsets: 47623:47723]
> In the flat baseline, every agent accesses every tool (4×16=64), store
> (4×12=48), and peer (4×3=12).

## Block 7: Cost Excerpts
**Location**: `Introduction` [offsets: 6384:6747]
> We apply the framework to a Security Orchestration, Au-
> tomation, and Response (SOAR) architecture adopting the Model
> Context Protocol (MCP) [37] as its structural basis, embedding se-
> curity as an architectural constraint rather than a runtime policy
> overlay, and evaluate the design through coverage analysis, attack
> path tracing, and trust boundary assessment.
**Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 12211:12447]
> Steganographic communication further facilitates covert coordina-
> tion, allowing agents to exchange hidden messages through benign-
> appearing outputs, such as header metadata, rendering traditional
> oversight mechanisms ineffective [33].
**Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 18145:18575]
> In practice, this demands layering four
> complementary mechanisms: signed manifests for cryptographic
> tool provenance, preventing identity forgery and authentication
> bypass; admin-approved catalogs with centralized discovery, miti-
> gating privilege escalation and biased tool selection; runtime access
> policies enforcing least privilege per session; and continuous seman-
> tic monitoring to detect collusion and covert coordination.
**Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 23944:24080]
> Once data enters memory, it
> becomes indistinguishable from fact, as the agent cannot discern
> between benign and adversarial information.
**Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 24145:24330]
> Adversaries can induce
> agents to construct poisoned knowledge from benign-appearing
> artifacts by exploiting the tendency to replicate patterns: a self-
> reinforcing error cycle [47, 55].
**Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 32340:32742]
> Therefore, critical bottlenecks include: (i) alert
> fatigue from high false-positive rates requiring manual review; (ii)
> knowledge fragmentation where context resides across disconnected
> systems (ticketing, SIEM, CTI platforms); (iii) decision latency in
> time-sensitive response actions requiring manager approval; and
> (iv) skill gaps where junior analysts struggle to interpret complex
> attack patterns.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Abstract` [offsets: 118:538]
> Abstract
> 
> Multi-agent systems (MAS) powered by LLMs promise adaptive,
> reasoning-driven enterprise workflows, yet granting agents au-
> tonomous control over tools, memory, and communication intro-
> duces attack surfaces absent from deterministic pipelines. While
> current research largely addresses prompt-level exploits and nar-
> row individual vectors, it lacks a holistic architectural model for
> enterprise-grade security.
**Matched Term**: `white-box` | **Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 24771:25193]
> For example, RobustRAG processes retrieved passages in
> disjoint isolation before secure aggregation [57]. This isolate-then-
> aggregate paradigm provides certifiable guarantees: that bounded
> poisoned passages cannot corrupt the final output, even under
> white-box threat models. In multi-agent settings, integrity extends
> to synchronization: where agents share memory, concurrent read-
> /write can lead to inconsistency [56].
**Matched Term**: `Adaptive` | **Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 35478:35625]
> 4.1.3
> Research & Adaptive Improvement. Novel attack variants
> evade signature-based detection, requiring hypothesis-driven dy-
> namic threat hunting.
**Matched Term**: `evade` | **Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 35478:35762]
> 4.1.3
> Research & Adaptive Improvement. Novel attack variants
> evade signature-based detection, requiring hypothesis-driven dy-
> namic threat hunting. Analysts iteratively formulate hypotheses,
> query diverse data sources, refine theories based on findings, and
> adapt investigation paths.
**Matched Term**: `adaptive` | **Location**: `architecture with phase-scoped agents, consensus-validated` [offsets: 35763:36329]
> This self-reflective loop demands adap-
> tive planning, adjusting next steps based on prior observations
> and episodic memory to track hypothesis evolution. Static simula-
> tions fail against adaptive adversaries [8]; rigid workflows cannot
> accommodate investigative pivots when initial hypotheses prove
> incorrect. Agentic AI provides this adaptability by maintaining
> an investigation state in memory while dynamically exploring for
> knowledge to support hypothesis testing, and by coordinating col-
> laborative investigation (e.g., VirusTotal) and reporting (e.g., CVE).
**Matched Term**: `Adaptive` | **Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 40527:40635]
> Research & Adaptive Improvement. Report agents coordi-
> nate adaptive scouting and post-incident improvement.
**Matched Term**: `adaptive` | **Location**: `Architecture Overview. For agentic CyberOps, we employ a` [offsets: 40527:40771]
> Research & Adaptive Improvement. Report agents coordi-
> nate adaptive scouting and post-incident improvement. For scout-
> ing, agents track hypothesis evolution in episodic memory while
> querying threat intelligence feeds and third-party services.
**Matched Term**: `adaptive` | **Location**: `Discussion (The Next)` [offsets: 48566:48941]
> but remain unexplored [2]. The verify-first paradigm introduces
> validation latency that may impact time-critical scenarios, motivat-
> ing adaptive consensus thresholds that scale rigor with action re-
> versibility [46, 50]. Moreover, consensus loops are themselves attack
> surfaces: a compromised validator or poisoned policy repository
> can collapse the verification layer [55].
**Matched Term**: `Adaptive` | **Location**: `A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems. arXiv` [offsets: 80936:81116]
> Adaptive scouting adopted; security
> gaps motivate our defensive overlay.
> 
> Agentic offensive capabilities with
> adaptive planning validate the need
> for dynamic playbooks in CyberOps.
**Matched Term**: `adaptive` | **Location**: `A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems. arXiv` [offsets: 81010:81274]
> Agentic offensive capabilities with
> adaptive planning validate the need
> for dynamic playbooks in CyberOps.
> 
> §4.1.3: Adaptive Improvement
> 
> Delegation requirements for trust cal-
> ibration and systemic resilience align
> with AgenticCyOps’s verified execu-
> tion design.
**Matched Term**: `Adaptive` | **Location**: `A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems. arXiv` [offsets: 81118:81456]
> §4.1.3: Adaptive Improvement
> 
> Delegation requirements for trust cal-
> ibration and systemic resilience align
> with AgenticCyOps’s verified execu-
> tion design.
> 
> §5: Architectural alignment
> 
> Universal inter-agent trust exploita-
> tion and RAG backdoors validate tool
> and memory surface vulnerabilities
> across component and coordination
> layers.
**Matched Term**: `Adaptive` | **Location**: `A Full-Stack Benchmark for Privacy Leakage in Multi-Agent LLM Systems. arXiv` [offsets: 81628:81848]
> §4.1.2: Decision Making, §4.1.3
> Adaptive Improvement
> Challita et al. [8]
> RedTeamLLM: agentic offensive security with
> dynamic plan correction, memory manage-
> ment, and ReAct reasoning; outperforms Pen-
> testGPT on VULNHUB.
