# Evidence Locator Packet: herman-2025-securing-model-context-protocol-mcp

- **Title**: Securing the Model Context Protocol (MCP): Risks, Controls, and Governance
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: proposal_only
- **Link**: https://arxiv.org/abs/2511.20920
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\herman-2025-securing-model-context-protocol-mcp\fulltext.txt
- **Character Count**: 90123

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) replaces static,` [offsets: 1048:1385]
> In response, we propose a set of practical controls,
> including per-user authentication with scoped authorization,
> provenance tracking across agent workflows, containerized
> sandboxing with input/output checks, inline policy enforcement
> with DLP and anomaly detection, and centralized governance
> using private registries or gateway layers.

## Block 3: Method Locator
**Section Heading**: `1.1. MCP Overview and Architecture` [section offsets: 1784:3667]
**First 120 words verbatim** [offsets: 1784:2606]
> 1.1. MCP Overview and Architecture
> 
> Large language models (LLMs) are increasingly able to
> carry out multi-step reasoning and call external functions to
> complete tasks. Until recently, these function calls had to be
> manually configured to connect LLMs to external services,
> so most LLMs systems ran in relatively closed environments
> with limited access to external resources [1]. MCP is an
> open standard designed to define how LLMs communicate
> with external applications, data sources, and tools, enabling
> them to obtain relevant context and execute actions on exter-
> nal systems [2]. The MCP standard can be conceptualized
> as a universal interface layer for AI systems, analogous to a
> 
> Securing the Model Context Protocol (MCP):
> 
> Risks, Controls, and Governance
> 
> Shanita Sojan
> 
> Darktrace
> Email: shanita.sojan@darktrace.com
**Section Heading**: `3.3.3. Generic Tool Design Risks. Many official MCP` [section offsets: 31863:32549]
**First 120 words verbatim** [offsets: 31863:32747]
> 3.3.3. Generic Tool Design Risks. Many official MCP
> servers
> provide
> generic
> tools
> that
> mirror
> API
> end-
> points rather than safe, parameterized operations. The
> Snowflake official MCP server, for example, exposes an
> execute_sql tool accepting arbitrary SQL queries.
> Agents have to generate different SQL queries each time
> for the same request, making results non-deterministic and
> potentially wrong.
> 
> Instead,
> organizations
> need
> tools
> that
> map
> to
> specific
> use
> cases.
> For
> example,
> get_revenue_for_month(month, year)
> that
> map to approved, parameterized queries reviewed by data
> 
> --- PAGE BREAK ---
> 
> teams. This requires organizations to maintain and deploy
> custom MCP deployments securely.
> 
> 3.4. Operational Security: Data Sensitivity and
> Runtime Monitoring
> 
> Even with trusted servers properly configured and sand-
> boxed, runtime security challenges remain. Organizations
> must monitor what
**Section Heading**: `architecture eliminates arbitrary code execution risks (Sec-` [section offsets: 48673:50464]
**First 120 words verbatim** [offsets: 48673:49594]
> architecture eliminates arbitrary code execution risks (Sec-
> tion 3.2.5) and ensures all servers operate under centralized
> security controls.
> 
> Credential and authentication governance. Central-
> ized credential management eliminates user-managed tokens
> and API keys. All MCP servers authenticate using per-
> user OAuth flows integrated with organizational identity
> providers. Users should never see or handle raw creden-
> tials, with authentication occurring transparently through the
> identity provider.
> 
> Compliance policies and data governance. Organi-
> zations define organization-wide policies specifying which
> data types may be processed by agents. HIPAA-regulated
> healthcare data, PCI-DSS payment card data, or GDPR-
> protected personal data may be prohibited from agent work-
> flows, or subject to strict redaction and audit requirements.
> Compliance policy templates align with regulatory require-
> ments, with audit trail
**Section Heading**: `4.6. Gateway Architecture for Control Enforce-` [section offsets: 50464:51937]
**First 120 words verbatim** [offsets: 50464:51310]
> 4.6. Gateway Architecture for Control Enforce-
> ment
> 
> The controls described in Sections 4.1–4.5 can be op-
> erationalized through a gateway architecture (Figure 2) that
> interposes between AI agents and MCP servers, acting as a
> centralized security control plane [24]. Rather than agents
> connecting directly to MCP servers, all MCP protocol traffic
> flows through the gateway, enabling comprehensive moni-
> toring, policy enforcement, and risk mitigation.
> 
> This centralization, however, introduces practical trade-
> offs that architects must account for. Each tool call now
> traverses an additional network and policy layer, which
> can increase latency for agent–tool interactions unless the
> gateway is deployed close to agents and optimized for
> streaming and batching. Operating the gateway as a shared
> control point also adds complexity: configuration

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `3.1.2. Cross-System Data Exfiltration. The severity of` [offsets: 22196:22591]
> System B (Data Source): Sensitive data is accessible
> to the agent (e.g., data warehouse, internal databases, code
> repositories)
> 
> System C (Exfiltration Target): Sensitive data is leaked
> via external communication capabilities (e.g., attacker-
> controlled email, HTTP endpoints, cloud storage)
> 
> The agent acts as a data exfiltration conduit, bridg-
> ing systems the attacker cannot directly access.
**Location**: `3.4.2. Secrets and Credentials Exposure. Engineering` [offsets: 34797:35025]
> Engineering
> agents connected to cloud infrastructure, Kubernetes clus-
> ters, CI/CD systems, and code repositories encounter secrets
> everywhere: API keys, database credentials, cloud access
> keys, service account tokens, SSH keys.
**Location**: `4.4. Inline Policy Enforcement` [offsets: 45834:46244]
> In this paper we
> do not present detailed benchmarks of enforcement cost;
> instead, we treat “no user-perceptible latency increase” as
> a design objective and rely on standard systems techniques
> (co-locating the gateway with agents, streaming responses,
> caching policy decisions, and avoiding unnecessary round
> trips) to keep end-to-end response times within the latency
> envelope expected by users and developers.
**Location**: `5.2. NIST AI Risk Management Framework Func-` [offsets: 56204:56511]
> For MCP deployments, this requires docu-
> menting agent types (for example, customer support, pro-
> ductivity, and engineering agents), connected servers and
> tools, underlying data stores (such as CRM platforms, ware-
> houses, and code repositories), and applicable regulatory
> obligations for each data domain.
**Location**: `6.1. Open Research Problems` [offsets: 69435:69628]
> One direction is
> to develop selective context mechanisms that decide, per
> request, which portions of the available state are relevant,
> instead of exposing full histories or datasets by default.
**Location**: `6.1. Open Research Problems` [offsets: 69784:69989]
> Secure multi-party
> computation techniques could enable agents to collaborate
> across organizational boundaries without revealing raw data,
> providing joint functionality while keeping local datasets
> private.

## Block 6: Baseline Excerpts
**Location**: `3.4.3. Agent Behavior Anomalies. Runtime monitoring` [offsets: 35817:35991]
> Based on logged agent data, behavioral baselines can
> be established: typical tools used per user and role, typical
> tool call sequences, typical data volumes and access times.
**Location**: `3.4.3. Agent Behavior Anomalies. Runtime monitoring` [offsets: 35992:36147]
> Deviations from baselines should trigger alerts, for example:
> unusual data volume spikes, activity during after hours, or
> repeated authentication failures.
**Location**: `6.1. Open Research Problems` [offsets: 63976:64150]
> —
> Baseline learning, de-
> viation detection, rate
> limiting
> 
> SIEM/SOAR
> integration, monitoring
> dashboards
> 
> highlight a central area where the research community can
> contribute.

## Block 7: Cost Excerpts
**Location**: `1.3.1. The Paradigm Shift. Traditional software security` [offsets: 7031:7198]
> This shift from static to dynamic runtime logic cre-
> ates new vulnerabilities: agents may inadvertently follow
> malicious instructions in data sources they access [11].
**Location**: `1.5. Limitations of Existing Frameworks` [offsets: 12414:12598]
> However,
> these standards do not provide specific controls for MCP-
> style protocol security, agent authentication and authoriza-
> tion, or runtime monitoring of dynamic tool invocations.
**Location**: `3.2.4. Response Injection Attacks. Tool responses are` [offsets: 27049:27127]
> First, the server establishes legitimacy through initial
> benign functionality.
**Location**: `3.3. Configuration and Governance Risks: Trusted` [offsets: 29527:29619]
> delete_file
> and
> delete_workflow_run_logs
> alongside benign tools like get_pull_requests [25].
**Location**: `3.3. Configuration and Governance Risks: Trusted` [offsets: 30069:30171]
> All-
> most all MCP hosts dynamically enable new tools at runtime
> as servers add or remove capabilities.
**Location**: `3.4. Operational Security: Data Sensitivity and` [offsets: 32554:32715]
> Operational Security: Data Sensitivity and
> Runtime Monitoring
> 
> Even with trusted servers properly configured and sand-
> boxed, runtime security challenges remain.

## Block 8: Limitations
**Section Heading**: `1.5. Limitations of Existing Frameworks` [section offsets: 11394:13074]
**First 120 words verbatim** [offsets: 11394:12297]
> 1.5. Limitations of Existing Frameworks
> 
> Existing AI governance frameworks, including the
> NIST AI Risk Management Framework [27] and ISO/IEC
> 42001 [29], focus primarily on model-level risks such as
> bias, fairness, and transparency. They do not address the ar-
> chitectural security challenges introduced by dynamic agent
> systems with broad tool access and user-generated con-
> tent exposure. Traditional application security frameworks
> assume static program analysis and developer-driven inte-
> gration. Neither paradigm adequately captures the risks of
> MCP-enabled multi-agent systems.
> 
> The NIST AI Risk Management Framework provides
> guidance for managing AI system trustworthiness and
> risks [27], but does not specifically address the security im-
> plications of dynamic tool invocation and cross-system data
> flows inherent to MCP architectures. ISO/IEC 27001:2022
> establishes requirements for information

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `1.6. Contributions` [offsets: 14140:14393]
> •
> We identify critical open research problems includ-
> ing verifiable tool registries, formal verification for
> adaptive systems, and privacy-preserving agent op-
> erations, establishing a research agenda for securing
> dynamic agent systems (Section 6).
> 
> 2.
**Matched Term**: `circumvent` | **Location**: `2.2.3. Adversary Type 3: The Helpful Agent as Inadver-` [offsets: 17773:18308]
> The boundary is important: a software bug
> produces behavior that contradicts program logic, and a
> misconfiguration exposes capabilities that operators did not
> intend to grant. By contrast, an inadvertent agent issues
> well-formed tool calls and follows available policies, yet
> its task-optimization leads it to chain actions that acciden-
> tally disclose sensitive data, escalate access, or circumvent
> 
> safeguards. These incidents arise from emergent decision-
> making over prompts and context, rather than from defects
> in implementation.
**Matched Term**: `adaptive` | **Location**: `6.1. Open Research Problems` [offsets: 65874:66294]
> Finally, logging must become
> semantics-aware: the system should distinguish, for exam-
> ple, between an agent reading configuration files as part
> of normal setup and reading .aws/credentials as a
> likely precursor to credential theft. The core challenge is to
> design analysis techniques that treat agents as adaptive, goal-
> seeking systems rather than as conventional microservices.
> 
> Verifiable tool and server registries.
**Matched Term**: `adaptive` | **Location**: `6.1. Open Research Problems` [offsets: 67937:68420]
> Tradi-
> tional formal methods typically target programs with clearly
> specified state spaces and transition relations. MCP-based
> agents violate these assumptions through adaptive behavior,
> tool composition, and natural language interfaces, and the
> rapidly evolving MCP specification introduces further insta-
> bility. This calls for verification approaches that can reason
> compositionally about individual tools and their combina-
> tions, even when tools are added or updated at runtime.
**Matched Term**: `Adaptive` | **Location**: `E. Ohana, A. Giloni, S. Bose, C. Picardi, Y. Elovici, and A. Shab-` [offsets: 82607:82739]
> Kompella, “Uncertainty-Aware,
> 
> Risk-Adaptive
> Access
> Control
> for
> Agentic
> Systems
> using
> an
> LLM-Judged TBAC Model,” Oct.2025. [Online].
