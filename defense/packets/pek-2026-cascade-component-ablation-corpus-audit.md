# Evidence Locator Packet: pek-2026-cascade-component-ablation-corpus-audit

- **Title**: CASCADE: A Component Ablation and Corpus Audit of a Layered Local Defense for MCP-Based Systems
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: benchmark_measurement
- **Link**: https://arxiv.org/abs/2604.17125
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\pek-2026-cascade-component-ablation-corpus-audit\fulltext.txt
- **Character Count**: 117659

## Block 2: Contribution Sentences
no hits

## Block 3: Method Locator
**Section Heading**: `implementation error [4]. Despite its rapid adoption, the` [section offsets: 4916:5252]
**First 120 words verbatim** [offsets: 4916:5691]
> implementation error [4]. Despite its rapid adoption, the
> MCP ecosystem remains in its early stages, with critical
> areas such as security, tool discoverability, and remote de-
> ployment lacking comprehensive solutions [5]. One of the
> most serious threats to MCP-based systems is tool poison-
> ing, classified by OWASP as MCP03:2025 [6].
> 
> 1.2. Problem Statement
> Figure 1 illustrates the architecture of a traditional LLM
> system. In such systems, the user directly sends a prompt
> to the language model, which generates a response. In this
> simple architecture, the attack surface is limited to user
> input only. In contrast, MCP-based systems, as shown in
> Figure 2, exhibit a significantly more complex architecture.
> User input is first transmitted to the MCP Host (i.e., the
> LLM);
**Section Heading**: `Architecture` [section offsets: 23070:23083]
**First 120 words verbatim** [offsets: 23070:23887]
> Architecture
> Evaluation data
> Reported FPR
> Local
> Semantic
> Ablation
> 
> Context Injection [20]∗
> Deployment
> harden-
> ing:
> prompt
> shield,
> RBAC, rate limit
> 
> MCPShield [21]∗
> 3-phase lifecycle cog-
> nition
> 
> 76
> malicious
> servers,
> 6
> backbones
> 
> MCP Guardian [22]
> Regex WAF middle-
> ware
> 
> 1 server, scenario
> tests
> 
> MINDGUARD [23]∗
> White-box
> attention
> provenance
> 
> MCPTox; ToolACE
> clean negatives; 7
> model configs
> 
> Jamshidi et al. [24]∗
> RSA signing + LLM
> vetting + heuristics
> 
> 1,800+ runs (syn-
> thetic)
> 
> MCP-Guard [25]∗
> Regex + fine-tuned
> E5 + LLM arbitration
> 
> 70,448 built; 5,258
> used
> 
> CASCADE (this work)
> Regex
> +
> BGE
> +
> Llama3 review
> 
> 5,000
> (mixed
> provenance)
> 
> a GPT-4-augmented benchmark of 70,448 samples, from
> which a balanced subset of 5,258 is used in the reported
> experiments, and it includes a stage-isolation ablation. Its
> best
**Section Heading**: `3. CASCADE Architecture` [section offsets: 29839:30731]
**First 120 words verbatim** [offsets: 29839:30588]
> 3. CASCADE Architecture
> 
> The CASCADE architecture is illustrated in Figure 3.
> An incoming request passes through a rule-based pre-filter
> (Layer 1) and a semantic stage with an optional local review
> model (Layer 2). A policy stage fuses their signals into a
> single decision score and assigns one of three final statuses.
> Requests that reach the MCP Host are additionally subject
> to an output-oriented pattern check (Layer 3), which is
> described here for completeness but is excluded from the
> evaluation for the reasons given in Section 3.3.
> 
> Layer 1 emits a binary decision: an input is either flagged
> (L1_BLOCK) or passed (L1_PASS); there is no intermediate
> Layer 1 outcome. The three-valued interface of the system
> as a whole (ALLOW, REVIEW, BLOCK)
**Section Heading**: `implementation identified by the pinned commit and` [section offsets: 98252:98337]
**First 120 words verbatim** [offsets: 98252:99023]
> implementation identified by the pinned commit and
> the aggregation rule of Table 4.
> 
> 6.4. Comparison and cost measurement
> 12. No external baseline. No system in Table 1 was re-
> implemented on this corpus, and no detector outside
> 
> İ. Abasıkeleş-Turgut and E. Gümüş: Preprint
> Page 19 of 23
> 
> --- PAGE BREAK ---
> 
> the system’s own layers was evaluated. All litera-
> ture figures quoted here were obtained under different
> datasets and protocols; Table 1 is descriptive and
> supports no claim of superiority.
> 13. Single-run cost measurement. The latency figures
> come from one serial execution per configuration on
> a single machine, with a warm cache and no con-
> currency, and no repetitions, confidence intervals, or
> memory measurements are available.
> 
> 6.5. Residual failure modes

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation Methodology` [section offsets: 1312:1352]
**First 120 words verbatim** [offsets: 1312:2174]
> Evaluation Methodology
> Reproducibility
> 
> 1. Introduction
> 
> 1.1. Motivation
> Large language models (LLMs) are utilized across a
> broad spectrum of applications, from digital assistants to
> AI-powered journalism, owing to their ability to generate
> human-like text. In recent years, autonomous AI agents
> capable of interacting with various tools and data sources
> have attracted increasing attention. This progress accelerated
> in 2023 with OpenAI’s introduction of function calling,
> enabling language models to invoke external APIs in a struc-
> tured manner. This advancement allowed LLMs to retrieve
> real-time data, perform computations, and interact with ex-
> ternal systems. In late 2024, Anthropic released the Model
> Context Protocol (MCP), a universal standard for defining,
> discovering, and invoking external tools in AI applications
> [1].
> 
> Adoption has been rapid: an
**Section Heading**: `Evaluation data` [section offsets: 23083:23822]
**First 120 words verbatim** [offsets: 23083:23901]
> Evaluation data
> Reported FPR
> Local
> Semantic
> Ablation
> 
> Context Injection [20]∗
> Deployment
> harden-
> ing:
> prompt
> shield,
> RBAC, rate limit
> 
> MCPShield [21]∗
> 3-phase lifecycle cog-
> nition
> 
> 76
> malicious
> servers,
> 6
> backbones
> 
> MCP Guardian [22]
> Regex WAF middle-
> ware
> 
> 1 server, scenario
> tests
> 
> MINDGUARD [23]∗
> White-box
> attention
> provenance
> 
> MCPTox; ToolACE
> clean negatives; 7
> model configs
> 
> Jamshidi et al. [24]∗
> RSA signing + LLM
> vetting + heuristics
> 
> 1,800+ runs (syn-
> thetic)
> 
> MCP-Guard [25]∗
> Regex + fine-tuned
> E5 + LLM arbitration
> 
> 70,448 built; 5,258
> used
> 
> CASCADE (this work)
> Regex
> +
> BGE
> +
> Llama3 review
> 
> 5,000
> (mixed
> provenance)
> 
> a GPT-4-augmented benchmark of 70,448 samples, from
> which a balanced subset of 5,258 is used in the reported
> experiments, and it includes a stage-isolation ablation. Its
> best configuration
**Section Heading**: `experiments, and it includes a stage-isolation ablation. Its` [section offsets: 23822:25008]
**First 120 words verbatim** [offsets: 23822:24617]
> experiments, and it includes a stage-isolation ablation. Its
> best configuration reaches an F1-score of 95.4% at 505.9 ms
> per request; the frequently quoted 455.9 ms figure is the
> average across eight arbitration backbones, where the F1-
> score is 89.1%.
> 
> MCP-Guard is the closest published system to the archi-
> tecture described here, and the resemblance is worth stating
> precisely. Its reported experiments run on a local server with
> open-weight arbitration models, and its deployment guid-
> ance recommends on-premise operation, so local execution
> does not distinguish the two designs. It escalates to arbitra-
> tion only when the neural stage returns a score in a narrow
> ambiguous band, and explicitly contrasts this conditional
> activation with a design that routes all requests through
> cascaded
**Section Heading**: `3. Undocumented corpus provenance. Evaluation cor-` [section offsets: 28073:28693]
**First 120 words verbatim** [offsets: 28073:28831]
> 3. Undocumented corpus provenance. Evaluation cor-
> pora are frequently described only by size and by the
> names of contributing sources. Where a corpus has
> been expanded by template-based mutation or model-
> assisted generation, the expansion procedure, the ratio
> of derived to original material, the number of dupli-
> cate records, and any overlap with the detector’s own
> reference material are rarely reported, so the extent
> to which a metric reflects generalization cannot be
> assessed. This observation applies to the corpus used
> in the present study as well, and Section 4.2 reports
> these quantities for it explicitly.
> 4. No evaluation under a common protocol. Each sys-
> tem is evaluated on a corpus of its authors’ construc-
> tion, with its own threat model

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation data` [offsets: 23713:23821]
> a GPT-4-augmented benchmark of 70,448 samples, from
> which a balanced subset of 5,258 is used in the reported
**Location**: `4. No evaluation under a common protocol. Each sys-` [offsets: 28865:28973]
> Sample counts range from a single server
> exercised by hand [22] to a 70,448-record generated
> benchmark [25].
**Location**: `12. No external baseline. No system in Table 1 was re-` [offsets: 98600:98751]
> All litera-
> ture figures quoted here were obtained under different
> datasets and protocols; Table 1 is descriptive and
> supports no claim of superiority.

