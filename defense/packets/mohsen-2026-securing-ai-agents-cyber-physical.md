# Evidence Locator Packet: mohsen-2026-securing-ai-agents-cyber-physical

- **Title**: Securing AI Agents in Cyber-Physical Systems: A Survey of Environmental Interactions, Deepfake Threats, and Defenses
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_cek_recall
- **Role Status**: Human Coded: survey_review
- **Link**: https://arxiv.org/abs/2601.20184
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\mohsen-2026-securing-ai-agents-cyber-physical\fulltext.txt
- **Character Count**: 278233

## Block 2: Contribution Sentences
**Location**: `Abstract—The increasing integration of AI agents into cyber-` [offsets: 334:1249]
> Abstract—The increasing integration of AI agents into cyber-
> physical systems (CPS) introduces new security risks that extend
> beyond traditional cyber or physical threat models. Recent
> advances in generative AI enable deepfake and semantic manip-
> ulation attacks that can compromise agent perception, reasoning,
> and interaction with the physical environment, while emerging
> protocols such as the Model Context Protocol (MCP) further
> expand the attack surface through dynamic tool use and cross-
> domain context sharing. This survey provides a comprehensive
> review of security threats targeting AI agents in CPS, with a
> particular focus on environmental interactions, deepfake-driven
> attacks, and MCP-mediated vulnerabilities. We organize the
> literature using the SENTINEL framework, a lifecycle-aware
> methodology that integrates threat characterization, feasibility
> analysis under CPS constraints, defense selection,

## Block 3: Method Locator
**Section Heading**: `methodology that integrates threat characterization, feasibility` [section offsets: 1134:1962]
**First 120 words verbatim** [offsets: 1134:2125]
> methodology that integrates threat characterization, feasibility
> analysis under CPS constraints, defense selection, and continuous
> validation. Through an end-to-end case study grounded in a
> real-world smart grid deployment, we quantitatively illustrate
> how timing, noise, and false-positive costs constrain deployable
> defenses, and why detection mechanisms alone are insufficient as
> decision authorities in safety-critical CPS. The survey highlights
> the role of provenance- and physics-grounded trust mechanisms
> and defense-in-depth architectures, and outlines open challenges
> toward trustworthy AI-enabled CPS.
> 
> arXiv:2601.20184v1  [cs.CR]  28 Jan 2026
> 
> Index Terms—Cyber-Physical Systems (CPS), AI Agents,
> Model Context Protocol (MCP), Deepfake Attacks, AI-Generated
> Content (AIGC), Security, Detection, Defense, Mitigation.
> 
> I. INTRODUCTION
> 
> As autonomous AI agents increasingly integrate into cyber-
> physical systems (CPS), the boundary between intelligence
> and the physical world blurs.
**Section Heading**: `methodology for matching defense strategies to specific de-` [section offsets: 18295:19615]
**First 120 words verbatim** [offsets: 18295:19227]
> methodology for matching defense strategies to specific de-
> ployment contexts. The SENTINEL framework operational-
> izes the selection of security mechanisms by integrating threat
> modeling, resource constraints, and operational requirements
> into a unified decision process.
> 
> Figure 6 outlines the workflow of the SENTINEL frame-
> work. It recognizes that MCP-enabled AI agents in CPS
> operate under fundamentally different constraints than tradi-
> tional IT systems or standalone AI applications. These systems
> must balance security with safety-critical timing requirements,
> operate with limited computational resources at edge devices,
> maintain availability for physical process control, and preserve
> privacy while enabling necessary monitoring. Additionally, the
> distributed nature of MCP architectures, where agents interact
> with external tool servers and shared context repositories,
> creates unique trust boundaries that traditional
**Section Heading**: `D. Phase 4: Defense-in-Depth Architecture Design` [section offsets: 27733:27896]
**First 120 words verbatim** [offsets: 27733:28707]
> D. Phase 4: Defense-in-Depth Architecture Design
> 
> Recognizing that no single security mechanism provides
> complete protection, Phase 4 constructs a layered defense
> architecture that integrates complementary techniques to ad-
> dress the threat landscape comprehensively. Figure 7 illus-
> trates the four-tier defense-in-depth architecture that Phase 4
> 
> constructs for MCP-enabled cyber-physical systems, showing
> how complementary security mechanisms combine to provide
> comprehensive protection against deepfake threats.
> 
> The perimeter tier implements proactive defenses before
> threats reach agent decision-making processes, including input
> validation and sanitization at MCP server boundaries, cryp-
> tographic authentication of content provenance using C2PA
> or similar standards, and reputation-based filtering of external
> data sources and tool providers. These mechanisms reduce the
> attack surface by rejecting obviously malicious inputs before
> they consume detection resources
**Section Heading**: `architecture that integrates complementary techniques to ad-` [section offsets: 27896:31126]
**First 120 words verbatim** [offsets: 27896:28861]
> architecture that integrates complementary techniques to ad-
> dress the threat landscape comprehensively. Figure 7 illus-
> trates the four-tier defense-in-depth architecture that Phase 4
> 
> constructs for MCP-enabled cyber-physical systems, showing
> how complementary security mechanisms combine to provide
> comprehensive protection against deepfake threats.
> 
> The perimeter tier implements proactive defenses before
> threats reach agent decision-making processes, including input
> validation and sanitization at MCP server boundaries, cryp-
> tographic authentication of content provenance using C2PA
> or similar standards, and reputation-based filtering of external
> data sources and tool providers. These mechanisms reduce the
> attack surface by rejecting obviously malicious inputs before
> they consume detection resources or influence agent behavior.
> 
> The detection tier deploys deepfake detection mechanisms
> matched to the threat profile and positioned according to
> resource

