# Evidence Locator Packet: mehrdad-2026-mcp-dpt-defense-placement-taxonomy

- **Title**: MCP-DPT: A Defense-Placement Taxonomy and Coverage Analysis for Model Context Protocol Security
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: survey_review
- **Link**: https://arxiv.org/abs/2604.07551
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\mehrdad-2026-mcp-dpt-defense-placement-taxonomy\fulltext.txt
- **Character Count**: 95447

## Block 2: Contribution Sentences
no hits

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `Header / Abstract` [offsets: 617:770]
> are largely attack-centric or benchmark-driven, providing limited guidance on where mitigation responsibility should reside within
> 
> the MCP architecture.
**Location**: `Introduction` [offsets: 4372:4468]
> Recent work has started to systematize MCP security through dedicated benchmarks and taxonomies.
**Location**: `Background` [offsets: 12534:12638]
> Several benchmark efforts introduce taxonomies through structured attack lists and evaluation pipelines.
**Location**: `Background` [offsets: 13255:13307]
> centric taxonomies or benchmark-driven threat lists.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 15538:15762]
> Current benchmarks primarily evaluate attack feasibility and success, but
> 
> seldom map attacks to available academic or industrial defenses or explicitly identify which attacks remain
> 
> • Lack of a systematic defense overview.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 17509:17667]
> descriptions from benchmarks [16, 62, 67], server-side threat analyses [46, 47, 67], ecosystem measurement studies
> 
> [18], and protocol safety frameworks [23].

## Block 6: Baseline Excerpts
**Location**: `Background` [offsets: 13205:13307]
> 2.4
> Prior Work on MCP Security Attack Taxonomies
> 
> centric taxonomies or benchmark-driven threat lists.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 16598:16796]
> Critically, no prior work explicitly maps
> 
> attacks to defense layers or assigns enforcement responsibility to specific architectural stakeholders — both dimensions
> 
> receive × across all six columns.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 16880:17045]
> MCIP being the strongest prior work (✓on defense-in-depth), yet even MCIP does not identify primary versus secondary
> 
> defense points or expose under-defended layers.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 22541:22758]
> Prior work has shown that many failures in LLM-based
> 
> systems arise not from the model itself, but from insufficient enforcement at the application boundary where model
> 
> decisions are translated into actions [25, 56].
**Location**: `Conclusion` [offsets: 65621:65856]
> Prior work indicates that MCP agents can be misled about the semantic role or trust
> 
> level of resources returned by tools or servers, causing untrusted artifacts to be interpreted as authoritative data or executable
> 
> guidance [41, 66].
**Location**: `Conclusion` [offsets: 66704:66917]
> Prior work shows that manipulated intermediate outputs or
> 
> context can cause MCP agents to deviate from expected execution paths, although these behaviors are not explicitly framed as
> 
> Malicious Tool Registration.

## Block 7: Cost Excerpts
**Location**: `Introduction` [offsets: 4254:4468]
> (creation, operation, update) and emphasize that distribution and maintenance practices are inseparable from runtime
> 
> Recent work has started to systematize MCP security through dedicated benchmarks and taxonomies.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 15195:15537]
> Proposed defenses—including protocol-level constraints and runtime monitoring
> 
> mechanisms—address only subsets of known attacks, leaving gaps at critical layers such as registries, clients,
> 
> --- PAGE BREAK ---
> 
> MCP-DPT: A Defense-Placement Taxonomy and Coverage Analysis for Model Context Protocol Security
> 5
> 
> • Unclear defense effectiveness.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 23564:23795]
> The MCP Client/SDK layer comprises the software runtime that bridges the language model-
> 
> driven agent with external MCP servers, handling protocol parsing, request construction, response interpretation, and
> 
> local execution logic.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 24519:24756]
> The MCP Server/Tool Execution layer represents the runtime environment in
> 
> which MCP tools are implemented and executed [42, 49], including server-side logic, exposed APIs, authentication
> 
> checks, plugin loading, and resource management.
**Location**: `Limitations of Existing MCP Security Research` [offsets: 27682:27768]
> guarantees, and long-term ecosystem safety rather than runtime correctness alone [18].
**Location**: `Limitations of Existing MCP Security Research` [offsets: 29600:29731]
> intervention before malicious influence propagates into later stages such as orchestration, tool invocation, or runtime
> 
> execution.

## Block 8: Limitations
**Section Heading**: `Limitations of Existing MCP Security Research` [section offsets: 13457:49221]
**First 120 words verbatim** [offsets: 13457:14405]
> Limitations of Existing MCP Security Research
> 
> important limitations.
> 
> components are responsible for enforcement.
> 
> about defense ordering and composition.
> 
> transport, and the software supply chain.
> 
> Extending attack categorization to more realistic settings, Zong et al. [69] introduce MCP-SafetyBench, which
> 
> classifies attacks across server-, host-, and user-level interactions and highlights compounding safety failures in multi-
> 
> turn, cross-server workflows. Complementing these studies, the large-scale ecosystem analysis by Hasan et al. [18]
> 
> reveals that MCP-specific vulnerabilities are widespread in open-source servers, underscoring the systemic nature of the
> 
> threat landscape. Finally, Jing et al. [23] propose MCIP, a protocol-level safety framework accompanied by a fine-grained
> 
> taxonomy of unsafe MCP behaviors, emphasizing contextual integrity rather than isolated exploits. Collectively, these
> 
> works establish a rich catalog of

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `Limitations of Existing MCP Security Research` [offsets: 37252:37516]
> monitor intermediate decision signals to identify subtle manipulation attempts—such as tool poisoning or preference
> 
> steering—that may evade output-level defenses. By intervening during decision-making, they can detect attacks before
> 
> harmful actions are executed.
**Matched Term**: `evade` | **Location**: `Conclusion` [offsets: 53368:53957]
> Second, the scarcity of decision-level defenses indicates an
> 
> important research gap—attacks that steer tool selection or parameterization can evade output-only checks, especially in multi-step
> 
> workflows. In general, the taxonomy can serve as a placement-oriented checklist for evaluating MCP deployments and as a roadmap
> 
> This paper introduced a defense-placement-oriented taxonomy for Model Context Protocol (MCP) security that organizes MCP-specific
> 
> attacks by architectural responsibility and identifies primary and secondary enforcement points to support defense-in-depth reasoning.
**Matched Term**: `circumvent` | **Location**: `Conclusion` [offsets: 63126:63660]
> Prompt Injection. Prompt injection denotes any attack in which adversarial text is crafted to override, circumvent, or subvert the
> 
> model’s existing safety instructions and policies. In MCP settings, such payloads can be delivered via user input, tool output, or
> 
> --- PAGE BREAK ---
> 
> MCP-DPT: A Defense-Placement Taxonomy and Coverage Analysis for Model Context Protocol Security
> 19
> 
> external resources, causing the agent to prioritize attacker goals and potentially invoke high-impact tools in violation of the original
> 
> Goal Hijack.
