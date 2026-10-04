# Evidence Locator Packet: sultan-2026-content-aware-attack-detection-llm

- **Title**: Content-Aware Attack Detection in LLM Agent Tool-Call Traffic: An Empirical Study of Features, Architectures, and Evaluation Protocols
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: scan_cepat
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2605.11053
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\sultan-2026-content-aware-attack-detection-llm\fulltext.txt
- **Character Count**: 46965

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 267:1103]
> Abstract
> 
> The Model Context Protocol (MCP) has become a widely adopted interface
> for LLM agents to invoke external tools, yet learned monitoring of MCP
> tool-call traffic remains underexplored. In this article, the proposed detector
> is presented as an attack detection framework for MCP tool-call traffic that
> encodes each agent session as a graph (tool calls as nodes, sequential and
> data-flow links as edges), enriches nodes with sentence-embedding features
> over arguments and responses, and classifies sessions as benign or attacked.
> Three GNN architectures (GAT, GCN, GraphSAGE), a no-graph MLP, and
> classical baselines (XGBoost, random forest, logistic regression, linear SVM)
> are evaluated, with the full architecture comparison conducted on RAS-Eval
> (task-stratified splits) and GraphSAGE retained as the GNN baseline on AT-
> Bench

## Block 3: Method Locator
**Section Heading**: `4. Detection Framework` [section offsets: 12184:12266]
**First 120 words verbatim** [offsets: 12184:12953]
> 4. Detection Framework
> 
> Figure 1 presents an overview of the detection pipeline.
> 
> 4.1. Session-to-Graph Encoding
> Each agent session is encoded as a graph G = (V, E) where nodes repre-
> sent individual tool calls and edges capture inter-call relationships. Figure 2
> illustrates a representative MCP session containing a data exfiltration attack,
> and Figure 3 shows the corresponding graph encoding.
> 
> Nodes. For a session with n tool calls, n nodes v1, . . . , vn are created, one
> per call. Each node stores the tool name, serialized arguments, tool response,
> response length, and a parameter hash (MD5 of serialized arguments, modulo
> 10,000).
> Edges. Two edge types are defined, both stored bidirectionally (effec-
> tively undirected) to allow symmetric message passing:
> 
> 6
**Section Heading**: `Method` [section offsets: 25276:26331]
**First 120 words verbatim** [offsets: 25276:26133]
> Method
> Features
> AUROC
> F1
> Recall
> FPR
> 
> Sup. SAGE
> Content
> 0.917±.018
> 0.731±.085
> 0.769±.038
> 0.107±.021
> SSL+FT (GAT)
> Content
> 0.939±.012
> —
> —
> —
> 
> Sup. SAGE
> Metadata
> 0.640±.106
> 0.527±.274
> 0.414±.239
> 0.226±.134
> SSL+FT (GAT)
> Metadata
> 0.510±.079
> 0.352±.138
> 0.236±.117
> 0.305±.186
> 
> Three findings emerge:
> Finding 1: Content features are essential. It can be seen from Ta-
> ble 5 that content embeddings perform considerably better than metadata-
> only features across both paradigms. More specifically, the AUROC of su-
> pervised GraphSAGE was lifted from 0.640 (metadata) to 0.917 (content),
> a 27.7-percentage-point gap. MCP attacks in RAS-Eval primarily alter the
> 
> 13
> 
> --- PAGE BREAK ---
> 
> semantic content of tool interactions (substituting arguments, returning fal-
> sified responses) rather than changing which tools are called or how they are
> structured. A metadata-only
**Section Heading**: `architecture-matched comparison (GAT encoder, 5-fold cross-validation), an` [section offsets: 26331:27632]
**First 120 words verbatim** [offsets: 26331:27167]
> architecture-matched comparison (GAT encoder, 5-fold cross-validation), an
> AUROC of 0.939 was reached by contrastive pre-training followed by fine-
> tuning, which is statistically indistinguishable from supervised training from
> scratch with the same encoder (0.944, Table 10). When compared with the
> strongest supervised configuration (GraphSAGE, 0.917 in Table 5), SSL+FT
> (GAT) lies in the same range, although the comparison is then confounded
> by architecture choice. This parity, however, does not extend to the low-
> label regime (§6.6). It should be noted that supervised training matched or
> performed better than SSL at every label fraction ≥5%. With metadata
> features, SSL collapsed to an AUROC of 0.510, confirming that content-level
> signal is what makes the contrastive objective useful.
> 
> Finding 3:
> Metadata features enable task
**Section Heading**: `6.2. Architecture Comparison` [section offsets: 27632:27996]
**First 120 words verbatim** [offsets: 27632:28478]
> 6.2. Architecture Comparison
> Table 6 compares the three GNN architectures and the no-graph MLP
> baseline on RAS-Eval with content features under task-stratified evaluation.
> 
> Table 6: Architecture comparison on RAS-Eval (content features, task-stratified, 3 seeds).
> MLP applies the same readout (mean + max pooling) to raw node features without graph
> convolutions.
> 
> Architecture
> AUROC
> F1
> Recall
> FPR
> 
> GraphSAGE
> 0.917±.018
> 0.731±.085
> 0.769±.038
> 0.107±.021
> GCN
> 0.902±.007
> 0.740±.054
> 0.789±.028
> 0.131±.019
> MLP (no graph)
> 0.896±.010
> 0.727±.066
> 0.773±.033
> 0.143±.056
> GAT
> 0.891±.023
> 0.767±.028
> 0.832±.052
> 0.178±.046
> 
> 14
> 
> --- PAGE BREAK ---
> 
> As can be seen from Table 6, an AUROC above 0.89 was attained by all
> architectures, with differences of at most 2.6 percentage points across models.
> It is realized that the benefit of graph message passing over the

