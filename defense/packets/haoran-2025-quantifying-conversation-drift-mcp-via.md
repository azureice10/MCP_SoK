# Evidence Locator Packet: haoran-2025-quantifying-conversation-drift-mcp-via

- **Title**: Quantifying Conversation Drift in MCP via Latent Polytope
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2508.06418
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\haoran-2025-quantifying-conversation-drift-mcp-via\fulltext.txt
- **Character Count**: 44170

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 988:1188]
> To address these limitations, we propose SECMCP,
> a secure framework that detects and quantifies conversation
> drift, deviations in latent space trajectories induced by ad-
> versarial external knowledge.
**Location**: `Abstract` [offsets: 1401:1634]
> We evaluate SECMCP on three state-of-the-art LLMs
> (Llama3, Vicuna, Mistral) across benchmark datasets (MS
> MARCO, HotpotQA, FinQA), demonstrating robust detec-
> tion with AUROC scores exceeding 0.915 while maintaining
> system usability.
**Location**: `Abstract` [offsets: 1635:1841]
> Our contributions include a systematic cate-
> gorization of MCP security threats, a novel latent polytope-
> based methodology for quantifying conversation drift, and
> empirical validation of SECMCP’s efficacy.
**Location**: `Introduction` [offsets: 4677:5511]
> we propose SECMCP, a
> secure MCP framework that detects and quantifies con-
> versation drift induced by adversarial external knowledge.
> Our key insight is that adversarial instructions, while of-
> ten benign in surface text, activate distinct clusters of neu-
> rons in the latent space, thereby shifting the trajectory
> of conversation generation. Building on this observation,
> SECMCP
> leverages activation vector representations of
> LLM queries and models conversational dynamics within
> a latent polytope space. By quantifying deviations from ex-
> 
> --- PAGE BREAK ---
> 
> Local Data   &  Remote Services
> User
> 
> Prompt: Email me 
> my top 3 GitHub 
> repos by stars.
> 
> MCP Hosts
> 
> MCP Clients
> 
> Commu-
> 
> AI Agents,
> 
> nication Sampling
> 
> IDEs, …
> 
> pected conversational trajectories, SECMCP enables proac-
> tive detection of data exfiltration, misleading, and

## Block 3: Method Locator
**Section Heading**: `method.` [section offsets: 31211:32598]
**First 120 words verbatim** [offsets: 31211:31934]
> method.
> 
> Number of Anchor Samples
> In the detection process of
> SECMCP, a certain number of anchor samples are required
> to compute the distances between the activation vectors of
> benign samples, malicious samples, and the anchors. We
> evaluated the impact of the number of anchor samples on
> the effectiveness of the system by varying the anchor count
> from 200 to 2000 in increments of 200, using the Llama3-
> 8B model and three datasets. The results are presented in
> Figure 5.
> 
> As shown in the Figure 5, the detection effectiveness of
> the system generally exhibits a positive correlation with the
> number of anchor samples. As the number of anchors in-
> creases, the system is able to capture more representative
> features of both

## Block 4: Evaluation Locator
**Section Heading**: `Evaluation Metric` [section offsets: 25382:31211]
**First 120 words verbatim** [offsets: 25382:26138]
> Evaluation Metric
> The primary goal of our system is to
> detect whether conversational drift has occurred within an
> agent. This problem is essentially a binary classification
> task. Accordingly, we adopt the commonly used evaluation
> metric AUROC, which quantifies the area under the ROC
> curve formed by the True Positive Rate (TPR) and the False
> Positive Rate (FPR). A higher AUROC value, approaching
> 1, indicates better model performance.
> 
> Hyper-parameters
> For distance-based matching, the de-
> fault number of anchor samples is set to 1000. The top-k
> value for retrieval in the MCP server is configured to 5.
> For the three large language models evaluated, computations
> are performed at layers 0, 7, 15, 23, and 31, with the best-
> performing result among them

