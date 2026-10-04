# Evidence Locator Packet: arash-2025-mcp-bridge-lightweight-llm-agnostic

- **Title**: MCP Bridge: A Lightweight, LLM-Agnostic RESTful Proxy for Model Context Protocol Servers
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: position_other
- **Link**: https://arxiv.org/abs/2504.08999
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\arash-2025-mcp-bridge-lightweight-llm-agnostic\fulltext.txt
- **Character Count**: 60128

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 829:971]
> We present MCP Bridge, a lightweight RESTful proxy that
> connects to multiple MCP servers and exposes their capabilities through a unified
> API.
**Location**: `1 Introduction` [offsets: 4122:4993]
> we present MCP Bridge—a lightweight, fast, and
> LLM-agnostic proxy that connects to multiple MCP servers and exposes their capa-
> bilities through a unified REST API. The architecture is shown in Figure 1. While
> Anthropic’s MCP SDK provides a reference client/server implementation, MCP Bridge
> focuses on deployment: it acts as a stable REST adapter that allows heterogeneous
> clients (e.g., browsers, mobile applications, edge devices) to use MCP servers without
> local process execution via STDIO transports. MCP Bridge also implements a risk-
> based execution model that supports standard execution, a confirmation workflow for
> medium-risk tools, and Docker isolation for high-risk tools, while maintaining back-
> ward compatibility with standard MCP clients. The implementation is available as an
> open-source project at https://github.com/INQUIRELAB/mcp-bridge-api.
> 
> 2
> 
> ---

## Block 3: Method Locator
**Section Heading**: `Architecture, Tool Integration, Risk-Based Execution` [section offsets: 2263:2340]
**First 120 words verbatim** [offsets: 2263:3150]
> Architecture, Tool Integration, Risk-Based Execution
> 
> 1
> 
> --- PAGE BREAK ---
> 
> 1 Introduction
> 
> Large Language Models (LLMs) have revolutionized natural language processing.
> They enable sophisticated conversational agents that can understand and generate
> human-like text across numerous domains [1]. Despite their impressive capabilities,
> these models are inherently limited by their training data and lack access to real-time
> information, specialized tools, and the ability to perform actions in external systems
> [2]. To overcome these limitations, there has been a significant push toward augment-
> ing LLMs with external tools and data sources, allowing them to retrieve information,
> execute computations, and interact with various services [3].
> 
> The Model Context Protocol (MCP) represents a significant advancement in this
> direction, providing a standardized interface for connecting AI
**Section Heading**: `3 System Design and Implementation` [section offsets: 10382:10690]
**First 120 words verbatim** [offsets: 10382:11220]
> 3 System Design and Implementation
> 
> This section describes the design and implementation of MCP Bridge, a lightweight,
> fast, and LLM-agnostic proxy for Model Context Protocol (MCP) servers. We detail
> the system architecture, API design, server management, security model, and client
> integration components.
> 
> 3.1 System Architecture and Technology Stack
> 
> MCP Bridge follows a layered architecture that decouples client applications from
> the underlying MCP server processes. Figure 1 illustrates this design, where client
> applications communicate with the proxy via a standardized REST API, and the
> proxy manages connections to multiple MCP servers.
> 
> The system is built on Node.js (18+) and uses the following core components:
> 
> • Express.js: Provides the HTTP server and routing capabilities
> • Child Process API: Manages spawned MCP server
**Section Heading**: `3.1 System Architecture and Technology Stack` [section offsets: 10690:11762]
**First 120 words verbatim** [offsets: 10690:11557]
> 3.1 System Architecture and Technology Stack
> 
> MCP Bridge follows a layered architecture that decouples client applications from
> the underlying MCP server processes. Figure 1 illustrates this design, where client
> applications communicate with the proxy via a standardized REST API, and the
> proxy manages connections to multiple MCP servers.
> 
> The system is built on Node.js (18+) and uses the following core components:
> 
> • Express.js: Provides the HTTP server and routing capabilities
> • Child Process API: Manages spawned MCP server processes
> • Server-Sent Events (SSE): Enables real-time communication between some
> MCP servers and the proxy
> • Docker SDK: Facilitates containerized execution for high-risk operations
> 
> This technology stack was chosen for its minimal footprint, cross-platform com-
> patibility, and non-blocking I/O capabilities—critical requirements for
**Section Heading**: `Method` [section offsets: 12863:12883]
**First 120 words verbatim** [offsets: 12863:13775]
> Method
> Description
> 
> 3.3 Server Management and Connection Handling
> 
> 3.4 Security Model and Risk-Based Execution
> 
> The risk-based execution model defines three levels:
> 
> /servers
> GET
> List all connected MCP servers
> /servers
> POST
> Start a new MCP server
> /servers/{serverId}
> DELETE
> Stop and remove a server
> /health
> GET
> Get health status of MCP Bridge
> /confirmations/{id}
> POST
> Confirm execution of a medium-risk request
> /servers/{id}/tools
> GET
> List all tools for a specific server
> /servers/{id}/tools/{toolName}
> POST
> Execute a specific tool
> /servers/{id}/resources
> GET
> List all resources
> /servers/{id}/prompts
> GET
> List all prompts
> 
> MCP Bridge dynamically manages connections to MCP servers, supporting both stan-
> dard STDIO-based servers and newer Server-Sent Events (SSE) implementations.
> The server management subsystem handles server lifecycle (startup, monitoring, and
> teardown) and efficiently routes requests to the

