# Evidence Locator Packet: xinyi-2026-smcp-secure-model-context-protocol

- **Title**: SMCP: Secure Model Context Protocol
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2602.01129
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\xinyi-2026-smcp-secure-model-context-protocol\fulltext.txt
- **Character Count**: 85519

## Block 2: Contribution Sentences
no hits

## Block 3: Method Locator
**Section Heading**: `Implementation is complex, maintenance` [section offsets: 13023:15957]
**First 120 words verbatim** [offsets: 13023:13885]
> Implementation is complex, maintenance
> costs are high, and scalability is limited.
> 
> The approach is typically stateless, re-
> stricted to a single platform, and difficult
> to reuse across different environments.
> 
> Integration is highly dependent on specific
> frameworks, resulting in weak interoper-
> ability and limited extensibility.
> 
> This method is limited to information re-
> trieval and does not support action execu-
> tion or data modification.
> 
> The protocol ecosystem is still evolving,
> and consistency and security best practices
> are not yet fully established.
> 
> MCP Servers
> 
> Transfer Layer
> 
> Web Services
> 
> Data
> Source
> 
> Server
> 
> Database
> 
> ②Initial Response
> 
> Local Files
> 
> 1:1
> 
> Capabilities
> 
> Tool Selection
> API Invocation
> 
> Tools
> Resources
> Prompts
> 
> Fig. 2. The Workflow of MCP (Reproduced from Our Previous Work [6]).
> 
> managing responses, and coordinating the process

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 25189:25385]
> This includes not only human users
> and organizational accounts, but also different types of agents, tools, and external resource services
> such as MCP servers, model services, and dataset services.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 26849:26902]
> Resource
> Model API, dataset,
> external service
> 
> , Vol.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 30487:30584]
> Models and datasets must declare training
> data sources, usage restrictions, and sensitivity tags.

## Block 6: Baseline Excerpts
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 19591:19645]
> causing deviation from the intended security baseline.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 27102:28225]
> Login secret, certificate, or verifi-
> able credential; encodes user affili-
> ation, role, authorization baseline,
> and compliance attributes
> 
> Each MCP Host assigned a 32-character iden-
> tity code; registry records code or model
> hash, deployment environment, functional
> scope, and operational boundaries
> 
> Host digital credential with public
> key, declared capabilities, permis-
> sion baseline, and optionally dele-
> gation or controller information
> 
> Each server endpoint or instance issued
> a unique identity code; registry maintains
> provider/operator, exposed capability de-
> scription, and service sensitivity level
> 
> Service certificate or verifiable cre-
> dential; includes service identity,
> supported authentication, compli-
> ance and data handling policy, and
> operational trust attributes
> 
> Each resource assigned a unique modelId,
> datasetId, etc.; registry stores owner, ver-
> sion, provenance, and sensitivity labels
> 
> Resource-level credential or asser-
> tion issued by trust anchor; spec-
> ifies compliance, permitted usage
> scope, risk classification, and sup-
> ports auditability
> 
> 4.1.3
> Structured Identity Code for All Entities.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 27404:28225]
> Host digital credential with public
> key, declared capabilities, permis-
> sion baseline, and optionally dele-
> gation or controller information
> 
> Each server endpoint or instance issued
> a unique identity code; registry maintains
> provider/operator, exposed capability de-
> scription, and service sensitivity level
> 
> Service certificate or verifiable cre-
> dential; includes service identity,
> supported authentication, compli-
> ance and data handling policy, and
> operational trust attributes
> 
> Each resource assigned a unique modelId,
> datasetId, etc.; registry stores owner, ver-
> sion, provenance, and sensitivity labels
> 
> Resource-level credential or asser-
> tion issued by trust anchor; spec-
> ifies compliance, permitted usage
> scope, risk classification, and sup-
> ports auditability
> 
> 4.1.3
> Structured Identity Code for All Entities.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 29785:30027]
> The registration service evaluates risk and required evidence based
> on task sensitivity and deployment context, verifies all proofs, then creates a registry entry, assigns
> the identity code, and snapshots verified information as the baseline.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 30029:30295]
> Likewise, users and organizations must complete registration and verification (potentially lever-
> aging existing IAM/IDaaS infrastructure), incorporating account attributes, organizational relation-
> ships, and baseline authorization into the unified identity domain.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 35680:35893]
> Through this mecha-
> nism, all downstream operations inherit a consistent and auditable security baseline, supporting
> end-to-end access control, policy enforcement, and auditability across the entire SMCP workflow.