## Block 5: Attack-Set Excerpts
**Location**: `Evaluation Metric` [offsets: 26401:26488]
> We conduct our evaluation using the datasets and attack
> methods described in the setup.
**Location**: `Evaluation Metric` [offsets: 26824:26929]
> The performance of SECMCP on
> the Ms Marco dataset is comparatively lower than that on
> FinQA and HotpotQA.
**Location**: `Evaluation Metric` [offsets: 26930:27074]
> We attribute this to the broader top-
> ical diversity of the Ms Marco dataset, which poses greater
> challenges for the model in identifying risks.
**Location**: `Evaluation Metric` [offsets: 27076:27734]
> Risk
> LLMs
> Datasets
> AUROC
> 
> FinQA
> 0.987
> HotpotQA
> 0.989
> Ms Marco
> 0.992
> 
> Llama3-8B
> 
> FinQA
> 0.981
> HotpotQA
> 0.990
> Ms Marco
> 0.994
> 
> Data
> Exfiltration
> 
> Mistral-7B
> 
> FinQA
> 0.985
> HotpotQA
> 0.990
> Ms Marco
> 0.994
> 
> Vicuna-7B
> 
> FinQA
> 0.986
> HotpotQA
> 0.969
> Ms Marco
> 0.915
> 
> Llama3-8B
> 
> FinQA
> 0.992
> HotpotQA
> 0.977
> Ms Marco
> 0.964
> 
> Misleading
> 
> Mistral-7B
> 
> FinQA
> 0.997
> HotpotQA
> 0.949
> Ms Marco
> 0.933
> 
> Vicuna-7B
> 
> FinQA
> 0.995
> HotpotQA
> 0.995
> Ms Marco
> 0.973
> 
> Llama3-8B
> 
> FinQA
> 0.999
> HotpotQA
> 0.995
> Ms Marco
> 0.966
> 
> Hijacking
> 
> Mistral-7B
> 
> FinQA
> 0.992
> HotpotQA
> 0.991
> Ms Marco
> 0.974
> 
> Vicuna-7B
> 
> Table 1: The effectiveness of SECMCP across multiple sce-
> narios involving three categories of risks.
**Location**: `Evaluation Metric` [offsets: 27995:28168]
> A total of 3,000 ma-
> licious samples are selected from the three risk categories,
> along with 5,000 benign samples from the FinQA dataset to
> construct the evaluation dataset.
**Location**: `Evaluation Metric` [offsets: 29157:29202]
> We select HotpotQA as the evaluation dataset.

## Block 6: Baseline Excerpts
**Location**: `Evaluation Metric` [offsets: 26313:26399]
> MCP-powered agent system and compare its performance
> against several baseline methods.
**Location**: `Evaluation Metric` [offsets: 27736:27819]
> We also compare SECMCP with several baseline methods
> commonly used for LLM defense.
**Location**: `Evaluation Metric` [offsets: 28560:28637]
> Figure 3: Comparison of effectiveness with baseline meth-
> ods
> 
> success rates.
**Location**: `Evaluation Metric` [offsets: 28780:28882]
> In contrast, our method
> significantly outperforms these baseline approaches in terms
> of effectiveness.
**Location**: `Evaluation Metric` [offsets: 30033:30628]
> Ablation Study
> 
> In this section, we conduct ablation studies to examine the
> impact of three key design factors: the visualizations of the
> 
> --- PAGE BREAK ---
> 
> 60
> 
> Benign
> Malicious
> 
> 40
> 
> 40
> 
> 20
> 
> Component 2
> 
> Component 2
> 
> 20
> 
> 0
> 
> 0
> 
> 20
> 
> 20
> 
> 40
> 
> 40
> 
> 40
> 20
> 0
> 20
> 40
> 60
> Component 1
> 
> (a) Data Exfiltration
> 
> 1.01
> 
> 1.01
> 
> 0.98
> 
> 0.98
> 
> AUROC
> 
> AUROC
> 
> 0.95
> 
> 0.95
> 
> 0.92
> 
> 0.92
> 
> FinQA
> HotpotQA
> MS MARCO
> 
> 0.89
> 
> 0.89
> 
> 0.86
> 
> 0.86
> 
> 200
> 400
> 600
> 800
> 1000
> 1200
> 1400
> 1600
> 1800
> 2000
> Number of Anchor Samples
> 
> (a) Data Exfiltration
> 
> activation deviation, the number of anchor samples, and the
> selection of activation layers.
**Location**: `Evaluation Metric` [offsets: 30049:30628]
> In this section, we conduct ablation studies to examine the
> impact of three key design factors: the visualizations of the
> 
> --- PAGE BREAK ---
> 
> 60
> 
> Benign
> Malicious
> 
> 40
> 
> 40
> 
> 20
> 
> Component 2
> 
> Component 2
> 
> 20
> 
> 0
> 
> 0
> 
> 20
> 
> 20
> 
> 40
> 
> 40
> 
> 40
> 20
> 0
> 20
> 40
> 60
> Component 1
> 
> (a) Data Exfiltration
> 
> 1.01
> 
> 1.01
> 
> 0.98
> 
> 0.98
> 
> AUROC
> 
> AUROC
> 
> 0.95
> 
> 0.95
> 
> 0.92
> 
> 0.92
> 
> FinQA
> HotpotQA
> MS MARCO
> 
> 0.89
> 
> 0.89
> 
> 0.86
> 
> 0.86
> 
> 200
> 400
> 600
> 800
> 1000
> 1200
> 1400
> 1600
> 1800
> 2000
> Number of Anchor Samples
> 
> (a) Data Exfiltration
> 
> activation deviation, the number of anchor samples, and the
> selection of activation layers.