## Block 6: Baseline Excerpts
**Location**: `Evaluation data` [offsets: 23083:23481]
> Evaluation data
> Reported FPR
> Local
> Semantic
> Ablation
> 
> Context Injection [20]∗
> Deployment
> harden-
> ing:
> prompt
> shield,
> RBAC, rate limit
> 
> MCPShield [21]∗
> 3-phase lifecycle cog-
> nition
> 
> 76
> malicious
> servers,
> 6
> backbones
> 
> MCP Guardian [22]
> Regex WAF middle-
> ware
> 
> 1 server, scenario
> tests
> 
> MINDGUARD [23]∗
> White-box
> attention
> provenance
> 
> MCPTox; ToolACE
> clean negatives; 7
> model configs
> 
> Jamshidi et al.
**Location**: `experiments, and it includes a stage-isolation ablation. Its` [offsets: 23822:23878]
> experiments, and it includes a stage-isolation ablation.
**Location**: `4. No evaluation under a common protocol. Each sys-` [offsets: 29036:29085]
> Component-level ablation is not among these gaps.
**Location**: `4. No evaluation under a common protocol. Each sys-` [offsets: 29335:29452]
> The ablation presented here is therefore an estab-
> lished practice applied to this system, not a novel method-
> ology.
**Location**: `3.4. Decision Aggregation and Evaluation` [offsets: 39594:39784]
> It is not a presen-
> tational detail: it determines what the ablation in Section 4.4
> is able to measure, and Section 5.1 argues that it is a general
> obstacle to comparing published detectors.
**Location**: `4.6. Category- and Type-Level Results` [offsets: 70594:70831]
> The categories in which the lexical baseline already
> performs well—data exfiltration and prompt injection—are
> those whose instances tend to contain structurally distinc-
> tive tokens such as credential names or explicit override
> phrasing.

