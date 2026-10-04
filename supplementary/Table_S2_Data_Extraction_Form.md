# Supplementary Table S2: Data Extraction Form

The following standardized data extraction schema was applied to all 182 extracted corpus records (171 MCP-specific synthesis works and 11 Set B background works). Extraction was performed by the primary author and verified against an independent 20% calibration audit.

| Field Name | Data Type | Permitted Values / Schema | Description |
| :--- | :--- | :--- | :--- |
| `record_id` | String | Unique identifier | Format: `<first_author>-<year>-<short_title>` (e.g., `hou-2026-mcp-landscape`). |
| `title` | String | Verbatim string | Full canonical title of the publication or standard. |
| `authors` | String | Semicolon-delimited | Full author list. |
| `year` | Integer | `2024`, `2025`, `2026` (or historical for Set B) | Year of publication or official release. |
| `venue_or_source` | String | String | Conference, journal, repository, or standard body (e.g., *IEEE S&P*, *ACM TOSEM*, *arXiv*). |
| `doi_or_url` | String | DOI string or URL | Persistent DOI or official web link. |
| `evidence_tier` | Categorical | `E1`, `E2`, `E3`, `E4`, `E5` | Evidence quality tier (Table 4 in main text). |
| `mcp_protocol_version`| Categorical | `2024-11-05`, `2025-03-26`, `2025-06-18`, `2025-11-25`, `2026-02-17`, `Unspecified` | Exact MCP specification revision evaluated or targeted. |
| `sdk_version` | String | Text | Language SDK tested (e.g., Python SDK `v0.1.0`–`v1.2.0`, TypeScript SDK `v0.6.0`, FastMCP). |
| `host_client_tested` | String | Text | Client environments tested (e.g., Claude Desktop, Cursor, Cline, custom harness). |
| `threat_layer` | Categorical | `A`, `B`, `C`, `D`, `Multi`, `None` | Structural layer in MCP architecture (A: Semantic, B: Protocol, C: Server/Host, D: Client UI). |
| `taxonomy_class_primary`| Categorical | `A1`–`A3`, `B1`–`B3`, `C1`–`C7`, `D1`–`D3` | Primary taxonomy classification under 16-class system. |
| `taxonomy_class_secondary`| Categorical | `None`, or valid class ID | Secondary classification for multi-stage attacks. |
| `boundary_crossing` | Categorical | `U -> L`, `L -> S_i`, `S_i -> L`, `S_i -> X_i`, `S_i -> S_j`, `L -> UI` | Architectural trust boundary traversed by attack or defense. |
| `attack_vector` | Text | Free text | Specific exploitation technique (e.g., tool injection, confused deputy, cross-tenant leak). |
| `defense_role` | Categorical | `primary`, `secondary`, `proposal_only`, `none` | Role of defense proposal in the paper. |
| `defense_name` | String | Text | Formal system or defense mechanism name (e.g., `SAMOS`, `ChainWatch`, `MCIP`). |
| `defense_maturity` | Categorical | `L0`, `L1`, `L2`, `L3` | Maturity level (L0: Conceptual, L1: Offline/Proof-of-Concept, L2: Integrated/Testbed, L3: Production). |
| `defense_placement` | Categorical | `Client Host`, `Local Proxy`, `Server Runtime`, `Model Pipeline`, `Transport Gateway` | Architectural insertion point of the defense. |
| `adaptive_evaluation` | Categorical | `Yes`, `No`, `Unclear`, `N/A` | Evaluated against an adaptive adversary intentionally targeting defense heuristics? |
| `empirical_metric` | Text | Text | Primary quantitative evaluation metrics (e.g., ASR, Detection F1, Latency overhead). |
