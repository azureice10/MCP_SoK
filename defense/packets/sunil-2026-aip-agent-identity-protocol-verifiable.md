# Evidence Locator Packet: sunil-2026-aip-agent-identity-protocol-verifiable

- **Title**: AIP: Agent Identity Protocol for Verifiable Delegation Across MCP and A2A
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2603.24775
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\sunil-2026-aip-agent-identity-protocol-verifiable\fulltext.txt
- **Character Count**: 55328

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 612:789]
> We introduce Invocation-Bound
> Capability Tokens (IBCTs), a primitive that fuses identity, attenuated authorization, and provenance
> binding into a single append-only token chain.
**Location**: `Introduction` [offsets: 4436:5286]
> we introduce Invocation-Bound Capability Tokens (IBCTs),
> a primitive that unifies identity, attenuated authorization, and provenance binding in a single evolvable
> token chain. IBCTs operate in two wire formats: compact mode (a signed JWT for single-hop MCP
> calls) and chained mode (a Biscuit token with Datalog policies for multi-hop delegation chains with
> completion blocks). Second, we evaluate AIP with reference implementations in Python and Rust,
> demonstrating sub-millisecond verification for compact tokens (0.049 ms Rust, 0.189 ms Python), linear
> scaling of chained tokens at 340–380 bytes per delegation block, negligible overhead (0.086% of total
> latency) in a real multi-agent deployment with Gemini 2.5 Flash inference, and 100% attack rejection
> across 600 adversarial tests spanning six attack categories.
> 
> AIP complements our prior work

## Block 3: Method Locator
**Section Heading**: `Implementation` [section offsets: 32757:35447]
**First 120 words verbatim** [offsets: 32757:33656]
> Implementation
> 
> 1https://github.com/sunilp/aip
> 
> 10
> 
> At each step, fields checked include: signature validity, scope subset enforcement, budget attenu-
> ation, depth bounds, expiry timestamps, and non-empty delegation context. The completed IBCT an-
> swers who authorized the action, through which agents the delegation flowed, what constraints applied
> at each hop, and what the outcome was.
> 
> We provide reference implementations of AIP in Python (primary SDK) and Rust (reference implemen-
> tation). Both implement compact and chained modes with full cross-language interoperability. All code
> is open source under the Apache 2.0 license.1
> 
> The Python SDK (aip-sdk) is organized into three packages. aip_core provides Ed25519 key-
> pair management (wrapping the cryptography library), AipId parsing for both aip:web and aip:key
> schemes, and identity document verification including self-signature checks.

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 35447:38916]
**First 120 words verbatim** [offsets: 35447:36211]
> Evaluation
> 
> 5.1
> Hypotheses
> 
> 5.2
> Microbenchmarks (H1, H2)
> 
> 11
> 
> Component
> Rust (crate / LOC)
> Python (package / LOC)
> Tests
> 
> Identity
> aip-core / 462
> aip_core / 309
> 6 + 19
> Tokens
> aip-token / 601
> aip_token / 442
> 7 + 27
> Middleware
> aip-mcp / 151
> aip_mcp / 76
> 7 + 12
> 
> Total
> 1,214 LOC
> 827 LOC
> 20 + 58
> 
> AIP serves as the identity layer for the JAMJET agent runtime, which also hosts our LDP pro-
> tocol (Prakash, 2025b) (provenance) and our DCI framework (Prakash, 2025a) (reasoning). Identity
> documents link to LDP via the extensions field, and completion blocks link to provenance records via
> ldp_provenance_id.
> 
> This section evaluates AIP along four dimensions: compact mode overhead (microbenchmarks), chained
> mode scaling (microbenchmarks), real-world deployment overhead

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 36315:36437]
> All benchmarks were run on an Apple
> M3 Max (macOS 15.3), using the Python and Rust implementations described in Section 4.
**Location**: `Evaluation` [offsets: 36438:36534]
> Compact
> mode benchmarks used 1,000 iterations; chained mode used 100 iterations per depth level.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 35739:35919]
> AIP serves as the identity layer for the JAMJET agent runtime, which also hosts our LDP pro-
> tocol (Prakash, 2025b) (provenance) and our DCI framework (Prakash, 2025a) (reasoning).
**Location**: `Evaluation` [offsets: 36050:36314]
> This section evaluates AIP along four dimensions: compact mode overhead (microbenchmarks), chained
> mode scaling (microbenchmarks), real-world deployment overhead with LLM inference (real HTTP and
> Gemini 2.5 Flash), and adversarial security (six attack categories).
**Location**: `Evaluation` [offsets: 36610:36731]
> We state four hypotheses:
> • H1: Compact mode adds negligible overhead to MCP tool calls (sub-millisecond over real HTTP).
**Location**: `Evaluation` [offsets: 36732:36851]
> • H2: Chained mode delegation overhead scales linearly with chain depth, both in token size and veri-
> fication latency.
**Location**: `Evaluation` [offsets: 36852:36942]
> • H3: AIP overhead is negligible relative to real LLM inference in multi-agent delegation.
**Location**: `Evaluation` [offsets: 37098:37205]
> Rust verification
> averages 0.049 ms (p99: 0.059 ms); Python verification averages 0.189 ms (p99: 0.231 ms).

