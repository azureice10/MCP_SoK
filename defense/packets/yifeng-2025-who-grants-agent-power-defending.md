# Evidence Locator Packet: yifeng-2025-who-grants-agent-power-defending

- **Title**: Who Grants the Agent Power? Defending Against Instruction Injection via Task-Centric Access Control
- **Year**: 2025
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2510.26212
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\yifeng-2025-who-grants-agent-power-defending\fulltext.txt
- **Character Count**: 15898

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 832:963]
> We present AgentSentry,
> a lightweight runtime task-centric access control framework that
> enforces dynamic, task-scoped permissions.
**Location**: `Introduction` [offsets: 5208:6013]
> we propose AgentSentry, a novel
> task-centric access control framework. The core principle of AgentSen-
> try is to dynamically scope an agent’s permissions to the specific,
> user-authorized task at hand. It grants minimal, temporary priv-
> ileges that are automatically revoked upon task completion. Our
> contributions are:
> • We define and formalize the threat of multimodal instruction
> injection against AI agents in a realistic threat model that assumes
> an uncompromised OS and unmodified apps.
> • We propose Task-Centric Access Control as a new security para-
> digm for AI agents and present AgentSentry, a lightweight run-
> time framework to enforce it.
> • We demonstrate through a compelling case study that AgentSen-
> try effectively prevents instruction injection attacks while allow-
> ing legitimate tasks to

## Block 3: Method Locator
no hits

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
no hits

## Block 6: Baseline Excerpts
**Location**: `Introduction` [offsets: 6566:6691]
> Unlike prior work [11], we adopt a real-
> world setting that assumes the attacker has no special privileges
> on the device [8].

## Block 7: Cost Excerpts
**Location**: `Abstract` [offsets: 704:831]
> Malicious instructions,
> embedded in otherwise benign content like emails, can hijack the
> agent to perform unauthorized actions.
**Location**: `Abstract` [offsets: 832:963]
> We present AgentSentry,
> a lightweight runtime task-centric access control framework that
> enforces dynamic, task-scoped permissions.
**Location**: `Introduction` [offsets: 6692:6874]
> Their sole vector is content injection: embed-
> ding malicious natural language instructions within benign car-
> riers—such as emails or webpages—that the agent is expected to
> process.
**Location**: `Introduction` [offsets: 7184:7304]
> Our model assumes the
> defender can mediate the agent’s actions at runtime but cannot pre-
> sanitize all external content.
**Location**: `Introduction` [offsets: 8298:8386]
> Figure 1: AgentSentry Architecture: Task-to-Policy Genera-
> tion and Runtime Enforcement.
**Location**: `2. Runtime Enforcement. The Policy Enforcement Point (PEP)` [offsets: 9383:9403]
> Runtime Enforcement.

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
