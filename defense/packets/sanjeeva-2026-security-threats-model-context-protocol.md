# Evidence Locator Packet: sanjeeva-2026-security-threats-model-context-protocol

- **Title**: Security Threats in the Model Context Protocol: A Comprehensive Survey and Trust Boundary Mitigation Framework for Agentic AI Systems
- **Year**: 2026
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: survey_review
- **Link**: https://doi.org/10.21275/sr26316110418
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\sanjeeva-2026-security-threats-model-context-protocol\fulltext.txt
- **Character Count**: 39651

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 884:1143]
> This paper presents the first comprehensive academic su
> rvey of MCP 
> security threats, synthesizing findings from seven disclosed CVEs, eleven major security incidents, and over a dozen demonstr
> ated attack 
> classes documented between April and December 2025.
**Location**: `Abstract` [offsets: 1144:1452]
> We propose a formal ten
> -
> class threat taxonomy spanning 
> tool poisoning, indirect 
> prompt injection via tool responses, cross
> -
> server data exfiltration, tool shadowing, supply
> -
> chain attacks, rug
> -
> pull exploits, credential theft, 
> sampling abuse, terminal deception, and inter
> -
> agent trust exploitation.
**Location**: `Introduction` [offsets: 5285:6156]
> we present a 
> formal ten
> -
> class threat taxonomy for MCP, grounded in 
> demonstrated attacks rather than theoretical vulnerabilities 
> (Section 3). Second, we provide the first systematic mapping 
> of MCP threats to four 
> major governance frameworks 
> released in 2025
> –
> 2026 (Section 5). Third, we analyze 
> domain
> -
> specific threat amplification in healthcare, financial 
> services, and enterprise IT environments (Section 6). Fourth, 
> we propose a Trust Boundary Mitigation Framework (T
> BMF) 
> that combines six reinforcing defense layers into a deployable 
> architecture (Section 7). We conclude by identifying six key 
> insights and open research challenges for the community 
> (Section 8).
>  
>  
>  
>  
> Paper ID: SR26316110418
> DOI: https://dx.doi.org/10.21275/SR26316110418
> 990 
> 
> International Journal of Science and Research (IJSR)
>  
> ISSN: 2319
> -
> 7064
>  
> Impact Factor 2025: 7.089

