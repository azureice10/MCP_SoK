# Evidence Locator Packet: om-2026-chainwatch-kill-chain-aligned-sequential

- **Title**: ChainWatch: A Kill Chain-Aligned Sequential Detection Framework for Multi-Step Attacks in MCP-Based AI Agent Systems
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2607.19432
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\om-2026-chainwatch-kill-chain-aligned-sequential\fulltext.txt
- **Character Count**: 26263

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol is an open source stan-` [offsets: 855:951]
> This paper presents ChainWatch, a sequential
> detection framework designed for this threat class.

## Block 3: Method Locator
**Section Heading**: `A. MCP Architecture` [section offsets: 4734:5897]
**First 120 words verbatim** [offsets: 4734:5476]
> A. MCP Architecture
> 
> MCP defines a three-component architecture over JSON-
> RPC 2.0 [1]. The Host is the user-facing AI application
> — Claude Desktop, Cursor, or a custom agent. The Client
> 
> --- PAGE BREAK ---
> 
> manages connections to MCP servers on the host’s behalf.
> The Server exposes tools, resources, and prompt templates.
> When a user makes a request, the host uses the client to query
> available tools, the model reads their descriptions to decide
> which to invoke, and the client executes the call against the
> server and returns the result.
> 
> Tools are the primary attack surface because the model
> treats their descriptions as trusted input when planning which
> actions to take. Two properties of the MCP specification are
> directly relevant to
**Section Heading**: `IV. CHAINWATCH FRAMEWORK` [section offsets: 12577:12603]
**First 120 words verbatim** [offsets: 12577:13395]
> IV. CHAINWATCH FRAMEWORK
> 
> A. Architecture
> 
> The framework presented here is a design specification.
> Each component is described in terms of its intended be-
> haviour when implemented; this section does not document
> a system that is currently in operation. The Feature Extraction
> Layer converts each raw tool call into a 20-dimensional feature
> vector. The Kill Chain Stage Classifier assigns a kill chain
> stage label to each vector using an HMM. The Sequential
> Pattern Analyzer watches the sequence of stage labels and
> triggers detection rules when that sequence exhibits suspicious
> progression characteristics (Fig. 2).
> 
> Fig. 2. ChainWatch three-component detection pipeline with alert engine.
> 
> B. Feature Extraction Layer
> 
> Raw MCP tool calls — JSON objects with variable-length
> names, parameters, and responses — cannot
**Section Heading**: `A. Architecture` [section offsets: 12603:13270]
**First 120 words verbatim** [offsets: 12603:13412]
> A. Architecture
> 
> The framework presented here is a design specification.
> Each component is described in terms of its intended be-
> haviour when implemented; this section does not document
> a system that is currently in operation. The Feature Extraction
> Layer converts each raw tool call into a 20-dimensional feature
> vector. The Kill Chain Stage Classifier assigns a kill chain
> stage label to each vector using an HMM. The Sequential
> Pattern Analyzer watches the sequence of stage labels and
> triggers detection rules when that sequence exhibits suspicious
> progression characteristics (Fig. 2).
> 
> Fig. 2. ChainWatch three-component detection pipeline with alert engine.
> 
> B. Feature Extraction Layer
> 
> Raw MCP tool calls — JSON objects with variable-length
> names, parameters, and responses — cannot be directly con-

## Block 4: Evaluation Locator
**Section Heading**: `results [22]. MCPTox evaluated these attacks against 45 real-` [section offsets: 6377:7013]
**First 120 words verbatim** [offsets: 6377:7220]
> results [22]. MCPTox evaluated these attacks against 45 real-
> world MCP servers and found 72.8% success rates against o1-
> mini [10]. Rug-pull attacks gain user approval with a benign
> tool definition, then silently replace it with malicious instruc-
> tions [4], [11]. Cross-agent escalation combines injection with
> configuration poisoning across agent instances [21]. Sequential
> Tool Chain Attacks compose individually clean MCP tool calls
> into coordinated sequences achieving over 90% attack success
> rates against GPT-4.1 [5]. A review of MCP security literature
> up to April 2026 found no published defense targeting this
> threat class.
> 
> C. Existing MCP Defenses
> 
> MCPShield reasons over accumulated historical traces to
> calibrate trust in individual servers, detecting server be-
> havioural drift including tool definition changes [7]. MCP-
> Guard
**Section Heading**: `V. EVALUATION` [section offsets: 17766:17781]
**First 120 words verbatim** [offsets: 17766:18575]
> V. EVALUATION
> 
> A. Evaluation Approach
> 
> Testing ChainWatch properly requires labelled session
> traces
> where
> benign-looking
> calls
> build
> toward
> an
> at-
> tack — data that no existing benchmark provides. MCP-
> Tox [10] and MCP-AttackBench [8] were designed for per-
> invocation testing and carry no chained sequence data. MCP-
> SafetyBench [17] handles multi-turn scenarios and is where
> empirical validation is planned. Until that data exists, the eval-
> uation takes the form of scenario analyses: documented attacks
> 
> --- PAGE BREAK ---
> 
> from the research literature traced through the framework step
> by step.
> 
> B. Attack Scenario Analyses
> 
> Each scenario takes an attack sequence from the secu-
> rity research literature and traces it through the ChainWatch
> detection design, showing which rules would apply at each
> stage.
**Section Heading**: `A. Evaluation Approach` [section offsets: 17781:18366]
**First 120 words verbatim** [offsets: 17781:18590]
> A. Evaluation Approach
> 
> Testing ChainWatch properly requires labelled session
> traces
> where
> benign-looking
> calls
> build
> toward
> an
> at-
> tack — data that no existing benchmark provides. MCP-
> Tox [10] and MCP-AttackBench [8] were designed for per-
> invocation testing and carry no chained sequence data. MCP-
> SafetyBench [17] handles multi-turn scenarios and is where
> empirical validation is planned. Until that data exists, the eval-
> uation takes the form of scenario analyses: documented attacks
> 
> --- PAGE BREAK ---
> 
> from the research literature traced through the framework step
> by step.
> 
> B. Attack Scenario Analyses
> 
> Each scenario takes an attack sequence from the secu-
> rity research literature and traces it through the ChainWatch
> detection design, showing which rules would apply at each
> stage. Feature values

## Block 5: Attack-Set Excerpts
**Location**: `A. Evaluation Approach` [offsets: 17805:17961]
> Testing ChainWatch properly requires labelled session
> traces
> where
> benign-looking
> calls
> build
> toward
> an
> at-
> tack — data that no existing benchmark provides.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `results [22]. MCPTox evaluated these attacks against 45 real-` [offsets: 6510:6642]
> Rug-pull attacks gain user approval with a benign
> tool definition, then silently replace it with malicious instruc-
> tions [4], [11].
**Location**: `A. Evaluation Approach` [offsets: 17805:17961]
> Testing ChainWatch properly requires labelled session
> traces
> where
> benign-looking
> calls
> build
> toward
> an
> at-
> tack — data that no existing benchmark provides.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `Adaptive` | **Location**: `REFERENCES` [offsets: 23164:23330]
> Wang, and Q. Wen, “MCPShield: A Security Cognition
> Layer for Adaptive Trust Calibration in Model Context Protocol Agents,”
> arXiv preprint arXiv:2602.14281, Feb. 2026.
