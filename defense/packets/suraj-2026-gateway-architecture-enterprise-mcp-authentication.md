# Evidence Locator Packet: suraj-2026-gateway-architecture-enterprise-mcp-authentication

- **Title**: A Gateway Architecture for Enterprise MCP Authentication: Unifying Heterogeneous Auth, Identity Delegation, and the User / Non-User Persona Problem
- **Year**: 2026
- **Evidence Tier**: E2
- **Triage**: kandidat_agent
- **Role Status**: Human Coded: defense_primary
- **Link**: https://arxiv.org/abs/2608.10760
- **Fulltext Path**: mcp-sok-corpus\corpus\E2_preprint\suraj-2026-gateway-architecture-enterprise-mcp-authentication\fulltext.txt
- **Character Count**: 38853

## Block 2: Contribution Sentences
**Location**: `Abstract` [offsets: 722:920]
> This paper reports an industry
> deployment that resolves the crisis with a centralized
> MCP gateway: a single aggregation, governance, and
> authentication layer that fronts every downstream MCP
> server.
**Location**: `Abstract` [offsets: 964:1025]
> We make four contributions grounded in production
> experience.
**Location**: `Abstract` [offsets: 1026:1150]
> First, we present a two-axis authenti-
> cation model that every MCP server must satisfy—
> a persona axis (interactive user vs.

## Block 3: Method Locator
**Section Heading**: `A Gateway Architecture for Enterprise MCP Authentication` [section offsets: 15:164]
**First 120 words verbatim** [offsets: 15:822]
> A Gateway Architecture for Enterprise MCP Authentication
> 
> Authentication:
> Unifying Heterogeneous Auth, Identity Delegation, and the User / Non-User
> 
> Abstract
> 
> The Model Context Protocol (MCP) has become the
> de-facto interface for connecting LLM agents to enter-
> prise tools, and adoption has been explosive: within
> a year, large organizations went from zero to dozens
> of internally built MCP servers.
> That speed created
> a governance crisis. Each team implemented authenti-
> cation independently—some with no auth, some with
> API keys, some with full OAuth—producing a frag-
> mented landscape with no consistent way to authorize
> callers, track who did what, or offboard a departing em-
> ployee across the fleet. This paper reports an industry
> deployment that resolves the crisis with a centralized
> MCP gateway: a
**Section Heading**: `A Gateway Architecture for Enterprise MCP` [section offsets: 2371:2678]
**First 120 words verbatim** [offsets: 2371:3159]
> A Gateway Architecture for Enterprise MCP
> 
> Persona Problem
> 
> Suraj Kumar∗
> Amy Wang†
> Srinivasan Manoharan‡
> 
> Enterprise AI Platform Engineering
> 
> August 2026
> 
> enterprise authentication, OAuth 2.0, RFC 8693 token
> exchange, PKCE, device code, ROPC, service accounts,
> AI agent identity, zero-trust, API gateway
> 
> 1
> Introduction
> 
> 1.1
> The
> Governance
> Crisis
> Behind
> MCP Adoption
> 
> When the Model Context Protocol [1] was published
> in late 2024, it solved a real problem elegantly: it gave
> LLM agents a uniform way to discover and invoke exter-
> nal tools. Adoption inside large enterprises was imme-
> diate and uncoordinated. A team that wanted to expose
> its service to an internal AI assistant could stand up an
> MCP server in an afternoon. Within months, a single
> organization could find itself running
**Section Heading**: `A Gateway Architecture for Enterprise MCP Authentication` [section offsets: 4517:4678]
**First 120 words verbatim** [offsets: 4517:5269]
> A Gateway Architecture for Enterprise MCP Authentication
> 
> dar, and document tools. It must serve two very differ-
> ent kinds of caller through the same endpoint:
> 1. An interactive employee asking an AI assistant to
> “summarize my unread mail.”
> This call must run
> as that user: it must see only their mailbox, and
> the downstream Microsoft Graph token must carry
> their identity.
> This requires an interactive OAuth
> authorization-code flow with the downstream iden-
> tity provider.
> 2. A nightly automation that compiles a team calen-
> dar digest. No human is in the loop. It authenticates
> with its own service-account credentials (client cre-
> dentials), and must not be able to impersonate any
> individual user.
> A naive design would stand up two servers—one per
**Section Heading**: `A Gateway Architecture for Enterprise MCP Authentication` [section offsets: 9628:13609]
**First 120 words verbatim** [offsets: 9628:10504]
> A Gateway Architecture for Enterprise MCP Authentication
> 
> Figure 1: System overview. Heterogeneous clients authenticate once to the gateway, which authenticates them against
> enterprise SSO and resolves the correct downstream credential per MCP server. The gateway is the single point for auth,
> aggregation, guardrails, observability, and token caching. Downstream servers only verify gateway-issued tokens via a shared
> SDK.
> 
> MCP GATEWAY
> Web Clients
> 
> client auth
> 
> chat UIs (user)
> 
> Desktop Clients
> 
> native apps (user)
> 
> Custom SDK Clients
> 
> user + non-user
> 
> Low/No-code
> 
> user + non-user
> 
> Table 1: Per-server auth vs. centralized gateway.
> 
> Dimension
> Per-server
> Gateway
> 
> SSO registrations
> N (one each)
> 1
> Audit trail
> Fragmented
> Unified
> Offboarding
> Contact
> each
> team
> 
> Central revoke
> 
> Token caching
> Re-
> implemented
> 
> Shared
> 
> Tool-context bloat
> N catalogs
> Tool search
> Guardrails
> Per-team

## Block 4: Evaluation Locator
no hits

## Block 5: Attack-Set Excerpts
**Location**: `A Gateway Architecture for Enterprise MCP Authentication` [offsets: 28347:28521]
> • Downstream
> authorization
> —
> fine-grained,
> resource-level decisions made by the downstream
> system
> using
> the
> forwarded
> credential:
> which
> records, which mailbox, which dataset.

## Block 6: Baseline Excerpts
no hits

## Block 7: Cost Excerpts
no hits

## Block 8: Limitations
no hits

## Block 9: Adaptivity Hits
no hits
