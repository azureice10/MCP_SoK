# Evidence Locator Packet: tobias-2026-machine-learning-based-detection-mcp

- **Title**: Machine Learning-Based Detection of MCP Attacks
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2604.10534
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\tobias-2026-machine-learning-based-detection-mcp\fulltext.txt
- **Character Count**: 54937

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 113:922]
> Abstract
> 
> The Model Context Protocol (MCP) is a new and emerg-
> ing technology that extends the functionality of large lan-
> guage models, improving workflows but also exposing
> users to a new attack surface. Several studies have high-
> lighted related security flaws, but MCP attack detection
> remains underexplored. To address this research gap, this
> study develops and evaluates a range of supervised ma-
> chine learning approaches, including both traditional and
> deep-learning models. We evaluated the systems on the
> detection of malicious MCP tool descriptions in two sce-
> narios: (1) a binary classification task distinguishing mali-
> cious from benign tools, and (2) a multiclass classification
> task identifying the attack type while separating benign
> from malicious tools. In addition to the machine learning

## Block 3: Method Locator
**Section Heading**: `Implementation, a method commonly used in computer` [section offsets: 12648:20961]
**First 120 words verbatim** [offsets: 12648:13497]
> Implementation, a method commonly used in computer
> science research when developing new software architec-
> 
> 3
> 
> tures, algorithms, or programs, also known as artifacts [9],
> is created to improve existing approaches. Such artifact
> typically requires comparison with existing techniques,
> which will be difficult in the current study because the
> technique is state-of-the-art and has no direct predeces-
> sors.
> 
> Experimentation, one of the fundamental scientific re-
> search methods, aims to verify or falsify a hypothesis by
> examining variables and how they are affected by differ-
> ent experimental conditions. Experimentation methods,
> which align to some degree with the experimental nature
> of this project, are especially useful when developing arti-
> ficial intelligence models and verifying results. However,
> this study focuses on creating a malicious

## Block 4: Evaluation Locator
**Section Heading**: `Results from this analysis revealed five classes with low` [section offsets: 20961:27933]
**First 120 words verbatim** [offsets: 20961:21798]
> Results from this analysis revealed five classes with low
> significance differences. The classes — Service Disrup-
> 
> 5
> 
> tion, Privacy Leakage, Data Tampering, Instruction Tam-
> pering — were merged into a single class labeled Informa-
> tion manipulation. This resulted in a new dataset contain-
> ing seven classes, on which models will be trained, tested,
> and evaluated. The corresponding cosine similarity matrix
> showed significantly lower similarity between classes.
> 
> Figure 5: Cosine Similarity matrix after class concatena-
> tion
> 
> 3.3.4
> Expanding dataset
> 
> The initial dataset was insufficient for training. To ad-
> dress this, back-translation was used to augment the
> dataset [20]. Because the project scope was limited to En-
> glish, languages linguistically distant from English were
> chosen [21]: Arabic, Chinese, Japanese, and Korean. For
**Section Heading**: `Evaluation Metrics` [section offsets: 27933:30696]
**First 120 words verbatim** [offsets: 27933:28700]
> Evaluation Metrics
> 
> The experimental results were measured using the metrics:
> accuracy, precision, recall, and F1-score.
> Accuracy measures the overall proportion of correct pre-
> dictions and is defined as
> 
> Accuracy =
> TP+TN
> TP+TN +FP+FN ,
> (1)
> 
> where TP, TN, FP, FN denote True Positive, True Nega-
> tive, False Positive, and False Negative [28]. This pro-
> vides a high-level summary of model performance but can
> be misleading when datasets are imbalanced due to the
> accuracy paradox [29], which states that in an imbalanced
> 
> 7
> 
> dataset a model can achieve high accuracy simply by pre-
> dicting the majority class for every sample.
> 
> Precision measures how many of the model’s positive
> predictions are actually positive. Precision is measured
> as:
> 
> Precision =
> TP
> TP+FP
> (2)
**Section Heading**: `Evaluation Results` [section offsets: 30696:32116]
**First 120 words verbatim** [offsets: 30696:31550]
> Evaluation Results
> 
> We evaluate the models on two different classification
> tasks, binary classification and multi-classification with 11
> classes, comparing the different models against each other
> and one state-of-the-art detection method.
> 
> 4.1
> Binary Classification
> 
> Based on the results, Table 1 summarizes the metrics ob-
> tained. The lowest-scoring model across all five metrics
> was the untuned (baseline) BERT model. Untuned BERT
> achieved an accuracy of 56.34%, compared with 69.01%
> for the YARA rule-based detection system.
> Although
> these models appear similar when considering accuracy
> alone, precision, recall, and F1-score tell a different story.
> YARA achieved precision 62.50%, recall 20.83%, and F1-
> score 31.25%, whereas the untuned BERT obtained preci-
> sion 11.11%, recall 4.17%, and F1-score 6.06%.
> 
> The confusion matrices (Figures 6b and 6a)
**Section Heading**: `results: accuracy, precision, recall, and F1-score each` [section offsets: 32116:36958]
**First 120 words verbatim** [offsets: 32116:32944]
> results: accuracy, precision, recall, and F1-score each
> reached 100%. Their confusion matrices (Figure 6) show
> 94 true negatives and 48 true positives, with no false posi-
> tives or false negatives.
> 
> Table 1: Binary models
> 
> Model
> Accuracy
> Precision
> Recall
> F1 Score
> YARA
> 69.01%
> 62.50%
> 20.83%
> 31.25%
> BERT *
> 56.34%
> 11.11%
> 4.17%
> 6.06%
> BERT
> 100.00%
> 100.00%
> 100.00%
> 100.00%
> SVC
> 100.00%
> 100.00%
> 100.00%
> 100.00%
> BiLSTM
> 100.00%
> 100.00%
> 100.00%
> 100.00%
> 
> * model is untuned only using pre-weights
> bert-base-uncased
> 
> 4.2
> Multiclass Classification
> 
> Multiclass classification, a more complex problem than bi-
> nary classification, was tested on four models: untuned
> BERT, fine-tuned BERT, SVC, and BiLSTM. Results pre-
> sented in Table 2.
> Beginning with an untuned model
> that performs significantly worse than fine-tuned models.
> 
> 8
> 
> Scoring only

