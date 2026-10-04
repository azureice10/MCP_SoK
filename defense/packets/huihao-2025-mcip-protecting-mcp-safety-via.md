# Evidence Locator Packet: huihao-2025-mcip-protecting-mcp-safety-via

- **Title**: MCIP: Protecting MCP Safety via Model Contextual Integrity Protocol
- **Year**: 2025
- **Evidence Tier**: E1
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://doi.org/10.18653/v1/2025.emnlp-main.62
- **Fulltext Path**: mcp-sok-corpus\corpus\E1_peer_reviewed\huihao-2025-mcip-protecting-mcp-safety-via\fulltext.txt
- **Character Count**: 66844

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 441:501]
> This paper proposes
> a novel framework to enhance MCP safety.
**Location**: `Abstract` [offsets: 502:728]
> Guided by the MAESTRO framework, we first
> analyze the missing safety mechanisms in MCP,
> and based on this analysis, we propose the
> Model Contextual Integrity Protocol (MCIP),
> a refined version of MCP that addresses these
> gaps.
**Location**: `Abstract` [offsets: 729:850]
> Next, we develop a fine-grained taxon-
> omy that captures a diverse range of unsafe be-
> haviors observed in MCP scenarios.
**Location**: `Abstract` [offsets: 851:1037]
> Building
> on this taxonomy, we develop benchmark and
> training data that support the evaluation and
> improvement of LLMs’ capabilities in iden-
> tifying safety risks within MCP interactions.
**Location**: `Introduction` [offsets: 4303:5025]
> we introduce the Model
> Contextual Integrity Protocol (MCIP) as a safety-
> enhanced version of MCP. In this study, we rely
> on the MAESTRO framework, which is a safety
> modeling framework for agent AI (CSA, 2025).
> Specifically, we first map MCP components to
> the corresponding MAESTRO layers to guide our
> work. From this mapping, we locate missing safety-
> related components in MCP, which are tracking
> tools and safety aware models. As a suite of safety
> models, we provide a risk taxonomy and taxonomy-
> guided data for evaluation and training.
> 
> To the best of our knowledge, this is the first
> attempt to evaluate the safety of MCP. Our work
> emphasizes putting the function calls in a multi-
> component context to decide whether

