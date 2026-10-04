# Evidence Locator Packet: xinyi-2026-unsafe-flow-uncovering-bidirectional-data

- **Title**: Unsafe by Flow: Uncovering Bidirectional Data-Flow Risks in MCP Ecosystem
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2605.07836
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\xinyi-2026-unsafe-flow-uncovering-bidirectional-data\fulltext.txt
- **Character Count**: 72433

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 873:1059]
> We present MCP-BiFlow, a
> bidirectional static analysis framework built around MCP-aware
> entrypoint recovery, protocol-specific taint modeling, and inter-
> procedural propagation analysis.

## Block 3: Method Locator
**Section Heading**: `implementation, or no matched` [section offsets: 13016:17871]
**First 120 words verbatim** [offsets: 13016:13952]
> implementation, or no matched
> tool-entry pattern */
> 
> src/index.ts
> 
> 1
> 
> server.setRequestHandler(ListToolsRequestSchema, async
> () => ({
> 
> Tool Discovery
> 
> 2
> 3
> 4
> 5
> 6
> 7
> 8
> 9
> 10
> 11
> 12
> 13
> 
> tools: [{
> 
> Tool
> 
> name: "fetch_html",
> description: "Fetch a website and return HTML",
> inputSchema: {
> 
> type: "object",
> properties: { url: { type: "string" } },
> required: ["url"],
> },
> }],
> }));
> 
> Tool Invocation
> 
> server.setRequestHandler(CallToolRequestSchema, async
> (request) => {
> 
> 14
> 
> const validatedArgs =
> RequestPayloadSchema.parse(request.params.arguments);
> 
> 15
> 16
> 17
> 18
> 
> if (request.params.name !== "fetch_html")
> 
> Request Source
> 
> throw new Error("Tool not found");
> return await Fetcher.html(validatedArgs);
> });
> 
> environment. Our focus is therefore not malicious infrastructure,
> but unsafe propagation caused by incomplete validation, insuffi-
> cient sanitization, or unsafe handling of externally obtained or
> internally sensitive data. The attacker does not

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 38894:39759]
**First 120 words verbatim** [offsets: 38894:39753]
> Evaluation
> 
> Our evaluation focuses on three aspects of MCP-BiFlow: detection
> effectiveness on confirmed cases, applicability to real-world MCP
> servers, and the role of its major components.
> RQ1: How well does MCP-BiFlow detect confirmed MCP
> 
> vulnerabilities relative to existing tools? We study this
> question on a benchmark of confirmed MCP vulnerability
> cases, using case-level detections and recall for comparison.
> RQ2: What vulnerabilities can MCP-BiFlow uncover in real-
> 
> world MCP servers? To answer this question, we apply
> MCP-BiFlow to real-world open-source MCP server reposi-
> tories and manually review the resulting candidate findings.
> RQ3: Which components are responsible for MCP-BiFlow’s
> 
> coverage and triage behavior? An ablation study is used to
> isolate how the major MCP-aware components affect reviewed-
> instance coverage and triage outcomes.
**Section Heading**: `Evaluation Setup` [section offsets: 39759:43278]
**First 120 words verbatim** [offsets: 39759:40580]
> Evaluation Setup
> 
> Tool implementation. We implemented a prototype of MCP-
> BiFlow on top of the open-source static analysis framework YASA [20].
> The pipeline consists of three main stages: MCP entrypoint recov-
> ery, MCP-specific taint specification, and bidirectional interpro-
> cedural taint analysis. Semantically ambiguous source and guard
> cases are handled through the LLM-assisted adjudication.
> Environment. All experiments were conducted on a server run-
> ning Ubuntu 22.04, equipped with two 64-core AMD EPYC 9954
> processors, 1024 GB of RAM, and six NVIDIA A100 GPUs, each
> with 80 GB of memory. The LLM-assisted analysis in our pipeline
> was powered by the gpt-5.3-codex-medium API.
> Baselines. We compare MCP-BiFlow against four baseline tools:
> CodeQL [15], Semgrep [52], Snyk Code [54], and MCPScan [2]. CodeQL
> serves
**Section Heading**: `Results are reported over reviewed instances rather than unique` [section offsets: 52522:53111]
**First 120 words verbatim** [offsets: 52522:53283]
> Results are reported over reviewed instances rather than unique
> servers. The reviewed set contains 859 instances in total, of which
> 424 are confirmed, 302 unresolved, and 133 rejected. These counts
> are not directly comparable to the server- and cluster-level figures
> in RQ2, since a single server may contribute multiple reviewed
> instances with different paths, sinks, or review outcomes. M1 and
> M2 both bear primarily on coverage. Removing M1 reduces sur-
> faced instances from 859 to 636 and confirmed instances from 424
> 
> --- PAGE BREAK ---
> 
> Conference’17, July 2017, Washington, DC, USA
> X Hou, Y Zhao, and H Wang
> 
> Table 5: Ablation on reviewed real-world instances.
> 
> Variant
> Confirmed
> Unresolved
> Rejected
> Retained
> Total
> M1+M2+M3
> 424
> 302
> 133
> 726
> 859
> w/o M1
> 287
**Section Heading**: `evaluation is disclosure-oriented, and semantically ambiguous cases` [section offsets: 56765:56871]
**First 120 words verbatim** [offsets: 56765:57626]
> evaluation is disclosure-oriented, and semantically ambiguous cases
> require LLM-assisted adjudication.
> 
> 6
> Related Work
> 
> Research on MCP security. As MCP becomes a foundational
> interface for tool-augmented AI ecosystems, its security and reli-
> ability have drawn increasing attention [21, 23]. Most prior work
> characterizes the MCP attack surface rather than statically recov-
> ering vulnerable data flows in server implementations. Hasan et
> al. [21] measure open-source MCP servers and identify common
> vulnerability categories and maintenance weaknesses, while Hou et
> al. [23] survey the broader MCP landscape, threat model, and open
> research directions. Zhao et al. [66] present a taxonomy of malicious
> MCP server behaviors and demonstrate proof-of-concept exploits,
> and Radosevich and Halloran [50] show that current MCP work-
> flows remain vulnerable to severe

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 39180:39310]
> We study this
> question on a benchmark of confirmed MCP vulnerability
> cases, using case-level detections and recall for comparison.
**Location**: `Evaluation Setup` [offsets: 40960:40968]
> Dataset.
**Location**: `Evaluation Setup` [offsets: 41499:41605]
> For RQ2, we gathered MCP server repositories
> from three public registries: mcp.so, PulseMCP, and MCPWorld.
**Location**: `Evaluation Setup` [offsets: 41606:41739]
> Start-
> ing from 75,380 GitHub repository links, URL normalization and
> cross-source deduplication produced 63,639 unique repositories.
**Location**: `Evaluation Setup` [offsets: 41740:41985]
> We
> then enriched each repository with GitHub metadata and applied
> rule-based filtering to retain accessible repositories likely to imple-
> ment MCP servers, removing clients, SDKs, examples, templates,
> registries, and archived or forked projects.
**Location**: `Evaluation Setup` [offsets: 42214:42341]
> The corpus contains 15,452 repositories: 8,047 in Python
> (52.1%), 4,977 in TypeScript (32.2%), and 2,428 in JavaScript (15.7%).

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 39626:39753]
> An ablation study is used to
> isolate how the major MCP-aware components affect reviewed-
> instance coverage and triage outcomes.
**Location**: `Evaluation Setup` [offsets: 40445:40455]
> Baselines.
**Location**: `Evaluation Setup` [offsets: 40456:40566]
> We compare MCP-BiFlow against four baseline tools:
> CodeQL [15], Semgrep [52], Snyk Code [54], and MCPScan [2].
**Location**: `Evaluation Setup` [offsets: 40567:40698]
> CodeQL
> serves as a representative query-based static analysis baseline, while
> Semgrep represents a lightweight rule-based analyzer.
**Location**: `Evaluation Setup` [offsets: 40699:40845]
> Snyk Code
> is a commercial semantic SAST baseline with announced support
> for MCP-specific input sources, mainly in FastMCP-based imple-
> mentations.
**Location**: `Evaluation Setup` [offsets: 40846:40959]
> MCPScan is the closest MCP-oriented baseline in our
> comparison, combining rule matching with LLM-assisted triage.