## Block 7: Cost Excerpts
**Location**: `Evaluation Metric` [offsets: 25561:25745]
> Accordingly, we adopt the commonly used evaluation
> metric AUROC, which quantifies the area under the ROC
> curve formed by the True Positive Rate (TPR) and the False
> Positive Rate (FPR).
**Location**: `Evaluation Metric` [offsets: 27102:27734]
> FinQA
> 0.987
> HotpotQA
> 0.989
> Ms Marco
> 0.992
> 
> Llama3-8B
> 
> FinQA
> 0.981
> HotpotQA
> 0.990
> Ms Marco
> 0.994
> 
> Data
> Exfiltration
> 
> Mistral-7B
> 
> FinQA
> 0.985
> HotpotQA
> 0.990
> Ms Marco
> 0.994
> 
> Vicuna-7B
> 
> FinQA
> 0.986
> HotpotQA
> 0.969
> Ms Marco
> 0.915
> 
> Llama3-8B
> 
> FinQA
> 0.992
> HotpotQA
> 0.977
> Ms Marco
> 0.964
> 
> Misleading
> 
> Mistral-7B
> 
> FinQA
> 0.997
> HotpotQA
> 0.949
> Ms Marco
> 0.933
> 
> Vicuna-7B
> 
> FinQA
> 0.995
> HotpotQA
> 0.995
> Ms Marco
> 0.973
> 
> Llama3-8B
> 
> FinQA
> 0.999
> HotpotQA
> 0.995
> Ms Marco
> 0.966
> 
> Hijacking
> 
> Mistral-7B
> 
> FinQA
> 0.992
> HotpotQA
> 0.991
> Ms Marco
> 0.974
> 
> Vicuna-7B
> 
> Table 1: The effectiveness of SECMCP across multiple sce-
> narios involving three categories of risks.
**Location**: `Evaluation Metric` [offsets: 27156:27734]
> FinQA
> 0.981
> HotpotQA
> 0.990
> Ms Marco
> 0.994
> 
> Data
> Exfiltration
> 
> Mistral-7B
> 
> FinQA
> 0.985
> HotpotQA
> 0.990
> Ms Marco
> 0.994
> 
> Vicuna-7B
> 
> FinQA
> 0.986
> HotpotQA
> 0.969
> Ms Marco
> 0.915
> 
> Llama3-8B
> 
> FinQA
> 0.992
> HotpotQA
> 0.977
> Ms Marco
> 0.964
> 
> Misleading
> 
> Mistral-7B
> 
> FinQA
> 0.997
> HotpotQA
> 0.949
> Ms Marco
> 0.933
> 
> Vicuna-7B
> 
> FinQA
> 0.995
> HotpotQA
> 0.995
> Ms Marco
> 0.973
> 
> Llama3-8B
> 
> FinQA
> 0.999
> HotpotQA
> 0.995
> Ms Marco
> 0.966
> 
> Hijacking
> 
> Mistral-7B
> 
> FinQA
> 0.992
> HotpotQA
> 0.991
> Ms Marco
> 0.974
> 
> Vicuna-7B
> 
> Table 1: The effectiveness of SECMCP across multiple sce-
> narios involving three categories of risks.
**Location**: `Evaluation Metric` [offsets: 27230:27734]
> FinQA
> 0.985
> HotpotQA
> 0.990
> Ms Marco
> 0.994
> 
> Vicuna-7B
> 
> FinQA
> 0.986
> HotpotQA
> 0.969
> Ms Marco
> 0.915
> 
> Llama3-8B
> 
> FinQA
> 0.992
> HotpotQA
> 0.977
> Ms Marco
> 0.964
> 
> Misleading
> 
> Mistral-7B
> 
> FinQA
> 0.997
> HotpotQA
> 0.949
> Ms Marco
> 0.933
> 
> Vicuna-7B
> 
> FinQA
> 0.995
> HotpotQA
> 0.995
> Ms Marco
> 0.973
> 
> Llama3-8B
> 
> FinQA
> 0.999
> HotpotQA
> 0.995
> Ms Marco
> 0.966
> 
> Hijacking
> 
> Mistral-7B
> 
> FinQA
> 0.992
> HotpotQA
> 0.991
> Ms Marco
> 0.974
> 
> Vicuna-7B
> 
> Table 1: The effectiveness of SECMCP across multiple sce-
> narios involving three categories of risks.
**Location**: `Evaluation Metric` [offsets: 27284:27734]
> FinQA
> 0.986
> HotpotQA
> 0.969
> Ms Marco
> 0.915
> 
> Llama3-8B
> 
> FinQA
> 0.992
> HotpotQA
> 0.977
> Ms Marco
> 0.964
> 
> Misleading
> 
> Mistral-7B
> 
> FinQA
> 0.997
> HotpotQA
> 0.949
> Ms Marco
> 0.933
> 
> Vicuna-7B
> 
> FinQA
> 0.995
> HotpotQA
> 0.995
> Ms Marco
> 0.973
> 
> Llama3-8B
> 
> FinQA
> 0.999
> HotpotQA
> 0.995
> Ms Marco
> 0.966
> 
> Hijacking
> 
> Mistral-7B
> 
> FinQA
> 0.992
> HotpotQA
> 0.991
> Ms Marco
> 0.974
> 
> Vicuna-7B
> 
> Table 1: The effectiveness of SECMCP across multiple sce-
> narios involving three categories of risks.
**Location**: `Evaluation Metric` [offsets: 27338:27734]
> FinQA
> 0.992
> HotpotQA
> 0.977
> Ms Marco
> 0.964
> 
> Misleading
> 
> Mistral-7B
> 
> FinQA
> 0.997
> HotpotQA
> 0.949
> Ms Marco
> 0.933
> 
> Vicuna-7B
> 
> FinQA
> 0.995
> HotpotQA
> 0.995
> Ms Marco
> 0.973
> 
> Llama3-8B
> 
> FinQA
> 0.999
> HotpotQA
> 0.995
> Ms Marco
> 0.966
> 
> Hijacking
> 
> Mistral-7B
> 
> FinQA
> 0.992
> HotpotQA
> 0.991
> Ms Marco
> 0.974
> 
> Vicuna-7B
> 
> Table 1: The effectiveness of SECMCP across multiple sce-
> narios involving three categories of risks.