## Block 7: Cost Excerpts
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 6019:6189]
> Recent frameworks like A2AS [13] discuss runtime security controls for agentic systems, and the
> latest standard [12] outlines general agent interconnection architectures.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 19146:19287]
> Rug Pulls
> Malicious Developer
> Initially benign servers or tools are later updated to include
> malicious payloads, betraying established trust.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 37693:37972]
> The runtime environment of SMCP involves four core roles:
> 
> --- PAGE BREAK ---
> 
> SMCP: Secure Model Context Protocol
> 11
> 
> Session Identifier
> sessionId
> A session ID shared across messages, tasks, and invocations, cor-
> responding to the session concept in agent interaction standards.
**Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 39793:39991]
> • Tool Service: This component connects to the tool catalog and runtime environment, is
> responsible for receiving invocation requests, orchestrating specific tool instances, and
> aggregating results.

## Block 8: Limitations
**Section Heading**: `Limitations` [section offsets: 11922:13023]
**First 120 words verbatim** [offsets: 11922:12812]
> Limitations
> 
> Manual API Integration Developers directly connect external APIs, offering
> 
> maximum flexibility for customized scenarios.
> 
> Plugins are discovered and invoked through standard-
> ized interfaces such as OpenAPI, simplifying integra-
> tion within one platform.
> 
> Standard Plugin
> 
> Tools are abstracted and orchestrated within an agent
> framework (e.g., LangChain), supporting dynamic se-
> lection and workflow management by the LLM.
> 
> Agent Framework
> 
> Retrieval-augmented generation enables LLMs to in-
> corporate external knowledge via vector search, en-
> hancing context understanding.
> 
> RAG + Vector DB
> 
> A unified and extensible protocol enables decoupled,
> dynamic discovery and invocation of tools and re-
> sources across applications and models.
> 
> Protocol-based (MCP)
> 
> MCP Workflow
> 
> MCP Hosts
> 
> (Chat Apps, IDEs,
> ···, AI Agents)
> 
> Prompt:
> “Can you please 
> fetch the latest 
> stock price of

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 38889:39054]
> The risk classification for the current task or invocation (e.g.,
> low, medium, high, critical), driving adaptive authentication and
> authorization strategies.
> 
> , Vol.
**Matched Term**: `adaptive` | **Location**: `X Hou, S Wang, Y Zhang, Z Xue, Y Zhao, C Fu, and H Wang` [offsets: 56723:57106]
> Through this context-driven, fine-grained policy evaluation, SMCP enforces the principle of least
> privilege: at every invocation, only the minimal necessary permissions and capabilities are granted,
> and these are dynamically adjusted as context changes, ensuring robust and adaptive security.
> 
> Comprehensive audit logging is a cornerstone of SMCP’s security and compliance framework.
**Matched Term**: `adaptive` | **Location**: `Related Work` [offsets: 74252:74673]
> MID TERM, the focus will shift to expanding SMCP’s policy enforcement and runtime auditing
> capabilities. Key directions include developing fine-grained risk-adaptive access control engines,
> scalable audit logging infrastructure, and advanced delegation and revocation management. Industry
> feedback and empirical studies will inform improvements in policy expressiveness, compliance
> automation, and operational efficiency.
**Matched Term**: `adaptive` | **Location**: `Conclusion` [offsets: 75872:76463]
> SMCP fills this gap by introducing unified digital identity and trust infrastructure,
> mutual authentication, continuous security context propagation, fine-grained policy enforcement,
> and structured audit logging directly at the protocol layer. Through these mechanisms, SMCP de-
> livers robust access control, adaptive runtime protection, and comprehensive accountability across
> agent-tool interactions. Our analysis and use cases demonstrate that SMCP can effectively mitigate
> the most pressing security threats in modern agentic workflows while maintaining flexibility and
> interoperability.
