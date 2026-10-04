# Evidence Locator Packet: alfredo-2026-attested-tool-server-admission-security

- **Title**: Attested Tool-Server Admission: A Security Extension to the Model Context Protocol
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2605.24248
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\alfredo-2026-attested-tool-server-admission-security\fulltext.txt
- **Character Count**: 66384

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 3286:3458]
> The component built for that, mcp-attested, generalizes into the
> extension this paper proposes; it ships in both the open enclawed-oss distribution and the enclaved
> flavor.
**Location**: `Abstract` [offsets: 4991:5102]
> This paper documents mcp-attested, the MCP admission layer, and generalizes
> it into a standards-style proposal.

## Block 3: Method Locator
**Section Heading**: `implementation.` [section offsets: 22911:33076]
**First 120 words verbatim** [offsets: 22911:23837]
> implementation.
> 
> verify(serverUrl, required):
> 
> doc
> <- GET serverUrl + "/.well-known/enclawed-clearance.json"
> 
> | on HTTP error or network failure: DENY("fetch failed")
> m
> <- parseManifest(doc)
> 
> DENY("signature verification failed")
> if not meets(m.clearance, required):
> DENY("server level below required")
> if m.netAllowedHosts nonempty and host(serverUrl) not in m.netAllowedHosts:
> 
> 5.1
> The trust root
> 
> 5.2
> Connection gating and flavor semantics
> 
> 8
> 
> The order is security-relevant. Capability and signedness are cheap structural checks; signer
> lookup and the approvedClearance check establish authority (does the trust root let this signer
> vouch for this level?) before the cryptographic verification; the signature check establishes authen-
> ticity; and only then does the level comparison establish sufficiency. A server cannot self-promote:
> 
> even a validly signed assertion is denied if the signing key is not authorized in the
**Section Heading**: `Methodology` [section offsets: 33092:35303]
**First 120 words verbatim** [offsets: 33092:33901]
> Methodology
> 
> capability, and so on — so a test isolates exactly one guard of Property 1.
> 
> 11
> 
> Hermetic, network-observing harness.
> Every test runs against in-memory stubs, never a live
> server. Two seams make this faithful rather than merely convenient: the verifier’s fetcher argument
> supplies the clearance assertion, and the transport’s fetchImpl supplies tool-call responses. The
> transport stub increments a counter on every call, so a denial that nonetheless leaked a network
> write would be caught by an assertion that the counter is zero. A fake runtime installed through
> setRuntime() records every audit append, so the audit vocabulary of Section 5.5 is checked directly
> rather than inferred.
> 
> Faithful positives, single-mutation negatives.
> Trust roots are seeded per test with freshly
> generated Ed25519

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 33076:33092]
**First 120 words verbatim** [offsets: 33076:33883]
> Evaluation
> 
> 7.1
> Methodology
> 
> capability, and so on — so a test isolates exactly one guard of Property 1.
> 
> 11
> 
> Hermetic, network-observing harness.
> Every test runs against in-memory stubs, never a live
> server. Two seams make this faithful rather than merely convenient: the verifier’s fetcher argument
> supplies the clearance assertion, and the transport’s fetchImpl supplies tool-call responses. The
> transport stub increments a counter on every call, so a denial that nonetheless leaked a network
> write would be caught by an assertion that the counter is zero. A fake runtime installed through
> setRuntime() records every audit append, so the audit vocabulary of Section 5.5 is checked directly
> rather than inferred.
> 
> Faithful positives, single-mutation negatives.
> Trust roots are seeded per test with freshly
**Section Heading**: `Results` [section offsets: 35303:52159]
**First 120 words verbatim** [offsets: 35303:36106]
> Results
> 
> Property under test
> Inputs
> Outcome
> 
> Property 1 authenticated, autho-
> rized admission
> 
> 7.3
> Dynamic and live conformance (gated)
> 
> 12
> 
> 2 valid + 12 invalid
> both valid admitted (incl. a host-bound as-
> sertion from its own origin); all 12 denied,
> each at the expected guard (unsigned, not-
> in-root, expired-signer, not-approved, bad-
> signature, below-required, host-not-bound,
> . . . )
> 
> The harness is adversarial in substance.
> Beyond confirming intended denials, the corpus
> surfaced a genuine origin-binding weakness in an earlier verifier — which is why the verifier now
> enforces the signed host allow-list (Property 1(h)). A from-scratch adversarial corpus that forces a
> real fix, rather than only re-confirming the happy path, is the evidence that the suite earns its name.
> 
> Two further harnesses

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
**Location**: `Results` [offsets: 37963:38298]
> This attacker-side campaign is complemented by independent defender-side baselines from the
> 
> --- PAGE BREAK ---
> 
> AlgoVoi Agent-Trust-Bench suite [8], whose differential profiles across 29-tool surfaces confirm that
> unprotected deployments remain uniformly vulnerable to the runtime routing and session exploits
> enumerated in Section 3.
**Location**: `Results` [offsets: 38076:38298]
> AlgoVoi Agent-Trust-Bench suite [8], whose differential profiles across 29-tool surfaces confirm that
> unprotected deployments remain uniformly vulnerable to the runtime routing and session exploits
> enumerated in Section 3.
**Location**: `Results` [offsets: 50561:50684]
> A continuous-monitoring framework requires a
> stable, cryptographically verified anchor to bind its behavioral baselines to.
**Location**: `Results` [offsets: 50781:50900]
> The unforgeable identity string that the runtime monitor uses
> as the primary indexing key for its tool-schema baseline.
**Location**: `Results` [offsets: 51278:51481]
> The downstream monitor anchors each tool baseline to the unique tuple (id, toolName) at the first
> observation post-admission, checking subsequent tools/list or tools/call envelopes against that
> baseline.
**Location**: `Results` [offsets: 51628:51842]
> State isolation: the wire format must
> not carry drift state, baseline histories, or schema-versioning metadata; baseline persistence and
> delta evaluation are strictly implementation concerns of the runtime monitor.

