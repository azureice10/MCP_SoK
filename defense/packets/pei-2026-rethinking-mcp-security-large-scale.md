# Evidence Locator Packet: pei-2026-rethinking-mcp-security-large-scale

- **Title**: Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: benchmark_measurement
- **Link**: https://arxiv.org/abs/2607.11086
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\pei-2026-rethinking-mcp-security-large-scale\fulltext.txt
- **Character Count**: 108308

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 919:1005]
> We
> present MCPZoo, the largest collection of MCP servers for dynamic
> analysis to date.
**Location**: `Abstract` [offsets: 1663:1772]
> While existing scanners re-
> port that 96.89% of servers are risky, we find that these signals are
> unreliable.

## Block 3: Method Locator
**Section Heading**: `Implementation` [section offsets: 27515:32420]
**First 120 words verbatim** [offsets: 27515:28380]
> Implementation
> 
> 3.5.1
> Environment & Configuration. The MCPZoo framework is
> deployed on a cluster of 5 servers (64-core CPUs, 256 GB memory
> each), where all build, verification, and diagnosis tasks are executed
> in the environments with a standardized Ubuntu 22.04 runtime
> for MCP servers. To support automated deployment, the agents
> rely on an LLM, Qwen3-235B-A22B-Instruct, to generate deploy-
> ment configurations, interpret failure signals, and guide iterative
> adjustments. To improve robustness, each server is assigned a max-
> imum of 5 build attempts, allowing the system to iteratively refine
> configurations and maximize deployment success at scale.
> 
> 3.5.2
> Alignment on Interaction. In practice, MCP servers support
> three distinct interaction mechanisms, i.e., stdio, SSE, and Stream-
> able HTTP, which differ in initialization semantics, communication
> patterns,

## Block 4: Evaluation Locator
**Section Heading**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [section offsets: 73416:76022]
**First 120 words verbatim** [offsets: 73416:74243]
> evaluation and runtime detection of MCP threats [52, 64]. Recent
> 
> 13
> 
> work further extends these efforts with automated threat intelli-
> gence pipelines for continuous MCP risk tracking and analysis [51].
> While these studies establish essential threat models and defensive
> mechanisms, they remain limited to theoretical analysis or small-
> scale validation. There is a lack of empirical evidence regarding how
> these security issues manifest and impact the broader, real-world
> MCP ecosystem at runtime. In contrast, our work complements
> these studies with ecosystem-scale runtime measurement, showing
> how such risks appear across real MCP servers rather than only in
> threat models or small validation settings.
> The Measurement of MCP Ecosystem. Recent studies mea-
> sure the MCP ecosystem from two perspectives: static inspec-
> tion

## Block 5: Attack-Set Excerpts
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 74325:74543]
> Some work characterizes the ecosystem at
> scale, including MCP architecture, lifecycle, repository distribu-
> tion, tool domains, and server-level risks across public registries
> and open-source repositories [19, 25, 56].
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 75153:75337]
> Existing work has examined emergent agent misuse, tool poison-
> ing, prompt-injection-style attacks, and executable MCP security
> benchmarks in curated settings [10, 44, 59, 61, 64, 66].
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 75745:75844]
> Our earlier MCPZoo preprint [63] introduced the initial dataset and
> automated deployment framework.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 73416:73473]
> evaluation and runtime detection of MCP threats [52, 64].
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 73772:73915]
> There is a lack of empirical evidence regarding how
> these security issues manifest and impact the broader, real-world
> MCP ecosystem at runtime.
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 73916:74123]
> In contrast, our work complements
> these studies with ecosystem-scale runtime measurement, showing
> how such risks appear across real MCP servers rather than only in
> threat models or small validation settings.
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 74158:74267]
> Recent studies mea-
> sure the MCP ecosystem from two perspectives: static inspec-
> tion and runtime evaluation.
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 74742:74841]
> While these ap-
> proaches scale well, they cannot verify deployment feasibility or
> runtime behavior.
**Location**: `evaluation and runtime detection of MCP threats [52, 64]. Recent` [offsets: 74842:74994]
> Our study addresses this gap by separating col-
> lected ecosystem scale from the subset that can actually be deployed,
> invoked, and evaluated at runtime.

## Block 8: Limitations
**Section Heading**: `limitations stem from systematic issues, including reliance on meta-` [section offsets: 7408:8807]
**First 120 words verbatim** [offsets: 7408:8255]
> limitations stem from systematic issues, including reliance on meta-
> data patterns, incomplete runtime interaction, and heuristic or
> LLM-based inference not grounded in exploitable behavior. To-
> gether, these findings shift the conclusion from MCP servers are
> unsafe to a more critical insight: current MCP security scanners are
> not yet reliable enough to support ecosystem-level security claims.
> 
> As a supporting service, we provide a public query interface that
> maps MCP servers to multi-scanner reports, cross-scanner agree-
> ment, and validation status when available, helping users to assess
> the potential risks of MCP servers while supporting ecosystem
> transparency and self-assessment across the MCP community. We
> hope these efforts contribute to a more reliable and trustworthy
> foundation for MCP security in practice.
> Contribution. We make

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `Background` [offsets: 24759:25249]
> To ensure process stability, the agent instanti-
> ates the container in an isolated sandbox and monitors its status
> for a post-startup period. This mechanism effectively detects imme-
> diate crash loops caused by runtime configuration issues, such as
> missing environment variables or permission denials, that typically
> evade static build-time checks. Crucially, if the process stops at any
> stage due to a build error or runtime crash, the agent automatically
> collects the logs and exit codes.
