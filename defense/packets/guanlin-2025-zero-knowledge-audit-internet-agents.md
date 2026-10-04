# Evidence Locator Packet: guanlin-2025-zero-knowledge-audit-internet-agents

- **Title**: Zero-Knowledge Audit for Internet of Agents: Privacy-Preserving Communication Verification with Model Context Protocol
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2512.14737
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\guanlin-2025-zero-knowledge-audit-internet-agents\fulltext.txt
- **Character Count**: 70084

## Block 2: Contribution Sentences
**Location**: `Abstract—Existing agent communication frameworks face crit-` [offsets: 559:694]
> We introduce a framework for auditing agent communications
> that keeps messages private while still checking they follow
> expected rules.

## Block 3: Method Locator
**Section Heading**: `implementation.` [section offsets: 62288:62852]
**First 120 words verbatim** [offsets: 62288:63232]
> implementation.
> 
> The experimental results demonstrate that while proof gen-
> eration introduces overhead, the asynchronous design ensures
> that this overhead has minimal impact on MCP communication
> performance, with total overhead remaining below 4.14%
> of communication costs. This suggests that zk-MCP is able
> to provide privacy-preserving audit verification with limited
> impact on standard MCP performance, indicating potential ap-
> plicability to IoA frameworks where communication efficiency
> is important and various types of AI agents may need to be
> supported.
> 
> VI. CONCLUSION
> 
> This paper presents the first zero-knowledge proof-based
> privacy-preserving audit framework for agent communications
> in IoA systems. By integrating MCP’s context-aware commu-
> nication capabilities with zk-SNARK’s privacy-preserving ver-
> ification mechanisms, zk-MCP enables verifiable audit trails
> without exposing sensitive communication content or com-
> promising
**Section Heading**: `implementation, which utilizes Circom circuits and integrates` [section offsets: 63971:64367]
**First 120 words verbatim** [offsets: 63971:64856]
> implementation, which utilizes Circom circuits and integrates
> with MCP’s bidirectional communication, offers an initial
> exploration of the framework’s practical feasibility for IoA
> deployments. While preliminary results are promising, further
> testing and refinement will be needed to fully assess its
> applicability to privacy-preserving audit verification in diverse
> and regulated environments.
> 
> REFERENCES
> 
> [1] V. S. Narajala and I. Habler, “Enterprise-grade security for the model
> 
> context protocol (mcp): Frameworks and mitigation strategies,” arXiv
> preprint arXiv:2504.08623, 2025.
> [2] R. Lavin, X. Liu, H. Mohanty, L. Norman, G. Zaarour, and B. Krish-
> 
> namachari, “A survey on the applications of zero-knowledge proofs,”
> arXiv preprint arXiv:2408.00243, 2024.
> [3] E. B. Sasson, A. Chiesa, C. Garman, M. Green, I. Miers, E. Tromer, and
> 
> M. Virza, “Zerocash: Decentralized anonymous

