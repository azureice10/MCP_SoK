# Evidence Locator Packet: yutao-2026-description-code-inconsistency-real-world

- **Title**: Description-Code Inconsistency in Real-world MCP Servers: Measurement, Detection, and Security Implications
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: benchmark_measurement
- **Link**: https://arxiv.org/abs/2606.04769
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\yutao-2026-description-code-inconsistency-real-world\fulltext.txt
- **Character Count**: 88810

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged as` [offsets: 842:923]
> In this paper, we present a comprehensive study of DCI
> in real-world MCP servers.
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged as` [offsets: 1060:1303]
> Guided by this
> taxonomy, we develop DCIChecker, an automated framework
> that combines structure-aware static analysis with the Direct-
> Reverse-Arbitration prompting method to cross-validate tool
> descriptions against actual code implementations.
**Location**: `Abstract—The Model Context Protocol (MCP) has emerged as` [offsets: 1698:1834]
> Finally, we
> propose mitigation strategies to enforce semantic consistency and
> enhance the reliability of the emerging agentic ecosystem.
**Location**: `I. INTRODUCTION` [offsets: 5470:6324]
> we present a comprehensive study
> of DCI in real-world MCP servers. Our study addresses three
> core questions: what DCI is, how to detect it at scale, and how
> much it matters in practice. We first introduce a taxonomy
> of DCI along two orthogonal dimensions: 1) Functionality
> Inconsistency captures mismatches in a tool’s primary intent,
> where the implementation fails to align with the promised
> functionality. This type includes overclaimed functionality
> (claiming non-existent capabilities), undeclared functionality
> (omitting existing capabilities), misclaimed functionality (per-
> forming a different task), and ambiguous descriptions that
> obscure the tool’s true purpose. 2) Undeclared Side Effects
> captures cases where the environmental impacts of executing
> a tool are not explicitly stated in the description, such as
> state mutations (e.g., unexpected

## Block 3: Method Locator
**Section Heading**: `implementation code, and then applies LLM-based seman-` [section offsets: 6713:9337]
**First 120 words verbatim** [offsets: 6713:7580]
> implementation code, and then applies LLM-based seman-
> tic reasoning to assess their consistency. To mitigate LLM
> sycophancy [5] and hallucinations [6], DCIChecker adopts a
> Direct-Reverse-Arbitration (DRA) prompting strategy. Specif-
> ically, DCIChecker issues both a direct prompt querying
> semantic consistency and a reverse prompt querying incon-
> sistency, and compares the resulting judgments and reasoning
> chains. When the two judgments conflict, an additional arbi-
> tration step is invoked to reconcile the final decision based
> on their rationales. Our evaluation shows that this design
> significantly improves both precision and recall, effectively
> reducing prompt-induced bias.
> 
> Using DCIChecker, we conduct a large-scale measurement
> study of DCI in real-world MCP servers. Our results show
> that DCI is widespread, affecting 9.93% of all tools, with a
> pronounced
**Section Heading**: `implementation. A typical workflow therefore proceeds as` [section offsets: 10842:11755]
**First 120 words verbatim** [offsets: 10842:11623]
> implementation. A typical workflow therefore proceeds as
> follows: the client retrieves a set of tools from one or more
> MCP servers, the LLM reads their descriptions, selects the
> tool that appears to match the user intent, and then constructs
> 
> --- PAGE BREAK ---
> 
> a structured invocation that conforms to the declared schema.
> This process is grounded entirely in server-provided metadata
> rather than verified runtime behavior.
> 
> This design makes MCP highly flexible and easy to extend,
> since tools can be integrated without requiring models to learn
> rigid, domain-specific APIs. At the same time, it creates a
> visibility gap: the LLM sees only the description-side interface,
> while the implementation remains opaque. As a result, the
> model implicitly assumes that the description is
**Section Heading**: `implementation. As shown in Table I, we further distinguish` [section offsets: 14338:14789]
**First 120 words verbatim** [offsets: 14338:15199]
> implementation. As shown in Table I, we further distinguish
> four subtypes according to the relation between claimed and
> implemented functionality.
> 
> Func-Un (Undeclared Functionality). Undeclared function-
> ality arises when the implementation provides additional func-
> tionality beyond what the description discloses. For example, a
> tool described as “search local files by name” may also query
> cloud storage and merge remote matches into the returned
> results. Although the visible task still appears to be file search,
> the implementation performs an additional undeclared function
> that lies outside the LLM’s reasoning context. Such hidden
> functionality can cause the LLM to invoke external capabilities
> it never intends, or to select the tool under an incomplete
> understanding of what it actually does.
> 
> Func-Over (Overclaimed Functionality). Overclaimed func-
**Section Heading**: `D. Implementation Details` [section offsets: 30465:30918]
**First 120 words verbatim** [offsets: 30465:31304]
> D. Implementation Details
> 
> DCIChecker is implemented using both static analysis and
> LLM-driven classification. To ensure deterministic and repro-
> ducible outputs, we use claude-sonnet-4-5-20250929-thinking
> with temperature set to 0, top-p set to 1.0, and a maximum
> generation length of 4, 096 tokens. In our experiments, we set
> the depth k = 3, which provides sufficient coverage of local
> business logic while keeping the analysis tractable. Additional
> implementation details, including the semantic extraction de-
> tails, the DRA-Prompting algorithm, and the prompt templates
> used, are provided in Appendices A and B.
> 
> V. REAL-WORLD MEASUREMENT
> 
> In this section, we present a large-scale empirical study
> of DCI in real-world MCP servers. We begin by introducing
> the dataset for comprehensively evaluating the effectiveness of
> DCI detection

## Block 4: Evaluation Locator
**Section Heading**: `results. Although the visible task still appears to be file search,` [section offsets: 14789:20658]
**First 120 words verbatim** [offsets: 14789:15601]
> results. Although the visible task still appears to be file search,
> the implementation performs an additional undeclared function
> that lies outside the LLM’s reasoning context. Such hidden
> functionality can cause the LLM to invoke external capabilities
> it never intends, or to select the tool under an incomplete
> understanding of what it actually does.
> 
> Func-Over (Overclaimed Functionality). Overclaimed func-
> tionality arises when the description advertises functionality
> that is not realized by the implementation. For example, a tool
> may claim to “search local and cloud files by name” while the
> code only searches local files. The inconsistency is not that
> the tool is entirely unrelated to its description, but that the
> claimed functionality overstates what the code can actually
> provide. Such overclaiming

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `results. Although the visible task still appears to be file search,` [offsets: 18226:18405]
> For example, a
> tool described as “search local files by name” may first
> build a full-disk index before executing the search, thereby
> imposing significant storage and CPU overhead.

## Block 8: Limitations
**Section Heading**: `Limitations and scope. Our study focuses on descrip-` [section offsets: 60540:61102]
**First 120 words verbatim** [offsets: 60540:61431]
> Limitations and scope. Our study focuses on descrip-
> tion–code consistency and does not attempt to detect gen-
> eral vulnerabilities in tool implementations unrelated to DCI.
> Moreover, automated semantic checking is inevitably imper-
> fect: descriptions can be ambiguous, implementations can
> depend on runtime context, and LLM-based analysis is prob-
> abilistic. These limitations further motivate ecosystem-level
> mitigations, including structured side-effect contracts and
> registry-based enforcement, which can reduce ambiguity and
> make verification more robust.
> 
> VIII. RELATED WORK
> 
> Comparing with MCPDiff. The closest prior work to
> ours is MCPDiff by Li et al. [9], which studies misleading
> tool descriptions in MCP through automated static analysis
> and large-scale measurement over 10,240 real-world MCP
> servers. MCPDiff reports four graded description-code match
> levels, making it the most

## Block 9: Adaptivity Hits
no hits