## Block 4: Evaluation Locator
**Section Heading**: `methodology for MCP tool alignment; Section 5 reports experimental results and` [section offsets: 6172:6374]
**First 120 words verbatim** [offsets: 6172:7039]
> methodology for MCP tool alignment; Section 5 reports experimental results and
> comparisons; Section 6 discusses future directions; and Section 7 concludes. Reward
> ablations are provided in Appendix A.
> 
> 2 Related Work
> 
> 2.1 Tool Use and Retrieval-Augmented Language Models
> 
> Large language models (LLMs) have increasingly been augmented with external data
> sources and tools to overcome their inherent knowledge and capability limitations
> [1, 2]. One prominent approach is retrieval-augmented generation (RAG), which inte-
> grates a document retriever with the model. Lewis et al. [3] introduced RAG as
> 
> 3
> 
> --- PAGE BREAK ---
> 
> 2.2 Standardization and LLM-Agnostic Integration
> 
> a general framework combining a parametric neural generator with non-parametric
> memory of retrieved documents, demonstrating improved performance on knowledge-
> intensive tasks. By linking to live
**Section Heading**: `results ←empty list` [section offsets: 20435:22898]
**First 120 words verbatim** [offsets: 20435:21320]
> results ←empty list
> 
> 9:
> for each tool in tools do
> 
> 11:
> if result.requiresConfirmation then
> 
> 13:
> if confirmation.confirmed then
> 
> 15:
> else
> 
> 17:
> end if
> 
> 18:
> end if
> 
> 19:
> Append result to results
> 
> 20:
> end for
> 
> 21:
> followupPrompt ←BuildResultPrompt(query, tools, results)
> 
> 22:
> finalResponse ←InvokeGeminiLLM(followupPrompt)
> 
> 23:
> return finalResponse
> 
> 24: end function
> 
> • Multi-step reasoning: Supports complex operations by sequencing tool calls
> • Security confirmation handling: Seamlessly manages the confirmation workflow
> for medium-risk operations
> • Flexible JSON display: Configurable verbosity for tool outputs
> • Automatic tool discovery: Detects and utilizes all available tools from connected
> servers
> 
> The agent’s architecture follows a conversational loop pattern (see Algorithm 4),
> where user inputs are processed by the Gemini LLM to generate appropriate tool calls
> to MCP Bridge.
**Section Heading**: `3.6 System Performance Evaluation` [section offsets: 22898:23593]
**First 120 words verbatim** [offsets: 22898:23740]
> 3.6 System Performance Evaluation
> 
> To validate the architectural claims presented above and quantify the performance
> characteristics of the REST proxy layer, we conducted a systematic benchmark
> of MCP Bridge measuring end-to-end latency, throughput under concurrent load,
> risk-level execution-path overhead, and resource utilization. All measurements were
> collected on a single machine running Windows 11 with an AMD Ryzen 7 7435HS (16
> logical cores) and 24,261 MB RAM, using Node.js v22.12.0. To ensure statistical reli-
> ability, latency and concurrency tests were repeated over three independent runs with
> 50 iterations per operation per run; we report mean ± standard deviation across runs.
> 
> 3.6.1 Benchmark Configuration
> 
> Four MCP servers were started simultaneously through MCP Bridge using the con-
> figuration summarized in Table 2. The
**Section Heading**: `4.2 Training and Evaluation Data` [section offsets: 31859:32916]
**First 120 words verbatim** [offsets: 31859:32713]
> 4.2 Training and Evaluation Data
> 
> We train on tool-use data derived from Toucan-1.5M [5]. The training script filters the
> SFT portion to subsets that contain tool calls (specifically single-turn-original,
> single-turn-diversify, and multi-turn) [5]. Each training instance provides a
> user question, a tool list tools (with per-tool name and description), and a
> comma-separated target tools field indicating the expected tool(s). During prompt
> construction, the tool list is inserted into the system message under an Available
> Tools header, with the number of tools and description length capped to reduce
> context length pressure.
> 
> We evaluate on MCPToolBench++ [10], a large-scale benchmark organized by tool
> category (Browser, File System, Search, Map, Pay, Finance). Each evaluation sample
> provides a query, tool metadata, and ground-truth function-call