## Block 7: Cost Excerpts
**Location**: `Evaluation Setup` [offsets: 42629:42748]
> Because the benchmark contains only vulnerable cases, we report
> case-level detections and recall rather than precision.

## Block 8: Limitations
**Section Heading**: `Limitations. MCP-BiFlow targets unsafe cross-boundary data` [section offsets: 55893:56765]
**First 120 words verbatim** [offsets: 55893:56840]
> Limitations. MCP-BiFlow targets unsafe cross-boundary data
> flows rather than the full space of MCP security problems. Authen-
> tication, authorization, business-logic, and deployment flaws fall
> outside its scope unless they manifest as analyzable data-flow viola-
> tions, and metadata-level attacks such as tool-description poisoning
> are not directly addressed unless those artifacts propagate into exe-
> cutable code paths captured by the analysis. On the practical side,
> false positives remain the main challenge: the pipeline may over-
> approximate attacker control, overlook effective local constraints,
> 
> or flag flows whose targets are fixed, configuration-only, or other-
> wise not meaningfully attacker-influenced. Completeness can also
> suffer when servers rely on reflective dispatch, runtime-generated
> handlers, or framework-specific wrappers. Finally, the real-world
> evaluation is disclosure-oriented, and semantically ambiguous cases
> require

## Block 9: Adaptivity Hits
no hits
