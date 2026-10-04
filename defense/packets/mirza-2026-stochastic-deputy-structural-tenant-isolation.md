# Evidence Locator Packet: mirza-2026-stochastic-deputy-structural-tenant-isolation

- **Title**: The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2609.14780
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\mirza-2026-stochastic-deputy-structural-tenant-isolation\fulltext.txt
- **Character Count**: 104693

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 1776:2514]
> Abstract
> 
> 1 Introduction
> 
> A
> multi-tenant
> service
> must
> ensure
> that
> a
> request issued on behalf of one tenant cannot
> read another tenant’s data. The overwhelmingly
> common implementation of this guarantee is
> parameter-mediated: the caller names the tenant
> it is acting for, the service validates that the caller
> is entitled to that tenant, and a filter is applied.
> The pattern is so routine that it is usually invis-
> ible. A tenant-specific request carries the caller’s
> resource selection in a request parameter.
> 
> 1
> 
> This works because of an assumption that is
> rarely stated. The caller is a deterministic pro-
> gram, its behaviour is fixed by its source code,
> and an adversary who wishes to change which
> tenant it names must first change that

## Block 3: Method Locator
**Section Heading**: `2. Structural design and argument. We give` [section offsets: 7716:7904]
**First 120 words verbatim** [offsets: 7716:8537]
> 2. Structural design and argument. We give
> five invariants and two enforcement points,
> then state the assumptions and failure modes
> of the resulting security argument (Sections 4
> to 4.6).
> 3. Database
> results. We identify transitive
> scope closure as a necessary invariant and show
> that set-valued scope can defeat index access.
> A lateral join restores indexed lookup when
> the tenant key is indexed; the deployed alter-
> native exhibits an entitlement-size planner cliff
> (Sections 5 to 6).
> 4. An interface ablation across eight model
> configurations and two transports. A 373-
> trial, three-arm experiment isolates the tool
> signature, measures both plausible and injected
> requests, and reveals a bypass when agents can
> rewrite scope (Section 8.8).
> 5. Production-scale
> evaluation.
> Structural,
> performance, and fail-closed tests
**Section Heading**: `4 Design` [section offsets: 14643:17020]
**First 120 words verbatim** [offsets: 14643:15392]
> 4 Design
> 
> The architecture rests on five invariants. We state
> each as a property of the system rather than
> a component, because the point is what cannot
> happen, not what is present.
> 
> 4
> 
> --- PAGE BREAK ---
> 
> Fig. 1 Trust-boundary map. Attacker-reachable content can influence the agent, but must not determine the verified scope.
> Dashed separation marks the intended boundary, not a guarantee against capabilities that bypass it.
> 
> Table 1 Attack vectors and the invariant that addresses
> each. “Enforced at” names the layer that must fail for the
> attack to succeed.
> 
> Vector
> Description
> Enforced
> at
> 
> V1:
> Argument
> steering
> 
> Agent emits a tenant id it is
> not entitled to
> 
> Interface
> (I1): no
> such
> argument
> 
> V2:
> Header
> injection
> 
> Client
> asserts
> identity
> via
**Section Heading**: `implementation, such that a tool cannot emit a` [section offsets: 20232:20888]
**First 120 words verbatim** [offsets: 20232:21006]
> implementation, such that a tool cannot emit a
> query lacking it.
> 
> 6
> 
> --- PAGE BREAK ---
> 
> Application-layer filtering distributed across
> tools fails by omission. With n tools over m
> tenant-scoped tables there are O(nm) sites at
> which a predicate can be forgotten, each omis-
> sion produces a silent cross-tenant read, and none
> produces an error.
> 
> Where the predicate should instead live is not
> a single answer but a choice constrained by how
> much authority one has over the database. We
> characterize two points, because reporting only
> the stronger one, as the enforcement-relocation lit-
> erature tends to, misrepresents what most teams
> can actually deploy.
> 
> 4.3.1 Point A: engine-enforced
> (definer-rights views)
> 
> The application account is granted SELECT on a
> set of generated
**Section Heading**: `implementation refuses to start unless the oper-` [section offsets: 23960:24145]
**First 120 words verbatim** [offsets: 23960:24704]
> implementation refuses to start unless the oper-
> ator names one explicitly. There is no default.
> A default would be a security decision made by
> whoever wrote the configuration parser.
> 
> 4.4 I4: Transitive scope closure
> 
> Property 4 (Transitive closure). Every tenant-
> owned relation reachable in a query, not only the
> primary, carries the tenant predicate.
> 
> This invariant is, in our experience, the one
> most often missed, and it is the one with the
> largest measured exposure. A predicate on the pri-
> mary table does not constrain a joined table. The
> query
> 
> FROM reservations r LEFT JOIN customer c
> 
> ON c.id = r.customer id
> 
> is correctly scoped on reservations and entirely
> unscoped on customer.
> 
> Whether this leaks depends on whether the
> foreign