## Block 7: Cost Excerpts
**Location**: `Evaluation data` [offsets: 23083:23481]
> Evaluation data
> Reported FPR
> Local
> Semantic
> Ablation
> 
> Context Injection [20]∗
> Deployment
> harden-
> ing:
> prompt
> shield,
> RBAC, rate limit
> 
> MCPShield [21]∗
> 3-phase lifecycle cog-
> nition
> 
> 76
> malicious
> servers,
> 6
> backbones
> 
> MCP Guardian [22]
> Regex WAF middle-
> ware
> 
> 1 server, scenario
> tests
> 
> MINDGUARD [23]∗
> White-box
> attention
> provenance
> 
> MCPTox; ToolACE
> clean negatives; 7
> model configs
> 
> Jamshidi et al.
**Location**: `experiments, and it includes a stage-isolation ablation. Its` [offsets: 23879:24074]
> Its
> best configuration reaches an F1-score of 95.4% at 505.9 ms
> per request; the frequently quoted 455.9 ms figure is the
> average across eight arbitration backbones, where the F1-
> score is 89.1%.
**Location**: `3.4. Decision Aggregation and Evaluation` [offsets: 43034:43275]
> A benign-
> consensus downgrade returns a record to the allowed state
> when Layer 1 scores it below 0.10 as benign, Layer 2 also
> reads it as benign, the fused score is within 0.02 of the review
> threshold, and no credential keywords are present.
**Location**: `3.4. Decision Aggregation and Evaluation` [offsets: 43862:44109]
> The benign-consensus down-
> grade is never the recorded reason for a decision: it acts by
> clamping the Layer 2 score rather than by assigning a status,
> and it is one of the two clamps whose point masses identify
> the review threshold in Section 5.3.
**Location**: `3.4. Decision Aggregation and Evaluation` [offsets: 45247:45377]
> The remaining 27 are attributed to an override
> path and recorded as scoring below the review threshold,
> and 23 of them are benign.
**Location**: `3.4. Decision Aggregation and Evaluation` [offsets: 46469:46590]
> A benign input routed to human review is counted
> identically to one blocked outright, yet the two are not the
> same event.

