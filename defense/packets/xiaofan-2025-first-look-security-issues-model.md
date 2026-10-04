# Evidence Locator Packet: xiaofan-2025-first-look-security-issues-model

- **Title**: A First Look at the Security Issues in the Model Context Protocol Ecosystem
- **Year**: 2025
- **Evidence Tier**: E1
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2510.16558
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\xiaofan-2025-first-look-security-issues-model\fulltext.txt
- **Character Count**: 81202

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged` [offsets: 480:584]
> In this
> paper, we present the first cross-entity security study of MCP
> under a two-stage attack surface.
**Location**: `I. INTRODUCTION` [offsets: 3110:3959]
> we present the first cross-entity security study
> of the current MCP ecosystem. We begin by outlining its
> architecture, which consists of MCP hosts, registries, and
> servers. These three entities form the analytical framework
> of our study. Registries list servers for integration. Servers
> implement various tools, each accompanied by tool metadata
> (e.g., description). Hosts retrieve and aggregate this metadata,
> mediate interactions between integrated servers and LLMs, and
> invoke tools returned by LLMs. This cross-entity workflow
> forms an end-to-end risk chain, from server discovery in
> registries, to server integration into hosts, to LLM-selected
> tool invocation inside hosts. Following this risk chain, we
> identify a unified two-stage attack surface. In the first stage
> (i.e., registry-level), weaknesses at the registry layer allow
> malicious or

## Block 3: Method Locator
**Section Heading**: `architecture, which consists of MCP hosts, registries, and` [section offsets: 3215:7689]
**First 120 words verbatim** [offsets: 3215:4083]
> architecture, which consists of MCP hosts, registries, and
> servers. These three entities form the analytical framework
> of our study. Registries list servers for integration. Servers
> implement various tools, each accompanied by tool metadata
> (e.g., description). Hosts retrieve and aggregate this metadata,
> mediate interactions between integrated servers and LLMs, and
> invoke tools returned by LLMs. This cross-entity workflow
> forms an end-to-end risk chain, from server discovery in
> registries, to server integration into hosts, to LLM-selected
> tool invocation inside hosts. Following this risk chain, we
> identify a unified two-stage attack surface. In the first stage
> (i.e., registry-level), weaknesses at the registry layer allow
> malicious or hijacked servers to be discovered and integrated
> into hosts. In the second stage (i.e., post-integration), once
> integrated,
**Section Heading**: `B. Indirect Exploitation via Server Implementation` [section offsets: 39158:41697]
**First 120 words verbatim** [offsets: 39158:39960]
> B. Indirect Exploitation via Server Implementation
> 
> The tool description can also implicitly influence benign
> tools provided by other servers configured on the same host.
> Tool Shadowing Attack. Because LLM reads all tool descrip-
> tions before selecting a tool, each description can influence
> the behavior of the LLM (e.g., extracting wrong parameters).
> Attackers can exploit this behavior by injecting malicious
> descriptions to mislead the LLM. In this way, a malicious
> tool can indirectly influence the behavior of a benign one,
> even without being invoked. For example, when a user intends
> 
> --- PAGE BREAK ---
> 
> TABLE III: Invalid links, empty server content, and missing
> README files in decentralized registries.
> 
> Registries
> Invalid Server
> File Links (%)
> 
> Empty Server
> 
> Missing
> README (%)
> 
> Content (%)

## Block 4: Evaluation Locator
**Section Heading**: `VIII. EVALUATION AND MEASUREMENT` [section offsets: 57268:57943]
**First 120 words verbatim** [offsets: 57268:58134]
> VIII. EVALUATION AND MEASUREMENT
> 
> We first evaluate the accuracy of our tool, MCPInspect, using
> a manually constructed dataset. We then apply it to perform
> a large-scale measurement based on the data collected. Since
> 
> --- PAGE BREAK ---
> 
> 1 async def handle_call_tool(..., arguments: dict...) -> ...
> 
> 2
> elif name == "visualize_data":
> 
> 3
> ...
> 
> 4
> vegalite_specification =
> 
> eval(arguments["vegalite_specification"])
> 
> Listing 4: Detected vulnerable tool within the MCP server
> mcp vegalite server [18].
> 
> we already present the result for sever links (e.g., redirection
> accounts) (Section VI), we now focus on servers with detected
> vulnerabilities and suspicious tool descriptions.
> 
> A. Evaluation Discussion
> 
> Evaluation of vulnerable MCP servers. We extract tools
> based on their specification syntax and perform rule-based
> detection using Semgrep. To evaluate the precision,
**Section Heading**: `A. Evaluation Discussion` [section offsets: 57943:57969]
**First 120 words verbatim** [offsets: 57943:58742]
> A. Evaluation Discussion
> 
> Evaluation of vulnerable MCP servers. We extract tools
> based on their specification syntax and perform rule-based
> detection using Semgrep. To evaluate the precision, we ran-
> domly select 41 out of 377 vulnerable MCP servers identified
> from the registry mcp.so. We then manually inspect these
> 41 servers. Our verification standard is as follows: for any
> detected vulnerability (e.g., code injection), if a corresponding
> tool parameter flows directly into the vulnerable sink without
> any validation checks, we classify it as a true positive. Listing 4
> presents a vulnerable tool detected within an MCP server. The
> argument vegalite specification is passed directly to eval,
> creating a code injection vulnerability (Line 4). Of the 41
> vulnerable servers, we manually confirm 4
**Section Heading**: `Evaluation of vulnerable MCP servers. We extract tools` [section offsets: 57969:58785]
**First 120 words verbatim** [offsets: 57969:58765]
> Evaluation of vulnerable MCP servers. We extract tools
> based on their specification syntax and perform rule-based
> detection using Semgrep. To evaluate the precision, we ran-
> domly select 41 out of 377 vulnerable MCP servers identified
> from the registry mcp.so. We then manually inspect these
> 41 servers. Our verification standard is as follows: for any
> detected vulnerability (e.g., code injection), if a corresponding
> tool parameter flows directly into the vulnerable sink without
> any validation checks, we classify it as a true positive. Listing 4
> presents a vulnerable tool detected within an MCP server. The
> argument vegalite specification is passed directly to eval,
> creating a code injection vulnerability (Line 4). Of the 41
> vulnerable servers, we manually confirm 4 false positives (i.e.,
**Section Heading**: `Evaluation of suspicious tool metadata. Tool metadata` [section offsets: 58785:58839]
**First 120 words verbatim** [offsets: 58785:59599]
> Evaluation of suspicious tool metadata. Tool metadata
> evaluation is guided by three dimensions. First, we examine
> whether a tool description contains instruction-like content that
> can influence model behavior (e.g., tool shadowing). Second,
> we assess whether such content affects actual tool invocation
> under MCP host execution (e.g., file access). Third, we check
> whether the case reflects an intentionally vulnerable proof-of-
> concept server or an unintended risk arising from host behavior
> (e.g., tool confusion). From the suspicious tool descriptions
> detected in the registry mcp.so, we identify 6 cases. Among
> them, 4 are used for proof-of-concept purposes, while 2 are
> vulnerable to tool confusion. Listing 5 shows one of the tool
> descriptions. This tool description instructs the LLM to invoke
> the tool mark

## Block 5: Attack-Set Excerpts
**Location**: `VIII. EVALUATION AND MEASUREMENT` [offsets: 57302:57395]
> We first evaluate the accuracy of our tool, MCPInspect, using
> a manually constructed dataset.
**Location**: `B. Measurement Results` [offsets: 59884:60128]
> Overall, we find that some links
> reference the same server repository; some server repositories
> have been deleted; some servers do not provide any tools; and
> in some cases, syntax errors during code-to-AST conversion
> caused extraction failures.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation of vulnerable MCP servers. We extract tools` [offsets: 58108:58229]
> To evaluate the precision, we ran-
> domly select 41 out of 377 vulnerable MCP servers identified
> from the registry mcp.so.
**Location**: `Evaluation of vulnerable MCP servers. We extract tools` [offsets: 58691:58784]
> Of the 41
> vulnerable servers, we manually confirm 4 false positives (i.e.,
> 90.24% precision).

## Block 8: Limitations
**Section Heading**: `C. Limitations and Future Work` [section offsets: 61642:62280]
**First 120 words verbatim** [offsets: 61642:62429]
> C. Limitations and Future Work
> 
> For tool extraction, our current implementation focuses on
> tools explicitly added through their specifications (e.g., through
> @server.list_tools()). However, tools that are added
> dynamically from a list, such as within a for loop, cannot yet
> be correctly extracted. For the vulnerability summary generator,
> we currently use the default Semgrep detection rules for MCP
> servers, which may lead to false positives. In the future, we
> plan to trace the source of such lists and extract tools directly
> from them. We also plan to construct custom rules specifically
> tailored for MCP servers to improve accuracy.
> 
> IX. DISCLOSURE
> 
> We have promptly disclosed our findings to both the
> corresponding host and relevant MCP registries. For example,
> we have reported the

## Block 9: Adaptivity Hits
no hits
