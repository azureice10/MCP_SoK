# Evidence Locator Packet: zhuoran-2026-mcp-sandboxscan-wasm-based-secure

- **Title**: MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2601.01241
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\zhuoran-2026-mcp-sandboxscan-wasm-based-secure\fulltext.txt
- **Character Count**: 63283

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 729:850]
> We present SandScope, an MCP-
> aware audit framework that combines runtime witness detection
> with semantic tool profiling.
**Location**: `Abstract` [offsets: 1393:1508]
> We evaluate SandScope
> on controlled cross-language subjects, an evasion benchmark, and a
> 100-repository MCP corpus.
**Location**: `Introduction` [offsets: 5768:6634]
> we propose SandScope, an MCP-aware
> 
> --- PAGE BREAK ---
> 
> Conference’17, July 2017, Washington, DC, USA
> Zhuoran Tan, Run Hao, Jeremy Singer, Yutian Tang, and Christos Anagnostopoulos
> 
> audit framework for third-party tools. SandScope combines two
> evidence layers: a runtime witness detector that reports observed
> source-to-sink exposures in LLM-visible MCP outputs, and a seman-
> tic profiler that recovers declared tool capabilities to characterize
> attack surface and guide testing when execution is incomplete. The
> core contributions are:
> 
> • We define LLM-visible MCP response fields, including tool-
> result text, prompt/messages fields, and structured return
> payloads, as protocol-level security sinks, and formulate
> external-to-sink exposure as runtime risk for MCP tools.
> • We build a scenario-driven runtime audit pipeline that exe-
> cutes portable tools under WASI

## Block 3: Method Locator
**Section Heading**: `implementation can reflect authority-bearing process state into` [section offsets: 47266:48929]
**First 120 words verbatim** [offsets: 47266:48173]
> implementation can reflect authority-bearing process state into
> LLM-visible output under protocol execution.
> 
> Repo B demonstrates an input-to-sink witness. The targeted pass
> generated schema-valid arguments containing MCP_INPUT_CANARY_*
> for repository or query fields of a code-repository tool. The server
> attempted the requested operation, failed because the generated
> identifier was invalid or inaccessible, and reflected the generated
> value in MCP-visible error or result text. This witness is not a vul-
> nerability by itself, but it confirms that SandScope can observe real
> client-input-to-result propagation in an MCP server.
> 
> Repo C illustrates the “observed egress only” category. The in-
> voked desktop/configuration-oriented tool was not classified as
> network-capable from recovered metadata, yet runtime monitoring
> recorded denied outbound connections to an external browser-
> support host. The same
**Section Heading**: `implementation runtime witnesses showing that environment, file,` [section offsets: 52105:53742]
**First 120 words verbatim** [offsets: 52105:52985]
> implementation runtime witnesses showing that environment, file,
> or network-intent sources reached LLM-visible MCP outputs.
> 
> Sandboxing and secure execution. WASM/WASI and OS-level
> sandboxes provide isolation boundaries for untrusted or semi-trusted
> code [6, 10, 13]. SandScope uses these mechanisms as backends
> rather than treating isolation as the main contribution. WASI is use-
> ful when a portable artifact or shim is available, while native stdio
> protocol driving preserves fidelity for unmodified MCP servers and
> should be paired with external OS containment when scanning
> untrusted native tools. The key distinction is that SandScope adds
> MCP-aware sink extraction, source-to-sink witness reporting, and
> semantic capability profiling on top of controlled execution.
> 
> Overall, existing work either isolates execution without MCP-
> aware leakage semantics, or inspects MCP and

