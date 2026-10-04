# Evidence Locator Packet: zhiyang-2026-acle-mcp-attested-capability-leases

- **Title**: ACLE-MCP: Attested Capability Leases for Execution-Time Trust in Remote LLM Tool Use
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2609.02690
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\zhiyang-2026-acle-mcp-attested-capability-leases\fulltext.txt
- **Character Count**: 41305

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 832:985]
> We present ACLE-MCP, an invocation-scoped architec-
> ture that couples delegated authorization, workload appraisal,
> and resource-side execution admission.

## Block 3: Method Locator
**Section Heading**: `Methodology` [section offsets: 14194:17742]
**First 120 words verbatim** [offsets: 14194:14990]
> Methodology
> Design Overview
> Figure
> 1
> shows
> how
> ACLE-MCP
> closes
> the
> post-
> authorization execution trust gap. The Host Orchestrator first
> normalizes the selected structured call and compiles the in-
> vocation boundary It. Low-risk calls may remain on the ordi-
> nary OAuth path when both Host and Provider policies per-
> mit. Medium- and high-risk calls trigger Attested Step-Up.
> The Verifier appraises the provider-side workload expected
> to serve the call, and the lease issuer combines the signed ap-
> praisal result, verified OAuth context, sender identity, and It
> into a short-lived capability lease. The provider-side Execu-
> tion Gate validates and consumes the lease before protected
> tool logic begins; only after all checks pass may the applica-
> tion workload execute the call.
> 
> The placement of

