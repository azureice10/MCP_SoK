# Evidence Locator Packet: biwei-2025-mcp-not-stand-misuse-cryptography

- **Title**: "MCP Does Not Stand for Misuse Cryptography Protocol": Uncovering Cryptographic Misuse in Model Context Protocol at Scale
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2512.03775
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\biwei-2025-mcp-not-stand-misuse-cryptography\fulltext.txt
- **Character Count**: 84200

## Block 2: Contribution Sentences
**Location**: `INTRODUCTION` [offsets: 7635:8586]
> we present MICRYSCOPE, a domain-specific analysis framework
> for detecting cryptographic misuses in MCP implementations. MICRYSCOPE introduces three key
> innovations: (i) a cross-language intermediate representation (IR) that normalizes cryptographic
> API usage across diverse ecosystems, ensuring consistent detection across languages; (ii) a hybrid
> dependency analysis that reconstructs both explicit and implicit relationships among functions in
> MCP’s plugin-style architecture. Unlike traditional control-flow analysis, this approach models
> may-dependencies created at runtime when the LLM orchestrates weakly coupled functions, thereby
> exposing insecure compositions that static analysis alone cannot reveal; and (iii) a taint-based misuse
> 
> --- PAGE BREAK ---
> 
> “MCP Does Not Stand for Misuse Cryptography Protocol”: Uncovering Cryptographic Misuse in Model Context Protocol
> 
> at Scale
> 3
> 
> detector that tracks data flows across function boundaries and

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
**Section Heading**: `EVALUATION` [section offsets: 45240:65091]
**First 120 words verbatim** [offsets: 45240:46073]
> EVALUATION
> 
> 5.1
> Experiment Setup
> 
> As shown in Figure 8, our analysis of those
> servers reveals several noteworthy patterns
> in markets and categories distribution. First,
> the ecosystem demonstrates a concentrated yet
> multipolar structure: while Mcpmarket alone
> accounts for roughly one quarter of all servers,
> Smithery Registry and Pulse MCP also con-
> tribute substantial shares, together forming a
> small set of dominant platforms. Second, in
> terms of functionality, Developer Tools over-
> whelmingly dominate the landscape, with more
> than half of all servers (∼5,000) falling into this
> category, underscoring the developer-centric
> nature of the MCP ecosystem. Finally, although
> secondary categories such as Data Science &
> ML, Database Management, and Web Scraping
> 
> , Vol. 1, No. 1, Article . Publication date: December 2025.
> 
> Developer

## Block 5: Attack-Set Excerpts
**Location**: `EVALUATION` [offsets: 47596:47698]
> Among them, Developer Tools
> dominate the dataset, with more than 2,300 instances from Mcpmarket alone.
**Location**: `EVALUATION` [offsets: 47699:47891]
> To mitigate class
> imbalance and avoid bias from sparsely distributed categories, we grouped the remaining servers
> into an “Other” category, ensuring a comprehensive and representative dataset.
**Location**: `EVALUATION` [offsets: 49448:49557]
> We evaluate the end-to-end performance of MICRYSCOPE when applied to the
> entire dataset of 9,403 MCP servers.
**Location**: `EVALUATION` [offsets: 50192:50364]
> The distribution suggests
> no sharp outliers: runtime grows smoothly with dataset size, and the full corpus can be processed
> in a feasible timeframe on a single workstation.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `EVALUATION` [offsets: 49433:49447]
> Time Overhead.
**Location**: `EVALUATION` [offsets: 49558:49705]
> As shown in Figure 9, the total execution time was broken down
> into three major stages: IR generation, dependency extraction, and misuse detection.
**Location**: `EVALUATION` [offsets: 49706:49818]
> The overall
> runtime is dominated by IR generation, which accounts for more than half of the total analysis time.
**Location**: `EVALUATION` [offsets: 49949:50191]
> In contrast, dependency extraction (must-/may-dependence analysis)
> and misuse detection (taint propagation and rule matching) together contribute a smaller fraction
> of the total runtime, showing that the heavy lifting lies in IR construction.
**Location**: `EVALUATION` [offsets: 50192:50364]
> The distribution suggests
> no sharp outliers: runtime grows smoothly with dataset size, and the full corpus can be processed
> in a feasible timeframe on a single workstation.
**Location**: `EVALUATION` [offsets: 50881:51152]
> When cryptographic parame-
> ters are generated dynamically at runtime (e.g.,
> IVs derived from system time or environment ran-
> domness), they may remain as unresolved vari-
> ables in the IR rather than being reduced to inse-
> cure constants, causing misuses to be overlooked.

## Block 8: Limitations
**Location**: `DISCUSSION`
**First 120 words verbatim** [offsets: 67695:68581]
> Limitations. Although MICRYSCOPE demonstrates strong capabilities in systematically uncover-
> ing cryptographic misuses across heterogeneous MCP servers, several limitations remain. First, our
> analysis pipeline is primarily static and relies on intermediate IR construction together with taint
> propagation. As a result, dynamic aspects of MCP servers (such as IVs generated at runtime from
> environment randomness or keys derived through user interactions) may not be fully captured,
> occasionally leading to false negatives. Second, our rule set, while covering eight representative mis-
> use categories, is still bounded by pre-defined patterns. Although such semantic gaps can obscure
> misuses (e.g., crypto wrapped in custom utility functions), in practice these cases are relatively rare
> compared to the broader misuse patterns we observed.Third, MICRYSCOPE focuses on code-level
> misuse

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `EVALUATION` [offsets: 51153:51491]
> Second, some projects embed cryptographic logic
> indirectly through wrappers, utility functions, or
> domain-specific libraries. If such patterns fall outside
> MICRYSCOPE ’s rule set, they may evade detection. One representative case is the MongoDB_Atlas
> server (Figure 10), where a custom md5 wrapper internally invoked the standard library.