## Block 8: Limitations
**Section Heading**: `limitations. Section 8 concludes.` [section offsets: 5818:5855]
**First 120 words verbatim** [offsets: 5818:6678]
> limitations. Section 8 concludes.
> 
> 2
> Related Work and Gap Analysis
> 
> 2.1
> W3C Decentralized Identifiers
> 
> 2.2
> OAuth 2.0/2.1
> 
> 2
> 
> Agent identity sits at the intersection of decentralized identity, capability-based authorization, and ser-
> vice mesh security. This section surveys eleven categories of prior work, identifies the specific property
> each fails to provide, and synthesizes the gap that AIP addresses. Table 1 summarizes the analysis
> across seven dimensions.
> 
> W3C Decentralized Identifiers (DIDs) (World Wide Web Consortium, 2026) provide self-sovereign,
> blockchain-anchored identity. DID v1.1 reached Candidate Recommendation in March 2026, yet adop-
> tion remains limited: Block abandoned its “Web5” DID initiative in late 2024 after failing to overcome
> wallet UX friction. For AI agents, wallet UX is irrelevant (agents are software), but the structural

## Block 9: Adaptivity Hits
**Matched Term**: `evasion` | **Location**: `Abstract` [offsets: 1336:1917]
> In a real multi-agent deployment with Gemini 2.5 Flash, AIP adds 2.35 ms of overhead
> (0.086% of total latency). Adversarial evaluation across 600 attack attempts shows 100% rejection,
> with two attack categories (delegation depth violation and audit evasion) uniquely caught by AIP’s
> chained delegation model.
> 
> Sunil Prakash1
> 
> arXiv:2603.24775v1  [cs.CR]  25 Mar 2026
> 
> 1
> Introduction
> 
> MCP and A2A
> 
> 1Indian School of Business, India , sunil_prakash_pgpmax2026@isb.edu
> 
> 1
> 
> AI agents are acquiring the ability to act: calling tools, spending money, and delegating work to other
> agents.
**Matched Term**: `evasion` | **Location**: `Discussion.` [offsets: 41026:42317]
> Wrong key verification
> Token signed by key A, verified against un-
> related key B
> 
> Empty
> context
> (audit
> evasion)
> 
> Delegation with empty context string to
> evade audit trail
> 
> Token forgery
> Base64 token tampered (character flip),
> then verified
> 
> Total (600 attempts)
> 100%
> 0%
> 67%
> 
> 5.5
> Adversarial Security Evaluation (H4)
> 
> 13
> 
> Component
> Mean
> Min
> Max
> 
> AIP create
> 0.385
> 0.146
> 0.934
> AIP delegate
> 0.510
> 0.248
> 0.820
> AIP verify
> 1.455
> 0.650
> 2.340
> 
> LLM orchestrator
> 1,019.886
> 832.813
> 1,293.494
> LLM specialist
> 1,727.052
> 1,557.999
> 1,897.933
> 
> End-to-end total
> 2,749.476
> 2,500.0
> 3,010.7
> 
> AIP as % of total
> 0.086%
> p99: 0.127%
> 
> 100%
> 0%
> 100%
> Chained Datalog checks en-
> force scope at every delega-
> tion hop
> 
> 100%
> 0%
> 0%
> max_depth in authority block
> prevents unbounded delega-
> tion
> 
> 100%
> 0%
> 100%
> Both compact (JWT exp) and
> chained (Datalog time check)
> enforce expiry
> 
> 100%
> 0%
> 100%
> Ed25519 signature binding at
> every layer
> 
> 100%
> 0%
> 0%
> Mandatory non-empty con-
> text on every delegation en-
> forces audit provenance
> 
> 100%
> 0%
> 100%
> Biscuit signature covers every
> block; any tampering is de-
> tected
> 
> for 99.91% of total time. The structural advantage of AIP is clear: because verification is purely lo-
> cal (no authorization server round-trip), protocol overhead scales with cryptographic operations, not
> network latency.
**Matched Term**: `evade` | **Location**: `Discussion.` [offsets: 41108:42317]
> Empty
> context
> (audit
> evasion)
> 
> Delegation with empty context string to
> evade audit trail
> 
> Token forgery
> Base64 token tampered (character flip),
> then verified
> 
> Total (600 attempts)
> 100%
> 0%
> 67%
> 
> 5.5
> Adversarial Security Evaluation (H4)
> 
> 13
> 
> Component
> Mean
> Min
> Max
> 
> AIP create
> 0.385
> 0.146
> 0.934
> AIP delegate
> 0.510
> 0.248
> 0.820
> AIP verify
> 1.455
> 0.650
> 2.340
> 
> LLM orchestrator
> 1,019.886
> 832.813
> 1,293.494
> LLM specialist
> 1,727.052
> 1,557.999
> 1,897.933
> 
> End-to-end total
> 2,749.476
> 2,500.0
> 3,010.7
> 
> AIP as % of total
> 0.086%
> p99: 0.127%
> 
> 100%
> 0%
> 100%
> Chained Datalog checks en-
> force scope at every delega-
> tion hop
> 
> 100%
> 0%
> 0%
> max_depth in authority block
> prevents unbounded delega-
> tion
> 
> 100%
> 0%
> 100%
> Both compact (JWT exp) and
> chained (Datalog time check)
> enforce expiry
> 
> 100%
> 0%
> 100%
> Ed25519 signature binding at
> every layer
> 
> 100%
> 0%
> 0%
> Mandatory non-empty con-
> text on every delegation en-
> forces audit provenance
> 
> 100%
> 0%
> 100%
> Biscuit signature covers every
> block; any tampering is de-
> tected
> 
> for 99.91% of total time. The structural advantage of AIP is clear: because verification is purely lo-
> cal (no authorization server round-trip), protocol overhead scales with cryptographic operations, not
> network latency.
**Matched Term**: `evasion` | **Location**: `Discussion.` [offsets: 42682:43039]
> Unsigned deployments rejected
> 0/600, confirming that without any authentication layer, all attacks succeed. Plain JWT deployments
> caught four of six attack types (scope widening, expired token replay, wrong key verification, and to-
> ken forgery) but missed two: depth violation and empty context audit evasion. These two failures are
> structurally important.
**Matched Term**: `evasion` | **Location**: `Discussion.` [offsets: 43236:43595]
> delegate silently without recording an audit trail. AIP uniquely defends against depth violation and au-
> dit evasion through mandatory delegation context and bounded depth in the authority block, attacks that
> neither unsigned nor JWT-only deployments can detect.
> 
> H1 supported: Compact verification is 0.049 ms (Rust) and 0.189 ms (Python) in microbenchmarks.
**Matched Term**: `evasion` | **Location**: `Discussion.` [offsets: 44261:44516]
> H4 supported: AIP rejected 600/600 adversarial attempts across six attack categories. Plain JWT
> missed two categories (depth violation, empty context audit evasion) that AIP’s chained delegation
> model uniquely detects. Unsigned deployments missed all six.
**Matched Term**: `evasion` | **Location**: `References` [offsets: 51779:52177]
> In a real multi-agent deployment with Gemini 2.5 Flash inference, AIP adds 2.35 ms of overhead
> (0.086% of total latency), confirming that identity verification is not a bottleneck. Adversarial evalu-
> ation across 600 attack attempts shows 100% rejection, with two categories (delegation depth violation
> and audit evasion) uniquely caught by AIP’s chained delegation model.
> 
> Three next steps follow.
