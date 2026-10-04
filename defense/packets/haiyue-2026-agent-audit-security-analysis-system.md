# Evidence Locator Packet: haiyue-2026-agent-audit-security-analysis-system

- **Title**: Agent Audit: A Security Analysis System for LLM Agent Applications
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2603.22853
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\haiyue-2026-agent-audit-security-analysis-system\fulltext.txt
- **Character Count**: 25929

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 656:734]
> We present Agent Audit, a security analysis system for LLM
> agent applications.
**Location**: `Introduction` [offsets: 6230:7094]
> we present
> Agent Audit, a security analysis system for LLM agent applica-
> tions. Agent Audit analyzes Python agent code and deployment
> artifacts through a multi-scanner pipeline that combines AST-based
> dataflow analysis, credential detection, structured configuration
> parsing, and privilege-risk checks. The system produces findings in
> terminal, JSON, Markdown, and SARIF formats, making it suitable
> for both local use and CI/CD workflows.
> Demo plan. In the live demonstration (§4), attendees scan real-
> world agent repositories and observe how Agent Audit identifies
> security risks across tool functions, prompt construction paths, and
> MCP deployment configurations. Findings are linked to source lo-
> cations and configuration paths, exportable to VS Code and GitHub
> Code Scanning for interactive triage. We also demonstrate the
> inspect subcommand, which connects

## Block 3: Method Locator
**Section Heading**: `Limitations. The current implementation is scoped to intra-` [section offsets: 17248:20593]
**First 120 words verbatim** [offsets: 17248:18037]
> Limitations. The current implementation is scoped to intra-
> procedural taint analysis; inter-procedural data flow across func-
> tion boundaries is not tracked. Python is the primary analysis
> target; TypeScript and JavaScript receive only regex-level scanning.
> Agent Audit detects code-level vulnerability patterns but does not
> execute or simulate runtime prompt injection payloads. Confidence
> 
> --- PAGE BREAK ---
> 
> thresholds are calibrated empirically rather than derived from a
> formal model.
> 
> 100
> 100
> 100
> 
> 85.7
> 
> 80
> 
> Recall (%)
> 
> 57.9
> 
> 60
> 
> 47.4
> 
> 40
> 
> 20
> 
> 0
> 7.1
> 
> 0
> 0
> 
> Set A
> Set B
> Set C
> 0
> 
> Agent Audit
> Semgrep
> Bandit
> 
> Figure 3: Per-set recall comparison on AVB. Agent Audit
> achieves 100% recall on injection/RCE and MCP vulnerability
> sets, where existing tools have limited or zero coverage.
> 
> 4

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation` [section offsets: 13948:17248]
**First 120 words verbatim** [offsets: 13948:14882]
> Evaluation
> 3.1
> Agent-Vuln-Bench (AVB)
> 
> We construct Agent-Vuln-Bench (AVB), an SWE-bench-style bench-
> mark for evaluating AI agent security scanners. AVB contains
> 22 samples organized into three vulnerability sets—injection/RCE
> (Set A, 19 vulnerabilities), MCP/components (Set B, 9), and data/au-
> thentication (Set C, 14)—with 42 expert-annotated vulnerabilities
> serving as the oracle. Samples are drawn from CVE reproductions,
> real-world agent vulnerability patterns, and MCP configuration
> attacks. The KNOWN subset includes reproductions of critical
> 
> CVEs such as LangChain’s LLMMathChain eval() injection [6]
> and PythonREPLTool remote code execution [7]. The WILD sub-
> set captures vulnerability patterns discovered in production agent
> code, including calculator tools with unsandboxed eval(), web-
> fetcher tools with SSRF via user-controlled URLs, and agent self-
> modification through dynamic importlib usage. Three samples
> target

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation` [offsets: 15128:15320]
> Agent Audit achieves 95.24%
> recall and 86.96% precision (F1 = 0.909) on the 42-vulnerability AVB
> benchmark, compared to 23.8% recall for Semgrep (F1 = 0.385) and
> 29.7% for Bandit (F1 = 0.458).
**Location**: `Evaluation` [offsets: 17133:17246]
> Scan time scales linearly with codebase size, with the full
> test suite (25,582 lines) completing in 1.27 seconds.