## Block 4: Evaluation Locator
**Section Heading**: `2. Task-stratified evaluation protocol. Standard random-split eval-` [section offsets: 5802:6185]
**First 120 words verbatim** [offsets: 5802:6678]
> 2. Task-stratified evaluation protocol. Standard random-split eval-
> uation is shown to conflate task memorization with attack detection,
> with the area under the ROC curve (AUROC) inflated by up to 25.8
> percentage points under random splits relative to task-disjoint splits.
> Task-disjoint 70/10/20 splits are adopted as the appropriate protocol
> for agent attack-detection benchmarks.
> 3. Empirical findings with deployment implications. Across three
> GNN architectures, an MLP baseline, four classical classifiers, and three
> dataset configurations, the experimental results show that content em-
> beddings are necessary, that tree ensembles on pooled SBERT features
> perform, to a great extent, better than the neural architectures in the
> primary RAS-Eval setting, and that contrastive pre-training does not
> provide a reliable label-efficiency advantage.
> 
> --- PAGE BREAK ---
> 
> Table
**Section Heading**: `4.3.3. MLP Baseline (No Graph Structure)` [section offsets: 18160:18527]
**First 120 words verbatim** [offsets: 18160:18875]
> 4.3.3. MLP Baseline (No Graph Structure)
> In order to isolate the contribution of graph message passing, an MLP
> baseline is included that applies the same dual readout (mean + max pooling)
> directly to raw node features, bypassing all GNN layers, followed by the same
> MLP classifier.
> 
> 9
> 
> 
> 
> i , {h(l)
> 
> (1)
> 
> j
> : j ∈N(i)}
> 
> i
> }) ∥MAX({h(L)
> 
> i
> })
> (2)
> 
> --- PAGE BREAK ---
> 
> 5. Evaluation Protocol
> 
> 5.1. Datasets
> In the experiments carried out in this study, two real-world agent trajec-
> tory datasets and a combined-source variant were used, as summarized in
> Table 2.
> 
> Table 2: Dataset statistics. All sessions contain at least one tool call. The “Tasks” column
> reports the number of distinct task definitions for RAS-Eval
**Section Heading**: `5. Evaluation Protocol` [section offsets: 18527:18551]
**First 120 words verbatim** [offsets: 18527:19291]
> 5. Evaluation Protocol
> 
> 5.1. Datasets
> In the experiments carried out in this study, two real-world agent trajec-
> tory datasets and a combined-source variant were used, as summarized in
> Table 2.
> 
> Table 2: Dataset statistics. All sessions contain at least one tool call. The “Tasks” column
> reports the number of distinct task definitions for RAS-Eval (used for task-stratified splits)
> and the number of curated trajectories for ATBench (which has no shared task structure).
> 
> Dataset
> Benign
> Attacked
> Tools
> Tasks
> 
> RAS-Eval [18]
> 605
> 3,797
> 34
> 80
> ATBench [19]
> 502
> 497
> 2,084
> 999
> Combined
> 1,939
> 4,294
> 2,118
> —
> 
> RAS-Eval [18] is the primary dataset used in this study. It provides
> 80 tasks across 5 domains (calendar, alarm, file management, database, web
> search) executed by
**Section Heading**: `5.2. Task-Stratified Evaluation` [section offsets: 21317:22365]
**First 120 words verbatim** [offsets: 21317:22205]
> 5.2. Task-Stratified Evaluation
> Standard random-split evaluation allows training and test sets to share
> the same task definitions. Because different tasks use different tool subsets,
> a classifier can learn task-specific tool signatures rather than generalizable
> attack patterns, which constitutes a form of task memorization.
> 
> This confound was discovered empirically: with metadata-only features
> on RAS-Eval, a random split inflated AUROC by 25.8 percentage points over
> a task-disjoint split (Table 3).
> 
> Table 3: Task-disjoint vs. label-stratified random split on RAS-Eval (supervised GAT,
> 70/10/20, 3 seeds). The gap between the two protocols quantifies task-memorization in-
> flation. Both protocols use the same model and training pipeline; only the split assignment
> differs. Content-feature numbers are from the architecture comparison (Table 6) and the
> matching label-stratified run.

