# Evidence Locator Packet: panduranga-2026-delegation-trust-empirical-gap-analysis

- **Title**: Delegation Without Trust: An Empirical Gap Analysis of Identity, Authorization, and Runtime Governance in Multi-Agent LLM Systems
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_secondary
- **Link**: https://arxiv.org/abs/2609.00267
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\panduranga-2026-delegation-trust-empirical-gap-analysis\fulltext.txt
- **Character Count**: 40802

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 1310:1735]
> Second, we show the gap is real: a default agent runtime
> modeling common framework practice (broad bearer credentials, authorization gated inside the
> model) fails all four threats, and across four widely used frameworks – LangGraph, CrewAI,
> AutoGen, and the Model Context Protocol (MCP) authorization model – three provide no
> built-in confinement and one only partial; no existing standard, alone, covers the requirement
> set.
**Location**: `Abstract` [offsets: 4756:4777]
> Our contributions:
> 
> 2

## Block 3: Method Locator
**Section Heading**: `Implementation` [section offsets: 15538:17651]
**First 120 words verbatim** [offsets: 15538:16314]
> Implementation
> 
> Standard / primitive
> R1
> R2
> R3
> R4
> R5
> R6
> R7
> R8
> 
> 6
> 
> deployment property none of them mandates. Second, and more importantly, the primitives have
> not been composed for the agent-to-agent case: there is today no standard profile that mints, at each
> delegation hop, a capability token that is simultaneously attenuated (R2), bound to the sub-agent’s
> workload identity (R3), short-lived (R4), and enforced at a PEP outside the model (R8). Closing
> that composition is the subject of Section 7.
> 
> 7
> The Broker: Design, Implementation, and Evaluation
> 
> We compose the primitives into an authorization broker / PEP that sits between agents and tools,
> 
> and we implement and adversarially evaluate it. The broker realizes the untrusted-model property
> by construction: a fully
**Section Heading**: `Architecture.` [section offsets: 21560:24662]
**First 120 words verbatim** [offsets: 21560:22417]
> Architecture.
> Client, RAG, MCP, and agentic applications connect through a single AI Gateway
> that provides authentication, authorization, routing, rate limiting, and observability, and embeds
> an MCP gateway (built on components such as Kong, LiteLLM, and Portkey). Agent identity is
> issued and validated by the VotalAI Agent IDP, which federates with enterprise identity providers
> (Okta, Auth0, Microsoft Entra, Google) and offers OIDC, SSO, MFA, attribute-based access control
> (ABAC), and a policy enforcement point; agents authenticate to tools and MCP servers using
> 
> IDP-issued tokens. Requests traverse guardrail model services containing pre-call and post-call
> content inspection and — central to this paper — an Agent & Tool Access Control stage performing
> role-based tool authorization and per-agent permission enforcement. A Redis tier caches tenant

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 17651:21560]
**First 120 words verbatim** [offsets: 17651:18418]
> Evaluation
> 
> We evaluate along four axes; all numbers are from our reference implementation.
> 
> 5. verify + enforce
> allow / deny
> 
> Tool / MCP server
> 
> 3. delegate
> 4. tool call (cap2, SVID2)
> 
> T1 confused deputy
> succeeds
> blocked
> T2 token theft / replay
> succeeds
> blocked
> T3 privilege escalation
> succeeds
> blocked
> T4 compromised sub-agent
> succeeds
> blocked
> 
> 7
> 
> Figure 1: Data flow through the broker. A human’s OIDC identity roots a capability token; each
> delegation hop is an issuer-mediated token exchange that mints an attenuated (cap2 ⊆cap1),
> SVID-bound, short-lived token. Every tool call is routed through the broker, which verifies the
> token and enforces its caveats outside the model (R8) before allowing the call. Agents run in an
> untrusted zone; a fully hijacked agent

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 18467:18502]
> Table 4: Attack outcome by runtime.
**Location**: `Evaluation` [offsets: 18503:18561]
> The broker blocks every threat the default runtime admits.
**Location**: `Evaluation` [offsets: 18797:18877]
> The default runtime of Section 5 and the broker share a common
> scenario harness.
**Location**: `Evaluation` [offsets: 18902:19008]
> Against the four adversaries, the default runtime fails all four and the
> broker blocks all four (Table 4).
**Location**: `Evaluation` [offsets: 20416:20425]
> Overhead.
**Location**: `Evaluation` [offsets: 20567:20681]
> Against model inference measured
> in hundreds of milliseconds to seconds, the governance layer is effectively free.

## Block 8: Limitations
**Section Heading**: `Threats to Validity` [section offsets: 24730:27894]
**First 120 words verbatim** [offsets: 24730:25560]
> Threats to Validity
> 
> 9
> 
> Continuous red-teaming.
> Shield includes an attack zone / red-teaming portal that continuously
> probes protected endpoints, synthesizing adversarial prompts on the fly in single-turn, multi-turn,
> and combined modes from a catalog of over 100 manipulation strategies — an operational analogue
> of the adversarial evaluation in Section 7.
> 
> Why model-side guardrails are not enough.
> Input/output content filters reduce the rate
> of successful injection but cannot provide R1–R8; they are probabilistic and sit inside the trust
> boundary we assume broken. Governance must be enforced by authority scoping outside the model,
> which content filtering complements but cannot replace.
> 
> Deployment cost.
> The broker adds a mediation point on the tool-call path and a per-hop token
> exchange. As Section 7 shows, enforcement

## Block 9: Adaptivity Hits
no hits
