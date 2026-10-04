# Evidence Locator Packet: huijun-2026-first-measurement-study-authentication-security

- **Title**: A First Measurement Study on Authentication Security in Real-World Remote MCP Servers
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: benchmark_measurement
- **Link**: https://arxiv.org/abs/2605.22333
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\huijun-2026-first-measurement-study-authentication-security\fulltext.txt
- **Character Count**: 80267

## Block 2: Contribution Sentences
**Location**: `Abstract—The Model Context Protocol (MCP) is emerging as` [offsets: 808:907]
> We present the first measurement study of authentication
> security in real-world remote MCP servers.
**Location**: `Abstract—The Model Context Protocol (MCP) is emerging as` [offsets: 1763:1997]
> Applying it to 119 testable real-world OAuth-enabled MCP
> servers, we find that each server exhibits at least one flaw,
> with a total of 325 flaws identified, among which dynamic client
> registration flaws affect 96.6% of tested servers.

## Block 3: Method Locator
**Section Heading**: `implementation deviations. Using mainstream cybersecurity` [section offsets: 5886:7770]
**First 120 words verbatim** [offsets: 5886:6790]
> implementation deviations. Using mainstream cybersecurity
> search engines, we identify 7,973 validated live remote MCP
> servers. Among them, 40.55% expose their tool interface
> with no authentication mechanism, while 2,428 implement
> OAuth-based authorization flows. We then analyze a fully
> testable subset of these OAuth deployments and distill three
> security-relevant characteristics: open client environments,
> dynamic client registration, and delegated authorization.
> 
> Based on these observations, we construct an authenti-
> cation flaw taxonomy for OAuth-based remote MCP, sum-
> marizing 9 security flaws across 4 categories. We also
> develop a semi-automated detection framework that recon-
> structs OAuth lifecycles from MCP traffic, applies passive
> checks to observed flows, and performs controlled active
> probing for flaws that require dynamic validation. Applying
> it to 119 OAuth-enabled MCP servers, we
**Section Heading**: `4.2. Taxonomy of Implementation Flaws` [section offsets: 30745:36825]
**First 120 words verbatim** [offsets: 30745:31575]
> 4.2. Taxonomy of Implementation Flaws
> 
> Guided by the abstracted workflow and the MCP and
> OAuth specifications, we derive a taxonomy of implemen-
> tation flaws in OAuth-based remote MCP servers. The tax-
> onomy asks which security checks should hold in each
> phase, then groups the ways these checks fail in practice. It
> contains nine flaw types in four categories: dynamic client
> registration flaws, delegated authorization flaws, open client
> environment flaws, and common OAuth misconfigurations.
> 
> The first three categories arise from the deployment
> characteristics, while the last captures conventional OAuth
> mistakes that remain prevalent in MCP deployments. Table 5
> summarizes the categories and the phases where they appear.
> 
> C1: Dynamic client registration flaws. These flaws
> arise when dynamic client registration accepts new
**Section Heading**: `5.1. Design Ideas` [section offsets: 37404:40557]
**First 120 words verbatim** [offsets: 37404:38238]
> 5.1. Design Ideas
> 
> Detecting MCP OAuth flaws requires more than apply-
> ing independent rules to individual HTTP requests. OAuth
> traffic in MCP deployments is often mixed with local call-
> backs, remote MCP callbacks, and upstream service au-
> thorization flows. Some flaws are only visible after recon-
> structing a full authorization lifecycle, while others require
> controlled mutations or browser-visible confirmation. These
> properties lead to three practical challenges.
> 
> •
> Challenge 1: Layer ambiguity. A single session may
> contain local-client callbacks, remote MCP call-
> backs, and upstream authorization flows. Without
> distinguishing these layers, a detector may apply a
> rule to the wrong OAuth flow or miss flaws that only
> arise in delegated authorization.
> 
> •
> Challenge 2: Lifecycle dependence. Several flaws
> cannot be determined
**Section Heading**: `Implementation Details. We use VSCode Copilot as the` [section offsets: 45832:46825]
**First 120 words verbatim** [offsets: 45832:46663]
> Implementation Details. We use VSCode Copilot as the
> MCP client and simultaneously leverage Burp Suite [28] to
> 
> 9
> 
> --- PAGE BREAK ---
> 
> monitor its communication traffic. Our detection framework
> runs as a Burp plugin, performing vulnerability checks on
> the captured requests and responses. Our automated detec-
> tion framework is built upon and extends OAuthScan, an
> existing Burp Suite extension [29]. The OAuthScan is ca-
> pable of identifying basic OAuth flaws (e.g., open redirects
> and weak state parameters). However, it lacks the architec-
> tural context required in MCP environments. Consequently,
> we restructured its core logic and extended its capabilities
> to address the three key characteristics of MCP identi-
> fied earlier. Specifically, we introduced customized lifecycle
> modeling. We overhauled its traffic classification

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation.` [section offsets: 7770:8064]
**First 120 words verbatim** [offsets: 7770:8564]
> Evaluation.
> We
> develop
> a
> semi-
> automated security detection framework and conduct
> a large-scale detection study of OAuth-based re-
> mote MCP servers. We manually tested 119 OAuth-
> enabled servers and found that all exhibit at least
> one flaw, obtaining 9 CVE IDs through responsible
> disclosure.
> 
> 2. Background
> 
> 2.1. Model Context Protocol (MCP)
> 
> The Model Context Protocol (MCP), introduced by An-
> thropic in November 2024, is an open standard for connect-
> ing LLM-based applications to external tools, data sources,
> and services [11]. Its architecture consists of three principal
> roles: (1) The MCP host is the user-facing AI application,
> such as Claude Desktop, Cursor IDE, or an autonomous AI
> agent, that orchestrates LLM interactions, enforces access
> control, and manages the lifecycle of MCP
**Section Heading**: `3.2. Identification Results` [section offsets: 16969:20702]
**First 120 words verbatim** [offsets: 16969:17798]
> 3.2. Identification Results
> 
> Table 1 summarizes the identification results. The
> search-engine queries produced a large initial dataset, which
> resulted in 28,715 unique candidate endpoints after dedu-
> plication by IP address and port. Active MCP probing
> further refined this set to 7,973 live remote MCP servers.
> To estimate false positives, two security researchers indepen-
> dently reviewed a random sample of 100 validated servers.
> We identified only 1 false positive, a non-standard JSON-
> RPC service that resembled an MCP handshake but did not
> expose a valid MCP tool interface.
> 
> TABLE 1. IDENTIFICATION RESULTS FOR REMOTE MCP SERVERS.
> 
> Candidate Discovery
> Automated Validation
> 28,715
> 7,973
> 
> Finding 1.1: Authentication mechanisms vary across
> validated remote MCP servers. Table 2 summarizes the au-
> thentication status of the
**Section Heading**: `EVALUATION.` [section offsets: 21599:24940]
**First 120 words verbatim** [offsets: 21599:22472]
> EVALUATION.
> 
> Subset
> OAuth-enabled
> DCR-enabled
> Testable
> Servers
> 2,428
> 1,118
> 119
> 
> To ensure valid and safe end-to-end testing, we man-
> ually filtered the initial deployments. We excluded 387
> redundant nodes (e.g., domain/IP overlaps, multi-instance
> deployments) and 32 invalid cases that required no authen-
> tication. Furthermore, 573 servers were deemed untestable:
> 50 exposed did not support DCR (returning HTTP 404),
> 207 suffered connection or execution failures, and 316
> were restricted by strict enterprise access controls. We then
> eliminated 7 anomalous nodes that immediately triggered a
> callback response upon receiving an authorization request
> without any user interaction, thus failing to constitute a
> complete OAuth semantic flow. These untestable factors are
> objective constraints (e.g., corporate network policies, server
> flaws, or lack of user interaction) that
**Section Heading**: `5. Real-world Evaluation` [section offsets: 36825:37404]
**First 120 words verbatim** [offsets: 36825:37644]
> 5. Real-world Evaluation
> 
> In this section, we examine how the flaw taxonomy
> manifests in real-world OAuth deployments. The detector
> follows the abstracted workflow: it first reconstructs the
> relevant OAuth lifecycle, then applies flaw-specific checks at
> the phases where the taxonomy indicates a security property
> should hold. We first explain the design ideas behind the
> detector, then describe the detection pipeline, report results
> on 119 testable OAuth-enabled remote MCP servers, and
> present case studies showing how individual flaws can com-
> pose into end-to-end attacks.
> 
> 5.1. Design Ideas
> 
> Detecting MCP OAuth flaws requires more than apply-
> ing independent rules to individual HTTP requests. OAuth
> traffic in MCP deployments is often mixed with local call-
> backs, remote MCP callbacks, and upstream service au-

## Block 5: Attack-Set Excerpts
**Location**: `3.2. Identification Results` [offsets: 17045:17202]
> The
> search-engine queries produced a large initial dataset, which
> resulted in 28,715 unique candidate endpoints after dedu-
> plication by IP address and port.
**Location**: `EVALUATION.` [offsets: 22586:22683]
> All subsequent statistical
> percentages are strictly scoped to this 119-server evaluation
> dataset.
**Location**: `5.3. Detection Results` [offsets: 46849:46873]
> Dataset and Performance.
**Location**: `5.3. Detection Results` [offsets: 46874:47033]
> We use the 119 testable
> DCR-enabled OAuth servers from Table 3 as the evaluation
> dataset and apply the detection pipeline to identify candidate
> flaw instances.
**Location**: `5.3. Detection Results` [offsets: 49137:49241]
> Finding 3.1: Every server in our evaluation dataset
> exhibits at least one confirmed authentication flaw.
**Location**: `evaluation dataset, led by Dynamic Client Registration` [offsets: 49749:49854]
> evaluation dataset, led by Dynamic Client Registration
> Flaws (C1) and Open Client Environment Flaws (C3).

## Block 6: Baseline Excerpts
**Location**: `5.3. Detection Results` [offsets: 48781:48914]
> The single false negative
> appeared in F5 and resulted from non-standard parameter
> naming that evaded our baseline signature matching.

## Block 7: Cost Excerpts
**Location**: `3.2. Identification Results` [offsets: 17281:17401]
> To estimate false positives, two security researchers indepen-
> dently reviewed a random sample of 100 validated servers.
**Location**: `3.2. Identification Results` [offsets: 17402:17550]
> We identified only 1 false positive, a non-standard JSON-
> RPC service that resembled an MCP handshake but did not
> expose a valid MCP tool interface.
**Location**: `EVALUATION.` [offsets: 23938:24124]
> As a result, the security of the OAuth
> flow depends heavily on runtime protections such as PKCE,
> redirect URI binding, short-lived authorization artifacts, and
> correct callback handling.
**Location**: `5.3. Detection Results` [offsets: 47810:47930]
> The framework produced 379
> candidate alerts, of which 325 were confirmed as true
> positives, and 54 were false positives.
**Location**: `5.3. Detection Results` [offsets: 47989:48086]
> This corresponds
> to 85.75% precision and 99.69% recall over the manually
> verified flaw instances.
**Location**: `5.3. Detection Results` [offsets: 48276:48341]
> The false positives mainly stem from two engineering
> constraints.

## Block 8: Limitations
**Section Heading**: `6.3. Limitations and Future Work` [section offsets: 63479:64633]
**First 120 words verbatim** [offsets: 63479:64299]
> 6.3. Limitations and Future Work
> 
> Our study has several limitations. First, our measurement
> relies on FOFA and Shodan for initial discovery, which may
> not capture MCP servers deployed behind CDNs, firewalls,
> or private networks, introducing coverage bias toward pub-
> licly indexed infrastructure; this scope was also guided by
> ethical considerations, as we restricted our study to publicly
> reachable assets to minimize risk to deployed systems and
> operators. Second, our flaw detection framework relies on
> rule-based matching, which requires manual specification
> 
> of each flaw type and may miss subtle or novel vulnerabil-
> ity patterns. Future work could replace this with LLM or
> agent-driven analysis for more adaptive and comprehensive
> detection.
> 
> As AI agents increasingly interact with external services
> on behalf of

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `6.3. Limitations and Future Work` [offsets: 64043:64428]
> of each flaw type and may miss subtle or novel vulnerabil-
> ity patterns. Future work could replace this with LLM or
> agent-driven analysis for more adaptive and comprehensive
> detection.
> 
> As AI agents increasingly interact with external services
> on behalf of users, the authentication patterns established
> by MCP will likely influence other agent protocols such as
> A2A [30] and ANP [31].