## Block 8: Limitations
**Section Heading**: `6. Limitations` [section offsets: 92959:93091]
**First 120 words verbatim** [offsets: 92959:93715]
> 6. Limitations
> 
> The measurements of Section 4 are bounded in the
> following ways, grouped by the kind of conclusion each
> restricts.
> 
> 6.1. Evaluation design
> 1. Development-corpus measurement with fitted thresh-
> olds. The implementation and its two thresholds were
> developed with reference to the same 5,000 samples
> on which the reported figures were computed, and
> no threshold was obtained from an independent set.
> The development record of how the operating point
> was reached is inconsistent, as Section 4.2.5 reports;
> what every account of it shares is that no held-out
> data enters at any stage. One tenth of the evaluation
> data was visible during calibration under the account
> that names a 500-sample subset, and is scored again in
> every result; under the

## Block 9: Adaptivity Hits
**Matched Term**: `white-box` | **Location**: `2.1. Published defense systems` [offsets: 19571:20033]
> MINDGUARD [23], a white-box defense system, an-
> alyzes the LLM’s internal attention patterns to compute a
> Decision Dependency Graph and a Total Attention Energy
> metric, reporting sub-second processing and no token over-
> head. Its headline 94–99% average precision is the range
> obtained on its clean negative set; on MCPTox itself, where
> benign samples sit in a poisoned context, average precision
> across the seven model configurations ranges from 81.6% to
> 98.1%.
**Matched Term**: `White-box` | **Location**: `Evaluation data` [offsets: 23342:23878]
> 1 server, scenario
> tests
> 
> MINDGUARD [23]∗
> White-box
> attention
> provenance
> 
> MCPTox; ToolACE
> clean negatives; 7
> model configs
> 
> Jamshidi et al. [24]∗
> RSA signing + LLM
> vetting + heuristics
> 
> 1,800+ runs (syn-
> thetic)
> 
> MCP-Guard [25]∗
> Regex + fine-tuned
> E5 + LLM arbitration
> 
> 70,448 built; 5,258
> used
> 
> CASCADE (this work)
> Regex
> +
> BGE
> +
> Llama3 review
> 
> 5,000
> (mixed
> provenance)
> 
> a GPT-4-augmented benchmark of 70,448 samples, from
> which a balanced subset of 5,258 is used in the reported
> experiments, and it includes a stage-isolation ablation.
**Matched Term**: `White-box` | **Location**: `2. White-box requirements. The strongest reported de-` [offsets: 27778:27917]
> 2. White-box requirements. The strongest reported de-
> tection performance [23] depends on access to the
> serving model’s attention matrices.
**Matched Term**: `evasion` | **Location**: `3.1. Layer 1: Rule-Based Pre-Filter` [offsets: 31209:31663]
> Following preprocessing, four analysis views are gener-
> ated for each input: the original text, the normalized text, a
> squashed view in which repeated characters are compressed,
> and a lowercased view. All detection patterns are evaluated
> against each of the four views, so that an evasion that defeats
> one representation is still exposed in another.
> 
> The pattern inventory is summarized in Table 3, whose
> counts were verified against the pinned revision.
**Matched Term**: `evasion` | **Location**: `7. Language coverage. 77.4% of records are pure-ASCII` [offsets: 96388:96703]
> 77.4% of records are pure-ASCII
> English; the remaining 22.6% contain Turkish ho-
> moglyph test material, Japanese system commands,
> or other non-ASCII characters. These are evasion
> tests rather than natural-language samples in other
> languages, so performance on genuine multilingual
> attack phrasing is untested.
> 
> 6.3.
**Matched Term**: `adaptive` | **Location**: `9. No live MCP evaluation. Multi-step tool invoca-` [offsets: 97023:97252]
> No live MCP evaluation. Multi-step tool invoca-
> tion, session context, cross-server coordination, and
> adaptive attacks are outside the evaluation; the threat
> model of Section 1 is broader than what the experi-
> ment exercises.
> 10.
**Matched Term**: `adaptive` | **Location**: `X. Li, Mcptox: A benchmark for tool poisoning attack on real-world` [offsets: 116496:116661]
> Wang, Q. Wen, MCPShield: A security cognition
> layer for adaptive trust calibration in model context protocol agents,
> accessed: 2026-09-01 (2026). arXiv:2602.14281v3.