## Block 3: Method Locator
**Section Heading**: `architecture (Section 7). We conclude by identifying six key` [section offsets: 5839:6279]
**First 120 words verbatim** [offsets: 5839:6681]
> architecture (Section 7). We conclude by identifying six key 
> insights and open research challenges for the community 
> (Section 8).
>  
>  
>  
>  
> Paper ID: SR26316110418
> DOI: https://dx.doi.org/10.21275/SR26316110418
> 990 
> 
> International Journal of Science and Research (IJSR)
>  
> ISSN: 2319
> -
> 7064
>  
> Impact Factor 2025: 7.089
>  
> Volume 15 Issue 3, March 2026
>  
> Fully Refereed | Open Access | Double Blind Peer Reviewed Journal
>  
> www.ijsr.net
>  
> 2.
>  
> Background: MCP Architecture and 
> Security Properties
>  
>  
> 2.1 Protocol Architecture
>  
>  
> MCP implements a client
> -
> host
> -
> server architecture built on 
> JSON
> -
> RPC 2.0 [1]. The 
> host
>  
> application (e.g., an IDE or AI 
> assistant) manages multiple 
> MCP clients
> , each maintaining a 
> stateful one
> -
> to
> -
> one session with an 
> MCP server
>  
> that exposes 
> three primitive types: 
> tools
>  
> (executable functions),
**Section Heading**: `2.1 Protocol Architecture` [section offsets: 6337:7566]
**First 120 words verbatim** [offsets: 6337:7121]
> 2.1 Protocol Architecture
>  
>  
> MCP implements a client
> -
> host
> -
> server architecture built on 
> JSON
> -
> RPC 2.0 [1]. The 
> host
>  
> application (e.g., an IDE or AI 
> assistant) manages multiple 
> MCP clients
> , each maintaining a 
> stateful one
> -
> to
> -
> one session with an 
> MCP server
>  
> that exposes 
> three primitive types: 
> tools
>  
> (executable functions), 
> resources
>  
> (data endpoints), and 
> prompts
>  
> (templated interaction 
> patterns). The protocol specification has evolved through four 
> versions (2024
> -
> 11
> -
> 05, 2025
> -
> 03
> -
> 26, 2025
> -
> 06
> -
> 18, and 2025
> -
> 11
> -
> 25), progressively adding OAuth 2.1 au
> thorization, 
> Streamable HTTP transport, structured tool output, 
> elicitation, and a tasks primitive for asynchronous operations 
> [9].
>  
>  
> Tool discovery occurs via the 
> tools/list
>  
> endpoint,
**Section Heading**: `architecture cannot rely on model` [section offsets: 29397:29552]
**First 120 words verbatim** [offsets: 29397:30280]
> architecture cannot rely on model
> -
> level safety. Trust must be 
> enforced architecturally.
>  
>  
> Third, 
> the gateway represents the minimum viable security 
> architecture. Without a centralized enforcement point 
> independent of the LLM’s probabilistic reasoning, no MCP 
> deployment can achieve deterministic security guarantees.
>  
>  
> Fourth, 
> availability protection is completely absent. A 
> systematization of knowledge covering 78 defense papers 
> found that all 41 surveyed defenses focus exclusively on 
> integrity [39]. No published method protects against denial
> -
> of
> -
> service attacks on agentic syste
> ms
> -
>  
> a critical research gap.
>  
>  
> Fifth, 
> domain
> -
> specific regulatory pressure is increasing and 
> substantive. FINRA [29], HIPAA [27], and GDPR authorities 
> [40] have all begun issuing agent
> -
> specific guidance.
>  
>  
> Sixth, 
> formal methods should target the authorization layer,
**Section Heading**: `architecture. Without a centralized enforcement point` [section offsets: 29552:30823]
**First 120 words verbatim** [offsets: 29552:30483]
> architecture. Without a centralized enforcement point 
> independent of the LLM’s probabilistic reasoning, no MCP 
> deployment can achieve deterministic security guarantees.
>  
>  
> Fourth, 
> availability protection is completely absent. A 
> systematization of knowledge covering 78 defense papers 
> found that all 41 surveyed defenses focus exclusively on 
> integrity [39]. No published method protects against denial
> -
> of
> -
> service attacks on agentic syste
> ms
> -
>  
> a critical research gap.
>  
>  
> Fifth, 
> domain
> -
> specific regulatory pressure is increasing and 
> substantive. FINRA [29], HIPAA [27], and GDPR authorities 
> [40] have all begun issuing agent
> -
> specific guidance.
>  
>  
> Sixth, 
> formal methods should target the authorization layer, 
> not the model. MiniScope’s approach of constructing 
> verifiable permission hierarchies from OAuth scopes [34] 
> Paper ID: SR26316110418
> DOI: https://dx.doi.org/10.21275/SR26316110418
> 996 
> 
> International

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `3.1 T1: Tool Poisoning` [offsets: 12858:13121]
> The MCPTox benchmark evaluated 45 
> real
> -
> world MCP servers across 20 LLM agents, finding that 
> more capable models are 
> more
>  
> susceptible: Claude
> -
> 3.7
> -
> Sonnet refused attacks less than 3% of the time, and o1
> -
> mini 
> exhibited a 72.8% attack success rate [11].
**Location**: `3.2 T2` [offsets: 13433:13921]
> Demonstrated incidents include a 
> GitHub MCP exploit (May 2025) where a crafted GitHub 
> issue caused an agent to access private repositories and 
> exfiltrate data through a public pull request [12]; a 
> Supabase/Cursor exploit (June 2025) w
> here a support ticket 
> containing malicious SQL was executed by an agent with 
> service
> -
> role database access; and zero
> -
> click attacks throu
> gh 
> Jira and Google Docs MCP servers where malicious content 
> auto
> -
> executed without user interaction [5].

## Block 6: Baseline Excerpts
**Location**: `2.3 Comparison with Traditional API Security Models` [offsets: 8936:9066]
> 2.3 Comparison with Traditional API Security Models
>  
>  
> Traditional API security operates on fundamentally different 
> assumptions.
**Location**: `7.4 Layer 4: Runtime Behavioral Monitoring` [offsets: 26654:26801]
> Multi
> -
> layer detection combines rule
> -
> based checks, statistical 
> baselines, machine learning anomaly models, and LLM
> -
> scheduled verifier agents.