## Block 8: Limitations
**Section Heading**: `Limitations and Future Work` [section offsets: 33307:34107]
**First 120 words verbatim** [offsets: 33307:34199]
> Limitations and Future Work
> Despite its promising performance, our method has sev-
> eral limitations. First, the method assumes a stable query-
> response structure and is not directly applicable to large-
> scale agentic environments with asynchronous, multi-agent
> protocols such as A2A, where conversation boundaries and
> speaker roles are fluid. Second, although the approach cap-
> tures topic-level deviations effectively, it lacks granularity
> for token-level attribution, limiting its applicability in con-
> texts requiring fine-grained control. Third, although our ac-
> tivation deviation-based method performs well in drift de-
> tection, its decision-making process lacks interpretability,
> which limits the applicability of the approach in scenarios
> that require high transparency.
> 
> --- PAGE BREAK ---
> 
> References
> 2022. GonzaloA/fake news.
> Abdelnabi, S.; Fay, A.; Cherubin, G.; Salem, A.; Fritz,

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `Introduction` [offsets: 2746:3319]
> To mitigate these limitations, Anthropic recently intro-
> duced the Model Context Protocol (MCP), a framework de-
> signed to extend LLM functionality through integration with
> external tools such as web search engines and knowledge
> databases. MCP enables LLMs to dynamically aggregate in-
> formation from multiple contextual streams, thereby sup-
> porting real-time decision making and adaptive service de-
> livery. For instance, a web search tool allows retrieval of up-
> to-date news and wikipedia, while knowledge database tools
> facilitate access to specialized domain corpora.
**Matched Term**: `adaptive` | **Location**: `Evaluation Metric` [offsets: 28884:29155]
> Robustness
> 
> To evaluate the robustness of SECMCP against adaptive at-
> tacks, we simulate scenarios where adversaries adjust their
> strategies in response to the defense method. In this section,
> we specifically consider adversaries employing a synonym
> replacement strategy.
**Matched Term**: `adaptive` | **Location**: `Conclusion` [offsets: 32739:33305]
> By leveraging activation vector deviations in-
> duced by malicious inputs, our method captures subtle se-
> mantic changes in model behavior that traditional output-
> based or rule-based detectors often miss. Extensive exper-
> iments across multiple datasets and risk types demonstrate
> that SECMCP achieves high detection accuracy while main-
> taining robustness against adaptive threats. Compared to
> prior approaches that rely on predefined attack signatures or
> heuristics, our method is inherently generalizable and does
> not require prior knowledge of the attack format.
