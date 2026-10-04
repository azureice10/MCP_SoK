# Supplementary Table S1: Query Strings, Sources, and Identification Counts

## 1. Search Query Specifications

| Source Database | Query Syntax / Parameters | Target Fields | Date Window | Raw Hits | Deduplicated Hits |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **arXiv** | `all:"Model Context Protocol" OR all:"MCP"` combined with security filters (`security`, `vulnerability`, `attack`, `injection`, `poisoning`) | All fields | Nov 2024 – Sep 2026 | 200 | 184 |
| **OpenAlex** | `default.search:"Model Context Protocol"` AND (`security` OR `attack` OR `vulnerability`) | Title, Abstract, Concepts | Nov 2024 – Sep 2026 | 200 | 178 |
| **Semantic Scholar** | `query: "Model Context Protocol security"` (via REST API) | Title, Abstract | Nov 2024 – Sep 2026 | 95 | 92 |
| **Gray Literature & Standards** | Direct monitoring: MCP GitHub specifications, OWASP GenAI Top 10, NSA Agent Guidance, NVD/GHSA CVE trackers, Vendor advisories | Full text / advisories | Nov 2024 – Sep 2026 | 102 | 102 |
| **IEEE Xplore (Native)** | `("All Metadata":"Model Context Protocol") AND ("All Metadata":security OR "All Metadata":attack OR "All Metadata":vulnerability OR "All Metadata":threat OR "All Metadata":"prompt injection" OR "All Metadata":poisoning OR "All Metadata":authorization)` | All Metadata | 2024 – Sep 2026 | 112 | 112 |
| **ACM Digital Library (Native)** | `[[Title: "model context protocol"] OR [Abstract: "model context protocol"]] AND [[Abstract: security] OR [Abstract: attack*] OR [Abstract: vulnerab*] OR [Abstract: threat*] OR [Abstract: "prompt injection"] OR [Abstract: poisoning] OR [Abstract: authoriz*]]` | Title, Abstract | Post-Nov 1, 2024 | 13 | 13 |
| **Scopus (Native / Elsevier)** | `TITLE-ABS-KEY("Model Context Protocol" AND (security OR attack OR vulnerability OR threat OR "prompt injection" OR poisoning OR authorization))` | Title, Abstract, Keywords | Nov 2024 – Sep 2026 | 172 | 172 |

---

## 2. Cross-Database Deduplication & Disposition

```
Phase 1: Baseline Pool (Identification: Sep 2026)
  • Academic Databases (arXiv, OpenAlex, Semantic Scholar): 495 raw records
  • Gray Literature & Standards (NVD, GitHub, OWASP, NSA): 102 raw records
  • Deduplication across sources -> 460 unique records
  • Disposition: 157 included (148 MCP synthesis + 9 Set B background), 303 excluded.

Phase 2: Supplementary Native Academic Searches (Identification: Oct 2026)
  • Raw Retrieval: IEEE Xplore (112), Scopus (172), ACM Digital Library (13) = 297 records
  • Cross-database deduplication -> 213 unique records
    - Scopus-only: 88 records
    - IEEE + Scopus overlap: 82 records
    - IEEE-only: 30 records
    - ACM-only: 11 records
    - ACM + Scopus overlap: 2 records
  • Overlap with Phase 1 Baseline Pool (454): 56 records (36 included, 20 excluded)
  • New unique records evaluated under calibrated PRISMA protocol: 154 records
  • Disposition: 25 included (23 Tier E1 MCP synthesis + 2 Set B background), 129 excluded.

Consolidated PRISMA Screening Pool:
  • Total unique deduplicated records screened: 614 records (460 baseline + 154 supplementary)
  • Total records excluded: 432 records (303 baseline + 129 supplementary)
  • Total records extracted: 182 records (171 MCP-specific synthesis + 11 Set B background)
  • External held-out validation benchmark: 22 records (20 CVEs + 2 Vendor Disclosures)
```