## Block 6: Baseline Excerpts
**Location**: `Evaluation` [offsets: 14862:15014]
> Three samples
> target MCP-specific supply-chain attacks: tool shadowing across
> MCP servers, tool description poisoning, and baseline configuration
> drift.
**Location**: `Evaluation` [offsets: 15128:15320]
> Agent Audit achieves 95.24%
> recall and 86.96% precision (F1 = 0.909) on the 42-vulnerability AVB
> benchmark, compared to 23.8% recall for Semgrep (F1 = 0.385) and
> 29.7% for Bandit (F1 = 0.458).

## Block 7: Cost Excerpts
**Location**: `Evaluation` [offsets: 15128:15320]
> Agent Audit achieves 95.24%
> recall and 86.96% precision (F1 = 0.909) on the 42-vulnerability AVB
> benchmark, compared to 23.8% recall for Semgrep (F1 = 0.385) and
> 29.7% for Bandit (F1 = 0.458).
**Location**: `Evaluation` [offsets: 15881:16201]
> True Positives
> 40
> 10
> 11
> False Negatives
> 2
> 32
> 26
> False Positives
> 6
> 0
> 0
> 
> Recall
> 95.24%
> 23.8%
> 29.7%
> Precision
> 86.96%
> 100.0%
> 100.0%
> F1 Score
> 0.909
> 0.385
> 0.458
> 
> Exclusive detections
> 30
> 0
> 1
> MCP vuln coverage
> 100%
> 0%
> 0%
> OWASP ASI coverage
> 10/10
> ∼1/10
> ∼1/10
> 
> Figure 3 breaks down detection performance by vulnerability
> category.
**Location**: `Evaluation` [offsets: 15952:16201]
> Recall
> 95.24%
> 23.8%
> 29.7%
> Precision
> 86.96%
> 100.0%
> 100.0%
> F1 Score
> 0.909
> 0.385
> 0.458
> 
> Exclusive detections
> 30
> 0
> 1
> MCP vuln coverage
> 100%
> 0%
> 0%
> OWASP ASI coverage
> 10/10
> ∼1/10
> ∼1/10
> 
> Figure 3 breaks down detection performance by vulnerability
> category.
**Location**: `Evaluation` [offsets: 16506:16671]
> Semgrep and Bandit achieve 100% precision because they de-
> tect so few agent-specific vulnerabilities (10 and 11 TPs respectively,
> missing 32 and 26 oracle entries).
**Location**: `Evaluation` [offsets: 16672:16870]
> Agent Audit’s six false positives
> (precision 86.96%) arise from MCP configuration heuristics flagging
> safe patterns—an acceptable trade-off given the 4× recall advantage
> and 30 exclusive detections.
**Location**: `Evaluation` [offsets: 16885:17060]
> Agent Audit scans 22,009 lines of Python in
> 0.87 seconds (25,000 lines/sec), matching Bandit’s speed (0.90s)
> while being 6.9× faster than Semgrep (5.94s) on the same codebase.

## Block 8: Limitations
**Section Heading**: `Limitations. The current implementation is scoped to intra-` [section offsets: 17248:20593]
**First 120 words verbatim** [offsets: 17248:18037]
> Limitations. The current implementation is scoped to intra-
> procedural taint analysis; inter-procedural data flow across func-
> tion boundaries is not tracked. Python is the primary analysis
> target; TypeScript and JavaScript receive only regex-level scanning.
> Agent Audit detects code-level vulnerability patterns but does not
> execute or simulate runtime prompt injection payloads. Confidence
> 
> --- PAGE BREAK ---
> 
> thresholds are calibrated empirically rather than derived from a
> formal model.
> 
> 100
> 100
> 100
> 
> 85.7
> 
> 80
> 
> Recall (%)
> 
> 57.9
> 
> 60
> 
> 47.4
> 
> 40
> 
> 20
> 
> 0
> 7.1
> 
> 0
> 0
> 
> Set A
> Set B
> Set C
> 0
> 
> Agent Audit
> Semgrep
> Bandit
> 
> Figure 3: Per-set recall comparison on AVB. Agent Audit
> achieves 100% recall on injection/RCE and MCP vulnerability
> sets, where existing tools have limited or zero coverage.
> 
> 4

## Block 9: Adaptivity Hits
no hits