## Block 4: Evaluation Locator
**Section Heading**: `12. These results show that SandScope provides practical, auditable` [section offsets: 1880:3605]
**First 120 words verbatim** [offsets: 1880:2670]
> 12. These results show that SandScope provides practical, auditable
> evidence for MCP tool risk through controlled execution, MCP-
> aware sink extraction, runtime witness reporting, and semantic
> capability profiling.
> 
> CCS Concepts
> 
> • Security and privacy →Software security engineering; Op-
> erating systems security; Information flow control; • Software and
> its engineering →Dynamic analysis.
> 
> Permission to make digital or hard copies of all or part of this work for personal or
> classroom use is granted without fee provided that copies are not made or distributed
> for profit or commercial advantage and that copies bear this notice and the full citation
> on the first page. Copyrights for components of this work owned by others than the
> author(s) must be honored. Abstracting with credit is
**Section Heading**: `Evaluation` [section offsets: 29601:45076]
**First 120 words verbatim** [offsets: 29601:30461]
> Evaluation
> 
> We evaluate SandScope along four questions:
> 
> • RQ1: Can SandScope produce auditable runtime witnesses
> when authority-bearing sources are reflected into LLM-visible
> MCP sinks under controlled MCP executions?
> 
> --- PAGE BREAK ---
> 
> MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools
> Conference’17, July 2017, Washington, DC, USA
> 
> • RQ2: How does the lightweight witness detector behave un-
> der low-effort transformations and known evasion patterns?
> • RQ3: What fraction of real-world MCP repositories can be
> dynamically executed through a shallow corpus scan, and
> what are the dominant failure modes?
> • RQ4: Does targeted schema-guided exploration uncover
> source-to-sink witnesses in real MCP servers that already
> complete a shallow protocol session?
> • RQ5: How much corpus visibility does semantic profiling
> provide beyond

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 30087:30238]
> • RQ3: What fraction of real-world MCP repositories can be
> dynamically executed through a shallow corpus scan, and
> what are the dominant failure modes?
**Location**: `Evaluation` [offsets: 30599:30939]
> First, a controlled cross-
> language benchmark includes 30 Go, Python, Rust, and TypeScript
> subjects spanning benign tools, environment leaks, file-exfiltration
> fixtures, upstream-content echoes, C2-beacon fixtures, and MCP
> protocol variants; it measures source-to-sink witnesses, false pos-
> itives and negatives, and execution-path support.
**Location**: `Evaluation` [offsets: 30940:31144]
> Second, a shal-
> low scan of 100 real-world MCP repositories measures dynamic
> coverage, failure modes, latency, semantic extraction coverage, de-
> clared capabilities, and semantic/runtime egress agreement.
**Location**: `Evaluation` [offsets: 31355:31441]
> The controlled benchmark contains 30 sub-
> jects across four implementation ecosystems.
**Location**: `Evaluation` [offsets: 31707:31777]
> The real-world corpus contains 100 popu-
> lar MCP-related repositories.
**Location**: `Evaluation` [offsets: 31778:31929]
> SandScope resolves 91 repositories
> for dynamic scanning and attempts startup, protocol initializa-
> tion, tools/list discovery, and tool-call execution.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `12. These results show that SandScope provides practical, auditable` [offsets: 1884:2094]
> These results show that SandScope provides practical, auditable
> evidence for MCP tool risk through controlled execution, MCP-
> aware sink extraction, runtime witness reporting, and semantic
> capability profiling.
**Location**: `12. These results show that SandScope provides practical, auditable` [offsets: 3442:3522]
> MCP-SandboxScan: WASM-based Secure Execution and
> Runtime Analysis for MCP Tools.
**Location**: `Evaluation` [offsets: 29658:29819]
> • RQ1: Can SandScope produce auditable runtime witnesses
> when authority-bearing sources are reflected into LLM-visible
> MCP sinks under controlled MCP executions?
**Location**: `Evaluation` [offsets: 29841:30086]
> MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools
> Conference’17, July 2017, Washington, DC, USA
> 
> • RQ2: How does the lightweight witness detector behave un-
> der low-effort transformations and known evasion patterns?
**Location**: `Evaluation` [offsets: 30389:30556]
> • RQ5: How much corpus visibility does semantic profiling
> provide beyond dynamic execution, and how do declared
> egress capabilities align with runtime egress evidence?
**Location**: `Evaluation` [offsets: 30599:30939]
> First, a controlled cross-
> language benchmark includes 30 Go, Python, Rust, and TypeScript
> subjects spanning benign tools, environment leaks, file-exfiltration
> fixtures, upstream-content echoes, C2-beacon fixtures, and MCP
> protocol variants; it measures source-to-sink witnesses, false pos-
> itives and negatives, and execution-path support.