## Block 4: Evaluation Locator
**Section Heading**: `III. SENTINEL FRAMEWORK: SYSTEMATIC EVALUATION` [section offsets: 17863:18295]
**First 120 words verbatim** [offsets: 17863:18748]
> III. SENTINEL FRAMEWORK: SYSTEMATIC EVALUATION
> 
> AND THREAT-INFORMED DEFENSE SELECTION
> 
> Before examining specific threats to AI agents in CPS, we
> introduce the a Systematic Evaluation and Threat-Informed
> NEtwork defense seLection (SENTINEL) framework. This
> framework addresses a critical gap in the literature: while
> numerous surveys catalog security mechanisms for AI sys-
> tems or enumerate threats to CPS, few provide a systematic
> methodology for matching defense strategies to specific de-
> ployment contexts. The SENTINEL framework operational-
> izes the selection of security mechanisms by integrating threat
> modeling, resource constraints, and operational requirements
> into a unified decision process.
> 
> Figure 6 outlines the workflow of the SENTINEL frame-
> work. It recognizes that MCP-enabled AI agents in CPS
> operate under fundamentally different constraints than tradi-
> tional IT
**Section Heading**: `evaluation should include both isolated mechanism testing,` [section offsets: 31620:33386]
**First 120 words verbatim** [offsets: 31620:32637]
> evaluation should include both isolated mechanism testing,
> verifying that individual detection techniques achieve specified
> accuracy and latency targets, and integrated system testing
> that validates the complete defense-in-depth architecture under
> realistic conditions, including normal operational workload,
> concurrent multi-vector attacks, and resource-degradation sce-
> narios.
> 
> The framework specifies three validation methodologies ap-
> propriate for different CPS contexts. Laboratory testbeds pro-
> vide controlled environments for detailed performance charac-
> terization without risking operational systems, enabling com-
> prehensive testing against both documented attacks and novel
> adversarial examples generated through red team exercises.
> Digital twin simulation leverages physics-based models of
> CPS processes to evaluate security mechanisms under realistic
> operational conditions while maintaining safety, particularly
> valuable for testing response tier policies that could trigger
> unsafe states if deployed
**Section Heading**: `D. Real-world incidents and case studies` [section offsets: 54948:57270]
**First 120 words verbatim** [offsets: 54948:55793]
> D. Real-world incidents and case studies
> 
> 1) User-Agent Surface incidents: This category examines
> the Trust Dimension between human operators and AI agents.
> 
> A primary example is the deepfake heist where attackers used
> multi-persona video deepfakes to deceive staff into authorizing
> a $25 million transfer, as detailed in [116], [133]. SENTINEL
> classifies this as a high-impact behavioral emulation attack that
> exploits the U-A surface by bypassing traditional human-in-
> the-loop verification.
> 
> The accessibility of generative AI has empowered oppor-
> tunistic attackers, such as adolescents using AI for non-
> consensual image generation, to breach the Privacy Dimension
> of public spaces [116]. Such incidents force a reassessment of
> standard security hygiene, as the barrier to entry for high-
> fidelity deception has dropped significantly [297].
**Section Heading**: `VIII. CASE STUDY: AUTHENTICATING SMART GRID` [section offsets: 169498:180852]
**First 120 words verbatim** [offsets: 169498:170316]
> VIII. CASE STUDY: AUTHENTICATING SMART GRID
> 
> DIGITAL TWINS
> 
> To demonstrate how the principles surveyed in this work
> apply in a concrete CPS context, we present a case study based
> on ANCHOR-Grid, a smart grid DT authentication framework
> that leverages real-world environmental data to secure cyber-
> physical representations [132]. This case study shows how
> the SENTINEL framework can be operationalized to address
> deepfake threats against DTs and underscores the role of
> physical anchors in CPS security.
> 
> In smart grid systems, DTs are virtual replicas of phys-
> ical grid components used for simulation, monitoring, and
> decision support. Their fidelity to the real grid is critical:
> attackers who manipulate DT inputs or states can disrupt
> operational decision-making, thereby creating reliability and
> 
> safety hazards.

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
**Location**: `evaluation should include both isolated mechanism testing,` [offsets: 31620:31999]
> evaluation should include both isolated mechanism testing,
> verifying that individual detection techniques achieve specified
> accuracy and latency targets, and integrated system testing
> that validates the complete defense-in-depth architecture under
> realistic conditions, including normal operational workload,
> concurrent multi-vector attacks, and resource-degradation sce-
> narios.
**Location**: `VIII. CASE STUDY: AUTHENTICATING SMART GRID` [offsets: 173355:173615]
> Security mechanisms introduced at the DT interface
> must therefore satisfy bounded latency and low false-positive
> requirements, as delayed or spurious alarms can trigger unnec-
> essary mitigation actions, operator intervention, or degraded
> situational awareness.
**Location**: `VIII. CASE STUDY: AUTHENTICATING SMART GRID` [offsets: 173945:174080]
> cation remains effective under realistic network latency and
> noise conditions, rather than assuming idealized communi-
> cation channels.
**Location**: `VIII. CASE STUDY: AUTHENTICATING SMART GRID` [offsets: 174081:174301]
> Reported results show that authentication
> performance is maintained under network delays on the order
> of O(102ms), a range compatible with DT validation and
> monitoring workflows but not with ultra-fast protection relays.
**Location**: `VIII. CASE STUDY: AUTHENTICATING SMART GRID` [offsets: 174606:174800]
> These values demonstrate that ENF-based authenti-
> cation remains effective under realistic latency, noise, and
> replay conditions, while maintaining acceptable detection and
> false positive rates.
**Location**: `VIII. CASE STUDY: AUTHENTICATING SMART GRID` [offsets: 177042:177208]
> Importantly,
> the anchoring mechanism operates passively and incurs mini-
> mal computational overhead, preserving real-time performance
> while enhancing trustworthiness.