## Block 3: Method Locator
**Section Heading**: `implementation under the Apache-2.0 license` [section offsets: 36191:36988]
**First 120 words verbatim** [offsets: 36191:36953]
> implementation under the Apache-2.0 license
> Potential Risks: Our proposed taxonomy sum-
> marizes potential vulnerabilities,
> which may
> inadvertently offer insights to attackers seeking to
> exploit MCP systems. However, given the urgent
> need for a systematic safety analysis for MCP, we
> believe it is essential to share our findings in full.
> 
> Acknowledgments
> 
> The authors of this paper were supported by the
> ITSP Platform Research Project (ITS/189/23FP)
> from ITC of Hong Kong, SAR, China, and the
> AoE (AoE/E-601/24-N), the RIF (R6021-20) and
> the GRF (16205322) from RGC of Hong Kong,
> SAR, China. The work described in this paper was
> conducted in full or in part by Dr. Haoran Li, JC
> STEM Early Career Research Fellow, supported by
> The Hong Kong Jockey Club Charities

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation Metrics` [section offsets: 25013:33516]
**First 120 words verbatim** [offsets: 25013:25864]
> Evaluation Metrics
> 
> Our evaluation is based on three metrics: two that
> measure the model’s safety robustness, and one
> 
> 1182
> 
> --- PAGE BREAK ---
> 
> that assesses its practical utility:
> 
> Safety Metrics:
> Since our benchmark supports
> both binary classification (safe vs. unsafe) and
> fine-grained 11-way classification of risk types,
> we define two security evaluation metrics: Safety
> Awareness, measured by accuracy on the binary
> classification task, and Risk Resistance, measured
> by accuracy on the 11-class risk identification task.
> The ToolACE Risk Resistance is designed to evalu-
> ate the model’s generalization ability by introduc-
> ing entirely unseen functions that differ from those
> used during training.
> 
> Utility Metrics:
> Since MCIP-bench is designed
> to evaluate safety-related vulnerabilities, it is impor-
> tant to verify whether the safety-oriented

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation Metrics` [offsets: 25196:25277]
> Safety Metrics:
> Since our benchmark supports
> both binary classification (safe vs.
**Location**: `Evaluation Metrics` [offsets: 25916:26069]
> Therefore,
> we further use the BFCL-v3 benchmark (Yan et al.,
> 2024) to assess the trade-off between security ro-
> bustness and function calling capability.
**Location**: `Evaluation Metrics` [offsets: 26070:26242]
> We adopt
> the overall accuracy from the BFCL-v3 benchmark
> as a measure of the model’s utility, reflecting its
> general functional capability under non-adversarial
> conditions.

## Block 6: Baseline Excerpts
**Location**: `Evaluation Metrics` [offsets: 26692:26883]
> In this section, we conduct extensive experiments
> to evaluate the risk identification capabilities of
> state-of-the-art models, including those optimized
> for tool use and general-purpose LLMs.
**Location**: `Evaluation Metrics` [offsets: 26884:27031]
> In addition,
> we conduct ablation studies to analyze the potential
> causes of LLM vulnerabilities and to evaluate the
> effectiveness of MCIP Guardian.
**Location**: `Evaluation Metrics` [offsets: 27106:27159]
> performance across baseline models and MCIP
> Guardian.
**Location**: `Evaluation Metrics` [offsets: 27626:27756]
> Even the
> best-performing baseline, DeepSeek-R1, reached
> only 67.37%, highlighting the significant gap in
> models’ safety awareness.
**Location**: `Evaluation Metrics` [offsets: 31554:31693]
> In Section 7.2, we further conduct
> an ablation study to systematically investigate this
> trade-off between functional capability and safety.
**Location**: `Evaluation Metrics` [offsets: 31695:31779]
> 7.2
> Ablation Study
> 
> We further include ablation studies to provide
> 
> deeper insights.

## Block 7: Cost Excerpts
**Location**: `Evaluation Metrics` [offsets: 25158:25277]
> that assesses its practical utility:
> 
> Safety Metrics:
> Since our benchmark supports
> both binary classification (safe vs.
**Location**: `Evaluation Metrics` [offsets: 25719:25915]
> Utility Metrics:
> Since MCIP-bench is designed
> to evaluate safety-related vulnerabilities, it is impor-
> tant to verify whether the safety-oriented design of
> the MCIP Guardian affects its usability.
**Location**: `Evaluation Metrics` [offsets: 26070:26242]
> We adopt
> the overall accuracy from the BFCL-v3 benchmark
> as a measure of the model’s utility, reflecting its
> general functional capability under non-adversarial
> conditions.
**Location**: `Evaluation Metrics` [offsets: 28070:28212]
> One possi-
> ble explanation is that these models tend to over-
> approve, lacking sufficient discrimination between
> benign and adversarial calls.
**Location**: `Evaluation Metrics` [offsets: 29050:29101]
> LLMs appear to exhibit a safety–utility trade-
> off.
**Location**: `Evaluation Metrics` [offsets: 29102:29210]
> We examine the dual dimensions of utility
> and safety, measured by BFCL overall accuracy
> and Risk Resistance.

## Block 8: Limitations
**Section Heading**: `Limitations` [section offsets: 34236:36191]
**First 120 words verbatim** [offsets: 34236:35088]
> Limitations
> 
> Our method does not simulate or enumerate spe-
> cific adversarial attack strategies. While our tax-
> onomy accounts for potential risks by considering
> malicious sources and plausible threat goals, the
> framework itself does not explicitly capture the
> full diversity of concrete attack techniques, such
> as prompt injection variants or malicious payload
> construction. We leave the integration of adaptive
> threat modeling and dynamic adversarial training
> as promising directions for future work. In addition,
> while our training method significantly improves
> the model’s ability to identify specific risks, the
> absolute performance, 54.16% on the risk resis-
> tance metric, still leaves room for improvement.
> Future work could explore more fine-grained su-
> pervision or targeted training strategies to enhance
> the model’s sensitivity to risk types

## Block 9: Adaptivity Hits
**Matched Term**: `Evasion` | **Location**: `MCI Definition` [offsets: 17858:18133]
> privilege escalation.
> Evasion
> Single-flow
> Server
> Expired 
> Privilege 
> Redundancy
> 
> Termination
> 
> configurations cause persistent errors.
> Drift
> Inter-flow
> Server
> Configuration
> 
> Drift
> 
> principle)
> Client
> Server
> Version 
> Mismatch
> 
> a verification step should precede any data access.
**Matched Term**: `adaptive` | **Location**: `Limitations` [offsets: 34333:34949]
> While our tax-
> onomy accounts for potential risks by considering
> malicious sources and plausible threat goals, the
> framework itself does not explicitly capture the
> full diversity of concrete attack techniques, such
> as prompt injection variants or malicious payload
> construction. We leave the integration of adaptive
> threat modeling and dynamic adversarial training
> as promising directions for future work. In addition,
> while our training method significantly improves
> the model’s ability to identify specific risks, the
> absolute performance, 54.16% on the risk resis-
> tance metric, still leaves room for improvement.
