# Evidence Locator Packet: yiheng-2026-component-manipulation-system-compromise-understanding

- **Title**: From Component Manipulation to System Compromise: Understanding and Detecting Malicious MCP Servers
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2604.01905
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\yiheng-2026-component-manipulation-system-compromise-understanding\fulltext.txt
- **Character Count**: 124713

## Block 2: Contribution Sentences
**Location**: `INTRODUCTION` [offsets: 8166:9057]
> we propose and implement a two-stage approach Connor that detects malicious MCP
> 
> servers through behavioral deviation analysis. The first stage conducts pre-execution analysis to identify malicious shell
> 
> commands embedded in the server’s configuration and extract each tool’s function intent. The second stage performs
> 
> in-execution analysis that invokes tools in a simulated host and detects deviations between the traced behavior and the
> 
> function intent via step-wise trajectory-based analysis. Crucially, Connor identifies the deviation at each interaction
> 
> step rather than waiting for the complete execution, enabling early termination of detection. Further, unlike prior work
> 
> that examines isolated steps, Connor traces multi-step execution trajectories to detect compositional attacks where
> 
> We compare Connor to three state-of-the-art detectors [2, 40, 66] on our curated dataset;

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
**Section Heading**: `EVALUATION` [section offsets: 80319:80436]
**First 120 words verbatim** [offsets: 80319:81141]
> EVALUATION
> 
> LLM.
> 
> We design three research questions to evaluate Connor.
> 
> by the step-wise detection mechanism?
> 
> 6.1
> Evaluation Setup
> 
> Manuscript submitted to ACM
> 
> We have implemented Connor in 9k lines of Python code. For the code slicing module, we employ Joern [42] to perform
> 
> static analysis and generate CPG. The simulated host is built upon the LangChain framework [46] to orchestrate
> 
> multi-step agent interactions. Our implementation adopts an LLM deployment strategy based on security characteristics.
> 
> Specifically, for the interactive agent within the simulated host, we select Claude Sonnet 4.0 [8], as it exhibits the
> 
> highest ASR in our attack effectiveness evaluations (see Sec. 4.2), making it more susceptible to trigger malicious
> 
> behaviors and thereby enabling more effective detection of the potential
**Section Heading**: `Evaluation Setup` [section offsets: 80436:87850]
**First 120 words verbatim** [offsets: 80436:81278]
> Evaluation Setup
> 
> Manuscript submitted to ACM
> 
> We have implemented Connor in 9k lines of Python code. For the code slicing module, we employ Joern [42] to perform
> 
> static analysis and generate CPG. The simulated host is built upon the LangChain framework [46] to orchestrate
> 
> multi-step agent interactions. Our implementation adopts an LLM deployment strategy based on security characteristics.
> 
> Specifically, for the interactive agent within the simulated host, we select Claude Sonnet 4.0 [8], as it exhibits the
> 
> highest ASR in our attack effectiveness evaluations (see Sec. 4.2), making it more susceptible to trigger malicious
> 
> behaviors and thereby enabling more effective detection of the potential attacks. For Config Analyzer, Intent Inspector,
> 
> Intent-Aligned Query Generator, Code Semantic Generator, and Behavior Deviation Judger,

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation Setup` [offsets: 81651:81670]
> Dataset Collection.
**Location**: `Evaluation Setup` [offsets: 81764:81969]
> patterns, our malicious dataset comprises 114 PoC servers we developed, together with 20 publicly available malicious
> 
> PoC servers from existing research [30, 34, 65, 72], totaling 134 malicious instances.
**Location**: `Evaluation Setup` [offsets: 82606:82687]
> their PoCs were not yet publicly available at the time of our dataset collection.
**Location**: `Evaluation Setup` [offsets: 82688:82760]
> For the benign dataset, we employed
> 
> --- PAGE BREAK ---
> 
> 22
> Huang et al.
**Location**: `Evaluation Setup` [offsets: 83701:83741]
> We run all tools on the curated dataset.
**Location**: `Evaluation Setup` [offsets: 84595:84829]
> curated dataset, i.e., (1) ablating Config Analyzer; (2) ablating Intent Inspector; (3) ablating Code Semantic Generator; and
> 
> (4) replacing sliced code with the full, unsliced tool source code to assess the necessity of code slicing.

## Block 6: Baseline Excerpts
**Location**: `Evaluation Setup` [offsets: 81310:81424]
> • RQ4: Effectiveness Evaluation: How is the effectiveness of Connor, compared to state-of-the-art detection tools?
**Location**: `Evaluation Setup` [offsets: 81426:81535]
> • RQ5: Ablation Study: What is the contribution of each key component to the overall effectiveness of Connor?
**Location**: `Evaluation Setup` [offsets: 83238:83265]
> State-of-the-Art Selection.
**Location**: `Evaluation Setup` [offsets: 83266:83424]
> We select baseline detection tools based on two criteria, i.e., (1) open-source, and
> 
> (2) analyze entire MCP server packages not just detect prompt injection.
**Location**: `Evaluation Setup` [offsets: 83425:83552]
> We identify three state-of-the-art tools
> 
> satisfying these criteria, i.e., MCP-Scan [40], AI-Infra-Guard [66], and MCPScan [2].
**Location**: `Evaluation Setup` [offsets: 85437:85484]
> forms all baseline approaches by 8.9% to 59.6%.

## Block 7: Cost Excerpts
**Location**: `Evaluation Setup` [offsets: 81537:81670]
> • RQ6: Usefulness Evaluation: How useful is Connor in real-world detections, and what is the overhead introduced
> 
> Dataset Collection.
**Location**: `Evaluation Setup` [offsets: 82688:82760]
> For the benign dataset, we employed
> 
> --- PAGE BREAK ---
> 
> 22
> Huang et al.
**Location**: `Evaluation Setup` [offsets: 83148:83236]
> From these, we randomly sampled 130 servers and manually verified that they were benign.
**Location**: `Evaluation Setup` [offsets: 83928:83989]
> We evaluate effectiveness by precision, recall, and F1-score.
**Location**: `Evaluation Setup` [offsets: 84221:84483]
> Tool
> Precision
> Recall
> F1-Score
> 
> MCP-Scan [40]
> 60.5%
> 58.2%
> 59.3%
> AI-Infra-Guard[66]
> 81.8%
> 91.0%
> 86.2%
> MCPScan [2]
> 75.0%
> 69.4%
> 72.1%
> Connor
> 98.4%
> 91.1%
> 94.6%
> 
> measure the detection overhead of Connor to assess the practicality of the step-wise detection mechanism.
**Location**: `Evaluation Setup` [offsets: 84378:84483]
> measure the detection overhead of Connor to assess the practicality of the step-wise detection mechanism.

## Block 8: Limitations
**Location**: `RELATED WORK`
**First 120 words verbatim** [offsets: 97018:97874]
> Limitations. First, we require that the MCP server can run without configuration. This improves fidelity but
> 
> reduces applicability to servers that require setup or interaction. A practical pattern is to manually configure such
> 
> servers before running our pipeline, which requires human effort. Accordingly, a promising direction is to combine our
> 
> proxy-based analysis with complementary static detectors to strengthen defenses. Second, since we rely on behavioral
> 
> deviation, attacks whose malicious logic is not exercised at runtime may evade detection. Third, tool metadata can
> 
> affect results, as incomplete or ambiguous tool descriptions may increase false positives by obscuring intended behavior.
> 
> Fourth, in the simulated-host scenario, queries are generated per tool based on its function intent, and thus attacks that
> 
> distribute malicious logic

## Block 9: Adaptivity Hits
**Matched Term**: `evade` | **Location**: `LLM Provider` [offsets: 48566:49097]
> By splitting malicious logic across different components, e.g., embedding partial attack logic
> 
> in prompt injections while completing the attack through source code execution, attackers can evade LLM inherent
> 
> defenses that would detect malicious intent in any single component. For example, P3 and P7 demonstrate this strategy
> 
> by designing PoCs concatenating sensitive paths to tool arguments via prompt injection, while the tool source code
> 
> implements conditional logic to parse these arguments and trigger malicious behaviors.
**Matched Term**: `evade` | **Location**: `LLM Provider` [offsets: 58459:58583]
> 5.1
> Pre-Execution Analysis
> 
> or operator reordering) to evade rule-based detection.
> 
> installation to prevent potential risks.
**Matched Term**: `evade` | **Location**: `RELATED WORK` [offsets: 97448:97722]
> Second, since we rely on behavioral
> 
> deviation, attacks whose malicious logic is not exercised at runtime may evade detection. Third, tool metadata can
> 
> affect results, as incomplete or ambiguous tool descriptions may increase false positives by obscuring intended behavior.
**Matched Term**: `evade` | **Location**: `RELATED WORK` [offsets: 97848:98099]
> distribute malicious logic across multiple tools (requiring a specific user-driven invocation sequence to trigger) may
> 
> not be exercised and thus evade detection. In the proxy-based deployment on a real host, Connor can be deployed to
> 
> MCP Ecosystems.
