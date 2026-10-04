# Evidence Locator Packet: xinyi-2026-model-context-protocol-mcp-landscape

- **Title**: Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions
- **Year**: 2026
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: survey_review
- **Link**: https://arxiv.org/abs/2503.23278
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\xinyi-2026-model-context-protocol-mcp-landscape\fulltext.txt
- **Character Count**: 156292

## Block 2: Contribution Sentences
no hits

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 22246:22357]
> Resources provide access to structured and unstruc-
> tured datasets that the MCP server can expose to AI models.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 22358:22432]
> These datasets may come from
> local storage, databases, or cloud platforms.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 30697:30898]
> Developers can subsequently publish
> their packaged servers to various MCP server markets, as illustrated in Table 2, allowing end users
> to discover and install servers directly from these repositories.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 33315:33449]
> External resource access occurs when the server needs to obtain supplementary
> data from third-party systems or knowledge repositories.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 36341:36548]
> The dataset
> summarized in this table was compiled through manual inspection, drawing on official documenta-
> tion from the earliest MCP supporters and extended via community discussions and repository
> mining.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 36766:36944]
> To enhance transparency and facilitate future updates, the
> dataset will be maintained as a public repository1, enabling ongoing community contributions and
> periodic verification.

## Block 6: Baseline Excerpts
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 10553:10629]
> § 7 reviews prior work on tool integration and security in
> LLM applications.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 102834:102950]
> Similar
> risks occur when MCP components expose unprotected HTTP or WebSocket endpoints where
> 
> --- PAGE BREAK ---
> 
> 26
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 111037:111203]
> Configuration drift occurs when unintended or uncoordinated changes
> accumulate in a system’s configuration, causing it to deviate from the intended security baseline.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 112434:112568]
> Mitigating configuration drift requires maintaining alignment between the deployed runtime
> state and a defined configuration baseline.
**Location**: `DISCUSSION` [offsets: 117367:117524]
> Since MCP servers are primarily managed by inde-
> pendent developers, there is no central authority to audit security baselines or enforce uniform
> compliance.

## Block 7: Cost Excerpts
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 6146:6388]
> Second,
> MCP supports dynamic discovery and schema negotiation: the client can list available tools at
> runtime, retrieve their capabilities, and invoke them in a uniform manner, without requiring prior
> hardcoding or platform-specific adapters.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 25270:25392]
> The operation phase corresponds to the runtime period when users
> actively interact with the server through the MCP system.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 31619:31837]
> Environment setup ensures that the deployed MCP server operates under the correct runtime
> 
> --- PAGE BREAK ---
> 
> Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions
> 9
> 
> configuration.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 31997:32138]
> Configuration isolation
> and principle-of-least-privilege practices help mitigate risks of unauthorized access or data leakage
> during runtime.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 32429:32596]
> The operation phase represents the runtime stage of the MCP server
> lifecycle, where the deployed server actively interacts with users, clients, and external resources.
**Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 33169:33314]
> Misinterpretation can lead to
> incorrect tool execution or unnecessary resource calls, potentially increasing latency or amplifying
> risk exposure.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 99332:99928]
> As shown in
> Figure 13, a single natural language request can trigger a sequence of legitimate tool calls that
> collectively lead to data exfiltration, uch as listing files, reading configuration data, extracting
> credentials, and exporting results to a public location. Because each step operates within the
> model’s authorized permissions, these activities often evade traditional access control or policy
> enforcement mechanisms. This attack is characterized by its implicit orchestration, where the
> model autonomously plans and chains approved tools without explicit malicious code or user intent.
**Matched Term**: `adaptive` | **Location**: `X Hou, Y Zhao, S Wang, and H Wang` [offsets: 128472:128754]
> Maintaining active sandbox enforcement during execution ensures
> that even valid sessions cannot exceed defined resource boundaries. Implement consistent
> session management and adaptive logging. Each user or process connecting to the server
> should have its own authenticated session.
