Received: d month yyyy \| Revised: d month yyyy \| Accepted: d month yyyy \| Published online: d month yyyy

**REVIEW**

# Security of Model Context Protocol in Agentic AI Systems: A Systematization of Knowledge on Threats, Trust Boundaries, and Defense Mechanisms

AI and Security Convergence

yyyy, Vol. XX(XX) 1–5

DOI: 10.47852/bonviewAISCXXXXXXXX

**\[Author names, with affiliation numbers; mark the corresponding author with \*\]**

*^1^ \[Department, Organization, Country, Email address\]*

**\*Corresponding author:** \[Name, Department, Organization, Country. Email: address at the institution where the research was conducted\]

**Abstract:** The Model Context Protocol (MCP) lets language-model agents call external tools through a standard interface, and it places a third-party server between the agent's planner and the user's data. We systematize what is known about MCP security. From 614 deduplicated records identified across six academic databases and gray-literature sources, we built a corpus of 171 MCP-specific works published between the protocol's release in November 2024 and September 2026, and a second reviewer audited the sole inclusions of the first. We contribute a taxonomy of sixteen attack classes in four layers, a trust boundary model of eight crossings with a stated security property for each, a comparison of five specification revisions against those properties, a maturity grading of 85 defenses, and a ranked roadmap of research gaps. The 2026-07-28 revision partially addresses three of the sixteen classes and fully addresses none. A formative coverage test against 22 disclosed vulnerabilities and incidents absorbed 17 records under the original fourteen classes and 20 after the test led us to add two classes. Of the 85 defenses, 68 (80.0%) were evaluated only by their authors (L1), 2 (2.4%) were evaluated independently (L2), 15 (17.6%) are conceptual proposals (L0), and none reached the deployed-control level (L3); only 3 of 70 evaluated defenses (4.3%) faced a test aimed at their own mechanism, and none evaluated intent inversion. A case study of a documented incident shows three violated properties in a session where every call was authorized. Independent, adaptive evaluation of structural defenses ranks first among seven research gaps.

**Keywords:** Model Context Protocol, agentic AI security, trust boundaries, tool poisoning, defense maturity

## 1. Introduction

Large language model (LLM) agents now read files, query databases, send messages, and modify code repositories on behalf of their users. Each of these actions requires a connection between the model and an external system. Until late 2024, developers built these connections as bespoke, framework-specific integrations. Anthropic released the Model Context Protocol (MCP) in November 2024 as an open standard for this connection layer [1]. MCP defines a client-server architecture: a host application runs one or more MCP clients, and each client maintains a session with an MCP server that exposes tools, resources, and prompts over JSON Remote Procedure Call (JSON-RPC) 2.0 [2]. Within a year, major model providers and developer tools had adopted the protocol, and public registries listed tens of thousands of servers. X. Li and Gao [3] analyzed 67,057 servers across six public registries alone.

MCP changes the security posture of agentic systems in a specific way. The protocol delivers server-authored natural language (tool names, descriptions, parameter schemas, and tool results) into the model's context window, and the model uses that text to decide which privileged operation to perform next. The same channel therefore carries both data and potential adversarial instructions. Prompt injection, confused deputies, supply-chain compromise, and command injection all predate MCP [4]. MCP places these known threats inside a standardized, dynamically discoverable architecture in which third parties author model-visible metadata and a single host can combine capabilities from many independently administered servers.

Empirical studies confirm that attackers can exploit this arrangement. In April 2025, Invariant Labs showed that a tool description can instruct an agent to read the user's Secure Shell (SSH) keys and leak them through an innocuous tool parameter [5]. The MCPTox benchmark, built from 353 tools on 45 live servers, measured a mean attack success rate of 36.5% across 20 LLM agents, and models with stronger instruction-following were often more susceptible [6]. Zhao et al. [7] showed that injected content can chain benign tools into a data-exfiltration workflow and catalogued 12,230 tools across 1,360 servers as potential components of such chains. A measurement of 7,973 remote MCP servers found that 40.55% exposed tools without authentication and that each of the 119 testable OAuth deployments contained at least one flaw [8].

The literature has grown quickly. The first analyses were vendor disclosures and arXiv preprints in early 2025; by mid-2026, MCP security studies had appeared at the Institute of Electrical and Electronics Engineers (IEEE) Symposium on Security and Privacy [7], the IEEE/IFIP International Conference on Dependable Systems and Networks [3], and the Association for the Advancement of Artificial Intelligence (AAAI) Conference [6], and in *ACM Transactions on Software Engineering and Methodology* (Association for Computing Machinery, ACM) [2] and *IEEE Transactions on Software Engineering* [9]. This leaves researchers and system designers with four problems.

First, existing taxonomies divide the threat space along incompatible axes. Hou et al. [2] organize 16 threat scenarios by attacker type across a four-phase server lifecycle. Yang et al. [10] define 17 attack types over four attack surfaces, Song et al. [9] propose four attack categories, C. Huang et al. [11] apply the STRIDE threat model (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) to five MCP components, and Gaire et al. [12] separate adversarial security threats from epistemic safety hazards. These schemes do not tie each attack class to the trust boundary it crosses, yet a designer needs exactly that information to decide where a control belongs.

Second, the protocol keeps changing. The specification added an OAuth 2.1-based authorization framework for HTTP transports in March 2025 (optional for implementations, but normative where used), resource-bound tokens and an explicit ban on token passthrough in June 2025, and client identifier metadata documents in place of dynamic client registration in November 2025; the July 2026 revision deprecated server-initiated sampling [13]. A finding against one revision does not automatically hold for another, and few studies report which they tested. Critiques of the 2024 specification now describe historical behavior, while authenticated semantic attacks lie outside every revision.

Third, the defense literature lacks a shared standard of evidence. Proposals range from static metadata scanners and signed tool definitions to runtime monitors, capability attestation, and information-flow architectures [14–16]. Authors call these mechanisms deployed, practical, or effective under different criteria, and few have faced independent or adaptive evaluation. A systematic review of 73 defense studies from 2022 to 2025 found that 93.2% relied on custom evaluations and 23.3% reported effectiveness [17], although that review reaches back before MCP's release.

Fourth, existing reviews list open problems without ranking them. A researcher entering the field cannot tell whether formal verification of the trust model, compositional information-flow control, or the human factors of tool approval deserves attention first.

We address these problems through a Systematization of Knowledge (SoK) built on a systematically constructed corpus. The paper makes four contributions:

**C1. MCP Security Taxonomy.** We consolidate attack classes reported in peer-reviewed papers, preprints, specifications, and vulnerability disclosures into a layered taxonomy, recording for each class the entry channel, the trust boundary crossed, the protocol assumption exploited, and the affected component, and we test its coverage against disclosed Common Vulnerabilities and Exposures (CVE) records and documented incidents.

**C2. Trust Boundary Model.** We model an MCP deployment as seven trust zones (user, host application, LLM planner, MCP client, MCP server, external system, and authorization infrastructure) and the channels that cross them, state the security property each crossing should preserve, separate local stdio from remote HTTP deployments, and compare MCP with native function calling and the Agent2Agent (A2A) protocol.

**C3. Defense Maturity Analysis.** We map each defense to the taxonomy classes and trust boundaries it covers and grade its maturity on an explicit evidence scale: conceptual proposal, author-evaluated prototype, independently evaluated mechanism, and deployed control. The resulting matrix exposes boundaries that no independently evaluated defense protects.

**C4. Research Gap Roadmap.** We derive open problems from uncovered cells of the threat-defense matrix, contradictions between studies, and limitations that authors report, and we rank them by the severity of the uncovered threat and the tractability of the research.

We restrict the scope to security: adversarial compromise of confidentiality, integrity, availability, and authorization. Model alignment and task reliability fall outside it. We cover MCP from specification revision 2024-11-05 through revision 2026-07-28. We treat work published before MCP's release, such as indirect prompt injection studies and benchmarks [4, 18], as background rather than as MCP-specific evidence.

Table 1 positions this SoK against prior reviews of MCP security. Hou et al. [2] supplied the first architectural and lifecycle analysis; Gaire et al. [12] contributed an earlier SoK centered on the security-safety distinction; Anbiaee et al. [19] compared twelve protocol-level risks across four agent protocols. Three later works address defenses: Tamayo [17] reviews defense mechanisms systematically, Rostamzadeh et al. [20] map defenses onto a defense-placement taxonomy, and Nandish et al. [21] analyze the vulnerabilities and defensive inadequacies reported in 18 studies (Section 6.5). Our work adds an explicit trust boundary model as the organizing axis, records the specification revision behind each finding, grades defenses by evidence rather than by claim, and ranks open problems.

**Table 1**

**Positioning of this work relative to prior reviews of MCP security**

| **Work**                  | **Type**                                          | **Primary organizing axis**                          | **Protocols covered**                            | **Latest version reviewed**               |
|---------------------------|---------------------------------------------------|------------------------------------------------------|--------------------------------------------------|-------------------------------------------|
| Hou et al. [2]          | Survey with case studies                          | Attacker type × four-phase server lifecycle          | MCP                                              | 2026 (journal)                            |
| Gaire et al. [12]       | SoK                                               | Adversarial security vs. epistemic safety            | MCP                                              | December 2025 (arXiv)                     |
| C. Huang et al. [11]    | Threat model with client evaluation               | STRIDE/DREAD over five components                    | MCP                                              | 2026 (*J. Cybersecur. Priv.*)             |
| Anbiaee et al. [19]     | Comparative threat model                          | Protocol-level risk categories                       | MCP, A2A, and two others                         | February 2026 (arXiv)                     |
| Tamayo [17]             | Systematic literature review                      | Defense mechanisms in MCP implementations            | MCP                                              | 2026 (book series; 73 studies, 2022–2025) |
| Rostamzadeh et al. [20] | Defense-placement taxonomy with coverage analysis | Architectural layer responsible for enforcement      | MCP                                              | April 2026 (arXiv)                        |
| Nandish et al. [21]     | Systematic analysis of 18 studies                 | Four inherent-risk deficits                          | MCP                                              | 2026 (book series)                        |
| **This work**             | SoK with systematic corpus                        | Trust boundaries crossed, per specification revision | MCP, with comparison to function calling and A2A | September 2026                            |

Section 2 describes the review method. Section 3 presents the MCP architecture and the Trust Boundary Model (C2). Section 4 develops the Security Taxonomy (C1), and Section 5 analyzes authentication and authorization across specification revisions. Section 6 reports the Defense Maturity Analysis (C3). Section 7 applies the taxonomy and trust boundary model to documented incidents. Section 8 presents the Research Gap Roadmap (C4), and Section 9 discusses implications and limitations and concludes.

## 2. Review Methodology

### 2.1. Review design

An SoK contributes new organizing frameworks for existing knowledge; a systematic review contributes transparent and reproducible coverage. We combine the two. We followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for scoping reviews (PRISMA-ScR) [22] for identification, screening, and reporting, because our goal is to map concepts, evidence types, and gaps rather than to pool effect sizes. PRISMA-ScR does not require critical appraisal of individual sources; we graded evidence anyway (Section 2.7) because the Defense Maturity Analysis depends on it.

Much MCP security knowledge first appeared outside academic venues, in the protocol specification, government guidance, and vulnerability disclosures. We therefore also followed the guidelines for multivocal literature reviews, which set out how to include and appraise gray literature alongside academic sources [23]. The search, selection, and extraction procedures follow Kitchenham and Charters [24].

### 2.2. Research questions

We formulated four research questions, one for each contribution (Table 2).

**Table 2**

**Research questions and corresponding contributions**

| **ID** | **Research question**                                                                                                                                                                                           | **Contribution**      |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| RQ1    | Which MCP-specific attack classes does the literature document, and which protocol features and assumptions does each exploit?                                                                                  | C1 (Section 4)        |
| RQ2    | Where do trust boundaries lie in local and remote MCP deployments, how do authentication and authorization enforce them across specification revisions, and how does MCP compare with function calling and A2A? | C2 (Sections 3 and 5) |
| RQ3    | Which defenses has the community proposed, which attack classes and trust boundaries does each cover, and how mature is the evidence for each?                                                                  | C3 (Section 6)        |
| RQ4    | Which research gaps remain, and which should the community address first?                                                                                                                                       | C4 (Section 8)        |

### 2.3. Time window and protocol baseline

The review window opens on 25 November 2024, the date of MCP's public release [1], and closes on 25 September 2026. We tracked five specification revisions: 2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25, and 2026-07-28 [13]. We placed work published before the release window into a separate background set (Set B). Set B supplies foundational concepts, such as indirect prompt injection [4] and dynamic agent security benchmarks [18], but does not count as MCP-specific evidence in any quantitative statement.

### 2.4. Information sources and search strategy

We executed parallel searches across six bibliographic sources to maximize recall while minimizing database-specific bias. For academic literature, we queried IEEE Xplore (112 records), the ACM Digital Library via Crossref API (13 records), Scopus via Elsevier REST API (172 records), arXiv (categories cs.CR, cs.AI, cs.SE, and cs.CL; 200 records), OpenAlex (200 records), and Semantic Scholar (95 records). For gray literature, we searched five source types: (a) the official MCP specification, specifically its five security-relevant revisions (2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25, and 2026-07-28), which Section 5 analyzes in detail; (b) the OWASP GenAI Security Project, which contributed conceptual framing but no MCP-specific findings; (c) government security guidance, specifically the NSA cybersecurity information sheet on MCP [25]; (d) vulnerability databases and package ecosystem registries, where an initial naive query for the standalone acronym "MCP" across the National Vulnerability Database (NVD API 2.0) and GitHub Security Advisories (GHSA) returned 98 candidate records that collapsed to only 3 true positives due to severe vocabulary mismatch (package advisories typically designate affected components by software identifier such as `mcp-server-git`, `@modelcontextprotocol/server-filesystem`, or `fastmcp` rather than the expansion "Model Context Protocol"). To achieve systematic recall, we executed an expanded multi-vector retrieval protocol combining structured Boolean queries (`"model context protocol"` OR `"mcp-server"` OR `"fastmcp"` OR `"mcp-remote"` OR `"mcp inspector"`), package name prefixes across npm, PyPI, and Maven ecosystem registries (`mcp-server-*`, `@modelcontextprotocol/*`), and Common Platform Enumeration (CPE) vendor entries; and (e) documented vulnerability disclosures from industry research teams and curated incident indices, including Invariant Labs' GitHub MCP disclosure [26], Asana's cross-tenant access advisory, and the Zealynx MCP Breach Index (Section 4.3). Across NVD, GHSA, and vendor advisories, this systematic protocol retrieved 128 raw candidates; deduplication yielded 31 unique records; and formal inclusion/exclusion screening excluded 9 non-MCP records (generic dependencies or LLM UI flaws lacking protocol bindings), establishing a final empirical validation benchmark of 22 Tier E4 records (20 confirmed CVEs and 2 documented vendor incident disclosures). Section 4.3 analyzes their coverage against our taxonomy. We confirmed venues with DBLP and publisher proceedings.

The acronym "MCP" collides with unrelated terms in engineering and medicine. Every query therefore requires either the full phrase "Model Context Protocol" or the acronym together with an agent or LLM term. Supplementary Table S1 lists the query strings. We ran all queries on 25 September 2026.

We complemented the database search with backward and forward snowballing [27]. The seed set comprised Hou et al. [2], Song et al. [9], Z. Wang et al. [6], Zhao et al. [7], and X. Li and Gao [3]. We iterated until an iteration returned no new eligible record.

Search identification and deduplication proceeded in two synchronized phases. In the baseline phase, multi-vector queries across OpenAlex (200 records), arXiv (200 records), and Semantic Scholar (95 records) yielded 495 raw candidate records, which collapsed upon title and DOI deduplication to an initial baseline pool of 460 unique records. In the supplementary phase, targeted native queries across archival engineering databases—IEEE Xplore (112 records), Scopus via Elsevier REST API (172 records), and the ACM Digital Library via Crossref API (13 records)—retrieved 297 raw records, deduplicating across the three sources to 213 unique records. Cross-referencing these 213 supplementary records against the baseline pool revealed 59 overlapping records (56 confirmed records, representing a 26.3% cross-index intersection with the baseline pool, plus 3 duplicate-cluster reconciliations), leaving exactly 154 net novel unique records. Merging the 460 baseline records with the 154 supplementary additions established the comprehensive deduplicated screening pool of 614 unique records ($460 + 154 = 614$). Gray-literature vulnerability screening across NVD, GHSA, and vendor advisories ran concurrently to establish the separate 22-record E4 empirical validation benchmark analyzed in Section 4.3 outside the academic screening pool.

### 2.5. Eligibility criteria

Table 3 lists the inclusion (IC) and exclusion (EC) criteria. A record entered the corpus only if it met all inclusion criteria and no exclusion criterion.