## Block 5: Attack-Set Excerpts
**Location**: `Results from this analysis revealed five classes with low` [offsets: 21212:21326]
> This resulted in a new dataset contain-
> ing seven classes, on which models will be trained, tested,
> and evaluated.
**Location**: `Results from this analysis revealed five classes with low` [offsets: 21490:21565]
> 3.3.4
> Expanding dataset
> 
> The initial dataset was insufficient for training.
**Location**: `Results from this analysis revealed five classes with low` [offsets: 21515:21565]
> The initial dataset was insufficient for training.
**Location**: `Results from this analysis revealed five classes with low` [offsets: 21566:21639]
> To ad-
> dress this, back-translation was used to augment the
> dataset [20].
**Location**: `Results from this analysis revealed five classes with low` [offsets: 21962:22116]
> To prevent
> near-duplicates in the final dataset, a similarity filter was
> applied, and retained only back-translations with a simi-
> larity score below 0.8.
**Location**: `Results from this analysis revealed five classes with low` [offsets: 22458:22558]
> The YARA rules from this project were used
> as a benchmark representing the current state of the art.

## Block 6: Baseline Excerpts
**Location**: `Results from this analysis revealed five classes with low` [offsets: 23297:23421]
> This study aims to compare machine learning detection
> approaches with state-of-the-art methods, such as rule-
> based systems.
**Location**: `Evaluation Results` [offsets: 30716:30934]
> We evaluate the models on two different classification
> tasks, binary classification and multi-classification with 11
> classes, comparing the different models against each other
> and one state-of-the-art detection method.
**Location**: `Evaluation Results` [offsets: 31028:31115]
> The lowest-scoring model across all five metrics
> was the untuned (baseline) BERT model.
**Location**: `Evaluation Results` [offsets: 31116:31223]
> Untuned BERT
> achieved an accuracy of 56.34%, compared with 69.01%
> for the YARA rule-based detection system.
**Location**: `results (Section 4.1): Increasing the number of classes` [offsets: 43337:43490]
> BERT achieved an impressive accuracy
> of 97.89% and a precision of 98.10% compared to pre-
> vious accuracy of 88.73% and precision of 89.01% (see
> Table 2).

## Block 7: Cost Excerpts
**Location**: `Results from this analysis revealed five classes with low` [offsets: 23058:23261]
> Since YARA rules operate on
> binary classification, distinguishing only between benign
> and malicious tool descriptions, they will not be applied
> to or evaluated for the multi-class classification problem.
**Location**: `Results from this analysis revealed five classes with low` [offsets: 25909:26166]
> To evaluate the capabilities of models presented in Sec-
> tion 3.3.6, two experiments are formulated, the first be-
> ing binary classification, aligning with the primary goal
> of any malware defense system, to accurately distinguish
> benign from malicious data.
**Location**: `Results from this analysis revealed five classes with low` [offsets: 26994:27219]
> For binary classification only, we
> also evaluated a YARA rule-based system; since YARA is
> designed solely for detection, classifying samples as mali-
> cious or benign, and is therefore not suited for multiclass
> classification.
**Location**: `Evaluation Metrics` [offsets: 27953:28053]
> The experimental results were measured using the metrics:
> accuracy, precision, recall, and F1-score.
**Location**: `Evaluation Metrics` [offsets: 28176:28276]
> where TP, TN, FP, FN denote True Positive, True Nega-
> tive, False Positive, and False Negative [28].
**Location**: `Evaluation Metrics` [offsets: 28562:28648]
> Precision measures how many of the model’s positive
> predictions are actually positive.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