## Block 7: Cost Excerpts
**Location**: `Abstract` [offsets: 1453:1960]
> We map these th
> reats against four emerging governance 
> frameworks (OWASP Top 10 for Agentic Applications 2026, MITRE ATLAS, NIST IR 8596, and CSA MAESTRO), analyze domain
> -
> specific risk amplification in healthcare, financial services, and enterprise IT, and propose a defen
> se
> -
> in
> -
> depth Trust Boundary Mitigation 
> Framework (TBMF) combining MCP gateways, zero
> -
> trust identity, capability
> -
> based least privilege via OAuth scopes, runtime behavioral 
> monitoring, and human
> -
> in
> -
> the
> -
> loop governance.
**Location**: `Introduction` [offsets: 4021:4309]
> When an AI agent operates 
> under MCP, it dynamically discovers tools described in 
> natural language, interprets those descriptions using a 
> probabilistic language model, sel
> ects and sequences tool 
> invocations at runtime, and acts on tool responses that may 
> contain adversarial content.
**Location**: `A Ten` [offsets: 11505:12162]
> Benign tool definitions changed to malicious versions post
> -
> approval
>  
> Invariant Labs disclosure [13]
>  
> T7: Credential Theft
>  
> Plaintext API keys/tokens extracted from MCP server configurations
>  
> Trail of Bits audit [16]
>  
> T8: Sampling 
> Exploitation
>  
> MCP sampling primitive abused for resource theft and conversation hijacking
>  
> Unit 42 research [17]
>  
> T9: Terminal Deception
>  
> ANSI escape sequences hide malicious instructions from user while LLM 
> processes them
>  
> Trail of Bits disclosure [16]
>  
> T10: Inter
> -
> Agent Trust
>  
> 100% of tested LLMs execute malicious commands from peer agents that they 
> resist from humans
>  
> Multi
> -
> agent study, Jul 2025 [18]
**Location**: `7.4 Layer 4: Runtime Behavioral Monitoring` [offsets: 26607:26801]
> 7.4 Layer 4: Runtime Behavioral Monitoring
>  
>  
> Multi
> -
> layer detection combines rule
> -
> based checks, statistical 
> baselines, machine learning anomaly models, and LLM
> -
> scheduled verifier agents.
**Location**: `7.6 Layer 6: Static Analysis and Supply` [offsets: 28299:28545]
> L4: Runtime Monitoring
>  
> T1, T2, T3, T6, T9 (anomaly detection, trajectory analysis)
>  
> L5: Human
> -
> in
> -
> the
> -
> Loop
>  
> T1, T2, T3, T4 (high
> -
> risk action gates)
>  
> L6: Static/Supply Chain
>  
> T5, T6, T7 (pre
> -
> deployment scanning, tool pinning)
>  
>  
> 8.
**Location**: `Discussion: Key Insights and Open Research` [offsets: 29107:29222]
> This is a structural problem: improving model 
> capability amplifies both utility and vulnerability 
> simultaneously.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `7.4 Layer 4: Runtime Behavioral Monitoring` [offsets: 26654:27344]
> Multi
> -
> layer detection combines rule
> -
> based checks, statistical 
> baselines, machine learning anomaly models, and LLM
> -
> scheduled verifier agents. AgentArmor’s program analysis 
> approach on agent execution traces reduces attack success 
> rates to 3% with only 1% ut
> ility loss [36], while AgenTRIM 
> (January 2026) addresses over
> -
> permissioning through 
> adaptive per
> -
> step least
> -
> privilege enforcement [37].
>  
>  
> 7.5 Layer 5: Human
> -
> in
> -
> the
> -
> Loop for High
> -
> Risk 
> Operations
>  
>  
> Standards
> -
> based asynchronous authorization via CIBA 
> enables agents to request human approval without blocking 
> workflow execution, with tiered approval levels calibrated to 
> operation risk classification.
**Matched Term**: `Adaptive` | **Location**: `F. Errico et al., “Gap Analysis of AI Governance` [offsets: 38182:38288]
> AgenTRIM Authors, “AgenTRIM: Adaptive Per
> -
> Step 
> Least
> -
> Privilege Enforcement for AI Agents,” Jan. 2026.
