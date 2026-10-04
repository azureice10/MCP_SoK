# Evidence Locator Packet: weibo-2025-when-mcp-servers-attack-taxonomy

- **Title**: When MCP Servers Attack: Taxonomy, Feasibility, and Mitigation
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: survey_review
- **Link**: https://arxiv.org/abs/2509.24272
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\weibo-2025-when-mcp-servers-attack-taxonomy\fulltext.txt
- **Character Count**: 72730

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 729:948]
> To address this gap, we present the first systematic
> study that treats MCP servers as active threat actors and decom-
> poses them into core components to examine how adversarial de-
> velopers can implant malicious intent.
**Location**: `Abstract` [offsets: 1308:1449]
> For each category, we develop Proof-of-Concept (PoC) servers and
> demonstrate their effectiveness across diverse real-world host–LLM
> settings.

## Block 3: Method Locator
**Section Heading**: `implementation and detection?` [section offsets: 5335:5748]
**First 120 words verbatim** [offsets: 5335:6139]
> implementation and detection?
> 
> To answer these research questions, we first conduct a component-
> based MCP server attack analysis (§3), and evaluate these attacks
> against various MCP hosts and LLM models (§4.1). We further
> 
> --- PAGE BREAK ---
> 
> Local MCP Server
> 
> Local Resource
> 
> External Resource
> 
> Prompts
> Tools
> Resource
> 
> MCP Host
> 
> MCP Client
> Stdio
> HTTP
> 
> MCP Client
> Remote MCP Server
> 
> Host 
> Orchestrator
> UI
> 
> User
> 
> LLM Client
> 
> LLM Provider
> 
> Figure 1: MCP architecture overview.
> 
> investigate the difficulty of attack implementation and detection
> bypassing (§4.2) to measure the real-world attack feasibility.
> 
> Based on the analysis and experiment results, we obtain the fol-
> lowing key findings: (1) Malicious MCP servers are able to launch
> 12 categories of attacks, which can be organized into a component-
**Section Heading**: `architecture, including three distinct components: host, client,` [section offsets: 8344:12712]
**First 120 words verbatim** [offsets: 8344:9135]
> architecture, including three distinct components: host, client,
> 
> Zhao et al.
> 
> and server. The MCP host is an LLM-based application, such as
> Claude Desktop [3], Cursor [10], or Windsurf [38]. Within a host,
> each MCP client establishes and maintains a one-to-one connection
> with an MCP server. The MCP host may manage multiple such
> clients to support multiple servers. The MCP client handles message
> transport, tool discovery, tool invocation, and resource access on
> behalf of the host application. The MCP server provides the client
> with context, tools, and prompts, thereby extending the LLM with
> outward-facing capabilities [4].
> 
> 2.2
> MCP Servers
> 
> MCP servers can be developed independently of host applications
> and easily plugged into different hosts, and thus have been widely
> adopted [7,

## Block 4: Evaluation Locator
**Section Heading**: `Experiments & Evaluation` [section offsets: 49848:50457]
**First 120 words verbatim** [offsets: 49848:50630]
> Experiments & Evaluation
> 
> In this section, we answer the RQ2 and RQ3 posed in §1. Specifi-
> cally, for RQ2, we implement PoC malicious MCP servers for each
> attack category in our taxonomy and evaluate their effectiveness
> across multiple host–LLM combinations. For RQ3, we develop a
> server generator to demonstrate the ease of implementing mali-
> cious MCP servers at scale. We then assess existing MCP security
> scanners on generated servers, demonstrating how easily such at-
> tacks can be deployed in practice. The PoC implementations and
> generator source code will be publicly accessible upon acceptance.
> 
> 4.1
> Evaluation of MCP Server Attacks across
> Hosts and LLMs
> 
> According to our attack taxonomy, we implement twelve PoC MCP
> servers, each designed to resemble plausible real-world
**Section Heading**: `Evaluation of MCP Server Attacks across` [section offsets: 50457:51652]
**First 120 words verbatim** [offsets: 50457:51234]
> Evaluation of MCP Server Attacks across
> Hosts and LLMs
> 
> According to our attack taxonomy, we implement twelve PoC MCP
> servers, each designed to resemble plausible real-world use cases.
> All PoC servers are installed locally, and each server is evaluated
> individually. The experimental setup and results are presented be-
> low.
> 
> 4.1.1
> Host & Model Selection. Prior MCP security studies typi-
> cally evaluate attacks only against LLMs, which does not fully
> reflect real-world MCP deployments. In this work, we evaluate
> MCP server attacks in realistic settings across multiple host appli-
> cations equipped with different backbone LLMs. For the hosts, we
> choose Claude Desktop [3] (an AI chat application), Cursor [10]
> (an AI code editor), and a custom host built with the open-source
**Section Heading**: `Evaluation Metrics. We use Attack Success Rate (ASR) as the` [section offsets: 51652:52660]
**First 120 words verbatim** [offsets: 51652:52405]
> Evaluation Metrics. We use Attack Success Rate (ASR) as the
> primary evaluation metric. For each attack type, we define ASR as
> the proportion of trials in which the malicious MCP server achieves
> its intended effect (e.g., leaking data, executing unauthorized opera-
> tions) without being blocked or interrupted by the host or LLM. To
> account for variability in model behavior, each attack is executed
> 15 times per host–model pair, with each trail initiated in a fresh
> conversation.
> 
> 4.1.3
> Experiment Results. Experiment results are summarized in
> Tab.2. Note that A7 and A10 are not included in this table. A7
> 
> is evaluated separately because the tested hosts do not currently
> support LLM-driven resource selection. A10 is not suitable for this
> table as it
**Section Heading**: `experimental results.` [section offsets: 52660:53317]
**First 120 words verbatim** [offsets: 52660:53404]
> experimental results.
> 
> Attacks with 100% Success Rate. Six PoC servers (A2, A3, A5, A6,
> A8, and A11) achieved a 100% ASR across all host–LLM combina-
> tions. A2’s success shows hosts do not validate their config files,
> accepting even malicious Docker commands. A3, A5, A8, and A11
> succeeded because hosts do not check if server behavior matches
> its declared functionality, allowing extra malicious code to run un-
> detected. The 100% ASR of A6 demonstrates that hosts do not filter
> tool outputs; results are injected directly into the LLM context, and
> all LLMs relay malicious content to users.
> 
> Attacks Yielding Different Outcomes Across Hosts with the Same
> LLM. We observed four cases where attack outcomes varied by host
> despite using the same

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `Evaluation of Existing MCP Server Security` [offsets: 57479:57710]
> In our implementation, the seed pools consist of 5 malicious
> launch commands, 7 malicious initialization code snippets, 10 mali-
> cious and 30 benign tools, 10 malicious and 10 benign resources,
> and 5 malicious and 5 benign prompts.
**Location**: `Evaluation of Existing MCP Server Security` [offsets: 57711:57810]
> Benign components do not
> introduce attacks; they serve to diversify the space of generated
> servers.
**Location**: `Evaluation of Existing MCP Server Security` [offsets: 61092:61469]
> MCP Host 
> •
> Safe configuration handling
> •
> Trust management
> •
> Runtime supervision
> •
> Safety system prompts
> •
> User Transparency
> 
> LLM
> •
> Caution with server output
> •
> Priority on user queries
> •
> Resistance to injected instructions
> •
> Anomaly detection
> 
> User
> •
> Caution with third-party servers
> •
> Principle of least privilege
> 
> Figure 8: Roles and security practices in the MCP ecosystem.

## Block 8: Limitations
**Section Heading**: `Limitations of Existing Work` [section offsets: 12712:26165]
**First 120 words verbatim** [offsets: 12712:13553]
> Limitations of Existing Work
> 
> As MCP gains wider attention and adoption, recent research has
> begun to discuss its security challenges. Hou et al. [19] highlight
> potential security risks associated with the creation, operation,
> and update phases of MCP servers, including installer spoofing,
> sandbox escape, and redeployment of vulnerable versions. From the
> perspective of the primary roles in MCP, Narajala and Habler [27]
> identify several categories of MCP security threats: MCP server
> threats, MCP client threats, MCP host environment threats, data
> sources and external resources threats, tool-related threats, and
> prompt-related threats. Jing et al. [21] categorize risks in MCP
> interactions into five dimensions: Stage, Source, Scope, Type, and
> the corresponding MAESTRO layers. Based on their threat analysis,
> they introduce an enhanced

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `LLM. This opacity creates opportunities for malicious server de-` [offsets: 38783:39122]
> An attacker can
> deliberately misrepresent this field, causing the host to apply incor-
> rect handlers and potentially resulting in parsing errors or crashes.
> Moreover, because different MIME types may be subject to different
> validation or security checks, such mislabeling can also be abused
> to evade detection.
> 
> (2) Resource impersonation.
