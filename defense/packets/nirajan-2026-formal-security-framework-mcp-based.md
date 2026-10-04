# Evidence Locator Packet: nirajan-2026-formal-security-framework-mcp-based

- **Title**: A Formal Security Framework for MCP-Based AI Agents: Threat Taxonomy, Verification Models, and Defense Mechanisms
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: survey_review
- **Link**: https://arxiv.org/abs/2604.05969
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\nirajan-2026-formal-security-framework-mcp-based\fulltext.txt
- **Character Count**: 54864

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP), introduced by` [offsets: 827:924]
> This
> paper presents MCPSHIELD, a comprehensive formal security
> framework for MCP-based AI agents.
**Location**: `I. INTRODUCTION` [offsets: 5667:6536]
> Our contributions are:
> 
> • Unified Threat Taxonomy (Section III). We synthesize
> findings from 12 MCP security papers, 5 benchmarks, and
> the OWASP Top 10 for LLM Applications into a hierarchical
> taxonomy of 7 threat categories and 23 attack vectors orga-
> nized across 4 attack surfaces, providing the first common
> vocabulary for MCP security.
> 
> • Formal Verification Model (Section IV). We introduce a
> labeled transition system with trust-boundary annotations
> (MMCP) that formalizes MCP interactions as state tran-
> sitions. We define four fundamental security properties—
> tool integrity, data confinement, privilege boundedness, and
> context isolation—and provide decidability results for their
> verification.
> 
> • Comparative Defense Analysis (Section V). We systemat-
> ically evaluate 12 existing defense mechanisms against our
> taxonomy, mapping coverage gaps and identifying

## Block 3: Method Locator
**Section Heading**: `A Formal Security Framework for MCP-Based AI` [section offsets: 0:96]
**First 120 words verbatim** [offsets: 0:880]
> A Formal Security Framework for MCP-Based AI
> Agents: Threat Taxonomy, Verification Models, and
> 
> Abstract—The Model Context Protocol (MCP), introduced by
> Anthropic in November 2024 and now governed by the Linux
> Foundation’s Agentic AI Foundation, has rapidly become the de
> facto standard for connecting large language model (LLM)-based
> agents to external tools and data sources, with over 97 million
> monthly SDK downloads and more than 177,000 registered tools.
> However, this explosive adoption has exposed a critical gap:
> the absence of a unified, formal security framework capable
> of systematically characterizing, analyzing, and mitigating the
> diverse threats facing MCP-based agent ecosystems. Existing
> security research remains fragmented across individual attack
> papers, isolated benchmarks, and point defense mechanisms. This
> paper presents MCPSHIELD, a comprehensive formal
**Section Heading**: `LLM Applications [27], the STRIDE framework [28], and the` [section offsets: 13049:13144]
**First 120 words verbatim** [offsets: 13049:13924]
> LLM Applications [27], the STRIDE framework [28], and the
> 177,000-tool empirical dataset [7].
> 
> A. Attack Surface Model
> 
> We identify four attack surfaces in MCP-based agent sys-
> tems:
> 
> Definition 1 (MCP Attack Surfaces). An MCP agent system
> exposes four attack surfaces:
> 
> 1) Stool: Tool Interface Surface. The boundary between the
> LLM agent and MCP tool definitions, including tool de-
> scriptions, parameter schemas, and return values.
> 2) Stransport: Transport Surface. The communication channel
> between MCP clients and servers, including JSON-RPC
> messages, session state, and transport-layer security.
> 3) Sserver: Server Surface. The MCP server implementation
> itself, including its authentication mechanisms, resource
> access patterns, and supply chain dependencies.
> 4) Scompose: Composition Surface. The emergent surface cre-
> ated when multiple MCP servers, tools, and agents
**Section Heading**: `D. Verification Approach` [section offsets: 26166:27464]
**First 120 words verbatim** [offsets: 26166:26933]
> D. Verification Approach
> 
> Theorem 1 (Decidability of Tool Integrity). Tool integrity
> (Property 1) is decidable in O(|τ|·|T|) time by maintaining a
> cryptographic hash of each tool’s definition at approval time
> and comparing it before each invocation.
> 
> Proof. At approval time, compute ht = H(def(t)) for each
> tool t, where H is a collision-resistant hash function. Before
> each invocation call(t), compute h′
> 
> t = H(defcurrent(t)). The
> check ht = h′
> 
> t requires O(1) per invocation, and there are at
> most |τ| invocations across |T| tools.
> 
> Theorem 2 (Decidability of Data Confinement). Data con-
> finement (Property 2) is decidable when the number of trust
> domains and security levels is finite, by constructing the
> product automaton of the MCP transition system and the
**Section Heading**: `VI. MCPSHIELD: DEFENSE-IN-DEPTH ARCHITECTURE` [section offsets: 32482:32743]
**First 120 words verbatim** [offsets: 32482:33356]
> VI. MCPSHIELD: DEFENSE-IN-DEPTH ARCHITECTURE
> 
> Based on the coverage gap analysis, we propose MCP-
> SHIELD, a layered security architecture that integrates four
> complementary defense layers to achieve comprehensive cov-
> erage across all seven threat categories.
> 
> A. Architectural Overview
> 
> MCPSHIELD follows a defense-in-depth strategy inspired
> by zero trust principles [36] and capability-based security [37].
> The architecture consists of four layers:
> 1) Layer 1: Capability-Based Access Control (L-CAC).
> Governs what each agent can do by restricting tool in-
> vocations to explicitly granted capabilities.
> 2) Layer 2: Cryptographic Tool Attestation (L-CTA). En-
> sures what each tool is by verifying tool identity, integrity,
> and provenance at every invocation.
> 3) Layer 3: Information Flow Tracking (L-IFT). Controls
> where data goes by enforcing the data confinement property

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `Abstract—The Model Context Protocol (MCP), introduced by` [offsets: 697:826]
> Existing
> security research remains fragmented across individual attack
> papers, isolated benchmarks, and point defense mechanisms.
**Location**: `I. INTRODUCTION` [offsets: 4565:4715]
> Benchmarks
> such
> as
> MCPTox
> [10],
> MCP-SafetyBench
> [14],
> and
> MCPSecBench
> [13]
> evaluate
> specific
> attack
> categories
> but use incompatible threat taxonomies.
**Location**: `I. INTRODUCTION` [offsets: 5732:6007]
> We synthesize
> findings from 12 MCP security papers, 5 benchmarks, and
> the OWASP Top 10 for LLM Applications into a hierarchical
> taxonomy of 7 threat categories and 23 attack vectors orga-
> nized across 4 attack surfaces, providing the first common
> vocabulary for MCP security.
**Location**: `B. MCP Ecosystem Scale` [offsets: 8508:8693]
> Stein [7] conducted the first large-scale empirical study of
> the MCP ecosystem, monitoring 177,436 tools across public
> MCP server repositories between November 2024 and Febru-
> ary 2026.
**Location**: `D. Related Security Work` [offsets: 10636:10651]
> MCP Benchmarks.
**Location**: `D. Related Security Work` [offsets: 10652:10807]
> MCPTox [10] benchmarks tool poison-
> ing attacks across 45 real-world MCP servers with 353 tools
> and 1,312 malicious test cases spanning 11 risk categories.

## Block 6: Baseline Excerpts
**Location**: `D. Related Security Work` [offsets: 12290:12601]
> Unlike prior work, this paper provides:
> (a) a unified threat taxonomy reconciling all existing MCP-
> specific taxonomies, (b) the first formal model with verifiable
> security properties for MCP interactions, and (c) a defense-in-
> depth architecture informed by systematic coverage analysis
> of existing mechanisms.

## Block 7: Cost Excerpts
**Location**: `Abstract—The Model Context Protocol (MCP), introduced by` [offsets: 925:1636]
> We make four principal
> contributions: (1) a hierarchical threat taxonomy comprising
> 7 threat categories and 23 distinct attack vectors organized
> across four attack surfaces, grounded in the analysis of 177,000+
> MCP tools; (2) a formal verification model based on labeled
> transition systems with trust-boundary annotations that enables
> static and runtime analysis of MCP tool interaction chains; (3) a
> systematic comparative evaluation of 12 existing defense mecha-
> nisms, identifying coverage gaps across our threat taxonomy;
> and (4) a defense-in-depth reference architecture integrating
> capability-based access control, cryptographic tool attestation,
> information flow tracking, and runtime policy enforcement.
**Location**: `I. INTRODUCTION` [offsets: 6704:6924]
> We propose MCPSHIELD, an integrated security architec-
> ture combining four complementary layers: capability-based
> access control, cryptographic tool attestation, information
> flow tracking, and runtime policy enforcement.
**Location**: `B. Threat Categories` [offsets: 17974:18069]
> An attacker composes indi-
> vidually benign tool invocations to achieve an unauthorized
> outcome.
**Location**: `D. Verification Approach` [offsets: 27207:27462]
> We note that runtime enforcement of these properties can
> leverage security automata [33], where a monitor observes
> the trace of MCP operations and terminates (or modifies,
> following edit automata [34]) any execution that would violate
> a security property.
**Location**: `V. COMPARATIVE ANALYSIS OF DEFENSE MECHANISMS` [offsets: 27598:27801]
> For each mechanism, we assess:
> (a) which threat categories it addresses, (b) its enforcement
> model (preventive, detective, or reactive), (c) its deployment
> requirements, and (d) its performance overhead.
**Location**: `A. Defense Mechanism Catalog` [offsets: 28221:28438]
> Three-stage defense: Stage 1 per-
> forms lightweight pattern-based static scanning (<2ms la-
> tency), Stage 2 uses E5 text embeddings for deep neural
> detection, and Stage 3 employs LLM arbitration for ambigu-
> ous cases.

## Block 8: Limitations
**Section Heading**: `D. Limitations` [section offsets: 41774:42932]
**First 120 words verbatim** [offsets: 41774:42645]
> D. Limitations
> 
> Our work has several limitations that we acknowledge
> transparently:
> 1) Theoretical framework without implementation. MCP-
> SHIELD is a reference architecture with formal properties
> but has not been implemented or empirically evaluated.
> Real-world deployment may reveal practical challenges not
> captured in our model.
> 2) LLM-internal attacks are out of scope. Our formal model
> operates at the protocol level and cannot address attacks
> that exploit LLM-internal reasoning (e.g., sophisticated
> prompt injections that bypass semantic analysis). Defense
> against these requires advances in LLM alignment and
> robustness.
> 3) Coverage metric is theoretical. Our 91% coverage claim
> is based on mapping defense layers to threat vectors. Actual
> effectiveness depends on the quality of implementation and
> the adversary’s sophistication.
> 4) Dynamic threat landscape. Our

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `VIII. OPEN RESEARCH CHALLENGES` [offsets: 44354:44711]
> Each MCPSHIELD layer can itself become an attack target.
> An adversary might craft tool descriptions that evade MCP-
> Guard’s pattern matching, forge capabilities by exploiting
> implementation bugs, or poison the behavioral profiles used
> for anomaly detection. A security analysis of the defense
> architecture itself (defense-against-defense attacks) is needed.
