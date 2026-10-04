# Evidence Locator Packet: huan-2026-zero-trust-authorization-discovery-enterprise

- **Title**: Zero-Trust Authorization and Discovery for Enterprise MCP
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2609.22573
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\huan-2026-zero-trust-authorization-discovery-enterprise\fulltext.txt
- **Character Count**: 70134

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 104:1018]
> Abstract
> 
> LLM agents translate natural-language context, which may include
> attacker-controlled text, into privileged tool calls, so authorization
> must remain effective even when an agent is prompt-injected or
> otherwise adversarially steered. The Model Context Protocol (MCP)
> has become a widely adopted interface for this boundary, yet the
> authentication and authorization primitives in its official SDKs
> fall short of enterprise zero-trust requirements—most acutely the
> dual-persona model, in which one server must serve human users
> (corporate SSO) and automated agents (service-account credentials
> in a different header) at once. We conduct a systematic gap analysis
> of six surveyed MCP SDKs (Python, TypeScript, Go, Rust, C#, Swift)
> and identify three structural shortcomings: Authorization-header-
> bound credential extraction that makes dual-persona deployment
> difficult without replacing SDK-level middleware,

## Block 3: Method Locator
**Section Heading**: `Architecture and Design` [section offsets: 18974:30566]
**First 120 words verbatim** [offsets: 18974:19843]
> Architecture and Design
> 3.1
> Design Principles
> 
> We operate at native framework extension points only (Starlette
> HTTP middleware, FastMCP application middleware, FastMCP cus-
> tom_route for the pre-auth metadata route, and Python function
> decorators) with no monkey-patching, no private-API access, and
> no modification to the MCP protocol or FastMCP core. Authentica-
> tion composition uses OR logic at the middleware level so a server
> can accept any of several credential types (the same mechanism
> also composes with AND, requiring multiple credentials at once
> for high-assurance deployments). A dedicated pre-authentication
> endpoint resolves the registry bootstrap problem; we treat schema
> exposure as an explicit design tradeoff, with execution capability
> gated behind the authenticated MCP path. The permission decora-
> tor preserves the wrapped function’s signature via
**Section Heading**: `architecture: (i) the baseline attempt distribution that an LLM-only` [section offsets: 35075:36069]
**First 120 words verbatim** [offsets: 35075:35844]
> architecture: (i) the baseline attempt distribution that an LLM-only
> (refusal-trained) deployment is actually exposed to under prompt
> injection on the same scope set, (ii) how that distribution varies
> across vendor and model family on identical inputs, and (iii) the
> leak rate at which LLMs still mention the forbidden tool name even
> when it is absent from their schema, which sets the size of the
> side-channel surface the decorator must close (Section 4.3.4). We do
> not benchmark model robustness against prompt injection; existing
> benchmarks [9, 40] do that on far larger corpora.
> 
> To evaluate G1 empirically, we measure whether an LLM agent
> operating under viewer-only credentials can be induced (through
> prompt injection) to (a) attempt to call a forbidden tool and
**Section Heading**: `Methodology. The corpus is 60 LLM-assisted, hand-reviewed` [section offsets: 38362:40413]
**First 120 words verbatim** [offsets: 38362:39305]
> Methodology. The corpus is 60 LLM-assisted, hand-reviewed
> prompt-injection payloads, 15 per class (direct injection, indirect
> injection, role-play bypass, context overflow); each class exercises
> distinct social-engineering hooks (authority, urgency, fake policy,
> chain-of-thought hijack, tool-output poisoning, identity swap, simu-
> lation framing, runbook tail). We sweep four frontier LLMs through
> an OpenAI-compatible enterprise gateway: gpt-5, claude-sonnet-
> 4-6, claude-opus-4-7, gemini-2.5-pro. For each (model, prompt)
> pair we run three attempts with seeds {42, 43, 44}; for non-reasoning-
> class models temperature varies across {0.0, 0.3, 0.7}, and reasoning-
> class models (gpt-5, claude-opus-4-7) use the gateway’s default
> 
> 7
> 
> sampling (user-controllable temperature is unsupported). The sys-
> tem prompt is intentionally minimal so defenses come from archi-
> tecture, not refusal instructions. The full grid is 4×3×60×3 = 2160
> attempts,

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 30566:35075]
**First 120 words verbatim** [offsets: 30566:31532]
> Evaluation
> 4.1
> Comparison and Zero-Trust Mapping
> 
> Against FastMCP, our extensions fill five capability gaps: middleware-
> level heterogeneous auth-backend pluggability (vs. FastMCP’s verify-
> only TokenVerifier and provider-level MultiAuth); verifying opaque
> tokens against vendors that lack an RFC-7662 endpoint (e.g., GitHub,
> GCP), with scope mapping (vs. FastMCP’s RFC-7662-only Intro-
> spectionTokenVerifier); pre-auth tool/prompt/resource discov-
> ery (vs. OAuth-metadata-only); component filtering for tools, prompts,
> and resources; and declarative AND/OR per-tool authorization pre-
> serving function signatures. The extensions map to NIST SP 800-
> 207 tenets: C1+C2 instantiate “never trust, always verify” at the
> credential-ingress and verification layers (C2 within a bounded
> cache window for continuous verification); C3 reflects “assume
> breach” by exposing schemas without invocation; C4 enforces least-
> privilege access at the granularity of individual tools.
**Section Heading**: `architecture: (i) the baseline attempt distribution that an LLM-only` [section offsets: 35075:36069]
**First 120 words verbatim** [offsets: 35075:35844]
> architecture: (i) the baseline attempt distribution that an LLM-only
> (refusal-trained) deployment is actually exposed to under prompt
> injection on the same scope set, (ii) how that distribution varies
> across vendor and model family on identical inputs, and (iii) the
> leak rate at which LLMs still mention the forbidden tool name even
> when it is absent from their schema, which sets the size of the
> side-channel surface the decorator must close (Section 4.3.4). We do
> not benchmark model robustness against prompt injection; existing
> benchmarks [9, 40] do that on far larger corpora.
> 
> To evaluate G1 empirically, we measure whether an LLM agent
> operating under viewer-only credentials can be induced (through
> prompt injection) to (a) attempt to call a forbidden tool and
**Section Heading**: `Results. Table 4 reports per-(model, attack-class) attempt counts` [section offsets: 40413:42550]
**First 120 words verbatim** [offsets: 40413:41204]
> Results. Table 4 reports per-(model, attack-class) attempt counts
> under baseline (45 per cell) and the aggregate filter-only / with-
> extensions columns. Wilson 95% intervals [38]: 152/720 (21.1%,
> 
> [18.3, 24.2]) under baseline; 0/720 ([0, 0.5]) under both filter-only
> and with-extensions, which follow the structural argument above.
> The informative part of the table is the baseline column: with no
> C4 and the forbidden tool still visible to the agent, it measures how
> exposed an alignment-only deployment is to prompt injection.
> 
> Two non-structural findings emerge.
> (i) Models do not suppress a forbidden tool name the prompt lets
> them infer. A leak flag records whether the LLM mentioned the for-
> bidden tool name anywhere in its response; 59/60 payloads make
> restart_pod inferable from the

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 32896:33271]
> Both this benchmark and the ad-
> versarial evaluation (Section 4.3) run against a common testbed:
> MCP servers registering eight mock Kubernetes tools, split into four
> viewer-permissioned (e.g., get_metrics) and four admin-permissioned
> (e.g., restart_pod) operations, with a stub TokenVerifier that
> issues a fixed viewer scope on any non-empty bearer token (no
> IdP round-trip).
**Location**: `Evaluation` [offsets: 33272:33481]
> To isolate the SDK’s own cost, we ran a micro-
> benchmark: 1000 requests per (configuration, operation) per round,
> median over three rounds, after 50 warm-ups, across four cumula-
> tive configurations (Table 2).
**Location**: `architecture: (i) the baseline attempt distribution that an LLM-only` [offsets: 35536:35657]
> We do
> not benchmark model robustness against prompt injection; existing
> benchmarks [9, 40] do that on far larger corpora.

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 33482:33606]
> The +auth row uses FastMCP’s own
> RemoteAuthProvider (not our contribution), so we take it as the
> baseline for our additions.
**Location**: `Evaluation` [offsets: 34070:34329]
> vanilla MCP
> 1.71
> 1.98
> 2.15
> 2.41
> +auth
> 1.78
> 2.07
> 2.18
> 2.58
> +auth+filter
> 1.70
> 2.08
> 2.21
> 2.59
> +auth+filter+decorator
> 1.67
> 1.92
> 2.18
> 2.49
> 
> 4.3
> Adversarial Evaluation
> 
> This subsection demonstrates how the contributions defend the
> threats enumerated in Section 2.4.
**Location**: `Evaluation` [offsets: 34463:34603]
> The G1 entry shows the
> baseline→with-extensions attempt rate (4 LLMs, 2160 attempts;
> details in Section 4.3.1); succeeded = 0 in every cell.
**Location**: `architecture: (i) the baseline attempt distribution that an LLM-only` [offsets: 35075:35535]
> architecture: (i) the baseline attempt distribution that an LLM-only
> (refusal-trained) deployment is actually exposed to under prompt
> injection on the same scope set, (ii) how that distribution varies
> across vendor and model family on identical inputs, and (iii) the
> leak rate at which LLMs still mention the forbidden tool name even
> when it is absent from their schema, which sets the size of the
> side-channel surface the decorator must close (Section 4.3.4).
**Location**: `Results. Table 4 reports per-(model, attack-class) attempt counts` [offsets: 40422:40565]
> Table 4 reports per-(model, attack-class) attempt counts
> under baseline (45 per cell) and the aggregate filter-only / with-
> extensions columns.
**Location**: `Results. Table 4 reports per-(model, attack-class) attempt counts` [offsets: 40610:40744]
> [18.3, 24.2]) under baseline; 0/720 ([0, 0.5]) under both filter-only
> and with-extensions, which follow the structural argument above.

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 31922:32202]
> In a 7-day production trace, the C2 introspection cache served
> 96.1% of verification requests from local memory at 9.9 ms p50, ver-
> sus 296 ms p50 on miss—a ∼30× p50 speedup bounding IdP load to
> one introspection per (token, TTL-window) pair (staleness tradeoff
> in Section 4.3.3).
**Location**: `Evaluation` [offsets: 32203:32821]
> Qualitatively, pre-auth metadata replaced hand-
> maintained YAML manifests that drifted from live servers; compo-
> nent filtering eliminated the PermissionError/wasted-LLM-cycle
> class—hiding unauthorized tools stops the agent from spending
> calls on operations it cannot perform and from forming a mistaken
> view of its own capabilities, and as a side benefit trims the tool
> schemas loaded into its context, cutting input tokens and thus per-
> call cost and latency; and dual-persona authentication lets a single
> server serve both human and automation callers, instead of running
> a separate server for each credential type.
**Location**: `Evaluation` [offsets: 32870:32895]
> Framework-layer overhead.
**Location**: `Evaluation` [offsets: 33607:33959]
> On top of it, our permission filter and
> per-tool decorator add ∼0 ms at p50 and ≤∼0.15 ms at p95—on the
> order of the run-to-run noise across rounds—so the overhead of our
> extensions is negligible; list_tools is even marginally cheaper
> once filtering is on, since a viewer receives four tools instead of
> eight and the smaller response serializes faster.
**Location**: `Evaluation` [offsets: 33961:34015]
> Table 2: SDK framework-layer per-request latency (ms).

## Block 8: Limitations
**Section Heading**: `Limitations and Deployment Notes` [section offsets: 49287:51512]
**First 120 words verbatim** [offsets: 49287:50149]
> Limitations and Deployment Notes
> 
> Corpus scope. We evaluate 60 hand-reviewed prompt-injection
> payloads against one forbidden tool (Section 4.3.1) and do not claim
> coverage of the broader attack space. The 0/720 result under filter-
> only and with-extensions is structural, not a claim about this corpus
> specifically: visibility filtering removes the tool from the model’s
> schema, and invocation-time authorization blocks any direct call
> regardless of phrasing, so neither would change with a larger cor-
> pus. What the corpus does characterize empirically is model-side
> behavior on the corpus itself—the baseline attempt-rate variation
> across vendors and the name-disclosure leak rate—which is where
> coverage claims would matter. Obfuscation and encoding attacks
> are left to dedicated robustness benchmarks [9, 40].
> 
> Default visibility for undeclared components. A

## Block 9: Adaptivity Hits
no hits