## Block 8: Limitations
**Section Heading**: `limitations, and unified research priorities for securing MCP-` [section offsets: 106598:107367]
**First 120 words verbatim** [offsets: 106598:107554]
> limitations, and unified research priorities for securing MCP-
> enabled CPS.
> 
> 1) Common Strengths Across Modalities:
> Research on
> deepfake threats has achieved notable progress applicable to
> CPS security. Comprehensive attack taxonomies have been
> developed for each modality—visual (display spoofing, face-
> swap, scene synthesis), audio (voice cloning, replay attacks),
> textual (tool poisoning, prompt injection, rug pulls), and
> behavioral (sensor spoofing, anomaly mimicry, stealthy mal-
> ware). Multi-modal defense strategies combining physiolog-
> ical signals (rPPG), provenance frameworks (C2PA), and
> cross-sensor fusion demonstrate improved robustness over
> 
> TABLE XVIII
> EMBODIED AI ATTACK MECHANISMS
> 
> Mechanism
> Target System
> Success
> Rate
> 
> Physical
> Risk
> Word Injection
> LLM Decision
> High
> High
> Scenario Manip-
> ulation
> 
> Context
> High
> Critical
> 
> Knowledge
> Injection
> 
> Memory
> Medium
> High
> 
> Sensor Spoofing
> Perception
> High
> Critical
> Adversarial
> Patches
> 
> Vision
> Medium

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `I. INTRODUCTION` [offsets: 7640:8247]
> 5) An end-to-end CPS case study leveraging ANCHOR-
> Grid [132] demonstrates how the proposed SENTINEL
> framework can be operationalized under concrete timing,
> noise, and safety constraints.
> 6) A discussion of open challenges and directions, empha-
> sizing the tension between real-time performance, gener-
> alization, privacy, and adaptive adversaries [82], [145].
> By consolidating insights from recent literature on AI
> security, generative models, and CPS resilience, we hope this
> survey will serve as a foundational reference for researchers
> and system designers seeking to build trustworthy AI agents
> in CPS.
**Matched Term**: `evade` | **Location**: `D. Deepfake (AI-Generated Content) Technologies` [offsets: 15860:16209]
> X, JANUARY 2026
> 4
> 
> Text and behavioral emulation: LLMs can produce im-
> personated instructions/logs and synthesize plausible telemetry
> or user behaviors to evade anomaly detectors. Multi-agent
> attack studies reveal how untrusted content and peer messages
> can induce unsafe tool calls and system-level compromise
> when trust boundaries are weak [213].
**Matched Term**: `evasion` | **Location**: `C. Phase 3: Constraint-Aware Defense Mechanism Selection` [offsets: 25471:26125]
> The detection effectiveness dimension captures mechanism
> accuracy through true positive and false positive rates for
> relevant attack types, robustness to adversarial adaptation and
> evasion attempts, generalization capability to novel deepfake
> generators not seen during training, and coverage breadth
> across different attack modalities. Computational requirements
> specify processing resources that include CPU, GPU, and
> memory footprints, latency from input acquisition to threat
> verdict delivery, scalability characteristics as system size or
> attack volume increases, and whether processing can occur at
> edge devices or requires centralized computation.
**Matched Term**: `red team` | **Location**: `evaluation should include both isolated mechanism testing,` [offsets: 32001:32672]
> The framework specifies three validation methodologies ap-
> propriate for different CPS contexts. Laboratory testbeds pro-
> vide controlled environments for detailed performance charac-
> terization without risking operational systems, enabling com-
> prehensive testing against both documented attacks and novel
> adversarial examples generated through red team exercises.
> Digital twin simulation leverages physics-based models of
> CPS processes to evaluate security mechanisms under realistic
> operational conditions while maintaining safety, particularly
> valuable for testing response tier policies that could trigger
> unsafe states if deployed prematurely in production systems.
**Matched Term**: `Adaptive` | **Location**: `F. Phase 6: Continuous Monitoring and Adaptive Defense` [offsets: 33386:33941]
> F. Phase 6: Continuous Monitoring and Adaptive Defense
> 
> The final phase recognizes that security is not a one-time
> deployment but an ongoing process that requires continuous
> monitoring and adaptation. The framework specifies metrics
> for operational security monitoring, including attack detection
> and false-positive rates relative to baseline expectations, se-
> curity mechanism resource consumption relative to budgets,
> degradation in system performance caused by security over-
> head, and coverage gaps where new attack techniques evade
> deployed defenses.
**Matched Term**: `evade` | **Location**: `F. Phase 6: Continuous Monitoring and Adaptive Defense` [offsets: 33442:34356]
> The final phase recognizes that security is not a one-time
> deployment but an ongoing process that requires continuous
> monitoring and adaptation. The framework specifies metrics
> for operational security monitoring, including attack detection
> and false-positive rates relative to baseline expectations, se-
> curity mechanism resource consumption relative to budgets,
> degradation in system performance caused by security over-
> head, and coverage gaps where new attack techniques evade
> deployed defenses.
> 
> Trigger conditions for defense mechanism updates include
> detection accuracy falling below acceptable thresholds, indi-
> cating adversarial adaptation, the emergence of new threat
> intelligence about attack techniques or vulnerable components,
> changes to system configuration or operational requirements
> that alter threat landscape or constraint profiles, and security
> incidents that reveal gaps in defense coverage.
**Matched Term**: `Adaptive` | **Location**: `A. User–Agent (U–A) Interface Analysis` [offsets: 43213:43850]
> • Verified Code Generation: Ensuring that the tool calls
> and scripts generated by agents adhere to strict safety
> specifications remains difficult, as seen in recent efforts
> toward verified code generation frameworks like Veri-
> Guard [221]
> 
> • Adaptive Robustness:
> As adversaries adapt to current
> filters, there is a need for defense mechanisms that can
> survive an ”adaptive arms race” by dynamically updating
> their detection logic [79].
> 
> • Multi-Agent Adversarial Dynamics: In environments
> where multiple agents interact, compromised proxies can
> lead to cascading failures that are poorly understood in
> existing security literature [375].
**Matched Term**: `evade` | **Location**: `V. DEEPFAKES AS A CPS SECURITY THREAT` [offsets: 58964:59482]
> Recent scientific findings underscore the need for
> robust defenses, such as provenance tracking, to counter these
> threats in real-time CPS operations [191], [213]. Behavioral
> deepfakes, in particular, pose stealthy risks by emulating
> anomalies to evade detection in multi-agent systems, poten-
> tially leading to physical infrastructure compromises. Overall,
> the convergence of deepfake technologies with MCP-enabled
> ecosystems demands interdisciplinary approaches to mitigate
> evolving adversarial manipulations in CPS.
**Matched Term**: `evade` | **Location**: `A. Visual Deepfakes` [offsets: 60721:61364]
> From an attack-method perspective, presentation and deep-
> fake attacks encompass display-mediated spoofing (utilizing
> high-resolution screens and virtual cameras on RTSP feeds),
> face reenactment/face-swap to evade watchlist matching, and
> scene-level synthesis to fabricate individuals or activities. Sys-
> tematizations of face anti-spoofing and deepfake detection em-
> phasize that detectors that excel on curated datasets generalize
> poorly to in-the-wild content and to new generators, necessi-
> tating spatiotemporal cues, physiological signals (e.g., rPPG),
> and cross-modal checks to lift robustness in operational CCTV
> settings [163], [228].
**Matched Term**: `evade` | **Location**: `B. Audio Deepfakes` [offsets: 66608:67304]
> In a related incident, voice
> cloning was used to impersonate operators in vehicle control
> centers, issuing false commands that altered traffic manage-
> ment protocols and caused real-time safety hazards [285]. Such
> multi-modal deceptions not only undermine system integrity
> but also expose gaps in current detection methods, as attack-
> ers leverage generative models to evade traditional anomaly
> checks in dynamic CPS environments. Additionally, case
> studies emphasize the role of adversarial training failures in
> exacerbating breaches, including instances in which manipu-
> lated sensor inputs in healthcare CPS led to erroneous medical
> device operations, compromising patient safety [166], [261].
**Matched Term**: `evade` | **Location**: `Method` [offsets: 70609:71228]
> Yes
> 
> wav2vec-CM
> Self-supervised
> High compute
> Medium
> Spectrogram CNN
> Fast, proven
> Codec sensitive
> Yes
> Prosodic Analysis
> Interpretable
> Easy to evade
> Yes
> LCNN
> Lightweight
> Limited capac-
> ity
> 
> Yes
> 
> RawNet2
> End-to-end
> Large model
> Medium
> 
> TABLE IX
> VOICE CLONING SYSTEMS COMPARISON
> 
> System
> Enrollment
> Quality
> VALL-E
> 3 sec
> Human-parity
> XTTS
> 6 sec
> Near-parity
> Tortoise
> 30 sec
> High
> RVC
> Variable
> High
> 
> C. Textual Deepfakes
> 
> Textual deepfakes in the context of the MCP refer to
> AI-generated or manipulated text that deceives LLMs by
> embedding malicious instructions within tool descriptions,
> metadata, or external data sources [92].
**Matched Term**: `evade` | **Location**: `C. Textual Deepfakes` [offsets: 75350:75940]
> When MCP connectors synchronize external knowledge
> bases or message buses into an agent’s context window,
> fabricated narratives can bias diagnosis, triage, or planning
> modules, leading to mis-prioritized repairs, unnecessary shut-
> downs, or inappropriate configuration changes [162]. The
> misinformation literature shows that deep neural generators
> exploit stylistic and rhetorical patterns that evade simple
> lexicon checks. That multimodal and context-aware models
> are needed to reconcile claims with telemetry or verified
> knowledge graphs before agents treat text as actionable state
> [27].
**Matched Term**: `evasion` | **Location**: `C. Textual Deepfakes` [offsets: 77255:78088]
> these crafted instructions can exploit model-level instruction-
> following to induce unsafe tool sequences, escalate from low-
> risk to high-risk capabilities, or propagate across agents via
> shared memory and broadcast channels [193]. Security surveys
> of LLM use and agent tooling reveal the resulting attack sur-
> face, including role confusion, policy evasion through semantic
> reframing, and cross-tool “confused-deputy” behaviors that
> occur when untrusted text is mapped to high-privilege tool
> invocations.
> 
> Contemporary work on agent ecosystems proposes enforce-
> able interfaces (explicit argument typing, capability scoping,
> and pre-/post-conditions) and provenance signals (watermarks,
> cryptographic signing of trusted instructions) that agents can
> check before executing sensitive steps or sharing derived plans
> with peers [367].
**Matched Term**: `evade` | **Location**: `D. Behavioral Deepfakes` [offsets: 79315:79977]
> Recent research underscores how behavior
> emulation can facilitate attacks such as context poisoning in
> MCP ecosystems, where emulated agent behaviors propagate
> misinformation, leading to real-time system compromises in
> CPS applications [373]. For instance, in multi-agent envi-
> ronments, adversaries can emulate cooperative behaviors to
> achieve collusion, exploiting MCP’s standardized messaging to
> mask anomalies and evade detection, particularly in domains
> such as autonomous robotics, where behavioral fidelity is
> critical [328].
> 
> A key vulnerability lies in sensor spoofing of MCP tools,
> which can cause unsafe actuations in industrial control systems
> [289].
**Matched Term**: `evasion` | **Location**: `D. Behavioral Deepfakes` [offsets: 81875:82606]
> A complementary thread examines adversarial time-series
> attacks that optimize over temporal features, e.g., seasonality,
> lagged correlations, and shapelets, so that injected traces are
> misclassified as routine by state-of-the-art detectors. Traffic
> and ICS studies show that such feature-aware perturbations de-
> grade multivariate detectors and forecasting-residual schemes
> alike, achieving high evasion with small, causality-respecting
> edits [209]. Domain studies in water networks similarly reveal
> that hydraulics-consistent sensor attacks can remain stealthy
> while steering control actions, highlighting the need to treat
> MCP tool outputs as untrusted inputs whose behavioral plau-
> sibility alone is insufficient for trust [11].
**Matched Term**: `evasion` | **Location**: `D. Behavioral Deepfakes` [offsets: 84352:85136]
> Empir-
> ical studies show that classifier decisions are sensitive to eva-
> sive behaviors such as delayed loading, environment checks,
> and feigned user-driven I/O, enabling samples to cross decision
> boundaries while preserving functional malicious goals [240].
> Broader meta-surveys of adversarial attacks on deep models,
> including detectors used in security analytics, reinforce that
> small, structured edits to behavior traces or feature embed-
> dings can induce misclassification across families and vendors,
> foreshadowing automated “policy-aware” evasion in MCP-
> mediated pipelines [255]. Parallel work explores automated
> generation of attack techniques using learning-based planners,
> suggesting that behavior mimicry may soon be synthesized at
> scale rather than hand-engineered [148].
**Matched Term**: `evade` | **Location**: `D. Behavioral Deepfakes` [offsets: 85138:86016]
> Stealth also manifests in command-and-control patterns
> tuned to resemble benign heartbeat and telemetry processes
> observed by MCP toolchains. Unsupervised analyses of bea-
> coning demonstrate that periodicity, jitter, and payload traits
> can be shaped to evade statistical profiling while maintaining
> reliable control, complicating anomaly detection that relies
> on coarse traffic statistics [215]. At the same time, dynamic
> graph-based detectors that model process–file–socket interac-
> tions reveal promise against such mimicry by capturing higher-
> order temporal context; results indicate improved resilience
> to look-alike behaviors compared with flat sequence models,
> provided that execution provenance and graph dynamics are
> preserved end-to-end through MCP connectors [24], and that
> ensemble defenses are evaluated against generative, transfer-
> capable malware families [226].
**Matched Term**: `Evasion` | **Location**: `E. Privacy implications` [offsets: 86693:87400]
> TABLE XII
> DETECTION METHODS FOR BEHAVIORAL DEEPFAKES
> 
> Method
> Approach
> Evasion
> Risk
> 
> Latency
> 
> Residual Tests
> Statistical
> High
> Low
> Autoencoder
> Reconstruction
> High
> Medium
> Graph-based
> Structural
> Medium
> High
> Spatio-temporal
> Multi-channel
> Medium
> High
> Physics-informed
> Domain knowl-
> edge
> 
> Low
> Medium
> 
> Ensemble
> Combined
> Low-
> Medium
> 
> High
> 
> data exploitation in CPS. Adversaries can leverage deepfake-
> generated synthetic interactions, such as fabricated user
> prompts or emulated agent behaviors, to impersonate entities
> within MCP ecosystems, enabling the unauthorized extraction
> of personally identifiable information (PII) from intercon-
> nected tools, including sensor APIs or collaborative databases
> [165], [308].
**Matched Term**: `evade` | **Location**: `Method` [offsets: 90365:91198]
> Within the MCP boundary, identity exposure also occurs
> through inference and linkage: outputs from face-swap detec-
> tion, liveness checks, or profile enrichment services can leak
> biometric and behavioral hints that enable deanonymization
> or later impersonation. Empirical work on generalization for
> deepfake detection reveals that performance is fragile under
> content, codec, and generator shifts, thereby increasing the
> likelihood that adversaries can curate “just-different-enough”
> media to evade filters and establish trust for subsequent
> identity takeovers [315]. Studies of human vulnerability to
> science and news deepfakes add that even well-informed
> operators misclassify realistic synthetic videos at non-trivial
> rates, compounding the risk when MCP agents escalate tool
> calls based on operator confirmation alone [86], [89].
**Matched Term**: `evade` | **Location**: `F. AI Agent Vulnerabilities to Deepfake Threats` [offsets: 95400:95687]
> • Gap 2: Complexity in internal executions – Behavioral
> deepfakes can mimic reasoning patterns to evade internal
> consistency checks.
> 
> • Gap 3: Variability of operational environments –
> Visual deepfakes alter environmental perception, causing
> agents to misinterpret physical world states.
**Matched Term**: `Adaptive` | **Location**: `limitations requires coordinated research efforts:` [offsets: 109628:109952]
> • Adaptive
> regulatory
> frameworks:
> Develop
> cross-
> jurisdictional mechanisms for rapid response to deepfake
> harms while preserving privacy and due process.
> 4) Comparative Summary: Table XXI summarizes detec-
> tion maturity, key limitations, and CPS deployment feasibility
> 
> --- PAGE BREAK ---
> 
> JOURNAL OF LATEX CLASS FILES, VOL.
**Matched Term**: `adaptive` | **Location**: `VI. DETECTION TECHNIQUES` [offsets: 113357:113938]
> However, chal-
> lenges persist in balancing detection efficacy with privacy
> preservation, as watermarking and cryptographic provenance
> require standardized implementation across MCP servers to
> prevent supply-chain exploits [118]. Evaluations on datasets
> like FaceForensics++ adapted for CPS scenarios reveal that
> hybrid AI algorithms, including generative adversarial network
> (GAN) discriminators, outperform single-modality methods
> by 15-20% in real-world deployments, highlighting the need
> for adaptive training to counter evolving threats in protocol-
> enabled AI agents [42].
> 
> A.
**Matched Term**: `evasion` | **Location**: `B. Audio` [offsets: 119285:119813]
> Recent developments integrate biometric liveness detection
> with acoustic analysis, improving resilience against spoof-
> ing in CPS, where audio commands trigger physical actions
> [249]. For instance, challenge-response protocols have been
> enhanced with machine learning to adapt challenges dynam-
> ically, reducing evasion rates in MCP ecosystems prone to
> voice impersonation [70]. Studies report high effectiveness in
> distinguishing live from synthetic speech, particularly in multi-
> factor authentication scenarios for CPS [259].
**Matched Term**: `evasion` | **Location**: `C. Text` [offsets: 122262:122600]
> Studies emphasize hybrid
> 
> approaches combining stylometric metrics with blockchain to
> enhance provenance and reduce evasion risks from adaptive
> adversaries [95]. Limitations such as sensitivity to text length
> are mitigated through multitask learning frameworks, enabling
> real-time detection in resource-constrained CPS environments
> [198].
**Matched Term**: `adaptive` | **Location**: `B. Multi-factor & Context Validation` [offsets: 146286:146686]
> Multi-factor mechanisms integrate environmental awareness
> and biometric fusion to counter deepfake threats and imper-
> sonation [378]. AI-driven adaptive Multi-factor authentication
> models assess risk in real-time [46], with cross-modal sensor
> checks achieving 96.3% verification accuracy [378]. To re-
> inforce security, event processing frameworks analyze system
> behavior for anomaly detection [339].
**Matched Term**: `adaptive` | **Location**: `B. Multi-factor & Context Validation` [offsets: 146687:147178]
> Privacy-preserving tech-
> niques include federated learning [46] and layered geolocation
> verification [216]. Furthermore, temporal context factors en-
> hance spoofing detection by approximately 30% [14], helping
> systems dynamically adjust encryption to address adaptive
> adversaries [295].
> 
> 1) Sensor Fusion: Sensor fusion aggregates diverse data
> sources to create unified contexts, enabling the detection of
> inconsistencies such as mismatched Electric Network Fre-
> quency (ENF) patterns [131].
**Matched Term**: `adaptive` | **Location**: `E. Human & Policy Measures` [offsets: 165574:165986]
> However,
> human detection capabilities are often insufficient to identify
> sophisticated deepfakes [112]. Consequently, scholars argue
> for adaptive legislation driven by public sentiment [59] and
> enforced through technical cryptographic standards [143] to
> safeguard the digital trust ecosystem.
> 
> 3) Standards: Standardization ensures interoperability and
> security across the multi-vendor ecosystems typical of CPS.
**Matched Term**: `adaptive` | **Location**: `F. Emerging research directions` [offsets: 169083:169503]
> introduce AgentBound, a policy en-
> forcement framework that intercepts tool calls at the protocol
> level to prevent unauthorized privilege escalation and resource
> abuse [56]. Furthermore, dynamic evaluation frameworks are
> being developed to stress-test these agentic logic flows against
> multi-turn adaptive attacks, moving beyond static benchmarks
> to ensure resilience in continuous interaction environments
> [381].
> 
> VIII.
**Matched Term**: `adaptive` | **Location**: `VIII. CASE STUDY: AUTHENTICATING SMART GRID` [offsets: 177634:178137]
> Deviations beyond expected tolerances signal poten-
> tial compromise or drift, triggering mitigation or investigation
> workflows. This validation strategy highlights a key insight for
> securing AI-enabled CPS: resilience emerges not from perfect
> detection, but from continuous grounding in physical reality
> combined with adaptive response mechanisms.
> 
> While ANCHOR-Grid did not explicitly deploy LLM agents
> or MCP-mediated tools, it provides a concrete template for
> securing future AI agents operating DTs.
**Matched Term**: `adaptive` | **Location**: `IX. OPEN CHALLENGES AND FUTURE DIRECTIONS` [offsets: 181327:182764]
> OPEN CHALLENGES AND FUTURE DIRECTIONS
> 
> Open challenges in MCP for CPS encompass the need for
> adaptive protocols that evolve in response to advancements
> in deepfakes, ensuring the seamless integration of detec-
> tion mechanisms without compromising tool interoperability
> 
> Security mechanisms must tolerate re-
> alistic communication delays without
> degrading integrity verification
> 
> ENF-based authentication remains ro-
> bust under latency levels typical of
> smart grid telemetry networks
> 
> False alarms must be tightly bounded to
> avoid unnecessary operator intervention
> or destabilizing control actions
> 
> Authentication must detect stale or
> replayed measurements within opera-
> tionally relevant time windows
> 
> Environmental noise must not invali-
> date authentication or cause spurious
> alarms
> 
> Heavyweight ML-based detection is
> difficult to deploy at scale under CPS
> resource constraints
> 
> ENF extraction and correlation are suit-
> able for edge or near-edge deployment
> 
> Security layers must be positioned ap-
> propriately within CPS control hierar-
> chies
> 
> ANCHOR-Grid functions as a trust-
> validation layer for digital twins rather
> than a real-time protection mechanism
> 
> or agent performance [99]. Identity fragmentation remains
> a persistent issue, where fragmented authentication across
> MCP servers heightens vulnerability to deepfake injections,
> necessitating unified identity management to maintain trust
> in agent-environment interactions [242].
**Matched Term**: `adaptive` | **Location**: `A. Rapid Changing Deepfake Detection Landscape` [offsets: 185884:186306]
> Transfer learning frameworks enable detectors
> to generalize from known generative artifacts, mitigating the
> lag behind novel creation methods [37]. Ensemble models
> that aggregate predictions from diverse architectures improve
> robustness, counteracting the adaptive nature of attackers [7].
> These advancements ensure MCP remains a viable conduit
> for secure CPS operations amid ongoing generational leaps in
> deepfakes [253].
**Matched Term**: `adaptive` | **Location**: `C. Intelligence at the Edge` [offsets: 188190:188485]
> Advancing these defenses includes adaptive optimization
> techniques that fine-tune parameters on-device, enhancing
> responsiveness to local CPS threats [306]. End-to-end frame-
> works minimize overhead by integrating detection directly into
> MCP protocols, supporting seamless edge deployment [107].
**Matched Term**: `adaptive` | **Location**: `X. CONCLUSION` [offsets: 195659:196173]
> In
> CPS, where failures can have physical repercussions, defense-
> in-depth ensures redundancy, with each layer addressing spe-
> cific vulnerabilities in agent interactions and environmental
> interfaces. By embedding these principles into MCP speci-
> fications, systems can achieve adaptive security, dynamically
> responding to threats while maintaining operational continuity.
> This multi-tiered strategy not only deters attacks but also
> minimizes their impact, promoting sustained functionality in
> adversarial settings.
**Matched Term**: `adaptive` | **Location**: `A. Rahman, X. Liang, N. W. Keong, K. De Zoysa et al., “Model context` [offsets: 206848:207000]
> Fereidouni, “Privacy-
> 
> preserving federated learning framework for risk-based adaptive au-
> thentication,” arXiv preprint arXiv:2508.18453, 2025.
> [47] J.
**Matched Term**: `adaptive` | **Location**: `D. Koirala, B. Pandey, and S. Das, “Model context protocols in adaptive` [offsets: 211654:211787]
> Pandey, and S. Das, “Model context protocols in adaptive
> transport systems: A survey,” arXiv preprint arXiv:2508.19239, 2025.
> [72] M.
**Matched Term**: `adaptive` | **Location**: `A. Raza, “Connected and automated vehicles: Infrastructure, applica-` [offsets: 257882:258082]
> Nagarajan, “Enhancing cloud security: A multi-
> 
> factor authentication and adaptive cryptography approach using ma-
> chine learning techniques,” IEEE Open Journal of the Computer
> Society, 2025.
> [296] T.
**Matched Term**: `adaptive` | **Location**: `M. Kazim, “Deepfake image forensics for privacy protection and` [offsets: 261731:261849]
> Jahangir,
> 
> “A multi-agent adaptive deep learning framework for online intrusion
> detection,” Cybersecurity, vol. 7, no.
**Matched Term**: `Adaptive` | **Location**: `A. Rezazadeh, A. Shah, Y. Bao et al., “Mcp-bench: Benchmarking` [offsets: 275102:275263]
> Panchal, and D. Kang, “Adaptive attacks break
> 
> defenses against indirect prompt injection attacks on llm agents,” arXiv
> preprint arXiv:2503.00061, 2025.
> [382] B.