## Block 4: Evaluation Locator
**Section Heading**: `results. We identify transitive` [section offsets: 7916:8203]
**First 120 words verbatim** [offsets: 7916:8739]
> results. We identify transitive
> scope closure as a necessary invariant and show
> that set-valued scope can defeat index access.
> A lateral join restores indexed lookup when
> the tenant key is indexed; the deployed alter-
> native exhibits an entitlement-size planner cliff
> (Sections 5 to 6).
> 4. An interface ablation across eight model
> configurations and two transports. A 373-
> trial, three-arm experiment isolates the tool
> signature, measures both plausible and injected
> requests, and reveals a bypass when agents can
> rewrite scope (Section 8.8).
> 5. Production-scale
> evaluation.
> Structural,
> performance, and fail-closed tests on an opera-
> tional dataset containing multiple GBs of data
> report both supporting and adverse findings,
> including index gaps, nullable tenant keys, and
> the weaker enforcement mode used by the
> measured
**Section Heading**: `evaluation.` [section offsets: 8479:8753]
**First 120 words verbatim** [offsets: 8479:9267]
> evaluation.
> Structural,
> performance, and fail-closed tests on an opera-
> tional dataset containing multiple GBs of data
> report both supporting and adverse findings,
> including index gaps, nullable tenant keys, and
> the weaker enforcement mode used by the
> measured deployment.
> 
> 2 Background and Problem
> Statement
> 
> 2.1 Tool-calling agents
> 
> Under MCP [3], a server advertises a set of tools,
> each with a name and a JSON-schema signature.
> A client, typically an LLM application, selects
> a tool and emits arguments conforming to the
> schema. The server executes and returns a result,
> which re-enters the model’s context.
> 
> The security-relevant property is that the argu-
> ment values are model output. They are not chosen
> 
> 3
> 
> by the user directly, not validated by any deter-
> ministic intermediary,
**Section Heading**: `8 Evaluation` [section offsets: 43315:43407]
**First 120 words verbatim** [offsets: 43315:44059]
> 8 Evaluation
> 
> We ask eight questions:
> 
> RQ1 Do the structural invariants hold, and does the
> 
> implementation’s model of the schema match
> reality?
> RQ2 What does enforcement relocation cost in query
> 
> performance?
> RQ3 Does the design scale with entitlement size?
> RQ4 Is the threat model warranted by the properties
> 
> of a real multi-tenant database?
> RQ5 Does the system fail closed?
> RQ6 Do the invariants verified against synthetic
> 
> inputs also hold against production data?
> 
> --- PAGE BREAK ---
> 
> RQ7 Does removing the tenant parameter change
> 
> what a real LLM agent can reach, and how does
> it compare to defending with a prompt?
> RQ8 Does the deployed server actually confine a real
> 
> principal to the tenants its credential grants?
> 
> 8.1 Setup, and what
**Section Heading**: `8.8.5 Results` [section offsets: 64008:71645]
**First 120 words verbatim** [offsets: 64008:64741]
> 8.8.5 Results
> 
> Table 14 reports all 373 trials with Wilson score
> intervals.
> 
> Arm
> A
> served
> every
> out-of-scope
> attempt: 26 of 26, which corresponds to 26
> of 41 trials (63 %, 95 % CI 48 % to 76 %; Fig. 6).
> The three current GPT-5.6 tiers declined all 15
> pretexts, showing why the behavioural rate must
> not be mistaken for an interface property. When
> an agent did select the other entitled tenant,
> however, conventional validation accepted every
> call. This vector is a normal-sounding business
> request, not an obfuscated attack. Several agents
> flagged the authorization concern and served the
> data anyway; one observed that tool success was
> not evidence of authorization, asked the user to
> confirm clearance, and still included the other

## Block 5: Attack-Set Excerpts
**Location**: `evaluation.` [offsets: 8491:8751]
> Structural,
> performance, and fail-closed tests on an opera-
> tional dataset containing multiple GBs of data
> report both supporting and adverse findings,
> including index gaps, nullable tenant keys, and
> the weaker enforcement mode used by the
> measured deployment.

## Block 6: Baseline Excerpts
**Location**: `8.8.5 Results` [offsets: 64765:64856]
> Table 14 Ablation results, 373 trials across eight model
> configurations and two transports.

## Block 7: Cost Excerpts
**Location**: `8.8.5 Results` [offsets: 65611:65810]
> Benign control
> A, B, C
> Claude
> 3
> 1
> 0
> 
> † obtained by forging the scope file, not through the tool
> 
> Resistance
> to
> blatant
> injection
> is
> configuration- and release-specific, not an
> authorization boundary.

## Block 8: Limitations
**Section Heading**: `10 Threats to Validity` [section offsets: 87918:90864]
**First 120 words verbatim** [offsets: 87918:88719]
> 10 Threats to Validity
> 
> External and construct validity. This is a
> single-system study. The field proportions and
> planner threshold are properties of one schema,
> optimizer, index layout, and data distribution;
> only the mechanisms are expected to transfer.
> Even two relationships on the same source table
> differed by four orders of magnitude in crossing
> rate. The assertions show that the stated invari-
> ants hold for tested inputs, not that the invariant
> set is complete. Moreover, our goal confines reads
> 
> 25
> 
> to a credential’s entitlement, not necessarily to the
> one tenant intended for a particular session.
> 
> Internal validity. Measurements ran against
> a
> live
> replica
> under
> uncontrolled
> load.
> A
> block-timed pilot incorrectly made JSON TABLE
> appear faster than IN; interleaved paired trials
> reversed

## Block 9: Adaptivity Hits
no hits
