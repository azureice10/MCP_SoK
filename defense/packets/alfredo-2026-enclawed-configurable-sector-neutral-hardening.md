# Evidence Locator Packet: alfredo-2026-enclawed-configurable-sector-neutral-hardening

- **Title**: enclawed: A Configurable, Sector-Neutral Hardening Framework for Single-User AI Assistant Gateways
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2604.16838
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\alfredo-2026-enclawed-configurable-sector-neutral-hardening\fulltext.txt
- **Character Count**: 76644

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 3060:4005]
> Abstract
> 
> 1
> Introduction
> 
> enclawed: A Configurable, Sector-Neutral Hardening
> 
> Framework for Single-User AI Assistant Gateways
> 
> Alfredo Metere
> Metere Consulting, LLC.
> alfredo.metere@metereconsulting.com
> 
> May 1, 2026
> 
> 1
> 
> Generative AI has crossed quickly from prototype into the operational fabric of regulated in-
> dustries. Financial-services firms use large language models (LLMs) for research summarization
> 
> --- PAGE BREAK ---
> 
> touching material non-public information (MNPI); healthcare systems apply them to protected
> health information (PHI); defense contractors handle controlled unclassified information (CUI)
> and International Traffic in Arms Regulations (ITAR)-controlled materials; legal teams rely
> on them for privileged-counsel work; pharmaceutical R&D operates on embargoed clinical-trial
> data. Each of these settings is governed by frameworks that pre-date generative AI but ap-
> ply to it directly — the Health Insurance Portability