## Block 7: Cost Excerpts
**Location**: `Results` [offsets: 38076:38298]
> AlgoVoi Agent-Trust-Bench suite [8], whose differential profiles across 29-tool surfaces confirm that
> unprotected deployments remain uniformly vulnerable to the runtime routing and session exploits
> enumerated in Section 3.
**Location**: `Results` [offsets: 38715:38775]
> Figure 2: Runtime configuration of the adversarial campaign.
**Location**: `Results` [offsets: 48870:48947]
> 9
> Composition with runtime drift monitoring
> 
> 16
> 
> Bootstrapping the ecosystem.
**Location**: `Results` [offsets: 50403:50501]
> This operational boundary is where a downstream runtime drift-monitoring layer
> composes with ATSA.
**Location**: `Results` [offsets: 50781:50900]
> The unforgeable identity string that the runtime monitor uses
> as the primary indexing key for its tool-schema baseline.
**Location**: `Results` [offsets: 51058:51184]
> The cryptographic guarantee that the entity producing
> tool definitions at execution time matches the entity that was admitted.

## Block 8: Limitations
**Section Heading**: `Limitations and future work` [section offsets: 55128:62577]
**First 120 words verbatim** [offsets: 55128:55908]
> Limitations and future work
> 
> 12
> Conclusions
> 
> 18
> 
> MCP left trust to the deployment, and that gap is exploitable everywhere — a prompt-injected
> model can drive a destructive tool on any server it reaches. A lone operator may absorb that risk;
> a regulated one cannot, and without an admission record cannot even audit it. We showed the
> missing trust layer can be added entirely above MCP, without changing a single message, and backed
> each guarantee (authenticated admission, tool least-privilege, auditability, tamper-resistance) with
> crafted and LLM-generated adversarial tests.
> 
> Why this belongs in the MCP specification, not in N vendor forks.
> Several forces argue
> for standardizing admission at the spec level rather than leaving it to each deployment:
> 
> • Trust does not compose

## Block 9: Adaptivity Hits
**Matched Term**: `evasion` | **Location**: `Abstract` [offsets: 6373:6884]
> 4. An adversarial evaluation (Section 7): we turn each stated property into an executable test
> driven by an LLM-generated red-team corpus (tool-name evasions and forged clearance assertions)
> and report the results — every evasion denied with zero leaked network writes and every forgery
> 
> --- PAGE BREAK ---
> 
> Figure 1: MCP today (a) versus the proposed attested tool-server admission (b). The extension
> adds a host-side gate and one server-published document; an unextended host ignores it and behaves
> as in (a).
**Matched Term**: `evasion` | **Location**: `Results` [offsets: 40736:41242]
> Tool-name evasion category
> unique
> denied
> admitted
> 
> unclassified / other
> 12,106
> 12,106
> 0
> whitespace / control char
> 9,012
> 9,012
> 0
> separator / command chaining
> 3,469
> 3,469
> 0
> near-miss (edit dist. ≤2)
> 1,251
> 1,251
> 0
> path-traversal
> 752
> 752
> 0
> homoglyph / zero-width / RTL
> 393
> 393
> 0
> case-variant of an allow name
> 42
> 42
> 0
> 
> Total (47,945 generated)
> 27,025
> 27,025
> 0
> 
> Network writes on denied calls: 0
> Forged assertions: 14,378 unique, 14,378 denied, 0 admitted
> 
> If it already works above MCP, why change the standard?