## Block 5: Attack-Set Excerpts
**Location**: `2. Task-stratified evaluation protocol. Standard random-split eval-` [offsets: 6076:6184]
> Task-disjoint 70/10/20 splits are adopted as the appropriate protocol
> for agent attack-detection benchmarks.
**Location**: `6.3. Classical Baselines` [offsets: 29614:29665]
> Table 7 presents results across all three datasets.
**Location**: `6.3. Classical Baselines` [offsets: 29875:30071]
> Dataset
> Classifier
> AUROC
> F1
> Recall
> FPR
> 
> RAS-Eval
> 
> ATBench
> 
> Combined
> 
> 15
> 
> XGBoost
> 0.975±.005
> 0.958±.005
> 0.927±.008
> 0.071±.031
> Random Forest
> 0.974±.006
> 0.972±.005
> 0.966±.015
> 0.191±.052
> Logistic Reg.
**Location**: `6.4. Per-Dataset Results` [offsets: 31161:31237]
> Per-Dataset Results
> Table 8 presents results for each dataset configuration.
**Location**: `6.4. Per-Dataset Results` [offsets: 31239:31307]
> Table 8: Per-dataset results (content features, GraphSAGE, 3 seeds).
**Location**: `6.4. Per-Dataset Results` [offsets: 31398:31698]
> Dataset
> AUROC
> AUPRC
> Recall
> FPR
> 
> RAS-Eval
> 0.917±.018
> 0.974±.022
> 0.769±.038
> 0.107±.021
> ATBench
> 0.762±.029
> 0.758±.012
> 0.643±.062
> 0.264±.026
> Combined
> 0.971±.004
> 0.987±.001
> 0.917±.016
> 0.098±.014
> 
> As can be seen from Table 8, the three dataset configurations exhibit
> markedly different difficulty profiles.

## Block 6: Baseline Excerpts
**Location**: `4.3.3. MLP Baseline (No Graph Structure)` [offsets: 18167:18441]
> MLP Baseline (No Graph Structure)
> In order to isolate the contribution of graph message passing, an MLP
> baseline is included that applies the same dual readout (mean + max pooling)
> directly to raw node features, bypassing all GNN layers, followed by the same
> MLP classifier.
**Location**: `6.3. Classical Baselines` [offsets: 28678:28971]
> Classical Baselines
> In order to further isolate the contribution of model architecture from fea-
> ture quality, classical machine learning classifiers were evaluated on the same
> pooled SBERT features used by the MLP baseline (1536-dimensional mean
> + max pooling of per-node content embeddings).
**Location**: `6.3. Classical Baselines` [offsets: 29667:29733]
> Table 7: Classical baselines on pooled content features (3 seeds).

