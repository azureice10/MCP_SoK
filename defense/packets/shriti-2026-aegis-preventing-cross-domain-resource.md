# Evidence Locator Packet: shriti-2026-aegis-preventing-cross-domain-resource

- **Title**: AEGIS: Preventing Cross-Domain Resource Abuse in MCP
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2608.20481
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\shriti-2026-aegis-preventing-cross-domain-resource\fulltext.txt
- **Character Count**: 39993

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) is an open-` [offsets: 1244:1441]
> In this paper, we present AEGIS, a policy enforcement compo-
> nent that enables administrators to define fine-grained safeguards
> against resource abuse across heterogeneous MCP tools and
> modalities.
**Location**: `I. INTRODUCTION` [offsets: 6733:7574]
> we present AEGIS, a secu-
> rity system that leverages the reasoning capabilities of large
> language models to assist in the creation and enforcement
> of policies that protect against resource abuse across diverse
> modalities and heterogeneous MCP servers. The main contri-
> butions of this paper are:
> 
> • A systematic investigation that identifies key parameters
> contributing to resource exhaustion across MCP servers.
> 
> • A methodology that uses LLMs to extract and normalize
> resource-related parameters from tool invocations into a
> unified taxonomy, enabling reusable policy templates and
> scalable policy enforcement across heterogeneous systems.
> 
> • A threshold estimation approach that provides end-to-end
> protection against resource abuse attacks in MCP servers.
> 
> II. BACKGROUND AND RELATED WORK
> 
> The Model Context Protocol (MCP) [1] is an open

## Block 3: Method Locator
**Section Heading**: `IV. APPROACH` [section offsets: 11614:11987]
**First 120 words verbatim** [offsets: 11614:12444]
> IV. APPROACH
> 
> Our approach addresses resource abuse in MCP servers
> through a Tool Ontology that formalizes and simplifies tool
> definitions. The ontology categorizes tools and their param-
> eters, enabling reusable policies and thresholds that prevent
> resource abuse. This section introduces the ontology and
> policy model; the next section presents the system architecture.
> 
> A. Tool Ontology
> 
> Figure 1(a) illustrates an MCP tool definition for a
> generateImages tool that generates n images at a speci-
> fied resolution. The figure also shows the corresponding
> Tool Ontology, which extracts the following information from
> the tool definition.
> 
> Modality. The primary data type processed by a tool (e.g., im-
> age, video, audio, text, location, or human-in-the-loop input).
> For example, generateImages is classified as an image
> modality.
**Section Heading**: `V. AEGIS SYSTEM ARCHITECTURE` [section offsets: 15891:16158]
**First 120 words verbatim** [offsets: 15891:16730]
> V. AEGIS SYSTEM ARCHITECTURE
> 
> AEGIS generates tool ontologies from tool definitions, con-
> structs policy templates, and estimates policy thresholds. The
> resulting policies are enforced through an MCP gateway.
> AEGIS operates in two phases: Bootstrapping and Runtime.
> 
> A. Bootstrapping Phase
> 
> Bootstrapping is an offline process that prepares policies
> before deployment. Figure 2 illustrates the bootstrapping phase
> of AEGIS, which consists of seven steps described below:
> 
> Collection (Step 1). At first AEGIS retrieves tool definitions
> registered with the MCP gateway using the list_tools()
> API, which returns tool schemas and metadata.
> 
> Ontology Identification (Step 2). Each tool definition is pro-
> cessed by an LLM using a structured system prompt (Figure 3)
> to generate a corresponding tool ontology. The prompt guides
> the model through
**Section Heading**: `B. Runtime Phase` [section offsets: 22626:23212]
**First 120 words verbatim** [offsets: 22626:23406]
> B. Runtime Phase
> 
> Figure 4 illustrates the runtime phase of AEGIS. At runtime,
> policies are enforced using a framework such as Open Policy
> 
> --- PAGE BREAK ---
> 
> Fig. 4. AEGIS Runtime
> 
> Agent (OPA). During a tool invocation, AEGIS checks whether
> the tool ontology exists in the cache. If present, the request
> parameters are normalized and evaluated against the policy.
> Requests within threshold limits are forwarded to the MCP
> server; otherwise they are rejected.
> 
> If the ontology is not cached, the request bypasses normal-
> ization and is considered out of scope for policy enforcement.
> 
> VI. IMPLEMENTATION
> 
> The runtime component of AEGIS was implemented using
> the ContextForge AI Gateway [8]. The system leverages the
> gateway’s plugin framework, which enables modular extension
> and
**Section Heading**: `VI. IMPLEMENTATION` [section offsets: 23212:23891]
**First 120 words verbatim** [offsets: 23212:24040]
> VI. IMPLEMENTATION
> 
> The runtime component of AEGIS was implemented using
> the ContextForge AI Gateway [8]. The system leverages the
> gateway’s plugin framework, which enables modular extension
> and policy control. To manage policy enforcement, the pre-
> existing OPA (Open Policy Agent) plugin was adopted as the
> foundational enforcement layer. In this configuration, each tool
> invocation request is first processed by AEGIS before being
> forwarded to OPA.
> 
> During the bootstrapping phase AEGIS collects all the tool
> definitions of the registered servers in the gateway running
> ontology identification using the Claude 4 Sonnet [27] LLM.
> Ontologies are cached in the Redis Database.
> 
> VII. EVALUATION
> 
> We evaluate AEGIS through the following research ques-
> tions.
> 
> RQ1. How accurately can AEGIS identify and categorize tool
> ontologies

## Block 4: Evaluation Locator
**Section Heading**: `VII. EVALUATION` [section offsets: 23891:24156]
**First 120 words verbatim** [offsets: 23891:24725]
> VII. EVALUATION
> 
> We evaluate AEGIS through the following research ques-
> tions.
> 
> RQ1. How accurately can AEGIS identify and categorize tool
> ontologies from MCP tool definitions?
> 
> RQ2. How effective is AEGIS at protecting MCP servers
> against resource abuse attacks?
> 
> A. Dataset
> 
> Since no publicly available labeled dataset exists for this
> task, we curated a dataset from 56 MCP servers spanning
> diverse modalities in the OpenTools MCP Registry [28].
> Across these servers, we collected 937 tool definitions. The
> corresponding tool schemas were crawled from the registry,
> and a custom parser extracted relevant metadata including
> tool names, descriptions, parameters, and associated server
> information.
> 
> The dataset covers a broad set of real-world MCP cat-
> egories, including Cloud Infrastructure (AWS, Azure, Al-
> ibaba, Qiniu), Database
**Section Heading**: `Experiments were conducted using Claude 4 Sonnet LLM` [section offsets: 26733:27645]
**First 120 words verbatim** [offsets: 26733:27594]
> Experiments were conducted using Claude 4 Sonnet LLM
> and repeated across three runs with default inference settings
> with each inference taking approximately 0.52 seconds. Over-
> all results show more than 84% accuracy across all ontology
> identification tasks. The model performed best on modality,
> operation, parameter characteristics classification and resource
> consumption detection tasks. Parameter normalization has
> lower performance metrics as compared to other tasks due
> to the complexity of the problem. Misclassifications primarily
> occurred in cases requiring additional contextual interpreta-
> tion. For example, distinguishing between storing a binary
> image file and posting an image on a social media platform
> requires understanding platform semantics. In systems such
> as Instagram, the term “post” may refer to either text or
> image content, leading to
**Section Heading**: `experiments were run on a MacBook Pro (Apple M1 Max chip` [section offsets: 30716:30794]
**First 120 words verbatim** [offsets: 30716:31541]
> experiments were run on a MacBook Pro (Apple M1 Max chip
> with 64 GB of RAM).
> 
> Experiments used MCP ClientSession with SSE trans-
> port. For each run, we collected the following metrics: latency
> (mean, min, max, median, p95, p99, standard deviation),
> throughput (requests/sec), error rate, resource usage (CPU
> and memory), and total wall-clock execution time. Although
> multiple metrics were recorded, the primary criterion for
> selecting parameter thresholds was error rate, as it generalizes
> well across heterogeneous MCP servers. Following MCP best
> practices [30], we targeted an error rate below 0.1%.
> 
> AEGIS analyzes the benchmarking results to determine
> parameter limits that maintain reliable performance under
> concurrent load. Across the 118 benchmark runs as mentioned
> in Figure 5, count=10 consistently maintained error
**Section Heading**: `Experiments used MCP ClientSession with SSE trans-` [section offsets: 30794:32211]
**First 120 words verbatim** [offsets: 30794:31647]
> Experiments used MCP ClientSession with SSE trans-
> port. For each run, we collected the following metrics: latency
> (mean, min, max, median, p95, p99, standard deviation),
> throughput (requests/sec), error rate, resource usage (CPU
> and memory), and total wall-clock execution time. Although
> multiple metrics were recorded, the primary criterion for
> selecting parameter thresholds was error rate, as it generalizes
> well across heterogeneous MCP servers. Following MCP best
> practices [30], we targeted an error rate below 0.1%.
> 
> AEGIS analyzes the benchmarking results to determine
> parameter limits that maintain reliable performance under
> concurrent load. Across the 118 benchmark runs as mentioned
> in Figure 5, count=10 consistently maintained error rates
> below 0.1% across all load levels, whereas count=100
> caused significant error spikes. Based on this

## Block 5: Attack-Set Excerpts
**Location**: `Experiments used MCP ClientSession with SSE trans-` [offsets: 31447:31633]
> Across the 118 benchmark runs as mentioned
> in Figure 5, count=10 consistently maintained error rates
> below 0.1% across all load levels, whereas count=100
> caused significant error spikes.

## Block 6: Baseline Excerpts
**Location**: `Experiments were conducted using Claude 4 Sonnet LLM` [offsets: 27124:27242]
> Parameter normalization has
> lower performance metrics as compared to other tasks due
> to the complexity of the problem.
**Location**: `Experiments used MCP ClientSession with SSE trans-` [offsets: 31840:32068]
> Specifically, we simulated an abuse scenario
> using count=1000 under a 200-concurrent-user load (1
> request per user) and measured the impact on key resources
> in both unprotected and protected configurations as shown in
> Table III.

## Block 7: Cost Excerpts
**Location**: `Experiments were conducted using Claude 4 Sonnet LLM` [offsets: 26733:26903]
> Experiments were conducted using Claude 4 Sonnet LLM
> and repeated across three runs with default inference settings
> with each inference taking approximately 0.52 seconds.
**Location**: `Experiments used MCP ClientSession with SSE trans-` [offsets: 30851:31073]
> For each run, we collected the following metrics: latency
> (mean, min, max, median, p95, p99, standard deviation),
> throughput (requests/sec), error rate, resource usage (CPU
> and memory), and total wall-clock execution time.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
