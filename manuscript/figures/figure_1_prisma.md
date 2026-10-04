# Figure 1: PRISMA-ScR Flow Diagram

```mermaid
flowchart TD
    subgraph Identification ["Identification (n = 614 unique records)"]
        A1["Baseline Academic Databases<br/>(arXiv, OpenAlex, Semantic Scholar)<br/>n = 495 raw records"] --> D1["Baseline Deduplication<br/>(n = 460 unique records)"]
        A2["Baseline Gray Literature & Standards<br/>(Spec, OWASP, NSA, NVD/GHSA, Vendor)<br/>n = 102 raw records"] --> D1
        B1["Supplementary Academic Databases<br/>(IEEE Xplore, ACM DL, Scopus)<br/>n = 297 raw records"] --> D2["Supplementary Deduplication<br/>(n = 213 unique records)"]
        D2 --> D3["Cross-Pool Deduplication<br/>(56 overlap with baseline)<br/>n = 154 supplementary records"]
        D1 --> Pool["Consolidated Screening Pool<br/>(460 baseline + 154 supplementary)<br/>n = 614 unique deduplicated records"]
        D3 --> Pool
    end

    subgraph Screening ["Screening & Eligibility (n = 614)"]
        Pool --> Screen["Title & Abstract Screening<br/>+ Substitution Testing<br/>(Dual-coder calibration κ = 0.84, n = 92;<br/>Post-audit reconciliation n = 137, n = 84)"]
        Screen --> Excluded["Excluded Records (n = 432)<br/>• IC2 Off-topic / Non-agent: 164<br/>• EC1 Plumbing / App without security claim: 125<br/>• EC2 Generic multi-agent security: 56<br/>• EC5 Acronym collision / Non-MCP: 82<br/>• EC3 Short abstract / Poster: 5<br/>• EC4 Non-English: 0"]
        Screen --> Included["Included Records (n = 182)"]
    end

    subgraph Extraction ["Extraction & Corpus Partitioning (n = 182)"]
        Included --> Corpus["MCP-Specific Synthesis Corpus<br/>(148 baseline + 23 supplementary)<br/>n = 171 records<br/>• Tier E1 Peer-Reviewed: 82<br/>• Tier E2 Preprints: 85<br/>• Tier E3 Specifications/Standards: 4"]
        Included --> SetB["Set B Methodological Background<br/>(9 baseline + 2 supplementary)<br/>n = 11 records"]
    end

    subgraph Validation ["External Empirical Validation (Held-Out Benchmark)"]
        Ext["Tier E4 Practitioner Disclosures & CVEs<br/>(20 CVEs + 2 Vendor Disclosures)<br/>n = 22 held-out empirical records<br/>• 15 Disclosure / Product Clusters<br/>• Pre-revision absorption: 17/22 (77.3%)<br/>• Post-revision absorption: 20/22 (90.9%)"]
    end

    Corpus -.->|"Taxonomy tested against"| Ext
```

**Figure 1 Caption:**  
PRISMA-ScR flow diagram illustrating the identification, screening, and inclusion phases across baseline (460 records) and supplementary academic searches (154 records), achieving exact arithmetic closure across all 614 records ($182\text{ included} + 432\text{ excluded} = 614$). The complete extracted corpus comprises 171 MCP-specific synthesis records and 11 Set B background records. The 22-record E4 benchmark serves as an external, held-out validation set.
