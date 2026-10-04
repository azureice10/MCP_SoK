# Evidence Locator Packet: sonu-2025-mcp-guardian-security-first-layer

- **Title**: MCP Guardian: A Security-First Layer for Safeguarding MCP-Based AI System
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2504.12757
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\sonu-2025-mcp-guardian-security-first-layer\fulltext.txt
- **Character Count**: 39659

## Block 2: Contribution Sentences
**Location**: `ABSTRACT` [offsets: 878:1056]
> We present MCP Guardian, a 
> framework that strengthens MCP-based communication with authentication, rate-limiting, 
> logging, tracing, and Web Application Firewall (WAF) scanning.

## Block 3: Method Locator
**Section Heading**: `3. RESEARCH METHODOLOGY` [section offsets: 16744:16771]
**First 120 words verbatim** [offsets: 16744:17646]
> 3. RESEARCH METHODOLOGY 
>  
> 3.1. Overview of the MCP Guardian Approach 
>  
> In order to secure and monitor interactions between MCP clients and servers, we propose MCP 
> Guardian as an intermediate “middleware” layer. Rather than requiring developers to embed 
> security checks directly into each tool server, MCP Guardian intercepts all calls via an override 
> of the invoke_tool method in MCP. This design choice ensures minimal disruption to existing 
> codebases while providing a central point of control for authentication, authorization, rate 
> limiting, request monitoring, and Web Application Firewall (WAF) scanning.
> 
> 112                                             Computer Science & Information Technology (CS & IT)
> 
> --- PAGE BREAK ---
> 
> 3.2. Core Components
> 
> 1. Authentication and Authorization
> 
> administrative privileges. 
>  
> 2. Rate Limiting
> 
> triggered by LLMs. 
>  
> 3. Web Application Firewall (WAF)
**Section Heading**: `3.1. Overview of the MCP Guardian Approach` [section offsets: 16771:17484]
**First 120 words verbatim** [offsets: 16771:17668]
> 3.1. Overview of the MCP Guardian Approach 
>  
> In order to secure and monitor interactions between MCP clients and servers, we propose MCP 
> Guardian as an intermediate “middleware” layer. Rather than requiring developers to embed 
> security checks directly into each tool server, MCP Guardian intercepts all calls via an override 
> of the invoke_tool method in MCP. This design choice ensures minimal disruption to existing 
> codebases while providing a central point of control for authentication, authorization, rate 
> limiting, request monitoring, and Web Application Firewall (WAF) scanning.
> 
> 112                                             Computer Science & Information Technology (CS & IT)
> 
> --- PAGE BREAK ---
> 
> 3.2. Core Components
> 
> 1. Authentication and Authorization
> 
> administrative privileges. 
>  
> 2. Rate Limiting
> 
> triggered by LLMs. 
>  
> 3. Web Application Firewall (WAF)
> 
> inputs from reaching
**Section Heading**: `3.3. System Architecture` [section offsets: 18787:19407]
**First 120 words verbatim** [offsets: 18787:19577]
> 3.3. System Architecture 
>  
> Figure 1 Conceptualized below is an illustration of how MCP Guardian fits into a typical LLM-
> based workflow:
> 
> --- PAGE BREAK ---
> 
> 1. Request Interception: The LLM client submits a request specifying which MCP tool it 
> intends to call. 
> 2. Security Checks: MCP Guardian validates the request token, checks rate limits, and 
> scans for malicious patterns. 
> 3. Invocation: If the request passes these checks, the Guardian forwards it to the original 
> MCP server. 
> 4. Response Handling: The server’s response is logged and then returned to the LLM 
> client, maintaining a complete audit trail. 
>  
> 3.4. Implementation Details 
>  
> We developed our MCP Guardian reference implementation in Python, building on a standard 
> MCP server setup. The design follows a middleware
**Section Heading**: `3.4. Implementation Details` [section offsets: 19407:19748]
**First 120 words verbatim** [offsets: 19407:20276]
> 3.4. Implementation Details 
>  
> We developed our MCP Guardian reference implementation in Python, building on a standard 
> MCP server setup. The design follows a middleware approach, intercepting calls between the AI 
> client (MCP client) and underlying tool servers through a single class that applies security and 
> observability controls. 
>  
> 3.4.1. Core Classes and Methods
> 
>  
> MCPGuardian: A class overriding the default invoke_mcp_tool method. It 
> orchestrates token validation, rate limiting, WAF scanning, logging, and optional 
> administrative alerts. 
>  
> guarded_invoke_tool():A 
> custom 
> method 
> that 
> examines 
> each 
> request’s 
> parameters—such as the user token and tool arguments—applies security rules, and 
> logs relevant data. Only when all checks pass does it forward the call to the original 
> MCP server function. 
>  
> In addition to these core methods, we have