## Block 4: Evaluation Locator
**Section Heading**: `results indicate that invocation-time binding between call au-` [section offsets: 1906:2067]
**First 120 words verbatim** [offsets: 1906:2716]
> results indicate that invocation-time binding between call au-
> thority and current workload state is a practical complement
> to OAuth-protected remote tool use.
> 
> Introduction
> 
> Large language model (LLM) applications increasingly in-
> voke external tools, data sources, and enterprise services
> through the Model Context Protocol (MCP). This shift
> from passive text generation to agentic execution allows a
> Host to retrieve private data, update records, invoke inter-
> nal APIs, and trigger external workflows. In remote deploy-
> ments, OAuth can authorize an MCP Client to access a pro-
> tected MCP Server. OAuth answers an important question—
> whether a client or user may access a resource—but it does
> not establish that the concrete provider-side workload exe-
> cuting a later invocation is still the execution unit
**Section Heading**: `evaluation covers replay, workload substitution, stale ap-` [section offsets: 6872:11717]
**First 120 words verbatim** [offsets: 6872:7662]
> evaluation covers replay, workload substitution, stale ap-
> praisal, scope misuse, undeclared proxying, and receipt
> violations, and extends the analysis to chained and stream-
> ing agent tool-use scenarios without redefining the core
> security problem.
> 
> Security Problem
> Post-Authorization Execution Trust Gap
> For an invocation at time t, let the Host-authorized invocation
> boundary be
> 
> It = ⟨aud, tool, op, obj, Θ, D, B, ρ⟩,
> (1)
> 
> where aud is the intended audience; tool, op, and obj iden-
> tify the tool, operation class, and object scope; Θ specifies
> parameter constraints; D is the approved downstream set; B
> is the side-effect budget; and ρ is the minimum workload-
> assurance policy.
> 
> Let the corresponding provider-side execution observation
> be
> 
> Et = ⟨wid, aud′, tool′, op′, obj′, θ′, D′,
**Section Heading**: `Evaluation` [section offsets: 20816:26175]
**First 120 words verbatim** [offsets: 20816:21713]
> Evaluation
> 
> We evaluate three questions: RQ1: Does invocation-time
> workload binding close the modeled post-authorization trust
> gap while preserving benign tool calls? RQ2: Which mech-
> anisms account for the observed security gains? RQ3: What
> integration cost and runtime overhead does the prototype
> introduce?
> 
> Experimental Setup
> 
> We implement separate Python services for the Verifier, lease
> issuer, Execution Gate, MCP tool service, and adversarial
> workloads, with components communicating over HTTP.
> The main controlled experiments use simulated OAuth, work-
> load appraisal, and sender proof to isolate lease issuance and
> resource-side execution logic. The Verifier produces signed
> appraisal results from evidence, freshness, and Provider pol-
> icy; the lease issuer validates the OAuth context, invocation
> boundary, and appraisal result before issuing a signed, short-
> lived, sender-constrained
**Section Heading**: `results in RQ2 identify the checks required to close these` [section offsets: 26175:32229]
**First 120 words verbatim** [offsets: 26175:27004]
> results in RQ2 identify the checks required to close these
> attacks.
> 
> Table 1 reports the agent tool-use extension. All five modes
> allow every benign task and therefore have a false-positive
> rate of zero in this diagnostic suite. OAuth-only and Attest-
> on-connect block none of the six execution-misuse families.
> Stateful LP blocks five families but misses streaming seman-
> tic mutation because it lacks fresh workload and invocation-
> state binding. Capability-only blocks four families but misses
> tool-chain step injection and streaming semantic mutation.
> Full ACLE-MCP blocks every evaluated scenario in every
> repetition and has a false-negative rate of zero. These scenar-
> ios broaden the evaluation context without changing the pa-
> per’s central claim about post-authorization workload trust.
> 
> In the current local simulation,

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
**Location**: `results in RQ2 identify the checks required to close these` [offsets: 27639:27843]
> RQ2: Ablation Study and Mechanism Attribution
> 
> We repeat the complete ACLE-MCP configuration and its
> component-removal variants over the same 24 scenarios, 10
> random seeds, and single-concurrency setting.
**Location**: `results in RQ2 identify the checks required to close these` [offsets: 28524:28730]
> The configuration without Attested Step-Up also disables
> workload-binding checks and should therefore be interpreted
> as a joint ablation of these two mechanisms rather than as
> removal of the Verifier alone.
**Location**: `results in RQ2 identify the checks required to close these` [offsets: 29276:29515]
> The main ablation uses single concurrency;
> although disabling single-flight leaves security unchanged,
> this setting does not actually exercise concurrent-request co-
> alescing, so we do not quantify the performance benefit of
> single-flight.
**Location**: `results in RQ2 identify the checks required to close these` [offsets: 31339:31512]
> Full ACLE-MCP has a request-level pooled p95 of 15.34 ms
> for normal allowed requests in the agent suite, compared with
> 12.20 ms for OAuth-only, a relative increase of 25.7%.

## Block 7: Cost Excerpts
**Location**: `evaluation covers replay, workload substitution, stale ap-` [offsets: 7795:8006]
> OAuth authorization establishes only that the client may ac-
> cess aud; it does not imply that wid is the expected workload,
> that s satisfies ρ, or that the appraisal remains sufficiently
> fresh at execution time.
**Location**: `Evaluation` [offsets: 20828:20982]
> We evaluate three questions: RQ1: Does invocation-time
> workload binding close the modeled post-authorization trust
> gap while preserving benign tool calls?
**Location**: `Evaluation` [offsets: 21048:21125]
> RQ3: What
> integration cost and runtime overhead does the prototype
> introduce?
**Location**: `Evaluation` [offsets: 21871:22011]
> The harness records request-level decisions, randomized sce-
> nario order, environment manifests, stage-level latency, and
> security outcomes.
**Location**: `Evaluation` [offsets: 24157:24338]
> The agent tool-use extension contains four benign task
> families: filesystem summarization, GitHub issue comment-
> ing, bounded database reporting, and Kubernetes status in-
> spection.
**Location**: `Evaluation` [offsets: 24673:24799]
> We report
> benign-task success, attack-blocking rate, false-positive and
> 
> Table 1: Agent tool-use results over ten repetitions.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
