# Evidence Locator Packet: charoes-2026-auditing-mcp-servers-privileged-tool

- **Title**: Auditing MCP Servers for Over-Privileged Tool Capabilities
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2603.21641
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\charoes-2026-auditing-mcp-servers-privileged-tool\fulltext.txt
- **Character Count**: 22046

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 498:604]
> We present
> mcp-sec-audit, an extensible security assessment toolkit designed
> specifically for MCP servers.
**Location**: `Introduction` [offsets: 3188:4135]
> We present mcp-sec-audit1, which analyzes both the implemen-
> tation code and MCP tool metadata, and reports capability-based
> deployment risks with actionable hardening guidance. Existing
> vulnerability scanners focus on package dependencies and con-
> tainer misconfigurations. While complementary, they do not infer
> runtime capabilities from tool definitions. Our tool bridges this
> gap by mapping code-level indicators to capability categories such
> as command_exec and file_write, and pairing them with least-
> privilege deployment recommendations. Many defenses focus on
> runtime policy enforcement. mcp-sec-audit operates earlier in
> the lifecycle as a pre-deployment audit tool using rule-driven static
> analysis and optional sandbox-based dynamic verification.
> 
> Contributions. This work makes the following contributions:
> 
> • Auditing Framework: We present mcp-sec-audit, an au-
> diting framework that automatically identifies high-risk ca-
> pabilities

## Block 3: Method Locator
**Section Heading**: `Implementation Details. We implemented our tool in Python` [section offsets: 11147:14721]
**First 120 words verbatim** [offsets: 11147:12023]
> Implementation Details. We implemented our tool in Python
> with a plugin-based architecture for extensibility.
> 
> • Static Analysis: We utilize efficient regular expression and
> keyword matching to identify patterns of privileged opera-
> tions such as subprocess.run and open(..., ’w’). Rule
> definitions are in TOML files (rules/keywords.toml), cur-
> rently supporting Python source code and MCP metadata
> JSON files.
> • Dynamic Analysis: It includes infrastructure for Docker
> SDK-based container management and CEF log parsing. The
> engine includes a Python-based MCP Fuzzer that handles
> the protocol handshake and automatically injects payloads
> such as shell injection and path traversal into tool arguments.
> The implementation expects an external Docker image with
> eBPF instrumentation to generate runtime telemetry.
> • Data Models: Strictly typed dataclasses define models
> including

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 14721:18438]
**First 120 words verbatim** [offsets: 14721:15589]
> Evaluation
> 
> We evaluate the detection rate of mcp-sec-audit along three ex-
> periments on a controlled vulnerable server, the MCPTox academic
> dataset [8], and a curated vulnerability lab.
> 
> Static Analysis Assessment. We test the static analyzer on a
> synthesized malicious tool (examples/static_analysis_test.py)
> with command execution, file I/O, and network operations. The
> static pipeline successfully identified all three capability categories
> with confidence scores ranging from 0.65 to 0.85, assigned a MEDIUM
> risk level (total score: 42.5/100), and generated 5 mitigation recom-
> mendations including Docker isolation and read-only mounts. The
> analysis completed in under 2 seconds without requiring Docker.
> 
> MCPTox Benchmark Assessment. We evaluate the detection
> capability of our tool on the MCPTox benchmark for tool poisoning
> attack on 45 real-world MCP servers

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 14733:14907]
> We evaluate the detection rate of mcp-sec-audit along three ex-
> periments on a controlled vulnerable server, the MCPTox academic
> dataset [8], and a curated vulnerability lab.
**Location**: `Evaluation` [offsets: 15433:15461]
> MCPTox Benchmark Assessment.
**Location**: `Evaluation` [offsets: 15462:15594]
> We evaluate the detection
> capability of our tool on the MCPTox benchmark for tool poisoning
> attack on 45 real-world MCP servers [8].
**Location**: `Evaluation` [offsets: 15990:16130]
> 124 samples (25.3%)
> did not have explicit capability indicators in the dataset metadata,
> though some may still be detected by broader rules.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 15364:15431]
> The
> analysis completed in under 2 seconds without requiring Docker.
**Location**: `Evaluation` [offsets: 18271:18434]
> Dynamic
> analysis consistently assigned higher scores than static analysis
> (average increase: +36.2 points), reflecting behavioral evidence from
> runtime monitoring.

## Block 8: Limitations
**Section Heading**: `Limitations and Future Work` [section offsets: 18438:20404]
**First 120 words verbatim** [offsets: 18438:19397]
> Limitations and Future Work
> 
> Language Support. The static analyzer currently supports Python
> and JSON metadata but not TypeScript/JavaScript, despite rule def-
> initions in keywords.toml. Extending language support requires
> implementing additional text-based analyzers following the exist-
> ing plugin interface.
> 
> Detection Accuracy. Pattern-based detection is inherently sus-
> ceptible to false positives (benign code matching risky keywords)
> and false negatives (obfuscated or indirect invocations). Rule re-
> finement and context-aware heuristics may improve precision. Al-
> though the tool identifies prompt injection patterns in tool de-
> scriptions, it does not validate runtime behavior against semantic
> constraints, including parameter manipulation and tool sequence hi-
> jacking. Hybrid approaches combining static rules with LLM-based
> semantic analysis may improve detection accuracy.
> 
> Dynamic Analysis Deployment. The sandbox-based pipeline
> requires Linux

## Block 9: Adaptivity Hits
no hits
