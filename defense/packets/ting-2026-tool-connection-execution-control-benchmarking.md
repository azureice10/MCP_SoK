# Evidence Locator Packet: ting-2026-tool-connection-execution-control-benchmarking

- **Title**: From Tool Connection to Execution Control: Benchmarking Security Invariants in MCP-Style Agent Runtimes
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2606.29073
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\ting-2026-tool-connection-execution-control-benchmarking\fulltext.txt
- **Character Count**: 58968

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 2797:2874]
> These pieces matter, and
> this paper does not argue that MCP ignores security.
**Location**: `Abstract` [offsets: 4362:4421]
> This paper frames that gap as an execution-control problem.
**Location**: `Abstract` [offsets: 6766:6801]
> The paper makes four contributions.

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 29059:48442]
**First 120 words verbatim** [offsets: 29059:29924]
> Evaluation
> 
> 7.1
> Security Outcomes
> 
> Table 4 summarizes the 10 security benchmark cases.
> 
> warning only; attack
> succeeds
> 
> INSUFFICIENT SCOPE
> with audit
> 
> warning only; attack
> succeeds
> 
> INSUFFICIENT SCOPE
> with audit
> 
> server identity check blocks RESOURCE DENIED with
> 
> audit
> 
> server identity check blocks RESOURCE DENIED with
> 
> audit
> 
> prompt present; attack
> succeeds
> 
> MISSING GRANT; grant
> without approval waits
> 
> prompt present; attack
> succeeds
> 
> warning only; attack
> succeeds
> 
> target data-class denial with
> audit
> 
> warning only; attack
> succeeds
> 
> HANDLE ACCESS
> DENIED with audit
> 
> manual checks block
> INITIALIZATION
> REQUIRED or version
> denial
> 
> 8
> 
> Each case records three primary fields per mode: attack success, blocked outcome, and audit completeness. An
> attack succeeds when the modeled unsafe effect completes or when a protocol method crosses a state boundary that
> should

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 29094:29145]
> Table 4 summarizes the 10 security benchmark cases.
**Location**: `Evaluation` [offsets: 30462:30535]
> The benchmark therefore treats prevention and evidence as two dimensions.
**Location**: `Evaluation` [offsets: 30943:31093]
> The paper-data linkage is therefore defined by the case fixtures, benchmark outputs, and generated tables
> rather than by hand-edited aggregate counts.
**Location**: `Evaluation` [offsets: 31373:31524]
> The benchmark runner emits JSON results, and the table generator derives the paper tables from the
> current JSON outputs rather than hand-edited counts.
**Location**: `Evaluation` [offsets: 31525:31625]
> The relevant artifact commands are run-benchmark.mjs,
> validate-results.mjs, and generate-tables.mjs.
**Location**: `Evaluation` [offsets: 31647:31697]
> Table 4: Security outcomes across benchmark modes.

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 32259:32300]
> Table 5: Counterfactual ablation results.
**Location**: `Evaluation` [offsets: 32517:32597]
> 7.2
> Ablation
> 
> 9
> 
> This is not intended to estimate real-world exploit prevalence.
**Location**: `Evaluation` [offsets: 32713:32883]
> The value of the result is therefore not that HCP
> blocks all possible attacks, but that each claimed invariant is executable, testable, and fails under targeted ablation.
**Location**: `Evaluation` [offsets: 34557:34660]
> The counterfactual ablation study disables one enforcement component at a time over benchmark outcomes.
**Location**: `Evaluation` [offsets: 35026:35078]
> Table 5 reports the counterfactual ablation results.
**Location**: `Evaluation` [offsets: 35080:35204]
> The instrumented ablation harness gives executable evidence for the same design claims without modifying the
> runtime source.

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 30265:30377]
> A runtime can block a bad call by raising an exception,
> but that does not by itself establish forensic evidence.
**Location**: `Evaluation` [offsets: 32598:32712]
> The benchmark is an invariant-coverage bench-
> mark: each case is constructed to cross a specific runtime boundary.
**Location**: `Evaluation` [offsets: 33097:33280]
> This distribution is
> the intended diagnostic: connection-layer mitigations help with identity and session state, while grant, handle, and
> data-pipe boundaries require runtime objects.
**Location**: `Evaluation` [offsets: 33702:33855]
> B2 reaches the same prevention
> result through runtime resource matching, which avoids relying on every provider to implement the same check
> consistently.
**Location**: `Evaluation` [offsets: 35080:35204]
> The instrumented ablation harness gives executable evidence for the same design claims without modifying the
> runtime source.
**Location**: `Evaluation` [offsets: 35985:36133]
> These harness variants are not supported runtime configurations; they are controlled experiments
> used to isolate the contribution of each mechanism.

## Block 8: Limitations
**Section Heading**: `Limitations` [section offsets: 48456:52554]
**First 120 words verbatim** [offsets: 48456:49348]
> Limitations
> 
> 13
> 
> A central limitation is that the evaluated runtime is in-memory. Grants, audit entries, registry records, and handles are
> not durable in the evaluated prototype. Provider attestation, sandbox isolation, cryptographic signing, and persistent
> policy stores are outside the evaluated scope. These omissions are deliberate so that the paper can isolate execution-
> control invariants before evaluating production platform machinery.
> 
> Moving from the evaluated prototype to a deployment-grade system would require several additional mecha-
> nisms. Grants and audit records would need durable storage and retention policy. Provider manifests would need a
> trust model, signature verification, or other attestation workflow. Shell, browser, network, and filesystem providers
> would need sandboxing appropriate to their risk. The runtime would also need administrative access control for

## Block 9: Adaptivity Hits
no hits
