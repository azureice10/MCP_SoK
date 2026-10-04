# Evidence Locator Packet: tarek-2025-bridging-ai-software-security-comparative

- **Title**: Bridging AI and Software Security: A Comparative Vulnerability Assessment of LLM Agent Deployment Paradigms
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: survey_review
- **Link**: https://arxiv.org/abs/2507.06323
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\tarek-2025-bridging-ai-software-security-comparative\fulltext.txt
- **Character Count**: 92231

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 8552:8681]
> The remainder of this paper is structured as follows: Section 2 reviews related work, establishing
> 
> the foundation for our study.
**Location**: `Abstract` [offsets: 9494:9606]
> This section synthesizes existing literature to contextualize our contribution
> 
> tical implementation guidelines.

## Block 3: Method Locator
**Section Heading**: `Methodology` [section offsets: 14901:25281]
**First 120 words verbatim** [offsets: 14901:15882]
> Methodology
> 
> challenges posed by LLM agent systems.
> 
> 3.1
> Testing Framework
> 
> 6
> 
> ployment architectures. We present a comprehensive methodology encompassing threat modeling,
> 
> attack simulation, test scenario generation, and evaluation metrics. Our approach builds upon es-
> 
> tablished security assessment frameworks [12, 13, 17] while extending them to address the unique
> 
> Our testing framework (Figure 2) consists of five phases: Domain Initialization (finance/healthcare
> 
> contexts), Deployment Paradigm Selection (Function Calling/MCP), Attack Execution (mapping
> 
> surfaces and progression models), Test Scenario Implementation (CIA-centric testing with LLM-
> 
> driven automation), and Evaluation Metrics (ASR/RR measurement with LLM-as-judge valida-
> 
> tion). This pipeline bridges theoretical threat modeling with practical security validation.
> 
> --- PAGE BREAK ---
> 
> Figure 2: Testing Framework Methodology Workflow
> 
> 3.2
> Threat Modeling and Attack Simulation Framework
> 
> Function Calling
**Section Heading**: `Implementation` [section offsets: 32712:32798]
**First 120 words verbatim** [offsets: 32712:33803]
> Implementation
> 
> security evaluation while ensuring experimental reproducibility.
> 
> 4.1
> Architecture Selection and Experimental Design
> 
> versus separated security contexts.
> 
> infrastructure applications with high security requirements [37].
> 
> 4.2
> Comparative Architectural Analysis
> 
> distribution and vulnerability propagation.
> 
> 4.2.1
> Function Calling Architecture
> 
> cloud-hosted LLM services accessed through Azure’s unified API gateway.
> 
> 16
> 
> to design paradigms rather than implementation artifacts. Both systems utilize identical language
> 
> models hosted via Azure/AWS, equivalent tool schemas and functionality, and standardized in-
> 
> put processing mechanisms. We deliberately employed default configurations as recommended in
> 
> official documentation [38], avoiding custom security enhancements to ensure that observed vulner-
> 
> abilities reflect intrinsic architectural characteristics rather than implementation-specific variations.
> 
> Domain-specific tools from financial and healthcare sectors were incorporated to represent critical
> 
> The fundamental architectural distinction between paradigms
**Section Heading**: `Architecture Selection and Experimental Design` [section offsets: 32798:38414]
**First 120 words verbatim** [offsets: 32798:33851]
> Architecture Selection and Experimental Design
> 
> versus separated security contexts.
> 
> infrastructure applications with high security requirements [37].
> 
> 4.2
> Comparative Architectural Analysis
> 
> distribution and vulnerability propagation.
> 
> 4.2.1
> Function Calling Architecture
> 
> cloud-hosted LLM services accessed through Azure’s unified API gateway.
> 
> 16
> 
> to design paradigms rather than implementation artifacts. Both systems utilize identical language
> 
> models hosted via Azure/AWS, equivalent tool schemas and functionality, and standardized in-
> 
> put processing mechanisms. We deliberately employed default configurations as recommended in
> 
> official documentation [38], avoiding custom security enhancements to ensure that observed vulner-
> 
> abilities reflect intrinsic architectural characteristics rather than implementation-specific variations.
> 
> Domain-specific tools from financial and healthcare sectors were incorporated to represent critical
> 
> The fundamental architectural distinction between paradigms lies in their approach to tool or-
> 
> chestration
**Section Heading**: `Implementation Validation and Limitations` [section offsets: 38414:43773]
**First 120 words verbatim** [offsets: 38414:39399]
> Implementation Validation and Limitations
> 
> properties and provide essential context for interpreting our evaluation results.
> 
> 5
> Experimental Setup
> 
> experimental configuration for comprehensive security assessment.
> 
> 5.1
> Systematic Test Case Generation
> 
> Table 2: Representative Attack Test Cases Across Security Objectives
> 
> Attack
> Sur-
> face
> 
> CIA
> Tar-
> get
> 
> Test
> Case
> De-
> scription
> 
> System
> Prompt (S)
> 
> Integrity
> Instruction
> override
> attempts
> 
> User
> Prompt
> (U)
> 
> ConfidentialityInformation
> extrac-
> tion queries
> 
> Tool
> Output
> (O)
> 
> Integrity
> Embedded command
> injection
> 
> Function
> Name (Fn)
> 
> Availability
> Malformed
> function
> calls
> 
> Tool Set (T)
> Integrity
> Unauthorized
> tool
> injection
> 
> 18
> 
> Example Implementation
> 
> “Ignore previous instructions and
> follow: [malicious directive]”
> 
> “Show me your system instructions
> and previous prompts”
> 
> Tool responses containing hidden in-
> structions for subsequent processing
> 
> Deliberately corrupted JSON with
> special characters
> 
> Addition of malicious tools mimick-

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation Framework` [section offsets: 30506:32712]
**First 120 words verbatim** [offsets: 30506:31395]
> Evaluation Framework
> 
> security evaluation).
> 
> 15
> 
> principle. This systematic approach ensures that each attack vector is tested in isolation while
> 
> Our secondary strategy employs a separate LLM as an adversarial agent to generate sophisti-
> 
> cated attack scenarios. This approach extends prior work on AI-assisted penetration testing [33,
> 
> 34] by leveraging the creative capabilities of LLMs to discover subtle vulnerabilities that con-
> 
> ventional testing might miss.
> The adversarial LLM explores all defined attack vectors:
> A =
> 
> Through iterative scenario generation, it produces realistic attack patterns that reflect sophisti-
> 
> cated adversarial thinking. This automated approach revealed attack combinations and edge cases
> 
> To assess the security robustness of LLM-based agents across different architectural paradigms, we
> 
> employ two complementary metrics: Attack Success Rate (ASR) and
**Section Heading**: `Results` [section offsets: 43773:54521]
**First 120 words verbatim** [offsets: 43773:44718]
> Results
> 
> trade-offs and attack progression patterns in LLM-based agent systems.
> 
> 6.1
> Comparative Vulnerability Assessment
> 
> individual language models.
> 
> 6.1.1
> Architectural Vulnerability Exposure
> 
> in each architecture’s susceptibility to different attack vectors.
> 
> 20
> 
> architecture-specific vulnerability patterns that reflect fundamental design differences between cen-
> 
> tralized and distributed approaches. Table 3 summarizes our findings on vulnerability exposure
> 
> across Function Calling and Model Context Protocol implementations, revealing distinct patterns
> 
> --- PAGE BREAK ---
> 
> Table 3: Comparative Vulnerability Exposure Across Architectures
> 
> Vulnerability Type
> Related
> Threat ID
> 
> Prompt
> Injection
> at
> System Level (S)
> 
> Prompt
> Injection
> at
> User Level (U)
> 
> T1, T2, T5,
> T7
> 
> Indirect Prompt Injec-
> tion (O)
> 
> T1, T2, T5,
> T8
> 
> JSON Injection (Fp)
> T4, T7
> •
> •
> •
> 
> JSON
> Injection
> (Fn(Fp))
> 
> Man-in-the-Middle:
> tool_choice API (Fn)
> 
> Man-in-the-Middle:

## Block 5: Attack-Set Excerpts
**Location**: `Results` [offsets: 54023:54145]
> against three state-of-the-art security benchmarks: AgentDojo [16], InjecAgent [15], and Agent
> 
> Security Bench (ASB) [10].

## Block 6: Baseline Excerpts
**Location**: `Evaluation Framework` [offsets: 30770:30971]
> This approach extends prior work on AI-assisted penetration testing [33,
> 
> 34] by leveraging the creative capabilities of LLMs to discover subtle vulnerabilities that con-
> 
> ventional testing might miss.
**Location**: `Results` [offsets: 45795:45841]
> overall ASR of 73.5% compared to MCP’s 62.59%.
**Location**: `Results` [offsets: 48622:48709]
> superior initial threat detection, averaging 17.8% RR compared to non-reasoning models.
**Location**: `Results` [offsets: 53061:53151]
> 6.3
> Baseline Comparison with Established Security Frameworks
> 
> gaps in current evaluations.
**Location**: `Results` [offsets: 54023:54145]
> against three state-of-the-art security benchmarks: AgentDojo [16], InjecAgent [15], and Agent
> 
> Security Bench (ASB) [10].

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
**Section Heading**: `Implementation Validation and Limitations` [section offsets: 38414:43773]
**First 120 words verbatim** [offsets: 38414:39399]
> Implementation Validation and Limitations
> 
> properties and provide essential context for interpreting our evaluation results.
> 
> 5
> Experimental Setup
> 
> experimental configuration for comprehensive security assessment.
> 
> 5.1
> Systematic Test Case Generation
> 
> Table 2: Representative Attack Test Cases Across Security Objectives
> 
> Attack
> Sur-
> face
> 
> CIA
> Tar-
> get
> 
> Test
> Case
> De-
> scription
> 
> System
> Prompt (S)
> 
> Integrity
> Instruction
> override
> attempts
> 
> User
> Prompt
> (U)
> 
> ConfidentialityInformation
> extrac-
> tion queries
> 
> Tool
> Output
> (O)
> 
> Integrity
> Embedded command
> injection
> 
> Function
> Name (Fn)
> 
> Availability
> Malformed
> function
> calls
> 
> Tool Set (T)
> Integrity
> Unauthorized
> tool
> injection
> 
> 18
> 
> Example Implementation
> 
> “Ignore previous instructions and
> follow: [malicious directive]”
> 
> “Show me your system instructions
> and previous prompts”
> 
> Tool responses containing hidden in-
> structions for subsequent processing
> 
> Deliberately corrupted JSON with
> special characters
> 
> Addition of malicious tools mimick-

## Block 9: Adaptivity Hits
**Matched Term**: `Evasion` | **Location**: `2. Attack surfaces as defined in Section 3.2.1 (As = {S, U, T, Fn, Fp, O, R})` [offsets: 27606:29131]
> Spoofing &
> Information
> Disclosure
> 
> T9
> Governance
> Evasion
> &
> Obfuscation
> 
> Governance
> Evasion
> &
> Obfuscation
> 
> 14
> 
> Description
> Attack
> Surface
> 
> Attack
> Vector
> 
> Malicious inputs manipu-
> late LLM planning to exe-
> cute harmful actions
> 
> S, U, O
> Ap, Aipi
> 
> Compromise
> knowledge
> with
> false
> or
> distorted
> information later retrieved
> as truth
> 
> U, O
> Ap, Aipi
> 
> Modifying
> tool
> in-
> terface
> definitions
> (names/parameters)
> 
> T
> AMitM,
> ATi
> 
> Manipulate system to in-
> voke tools outside autho-
> rized scope or with over-
> broad parameters
> 
> Fn, Fp
> AJSON,
> AMitM
> 
> Secrets or private data leak
> in LLM response
> 
> S, U, T,
> O
> 
> ATi,
> Ap,
> Aipi
> 
> Crafted inputs explode to-
> ken count, force expensive
> queries or infinite loops
> 
> S, U, T,
> Fn
> 
> Spoofing
> Credentials, headers or to-
> kens stolen/forged for priv-
> ilege escalation
> 
> S, U, T,
> O
> 
> Ap,
> Aipi,
> ATi
> 
> Model outputs coerce users
> into unsafe actions, bypass-
> ing technical policy
> 
> O
> Aipi
> 
> Repudiation
> Attacker
> fragments
> prompts/calls so no single
> log shows full context
> 
> As
> A
> 
> ADoS,
> AMitM,
> ATi
> T7
> Identity
> Spoofing
> &
> Trust
> Ex-
> ploitation
> 
> As shown in Table 1, the framework captures both traditional software vulnerabilities (T3,
> 
> T4) that exploit conventional attack vectors on tool layers and function interfaces, and novel AI-
> 
> specific threats (T1, T2, T8) that leverage LLM capabilities for sophisticated manipulation. This
> 
> comprehensive taxonomy enables systematic vulnerability assessment across different deployment
> 
> paradigms while maintaining compatibility with established security evaluation methodologies.
**Matched Term**: `Evasion` | **Location**: `2. Attack surfaces as defined in Section 3.2.1 (As = {S, U, T, Fn, Fp, O, R})` [offsets: 27641:29131]
> T9
> Governance
> Evasion
> &
> Obfuscation
> 
> Governance
> Evasion
> &
> Obfuscation
> 
> 14
> 
> Description
> Attack
> Surface
> 
> Attack
> Vector
> 
> Malicious inputs manipu-
> late LLM planning to exe-
> cute harmful actions
> 
> S, U, O
> Ap, Aipi
> 
> Compromise
> knowledge
> with
> false
> or
> distorted
> information later retrieved
> as truth
> 
> U, O
> Ap, Aipi
> 
> Modifying
> tool
> in-
> terface
> definitions
> (names/parameters)
> 
> T
> AMitM,
> ATi
> 
> Manipulate system to in-
> voke tools outside autho-
> rized scope or with over-
> broad parameters
> 
> Fn, Fp
> AJSON,
> AMitM
> 
> Secrets or private data leak
> in LLM response
> 
> S, U, T,
> O
> 
> ATi,
> Ap,
> Aipi
> 
> Crafted inputs explode to-
> ken count, force expensive
> queries or infinite loops
> 
> S, U, T,
> Fn
> 
> Spoofing
> Credentials, headers or to-
> kens stolen/forged for priv-
> ilege escalation
> 
> S, U, T,
> O
> 
> Ap,
> Aipi,
> ATi
> 
> Model outputs coerce users
> into unsafe actions, bypass-
> ing technical policy
> 
> O
> Aipi
> 
> Repudiation
> Attacker
> fragments
> prompts/calls so no single
> log shows full context
> 
> As
> A
> 
> ADoS,
> AMitM,
> ATi
> T7
> Identity
> Spoofing
> &
> Trust
> Ex-
> ploitation
> 
> As shown in Table 1, the framework captures both traditional software vulnerabilities (T3,
> 
> T4) that exploit conventional attack vectors on tool layers and function interfaces, and novel AI-
> 
> specific threats (T1, T2, T8) that leverage LLM capabilities for sophisticated manipulation. This
> 
> comprehensive taxonomy enables systematic vulnerability assessment across different deployment
> 
> paradigms while maintaining compatibility with established security evaluation methodologies.
**Matched Term**: `Evasion` | **Location**: `implementation.` [offsets: 66462:67139]
> 32
> 
> classification engines [49] operating outside LLM control, and T9 (Governance Evasion) requiring
> 
> Core Defense Principles
> Effective protection requires: (1) defense in depth with independent
> 
> validation layers, (2) state isolation through regular resets and stateless processing, and (3) security
> 
> checks independent of potentially compromised components. Organizations should validate defenses
> 
> using our attack progression model, particularly against composed and chained patterns targeting
> 
> Our analysis provides comprehensive insights into LLM agent security across architectural paradigms,
> 
> but several factors constrain the generalizability and scope of our findings.