## Block 4: Evaluation Locator
**Section Heading**: `21 Output results:;` [section offsets: 31442:31511]
**First 120 words verbatim** [offsets: 31442:32141]
> 21 Output results:;
> 
> 22 for j = 0 to K −1 do
> 
> 23
> counts[j] ←sum[j];
> 
> C. Security Analysis
> 
> The security properties of zk-MCP are defined as follows:
> Definition 1 (Data Authenticity). The prover can convince
> the verifier that the output counts are computed from the
> 
> --- PAGE BREAK ---
> 
> private input JSON messages that match the public hashes,
> without revealing the actual message content. Formally, we
> define the following experiment:
> 
> Expauth
> 
> zk-MCP,A(1λ, C) :
> 
> • (crs) ←Setup(1λ, C)
> 
> • (π, x) ←A(crs)
> 
> • w ←E(transA)
> 
> • If ((x, w) /∈RC and Verify(crs, π, x) = 1) return 1
> 
> • Else return 0
> Here, A is a non-uniform polynomial-time adversary, RC
> is the relation defined by the circuit C, transA is
**Section Heading**: `V. PERFORMANCE EVALUATION` [section offsets: 50471:51016]
**First 120 words verbatim** [offsets: 50471:51329]
> V. PERFORMANCE EVALUATION
> 
> In this section, we evaluate the performance of zk-MCP
> through comprehensive experiments. Our evaluation focuses
> on two key aspects: (1) the scalability of zero-knowledge
> proof generation with respect to circuit parameters, and (2)
> the impact of zk-MCP on standard MCP communication
> performance. The experimental results demonstrate that zk-
> MCP achieves privacy-preserving audit verification, with proof
> generation overhead remaining below 4.14% of total commu-
> nication costs due to asynchronous processing design.
> 
> A. Experiment Setup
> 
> Our experimental evaluation is conducted on two machines
> equipped with AMD 6850H processors (8 cores @ 3.2GHz)
> and 32GB RAM, running Arch Linux with kernel version
> 5.15.62.1. The MCP servers and zero-knowledge proof com-
> ponents are deployed on these machines to simulate agents
> communication
**Section Heading**: `A. Experiment Setup` [section offsets: 51016:51201]
**First 120 words verbatim** [offsets: 51016:51829]
> A. Experiment Setup
> 
> Our experimental evaluation is conducted on two machines
> equipped with AMD 6850H processors (8 cores @ 3.2GHz)
> and 32GB RAM, running Arch Linux with kernel version
> 5.15.62.1. The MCP servers and zero-knowledge proof com-
> ponents are deployed on these machines to simulate agents
> communication environment.
> 
> The zk-MCP circuit is implemented using Circom, a
> domain-specific language for zero-knowledge circuit design.
> The zero-knowledge proof framework is built on snarkjs,
> which provides the proving and verification algorithms for zk-
> SNARKs. The experimental MCP tools are implemented using
> the Python-based fastmcp library, which enables efficient MCP
> protocol implementation. The circuit parameters are config-
> ured as follows: MAX JSON = 64 bytes, MAX TYPE = 20
> bytes, and NUM TYPES = 8,
**Section Heading**: `B. Experiment 1: Circuit Parameter Scalability` [section offsets: 52197:57230]
**First 120 words verbatim** [offsets: 52197:52999]
> B. Experiment 1: Circuit Parameter Scalability
> 
> The first experiment evaluates the scalability of zk-MCP
> with respect to the number of messages processed by the
> zero-knowledge proof circuit. We vary the number of MCP
> messages n from 20 to 29 and measure the following perfor-
> mance metrics: (1) CPU time consumption for Setup, Prove,
> and Verify phases; (2) memory consumption during proof
> generation and verification; (3) circuit size metrics including
> constraint count and gate count; and (4) proof size and system
> parameter size (verification key and proving key) in bytes.
> 
> The circuit construction follows the zk-MCP specification
> in Sec. 4.2, where each message undergoes format validation,
> type extraction, type matching, count accumulation, and hash
> computation. As n increases, the circuit must

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
**Location**: `C. Experiment 2: MCP Communication Performance Impact` [offsets: 58233:58532]
> We measure the following
> metrics: (1) MCP message exchange latency (baseline standard
> MCP performance); (2) total session time including proof
> generation; (3) proof generation overhead as a percentage of
> total communication time; and (4) the time distribution across
> Setup, Prove, and Verify phases.
**Location**: `C. Experiment 2: MCP Communication Performance Impact` [offsets: 61341:61516]
> For a typical communication session with 8
> messages, the MCP communication time remains at baseline
> performance for each model, while proof generation adds min-
> imal overhead.
**Location**: `C. Experiment 2: MCP Communication Performance Impact` [offsets: 61554:61725]
> 6, DeepSeek
> V3, GPT-4.1mini, and GPT-3.5 turbo all demonstrate that zk-
> MCP introduces less than 4.14% overhead on their respective
> baseline MCP communication performance.