## Block 8: Limitations
**Section Heading**: `Discussion & Limitations` [section offsets: 48929:50779]
**First 120 words verbatim** [offsets: 48929:49800]
> Discussion & Limitations
> 
> SandScope separates runtime evidence from semantic attack-surface
> metadata and reports only positive, auditable witnesses: source-
> derived bytes, or normalized/decoded views of them, that appear
> in LLM-visible MCP sinks. This design makes findings explainable
> but incomplete. The detector covers exact substrings, suffix-aware
> snippets, separator-normalized chunking, and a small set of decoder
> passes, but does not infer arbitrary transformations such as encryp-
> tion, compression, hashing, semantic rewriting, summarization, or
> custom encodings. Therefore, absence of a witness is not evidence
> that no flow exists, and a flow-observed repository is not automati-
> cally a vulnerability; it only shows that seeded source bytes reached
> an LLM-visible sink in the exercised scenario.
> 
> Coverage is also limited by what SandScope can execute and ob-

## Block 9: Adaptivity Hits
**Matched Term**: `evasion` | **Location**: `Abstract` [offsets: 1230:1745]
> Its semantic layer recovers declared capabilities
> from tools/list metadata and static registrations to characterize at-
> tack surface when execution is incomplete. We evaluate SandScope
> on controlled cross-language subjects, an evasion benchmark, and a
> 100-repository MCP corpus. SandScope completes shallow dynamic
> scans for 35 repositories and, through a broader semantic profiling
> pass, recovers metadata for 1,127 tools across 71 repositories, in-
> cluding 886 tools with security-sensitive declared capabilities.
**Matched Term**: `evasion` | **Location**: `Introduction` [offsets: 6851:7759]
> • We introduce a complementary semantic profiling layer that
> recovers declared MCP tool capabilities from protocol-level
> tools/list metadata and static source registrations, en-
> abling attack-surface characterization when dynamic exe-
> cution fails and cross-validation of declared egress-related
> capabilities against runtime network evidence.
> • We evaluate SandScope on controlled cross-language sub-
> jects, an evasion benchmark, and a 100-repository MCP cor-
> pus, reporting runtime scan outcomes, transformation limits
> of lightweight witness detection, real-world execution cov-
> erage, latency, semantic capability distribution, and seman-
> tic/runtime agreement.
> 
> To our knowledge, SandScope is the first MCP-specific behav-
> ioral audit framework that treats LLM-visible protocol fields as
> security sinks and reports runtime source-to-sink witnesses across
> unmodified MCP servers and portable WASI subjects.
**Matched Term**: `evasion` | **Location**: `Evaluation` [offsets: 29841:30238]
> MCP-SandboxScan: WASM-based Secure Execution and Runtime Analysis for MCP Tools
> Conference’17, July 2017, Washington, DC, USA
> 
> • RQ2: How does the lightweight witness detector behave un-
> der low-effort transformations and known evasion patterns?
> • RQ3: What fraction of real-world MCP repositories can be
> dynamically executed through a shallow corpus scan, and
> what are the dominant failure modes?
**Matched Term**: `Evasion` | **Location**: `Evaluation` [offsets: 35251:35577]
> 4.3
> Evasion Benchmark
> 
> Table 2 compares raw substring matching with the enhanced wit-
> ness detector. Raw matching covers only verbatim and simple pre-
> fix/suffix exposures, whereas the enhanced detector adds normal-
> ized and decoded sink views for low-effort transformations such as
> ROT13, hex, base64, and separator chunking.
**Matched Term**: `evasion` | **Location**: `Evaluation` [offsets: 35579:35852]
> This result is not a general evasion defense. The enhanced detec-
> tor covers only recoverable transformations included in the bench-
> mark; encrypted, compressed, hashed, semantically rewritten, sum-
> marized, or custom-transformed leaks remain outside SandScope’s
> guarantee.