## Block 7: Cost Excerpts
**Location**: `evaluation. It is observed that the choice of feature mode has a considerably` [offsets: 24903:25158]
> The dashes in the SSL+FT (Content) row reflect that F1, recall,
> and FPR were not collected at the label-efficiency full-label point under matched thresh-
> old settings; the architecture-matched supervised counterpart at full labels is reported in
> Table 10.
**Location**: `6.3. Classical Baselines` [offsets: 28972:29348]
> All classifiers use fixed
> hyperparameters with class weighting: logistic regression (L-BFGS, C =1.0,
> balanced weights), linear support vector machine (SVM) via stochastic gra-
> dient descent (SGD) (hinge loss, α=10−4, balanced weights), random forest
> (200 trees, balanced weights), and XGBoost (200 rounds, histogram splitting,
> scale_pos_weight set to the benign/attack ratio).
**Location**: `6.3. Classical Baselines` [offsets: 29875:30071]
> Dataset
> Classifier
> AUROC
> F1
> Recall
> FPR
> 
> RAS-Eval
> 
> ATBench
> 
> Combined
> 
> 15
> 
> XGBoost
> 0.975±.005
> 0.958±.005
> 0.927±.008
> 0.071±.031
> Random Forest
> 0.974±.006
> 0.972±.005
> 0.966±.015
> 0.191±.052
> Logistic Reg.
**Location**: `6.4. Per-Dataset Results` [offsets: 31398:31698]
> Dataset
> AUROC
> AUPRC
> Recall
> FPR
> 
> RAS-Eval
> 0.917±.018
> 0.974±.022
> 0.769±.038
> 0.107±.021
> ATBench
> 0.762±.029
> 0.758±.012
> 0.643±.062
> 0.264±.026
> Combined
> 0.971±.004
> 0.987±.001
> 0.917±.016
> 0.098±.014
> 
> As can be seen from Table 8, the three dataset configurations exhibit
> markedly different difficulty profiles.
**Location**: `6.4. Per-Dataset Results` [offsets: 32010:32258]
> The Combined configuration
> yields the highest overall performance under label-stratified splits, but be-
> cause mcpbench contributes only benign examples from a different agent
> framework, source-specific cues may be partially exploited by the model.
**Location**: `6.4. Per-Dataset Results` [offsets: 32259:32421]
> This result is therefore interpreted as mixed-source in-distribution perfor-
> mance rather than evidence that pooling benign sources improves detection
> in general.

## Block 8: Limitations
**Section Heading**: `7.3. Limitations` [section offsets: 37803:39425]
**First 120 words verbatim** [offsets: 37803:38635]
> 7.3. Limitations
> Dataset scope. Both datasets are research benchmarks, and real-world
> MCP attacks observed in production may exhibit characteristics absent from
> either source. This limitation is mitigated by reporting on the combined-
> source variant in addition to each dataset alone.
> 
> Content dependency. The reliance on content-level features (sentence
> embeddings of tool arguments and responses) means the proposed detector
> requires access to tool-call content, not just metadata. In privacy-sensitive
> 
> 19
> 
> ATBench
> 
> Combined
> 
> 1%
> 5%
> 10%
> 25%
> 50%
> 100%
> Label fraction
> 
> 1%
> 5%
> 10%
> 25%
> 50%
> 100%
> Label fraction
> 
> SSL linear probe
> SSL + fine-tune
> Supervised
> 
> --- PAGE BREAK ---
> 
> deployments where content inspection is restricted, the metadata-only mode
> (AUROC of 0.64) may be the only viable option.
> 
> Single-model attacks. RAS-Eval benign

## Block 9: Adaptivity Hits
no hits