## Block 7: Cost Excerpts
**Location**: `V. PERFORMANCE EVALUATION` [offsets: 50794:51014]
> The experimental results demonstrate that zk-
> MCP achieves privacy-preserving audit verification, with proof
> generation overhead remaining below 4.14% of total commu-
> nication costs due to asynchronous processing design.
**Location**: `B. Experiment 1: Circuit Parameter Scalability` [offsets: 53675:54080]
> Time (seconds)
> 
> 10
> 1
> 
> 10
> 3
> 
> 10
> 0
> 
> 2
> 1
> 2
> 3
> 2
> 5
> 2
> 7
> 2
> 9
> 
> 2
> 1
> 2
> 3
> 2
> 5
> 2
> 7
> 2
> 9
> 
> Input Size (n)
> 
> Input Size (n)
> 
> (c) Constraints and Wires
> 
> (d) Generated File Sizes
> 
> 10
> 6
> 
> Constraints
> Wires
> 
> Proof JSON
> Verification Key
> ZKey (KB)
> 
> 10
> 6
> 
> 10
> 6
> 
> 10
> 5
> 
> 10
> 4
> 
> File Size (KB)
> 
> Constraints
> 
> 10
> 5
> 
> 10
> 5
> 
> Wires
> 
> 10
> 3
> 
> 10
> 2
> 
> 10
> 4
> 
> 10
> 4
> 
> 10
> 1
> 
> 2
> 1
> 2
> 3
> 2
> 5
> 2
> 7
> 2
> 9
> 
> 2
> 1
> 2
> 3
> 2
> 5
> 2
> 7
> 2
> 9
> 
> Input Size (n)
> 
> Input Size (n)
> 
> Fig.
**Location**: `B. Experiment 1: Circuit Parameter Scalability` [offsets: 56642:56706]
> 4(d),
> demonstrates efficient storage and communication overhead.
**Location**: `C. Experiment 2: MCP Communication Performance Impact` [offsets: 57804:57975]
> 4.4, zero-knowledge proof generation is performed
> asynchronously after MCP communication sessions complete,
> ensuring that MCP message exchange latency remains un-
> changed.
**Location**: `C. Experiment 2: MCP Communication Performance Impact` [offsets: 58233:58532]
> We measure the following
> metrics: (1) MCP message exchange latency (baseline standard
> MCP performance); (2) total session time including proof
> generation; (3) proof generation overhead as a percentage of
> total communication time; and (4) the time distribution across
> Setup, Prove, and Verify phases.
**Location**: `C. Experiment 2: MCP Communication Performance Impact` [offsets: 59195:59371]
> 6(c) for
> GPT-3.5 turbo, the results consistently demonstrate that zk-
> MCP introduces less than 4.14% overhead on original MCP
> communication performance across all three models.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
**Matched Term**: `adaptive` | **Location**: `A. Model Context Protocol Research` [offsets: 9968:10387]
> Research highlights the need for enterprise-grade mitigation
> frameworks, including systematic threat modeling, actionable
> security patterns, and technical controls tailored for MCP im-
> plementations. Recommendations emphasize rigorous gover-
> nance, continuous monitoring, and adaptive security measures
> throughout the MCP lifecycle.
> 
> Additionally, MCP research has explored multi-agent sys-
> tems and adaptive protocols.
**Matched Term**: `adaptive` | **Location**: `A. Model Context Protocol Research` [offsets: 10302:10552]
> Additionally, MCP research has explored multi-agent sys-
> tems and adaptive protocols. The works in [11], [12] demon-
> strate that MCP enables standardized context sharing, scalable
> coordination, and efficient context management in multi-agent
> systems.
**Matched Term**: `Adaptive` | **Location**: `A. Model Context Protocol Research` [offsets: 10388:11027]
> The works in [11], [12] demon-
> strate that MCP enables standardized context sharing, scalable
> coordination, and efficient context management in multi-agent
> systems. Adaptive protocols within MCP dynamically adjust
> information exchange based on task complexity and resource
> constraints, reducing communication overhead while maintain-
> ing performance in distributed sensor networks, autonomous
> vehicles, and collaborative problem-solving scenarios.
> 
> However, to the best of our knowledge, no previous
> work has considered the usage and implementation of zero-
> knowledge proof-based audit mechanisms in the MCP-based
> agent communication area.
**Matched Term**: `Adaptive` | **Location**: `A. System Model` [offsets: 18366:19117]
> [1], [9]
> MCP Security Threats &
> Mitigation
> 
> [11], [12]
> Multi-Agent Systems &
> Adaptive Protocols
> 
> [2], [13]
> Zero-Knowledge Proof
> Protocols
> 
> [2], [18], [19]
> ZKP Applications in
> Distributed Systems
> 
> [24], [25]
> Context Compression &
> Efficiency
> 
> [26], [27]
> Long-Context
> Processing
> 
> Our work
> ZK-based MCP
> audit model
> 
> TABLE II: Related Works on MCP Security, Privacy, and Zero-Knowledge Proofs
> 
> Reference
> Detailed descriptions
> [1], [9], [10]
> Implement MCP architecture, security frameworks, and enterprise-grade mit-
> igation strategies for multi-agent systems without zero-knowledge audit veri-
> fication.
> [11], [12], [24]
> Solving the MCP-based agent communication coordination, adaptive proto-
> cols, and context efficiency problems with traditional methods.
**Matched Term**: `adaptive` | **Location**: `A. System Model` [offsets: 18755:19260]
> Reference
> Detailed descriptions
> [1], [9], [10]
> Implement MCP architecture, security frameworks, and enterprise-grade mit-
> igation strategies for multi-agent systems without zero-knowledge audit veri-
> fication.
> [11], [12], [24]
> Solving the MCP-based agent communication coordination, adaptive proto-
> cols, and context efficiency problems with traditional methods.
> [2], [13], [14]
> Develop zero-knowledge proof protocols and applications in distributed sys-
> tems, blockchain, and IoT without MCP integration.
**Matched Term**: `Adaptive` | **Location**: `A. System Model` [offsets: 20314:20541]
> (1) MCP enables standardized context sharing and scalable
> coordination.
> (2) Adaptive protocols dynamically adjust information ex-
> change based on task complexity.
> 
> (1) zk-SNARKs, zk-STARKs, Bulletproofs for distributed
> systems.
**Matched Term**: `Adaptive` | **Location**: `M. Virza, “Zerocash: Decentralized anonymous payments from bitcoin,”` [offsets: 66223:66391]
> Konatham, and D. Uddandaraoo, “Adaptive model
> 
> context protocols for multi-agent collaboration,” Journal of Information
> Systems Engineering and Management, vol. 10, no.
**Matched Term**: `adaptive` | **Location**: `M. Virza, “Zerocash: Decentralized anonymous payments from bitcoin,”` [offsets: 66384:66462]
> 10, no. 50s, 2025,
> adaptive protocols for multi-agent collaboration. [Online].
