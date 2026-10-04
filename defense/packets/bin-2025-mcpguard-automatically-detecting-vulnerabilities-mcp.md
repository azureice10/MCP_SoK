# Evidence Locator Packet: bin-2025-mcpguard-automatically-detecting-vulnerabilities-mcp

- **Title**: MCPGuard : Automatically Detecting Vulnerabilities in MCP Servers
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2510.23673
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\bin-2025-mcpguard-automatically-detecting-vulnerabilities-mcp\fulltext.txt
- **Character Count**: 31538

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged as` [offsets: 810:1095]
> This paper systemat-
> ically analyzes the security landscape of MCP-based systems,
> identifying three principal threat categories: (1) agent hijack-
> ing attacks stemming from protocol design deficiencies; (2)
> traditional web vulnerabilities in MCP servers; and (3) supply
> chain security.

## Block 3: Method Locator
**Section Heading**: `architecture. Its core technical implementation first utilizes` [section offsets: 19634:20286]
**First 120 words verbatim** [offsets: 19634:20547]
> architecture. Its core technical implementation first utilizes
> lightweight static scanning with pattern-based detection for
> rapid threat filtering, supports real-time adaptation via hot
> updates, and follows a fail-fast mechanism to minimize
> overhead. Subsequently, it deploys a deep neural detection
> module, built on pre-trained text embedding models that
> are fully fine-tuned on MCP-specific threat data to capture
> domain-specific semantics that generic models may miss. Fi-
> nally, an intelligent arbitration mechanism employs an LLM
> to independently assess input safety based on standardized
> criteria, combining its judgment with the neural module’s
> results for uncertain cases to form a hybrid decision-making
> system, thereby balancing efficiency and accuracy.
> 
> Distinct from layered detection pipelines, McpSafe-
> tyScanner’s [12] contribution lies in its systematic exposure
> of critical vulnerabilities within

## Block 4: Evaluation Locator
**Section Heading**: `results for uncertain cases to form a hybrid decision-making` [section offsets: 20286:23455]
**First 120 words verbatim** [offsets: 20286:21182]
> results for uncertain cases to form a hybrid decision-making
> system, thereby balancing efficiency and accuracy.
> 
> Distinct from layered detection pipelines, McpSafe-
> tyScanner’s [12] contribution lies in its systematic exposure
> of critical vulnerabilities within MCP-enabled LLM sys-
> tems. It demonstrates that leading LLMs such as Claude 3.7
> and Llama-3.3-70B can be coerced into enabling malicious
> code execution, remote access control, and credential theft,
> even bypassing inconsistent guardrails. It further introduces
> a novel high-threat Retrieval-Agent Deception attack, where
> attackers corrupt public data with MCP-targeted commands
> that are triggered via retrieval tools, eliminating the need
> for direct system access. The scanner adopts a unique agen-
> tic framework comprising hacker, auditor, and supervisor
> agents that automatically probes MCP servers using their
> native tools, searches

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
