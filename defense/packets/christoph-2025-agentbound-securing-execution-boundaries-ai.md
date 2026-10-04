# Evidence Locator Packet: christoph-2025-agentbound-securing-execution-boundaries-ai

- **Title**: AgentBound: Securing Execution Boundaries of AI Agents
- **Year**: 2025
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2510.21236
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\christoph-2025-agentbound-securing-execution-boundaries-ai\fulltext.txt
- **Character Count**: 96753

## Block 2: Contribution Sentences
**Location**: `Introduction` [offsets: 9022:9884]
> we introduce AgentBound, the first access control framework that provides
> secure, capability-constrained execution to AI agent ecosystems. AgentBound consists of two
> main elements: an access control policy mechanism and a policy enforcement engine. The access
> control policy mechanism enables the specification of resources an MCP server needs to access
> (e.g., files, networks, or secrets). Our access control policy mechanism, inspired by the Android
> permission model, shifts the ecosystem away from “trust-by-default” toward least-privilege by
> making capabilities explicit. Policies define a common vocabulary for MCP servers that is simple
> to adopt and captures common resource needs. The policy enforcement engine provides a safety
> layer for running servers, ensuring they cannot exceed the capabilities specified in the policy–
> containing buggy or malicious

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `Header / Abstract` [offsets: 2401:2571]
> We build a dataset containing the 296 most popular MCP servers, and
> show that access control policies can be generated automatically from source code with 80.9% accuracy.
**Location**: `Introduction` [offsets: 10050:10140]
> We evaluated AgentBound by first collecting a dataset of the 296 most popular MCP servers.
**Location**: `Introduction` [offsets: 10448:10606]
> Indeed, we submitted 96 automatically generated manifests to the corresponding repositories
> and asked developers to review the corresponding MCP capabilities.

## Block 6: Baseline Excerpts
**Location**: `Background in AI Agents, MCP, and their Security` [offsets: 24399:24557]
> This enables least-privilege enforcement,
> improves transparency for developers and users, and establishes a uniform baseline for automated
> policy enforcement.

## Block 7: Cost Excerpts
**Location**: `Header / Abstract` [offsets: 2572:2745]
> We
> also show that AgentBound blocks the majority of security threats in several malicious MCP servers, and
> that the policy enforcement engine introduces negligible overhead.
**Location**: `Introduction` [offsets: 5664:5829]
> Yet, unlike mobile platforms that enforce runtime permission checks [7], MCP servers typically
> execute natively on host systems with few or no restrictions [52, 37].
**Location**: `Introduction` [offsets: 11285:11488]
> It is efficient (iii), as we
> compared the runtime of malicious MCP servers with and without AgentBound, showing that its
> policy enforcement engine introduces only a limited overhead of 0.6 ms on average.
**Location**: `Introduction` [offsets: 11680:11963]
> • We design AgentBound, a security framework for AI agents consisting of an access control
> policy mechanism supporting a declarative policy for MCP servers, and a policy enforcement
> engine that enforces the corresponding runtime permissions, supporting least-privilege and
> isolation.
**Location**: `Introduction` [offsets: 11964:12177]
> • We evaluate AgentBound showing that manifests can be generated automatically with high
> accuracy, that it reliably mitigates representative MCP security threats, and that the added
> runtime overhead is negligible.
**Location**: `Background in AI Agents, MCP, and their Security` [offsets: 17219:17407]
> Unlike mature platforms that pair system permissions with enforced runtime behavior (e.g., the
> Android’s App-Manifest) [10], MCP currently defines only the messaging and role abstractions.

## Block 8: Limitations
**Location**: `Discussion and Threats to Validity`
**First 120 words verbatim** [offsets: 71684:72522]
> Limitations of the approach. AgentBound cannot prevent attacks that do not violate the declared
> policy. For example, a puppet/tool poisoning may alter parameters of a permitted network call, B.2
> in Section 4.2, without violating the specified capabilities. Likewise, if the MCP server’s own logic
> has an application-level vulnerability (such as an SQL injection, B.4 in Section 4.2), AgentBound
> will not stop the attack, since the server is still only accessing resources that its manifest allows.
> 
> --- PAGE BREAK ---
> 
> AgentBound: Securing Execution Boundaries of AI Agents
> FSE096:19
> 
> Additionally, AgentBound’s trusted computing base includes Docker itself, Linux kernel features
> (namespaces, cgroups, iptables) that implement isolation, and the PyPI and Node.js runtimes.
> An adversary who can exploit a Docker vulnerability could bypass

## Block 9: Adaptivity Hits
**Matched Term**: `bypass our` | **Location**: `Discussion and Threats to Validity` [offsets: 72269:72920]
> Additionally, AgentBound’s trusted computing base includes Docker itself, Linux kernel features
> (namespaces, cgroups, iptables) that implement isolation, and the PyPI and Node.js runtimes.
> An adversary who can exploit a Docker vulnerability could bypass our protections; additional
> hardening layers, such as AppArmor or SELinux, can be applied to further secure the Docker
> runtime. Finally, while our capability set covers common MCP server behaviors, it is not guaranteed
> to be exhaustive and it follows a default-deny philosophy, i.e., block non-listed resources, which
> means a new server capability might be constrained until the policy is updated.