## Block 4: Evaluation Locator
**Section Heading**: `4. RESULTS` [section offsets: 25080:25336]
**First 120 words verbatim** [offsets: 25080:25947]
> 4. RESULTS 
>  
> We evaluated MCP Guardian in two primary dimensions: (a) its effectiveness at preventing or 
> mitigating malicious or unintended requests, and (b) the computational overhead introduced 
> when deployed within typical MCP-based communication. 
>  
> 4.1. Security Efficacy 
>  
> 4.1.1. Prompt Injection and Destructive Commands 
>  
> We tested scenarios where a user intentionally supplied malicious input, such as rm -rf /, hoping 
> the LLM would call a file system tool. MCP Guardian’s WAF scanning recognized the substring 
> rm\s+-rf, triggering an immediate block and returning a “Request blocked by WAF scanning” 
> message. 
>  
> High-Frequency Abuse:In a stress test, the client repeatedly invoked get_forecast 100 times in 
> quick succession. By setting a max_requests_per_token limit of 5, Guardian rejected requests 
> beyond the threshold, responding with a “429 Too
**Section Heading**: `4.2.1. Experimental Setup` [section offsets: 26720:27036]
**First 120 words verbatim** [offsets: 26720:27591]
> 4.2.1. Experimental Setup 
>  
> We conducted load tests on a VM (8-core CPU, Python 3.12) running a simple weather MCP 
> server protected by MCP Guardian. The baseline measured calls to get_forecast without the 
> Guardian, while the test scenario included the authentication, rate-limiting, and WAF scanning 
> modules. 
>  
> 4.2.2. Latency Measurements
> 
> Baseline (No MCP 
> Guardian)
> 
> MCP Guardian 
> 28.9 
> 36.7
> 
> Computer Science & Information Technology (CS & IT)                                           117
> 
> Table 1 Interpretation of Median latency and 95th percentile for different scenarios
> 
> Scenario 
> Median Latency (ms) 
> 95th 
> Percentile 
> (ms)
> 
> 25.1 
> 32.4
> 
> The Guardian introduced an absolute increase of about 3–4 ms in median latency which can be 
> observed in the Table 1 Interpretation of Median latency and 95th percentile for different 
> scenarios. This overhead primarily
**Section Heading**: `4.3. Summary of Results` [section offsets: 27997:28468]
**First 120 words verbatim** [offsets: 27997:28924]
> 4.3. Summary of Results
> 
>  
> Security: MCP Guardian effectively blocked unauthorized tokens, malicious commands 
> (e.g., drop table, rm -rf /), and excessive request rates, showcasing its robustness in 
> handling common attack patterns and resource misuse. 
>  
> Performance: The added overhead was modest, suggesting that organizations can adopt 
> MCP Guardian’s middleware approach without compromising responsiveness in typical 
> AI-driven applications.
> 
> --- PAGE BREAK ---
> 
> 5. DISCUSSION AND FUTURE WORK 
>  
> 5.1. Defense-in-Depth for Agentic AI 
>  
> MCP Guardian illustrates how established security measures—such as authentication, rate 
> limiting, and WAF scanning—can be applied to agentic workflows where Large Language 
> Models (LLMs) autonomously invoke tool APIs. Still, true defense-in-depth demands additional 
> safeguards:
> 
>  
> Sandboxing: MCP tools may be executed within containers or restricted privilege 
> environments. Even

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
**Location**: `4.2.1. Experimental Setup` [offsets: 26871:27032]
> The baseline measured calls to get_forecast without the 
> Guardian, while the test scenario included the authentication, rate-limiting, and WAF scanning 
> modules.

## Block 7: Cost Excerpts
**Location**: `4. RESULTS` [offsets: 25094:25332]
> We evaluated MCP Guardian in two primary dimensions: (a) its effectiveness at preventing or 
> mitigating malicious or unintended requests, and (b) the computational overhead introduced 
> when deployed within typical MCP-based communication.
**Location**: `4.3. Summary of Results` [offsets: 28252:28446]
>  
> Performance: The added overhead was modest, suggesting that organizations can adopt 
> MCP Guardian’s middleware approach without compromising responsiveness in typical 
> AI-driven applications.

## Block 8: Limitations
**Section Heading**: `5.4. Limitations` [section offsets: 31813:32977]
**First 120 words verbatim** [offsets: 31813:32694]
> 5.4. Limitations 
>  
> Although our results demonstrate the effectiveness of MCP Guardian in curbing malicious 
> requests and limiting resource overuse, several limitations merit attention:
> 
> 1. Regex-Based WAF: The proof-of-concept WAF relies on basic pattern matching. More 
> advanced intrusion detection (e.g., curated rulesets, ML-based classifiers) would likely 
> yield fewer false positives and a wider range of threat coverage. 
> 2. Centralized Logging: Writing logs to a local file may not scale well in large 
> deployments. Shifting to distributed log aggregation or cloud-based services can enhance 
> both reliability and query performance. 
> 3. Partial Attack Coverage: MCP Guardian cannot fully protect against a compromised 
> server or malicious code within an MCP tool itself. Complementary measures—such as 
> sandboxing and code-signing—are crucial to address deeper supply chain

## Block 9: Adaptivity Hits
no hits
