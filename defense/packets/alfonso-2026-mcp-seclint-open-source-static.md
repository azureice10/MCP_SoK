# Evidence Locator Packet: alfonso-2026-mcp-seclint-open-source-static

- **Title**: MCP-SecLint: An Open-Source Static Analyzer for Detecting Vulnerabilities in LLM Tool Integrations
- **Year**: 2026
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://doi.org/10.1145/3806007.3810961
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\alfonso-2026-mcp-seclint-open-source-static\fulltext.txt
- **Character Count**: 1947

## Block 2: Contribution Sentences
**Location**: `Abstract:` [offsets: 264:1151]
> Abstract:
> MCP-SecLint is an open-source static analysis tool designed to detect security vulnerabilities in LLM tool integrations, specifically targeting Model Context Protocol (MCP) servers implemented in JavaScript and TypeScript. It identifies security weaknesses by tracking the flow of untrusted tool arguments and sensitive data to dangerous sinks. The system is built with a modular and extensible architecture comprising three main components: 1. Detection of dangerous command execution, 2. Identification of token passthrough vulnerabilities, 3. Detection of unauthenticated endpoints. In an evaluation using 100 publicly available MCP server repositories from GitHub, MCP-SecLint revealed a 5% vulnerability rate, highlighting the prevalence of security issues in the current MCP ecosystem.
> 
> 1. Introduction
> Model Context Protocol (MCP) has rapidly emerged as an open standard

## Block 3: Method Locator
**Section Heading**: `2. Static Analysis Architecture` [section offsets: 1381:1712]
**First 120 words verbatim** [offsets: 1381:1946]
> 2. Static Analysis Architecture
> MCP-SecLint operates as an offline static analysis tool performing taint tracking on abstract syntax trees (AST). The enforcement occurs through offline analysis before server deployment, identifying vulnerable information flows and unsanitized parameters passing across server-to-sink boundaries.
> 
> 3. Evaluation and Results
> We evaluated MCP-SecLint on 100 MCP server implementations across GitHub. The analyzer identified critical vulnerabilities including sink injection and parameter command passthrough across 5% of repositories.

## Block 4: Evaluation Locator
**Section Heading**: `3. Evaluation and Results` [section offsets: 1712:1948]
**First 120 words verbatim** [offsets: 1712:1946]
> 3. Evaluation and Results
> We evaluated MCP-SecLint on 100 MCP server implementations across GitHub. The analyzer identified critical vulnerabilities including sink injection and parameter command passthrough across 5% of repositories.

## Block 5: Attack-Set Excerpts
**Location**: `3. Evaluation and Results` [offsets: 1715:1811]
> Evaluation and Results
> We evaluated MCP-SecLint on 100 MCP server implementations across GitHub.
**Location**: `3. Evaluation and Results` [offsets: 1812:1946]
> The analyzer identified critical vulnerabilities including sink injection and parameter command passthrough across 5% of repositories.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
