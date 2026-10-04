# Evidence Locator Packet: n-2025-breaking-protocol-security-analysis-model

- **Title**: Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents
- **Year**: 2025
- **Evidence Tier**: E1
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_secondary
- **Link**: https://doi.org/10.25559/sitito.021.202503.420-428
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\n-2025-breaking-protocol-security-analysis-model\fulltext.txt
- **Character Count**: 29641

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged` [offsets: 390:782]
> We present the first rigorous security
> analysis of MCP’s architectural design, identifying three funda-
> mental protocol-level vulnerabilities: (1) absence of capability
> attestation allowing servers to claim arbitrary permissions, (2)
> bidirectional sampling without origin authentication enabling
> server-side prompt injection, and (3) implicit trust propagation
> in multi-server configurations.
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged` [offsets: 1194:1415]
> We propose ATTESTMCP, a backward-compatible
> protocol extension adding capability attestation and message
> authentication, reducing attack success rates from 52.8% to
> 12.4% with median latency overhead of 8.3ms per message.

## Block 3: Method Locator
**Section Heading**: `A. Model Context Protocol Architecture` [section offsets: 4182:5024]
**First 120 words verbatim** [offsets: 4182:5121]
> A. Model Context Protocol Architecture
> MCP defines a client-server architecture with three roles:
> •Host:The user-facing application (e.g., Claude Desktop)
> •Client:MCP client within the host, managing server
> connections
> •Server:External process providing tools, resources, or
> prompts
> 1
> arXiv:2601.17549v1  [cs.CR]  24 Jan 2026
> 
> Communication occurs via JSON-RPC 2.0 over stdio or
> HTTP/SSE transports. The protocol defines three capability
> types:
> Resources:Read-only data (files, database records) exposed
> by servers. Clients retrieve resources viaresources/read
> requests.
> Tools:Executable functions servers expose. The LLM de-
> cides when to invoke tools based on their descriptions.
> Sampling:Critically, servers can request LLM completions
> from clients viasampling/createMessage, allowing
> servers to inject prompts and receive responses [17].
> B. Threat Model
> We consider an adversary who:
> •Controls or compromises one MCP server in a multi-
**Section Heading**: `implementation-level vulnerabilities, MCPSecBench [23]` [section offsets: 18329:18670]
**First 120 words verbatim** [offsets: 18329:19411]
> implementation-level vulnerabilities, MCPSecBench [23]
> provides attack taxonomies, and MCPGuard [25] offers
> runtime scanning, ATTESTMCP proposes concrete protocol
> additions (capability attestation, message authentication) that
> can be incorporated into the MCP specification itself—a
> complementary layer addressing protocol-level rather than
> implementation-level weaknesses.
> A. Design Principles
> 1)Capability Attestation:Servers must cryptographically
> prove capability possession via signed certificates from
> a capability authority.
> 2)Message Authentication:All JSON-RPC messages in-
> clude HMAC-SHA256 signatures binding content to
> authenticated server identity.
> 3)Origin Tagging:Sampling requests are tagged with
> server origin, enabling clients to distinguish server-
> injected from user-originated prompts.
> 4)Isolation Enforcement:Cross-server information flow
> requires explicit user authorization.
> 5)Replay Protection:Timestamp plus nonce with config-
> urable validity window.
> B. Trust Model Options
> A critical design decision is the capability authority archi-
> tecture. We evaluate
**Section Heading**: `implementation-level weaknesses.` [section offsets: 18670:18703]
**First 120 words verbatim** [offsets: 18670:19704]
> implementation-level weaknesses.
> A. Design Principles
> 1)Capability Attestation:Servers must cryptographically
> prove capability possession via signed certificates from
> a capability authority.
> 2)Message Authentication:All JSON-RPC messages in-
> clude HMAC-SHA256 signatures binding content to
> authenticated server identity.
> 3)Origin Tagging:Sampling requests are tagged with
> server origin, enabling clients to distinguish server-
> injected from user-originated prompts.
> 4)Isolation Enforcement:Cross-server information flow
> requires explicit user authorization.
> 5)Replay Protection:Timestamp plus nonce with config-
> urable validity window.
> B. Trust Model Options
> A critical design decision is the capability authority archi-
> tecture. We evaluate three models:
> TABLE VIII: Capability Authority Trust Models
> Model Pros Cons
> Centralized Simple PKI,
> easy revocation
> Single point of
> failure
> Federated Distributed,
> flexible
> Complex coor-
> dination
> Web-of-Trust Decentralized User complex-
> ity
> Our implementation uses thefederated model: platform
**Section Heading**: `A. Design Principles` [section offsets: 18703:19306]
**First 120 words verbatim** [offsets: 18703:19724]
> A. Design Principles
> 1)Capability Attestation:Servers must cryptographically
> prove capability possession via signed certificates from
> a capability authority.
> 2)Message Authentication:All JSON-RPC messages in-
> clude HMAC-SHA256 signatures binding content to
> authenticated server identity.
> 3)Origin Tagging:Sampling requests are tagged with
> server origin, enabling clients to distinguish server-
> injected from user-originated prompts.
> 4)Isolation Enforcement:Cross-server information flow
> requires explicit user authorization.
> 5)Replay Protection:Timestamp plus nonce with config-
> urable validity window.
> B. Trust Model Options
> A critical design decision is the capability authority archi-
> tecture. We evaluate three models:
> TABLE VIII: Capability Authority Trust Models
> Model Pros Cons
> Centralized Simple PKI,
> easy revocation
> Single point of
> failure
> Federated Distributed,
> flexible
> Complex coor-
> dination
> Web-of-Trust Decentralized User complex-
> ity
> Our implementation uses thefederated model: platform
> vendors (Anthropic,

## Block 4: Evaluation Locator
**Section Heading**: `experiments.` [section offsets: 13259:14207]
**First 120 words verbatim** [offsets: 13259:14299]
> experiments.
> A.PROTOAMPFramework
> Existing benchmarks (InjecAgent, AgentDojo) assume di-
> rect tool APIs rather than MCP’s client-server architecture.
> Concurrent work on MCP-Bench [22] evaluates capability and
> task completion, while MCPSecBench [23] catalogs attack
> types. Our PROTOAMP(Protocol Amplification Benchmark)
> differs by measuringprotocol amplification—how MCP’s ar-
> chitecture specifically increases attack success rates compared
> to non-MCP baselines:
> 1)MCP Server Wrappers:We implemented MCP-
> compliant servers wrapping benchmark tool functions,
> preserving semantic equivalence while adding protocol
> overhead.
> 3
> 
> 2)Attack Injection Points:We added injection capabili-
> ties at three protocol layers:
> •Resource content (indirect injection)
> •Tool response payloads
> •Sampling request prompts
> 3)Measurement Infrastructure:We instrumented clients
> to log all JSON-RPC messages, enabling analysis of
> attack propagation through protocol channels.
> B. Experimental Setup
> MCP Servers Under Test:
> •mcp-server-filesystem: File operations (read,
**Section Heading**: `B. Experimental Setup` [section offsets: 14207:14532]
**First 120 words verbatim** [offsets: 14207:15279]
> B. Experimental Setup
> MCP Servers Under Test:
> •mcp-server-filesystem: File operations (read,
> write, list)
> •mcp-server-git: Repository management (clone,
> commit, diff)
> •mcp-server-sqlite: Database queries (SELECT,
> INSERT)
> •mcp-server-slack: Messaging integration
> •adversarial-mcp: Custom server exercising protocol
> edge cases
> LLM Backends:Claude-3.5-Sonnet, GPT-4o, Llama-3.1-
> 70B
> Attack Scenarios:847 test cases:
> •InjecAgent adaptations: 312 (indirect injection, tool
> abuse)
> •AgentDojo adaptations: 398 (multi-step attacks)
> •Novel protocol-specific attacks: 137 (sampling, cross-
> server)
> Baseline:Equivalent tool integrations without MCP (direct
> function calls) to isolate protocol-specific effects.
> C. Controlled Variables
> To ensure valid comparison between MCP and baseline
> conditions:
> •Tool semantics identical between conditions
> •Same injection payloads used
> •LLM prompting strategy held constant
> •Network latency matched between conditions
> Latency Configuration:Baseline uses direct function calls
> with simulated network overhead matching MCP. Measured
> MCP latencies:
**Section Heading**: `V. RESULTS` [section offsets: 15448:15459]
**First 120 words verbatim** [offsets: 15448:16357]
> V. RESULTS
> A. Protocol Amplification Effect
> Table IV shows attack success rates (ASR) comparing MCP-
> integrated agents versus baseline (non-MCP) integrations.
> Key Finding:MCP’s architecture amplifies attack success
> by 23–41% depending on attack type. The largest amplification
> occurs in cross-server propagation, where MCP’s lack of iso-
> lation boundaries enables attacks impossible in single-server
> deployments.
> TABLE IV: Attack Success Rate: MCP vs. Baseline
> Attack Type Baseline MCP∆
> Indirect Injection (Resource) 31.2% 47.8% +16.6%
> Tool Response Manipulation 28.4% 52.1% +23.7%
> Cross-Server Propagation 19.7% 61.3% +41.6%
> Sampling-Based Injection N/A 67.2% —
> Overall26.4% 52.8%+26.4%
> B. Sampling Vulnerability Severity
> The sampling mechanism introduces a novel attack vector
> absent in non-MCP systems:
> TABLE V: Sampling Attack Analysis by Model
> Model ASR Exfil. Rate Persist.
> Claude-3.5-Sonnet 58.3% 42.1%
**Section Heading**: `experiments with PROTOAMP, we demonstrated that MCP’s` [section offsets: 25782:25836]
**First 120 words verbatim** [offsets: 25782:26697]
> experiments with PROTOAMP, we demonstrated that MCP’s
> architecture amplifies attack success rates by 23–41% com-
> pared to non-MCP integrations. Our proposed ATTESTMCP
> extension reduces attack success from 52.8% to 12.4% through
> capability attestation and message authentication, with accept-
> able performance overhead (8.3ms median per message).
> As MCP adoption accelerates, addressing these architectural
> weaknesses becomes critical. We recommend:
> 1) Protocol revision incorporating mandatory capability at-
> testation
> 2) Origin tagging requirements for all sampling requests
> 3) Explicit isolation boundaries with user-prompted cross-
> server authorization
> REFERENCES
> [1] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M.
> Fritz, “Not what you’ve signed up for: Compromising real-world LLM-
> integrated applications with indirect prompt injection,” inProc. ACM
> AISec, 2023.
> [2] Anthropic, “Model Context