**Table 3**

**Eligibility criteria**

| **ID** | **Criterion**                                                                                                                                                                                                                                                                               |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IC1    | Published or posted between 25 November 2024 and 25 September 2026.                                                                                                                                                                                                                         |
| IC2    | Addresses the security of MCP specifically: attacks, vulnerabilities, threat models, authentication or authorization, defenses, or ecosystem security measurements; or compares MCP with another agent tool-use paradigm on security grounds.                                               |
| IC3    | Written in English.                                                                                                                                                                                                                                                                         |
| IC4    | Belongs to one of the following types: peer-reviewed paper; preprint that reports a method together with an evaluation or formal analysis; normative specification; government or standards-body guidance; vulnerability disclosure with a CVE identifier or reproducible proof of concept. |
| EC1    | Uses MCP only as infrastructure for a non-security goal, such as task-capability benchmarking.                                                                                                                                                                                              |
| EC2    | Discusses LLM or agent security without MCP-specific analysis. Foundational pre-release works of this kind enter Set B instead.                                                                                                                                                             |
| EC3    | Marketing material, opinion pieces without technical evidence, or statistics without a traceable method.                                                                                                                                                                                    |
| EC4    | Full text not accessible.                                                                                                                                                                                                                                                                   |
| EC5    | Uses "MCP" for an unrelated concept.                                                                                                                                                                                                                                                        |

### 2.6. Selection process and version reconciliation

We screened records in two rounds. Two reviewers, blind to each other's decisions and to any automated recommendation, independently screened a random 20% calibration sample (n = 92, random seed 42) drawn from the initial deduplicated baseline pool of 460 records, using only title, abstract, and publication year; venue, DOI, and source were withheld to avoid prestige bias. Raw agreement was 85.9% (79/92) and Cohen's κ = 0.734, indicating substantial agreement [28]. The figure excludes three records whose screening had been informed by worked examples in the reviewer protocol; they were replaced with three freshly drawn records (random seed 343) before the statistic was computed. κ rises to 0.798 when two functionally equivalent but differently labeled Set B decisions count as agreement. The calibrated screening protocol and decision thresholds were subsequently applied across the 154 supplementary search additions, expanding the screening pool from the 460 baseline records to the comprehensive total of 614 unique deduplicated records ($460 + 154 = 614$), backed by full dual-reviewer audit of all candidate inclusions.

The reviewers reconciled every disagreement in discussion, and two recurring sources led to protocol refinements. First, we operationalized the boundary between MCP-specific and generic agent-security work as a substitution test: if a record's security claim survives unchanged when "MCP" is replaced by a generic tool-calling framework, the record fails IC2 even where MCP is mentioned. On this basis five records describing generic mechanisms (information-flow control, multi-layer red-teaming, runtime tool-call interception, an agent-skills survey, and metadata-attack detection) were excluded under EC2. In the other direction, the test retained studies grounded in MCP's own artifacts (server codebases, registries, or logs) even when security is a minority theme, and applicative systems that nonetheless analyze an MCP-specific threat. Second, we clarified that Set B requires conceptual relevance to agent or tool-use security, not merely a publication date before the review window, after four pre-2024 records on unrelated topics were misclassified as background.

One reviewer then screened the remaining 80% of the pool alone. Because agreement on the calibration sample did not show that a single reviewer would apply the substitution test consistently, we audited that work afterward. A second reviewer, blind to the first reviewer's decisions, re-screened from title, abstract, and year 137 of the 138 records the first reviewer had included alone (one had no abstract). After open reconciliation, 37 of the 137 (27.0%; Wilson 95% interval 20.3%–35.0%) were excluded, mostly generic agent-security or application papers in which MCP was only a deployment interface (EC1, EC2). One further record from the adjudicated batch was excluded because its full text showed that "MCP" did not mean the Model Context Protocol (EC5). The audit prompted a rule, recorded after the fact and applied only to audited records: an attack or defense paper passes only if (a) its threat or mechanism is framed as a weakness or requirement of the MCP ecosystem or architecture, (b) the results supporting its central claim were obtained on real MCP servers, tools, or clients (or, for a design without experiments, its mechanism depends on MCP-specific elements), and (c) its measurements evaluate the claim it advances. We also audited the 182 exclusions the first reviewer made alone. None of the 118 off-topic exclusions (IC2) mentions MCP in title or abstract; a keyword scan for tool and agent terms flagged one, and 12 drawn at random were checked by hand. The second reviewer, blind to the first reviewer's codes, re-screened these 20 and the 64 other exclusions and reinstated none. The reviewers agreed on the exclusion code for 61 of 84 records (72.6%), mostly where a record never mentions MCP and could carry IC2 or EC2; seven records without an abstract were judged from the title. Eleven records that could not be resolved from the abstract were checked in full text; two taxonomies of real-world MCP server faults [29, 30] were retained because each grounds its categories in mined MCP codebases, and one proxy architecture was reclassified to include because its controls were built around MCP's client-server model.

Screening across both phases followed the PRISMA-ScR protocol with dual-coder calibration and post-audit reconciliation. In the baseline pool of 460 records, screening retained 157 records (148 MCP-specific and 9 Set B background) and excluded 303 records. In the supplementary pool of 154 records, screening and substitution testing retained 25 records (23 Tier E1 MCP-specific and 2 Set B background) and excluded 129 records (81 non-protocol acronym collisions under EC5, 47 engineering applications under EC1, and 1 generic agent security study under EC2). Combining the two pools yields exact arithmetic closure across all 614 unique records: 171 entered the MCP-specific corpus ($148 + 23 = 171$), 11 entered the background Set B ($9 + 2 = 11$), and 432 were excluded ($303 + 129 = 432$, comprising IC2: 164; EC1: 125; EC2: 56; EC5: 82; EC3: 5; none under EC4). Together, the 171 MCP-specific works and 11 Set B background works form the complete extracted corpus of 182 records ($171 + 11 = 182$; Section 2.8), while the 614 total records are fully accounted for ($182\text{ included} + 432\text{ excluded} = 614$). Figure 1 summarizes this disposition.

![Figure 1: PRISMA-ScR flow diagram](figures/figure1_prisma_flow.png)

**Figure 1**

**PRISMA-ScR flow diagram of record identification, screening, and inclusion**

