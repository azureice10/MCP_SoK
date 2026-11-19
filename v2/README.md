# MCP SoK v2 replication data

This package supports the November 2026 update of the MCP security systematization of knowledge. The literature search closed on 16 November 2026. The advisory window covers 26 September through 16 November 2026, inclusive.

| File | Contents |
| --- | --- |
| [Corpus](data/dataset_s3_corpus_215_v2.csv) | 215 MCP-specific studies, including 199 in the conservative sensitivity set. |
| [Defense studies](data/dataset_s4_defenses_112_v2.csv) | 112 study records, including 102 in the conservative set. The `record_id` joins each defense to the corpus. |
| [Advisory screening](data/dataset_temporal_E4_256.csv) | 256 screened public advisory records, including 216 eligible and 40 excluded. |

For the conservative sets, select `Yes` in the corresponding legacy flag (`in_conservative_170` or `in_conservative_84`). Fields listing multiple attack classes use semicolon delimiters. The historical [v1 replication package](../README.md) contains the background set and earlier screening and coding documentation.

In the temporal coverage analysis, 136 eligible advisories fit a class as defined (`Yes`), 53 required a proposed extension (`Partial`), and 27 remained unclassified (`No`). The taxonomy was finalized after some advisories had appeared. Seven records with insufficient public detail (G6) were excluded in the primary analysis. Treating these seven as eligible gives a sensitivity range of 189/223 to 196/223 (84.8%–87.9%) for mappings including extensions.

Defense maturity grades are L0 (conceptual), L1 (author evaluation), L2 (independent evaluation), and L3 (documented deployment). The counts are 20, 90, 2, and 0. Six of the 92 evaluated defenses were flagged as adaptive at the study level.

## Verify the package

From the repository root, run `python3 v2/verify.py`. The script verifies the three CSV hashes, study joins, counts, advisory dates, and cluster-level coverage using the Python standard library.