## Block 3: Method Locator
**Section Heading**: `Architecture` [section offsets: 27071:30099]
**First 120 words verbatim** [offsets: 27071:27975]
> Architecture
> 
> 3.1
> Two flavors
> 
> 3.2
> Module set: cloud modules gated, not source-stripped
> 
> not enforced
> strict deny-by-default
> 
> informational
> required, exact match
> 
> permitted
> locked
> 
> permitted
> frozen non-configurable
> 
> loaded with warning
> rejected
> 
> 9
> 
> enclawed selects a flavor at boot via the ENCLAWED_FLAVOR environment variable.
> Table 4
> contrasts the two.
> 
> Earlier drafts of this paper argued that the safest cut was to delete the 78 cloud-channel and
> cloud-provider module directories from the upstream extensions/ tree so the unsafe state would
> be UNREACHABLE rather than UNSELECTED. After porting from upstream OpenClaw,
> the framework now ships all 134 module directories (cloud channels, cloud LLM providers,
> external search/browser/webhook modules, and local-capable modules) and delegates rejection
> to the host admission gate (src/plugins/manifest-registry.ts). In the enclaved flavor,
> every module
**Section Heading**: `Implementation` [section offsets: 30099:38828]
**First 120 words verbatim** [offsets: 30099:30940]
> Implementation
> 
> 4.1
> Hash-chained audit log
> 
> 10
> 
> The framework is delivered in two parallel surfaces:
> a TypeScript (TS) twin under
> src/enclawed/ that bundles with the upstream OpenClaw build, and a canonical refer-
> ence under enclawed/src/ written in plain Node ECMAScript Modules (.mjs) with zero
> runtime dependencies. The canonical surface runs under node –test without pnpm install,
> which keeps the standalone security suite cheap to exercise and trivial to audit.
> Table 5
> summarizes file counts and lines of code per tree.
> 
> Repository layout.
> The framework is hosted as enclawed-oss — the open-source, MIT-
> licensed, self-contained, public-bound git repository this paper documents.
> It carries the
> OpenClaw fork base, the framework primitives (classification, policy, audit, DLP, crypto
> wrapper, zeroize, module signing, trust root, HITL,
**Section Heading**: `Method` [section offsets: 38828:39397]
**First 120 words verbatim** [offsets: 38828:39669]
> Method
> B
> —
> refinement-typed
> dispatch.
> skill-formal-types.mjs
> exposes
> buildRefinedDispatch(M), which returns a frozen dispatcher that throws RefinementError
> on any envelope whose capability is outside M.caps. The dispatcher is the runtime’s only ingress
> to the host application programming interfaces (APIs); an envelope an adversarially-prompted
> large language model (LLM) emits cannot reach a host API without passing the type predicate.
> The data-processing inequality [58] bounds the per-envelope leakage at log2(|D| + 1) bits,
> where D = M.caps.
> 
> --- PAGE BREAK ---
> 
> Method C — bounded model checking.
> skill-formal-bmc.mjs runs an exhaustive
> depth-first search over the abstract envelope state space at bound K (default 8) and checks, on
> every symbolic trace, that the runtime biconditional of [10] holds (no world-state change with-
> out a
**Section Heading**: `Method C — bounded model checking.` [section offsets: 39397:52297]
**First 120 words verbatim** [offsets: 39397:40276]
> Method C — bounded model checking.
> skill-formal-bmc.mjs runs an exhaustive
> depth-first search over the abstract envelope state space at bound K (default 8) and checks, on
> every symbolic trace, that the runtime biconditional of [10] holds (no world-state change with-
> out a corresponding admitted envelope). The state-space size is (|D| + 1)K; for deployments
> with |D| ≤10 and K ≤8 the search explores at most 118 ≈2.1 × 108 traces, which discharges
> in seconds.
> 
> Proof-carrying skill bundle.
> The CLI scripts/skills-formal-verify.mjs composes the
> three methods, hashes each evidence file with a sorted-key canonical encoding, and signs a
> four-file bundle (static.json, types.proof.json, smt.unsat.json, manifest.attest.json)
> with the same Ed25519 module-signing primitive used for the manifest itself. The runtime’s
> bundle re-checker (verifyFormalBundle in skill-formal-bundle.mjs)

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 52297:55444]
**First 120 words verbatim** [offsets: 52297:53252]
> Evaluation
> 
> 8.1
> Test methodology
> 
> 8.2
> Unit test coverage
> 
> 8.3
> Adversarial pen-test coverage
> 
> 8.4
> Bugs found and fixed during construction
> 
> 17
> 
> 1. crypto-fips.deriveKey — ERR_CRYPTO_INVALID_SCRYPT_PARAMS at boundary. Lifted
> maxmem explicitly to 64 MiB.
> 
> 2. classification.makeLabel — compartments backed by Set were mutable through
> .add() despite Object.freeze. Switched to deduplicated, sorted, frozen arrays.
> 
> 3. classification.parse — auto-promoting TOP_SECRET to TOP_SECRET_SCI on any non-
> releasability segment broke format/parse round-tripping. Removed; SCI is a separately
> representable head.
> 
> 4. audit-log.append — concurrent calls raced on lastHash, producing a broken chain.
> Fixed with internal Promise queue.
> 
> 5. audit-log log-injection — payload strings containing raw newlines could spoof a fake
> JSONL record. Fixed with deepSanitize pass before record construction.
> 
> 6. trust-root — post-boot setTrustRoot could substitute attacker-controlled

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
**Section Heading**: `Limitations and Gaps the Deploying Organization Owns` [section offsets: 57136:58627]
**First 120 words verbatim** [offsets: 57136:57956]
> Limitations and Gaps the Deploying Organization Owns
> 
> The framework cannot, by itself, deliver an accredited deployment. The following gaps are
> explicitly out of scope and must be filled by the deploying organization’s security and compliance
> program:
> 
> --- PAGE BREAK ---
> 
> • Identity binding. canRead enforces Bell-LaPadula, but no identity layer ships. Integrate
> the organization’s identity provider (IdP) — using SAML, OIDC, or a smart card — and
> bind a clearance label to every session.
> 
> • OS-level mandatory access control. Defense in depth requires SELinux MLS or equivalent
> enforcing the same lattice outside the JavaScript process.
> 
> • Cross-trust-zone transfer.
> The framework forbids egress; a real deployment needs an
> accredited cross-zone control (a data diode, a file-transfer appliance, a manual review
> queue,

## Block 9: Adaptivity Hits
**Matched Term**: `evasion` | **Location**: `Header / Abstract` [offsets: 882:2130]
> The classification ladder is fully data-driven: a deploying organization selects from five
> built-in presets (generic, US-government, healthcare, financial services, three-tier) or sup-
> plies its own JSON. We accompany the implementation with a security review, a 356-
> case test suite (261 unit tests, 95 adversarial pen-tests) covering tamper detection, sig-
> nature forgery, fetch- and raw-socket egress bypass, audit-log truncation and re-ordering,
> trust-root mutation, DLP evasion, prompt injection, code injection, and biconditional ad-
> mission for net-capable extensions; real-time human-in-the-loop control (per-agent pause
> / resume / stop and approval queues); a memory-bounded secure transaction buffer with
> rollback (default cap 50% of system RAM, configurable); a strict-mode TypeScript type-
> check of every framework file; and a GitHub Actions workflow ready for continuous in-
> tegration.
> A newly added .mjs primitive — the biconditional extension-admission gate
> (extension-admission.mjs) — extends the paper’s skill trust schema to non-skill ex-
> tensions, so every loadable extension declaring net.egress must carry a signed mani-
> fest, an explicit per-extension host allowlist, and (in the enclaved flavor) a verification
> level ≥tested.
**Matched Term**: `evasion` | **Location**: `1. Always-on policy.` [offsets: 18394:18896]
> --- PAGE BREAK ---
> 
> • An adversarial test suite of 95 cases targeting tamper detection, signature forgery, fetch-
> and raw-socket egress bypass, audit-log truncation and re-ordering, trust-root mutation,
> DLP evasion, prompt injection, code injection, and biconditional admission for net-capable
> extensions, alongside 261 unit tests, all passing on Node 22.
> 
> • A GitHub Actions workflow that runs the suites on push, PR, and weekly cron, plus a
> strict-mode TypeScript typecheck of all 22 framework files.
**Matched Term**: `evasion` | **Location**: `Method` [offsets: 74098:76644]
> --- PAGE BREAK ---
> 
> File
> Tests
> Adversarial focus
> audit-log.pentest.mjs
> 6
> in-place edit, tail truncation (documented
> limit), record reorder, newline log-injection,
> __proto__ pollution, 100 concurrent appends
> signature-forgery.pentest.mjs
> 7
> wrong-key, signerKeyId swap, signature re-
> play across modules, downgrade attack, ca-
> pability injection, malformed signature, open-
> flavor warning capture
> egress-bypass.pentest.mjs
> 8
> hostname case normalization,
> Host-header
> spoofing,
> embedded
> credentials,
> IPv4-in-
> IPv6,
> file:/data:
> schemes,
> fetch reassign
> with/without freeze (latter via subprocess),
> malformed URLs
> trust-root-and-scheme.pentest.mjs
> 10
> setTrustRoot
> after
> lock,
> __proto__/constructor
> pollution,
> dupli-
> cate
> normalized
> names,
> non-contiguous
> ranks, negative rank, empty levels, non-string
> canonicalName, missing id, type checks
> dlp-evasion.pentest.mjs
> 8
> oversize cap, ReDoS bound, zero-width cam-
> ouflage, whitespace variants, redact correct-
> ness, PEM camouflage gap, null/undefined
> safety
> prompt-injection.pentest.mjs
> 11
> 5 spoofed roles, bidi overrides, zero-width
> camouflage, control chars, code-fence break-
> out, imperative-override phrases, multi-vector
> composite, idempotency
> code-injection.pentest.mjs
> 8
> shell-metachar manifest fields, JS-eval clear-
> ance rejected, function-shaped JSON treated
> as data, channel id path-traversal denied,
> __proto__ provider id, allowedDirs allowlist,
> malformed JSON error context, deep-JSON
> safety
> extension-egress-bypass.pentest.mjs
> 10
> raw-socket bypass via net.Socket.connect,
> net.createConnection
> (normalized-array
> form),
> http.request to literal IPs,
> sub-
> classed
> Socket,
> VPN-CIDR
> boundary,
> ipInCidr edges, onDeny audit hook, post-
> freeze tamper attempts
> extension-audit-tamper.pentest.mjs
> 12
> per-field record edits,
> recordHash forgery
> propagation, deletion of middle records, re-
> ordering, 32 concurrent appends, newline log-
> injection, prototype-pollution payloads, docu-
> mented tail-truncation gap
> extension-net-admission.pentest.mjs
> 15
> unknown capability tokens rejected, empty
> netAllowedHosts
> rejected,
> unsigned
> in
> enclaved
> rejected,
> signer-not-in-trust-root
> rejected,
> post-signing
> tamper
> caught
> (canonical
> bytes
> cover
> verification
> +
> netAllowedHosts),
> net.egress
> below
> tested rejected, per-extension Socket guard,
> biconditional D=S report
> Total OSS pen-tests
> 95
> 
> 25
> 
> Table 8: Adversarial test inventory. Each row covers a distinct attack family; cases that doc-
> ument a known limitation are noted as “documented” or “gap” so the deploying organization
> knows where defense-in-depth is required.