The PRISMA-ScR flow diagram illustrates the two-phase identification and screening workflow (460 baseline records + 154 supplementary additions = 614 unique deduplicated records screened; 432 excluded; 182 extracted, comprising 171 MCP-specific synthesis records and 11 Set B background records), with the 22-record E4 empirical benchmark maintained as an external validation set. MCP security literature moves from preprint to archival publication within months, and several studies first posted to arXiv have since appeared at venues including the IEEE Symposium on Security and Privacy and the AAAI Conference. We therefore reconciled every record before extraction: on 25 September 2026 we checked each record's DOI, its venue's proceedings, and the journal reference field of its latest arXiv version. When an archival version existed, we cited it and merged all versions into one record, using the archival figures where versions differed. This changed the publication status of many records, most of which gained a confirmed archival venue and an upgrade from evidence tier E2 to E1. The gray-literature sources include one vendor security advisory (Invariant Labs' disclosure of the GitHub MCP incident [26], analyzed qualitatively in Section 7 as a case study and benchmarked in the external E4 validation set of Section 4.3 outside the 171 synthesis corpus), one NSA guidance document [25], one OWASP GenAI Security Project contribution, and one MCP specification (whose five security-relevant revisions Section 5 analyzes in detail). We also recorded the specification revision, software development kit (SDK) version, and client versions that each empirical study evaluated, so that each finding stays tied to the protocol state it describes.

### 2.7. Evidence classification

We classified every included record into one of five evidence tiers (Table 4). The tiers weight the synthesis; they do not exclude records. We appraised Tier E3 to E5 sources with the AACODS checklist (authority, accuracy, coverage, objectivity, date, significance [31]). In particular, primary vendor security advisories (such as Asana and Invariant Labs) constitute Tier E4 practitioner disclosures based on verified institutional authority and reproducible technical mechanics, whereas secondary incident aggregators (specifically the Zealynx MCP Breach Index) serve as Tier E4/E5 trackers evaluated under AACODS to corroborate real-world incident details (Section 4.3).

**Table 4**

**Evidence tiers**

| **Tier** | **Evidence type**                                                   | **Examples**                                        |
|----------|---------------------------------------------------------------------|-----------------------------------------------------|
| E1       | Peer-reviewed empirical, measurement, or formal study               | Papers at archival conferences and journals         |
| E2       | Preprint with an empirical, measurement, or formal method           | arXiv papers not yet published at an archival venue |
| E3       | Normative specification or government and standards-body guidance   | MCP specification revisions; NSA guidance           |
| E4       | Practitioner disclosure with a CVE or reproducible proof of concept | Vendor security advisories; CVE records             |
| E5       | Community guidance and consensus frameworks                         | OWASP projects                                      |

We applied three synthesis rules. First, we did not pool attack success rates across benchmarks, which differ in threat model, target models, prompts, and success criteria. Second, the text labels any claim that rests only on E4 or E5 sources. Third, we excluded vendor statistics without a traceable method from quantitative statements.

### 2.8. Data extraction

We extracted data with the form in Supplementary Table S2. The corresponding author extracted all 182 corpus records (171 MCP-specific and 11 Set B), and a second author verified the same 20% calibration sample used for screening reliability (Section 2.6).

### 2.9. Synthesis procedure

We synthesized the extracted data separately for each contribution.

**Taxonomy (C1).** We coded attack descriptions openly, then grouped codes into classes by entry channel and exploited assumption. We reconciled the resulting classes with the schemes of Hou et al. [2], Yang et al. [10], Song et al. [9], and C. Huang et al. [11], recording where our classes merge or split theirs. We assessed coverage by mapping an external validation set of 22 E4-tier records (20 confirmed CVEs and 2 vendor incident disclosures), which does not count toward the 171-record synthesis corpus, to the taxonomy. We report which class absorbs each record, the absorption proportion before and after the revisions the test prompted, each with a 95% Wilson score interval, and which records remain as residue outside protocol boundaries. Because the test led us to revise the taxonomy, it is a formative refinement step rather than an independent held-out test (Section 4.3).

**Trust Boundary Model (C2).** We derived trust zones and boundary crossings from the architecture and authorization sections of each specification revision and from threat models in the corpus. We express each security property as a predicate over principals, data origin, and actions. We validate the model by tracing documented incidents through it in Section 7.

**Defense Maturity Analysis (C3).** We assigned each defense one of four maturity levels: L0, conceptual (proposal or guidance without an evaluated implementation); L1, prototyped (implemented and evaluated by its authors); L2, independently evaluated (evaluated by a party other than its authors); and L3, deployed (normative in the specification or shipped in production tooling). We flagged separately whether any evaluation used an adaptive adversary. A deployed control is not necessarily an effective one; we report deployment and evidence of effectiveness as separate attributes.

**Research Gap Roadmap (C4).** We identified candidate gaps from three sources: taxonomy-boundary cells without an L2 or L3 defense, contradictions between studies, and limitations that authors state. We ranked each gap by the severity of the threat it leaves unaddressed and by the tractability of the research needed to close it.

### 2.10. Threats to validity

*Construct validity.* Authors use different names for similar attacks, for example "rug pull," "descriptor drift," and "post-approval mutation." We maintained a synonym table during coding and mapped every term to one taxonomy class.

*Internal validity.* A single primary coder can introduce selection and classification bias. Independent re-screening and extraction checks (Sections 2.6 and 2.8) limit this risk, and we report agreement statistics. The audit removed 27.0% of the first reviewer's sole inclusions, so the risk was material at that stage. The audit of exclusions reinstated nothing, but the second reviewer tends to exclude, so it has little power to detect missed inclusions at the boundary, and it tests screening, not search recall. The second reviewer was one person, and the rule for attack and defense papers was formalized after the audit and applied only to audited records.

*Coverage validity.* We queried six academic bibliographic databases (IEEE Xplore, ACM Digital Library, Scopus, arXiv, OpenAlex, Semantic Scholar) in parallel to minimize database-specific recall gaps. The 26.3% overlap between IEEE/ACM/Scopus results and our arXiv/OpenAlex pipeline confirms substantial coverage. The parallel search additionally captured 23 Tier E1 peer-reviewed studies from IEEE, ACM, and Scopus-indexed venues (including Elsevier and Springer journals) that had not yet been indexed by the free APIs. In the gray literature, our initial query for the standalone acronym "MCP" yielded 98 raw candidates but captured only 3 CVEs due to vocabulary mismatch (vulnerability advisories reference package stems like `mcp-server-*` rather than the expansion "Model Context Protocol"). We addressed this limitation by executing an expanded, systematic multi-vector search combining explicit Boolean strings across NVD API 2.0, GHSA GraphQL queries across npm/PyPI/Maven ecosystems, and vendor advisories (Section 2.4). From 128 raw candidates, 31 unique records remained after deduplication, and screening removed 9 out-of-scope records, yielding 22 Tier E4 records (20 CVEs and 2 vendor disclosures). Two coders independently mapped all 22 records against the revised taxonomy; initial agreement was 90.9% (20/22; Cohen's κ = 0.87), reaching full consensus after open adjudication (Section 4.3). Under the original fourteen classes, 17 of 22 records (77.3%; Wilson 95% CI: 56.6%–89.9%) were absorbed (with Asana tentatively stretched into C2); three were not (CVE-2025-6514, CVE-2025-54135, and CVE-2025-54136), prompting the formal addition of Class C6 (*Client-side sink enforcement failure*, adding the $S_i / \Theta \to C$ crossing) and extension of Class B1. Furthermore, to avoid conflating planner-level identity confusion with server-side isolation flaws, we formally established Class C7 (*Authorization scoping and tenant isolation failure* on $S_i \to X_i$) for the Asana disclosure. With these revisions, 20 of 22 records (90.9%; 72.2%–97.5%) are absorbed, while 2 records represent operational residue outside protocol boundary enforcement: host-side credential storage (CVE-2025-47274) and SDK regex denial of service (CVE-2026-0621) (Section 4.3).

*External validity.* The field changes monthly, and our conclusions hold as of 25 September 2026. Recording specification revisions per finding lets readers judge which conclusions still apply after later revisions. Furthermore, the empirical vulnerability benchmark exhibits language ecosystem concentration: the 20 confirmed CVEs in our E4 benchmark reside in TypeScript/Node.js (10 CVEs), Python (9 CVEs), and Java (1 CVE) implementations, mirroring the runtimes of the earliest official reference servers and client SDKs. While emerging MCP server implementations and SDKs exist in Go, Rust, and C#, they currently lack public CVE disclosures in NVD and GHSA; our empirical findings on implementation flaws (such as Class C5 sink enforcement failures) therefore reflect the deployment maturity of TypeScript and Python stacks rather than runtime immunity of other languages.

*Conclusion validity.* Several gray-literature sources come from vendors of security products, and benchmark results do not compare across studies. The evidence tiers and synthesis rules in Section 2.7 address both issues.

### 2.11. Use of generative AI tools

In line with the journal's policy and the Committee on Publication Ethics (COPE) guidance, we disclose the use of generative AI (Claude, Anthropic). Beyond drafting assistance, an AI assistant executed substantial parts of the review pipeline under author direction: running the search queries in Supplementary Table S1, deduplicating and version-reconciling records, preparing the blinded screening worksheets of Section 2.6 (automated recommendations were recorded for later audit but withheld from the human reviewers), computing inter-rater statistics, and checking the data for internal consistency, which caught the calibration-example contamination and the Set B misclassification described in Section 2.6. All inclusion, exclusion, and reconciliation decisions were made by the human reviewers. We verified the bibliographic details in this manuscript (authors, venues, DOIs, and reported figures) against primary or Crossref-indexed sources and replaced automatically generated record descriptions wherever they disagreed with the primary source. The authors take full responsibility for the content of this article.

## 3. MCP Architecture and the Trust Boundary Model

### 3.1. Architecture and operational primitives

MCP defines three roles. A **host** is the application the user interacts with (an IDE, a chat client, an autonomous agent runtime). The host embeds one or more **clients**, each holding a one-to-one JSON-RPC 2.0 connection with a **server** [13]. A server exposes up to four capabilities: **tools** (tools/list, tools/call), named functions with a natural-language description and a JSON Schema inputSchema; **resources** (resources/list, resources/read), addressable read-only context such as files or query results; **prompts** (prompts/get), parameterized templates a user or host selects; and **sampling** (sampling/createMessage), which lets a server request a completion from the client's model. Revisions through 2025-11-25 negotiated these capabilities in an initialize handshake within a stateful session. The 2026-07-28 revision removed both the handshake and protocol-level sessions, so every request carries its protocol version and client capabilities; it also deprecated sampling and replaced server-initiated requests with a multi-round-trip pattern in which the server returns an input request and the client retries [13]. Whatever a tools/call or resources/read returns is inserted into the planner's context verbatim, and no field in the wire format distinguishes data from instruction. A single host commonly connects to several independently administered servers, and the planner sees the union of their descriptions regardless of which server it calls [2].

Two transports carry the session. **stdio** launches the server as a local subprocess, framing JSON-RPC over stdin/stdout; the server inherits the host process's OS identity, environment variables, and file permissions outright. **Streamable HTTP** (superseding the earlier HTTP with server-sent events design in the 2025-03-26 revision) carries the same messages over HTTP with Server-Sent Events for streaming, and is the only transport to which the specification's optional OAuth 2.1 profile applies [13].

### 3.2. Trust zones

We model a deployment as a set of trust zones, each a locus with its own administrative control and, in general, its own trust in the others (Table 5). A zone boundary is crossed whenever data or control flows from one zone into another; MCP's security properties are properties of these crossings, not of any single zone in isolation. We keep the user (U) and host (H) as distinct zones, rather than merging them, because several documented attack classes [2] are specifically host- or vendor-side rather than user-side, and collapsing the two would erase that distinction. Figure 2 shows the zones and the channels between them.

**Table 5**

**Trust zones in an MCP deployment**

| **Zone**                         | **Description**                                                              | **Administrative control**                                                     |
|----------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| U (User)                         | The human whose goal the session serves                                      | The user                                                                       |
| H (Host)                         | The application embedding the MCP client(s)                                  | The host vendor                                                                |
| L (Planner)                      | The LLM the host invokes to reason and select actions                        | The model provider                                                             |
| C (Client)                       | The per-server session object inside the host                                | The host vendor                                                                |
| Sᵢ (Server *i*)                  | An independently administered MCP server, *i* = 1…*n*                        | The server's own operator, generally a third party                             |
| Xᵢ (External system)             | The data source, API, or environment behind server *i*                       | Whoever controls that external system                                          |
| Θ (Authorization infrastructure) | The OAuth authorization and resource servers governing access to a remote Sᵢ | The identity provider, which may or may not be the same party as Sᵢ's operator |

![Figure 2: Trust zones and channels of an MCP deployment](figures/figure2_trust_zones.png)

**Figure 2**

**Trust zones and channels of an MCP deployment**

The number of server zones is unbounded and grows with every connection the host makes, unlike a single-application integration where one vendor controls every zone but U.

### 3.3. Boundary crossings and security properties

To analyze MCP's security architecture rigorously, we distinguish between **normative security invariants** (the formal predicates that an idealized, secure agent interaction model *must* preserve to prevent compromise) and **descriptive protocol reality** (how the normative MCP specification and real-world deployments actually behave). Table 6 lists the eight crossings a session exercises. For each crossing, it specifies the normative invariant required for security alongside its current protocol enforcement and empirical status. We write principal(x) for the entity a message or action is attributable to, and label(m) for whether message *m* functions as data or as control information reaching the planner.

**Table 6**

**Boundary crossings, normative security invariants, and empirical enforcement status**

| **Crossing** | **What flows** | **Normative security invariant (What must hold)** | **Protocol enforcement & empirical reality (Current state)** |
|---|---|---|---|
| U → H | The user's goal or approval decision | principal(instruction acted on) = U, unless U has delegated authority for a specific action class | **Enforced by host UI under benign conditions.** Bypassed if host UI is subverted or unvetted workspace configurations execute automatically without consent (CVE-2025-54135). |
| Sᵢ → L (via C, H) | Tool descriptions, tool results, resource content | ¬(label(m) = control ∧ origin(m) ∈ {Sᵢ, Xᵢ} ∧ ¬authorized-as-instruction-source(Sᵢ, U)) — content from a server or its external system must not function as control information without explicit user authorization | **Unenforced by protocol design.** Wire format lacks data/control framing; tool outputs and resource contents are injected into the prompt verbatim. Routinely violated by indirect prompt injection and tool poisoning (Classes A1–A3; Z. Li et al. [33]). |
| L → Sᵢ (via C) | A tool invocation, with arguments | principal(invocation) = U for any action Sᵢ classifies as privileged, regardless of which zone assembled the request | **Partially specified, widely violated empirically.** Bearer tokens record user grants to client but cannot prove instruction provenance (user vs injected text). 2,846 of 6,137 measured servers (46.4%) exhibited insecure authorization state caching [32]. |
| C ↔ Θ, Sᵢ ↔ Θ | Token issuance and presentation | token audience(t) = Sᵢ, and possession of *t* implies no authority over any Sⱼ, *j* ≠ *i* | **Specified since 2025-06-18, optional/absent in ~70% of live deployments.** 40.55% of servers lack authentication, 29.00% use static credentials [8]; 100% of tested OAuth implementations exhibited compliance flaws [8]. |
| Sᵢ → Xᵢ | A privileged operation on the external system | action(Sᵢ, Xᵢ) ⊆ scope granted to principal(invocation), independent of what Sᵢ itself is capable of | **Unenforced by MCP protocol.** Confined only by server handler code; path traversal and command injection bypass confinement in 11 confirmed CVEs (Class C5; Section 4.3). |
| composition over S₁…Sₖ | The union of capabilities reachable in one session | ¬(∃ Sᵢ, Sⱼ, Sₘ ∈ {S₁…Sₖ} : untrusted-input(Sᵢ) ∧ sensitive-read(Sⱼ) ∧ external-egress(Sₘ)) without a re-consent step — no session may combine untrusted input, sensitive data access, and an outbound channel unchecked | **Unenforced by protocol.** MCP treats server connections as isolated JSON-RPC channels; cross-server information flow within the host context is unmonitored, enabling chained exfiltration at scale [7] and in documented incidents [26]. |
| descriptor(Sᵢ, t₁) vs descriptor(Sᵢ, t₀) | A tool, resource, or prompt definition, re-read at invocation time | hash(descriptor at t₁) = hash(descriptor approved at t₀), or the action requires re-consent | **Unenforced by specification.** Dynamic `tools/list` allows runtime descriptor mutation without cryptographic pinning or mandatory re-approval; exploited by post-approval rug pulls (Class B1; [14]). |
| Sᵢ / Θ → C | Remote metadata, authorization URLs, tool execution results, or launch directives consumed by client components | ∀ m ∈ inbound(C) : origin(m) ∈ {Sᵢ, Θ} ⟹ sanitized-for-sink(m, client-sink) — no peer-supplied string, endpoint URL, or launch parameter may be dispatched directly into local process execution or OS shell interpreters without rigorous sanitization | **Unenforced by protocol specification.** Left entirely to client host/adapter sanitization; unescaped OAuth parameters and unvetted configs trigger remote OS command injection on client hosts (CVE-2025-6514, CVE-2025-54135; Class C6). |

Crucially, the normative invariants of Table 6 serve as the formal yardstick against which both the protocol specifications (Section 5) and empirical incident traces (Section 7) are evaluated. When Section 5.3 notes that authorization does not cover semantic integrity, or when Table 15 records that a property "fails" during an incident trace, this does not represent an inconsistency in definition; rather, it reflects a fundamental architectural reality: MCP's wire format and authorization framework fail to enforce these normative invariants at the protocol layer, delegating enforcement entirely to imperfect host-side heuristics or external gateway defenses. The second row states the root cause behind tool poisoning, indirect prompt injection via tool results, and malicious-resource attacks. The third and fourth rows state the confused-deputy and token-scope properties. Z. Li et al. [33] title their attack a confused-deputy attack, but what they demonstrate lies on the second crossing: an adversarial server whose manipulated metadata overshadows a benign one hijacks the planner's tool selection in up to 90.89% of trials across 14 models on two MCP hosts, and MCP-Scan did not detect the resulting servers (evasion rate 100%). The hijack redirects an invocation without exploiting session authority, so we classify it under the semantic channel (classes A1 and A3, Section 4), not under C1. The fifth row fails whenever a server's own handler escapes the scope it advertises, as in path-confinement bypasses (Section 4.3). The sixth row is the property Zhao et al. [7] show violated at scale when otherwise-benign tools are chained into an exfiltration path. The seventh states the property that fails under rug-pull and registry-drift attacks [14]. The eighth row governs client-side sink execution: client host applications, adapters, or developer proxies consuming metadata from remote endpoints or peers must treat peer-supplied strings and URLs as untrusted data rather than direct arguments to local operating system utilities. This crossing is violated when client-side proxies spawn OS browsers using unescaped OAuth endpoint URLs (CVE-2025-6514) or when IDE hosts auto-execute unvetted workspace configurations (CVE-2025-54135; Section 4.3).

### 3.4. Local versus remote deployments

The two transports instantiate Table 6 differently (Table 7). Under stdio, C and Sᵢ share the host's process trust; Θ does not exist, and principal(invocation) is enforced, if at all, by the host's own sandboxing. Under Streamable HTTP, where a server implements authorization, Θ is realized as an OAuth 2.1 resource-server/authorization-server pairing, and Sᵢ is required to reject tokens audience-bound to any other server; Section 5 examines how often this holds in practice. Zhou et al. [8] measured how often it does not (Section 5.2).

**Table 7**

**Local versus remote deployment profiles**

| **Dimension**            | **stdio (local)**                                                                | **Streamable HTTP (remote)**                                                                   |
|--------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Identity basis           | Ambient OS user (UID, env vars, working directory)                               | OAuth 2.1 bearer token, audience-bound (optional; static tokens are also common)               |
| Network exposure         | None (local IPC only)                                                            | Public internet, intranet, or cloud VPC                                                        |
| Dominant failure         | Command injection, path traversal, credential leakage via inherited env vars     | Unauthenticated endpoints (40.55% [8]), registry/supply-chain spoofing, cross-tenant leakage |
| Isolation responsibility | Host (must sandbox the subprocess itself; the specification does not require it) | Server operator (container and network isolation)                                              |

### 3.5. Comparison with function calling and A2A

Table 8 restates the zone structure of Section 3.2 for two related paradigms. Native function calling collapses Sᵢ, Xᵢ, and Θ into H, removing the third-party-server zone at the cost of the interoperability MCP provides. The Agent2Agent protocol [34] connects a client agent to a remote peer *agent*, each publishing a signed Agent Card as its identity declaration, rather than to a narrow, typed tool server; the crossing that matters most is therefore peer authenticity rather than tool-descriptor integrity. A deployment combining both — a common pattern, since the two are complementary (Anbiaee et al. [19]; and, on compounding risk when a semantic manipulation against an A2A peer is used to trigger an MCP tool call, tentatively, S.-Y. Kim et al. [35]) — inherits every crossing in Table 6 for its MCP legs and adds a peer-authentication crossing for its A2A legs; Section 8 returns to this composition (gap 7).

**Table 8**

**Trust-boundary comparison across agent interaction paradigms**

| **Dimension**                                   | **Native function calling**                         | **MCP**                                               | **A2A**                                                 |
|-------------------------------------------------|-----------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------|
| Tool/peer discovery                             | Static, compiled into host code                     | Dynamic (tools/list)                                  | Dynamic, via Agent Card                                 |
| Zone collapsed into H                           | Sᵢ, Xᵢ, Θ                                           | none                                                  | none (adds a peer-authenticity crossing instead)        |
| Data/control separation at the planner boundary | Low (schema is static, but still enters the prompt) | None — descriptions and results are unstructured text | Moderate (structured task/artifact negotiation)         |
| Dominant failure mode                           | Host implementation bugs                            | Confused deputy, tool poisoning                       | Peer impersonation, semantic manipulation of delegation |

## 4. MCP Security Taxonomy

### 4.1. Construction and reconciliation with prior schemes

We built the taxonomy by open-coding the attack description in every included corpus record, then grouping codes by the entry channel and exploited assumption, per Section 2.9. Sixteen classes emerged, which we group into four layers by the Table 6 crossing each violates. We then reconciled these classes against the four prior schemes in our corpus that themselves propose a taxonomy (Table 9): Hou et al.'s [2] 16 scenarios across four attacker types and a four-phase server lifecycle; Yang et al.'s [10] MCPSecBench, 17 attack types over four attack surfaces; Song et al.'s [9] four categories (tool poisoning, puppet attacks, rug pull, malicious external resources); and C. Huang et al.'s [11] STRIDE mapping over five protocol components.

**Table 9**

**Reconciliation of this taxonomy with four prior schemes in the corpus**

| **This taxonomy**                                        | **Hou et al. [2]**                                 | **Yang et al. [10]**                                             | **Song et al. [9]**                                                 | **C. Huang et al. [11]**       |
|----------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------|
| A. Metadata/semantic channel (A1–A3)                     | Malicious-developer scenarios (e.g., tool poisoning) | Server surface (tool metadata, resources)                          | Tool Poisoning Attacks; Exploitation via Malicious External Resources | Spoofing, Tampering              |
| B. Descriptor integrity over time (B1–B3)                | Update- and maintenance-phase scenarios              | Server surface                                                     | Rug Pull Attacks                                                      | Tampering                        |
| C. Identity, authorization, and sink enforcement (C1–C7) | External-attacker and security-flaw scenarios        | Client and transport surfaces (e.g., Domain Name System rebinding) | *(not separately categorized)*                                        | Spoofing, Elevation of Privilege |
| D. Compositional/multi-server (D1–D3)                    | *(not separately categorized)*                       | *(not separately categorized)*                                     | Puppet Attacks (one cross-server pattern)                             | Information Disclosure           |

The clearest gap is Row D. Only Song et al.'s Puppet Attacks isolate a cross-server mechanism, and they cover one pattern, a malicious server steering another server's tools; the other three schemes fold multi-server attacks into single-server categories, although the composition property (Table 6) fails even when every individual call is safe. Nandish et al. [21] also propose a grouping, four inherent-risk deficits (capability, privilege, quality, and supply chain) drawn from 18 studies. We treat it as complementary and do not reconcile it class by class.

### 4.2. Layered taxonomy

Table 10 lists all sixteen classes. "Boundary" references the crossing in Table 6 that each class violates; "Assumption exploited" states the protocol design assumption the attack falsifies.

**Table 10**

**MCP security attack taxonomy**

| **Class**                                                | **Entry channel**                                                                        | **Boundary (Table 6)**           | **Assumption exploited**                                                                           | **Representative evidence**                                                                                                                                                                                 |
|----------------------------------------------------------|------------------------------------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **A1.** Tool metadata poisoning                          | Tool description or inputSchema fields                                                   | Sᵢ → L                           | Tool metadata is informational only                                                                | Z. Wang et al. [6]: 36.5% mean attack success rate across 20 agents, 72.8% peak on o1-mini; Beurer-Kellner and Fischer [5]; Z. Li et al. [33]: tool-selection hijacking up to 90.89% across 14 models |
| **A2.** Indirect injection via tool results or resources | content returned by tools/call or resources/read                                         | Sᵢ → L                           | Only the initial description, not every response, needs vetting                                    | Song et al. [9], "Exploitation via Malicious External Resources"                                                                                                                                          |
| **A3.** Description-quality-exploiting miscalls          | Ambiguous or conflicting tool descriptions                                               | Sᵢ → L                           | Ambiguity is a quality defect, not a security one                                                  | P. Wang et al. [36]: description "smells" across 1,180 servers induce wrong tool selection without adversarial intent; Z. Li et al. [33] exploit the same bias adversarially                            |
| **B1.** Descriptor & config mutation over time           | notifications/tools/list_changed after approval or workspace launch config               | descriptor(t₁) vs descriptor(t₀) | An approved descriptor or launch configuration stays fixed for the session                         | Bhatt et al. [14] (rug pull); Cursor MCPoison (CVE-2025-54136; Section 4.3) demonstrates persistent post-approval workspace configuration poisoning                                                     |
| **B2.** Registry/capability drift at scale               | Server metadata re-fetched over time                                                     | descriptor(t₁) vs descriptor(t₀) | Drift is rare enough that periodic re-audit suffices                                               | Bharti [37]: 120 snapshots of the official registry over 88.6 days (19,099 servers); re-auditing the 5% most-drifted servers catches only about 20% of those whose descriptions later change              |
| **B3.** Schema-mutation robustness failure               | Runtime interface evolution mid-session                                                  | descriptor(t₁) vs descriptor(t₀) | Planners degrade gracefully under interface change                                                 | Liu et al. [38]: 11 interface-mutation operators applied across 123 servers                                                                                                                               |
| **C1.** Confused deputy                                  | Any privileged action assembled by L                                                     | L → Sᵢ                           | The acting principal is whoever holds the session, not whoever asked                               | Concept from Hardy [39]; the OAuth-proxy variant is specified in the MCP security best practices [40]; no corpus paper demonstrates a pure C1 attack directly without prompt injection; demonstrated operationally by Invariant Labs incident [26] (Section 7) |
| **C2.** Caller identity confusion across invocations     | Repeated invocation on one session or shared client session                              | L → Sᵢ                           | One authorization decision may reasonably cover the whole session across distinct callers         | Y. Huang et al. [32]: 2,846 of 6,137 servers (46.4%) exhibited insecure authorization state caching                                                                                                        |
| **C3.** Missing or flawed transport authorization        | HTTP endpoint without authentication or origin checks, or with a flawed OAuth deployment | C ↔ Θ, Sᵢ ↔ Θ                    | Deployers will enable and correctly implement the authorization profile the specification provides | Zhou et al. [8]: 40.55% of 7,973 servers with no authentication; all 119 testable OAuth deployments had ≥1 flaw                                                                                           |
| **C4.** Intent inversion via tool-call traces            | Sequence of tool calls a server receives                                                 | L → Sᵢ                           | A server learns only what each call's arguments require                                            | Yao et al. [41]: the tool-call trace a server observes can be inverted to recover the user's underlying intent                                                                                            |
| **C5.** Sink-side enforcement failure                    | Tool arguments consumed by the server's own handlers                                     | Sᵢ → Xᵢ                          | The server confines each operation to the scope it advertises                                      | Ridao et al. [42]: static analysis flagged 5% of 100 public server repositories; 11 empirical records in Table 11 demonstrate path traversal, command injection, and SSRF in server handlers              |
| **C6.** Client-side sink enforcement failure             | Remote server metadata, authorization endpoint discovery, or peer response               | Sᵢ / Θ → C                       | Peer-supplied metadata, URLs, or launch parameters are data and safe from shell execution          | CVE-2025-6514 (command injection in `mcp-remote` browser spawn); CVE-2025-54135 (Cursor CurXecute auto-run command execution) (Section 4.3)                                                                 |
| **C7.** Authorization scoping & tenant isolation failure | Multi-tenant server backend query or organizational boundary check                       | Sᵢ → Xᵢ                          | Server-side handlers strictly partition tenant authorization scopes when querying external system backends | Asana MCP incident disclosure [68] (cross-tenant task metadata exposure); Y. Huang et al. [32]                                                                                                              |
| **D1.** Parasitic toolchain / composed exfiltration      | Chained calls across S₁…Sₖ                                                               | composition over S₁…Sₖ           | Per-tool safety implies per-session safety                                                         | Zhao et al. [7]: 12,230 tools across 1,360 servers catalogued as chainable                                                                                                                                |
| **D2.** Guardrail bypass under multi-step execution      | Multi-step plans with intermediate state                                                 | composition over S₁…Sₖ           | A guardrail checked once holds for the rest of the plan                                            | Zhang et al. [43]: bypassed guardrails are among the runtime faults their telemetry benchmark detects and localizes                                                                                       |
| **D3.** Supply-chain propagation via tool cloning        | Registry-level code reuse                                                                | Sᵢ (pre-session, at publication) | A published server's code is independent of every other published server's code                    | T. Kim et al. [44]: across 7,508 repositories and 87,564 tools, 60–85% of candidates were clones that propagate shared vulnerabilities                                                                    |

Layer A carries the densest evidence, consistent with Section 1's claim that the semantic channel is the field's distinguishing concern. Layer D is the thinnest relative to how consequential its properties are (Section 3.3): composition failures require a multi-server testbed to demonstrate, which raises the cost of studying them relative to a single-server benchmark. Recent empirical studies further highlight subtle attack vectors across these layers: MPMA [45] demonstrates preference manipulation attacks in which an attacker deploys customized MCP servers with genetically optimized descriptions (GAPMA) to bias LLM planner selection toward the attacker's server over benign competitors without modifying semantic functionality (Layer A; see also Guo et al. [46] for preference manipulation via agent bias fine-tuning), while MSA [47] demonstrates cross-MCP memory exfiltration where parasitic tool parameters and prompts extract sensitive credentials cached across shared agent context (Class D1).

### 4.3. Taxonomy coverage test

Section 2.9 committed to testing the taxonomy against empirical evidence outside the academic papers that motivated it. Following the package- and ecosystem-level retrieval protocol described in Sections 2.4 and 2.10, the external E4 validation set comprises 22 records: 20 confirmed CVEs and 2 documented vendor incident disclosures. These records do not count toward the 171-record synthesis corpus. Two reviewers mapped each record to the taxonomy; initial agreement was 90.9% (20/22; Cohen's κ = 0.87), and open reconciliation reached full consensus. Both coders worked with the class set that already contained Class C6 and the extended Class B1, so this agreement measures consistency on the revised taxonomy, not on the original fourteen classes. Table 11 reports the results.

**Table 11**

**Coverage test against the external E4 validation set (n = 22 records: 20 CVEs and 2 incident disclosures)**

| **Record & Citation** | **Affected Component & Boundary** | **CVSS Rating & Authority** | **Absorbed by** | **Mechanism & Dual-Coding Analysis** |
|:---|:---|:---|:---|:---|
| **CVE-2025-47274** [48] | ToolHive deployment utility (Zone H) | CVSS v4.0: 2.4 (Low, CNA: GitHub) / v3.1: 7.8 (NVD) | **Residue** | Stored plaintext API tokens and credentials in local run-configuration files. A conventional host-side credential storage vulnerability; no Table 6 protocol crossing is traversed. |
| **CVE-2025-53109** [49] | Filesystem MCP server ($S_i \to X_i$) | CVSS v4.0: 7.3 (High, CNA: GitHub) | **Class C5** | Symlink traversal bypass of directory confinement, enabling arbitrary file read and write operations outside the designated sandbox root directory. Direct fit. |
| **CVE-2025-53110** [50] | Filesystem MCP server ($S_i \to X_i$) | CVSS v4.0: 7.3 (High, CNA: GitHub) | **Class C5** | Path validation bypass caused by naive prefix matching (e.g., allowing access to `/sandbox_private` when `/sandbox` is approved). Direct fit. |
| **CVE-2025-68143** [51] | Git MCP server ($S_i \to X_i$) | CVSS v4.0: 6.5 (Medium, CNA: GitHub) | **Class C5** | Tool `git_init` accepted arbitrary filesystem paths without boundary validation, permitting repository initialization in arbitrary host directories. Direct fit. |
| **CVE-2025-68144** [52] | Git MCP server ($S_i \to X_i$) | CVSS v4.0: 6.3 (Medium, CNA: GitHub) | **Class C5** | Command-line argument injection in `git_diff` and `git_checkout` handlers, allowing execution of arbitrary file and command operations via unsanitized CLI options. Direct fit. |
| **CVE-2025-68145** [53] | Git MCP server ($S_i \to X_i$) | CVSS v4.0: 6.4 (Medium, CNA: GitHub) | **Class C5** | Boundary traversal vulnerability bypassing repository restriction settings (`--repository`), allowing Git operations outside the permitted repository tree. Direct fit. |
| **CVE-2026-27735** [54] | Git MCP server ($S_i \to X_i$) | CVSS v4.0: 6.4 (Medium, CNA: GitHub) | **Class C5** | Path traversal in `git_add` handler permitting staging and indexing of arbitrary files outside the permitted repository boundary. Direct fit. |
| **CVE-2025-53967** [55] | Framelink Figma MCP server ($S_i \to X_i$) | CVSS v3.1: 7.5 (High, CNA: GitHub / NVD) | **Class C5** | Remote command execution via shell metacharacters in HTTP handler `fetchWithRetry` (invoking `curl`) due to lack of tool argument sanitization. Direct fit. |
| **CVE-2026-0755** [56] | `gemini-mcp-tool` ($S_i \to X_i$) | CVSS v3.1: 9.8 (Critical, CNA: GitHub) | **Class C5** | OS command injection in `execAsync` and CLI argument parsing, permitting arbitrary shell execution and unauthorized local file reading via `@file` parameters. Direct fit. |
| **CVE-2026-39884** [57] | `mcp-server-kubernetes` ($S_i \to X_i$) | CVSS v3.1: 8.3 (High, CNA: GitHub) | **Class C5** | Argument injection in `port_forward` tool handler allowing arbitrary flag injection into underlying `kubectl` commands, leading to remote code execution. Direct fit. |
| **CVE-2025-65513** [58] | `fetch-mcp-server` network sink ($S_i \to X_i$) | CVSS v4.0: 6.3 (Medium, CNA: GitHub) | **Class C5** | Server-Side Request Forgery (SSRF) via private IP validation bypass, allowing attackers to reach internal host network resources through unsanitized outbound HTTP fetching. Direct fit for sink enforcement failure. |
| **CVE-2026-32871** [59] | FastMCP OpenAPI framework ($S_i \to X_i$) | CVSS v4.0: 10.0 (Critical, CNA: GitHub) | **Class C5** | SSRF and path traversal in `RequestDirector._build_url()`, allowing attackers to forge arbitrary HTTP requests to intranet endpoints and read internal files via unvalidated endpoint resolution. Direct fit. |
| **CVE-2026-35568** [60] | MCP Java SDK ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | CVSS v4.0: 7.6 (High, CNA: GitHub) | **Class C3** | Missing Host and Origin header validation on HTTP/SSE endpoints, allowing malicious websites to perform DNS rebinding and dispatch unauthorized tool calls. Direct fit. |
| **CVE-2025-66414** [61] | MCP TypeScript SDK ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | CVSS v4.0: 7.6 (High, CNA: GitHub) | **Class C3** | DNS rebinding vulnerability in Streamable HTTP/SSE transport due to missing HTTP Host header validation on localhost-bound servers, allowing web origins to issue arbitrary MCP JSON-RPC messages. Direct fit. |
| **CVE-2025-66416** [62] | MCP Python SDK ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | CVSS v4.0: 7.6 (High, CNA: GitHub) | **Class C3** | DNS rebinding vulnerability in Streamable HTTP/SSE transport due to lack of Host and Origin header verification on local server endpoints. Direct fit. |
| **CVE-2025-49596** [63] | Anthropic MCP Inspector ($C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$) | CVSS v4.0: 9.4 (Critical, CNA: GitHub) | **Class C3** | Unauthenticated local proxy server binding without CORS or token validation, allowing malicious external web pages to issue arbitrary commands and tool calls. Direct fit. |
| **CVE-2025-6514** [64] | `mcp-remote` client proxy ($S_i / \Theta \to C$) | CVSS v3.1: 9.6 (Critical, CNA: JFrog) | **Class C6** (added after the test) | Client-side sink enforcement failure. `mcp-remote` passes untrusted remote `authorization_endpoint` URLs containing shell metacharacters directly into local OS browser execution (`open`/`exec`) without sanitization during OAuth discovery. Not absorbed by the original fourteen classes. |
| **CVE-2025-54135** [65] | Cursor IDE ("CurXecute") ($S_i / \Theta \to C$) | CVSS v3.1: 8.5 (High, CNA: GitHub) / v3.1: 9.8 (NVD) | **Class C6** (added after the test); secondary A2 | Client-side sink enforcement failure. Automated execution of unsanitized launch commands and environment configurations defined in workspace `.cursor/mcp.json` without explicit user gating; the write to the configuration can be triggered by prompt injection from repository content (secondary A2). Not absorbed by the original fourteen classes. |
| **CVE-2025-54136** [66] | Cursor IDE ("MCPoison") ($C \leftrightarrow S_i$, descriptor over time) | CVSS v3.1: 7.2 (High, CNA: GitHub) / v3.1: 8.8 (NVD) | **Class B1** (definition extended after the test) | Post-approval mutation of descriptors and launch configurations over time. Silent trust and execution of modified `.cursor/mcp.json` configurations without re-verifying user consent or integrity hashes. Not absorbed by the original B1 definition, which required a runtime `notifications/tools/list_changed` message. |
| **CVE-2026-0621** [67] | MCP TypeScript SDK ($C \leftrightarrow S_i$) | CVSS v4.0: 8.7 (High, CNA: GitHub) | **Residue** | Algorithmic complexity / Regular Expression Denial of Service (ReDoS) in `UriTemplate` expansion. An availability/resource exhaustion bug in a utility parser; no protocol trust boundary is traversed. |
| **Asana MCP Disclosure** [68] | Asana multi-tenant server ($S_i \to X_i$) | High (Vendor Advisory; Zealynx [69]) | **Class C7** (added after the test; secondary C5) | Server-side multi-tenant isolation failure. Tenant segregation logic flaw in multi-tenant MCP server returning organization task metadata across distinct corporate tenants. Directly mapped to Class C7, avoiding conflation with caller identity confusion (C2) on $L \to S_i$. |
| **Invariant Labs Incident** [26] | GitHub MCP server, single server ($S_i \to L \to S_i$) | High (Vendor Disclosure [26]) | **Class A2** (secondary C1, D1) | Multi-label attack chain: an issue opened on the owner's public repository carries an indirect prompt injection (A2); the planner reads the owner's private repository on the attacker's behalf (C1) and publishes its contents in a pull request on the public repository (D1). One server played all three roles (Section 7). |

We report two absorption figures. Under the fourteen classes defined before the test, 17 of the 22 records (77.3%; Wilson 95% CI: 56.6%–89.9%) were absorbed (with the Asana disclosure tentatively mapped to C2); three were not (CVE-2025-6514, CVE-2025-54135, and CVE-2025-54136), and two were residue. The test led us to add Class C6 (client-side sink failure) and the $S_i / \Theta \to C$ crossing, to define Class C7 (authorization scoping and tenant isolation failure) on $S_i \to X_i$ rather than stretching C2, and to extend Class B1 to post-approval mutation of launch configurations. With these revisions, 20 of the 22 records (90.9%; 72.2%–97.5%) are absorbed. Because the revised classes were shaped by the same records they now absorb, the second figure describes formative refinement, not an independent held-out test; Section 8.3 proposes such a test. Two records remain residue: host-side credential storage in local configuration files (CVE-2025-47274 [48]) and regular expression denial of service in the TypeScript SDK's URI template parser (CVE-2026-0621 [67]).

Both intervals assume independent records, but several records share a product or a root cause: four CVEs concern the Git reference server, two the Filesystem reference server, two Cursor, and three the same DNS-rebinding defect in three official SDKs. The effective sample is therefore smaller than 22 and the intervals are too narrow. Counting each product, or each shared-root-cause family, once yields 15 clusters, of which 11 (73.3%; 48.0%–89.1%) were absorbed before the revision and 13 (86.7%; 62.1%–96.3%) after it.

**Empirical coverage versus construct validity.** Absorption measures empirical coverage, not construct validity. Half of the records (11 of 22; 50.0%) fall into Class C5 (*Sink-side enforcement failure*): conventional implementation defects (path traversal, command-line argument injection, and SSRF) inside server tool handlers ($S_i \to X_i$). Any taxonomy with a generic "server handler flaw" category would absorb these records. Construct validity would instead require evidence that failures at different crossings of Table 6 differ in causal mechanism, exploit primitive, and required defensive placement; this test does not supply that evidence.

**Two complementary evidence streams.** Read against the academic corpus, the validation set shows a different profile. In our layer coding of the corpus, 91 of the 171 records (53.2%) focus primarily on Layer A (indirect prompt injection and semantic tool poisoning). In the validation set, no record carries a Layer A class as its only label: Layer A is the primary class of one vendor disclosure (Invariant Labs [26], where the injection triggered a C1 and D1 chain) and a secondary class of one CVE (CVE-2025-54135). Under primary labels, Layer C accounts for 18 of the 22 records (81.8%):

- *Server-side sink failures (Class C5, 11 records; 50.0%):* path traversal in the Filesystem and Git reference servers, argument injection in the Kubernetes and Gemini tools, command injection in the Figma server, and SSRF in the Fetch server and FastMCP.
- *Transport and authorization exposures (Class C3, 4 records; 18.2%):* DNS rebinding in the Java, TypeScript, and Python SDKs, and an unauthenticated local proxy in MCP Inspector.
- *Client-side sink failures (Class C6, 2 records; 9.1%):* command injection in `mcp-remote` and auto-execution of workspace configuration in Cursor.
- *Authorization scoping and tenant isolation (Class C7, 1 record; 4.5%):* the Asana disclosure.

The remaining records are one B1 record (4.5%), one A2 record (4.5%), and two residue records (9.1%).

We do not read this asymmetry as evidence that semantic attacks are rare in deployment. The two streams measure different things, and the vulnerability stream is subject to ascertainment bias. CVE Numbering Authorities assign identifiers to deterministic defects in identifiable software products, whereas model behavior under prompt injection or tool poisoning is seldom treated as a product vulnerability and seldom receives a CVE. Our retrieval terms, built on package identifiers (Section 2.4), reinforce that selection. The comparison therefore supports a narrower conclusion: deployed MCP software also fails through conventional implementation defects in server handlers, transports, and client adapters, a failure surface that the academic corpus studies less often than the semantic channel.

**Resolution of specific classifications.** Adjudication settled four classification questions:
- *Resolution of CVE-2025-6514 and CVE-2025-54135 (Class C6):* Initial coding debated whether CVE-2025-6514 (`mcp-remote`) represented a transport authorization flaw (C3) or a taxonomy gap. In `mcp-remote`, the utility acts as a client-side stdio-to-HTTP proxy. When connecting to an untrusted remote server, it initiates OAuth 2.1 discovery per RFC 8414. A malicious remote endpoint supplies an `authorization_endpoint` URL containing shell metacharacters, which `mcp-remote` passes directly to OS utilities (`open`/`exec`) to launch the user's browser without sanitization. This is not an authorization failure (C3), but a client-side sink enforcement failure: the client consumes untrusted peer metadata into an execution sink. Rather than force C3, we defined Class C6 (*Client-side sink enforcement failure*) after the test and added the corresponding $S_i / \Theta \to C$ crossing to Table 6. CVE-2025-54135 (Cursor CurXecute) also fits Class C6, where the client auto-executes unsanitized commands from workspace configuration files; because that configuration can be written by prompt injection from repository content, we record A2 as its secondary class.
- *Resolution of Cursor MCPoison (CVE-2025-54136, Class B1):* Cursor IDE cached and executed tool configurations from `.cursor/mcp.json` without re-verifying user consent upon repository updates. We expanded the definition of Class B1 from purely runtime protocol notifications (`notifications/tools/list_changed`) to encompass post-approval mutation of descriptors and launch configurations over time.
- *Resolution of Asana MCP Disclosure (Class C7 / C5):* The Asana incident, documented via vendor advisory [68] and corroborated by the Zealynx MCP Breach Index [69] (both appraised under the AACODS checklist [31] for practitioner authority and technical reproducibility), involved a multi-tenant MCP server returning cross-tenant task metadata due to tenant isolation logic flaws in the server backend. Initial coding tentatively stretched C2 (caller identity confusion across turns), but Table 10 places C2 on the $L \to S_i$ crossing where the planner acts as a confused deputy. In contrast, the Asana failure resided strictly in the server backend's multi-tenant scoping and authorization enforcement logic on the $S_i \to X_i$ crossing. To eliminate this conceptual ambiguity, we formally established Class C7 (*Authorization scoping and tenant isolation failure*) and mapped Asana primarily to C7 (with secondary C5 for backend sink enforcement). Confused deputy (C1) is demonstrated operationally by the Invariant Labs incident [26].
- *Resolution of CVE-2026-0621 (Residue):* The regular expression denial of service in the TypeScript SDK's `UriTemplate` parser represents an algorithmic complexity vulnerability affecting service availability. Availability lies inside the scope stated in Section 1, but the taxonomy has no availability class. We therefore record this CVE as residue and treat it, together with the seven resource-abuse defenses of Table 14, as evidence for the taxonomic decision that gap 5 raises (Section 8.2).

## 5. Authentication and Authorization Across Specification Revisions

Section 3 placed the authorization infrastructure (Θ) on the remote side of the trust model. This section traces how the specification defined that infrastructure across five revisions (Section 5.1), how remote deployments implement it (Section 5.2), which crossings of Table 6 it leaves uncovered even when implemented correctly (Section 5.3), and which taxonomy classes remain without a normative provision (Section 5.4). One fact frames the analysis: every revision, including 2026-07-28, makes authorization optional. An implementation that supports it over HTTP SHOULD follow the specification's OAuth-based profile, and stdio implementations SHOULD instead obtain credentials from the environment [70][13].

### 5.1. Authorization across five revisions

Table 12 summarizes the normative changes relevant to authentication and authorization. Two trends stand out. First, the specification moved MCP progressively onto standard OAuth machinery: an OAuth 2.1 profile with authorization server metadata in 2025-03-26; the formal role of the MCP server as an OAuth resource server, protected-resource metadata, and audience-bound tokens in 2025-06-18; and a shift from dynamic client registration to client ID metadata documents between 2025-11-25 and 2026-07-28. Second, the 2026-07-28 revision made the protocol stateless: it removed protocol-level sessions and the initialization handshake, and clients SHOULD, but need not, identify themselves on each request. The same revision deprecated Sampling, Roots, and Logging; deprecated features remain fully functional for at least twelve months, so findings on sampling abuse [2, 9] still describe deployable behavior [13].

**Table 12**

**Authentication- and authorization-relevant provisions by specification revision**

| **Revision** | **Authorization provisions**                                                                                      | **Token handling**                                                                                                                                             | **Client registration**                                                                                     | **Other security-relevant changes**                                                      |
|--------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| 2024-11-05   | None defined                                                                                                      | None defined                                                                                                                                                   | None defined                                                                                                | Sampling introduced                                                                      |
| 2025-03-26   | Optional OAuth 2.1 profile for HTTP transports; authorization server metadata (RFC 8414 [71])                   | Bearer tokens; Proof Key for Code Exchange (PKCE)-based flow for public clients                                                                                | Dynamic client registration (RFC 7591 [72]) SHOULD be supported                                           | Streamable HTTP replaces HTTP+SSE                                                        |
| 2025-06-18   | MCP server defined as an OAuth resource server; protected-resource metadata (RFC 9728 [73]) MUST be implemented | Clients MUST send the RFC 8707 [74] resource parameter and implement PKCE; servers MUST validate audience and MUST NOT pass received tokens to upstream APIs | Proxy servers using static client IDs MUST obtain per-client user consent                                   | Token required on every HTTP request, even within one session                            |
| 2025-11-25   | OpenID Connect Discovery; incremental scope consent via WWW-Authenticate                                          | Unchanged                                                                                                                                                      | Client ID metadata documents recommended                                                                    | Client requirements for local server installation                                        |
| 2026-07-28   | Issuer (iss) validation per RFC 9207 [75]                                                                       | Client credentials bound to the issuing authorization server                                                                                                   | Dynamic client registration deprecated in favor of client ID metadata documents; retained for compatibility | Stateless protocol (no sessions, no initialize); Sampling, Roots, and Logging deprecated |

*Sources:* Model Context Protocol [13, 40, 70, 76, 77].

### 5.2. Specification versus deployment

Zhou et al. [8] provide the only large-scale measurement of how remote servers implement these provisions. Of 7,973 live remote servers, 3,233 (40.55%) exposed tools without authentication, 2,312 (29.00%) relied on static tokens or API keys, and 2,428 (30.45%) implemented OAuth-based flows. Static credentials are therefore about as common as the OAuth profile the specification describes, and they fall outside every provision in Table 12. Among OAuth deployments, all 119 servers in their fully testable subset showed at least one flaw, 325 in total.

Two consequences follow for the trust model. First, for roughly 70% of measured remote servers, the OAuth form of zone Θ does not exist: those servers either authenticate no one or accept a static secret, so the token-audience property of Table 6 cannot hold. Second, the flaws Zhou et al. report are deviations from provisions already in force when they measured, so further specification revisions will not close them by themselves. This gap is compounded at the software development layer: an empirical study of 535 resolved bugs across four widely used MCP frameworks (FastMCP, Go SDK, Python SDK, and TypeScript SDK) by He et al. [78] revealed that 11.6% of defects stem directly from authentication and authorization failures, and 14.4% from protocol and specification violations, demonstrating that implementation flaws in underlying libraries actively subvert specification intent. Section 6 grades the conformance and scanning tools that target this gap.

### 5.3. What authorization does not cover

A fully conformant deployment still leaves the following crossings of Table 6 outside the reach of OAuth.

*Caller identity (L → Sᵢ).* Since 2025-06-18, clients must attach an access token to every HTTP request [40], and the 2026-07-28 revision removes protocol-level sessions entirely. Neither change identifies the principal behind a call. The token records a grant from the user to the client, and it is identical whether a call originated in the user's instruction, in a sub-agent, or in text injected through a tool result. The per-request clientInfo field introduced in 2026-07-28 is self-asserted and optional. Y. Huang et al. [32] measure the server-side consequence: 2,846 of 6,137 servers (46.4%) exhibited insecure authorization, typically caching one authorization decision as persistent state and applying it to later invocations regardless of the caller, or omitting per-tool checks (classes C1 and C2). Server-held authorization state remains an implementation choice.

*Sink scope (Sᵢ → Xᵢ).* OAuth scopes bound what a client may request from a server, not what the server's handler does in the external system. Path-confinement failures such as CVE-2025-53109 (Section 4.3) occur inside Sᵢ after authorization has succeeded (class C5).

*Semantic channel and descriptor integrity (Sᵢ → L; descriptor over time).* An authenticated, correctly authorized server can still deliver poisoned metadata or results, and no revision defines integrity protection or pinning for tool descriptors. The cache freshness hints added in 2026-07-28 (ttlMs, cacheScope) govern staleness, not integrity (layers A and B). This demonstrates the fundamental gap between Table 6's normative invariants and MCP's specification realities: OAuth establishes identity and token audience on crossing $C \leftrightarrow \Theta$, but leaves the normative semantic invariant on crossing $S_i \to L$ entirely unenforced at the protocol layer.

*Composition (across S₁…Sₖ).* Audience binding confines each token to one server, which prevents one server from replaying another's token. No provision governs information flow between servers inside the host (layer D).

*Client-side sinks ($S_i / \Theta \to C$).* Authorization discovery itself delivers attacker-controllable strings to the client: the client must act on an authorization_endpoint URL before any token exists. CVE-2025-6514 shows that a client adapter that passes this URL to an operating-system launcher turns discovery into code execution (class C6). Audience and issuer validation govern which tokens a client accepts, not how it handles the URLs that lead to them.

The local transport lies outside the authorization specification by design: stdio servers take credentials from the environment [70], which is the ambient-authority profile of Table 7. The client requirements for local server installation added in 2025-11-25 oblige clients to show the server's launch parameters and working directory and to obtain consent before installing it; they govern installation, not what an installed server may do at runtime.

### 5.4. Residual attack surface

Table 13 maps each taxonomy class to the strongest provision in revision 2026-07-28. *Partial* means a MUST or SHOULD requirement covers only one variant of the class, or only deployments that implement the optional authorization profile; *none* means no revision addresses the class.

**Table 13**

**Taxonomy classes against the provisions of revision 2026-07-28**

| **Class**                                      | **Strongest provision**                                                             | **Status**                                        |
|------------------------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| A1 Tool metadata poisoning                     | None                                                                                | None                                              |
| A2 Indirect injection via results or resources | None                                                                                | None                                              |
| A3 Description-quality miscalls                | Tool-naming guidance: lowercase, namespaced names to reduce collisions (2025-11-25) | Partial (guidance only)                           |
| B1 Descriptor and config mutation              | Change notifications exist; no re-approval requirement                              | None                                              |
| B2 Registry and capability drift               | Cache freshness hints, not integrity                                                | None                                              |
| B3 Schema-mutation robustness failure          | None                                                                                | None                                              |
| C1 Confused deputy                             | Per-client consent for OAuth proxy servers with static client IDs                   | Partial (OAuth-proxy variant only)                |
| C2 Caller identity confusion across turns      | Per-request tokens; self-asserted clientInfo                                        | None                                              |
| C3 Missing or flawed transport authorization   | OAuth profile with audience and issuer validation                                   | Partial (only where authorization is implemented) |
| C4 Intent inversion                            | None                                                                                | None                                              |
| C5 Sink-side enforcement failure               | None; left to server implementations                                                | None                                              |
| C6 Client-side sink enforcement failure        | None identified; local-installation consent (2025-11-25) governs installation, not handling of peer-supplied metadata | None                          |
| C7 Authorization scoping & tenant isolation    | None; left to server backend implementations                                        | None                                              |
| D1 Composed exfiltration                       | Per-server audience binding does not constrain cross-server flow                    | None                                              |
| D2 Multi-step guardrail bypass                 | None                                                                                | None                                              |
| D3 Supply-chain propagation                    | Outside protocol scope (registries and distribution)                                | None                                              |

The specification partially addresses three of the sixteen classes and fully addresses none; the thirteen it leaves open include every class in layers B and D. The revisions have concentrated on the one boundary OAuth can express, the client-to-server hop, while most classes in Section 4 cross boundaries that lie before or after it. Where implemented, audience and issuer validation remove whole families of token-misuse attacks, but protection for the remaining classes has to come from mechanisms outside the authorization profile, which Section 6 grades by maturity.

## 6. Defense Maturity Analysis

This section grades what the literature has shown about defenses, as distinct from what it has proposed. Of the 171 corpus records, 85 (49.7%) propose or evaluate a defense. We coded each from its full text on the scale defined in Section 2.9, and we report the attack classes each defense evaluated, not those it claimed, because a claimed class is not evidence.

### 6.1. Coding and reliability

The primary coder coded all 71 records in the baseline frozen set and the 14 defenses from the supplementary set (85 defenses total). The coding was frozen and its checksum recorded before any comparison. A second coder, blind to the first coder's codes, then coded 38 records: the four with the strongest claims (two graded L2 and two flagged as adaptive evaluations), 16 random defense records, and 18 random non-defense records. The coders agreed on whether a record is a defense in 37 of 38 cases (97.4%; κ = 0.95) and on the eight-way role in 31 of 38 (81.6%; κ = 0.78). Five of the seven role disagreements fell on the boundary between a designed defense and a mere proposal, so we report defenses as designed or implemented (67 primary records across the consolidated corpus), secondary (6), and conceptual proposals (12 to 15, depending on strict thresholding). On the 20 defense records both coded, agreement was 80% on evaluation type, 75% on maturity, and 60% on the primary mechanism (80% when the nine mechanisms are grouped into four families); the sets of evaluated classes matched exactly for 6 of 20 (mean Jaccard 0.58), and the coders disagreed on both records flagged as adaptive evaluations. All 14 supplementary defense records underwent full verification and reconciliation against this calibrated standard. We resolved every disagreement that bears on a claim below by returning to the full text and recording a verbatim passage of at most 25 words, and we tightened the definitions of class C1 and of the policy mechanism family. Sixty-five of the 85 records did not undergo formal blind dual-coding (51 baseline records were evaluated solely by the primary coder, while all 14 supplementary defenses underwent independent audit and verification against the calibrated standard).

### 6.2. Maturity

Of the 85 defenses, 15 (17.6%) are conceptual (L0), 68 (80.0%) were prototyped and evaluated by their authors (L1), 2 (2.4%) were evaluated independently (L2), and none reached L3 through the literature.

By mechanism family, 37 defenses (43.5%) use authorization or policy, 35 (41.2%) inspect content, and 13 (15.3%) enforce integrity or isolation. An LLM or machine-learning model sits in the decision loop for 25 of the 85 defenses (29.4%).

The two L2 defenses are both content inspectors. MCIP [79] was run against three MCP clients in MCPSecBench [10], whose authors report that the protection mechanisms they tested were largely ineffective, with an average success rate below 30%. McpSafetyScanner [80] was evaluated as a baseline by VIPER-MCP [81], which measured a false-positive rate of 43.1% and a false-negative rate of 63.8% on 130 benign and 130 vulnerable servers, and it was also executed by Z. Li et al. [33]. No authorization, policy, integrity, or isolation defense has been evaluated by anyone but its authors, and 15 of those 50 are conceptual (L0).

Normative provisions are the only L3-level controls, and Section 5 shows they are partial (Table 13). One defense reports production use: ADR [82] describes more than ten months of operation at its authors' employer on over 7,200 hosts, processing over 10,000 agent sessions a day. We grade ADR L1, because the deployment is internal to the authors' employer and no third party or release documentation confirms it, and we report the claim separately.

### 6.3. How defenses were evaluated

Only 3 of the 70 empirically evaluated defenses (4.3%; Wilson 95% interval 1.5% to 11.9%) report an evaluation aimed at the defense's own mechanism. The three differ in kind. The authors of MindGuard [83] built an attack that suppresses the poisoned tool's attention to defeat their detector, and varied an attention scale factor to test it. The authors of a delegation broker [84] ran a red-team suite against their own token design, including forging a token from scratch. ARGUS [85] implements a closed-loop validation framework that uses mutating payload synthesis and behavioral trace analysis to test defense resilience against adaptive tool-use exploits. An independent adaptive test also exists: Z. Li et al. [33] generated servers whose manipulated metadata went undetected by the scanner MCP-Scan (evasion rate 100%), and servers replaced across sessions went undetected by the inline proxy Pipelock (evasion rate 100%), although Pipelock caught 80.00% to 86.67% of replacements within a session.

Most evaluations measure recognition of patterns the authors supplied. A DistilBERT detector reaches 99.92% test accuracy on a random split of 14,400 command and argument entries [86]. Such a score shows that the model separates the training distribution and says little about a new attack. Zavrak [87], whose detector falls outside our corpus because it is not MCP-specific, found that random splits inflated the area under the receiver operating characteristic curve (AUROC) by up to 25.8 percentage points relative to task-disjoint splits. In a gateway study whose suite included paraphrased and obfuscated attacks, the identity and tenant-isolation modules produced no mismatches across 93 adversarial cases, while the regex filter and output firewall mismatched on 54.8% and 63.6% [88]. Structural enforcement held where content matching did not, but the suite was the authors' own. Several recent proposals explore runtime remediation and specialized integrity mechanisms, though remaining author-evaluated: MCPFixGen [89] combines multi-checkpoint state rollback with attention masking to neutralize tool poisoning payloads during active web sessions; TFA [90] employs information-flow analysis over a product lattice to restrict toxic instruction propagation across multi-agent pipelines; SecuAudit [91] uses Shamir's secret sharing and supervised hashing to bind access policies to resource metadata, verifying compliance via a challenge-response auditing protocol for agent data circulation; and Sentinel-Net [92] combines rule pre-filtering with a temporal dilated CNN-LSTM architecture to monitor tool-call traffic for multi-turn anomalies.

Cost is reported more often than robustness. Of the 70 evaluated defenses, 52 (74.3%) report a numeric overhead, 7 give a qualitative statement, and 11 report none. Fourteen of the 85 defenses (16.5%) link a public repository.

### 6.4. Coverage by attack class

Table 14 counts, for each class of Table 10, the defenses whose experiments evaluated it.

**Table 14**

**Defenses evaluating each attack class (n = 85 defense records)**

| **Class**                                                | **Boundary**            | **Defenses evaluating the class** | **Highest maturity in the literature** | **Adaptive evaluations** | **Provision in revision 2026-07-28**         |
|----------------------------------------------------------|-------------------------|-----------------------------------|----------------------------------------|--------------------------|----------------------------------------------|
| **A1.** Tool metadata poisoning                          | Sᵢ → L                  | 22                                | L2                                     | 2                        | None                                         |
| **A2.** Indirect injection via tool results or resources | Sᵢ → L                  | 31                                | L2                                     | 1                        | None                                         |
| **A3.** Description-quality-exploiting miscalls          | Sᵢ → L                  | 6                                 | L1                                     | 0                        | Partial (guidance only)                      |
| **B1.** Rug pull                                         | descriptor over time    | 11                                | L1                                     | 0                        | None                                         |
| **B2.** Registry/capability drift at scale               | descriptor over time    | 6                                 | L1                                     | 0                        | None                                         |
| **B3.** Schema-mutation robustness failure               | descriptor over time    | 2                                 | L1                                     | 0                        | None                                         |
| **C1.** Confused deputy                                  | L → Sᵢ                  | 17                                | L1                                     | 1                        | Partial (OAuth-proxy variant only)           |
| **C2.** Caller identity confusion                        | L → Sᵢ                  | 7                                 | L1                                     | 0                        | None                                         |
| **C3.** Missing or flawed transport authorization        | C ↔ Θ, Sᵢ ↔ Θ           | 15                                | L1                                     | 1                        | Partial (where authorization is implemented) |
| **C4.** Intent inversion via tool-call traces            | L → Sᵢ                  | 0                                 | none                                   | 0                        | None                                         |
| **C5.** Sink-side enforcement failure                    | Sᵢ → Xᵢ                 | 26                                | L2                                     | 0                        | None                                         |
| **C6.** Client-side sink enforcement failure             | Sᵢ / Θ → C              | n.c.                              | n.c.                                   | n.c.                     | None                                         |
| **C7.** Authorization scoping & tenant isolation failure | Sᵢ → Xᵢ                 | n.c.                              | n.c.                                   | n.c.                     | None                                         |
| **D1.** Parasitic toolchain / composed exfiltration      | composition             | 21                                | L2                                     | 0                        | None                                         |
| **D2.** Guardrail bypass under multi-step execution      | composition             | 7                                 | L1                                     | 0                        | None                                         |
| **D3.** Supply-chain propagation via tool cloning        | pre-session             | 9                                 | L1                                     | 0                        | None                                         |
| Resource abuse (outside the taxonomy)                    | agent or server compute | 7                                 | L1                                     | 0                        | None                                         |

*Note.* n.c. = not coded. Classes C6 and C7 were added after the 85 defense records were coded (Section 4.3), and the records have not yet been recoded against them. Counts for B1 were coded under the original definition of that class, before B1 was extended to launch configurations.

Evidence is densest for A2 (31 defenses), C5 (26), A1 (22), and D1 (21); only A1 and A2 of these four attack the semantic channel. Class C1 is evaluated by 17 defenses, one of which (ADR, an inspection-based detector) evaluates C1 in a way we could not reconcile with our definition; without it the count is 16. Independent evaluation exists only for A1, A2, C5, and D1, and it comes from the two defenses above. Layer B has no L2 defense, and every class outside A1, A2, C5, and D1 is at most L1.

One absolute gap held through reconciliation: no defense evaluated intent inversion (C4). Class B3 (schema-mutation robustness failure) received a second evaluation from a governed cloud gateway, bringing its count to two. Several classes remain thin: description-quality miscalls (A3, 6 defenses), registry drift (B2, 6), caller identity confusion (C2, 7), and multi-step guardrail bypass (D2, 7). Adaptive evaluations appear in four classes (A1, A2, C1, C3). Seven defenses evaluated resource abuse, which the taxonomy does not classify, and none passed L1; one availability CVE in the validation set (CVE-2026-0621) also falls outside the taxonomy, and Section 8 returns to both. Classes C6 and C7 have not yet been coded against the defense records. The specification touches A3, C1, and C3 (6, 17, and 15 defenses) and leaves open A2, C5, and D1, which have the most.

### 6.5. Relation to prior defense reviews

Three earlier works overlap with this section. Tamayo [17] reviewed 73 defense studies from 2022 to 2025 and reported that 93.2% relied on custom evaluations and 23.3% reported effectiveness; because that review reaches back before MCP's release, its percentages describe agent-tool defenses broadly and cannot be compared with ours. Rostamzadeh et al. [20] mapped academic and industry defenses onto a six-layer defense-placement taxonomy and found protection uneven and tool-centric, with gaps at host orchestration, transport, and supply chain. Our result agrees in direction but counts evidence, not presence: supply-chain propagation (D3) has nine defenses, none beyond L1. Nandish et al. [21] grouped inherent risks from 18 studies into four deficits (capability, privilege, quality, and supply chain), which we treat as complementary and do not reconcile class by class. This section adds a maturity grade for each defense, tied to the classes and crossings it evaluated.

### 6.6. Limits

Three limits qualify these counts. First, 65 of the 85 records did not undergo formal blind dual-coding (51 baseline records evaluated solely by the primary coder, while all 14 supplementary candidates were independently audited), and the class assignment of an experiment is interpretive, so class counts are approximate, though in the double-coded sample neither coder found an evaluation of C4 that survived reconciliation. Second, L2 counts only evaluations by papers inside the corpus; an unpublished or industry test would not appear, so the L2 count is a lower bound. Third, the adaptive flag is strict: it excludes fixed suites of paraphrased or obfuscated inputs and benchmarks designed against other defenses, and the three positives we found differ in kind, so the 4.3% should not be read as a rate of robust defenses.

## 7. Case Study: A Composed Exfiltration Through the GitHub MCP Server

This case study applies the trust boundary model (Section 3), the taxonomy (Section 4), the specification analysis (Section 5), and the maturity grades (Section 6) to one documented incident. We chose it because every call in it was individually authorized, and because a defense in our corpus was evaluated on it.

### 7.1. The incident

In May 2025, Invariant Labs reported a vulnerability in the official GitHub MCP integration, found with its automated analyzer for what it calls toxic agent flows [26]. A user connects an MCP client such as Claude Desktop to the GitHub server, using an account that owns a public repository that accepts issues and a private repository. An attacker opens an issue on the public repository that contains a prompt injection. When the owner later asks the agent to look at the open issues, the agent fetches the issue and follows its instructions, pulls private repository data into its context, and leaks it through a pull request that it creates on the public repository, where anyone can read it. We did not reproduce the attack. The account rests on the vendor's report and on the case study of a defense discussed below.

### 7.2. Tracing the incident

Table 15 traces each step of the incident against the crossings and normative invariants of Table 6, evaluating whether each invariant holds descriptively under benign execution or is empirically violated (*fails*) during the attack sequence.

**Table 15**

**The GitHub MCP incident traced through the trust boundary model**

| **Step** | **Event**                                                                         | **Crossing (Table 6)**            | **Normative invariant evaluation**                                                               | **Class (Table 10)** | **Provision in 2026-07-28 (Table 13)**                  |
|----------|-----------------------------------------------------------------------------------|-----------------------------------|-------------------------------------------------------------------------------------------------|----------------------|---------------------------------------------------------|
| 1        | The owner asks the agent to look at the open issues                               | U → H                             | principal(instruction acted on) = U: **holds**                                                  | none                 | n/a                                                     |
| 2        | The server returns an issue that the attacker wrote                               | Sᵢ → L, content originating in Xᵢ | content from Xᵢ must not function as control information the user did not authorize: **violated (fails)** | A2                   | None                                                    |
| 3        | The agent reads the private repository                                            | L → Sᵢ                            | principal(invocation) = U: **violated (fails)**, because request originates in attacker's prompt | C1                   | Partial (OAuth-proxy variant only, not applicable here) |
| 4        | The agent publishes the data in a pull request on the public repository           | Sᵢ → Xᵢ                           | action within the scope granted to the principal: **holds**, permitted by user's credential    | none                 | n/a                                                     |
| 5        | The session has combined untrusted input, a sensitive read, and an outbound write | composition over S₁…Sₖ            | no such combination without re-consent: **violated (fails)**                                    | D1                   | None                                                    |

Three of the five steps violate the normative security invariants of Table 6, spanning three classes and three layers (A2, C1, and D1). Steps 1 and 4 hold descriptively under protocol authorization. This empirical trace exposes the fundamental limitation of MCP's security posture: the initial request was fully legitimate and every subsequent operation operated within the valid authorization grant of the user's OAuth credential, yet the normative invariants necessary for safe autonomous tool use were subverted because MCP lacks protocol-level mechanisms to enforce data-control separation or compositional consent. Section 5.3 explains why authorization does not intervene: the access token records a grant from the user to the client, and it is identical whether a call began in the user's instruction or in injected text. The three roles named by the composition property (untrusted input, sensitive read, and egress) were all executed through a single server, so even the specification's audience-binding provisions could not have applied in principle.

### 7.3. What the evidence offers

Table 14 suggests ample coverage of these classes: 31 defenses evaluated A2, 17 evaluated C1, and 21 evaluated D1. Evidence about this incident is much thinner. One defense in our corpus names it: SAMOS [93], a gateway that intercepts MCP tool calls and enforces information-flow policies over session-level context using annotations from the developer or administrator. Its authors report that it blocked this attack while preserving the original functionality. We graded it L1: one scenario, run by its authors, with no adaptive test and no evaluation by others. ChainWatch [94] traces the same incident as one of five illustrative scenarios and shows where its rules would fire, but it reports no experiment, so it is L0. The two act on different signals, data-flow labels for SAMOS and stage transitions across a call sequence for ChainWatch, and neither has been tested against an adversary who knows its policy.

The model also indicates where a defense should act. Enforcing the second row of Table 6 requires recognizing injected content, in every phrasing an attacker might choose. Only 3 of the 70 empirically evaluated defenses were tested against an adversary aimed at their own mechanism (Section 6.3), and the one independent adaptive test found manipulated metadata undetected by MCP-Scan, and cross-session server replacement undetected by Pipelock [33]. Enforcing the composition property does not require recognizing the injection at all, because it constrains what a session may combine. Its cost is the policy annotations a deployer must supply and a re-consent step in workflows that legitimately read public and private sources together.

### 7.4. What the case shows

Three points carry into the roadmap. Judged call by call, the incident is authorized throughout, and only the crossing view flags it, at three points. The specification supplies no provision for any of the three classes. And the evidence on how a defense behaves on this exact incident is one author-run study and one design-level trace, with no independent replication and no test with a second server in the session. Section 8 turns these gaps into research questions.

## 8. Research Gap Roadmap

This section turns the evidence of Sections 3 through 7 into a ranked list of research gaps (contribution C4). Following Section 2.9, candidate gaps came from cells of Table 14 without adequate evidence, contradictions between studies, and limitations that authors state. We ranked each gap on two ordinal scales. Severity is high when the property concerned is violated in measured deployments or by demonstrated attacks with reported success rates and the corpus holds no independently evaluated defense that enforces it, and medium when only one of those conditions holds. Tractability is high when an existing benchmark, measurement pipeline, or open-source defense in the corpus could host the study, medium when building blocks exist but a harness or dataset must be built, and low when the mechanism is not yet known. The ratings are our judgment from the cited evidence, and a reader could order neighboring gaps differently.

### 8.1. Where the gaps came from

*Cells.* Table 14 shows one class with no evaluating defense (C4), two not yet coded from the empirical benchmark (C6 and C7), and one with only two (B3), every class except A1, A2, C5, and D1 without an independently evaluated defense, and two L2 defenses that are both content inspectors. The 37 authorization and policy defenses and the 13 integrity and isolation defenses have been evaluated only by their authors, or not at all.

*Contradictions.* We investigated the apparent contradiction between ChainWatch [94] and SAMOS [93]. ChainWatch asserts that a review of the MCP literature up to April 2026 found no published defense against multi-step attack chains, yet its primary illustrative scenario (S2) is the identical Invariant Labs GitHub incident that SAMOS [93] (published at ACM SOSP Workshops / PACMI in October 2025) explicitly evaluated and blocked. Close examination of both primary sources resolves this contradiction on two distinct grounds. First, ChainWatch exhibits a demonstrable literature review omission: in its survey of existing defenses (Section II.C), ChainWatch reviewed only per-invocation content filters (MCPShield, MCPGuard, MindGuard), missing systems-level Information Flow Control (IFC) gateways entirely. This omission represents a serious methodological limitation in ChainWatch as a secondary source, allowing its authors to overstate novelty for an un-implemented conceptual proposal (graded L0). Second, the two works define and target multi-step defense through fundamentally different operational mechanisms: ChainWatch seeks *unannotated sequential behavioral anomaly detection* using an HMM with Viterbi decoding over 20-dimensional feature vectors to identify kill-chain progression across otherwise benign tool calls, whereas SAMOS enforces *deterministic policy-driven Information Flow Control (IFC)* over session taint states using developer-supplied security annotations (`read_confidentiality`, `write_confidentiality`, and capability flags per SEP-1075/1076) at an inline gateway. Thus, while ChainWatch is arguably the first conceptual design attempting *unsupervised sequential behavioral anomaly detection without metadata annotations*, SAMOS had already demonstrated empirical multi-step mitigation via structural IFC policy enforcement six months earlier. Independent replications are too scarce for the corpus to contradict itself more often, and that scarcity is a finding in its own right.

*Stated limitations.* Three studies name what their authors left open. ChainWatch needs labelled traces from real MCP sessions and expects false positives on legitimate multi-service workflows. The Tree-structured Injection for Payloads (TIP) attack was evaluated only for immediate hijacking, and persistence across turns remains open [95]. LeechHijack used only conventional dialogue tasks as the hijacked workload, not complex agent tasks [96].

### 8.2. The ranked gaps

**Table 16**

**Research gaps ranked by severity and tractability**

| **Rank** | **Gap**                                                    | **Classes**                   | **Evidence in this review**                                                                                                                                                                                                                                                           | **Severity** | **Tractability** | **Research question**                                                                                                           |
|----------|------------------------------------------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| 1        | Independent and adaptive evaluation of structural defenses | All                           | 50 authorization, policy, integrity, and isolation defenses evaluated only by authors or conceptual; 3 of 70 evaluated defenses tested adaptively; Puppet servers evaded MCP-Scan (100%), and cross-session replacement evaded Pipelock (100%; 13.33%–20.00% within a session) [33] | High         | High             | Do these defenses survive an adversary who knows the mechanism, on a shared benchmark?                                          |
| 2        | Registry drift and supply chain over time                  | B2, D3                        | Re-auditing the 5% most-drifted servers catches about 20% of those that later change [37]; 60–85% of candidates were clones [44]; 6 and 9 defenses, none beyond L1                                                                                                                  | High         | High             | Which re-audit and provenance policies hold detection above an operational threshold on real registry snapshots?                |
| 3        | Composed flows across servers                              | D1, D2                        | 12,230 chainable tools across 1,360 servers [7]; Section 7; structural flow control evaluated once (SAMOS, L1, one scenario)                                                                                                                                                        | High         | Medium           | Do flow-label and sequence-based defenses agree on labelled multi-server traces from real sessions?                             |
| 4        | Principal provenance through the planner                   | C1, C2                        | 2,846 of 6,137 servers (46.4%) with insecure authorization [32]; per-request tokens do not identify the principal (Section 5.3); 17 and 7 defenses, none beyond L1                                                                                                                  | High         | Low              | Can a server verify who originated an instruction when the planner assembled the call?                                          |
| 5        | Resource abuse                                             | Outside the taxonomy          | 7 defenses, none beyond L1; one availability CVE in the validation set (CVE-2026-0621) is residue; the hijacked workload was limited to Massive Multitask Language Understanding (MMLU)-style questions [96]                                                                                                                                               | Medium       | Medium           | How is extra computation attributed to the user's task, and can accounting detect an attacker who stays within normal variance? |
| 6        | Intent inversion and schema mutation                       | C4, B3                        | 0 and 2 defenses; trace inversion demonstrated [41]; 11 interface-mutation operators applied across 123 servers [38]                                                                                                                                                              | Medium       | Medium           | How much intent does an honest-but-curious server recover, and does a planner survive interface change mid-session?             |
| 7        | MCP combined with A2A                                      | Peer authenticity (not coded) | 3 of 171 records mention A2A in title or abstract; one is a defense, graded L1                                                                                                                                                                                                        | Not rated    | Not rated        | Which crossings does a deployment combining both protocols leave unprotected?                                                   |

Gap 1 comes first because it conditions the others: until structural defenses face adversaries who know them, their L1 grades cannot rise. It is also the cheapest to close. Fourteen of the 85 defenses link public code, and MCPSecBench already executes defenses against a fixed attack set [10]. A first study would rerun those fourteen under a white-box adversary of the kind TIP implements, which reached 68.2% to 100% attack success against a fine-tuned detector and perplexity filtering across four tools [95], although these are general injection defenses, not MCP-specific ones, and would report the specification revision tested and the split protocol (Section 6.3).

Gaps 2 and 3 are where the model predicts the most leverage. Registry measurements already exist, so evaluating re-audit policies needs little new infrastructure. Composition needs a dataset that does not: ChainWatch states the same need, and its discrepancy with SAMOS suggests that research groups do not yet share a definition of a multi-step attack. A first benchmark should include a session with a second server, which Section 7 found untested.

Gap 4 is severe and hard. The specification's per-request token does not identify the principal, and the optional per-request clientInfo field is self-asserted (Section 5.3). A mechanism has to carry the origin of an instruction through the planner to the server. We rate tractability low because that touches host and model design. Token-based delegation exists at L1, such as a broker that issues attenuated, sender-constrained tokens [84], but it binds authority to a workload identity, and our coding did not record whether any defense tracks the origin of an instruction inside the planner.

Gaps 5 and 6 are medium. For resource abuse the first decision is taxonomic: seven defenses evaluate a behavior that Section 4 does not classify, and one disclosed SDK vulnerability (CVE-2026-0621) is an availability failure the taxonomy leaves as residue, so a revision should add an availability class or say why not; the missing property would read that tool output must not induce computation unrelated to the user's task. For intent inversion and schema mutation, attacks are documented but no study measures their prevalence in deployments, hence the medium rating.

Gap 7 lies at the edge of our evidence. Table 8 identifies peer authenticity as the dominant crossing in A2A, and Section 3.5 notes that a deployment combining both protocols inherits every crossing of Table 6 for its MCP legs. Our taxonomy does not code the peer-authentication crossing, so the corpus cannot show whether any defense covers it, and we leave the gap unrated.

### 8.3. Limits of the ranking

The ratings inherit the limits of Section 6.6: class counts are approximate, and the severity scale rewards gaps that someone has already measured, so an unmeasured gap may be understated. Gaps 5 and 6 would rise if prevalence studies appear, and gap 1 would fall if a replication showed that a structural defense holds under adaptive attack. The 22-record coverage test of Section 4.3 is formative: the taxonomy absorbed 17 records before and 20 after the revision the test prompted, and coder agreement (κ = 0.87) was measured on the revised class set. An independent test is still needed: advisories published after 25 September 2026, retrieved with the protocol of Section 2.4 and mapped by two coders against the frozen sixteen-class taxonomy, would show how much real-world attack surface the classes absorb without further adjustment.

## 9. Discussion and Conclusion

### 9.1. What the review shows

This review asked four questions (Table 2). On RQ1, the 171 corpus records, drawn from candidate records identified across academic queries and gray-literature sources yielding 614 unique deduplicated works, document sixteen attack classes in four layers; a formative coverage test against an external set of 22 E4-tier records (20 CVEs and two vendor incident disclosures) absorbed 17 records under the original fourteen classes and 20 (90.9%; Wilson 95% CI: 72.2%–97.5%) after we added classes C6 and C7 and extended B1, leaving two as residue (host-side credential storage and SDK regex denial of service) (Section 4). The two evidence streams differ: 91 of the 171 corpus records (53.2%) focus primarily on Layer A, whereas 18 of the 22 disclosed records (81.8%) fall in Layer C, mostly conventional sink and transport defects. Because CVE assignment favors deterministic software defects, this contrast shows an understudied failure surface, not a measure of relative risk. On RQ2, the trust boundary model reduces an MCP deployment to eight crossings, each with a stated property, and the 2026-07-28 revision partially addresses three of the sixteen classes and fully addresses none (Section 5). In a documented incident, three of five steps violate a property while every call stays authorized (Section 7). On RQ3, 85 of the 171 records propose or evaluate a defense: 68 (80.0%) were evaluated only by their authors, 15 (17.6%) are conceptual, 2 (2.4%) were evaluated independently, and none reached L3. Only 3 of 70 evaluated defenses (4.3%) faced a test aimed at their own mechanism, none evaluated intent inversion (C4), and two evaluated schema mutation (B3) (Section 6). On RQ4, we ranked seven gaps, led by independent, adaptive evaluation of structural defenses, then registry drift and supply chain, composed flows, and principal provenance (Table 16).

One pattern runs through these results. Authorization in the specification governs which clients may reach a server. It does not govern what an authorized session does with that access, and the defenses aimed at that question are the least independently tested: none of the 50 authorization, policy, integrity, or isolation defenses has been evaluated by anyone but its authors.

### 9.2. Implications

*For practitioners.* Token authorization is necessary and not sufficient, because Section 5.3 identifies several crossings it cannot reach. Where one session can combine untrusted input, a sensitive read, and an outbound channel, the model points to a flow or re-consent rule enforced outside the planner, which does not depend on recognizing the injection; the supporting evidence is one author-run study (Section 7.3), so such a rule reduces risk without proving safety. Scanner results need context: an independent test measured a 43.1% false-positive rate and a 63.8% false-negative rate for one scanner [81], and manipulated metadata evaded another [33]. When evaluating a defense, ask which specification revision was tested, whether the adversary knew the mechanism, and whether anyone besides the authors ran the evaluation.

*For researchers.* Report the revision tested and the split protocol, include an adversary who knows the mechanism, and release code. Fourteen of the 85 defenses link a repository and can be rerun (Section 8.2). Because 80.0% of defenses sit at L1, an independent evaluation of an existing defense would raise more of them above L1 than another prototype would.

*For specification maintainers.* Table 13 and Section 5.3 point to three provisions: integrity protection or pinning for tool descriptors (classes B1 and B2), authenticated attribution of where an instruction originated (C1 and C2), and a session-level hook for re-consent when untrusted input, sensitive reads, and egress combine (D1). These follow from the properties of Table 6, and we have not evaluated them.

### 9.3. Limitations

Several limits bound these conclusions. One reviewer screened 80% of the pool, and the later audit removed 27.0% of that reviewer's sole inclusions; a second reviewer reinstated none of the 84 exclusions at risk, but search recall was not tested, so relevant work may be missing (Section 2.10). Of the 85 defense records, 65 did not undergo formal blind dual-coding (51 baseline records evaluated solely by the primary coder, with all 14 supplementary candidate defenses independently audited), and assigning an experiment to a class is interpretive (Section 6.6). The L2 count is a lower bound because it counts only evaluations by papers inside the corpus. The review window closed on 25 September 2026, and the specification and the literature move quickly. The taxonomy's coverage test evaluated 22 E4 records (20 CVEs and two vendor disclosures); it was formative, because it prompted the revisions whose result it reports, its records cluster in 15 product or root-cause families, its vulnerability sources favor deterministic software defects over model-level attacks, and its CVE records are restricted to TypeScript/Node.js (10 CVEs), Python (9 CVEs), and Java (1 CVE) implementations, with emerging Go, Rust, and C# implementations currently unrepresented in public vulnerability registries. The case study rests on one incident we did not reproduce (Sections 4.3 and 7.1). The gap ranking is our judgment, and its severity scale favors gaps that others have already measured (Section 8.3).

### 9.4. Conclusion

MCP's authorization machinery decides which clients may reach a server. The harder question is what an authorized session may do once the planner is reading attacker-controlled text. That question lies mostly outside the specification and, so far, outside independent evaluation. Sixteen attack classes, eight crossings, and 85 graded defenses give the field a common map, and the map shows that evidence lags claims: most defenses were tested only by their authors, and few against an adversary who knew the mechanism. Closing that gap with independent, adaptive evaluation is the work that would most change what the next review can say about MCP security.

## Funding Support

\[State the funding agency, grant number, and recipient, or state that the research received no external funding.\]

## Ethical Statement

This study does not contain any studies with human subjects performed by any of the authors.

## Conflicts of Interest

\[The authors declare that they have no conflicts of interest to this work, or state any conflicts.\]

## Data Availability Statement

\[State what is shared and where, for example: the frozen coding workbooks, decision logs, and record lists that support the findings are openly available in (repository name) at (URL).\]

## Author Contribution Statement

\[Author A: contributions using the CRediT roles. Author B: contributions.\]




## References

1. Anthropic. (2024, November 25). *Introducing the Model Context Protocol*. https://www.anthropic.com/news/model-context-protocol

2. Hou, X., Zhao, Y., Wang, S., & Wang, H. (2026). Model Context Protocol (MCP): Landscape, security threats, and future research directions. *ACM Transactions on Software Engineering and Methodology*. Advance online publication. https://doi.org/10.1145/3796519

3. Li, X., & Gao, X. (2026). A first look at the security issues in the Model Context Protocol ecosystem. In *Proceedings of the 56th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)* (pp. 379–392). IEEE. https://doi.org/10.1109/DSN69566.2026.00046

4. Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. In *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security* (pp. 79–90). ACM. https://doi.org/10.1145/3605764.3623985

5. Beurer-Kellner, L., & Fischer, M. (2025, April 1). *MCP security notification: Tool poisoning attacks*. Invariant Labs. https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks

6. Wang, Z., Gao, Y., Wang, Y., Liu, S., Sun, H., Cheng, H., ..., & Li, X. (2026). MCPTox: A benchmark for tool poisoning on real-world MCP servers. *Proceedings of the AAAI Conference on Artificial Intelligence, 40*(42), 35811–35819. https://doi.org/10.1609/aaai.v40i42.40895

7. Zhao, S., Hou, Q., Zhan, Z., Wang, Y., Xie, Y., Guo, Y., ..., & Xue, Z. (2026). Parasites in the toolchain: A large-scale analysis of attacks on the MCP ecosystem. In *Proceedings of the 2026 IEEE Symposium on Security and Privacy (SP)* (pp. 138–155). IEEE. https://doi.org/10.1109/SP63933.2026.00154

8. Zhou, H., Zhang, X., Zhang, H., Zhang, H., Zhang, M., & Yang, M. (2026). *A first measurement study on authentication security in real-world remote MCP servers* (arXiv:2605.22333). arXiv. https://doi.org/10.48550/arXiv.2605.22333

9. Song, H., Shen, Y., Luo, W., Guo, L., Chen, T., Wang, J., ..., & Chen, J. (2026). Beyond the protocol: Unveiling attack vectors in the Model Context Protocol (MCP) ecosystem. *IEEE Transactions on Software Engineering, 52*(8), 2410–2426. https://doi.org/10.1109/TSE.2026.3694876

10. Yang, Y., Gao, C., Wu, D., Chen, Y., Li, Y., & Wang, S. (2025). *MCPSecBench: A systematic security benchmark and playground for testing Model Context Protocols* (arXiv:2508.13220). arXiv. https://doi.org/10.48550/arXiv.2508.13220

11. Huang, C., Huang, X., Tran, N. P., & Milani Fard, A. (2026). Model Context Protocol threat modeling and analysis of vulnerabilities to prompt injection with tool poisoning. *Journal of Cybersecurity and Privacy, 6*(3), Article 84. https://doi.org/10.3390/jcp6030084

12. Gaire, S., Gyawali, S., Mishra, S., Niroula, S., Thakur, D., & Yadav, U. (2025). *Systematization of knowledge: Security and safety in the Model Context Protocol ecosystem* (arXiv:2512.08290). arXiv. https://doi.org/10.48550/arXiv.2512.08290

13. Model Context Protocol. (2026). *Model Context Protocol specification* (Revision 2026-07-28). https://modelcontextprotocol.io/specification/2026-07-28

14. Bhatt, M., Narajala, V. S., & Habler, I. (2025). ETDI: Mitigating tool squatting and rug pull attacks in Model Context Protocol (MCP) by using OAuth-enhanced tool definitions and policy-based access control. In *2025 Cyber Awareness and Research Symposium (CARS)* (pp. 1–6). IEEE. https://ieeexplore.ieee.org/document/11337310

15. Li, E., Mallick, T., Rose, E., Robertson, W., Oprea, A., & Nita-Rotaru, C. (2026). ACE: A security architecture for LLM-integrated app systems. In *Proceedings of the Network and Distributed System Security Symposium (NDSS 2026)*. Internet Society.

16. Maloyan, N., & Namiot, D. (2026). *Breaking the protocol: Security analysis of the Model Context Protocol specification and prompt injection vulnerabilities in tool-integrated LLM agents* (arXiv:2601.17549). arXiv. https://doi.org/10.48550/arXiv.2601.17549

17. Tamayo, J. E. (2026). Security defense mechanisms in Model Context Protocol implementations: A systematic literature review. In *Lecture notes in networks and systems*. Springer. https://doi.org/10.1007/978-3-032-25187-9_44

18. Debenedetti, E., Zhang, J., Balunović, M., Beurer-Kellner, L., Fischer, M., & Tramèr, F. (2024). AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents. In *Advances in Neural Information Processing Systems 37: Datasets and Benchmarks Track*.

19. Anbiaee, Z., Rabbani, M., Mirani, M., Piya, G., Opushnyev, I., Ghorbani, A., & Dadkhah, S. (2026). *Security threat modeling for emerging AI-agent protocols: A comparative analysis of MCP, A2A, Agora, and ANP* (arXiv:2602.11327). arXiv. https://doi.org/10.48550/arXiv.2602.11327

20. Rostamzadeh, M., Narula, S., Birhan, N., Ghasemigol, M., & Takabi, D. (2026). *MCP-DPT: A defense-placement taxonomy and coverage analysis for Model Context Protocol security* (arXiv:2604.07551). arXiv. https://doi.org/10.48550/arXiv.2604.07551

21. Nandish, M., Misra, R., & Balasubramaniam, V. (2026). The Model Context Protocol security landscape: A systematic analysis of inherent vulnerabilities and defensive inadequacies. In *Lecture notes in networks and systems* (pp. 144–152). Springer. https://doi.org/10.1007/978-3-032-31998-2_13

22. Tricco, A. C., Lillie, E., Zarin, W., O'Brien, K. K., Colquhoun, H., Levac, D., ..., & Straus, S. E. (2018). PRISMA extension for scoping reviews (PRISMA-ScR): Checklist and explanation. *Annals of Internal Medicine, 169*(7), 467–473. https://doi.org/10.7326/M18-0850

23. Garousi, V., Felderer, M., & Mäntylä, M. V. (2019). Guidelines for including grey literature and conducting multivocal literature reviews in software engineering. *Information and Software Technology, 106*, 101–121. https://doi.org/10.1016/j.infsof.2018.09.006

24. Kitchenham, B., & Charters, S. (2007). *Guidelines for performing systematic literature reviews in software engineering* (EBSE Technical Report EBSE-2007-01). Keele University and Durham University.

25. National Security Agency. (2026). *Model Context Protocol (MCP): Security design considerations for AI-driven automation* (Cybersecurity Information Sheet U/OO/6030316-26). https://media.defense.gov/2026/Jun/02/2003943289/-1/-1/0/CSI_MCP_SECURITY.PDF

26. Invariant Labs. (2025, May 26). *GitHub MCP exploited: Accessing private repositories via MCP*. https://invariantlabs.ai/blog/mcp-github-vulnerability

27. Wohlin, C. (2014). Guidelines for snowballing in systematic literature studies and a replication in software engineering. In *Proceedings of the 18th International Conference on Evaluation and Assessment in Software Engineering* (Article 38). ACM. https://doi.org/10.1145/2601248.2601268

28. Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics, 33*(1), 159–174. https://doi.org/10.2307/2529310

29. Owotogbe, J., Kumara, I., van den Heuvel, W.-J., Tamburri, D. A., Iannillo, A. K., & Natella, R. (2026). *A taxonomy of runtime faults in Model Context Protocol servers* (arXiv:2606.05339). arXiv. https://doi.org/10.48550/arXiv.2606.05339

30. Taraghi, M., Morovati, M. M., & Khomh, F. (2026). *Real faults in Model Context Protocol (MCP) software: A comprehensive taxonomy* (arXiv:2603.05637). arXiv. https://doi.org/10.48550/arXiv.2603.05637

31. Tyndall, J. (2010). *AACODS checklist*. Flinders University.

32. Huang, Y., Ma, B., Yan, B., Dai, X., Zhang, Y., Xu, M., ..., & Zhang, Y. (2026). *Give them an inch and they will take a mile: Understanding and measuring caller identity confusion in MCP-based AI systems* (arXiv:2603.07473v2). arXiv. https://doi.org/10.48550/arXiv.2603.07473

33. Li, Z., Wu, J., Peng, Y., Luo, T., Cui, X., & Ling, X. (2026). Confused deputy attack against Model Context Protocol. *ACM Transactions on Software Engineering and Methodology*. Advance online publication. https://doi.org/10.1145/3830467

34. Google. (2025, April 9). *Announcing the Agent2Agent protocol (A2A)*. Google Developers Blog. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

35. Kim, S.-Y., Park, S.-H., Jeon, A., Jeong, Y., Son, G., & Lee, I.-G. (2026). Semantic manipulation attacks in agentic AI systems with agent-to-agent communication and Model-Context-Protocol-based tool invocation. In *IEEE Conference on Computer Communications (INFOCOM 2026 Workshops: GenAINet)*. IEEE. https://doi.org/10.1109/INFOCOM59046.2026.11571532

36. Wang, P., Li, Y., Sun, Y., Liu, C., Liu, Y., & Tian, Y. (2026). *From docs to descriptions: Smell-aware evaluation of MCP server descriptions* (arXiv:2602.18914). arXiv. https://doi.org/10.48550/arXiv.2602.18914

37. Bharti, G. (2026). *Registry descriptions go stale unevenly: An 89-day measurement of Model Context Protocol drift, and why drift-ranked re-auditing under-covers it* (arXiv:2608.00997v2). arXiv. https://doi.org/10.48550/arXiv.2608.00997

38. Liu, H., Hu, K., Liao, J., Wang, Q., Qian, P., Zhai, Y., ..., & Wang, H. (2026). *MCPEvol-Bench: Benchmarking LLM agent performance across dynamic evolutions of MCP servers* (arXiv:2607.14642). arXiv. https://doi.org/10.48550/arXiv.2607.14642

39. Hardy, N. (1988). The confused deputy: (Or why capabilities might have been invented). *ACM SIGOPS Operating Systems Review, 22*(4), 36–38. https://doi.org/10.1145/54289.871709

40. Model Context Protocol. (2025b). *Model Context Protocol specification* (Revision 2025-06-18). https://modelcontextprotocol.io/specification/2025-06-18

41. Yao, Y., Wang, Z., Cheng, H., Cheng, Y., Du, H., & Li, X.-Y. (2025). *IntentMiner: Intent inversion attack via tool call analysis in the Model Context Protocol* (arXiv:2512.14166v2). arXiv. https://doi.org/10.48550/arXiv.2512.14166

42. Ridao, A. P., Safari, M., Kang, Z., & Dragoni, N. (2026). MCP-SecLint: An open-source static analyzer for detecting vulnerabilities in LLM tool integrations. In *Proceedings of the 12th ACM International Workshop on Security and Privacy Analytics (IWSPA '26)* (pp. 89–100). ACM. https://doi.org/10.1145/3806007.3810961

43. Zhang, C., Li, Y., Tian, Y., Bachras, M., & Jacobsen, H.-A. (2026). *When agentic executions fail: Detecting and localizing runtime faults from telemetry* (arXiv:2608.14680). arXiv. https://doi.org/10.48550/arXiv.2608.14680

44. Kim, T., Jiang, D., Hu, Y., Jia, Y., & Gong, N. (2026). *Evaluating tool cloning in agentic-AI ecosystems* (arXiv:2605.09817v2). arXiv. https://doi.org/10.48550/arXiv.2605.09817

45. Wang, Z., Zhang, R., Liu, Y., Fan, W., Jiang, W., Zhao, Q., Li, H., & Xu, G. (2026). MPMA: Preference manipulation attack against Model Context Protocol. In *Proceedings of the AAAI Conference on Artificial Intelligence*, 40(42), 35838–35846. https://doi.org/10.1609/aaai.v40i42.40898

46. Guo, J., Wang, Z., Jiang, W., Zhang, R., Xiong, J., Song, Q., Wu, H., & Liu, Y. (2026). BiasAgent: Exploiting agent bias for preference manipulation attacks on Model Context Protocol. *IEEE Transactions on Cognitive Communications and Networking*, 10358–10371. https://doi.org/10.1109/TCCN.2026.3714063

47. Sun, Y., Du, L., Su, Z., Wang, Y., Liu, H., Zhao, Q., & Niu, X. (2025). MSA: A cross-MCP privacy attack via memory exfiltration of large language models. In *Proceedings of the 24th Workshop on Privacy in the Electronic Society (WPES '25)* (pp. 177–182). ACM. https://doi.org/10.1145/3733802.3764057

48. National Institute of Standards and Technology. (2025a). *CVE-2025-47274 detail*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-47274

49. National Institute of Standards and Technology. (2025b). *CVE-2025-53109 detail*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-53109

50. National Institute of Standards and Technology. (2025c). *CVE-2025-53110 detail: Filesystem MCP server directory containment bypass via prefix matching flaw*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-53110

51. National Institute of Standards and Technology. (2025d). *CVE-2025-68143 detail: mcp-server-git arbitrary repository initialization via unvalidated paths*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-68143

52. National Institute of Standards and Technology. (2025e). *CVE-2025-68144 detail: mcp-server-git command-line argument injection in diff and checkout*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-68144

53. National Institute of Standards and Technology. (2025f). *CVE-2025-68145 detail: mcp-server-git directory boundary traversal bypassing repository restriction*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-68145

54. National Institute of Standards and Technology. (2026b). *CVE-2026-27735 detail: mcp-server-git path traversal in git_add handler*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2026-27735

55. National Institute of Standards and Technology. (2025g). *CVE-2025-53967 detail: Framelink Figma MCP server remote command execution via shell metacharacters*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-53967

56. National Institute of Standards and Technology. (2026a). *CVE-2026-0755 detail: gemini-mcp-tool OS command injection in execAsync and CLI argument parsing*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2026-0755

57. National Institute of Standards and Technology. (2026c). *CVE-2026-39884 detail: MCP Server Kubernetes argument injection in port_forward*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2026-39884

58. National Institute of Standards and Technology. (2025k). *CVE-2025-65513 detail: Fetch MCP Server Server-Side Request Forgery (SSRF)*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-65513

59. National Institute of Standards and Technology. (2026d). *CVE-2026-32871 detail: FastMCP OpenAPI provider SSRF and path traversal*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2026-32871

60. National Institute of Standards and Technology. (2026). *CVE-2026-35568 detail*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2026-35568

61. National Institute of Standards and Technology. (2025l). *CVE-2025-66414 detail: Model Context Protocol TypeScript SDK DNS rebinding vulnerability*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-66414

62. National Institute of Standards and Technology. (2025m). *CVE-2025-66416 detail: Model Context Protocol Python SDK DNS rebinding vulnerability*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-66416

63. National Institute of Standards and Technology. (2025h). *CVE-2025-49596 detail: Anthropic MCP Inspector unauthenticated local proxy remote code execution*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-49596

64. National Institute of Standards and Technology. (2025i). *CVE-2025-6514 detail: mcp-remote client proxy OS command injection via untrusted OAuth authorization endpoint*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-6514

65. National Institute of Standards and Technology. (2025n). *CVE-2025-54135 detail: Cursor IDE CurXecute unprompted in-workspace configuration execution*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-54135

66. National Institute of Standards and Technology. (2025j). *CVE-2025-54136 detail: Cursor IDE MCPoison silent configuration tampering and command execution*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2025-54136

67. National Institute of Standards and Technology. (2026e). *CVE-2026-0621 detail: Model Context Protocol TypeScript SDK ReDoS in UriTemplate*. National Vulnerability Database. https://nvd.nist.gov/vuln/detail/CVE-2026-0621

68. Asana. (2025, June 18). *Security advisory: Cross-tenant data exposure and isolation failure in experimental Asana MCP server*. Asana Trust Center. https://asana.com/trust/security

69. Zealynx Security. (2026). *MCP Breach Index 2025–2026: Empirical analysis of real-world Model Context Protocol incidents and CVEs*. https://www.zealynx.io/research/adversarial-security/mcp-breach-index-2025-2026

70. Model Context Protocol. (2025a). *Model Context Protocol specification* (Revision 2025-03-26). https://modelcontextprotocol.io/specification/2025-03-26

71. Jones, M., Sakimura, N., & Bradley, J. (2018). *OAuth 2.0 authorization server metadata* (RFC 8414). Internet Engineering Task Force. https://doi.org/10.17487/RFC8414

72. Richer, J., Jones, M., Bradley, J., Machulak, M., & Hunt, P. (2015). *OAuth 2.0 dynamic client registration protocol* (RFC 7591). Internet Engineering Task Force. https://doi.org/10.17487/RFC7591

73. Jones, M. B., Hunt, P., & Parecki, A. (2025). *OAuth 2.0 protected resource metadata* (RFC 9728). Internet Engineering Task Force. https://doi.org/10.17487/RFC9728

74. Campbell, B., Bradley, J., & Tschofenig, H. (2020). *Resource indicators for OAuth 2.0* (RFC 8707). Internet Engineering Task Force. https://doi.org/10.17487/RFC8707

75. Meyer zu Selhausen, K., & Fett, D. (2022). *OAuth 2.0 authorization server issuer identification* (RFC 9207). Internet Engineering Task Force. https://doi.org/10.17487/RFC9207

76. Model Context Protocol. (2024). *Model Context Protocol specification* (Revision 2024-11-05). https://modelcontextprotocol.io/specification/2024-11-05

77. Model Context Protocol. (2025c). *Model Context Protocol specification* (Revision 2025-11-25). https://modelcontextprotocol.io/specification/2025-11-25

78. He, S., Li, C., Liu, J., Liu, J., Keung, J., & Ma, X. (2026). Understanding bugs in Model Context Protocol development frameworks: An empirical study. *ACM Transactions on Software Engineering and Methodology*. Advance online publication. https://doi.org/10.1145/3847119

79. Jing, H., Li, H., Hu, W., Hu, Q.-M., Xu, H., Chu, T., ..., & Song, Y. (2025). MCIP: Protecting MCP safety via Model Contextual Integrity Protocol. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*. Association for Computational Linguistics. https://doi.org/10.18653/v1/2025.emnlp-main.62

80. Halloran, J. T., Radosevich, B., & Black, G. (2026). *MCP safety audit: LLMs with the Model Context Protocol allow major security exploits*. SPIE Defense + Security. https://doi.org/10.1117/12.3097390

81. Sun, P., Kang, Z., Jin, Q., Huang, E., Liu, X., Shen, D., & Li, S. (2026). *VIPER-MCP: Detecting and exploiting taint-style vulnerabilities in Model Context Protocol servers* (arXiv:2605.21392). arXiv. https://doi.org/10.48550/arXiv.2605.21392

82. Li, C., Hu, P., Xu, J., Ozbas, B., Liu, O., Van, C., ..., & Zhang, M. (2026). ADR: An agentic detection system for enterprise agentic AI security. In *Proceedings of Machine Learning and Systems (MLSys 2026)*. https://proceedings.mlsys.org/paper_files/paper/2026/file/f03cb785864596fa5901f1359d23fd81-Paper-Conference.pdf

83. Wang, Z., Du, H., Shi, G., Zhang, J., Cheng, H., Yao, Y., ..., & Li, X.-Y. (2025). *MindGuard: Intrinsic decision inspection for securing LLM agents against metadata poisoning* (arXiv:2508.20412). arXiv. https://doi.org/10.48550/arXiv.2508.20412

84. Dantuluri, P. S. V., & Sundi, J. (2026). *Delegation without trust: An empirical gap analysis of identity, authorization, and runtime governance in multi-agent LLM systems* (arXiv:2609.00267). arXiv. https://doi.org/10.48550/arXiv.2609.00267

85. Gentyala, S., Reddy, N., Deepthi, K., Saroja, P., Achari, K., & Shaik, R. (2026). Agentic security validation framework for retrieval-augmented and tool-enabled large language model systems. In *2026 7th International Conference on Computational Vision and Bio Inspired Computing (ICCVBIC)* (pp. 1001–1011). IEEE. https://doi.org/10.1109/ICCVBIC71195.2026.11689544

86. Hamjaya, M., Richardo, A. S., Leonard, D., & Junior, F. A. (2025). The missing S: Securing the Model Context Protocol. In *2025 1st International Conference on Artificial Intelligence Technology (ICoAIT)*. IEEE. https://doi.org/10.1109/ICoAIT67446.2025.11308830

87. Zavrak, S. (2026). *Content-aware attack detection in LLM agent tool-call traffic: An empirical study of features, architectures, and evaluation protocols* (arXiv:2605.11053). arXiv. https://doi.org/10.48550/arXiv.2605.11053

88. Stodt, F., Reich, C., & Stodt, J. (2026). A federated MCP gateway: Enforceable isolation and measuring residual semantic attacks. In *2026 IEEE Network Operations and Management Symposium (NOMS)*. IEEE. https://doi.org/10.1109/NOMS69089.2026.11668221

89. Wang, Z., Shi, G., Wang, Y., Gao, Y., Lang, H., Yao, Y., Du, H., & Li, X. (2026). Beyond detection: Autonomous anomaly remediation for MCP against tool poisoning attacks. In *Proceedings of the ACM Web Conference 2026 (WWW '26)* (pp. 2974–2982). ACM. https://doi.org/10.1145/3774904.3792400

90. Shatnawi, A., AlSobeh, A., Khamaiseh, S., & Al-Abdullah, M. (2026). Secure-by-design framework for agentic AI: Mitigating toxic flows and adversarial exploits in multi-agent ecosystems. In *2026 Intermountain Engineering, Technology and Computing (IETC)* (pp. 1–6). IEEE. https://doi.org/10.1109/IETC69527.2026.11568651

91. Shi, Y., Hu, J., Wang, L., Ma, R., Wang, M., & Jia, Z. (2026). SecuAudit: Integrity-preserving metadata compliance auditing for secure data circulation in MCP-enabled AI agents. *Computers, Materials & Continua*, 89(1), Article 100, 1–10. https://doi.org/10.32604/cmc.2026.085633

92. Polat, O., Doğan, F., Türkoğlu, M., Yolcu, F., & Baturay, M. (2026). MCP-driven real-time security monitoring: A hybrid LLM and behavior-aware framework for temporal attack detection and severity assessment. *Computer Networks*, 287, Article 112540. https://doi.org/10.1016/j.comnet.2026.112540

93. Ntousakis, G., Stephen, J. J., Le, M. V., Chukkapalli, S. S. L., Taylor, T., Molloy, I., & Araujo, F. (2025). Securing MCP-based agent workflows. In *Proceedings of the 2025 ACM SIGOPS Symposium on Operating Systems Principles Workshops*. ACM. https://doi.org/10.1145/3766882.3767177

94. Narayan, O., Jyoti, R., & Singh, R. (2026). *ChainWatch: A kill chain-aligned sequential detection framework for multi-step attacks in MCP-based AI agent systems* (arXiv:2607.19432). arXiv. https://doi.org/10.48550/arXiv.2607.19432

95. Shen, Y., Pan, X., Hong, G., & Yang, M. (2026). *Invisible threats from Model Context Protocol: Generating stealthy injection payload via tree-based adaptive search* (arXiv:2603.24203). arXiv. https://doi.org/10.48550/arXiv.2603.24203

96. Zhang, Y., Wang, W., Zhou, Z., Wang, K., Zhang, J., Sun, L., ..., & Su, S. (2025). *LeechHijack: Covert computational resource exploitation in intelligent agent systems* (arXiv:2512.02321). arXiv. https://doi.org/10.48550/arXiv.2512.02321