## Block 5: Attack-Set Excerpts
**Location**: `3.6 System Performance Evaluation` [offsets: 22933:23231]
> To validate the architectural claims presented above and quantify the performance
> characteristics of the REST proxy layer, we conducted a systematic benchmark
> of MCP Bridge measuring end-to-end latency, throughput under concurrent load,
> risk-level execution-path overhead, and resource utilization.
**Location**: `4.2 Training and Evaluation Data` [offsets: 32489:32626]
> We evaluate on MCPToolBench++ [10], a large-scale benchmark organized by tool
> category (Browser, File System, Search, Map, Pay, Finance).

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `3.6 System Performance Evaluation` [offsets: 22933:23231]
> To validate the architectural claims presented above and quantify the performance
> characteristics of the REST proxy layer, we conducted a systematic benchmark
> of MCP Bridge measuring end-to-end latency, throughput under concurrent load,
> risk-level execution-path overhead, and resource utilization.
**Location**: `3.6 System Performance Evaluation` [offsets: 23392:23591]
> To ensure statistical reli-
> ability, latency and concurrency tests were repeated over three independent runs with
> 50 iterations per operation per run; we report mean ± standard deviation across runs.
**Location**: `4.2 Training and Evaluation Data` [offsets: 32759:32890]
> For evaluation, each category is scored independently, and we
> report Precision, Recall, F1, and Accuracy aggregated across samples.
**Location**: `5 Experiments and Results` [offsets: 36423:36684]
> We evaluate tool-use behavior on MCPToolBench++ [10], reporting Precision, Recall,
> F1, and Accuracy for six tool categories (Browser, File System, Search, Map, Pay,
> Finance), with 50 randomly sampled evaluation instances per category (N=300 total;
> see Table 8).

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `6 Future Work` [offsets: 43550:44048]
> On the systems side, MCP Bridge can be extended with production-oriented fea-
> tures such as stronger multi-tenancy support, richer observability (structured tracing
> of tool calls and outcomes), and adaptive caching for idempotent requests. While the
> current implementation supports STDIO and SSE-backed MCP servers, broader trans-
> port coverage and improved server lifecycle management (including persistent server
> pools and backpressure-aware scheduling) would improve throughput under heavy
> load.