## Block 5: Attack-Set Excerpts
**Location**: `experiments.` [offsets: 13272:13407]
> A.PROTOAMPFramework
> Existing benchmarks (InjecAgent, AgentDojo) assume di-
> rect tool APIs rather than MCP’s client-server architecture.
**Location**: `experiments.` [offsets: 13530:13878]
> Our PROTOAMP(Protocol Amplification Benchmark)
> differs by measuringprotocol amplification—how MCP’s ar-
> chitecture specifically increases attack success rates compared
> to non-MCP baselines:
> 1)MCP Server Wrappers:We implemented MCP-
> compliant servers wrapping benchmark tool functions,
> preserving semantic equivalence while adding protocol
> overhead.

## Block 6: Baseline Excerpts
**Location**: `experiments.` [offsets: 13530:13878]
> Our PROTOAMP(Protocol Amplification Benchmark)
> differs by measuringprotocol amplification—how MCP’s ar-
> chitecture specifically increases attack success rates compared
> to non-MCP baselines:
> 1)MCP Server Wrappers:We implemented MCP-
> compliant servers wrapping benchmark tool functions,
> preserving semantic equivalence while adding protocol
> overhead.

## Block 7: Cost Excerpts
**Location**: `experiments.` [offsets: 13530:13878]
> Our PROTOAMP(Protocol Amplification Benchmark)
> differs by measuringprotocol amplification—how MCP’s ar-
> chitecture specifically increases attack success rates compared
> to non-MCP baselines:
> 1)MCP Server Wrappers:We implemented MCP-
> compliant servers wrapping benchmark tool functions,
> preserving semantic equivalence while adding protocol
> overhead.

## Block 8: Limitations
**Section Heading**: `G. Limitations` [section offsets: 22985:24075]
**First 120 words verbatim** [offsets: 22985:23910]
> G. Limitations
> ATTESTMCP does not address:
> •Attacks within a single legitimately-authorized server (the
> server has valid credentials but serves malicious content)
> •Social engineering of users to authorize malicious capa-
> bilities
> •CA compromise (mitigated by federation, but not elimi-
> nated)
> •First-contact attacks: Pinning (TOFU—Trust On First
> Use) provides no protection when a user first installs a
> malicious server that never claimed ATTESTMCP support
> •Ecosystem adoption: If most servers remain legacy/un-
> signed, users will default to “Permissive” mode, negating
> security benefits
> Residual 12.4% ASR primarily reflects indirect injection
> through legitimately-retrieved content—a fundamental limita-
> tion shared with all LLM systems that cannot be solved at the
> protocol layer.
> User Behavior Assumptions:Our ASR measurements
> assume users carefully review cross-server authorization
> prompts. In practice,alert fatiguemay

## Block 9: Adaptivity Hits
no hits
