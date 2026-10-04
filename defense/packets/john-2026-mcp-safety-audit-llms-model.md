# Evidence Locator Packet: john-2026-mcp-safety-audit-llms-model

- **Title**: MCP safety audit: LLMs with the model context protocol allow major security exploits
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_secondary
- **Link**: https://arxiv.org/abs/2504.03767
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\john-2026-mcp-safety-audit-llms-model\fulltext.txt
- **Character Count**: 37952

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 815:913]
> However, we show that the
> current MCP design carries a wide range of security risks for end-users.
**Location**: `Abstract` [offsets: 914:1145]
> In particular, we show that industry-leading LLMs may be coerced to use
> MCP tools and compromise an AI developer’s system through a wide
> range of attacks, e.g., malicious code execution, remote access control, and
> credential theft.
**Location**: `Abstract` [offsets: 1146:1352]
> In order to proactively mitigate the demonstrated (and
> related) attacks, we introduce a safety auditing tool, McpSafetyScanner, the
> first such agentic tool to assess the security of an arbitrary MCP server.
**Location**: `Abstract` [offsets: 3361:3491]
> However, we show that the current design of
> the MCP poses significant security risks for users developing generative AI solutions.
**Location**: `Abstract` [offsets: 3635:3873]
> In particular, we show that
> Claude 3.7 and Llama-3.3-70B may be prompted to use tools from default MCP servers
> which allow three different types of attacks: 1) malicious code execution, (2) remote access
> control, and (3) credential theft.
**Location**: `Abstract` [offsets: 3874:3992]
> Furthermore, we introduce a new multi-MCP server attack
> which enables both remote access control and credential theft.

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `Background` [offsets: 14868:15104]
> Thus, despite rigorous testing on
> previous (non-MCP related) safety benchmarks, Llama-3.3-70B-Instruct (and likely other
> LLMs) require re-evaluation given the immediate safety-and-security implications of en-
> abling LLMs with MCP tools.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Abstract` [offsets: 271:524]
> To reduce development overhead and enable seamless integration between
> potential components comprising any given generative AI application,
> the Model Context Protocol (MCP) (Anthropic, 2025d) has recently been
> released and, subsequently, widely adapted.
**Location**: `Abstract` [offsets: 4427:4612]
> Directly testing the ability of an LLM’s guardrails to prevent
> these attacks can thus produce false positives which, in turn, may provide a false sense of
> security against such attacks.
**Location**: `Background` [offsets: 20810:21069]
> McpSafetyScanner is fast (runtime of less than one minute to scan
> and generate each report on an M2 Max MacBook Pro) and, most importantly, accurate; the
> first report (displayed in Figure 20) catches exploits used in the demonstrated MCE, RAC,
> and CT attacks.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
