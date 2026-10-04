# Evidence Locator Packet: manish-2025-etdi-mitigating-tool-squatting-rug

- **Title**: ETDI: Mitigating Tool Squatting and Rug Pull Attacks in Model Context Protocol (MCP) by using OAuth-Enhanced Tool Definitions and Policy-Based Access Control
- **Year**: 2025
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2506.01333
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\manish-2025-etdi-mitigating-tool-squatting-rug\fulltext.txt
- **Character Count**: 48155

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) plays a crucial` [offsets: 705:819]
> This paper introduces the Enhanced Tool Definition
> Interface (ETDI), a security extension designed to fortify MCP.

## Block 3: Method Locator
**Section Heading**: `architecture and vulnerabilities, a detailed exposition of` [section offsets: 4097:4476]
**First 120 words verbatim** [offsets: 4097:5017]
> architecture and vulnerabilities, a detailed exposition of
> ETDI, its OAuth-enhancement, the proposed policy-based
> access control extension, and a security analysis of these
> combined measures. We have demonstrated the feasibility
> of these enhancements here: https://github.com/vineethsai/
> python-sdk and detailed documentation here: https://github.
> com/vineethsai/MCP-ETDI-docs.
> 
> II. THE MODEL CONTEXT PROTOCOL (MCP)
> 
> Before we dive in, we need to understand how Standard
> MCP works. MCP [1] operates on a distributed client-server
> model, enabling LLM applications (Hosts) to connect via
> MCP Clients to MCP Servers that expose tools, resources,
> and prompts.
> 
> --- PAGE BREAK ---
> 
> A. Architecture Overview
> 
> MCP operates on a distributed client-server model. Key
> components include:
> 
> • Host Applications: User-facing applications (e.g., AI-
> powered desktop apps, IDE extensions) that orchestrate
> interactions.
> 
> • MCP Clients:
**Section Heading**: `A. Architecture Overview` [section offsets: 4774:5656]
**First 120 words verbatim** [offsets: 4774:5617]
> A. Architecture Overview
> 
> MCP operates on a distributed client-server model. Key
> components include:
> 
> • Host Applications: User-facing applications (e.g., AI-
> powered desktop apps, IDE extensions) that orchestrate
> interactions.
> 
> • MCP Clients: Software components within Host Appli-
> cations that discover, connect to, and interact with MCP
> Servers.
> 
> • MCP Servers: Services that expose capabilities (tools,
> resources, prompts) to MCP Clients.
> 
> • Tools: Discrete functions or services invokable by an
> LLM via an MCP Server.
> 
> • Resources: Data sources accessible by the LLM for
> context.
> 
> • Prompts: Pre-defined templates guiding LLM tool/re-
> source usage.
> Figure 1 illustrates the high-level MCP architecture.
> 
> Fig. 1. High-Level MCP Architecture - This diagram shows the interaction
> flow between the user, host application, MCP client, LLM, and

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Abstract—The Model Context Protocol (MCP) plays a crucial` [offsets: 977:1224]
> We further propose extending MCP
> with fine-grained, policy-based access control, where tool capa-
> bilities are dynamically evaluated against explicit policies using
> a dedicated policy engine, considering runtime context beyond
> static OAuth scopes.
**Location**: `B. Attack Vector 2: Rug Pull Attacks` [offsets: 12956:13154]
> The tool ini-
> tially presents benign or expected behavior to gain trust and
> approval, then later changes to perform unauthorized actions
> 
> --- PAGE BREAK ---
> 
> without re-triggering a consent request.
**Location**: `B. Attack Vector 2: Rug Pull Attacks` [offsets: 14317:14439]
> • Exploitation of Established Trust: The attack leverages
> the trust established during the initial, benign approval
> phase.
**Location**: `D. EExample Workflow with Amaicy-Based Access Control` [offsets: 23443:23578]
> This approach moves beyond
> static permission declarations to dynamic evaluation based on
> the runtime environment and detailed policies.
**Location**: `49 ENDFUNCTION` [offsets: 31109:31231]
> By closely examining
> the runtime behavior of linked tools, this procedure adds an
> essential layer of operational security.
**Location**: `49 ENDFUNCTION` [offsets: 31460:31509]
> It allows for
> dynamic risk assessment at runtime.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
