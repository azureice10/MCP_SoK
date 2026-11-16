# Laporan Pembekuan Dataset & Perhitungan Ulang Menyeluruh (MCP_SoK)

**Tanggal Pembekuan:** 14 November 2026 (`FROZEN_RECONCILED_PUBLICATION_READY`)

**Cakupan:** Penyelesaian 106 antrean eksklusi (`P1` = 8, `P2` = 7, `P3` = 91), 4 kasus pertahanan prioritas (`Hierarchical Approaches`, `Attested Policy Brokerage`, `Jalendar/ZPAA`, `Samuel/Astral`), serta penautan versi preprint–publikasi final.

## 1. Manifes Berkas Dataset yang Dibekukan (SHA-256)

| Berkas Dataset Beku | Ukuran (Byte) | Checksum SHA-256 | Deskripsi Perubahan | 
| ----- | ----- | ----- | ----- | 
| `exclusion_code_reconciliation_worksheet.csv` | 58.951 | `461f4c13087a25cfd93043b689f63add07ba74b4ae5eb342a5bd00a209066e96` | Seluruh 106 baris dilengkapi `final_decision`, `final_code`, dan 4 kolom relasi versi preprint–publikasi final (`version_relation_type`, `canonical_corpus_id`, `canonical_published_doi_or_url`, `version_linkage_note`). | 
| `screening_pool_reconciled.json` | 680.225 | `49c7362cbb94922e044a3f161891cb7bd0e1b711e36fc1e8bb7181000b72bf95` | 616 baris (`row-0001` s.d. `row-0614` + `row-0615` & `row-0616` untuk 2 studi pertahanan Supplementary E1) dengan status `frozen_source_verified_2026-11-14`. | 
| `prisma_screening_pool_reconciled_frozen.csv` | 302.108 | `d8accd3b193f97dad2c641fbdb5576aec372647022d2b4a62475350c03ba6968` | Ekspor tabel CSV datar dari pool skrining yang telah direkonsiliasi dan dibekukan. | 
| `mcp_sok_corpus_182_reconciled_frozen.csv` | 64.506 | `eca0791c76153c20143664bd14542681a7a1ec09c057a971726857db9f9b7b1c` | Korpus sintesis spesifik MCP penuh (`N = 182`: 171 asli + 2 Supplementary E1 + 9 rekaman yang dibuka ulang dari `P1`/`P3`). | 
| `mcp_sok_corpus_173_conservative_frozen.csv` | 60.492 | `f3a481f99affa9770aac2b679df2ef737fb70c736022c3dc9da03da771f9e186` | Korpus sintesis konservatif (`N = 173`: 171 asli + 2 Supplementary E1 yang sudah ada di tabel pertahanan 85). | 
| `defenses_89_reconciled_frozen.csv` | 82.510 | `1a3e603089f43fa07d6a969b30ff638ab4aca04446955aec30c3daee28d3373e` | Tabel pertahanan terkonsolidasi penuh (`n = 89`: 85 pertahanan yang direkonsiliasi + 4 pertahanan baru dari `P1`/`P3`). | 
| `defenses_85_reconciled_frozen.csv` | 78.666 | `3db8e624f80276f56a186032b50a343ab08d6aae46c07df61a57d5415e2c2a8f` | Tabel 85 pertahanan asli setelah pembaruan bukti teks lengkap pada 4 kasus pertahanan prioritas. | 

## 2. Tabel Relasi Preprint–Publikasi Final & Deduplikasi (`P2` & `P3`)

| ID Rekaman pada Antrean | Keputusan & Kode | Jenis Relasi Versi (`version_relation_type`) | ID Rekaman Kanonik di Korpus / Set B (`canonical_corpus_id`) | DOI / URL Publikasi Final Kanonik | Catatan Relasi Preprint–Publikasi Final | 
| ----- | ----- | ----- | ----- | ----- | ----- | 
| `brandon-2025-mcp-safety-audit-llms-model` (`P2`) | `Duplicate [DUP]` | `preprint_of_included_e1` | `john-2026-mcp-safety-audit-llms-model` | <https://doi.org/10.1117/12.3097390> | Preprint [`arXiv:2504.03767`](https://arxiv.org/abs/2504.03767) (Radosevich & Halloran, 2025) dari makalah konferensi *SPIE Defense + Security 2026* (Halloran, Radosevich, & Black; Tier `E1`, Grade `L2`). | 
| `narek-2026-breaking-protocol-security-analysis-model` (`P2`) | `Duplicate [DUP]` | `arxiv_mirror_of_included_e1` | `n-2025-breaking-protocol-security-analysis-model` | <https://doi.org/10.25559/sitito.021.202503.420-428> | Salinan [`arXiv:2601.17549`](https://arxiv.org/abs/2601.17549) dari artikel jurnal *SITITO* Vol. 21 No. 3 hlm. 420–428 (Maloyan & Namiot, 2025; Tier `E1`, Grade `L1` *AttestMCP*). | 
| `tiwari-2025-model-context-protocol-vision-systems` (`P2`) | `Duplicate [DUP]` | `author_slug_duplicate_of_included_e2` | `aditi-2025-model-context-protocol-vision-systems` | <https://arxiv.org/abs/2509.22814> | Preprint [`arXiv:2509.22814v1`](https://arxiv.org/abs/2509.22814) yang identik; terindeks ganda akibat format nama keluarga vs. nama depan (`Tiwari, Aditi` vs. `Aditi Tiwari`). | 
| `xiaofan-2025-toward-understanding-security-issues-model` (`P2`) | `Duplicate [DUP]` | `preprint_of_included_e1` | `xiaofan-2025-first-look-security-issues-model` | <https://doi.org/10.1145/3731569.3764844> | Preprint [`arXiv:2510.16558`](https://arxiv.org/abs/2510.16558) (*Toward Understanding...*) dari makalah workshop ACM 2025 (*A First Look...*; Tier `E1`). | 
| `zi-2025-mpma-preference-manipulation-attack-model` (`P2`) | `Duplicate [DUP]` | `preprint_of_included_e1` | `zheng-2026-mpma-preference-manipulation-attack-model` | <https://doi.org/10.1609/aaai.v40i42.40898> | Preprint [`arXiv:2505.11154`](https://arxiv.org/abs/2505.11154) dari makalah konferensi *AAAI 2026* Vol. 40 No. 42 (Tier `E1`). | 
| `zehang-2024-ai-agents-threat-survey-key` (`P2`) | `Duplicate [DUP]` | `cross_pool_duplicate_of_set_b` | `zehang-2024-ai-agents-threat-survey-key` | <https://doi.org/10.48550/arXiv.2406.02630> | Duplikat ID persis lintas-pool (`Baseline row-0443` vs. `Supplementary row-0613`); dipertahankan tunggal di `Background Set B`. | 
| `zhaorun-2024-agentpoison-red-teaming-llm-agents` (`P2`) | `Duplicate [DUP]` | `cross_pool_duplicate_of_set_b` | `zhaorun-2024-agentpoison-red-teaming-llm-agents` | <https://doi.org/10.52202/079017-4136> | Duplikat ID persis lintas-pool (`Baseline row-0459` vs. `Supplementary row-0614`); dipertahankan tunggal di `Background Set B`. | 
| `mengying-2025-mcpzoo-large-scale-dataset-runnable` (`P3`) | `Exclude [EC1]` | `precursor_dataset_of_included_study` | `pei-2026-rethinking-mcp-security-large-scale` | [https://arxiv.org/abs/2607.11086v1](https://www.google.com/search?q=https://arxiv.org/abs/2607.11086v1) | Preprint dataset v1 ([`arXiv:2512.15144`](https://arxiv.org/abs/2512.15144), 9 penulis Fudan Univ., Contoh Terkalibrasi #6 $\rightarrow$ `EC1`); studi keamanan penuhnya (`pei-2026`) sudah `Include` di korpus. | 
| `zhiwei-2025-large-scale-evolvable-dataset-model` (`P3`) | `Exclude [EC1]` | `companion_dataset_of_included_study` | `weibo-2025-when-mcp-servers-attack-taxonomy` | <https://doi.org/10.48550/arXiv.2509.24272> | Makalah dataset `MCPCorpus` ([DOI: `10.1109/ase63991.2025.00356`](https://doi.org/10.1109/ase63991.2025.00356) / [`arXiv:2506.23474`](https://arxiv.org/abs/2506.23474) $\rightarrow$ `EC1`); studi serangan keamanannya (`weibo-2025`) sudah `Include` di korpus. | 
| `narek-2026-prompt-injection-attacks-agentic-coding` (`P3`) | `Include [E1]` | `published_journal_version_available` | `narek-2026-prompt-injection-attacks-agentic-coding` | <https://injoit.org/index.php/j1/article/view/2423> | Preprint [`arXiv:2601.17548`](https://arxiv.org/abs/2601.17548) memiliki publikasi final di *INJOIT 2026*. | 
| `alfredo-2026-enclawed-configurable-sector-neutral-hardening` (`P3`) | `Exclude [EC2]` | `companion_gateway_paper_of_included_study` | `alfredo-2026-attested-tool-server-admission-security` | <https://arxiv.org/abs/2605.24248> | Membahas pengerasan gateway *OpenClaw* (`EC2`); makalah khusus MCP dari penulis yang sama (`alfredo-2026-attested`) sudah `Include` di korpus. | 
| `john-2026-training-free-refusal-mcp-exploits` (`P3`) | `Exclude [EC2]` | `followup_model_layer_paper_of_included_study` | `john-2026-mcp-safety-audit-llms-model` | <https://doi.org/10.1117/12.3097390> | Penyelarasan lapisan model `RAG-Pref` (`EC2` sesuai `Addendum A1b`); makalah audit MCP dari penulis yang sama (`john-2026-mcp-safety-audit`) sudah `Include` di korpus. | 

## 3. Perhitungan Ulang Diagram Alir PRISMA-ScR (Section 2.4, Section 2.6, Figure 1)

Rekonsiliasi menyelaraskan dua anomali struktural pada snapshot lama: (a) 7 rekaman `P2` yang sebelumnya diberi kode `IC2` dikembalikan ke status sebenarnya sebagai duplikat versi/lintas-pool (`DUP`), dan (b) 2 studi pertahanan *Supplementary* (`hierarchical-approaches-for-2026` dan `attested-policy-brokerage-2026`) yang sudah ada di [`supplementary_pool_213_raw.csv`](https://drive.google.com/file/d/1mrEJib2nsShdUddRvqC6monHjHOsTVk_/view?usp=drivesdk) dan [`defenses_85_consolidated.csv`](https://drive.google.com/file/d/1bOFmU2tdZniglmt53hRrXqbHWEMc7-hN/view?usp=drivesdk) dipulihkan ke pool skrining menggantikan 2 baris duplikat lintas-pool `Set B` (`zehang-2024` dan `zhaorun-2024` yang memang berasal dari *Baseline Pool*).

| Tahap / Metrik PRISMA-ScR | Angka Naskah Lama (Snapshot Kuota) | Skema A: Reconciled Penuh (Dengan 9 Inklusi Baru `P1/P3` + 2 Supp E1) | Skema B: Konservatif (Tanpa Menambah 9 Inklusi Baru `P1/P3`, Hanya Koreksi Kode & 2 Supp E1) | 
| ----- | ----- | ----- | ----- | 
| **Identifikasi Baseline Mentah** (arXiv 200, OpenAlex 200, S2 95) | 495 | 495 | 495 | 
| **Baseline Pasca-Deduplikasi Awal** $\to$ **Pasca-Rekonsiliasi Versi (`-7 DUP`)** | 460 | **460 baris (`453` studi unik setelah `-7 DUP` versi/lintas-pool)** | **460 baris (`453` studi unik setelah `-7 DUP` versi/lintas-pool)** | 
| **Identifikasi Supplementary Mentah** (IEEE 112, Scopus 172, ACM 13) | 297 $\to$ 213 unik | 297 $\to$ 213 unik | 297 $\to$ 213 unik | 
| **Supplementary Bersih** (setelah irisannya dengan Baseline dihapus) | 154 | **156 baris unik** (`154` awal + `2` studi pertahanan E1 dipulihkan) | **156 baris unik** (`154` awal + `2` studi pertahanan E1 dipulihkan) | 
| **Total Baris Pool Skrining** (`Baseline + Supplementary`) | 614 baris (612 ID unik) | **616 baris total / `609` studi unik** (setelah `-7 DUP`) | **616 baris total / `609` studi unik** (setelah `-7 DUP`) | 
| **Total Rekaman Diekstraksi (`Included`)** | **182** (`171` Korpus + `11` Set B) | **193** (**`182` Korpus Spesifik MCP** + **`11` Set B**) | **184** (**`173` Korpus Spesifik MCP** + **`11` Set B**) | 
| — *Dari Baseline Pool* | 157 (`148` Korpus + `9` Set B) | **166** (`157` Korpus \[`148 + 9`\] + `9` Set B; `+7 DUP` di Baseline) | **157** (`148` Korpus + `9` Set B; `+7 DUP` di Baseline) | 
| — *Dari Supplementary Pool* | 25 (`23` Korpus + `2` Set B) | **27** (`25` Korpus Tier E1 \[`23 + 2`\] + `2` Set B; `0 DUP`) | **27** (`25` Korpus Tier E1 \[`23 + 2`\] + `2` Set B; `0 DUP`) | 
| **Total Rekaman Dikeluarkan (`Excluded` Unik, di luar `7 DUP`)** | **432** (termasuk `7 DUP` di dalam `IC2`) | **416 studi unik** (`+ 7 DUP = 423` baris non-inklusi) | **425 studi unik** (`+ 7 DUP = 432` baris non-inklusi) | 
| — **`IC2`** (*Tidak membahas keamanan MCP / di luar topik*) | 164 (kuota) | **148** (`143` non-ws + `5` ws) | **148** (`143` non-ws + `5` ws) | 
| — **`EC1`** (*MCP hanya dipakai sebagai infrastruktur non-keamanan*) | 125 (kuota) | **124** (`30` Base non-ws + `47` Base ws + `47` Supp) | **125** (jika `shaswata-2026` tetap `EC1`) atau **124** | 
| — **`EC2`** (*Keamanan LLM/agen umum tanpa analisis spesifik MCP*) | 56 (kuota) | **55** (`23` Base non-ws + `31` Base ws + `1` Supp) | **63** (jika 8 kandidat `P1/P3` tetap `EC2`) | 
| — **`EC3`** (*Opini / tinjauan umum tanpa bukti teknis*) | 5 | **5** (`5` Base ws) | **5** (`5` Base ws) | 
| — **`EC4`** (*Teks lengkap tidak dapat diakses*) | 0 | **0** (seluruh 4 sumber yang sempat tertunda berhasil dipulihkan) | **0** | 
| — **`EC5`** (*Benturan akronim "MCP" untuk konsep lain*) | 82 | **84** (`1` Base non-ws + `2` Base ws \[`vasanthrao-2026`, `pintu-2025`\] + `81` Supp) | **84** (`3` Base + `81` Supp) | 
| — **`DUP`** (*Duplikat versi preprint/arXiv atau lintas-pool*) | 0 (tersembunyi di `IC2`) | **7** (`5` preprint/slug korpus + `2` duplikat lintas-pool `Set B`) | **7** (`5` preprint/slug korpus + `2` duplikat lintas-pool `Set B`) | 

## 4. Perhitungan Ulang Distribusi Korpus (Section 4.3, Section 9.1, Supplementary Table S7)

| Dimensi / Kategori Korpus | Korpus Naskah Lama (`N = 171`) | Skema A: Korpus Reconciled Penuh (`N = 182`) | Skema B: Korpus Konservatif (`N = 173`) | 
| ----- | ----- | ----- | ----- | 
| **Layer A: Semantic Channel (`A1–A3`)** | 91 (53,2%) | **93 (51,1%)** | **91 (52,6%)** | 
| **Layer C: Identity, Authorization, & Sinks (`C1–C7`)** | 70 (40,9%) | **77 (42,3%)** | **72 (41,6%)** | 
| **Layer D: Cross-Server Composition (`D1–D3`)** | 8 (4,7%) | **9 (4,9%)** | **8 (4,6%)** | 
| **Layer B: Descriptor Integrity Over Time (`B1–B3`)** | 2 (1,2%) | **3 (1,6%)** | **2 (1,2%)** | 
| **Peran: `defense_primary`** | 67 (39,2%) | **68 (37,4%)** | **66 (38,2%)** | 
| **Peran: `defense_secondary`** | 6 (3,5%) | **7 (3,8%)** | **7 (4,0%)** | 
| **Peran: `proposal_only` (`L0` Konseptual)** | 10 (5,8%) | **14 (7,7%)** | **12 (6,9%)** | 
| **Subtotal Rekaman Pertahanan di Korpus** | 83 (kurang 2 dari 85) | **89 (48,9% dari 182 — 100% sinkron)** | **85 (49,1% dari 173 — 100% sinkron)** | 
| **Peran: `benchmark_measurement`** | 32 (18,7%) | **32 (17,6%)** | **32 (18,5%)** | 
| **Peran: `attack`** | 25 (14,6%) | **28 (15,4%)** (`+ seo-2026`, `xinpeng-2025`, `hyomin-2026`) | **25 (14,5%)** | 
| **Peran: `survey_review`** | 21 (12,3%) | **23 (12,6%)** (`+ mohammadreza-2026`, `narek-2026-prompt`) | **21 (12,1%)** | 
| **Peran: `position_other` & `not_defense`** | 7 + 3 = 10 (5,8%) | **7 + 3 = 10 (5,5%)** | **7 + 3 = 10 (5,8%)** | 
| **Evidence Tier `E1` (Peer-Reviewed)** | 65 (38,0%) | **71 (39,0%)** (`+ samuel-2026`, `hierarchical`, `attested`, `shanshan`, `seo`, `narek`) | **68 (39,3%)** (`+ samuel-2026`, `hierarchical`, `attested`) | 
| **Evidence Tier `E2` (Preprint)** | 101 (59,1%) | **106 (58,2%)** | **100 (57,8%)** | 
| **Evidence Tier `E3` & `E4`** | 1 (0,6%) & 4 (2,3%) | **1 (0,5%) & 4 (2,2%)** | **1 (0,6%) & 4 (2,3%)** | 

## 5. Perhitungan Ulang Distribusi Pertahanan (Section 6.1–6.3 & Supplementary Section S5)

Pemulihan teks lengkap untuk empat kasus prioritas menyelesaikan seluruh konflik antarsheet:

1. **`hierarchical-approaches-for-2026`** ([DOI: `10.1109/ACCESS.2026.3694881`](https://doi.org/10.1109/ACCESS.2026.3694881)): Unit yang dinilai ditetapkan pada **`MCP Firewall Plug-in`** (`defense_secondary`, paradigma `content_inspection_runtime`, titik penegakan `H`, **Grade `L1`** \[naik dari `L0`\], `classes_evaluated = A2;C5;OUT_OF_TAXONOMY:dns_poisoning`).

2. **`attested-policy-brokerage-2026`** ([DOI: `10.1109/CIACON70148.2026.11688532`](https://doi.org/10.1109/CIACON70148.2026.11688532)): Teks lengkap (`Section IV–V`, `Table II`) membuktikan pengujian ketahanan terhadap 5 vektor serangan (`T1–T5`) $\rightarrow$ `defense_primary`, paradigma `capability_or_token`, titik penegakan `gateway_proxy`, **Grade `L1`** (naik dari `L0`), `classes_evaluated = C1;C2;C3;C5`.

3. **`jalendar-2025-zero-trust-proof-gated-agent`** ([DOI: `10.22541/au.175761889.90929465/v1`](https://doi.org/10.22541/au.175761889.90929465/v1)): Teks lengkap (5 hlm.) memastikan makalah murni konseptual dengan target anggaran latensi `<10 ms` $\rightarrow$ `fulltext_available = Yes`, **Grade `L0`** dikonfirmasi, dan `evaluated = C1;C3` yang tersisa di `mcp_sok_corpus_171.csv` dikosongkan.

4. **`samuel-2026-secure-sandbox-environment-orchestrating-medical`** (*AMIA 2026*, `PMC13274365`): Teks lengkap (10 hlm.) memastikan publikasi prosiding peer-reviewed (**Tier `E1`**, naik dari `E2`), `fulltext_available = Yes`, menguji 10 *user story* fungsional dan *overhead* tanpa suite serangan adversarial $\rightarrow$ **Grade `L0`** untuk mitigasi serangan dikonfirmasi, dan `evaluated = A2;C3;D1` yang tersisa di `mcp_sok_corpus_171.csv` dikosongkan.

| Metrik Analisis Pertahanan (Section 6) | Naskah Lama (Amendemen A1, `n = 85`) | Skema B: Reconciled 85 Pertahanan (`n = 85`) | Skema A: Reconciled Penuh 89 Pertahanan (`n = 89`) | 
| ----- | ----- | ----- | ----- | 
| **`L0` — Proposal Konseptual (Tanpa Evaluasi Serangan)** | 17 (20,0%) | **15 (17,6%)** | **17 (19,1%)** (`+ edoardo-2025`, `shaswata-2026`) | 
| **`L1` — Prototipe Dievaluasi Penulis Sendiri** | 66 (77,6%) | **68 (80,0%)** (`+ hierarchical`, `attested`) | **70 (78,7%)** (`+ shanshan-2026`, `haiyue-2026`) | 
| **`L2` — Evaluasi Independen (`MCIP`, `McpSafetyScanner`)** | 2 (2,4%) | **2 (2,4%)** | **2 (2,2%)** | 
| **`L3` — Kontrol Terdeploy Terverifikasi Pihak Ketiga** | 0 (0,0%) | **0 (0,0%)** | **0 (0,0%)** | 
| **Total Pertahanan yang Dievaluasi Secara Empiris (`L1 + L2`)** | 68 (80,0%) | **70 (82,4%)** | **72 (80,9%)** | 
| **Keluarga Mekanisme 1: Otorisasi atau Kebijakan (*Authorization / Policy*)** | 37 (43,5%) | **36 (42,4%)** | **39 (43,8%)** (`27 deterministic_policy, 6 capability_or_token, 6 protocol_provision`) | 
| **Keluarga Mekanisme 2: Inspeksi Konten (*Content Inspection*)** | 35 (41,2%) | **36 (42,4%)** (`+ MCP Firewall Plug-in`) | **37 (41,6%)** (`23 runtime, 14 static`) | 
| **Keluarga Mekanisme 3: Integritas atau Isolasi (*Integrity / Isolation*)** | 13 (15,3%) | **13 (15,3%)** | **13 (14,6%)** (`8 integrity_provenance, 4 isolation_containment, 1 cryptographic_integrity`) | 
| **Pertahanan Struktural (Otorisasi/Kebijakan + Integritas/Isolasi)** | 50 (16 berstatus `L0`) | **49 (14 berstatus `L0`)** | **52 (16 berstatus `L0`)** | 
| **Melibatkan LLM / ML di Dalam Loop Keputusan** | 25 dari 85 (29,4%) | **25 dari 85 (29,4%)** | **25 dari 89 (28,1%)** | 
| **Evaluasi Adaptif di Antara Pertahanan yang Dievaluasi** | 3 dari 68 (4,4%; CI: 1,5%–12,2%) | **3 dari 70 (4,3%; CI: 1,5%–11,9%)** | **3 dari 72 (4,2%; CI: 1,4%–11,5%)** | 
| **Titik Penegakan (*Enforcement Points*)** | `gateway_proxy`: 54, `offline`: 10, `H`: 9, `C`: 5, `registry`: 3, `S`: 3, `G`: 1 | `gateway_proxy`: 53, `offline`: 10, `H`: 10, `C`: 5, `registry`: 3, `S`: 3, `G`: 1 | `gateway_proxy`: 54, `H`: 12, `offline`: 11, `C`: 5, `registry`: 3, `S`: 3, `G`: 1 | 

## 6. Perhitungan Ulang Tabel Cakupan Kelas Serangan (Table 14 & Table 16)

Setelah membersihkan kode evaluasi residual pada `jalendar-2025` dan `samuel-2026` di CSV korpus serta memasukkan hasil evaluasi teks lengkap dari `hierarchical-approaches-for-2026` (`A2;C5;OUT_OF_TAXONOMY:dns_poisoning`), `attested-policy-brokerage-2026` (`C1;C2;C3;C5`), `shanshan-2026` (`A2;C5;OUT_OF_TAXONOMY:resource_abuse`), dan `haiyue-2026` (`A1;B1;B2`), **selisih antara CSV korpus dan CSV pertahanan kini menjadi `0` pada seluruh kelas**:

| Kelas Serangan (Table 10 & Table 14) | Batas Kepercayaan (*Boundary*) | Naskah Lama (Tidak Sinkron dgn CSV Pertahanan) | CSV Pertahanan Lama (`defenses_85` Pra-Rekonsiliasi) | **Skema B: Reconciled 85 Pertahanan (`n = 85`, Sinkron 100%)** | **Skema A: Reconciled Penuh 89 Pertahanan (`n = 89`, Sinkron 100%)** | Maturitas Tertinggi & Evaluasi Adaptif | 
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| **A1.** *Tool metadata poisoning* | $S_i \to L$ | 22 | 22 | **22** (Diklaim: 35) | **23** (Diklaim: 36; `+ haiyue-2026`) | `L2` (Adaptif: 2) | 
| **A2.** *Indirect injection via tool results/resources* | $S_i \to L$ | 31 | 30 | **31** (Diklaim: 37; `+ hierarchical`) | **32** (Diklaim: 39; `+ shanshan-2026`) | `L2` (Adaptif: 1) | 
| **A3.** *Description-quality-exploiting miscalls* | $S_i \to L$ | 6 | 6 | **6** (Diklaim: 14) | **6** (Diklaim: 14) | `L1` (Adaptif: 0) | 
| **B1.** *Rug pull / post-approval mutation* | *descriptor over time* | 11 | 11 | **11** (Diklaim: 23) | **12** (Diklaim: 24; `+ haiyue-2026`) | `L1` (Adaptif: 0) | 
| **B2.** *Registry/capability drift at scale* | *descriptor over time* | 6 | 6 | **6** (Diklaim: 16) | **7** (Diklaim: 17; `+ haiyue-2026`) | `L1` (Adaptif: 0) | 
| **B3.** *Schema-mutation robustness failure* | *descriptor over time* | 2 | 2 | **2** (Diklaim: 4) | **2** (Diklaim: 4) | `L1` (Adaptif: 0) | 
| **C1.** *Confused deputy* | $L \to S_i$ | 17 | 16 | **17** (Diklaim: 26; `+ attested`) | **17** (Diklaim: 29) | `L1` (Adaptif: 1) | 
| **C2.** *Caller identity confusion* | $L \to S_i$ | 7 | 7 | **8** (Diklaim: 11; `+ attested`) | **8** (Diklaim: 13) | `L1` (Adaptif: 0) | 
| **C3.** *Missing or flawed transport authorization* | $C \leftrightarrow \Theta, S_i \leftrightarrow \Theta$ | 15 | 13 | **14** (Diklaim: 28; `+ attested`) | **14** (Diklaim: 29) | `L1` (Adaptif: 1) | 
| **C4.** *Intent inversion via tool-call traces* | $L \to S_i$ | **0** | **0** | **0** (Diklaim: 0) | **0** (Diklaim: 0) | `none` (Adaptif: 0) | 
| **C5.** *Sink-side enforcement failure* | $S_i \to X_i$ | 26 | 26 | **28** (Diklaim: 31; `+ hierarchical, attested`) | **29** (Diklaim: 34; `+ shanshan-2026`) | `L2` (Adaptif: 0) | 
| **C6.** *Client-side sink enforcement failure* | $S_i / \Theta \to C$ | n.c. | n.c. | **n.c.** | **n.c.** | `n.c.` | 
| **C7.** *Authorization scoping & tenant isolation* | $S_i \to X_i$ | n.c. | n.c. | **n.c.** | **n.c.** | `n.c.` | 
| **D1.** *Parasitic toolchain / composed exfiltration* | *composition* | 21 | 20 | **20** (Diklaim: 27; `- samuel-2026`) | **20** (Diklaim: 29) | `L2` (Adaptif: 0) | 
| **D2.** *Guardrail bypass under multi-step execution* | *composition* | 7 | 7 | **7** (Diklaim: 9) | **7** (Diklaim: 9) | `L1` (Adaptif: 0) | 
| **D3.** *Supply-chain propagation via tool cloning* | *pre-session* | 9 | 9 | **9** (Diklaim: 21) | **9** (Diklaim: 21) | `L1` (Adaptif: 0) | 
| *Resource abuse (outside the taxonomy)* | *agent / server compute* | 7 | 7 | **7** (Diklaim: 7) | **8** (Diklaim: 8; `+ shanshan-2026`) | `L1` (Adaptif: 0) | 
| *DNS poisoning (outside the taxonomy)* | *network resolution* | — | — | **1** (`hierarchical-approaches`) | **1** (`hierarchical-approaches`) | `L1` (Adaptif: 0) | 

## 7. Addendum Koreksi Pasca Cross-Check Teks Lengkap (14 November 2026)

Cross-check klaim naskah terhadap teks lengkap makalah korpus (`MCP SoK Papers`) menghasilkan koreksi berikut. Tabel di bagian 1–6 di atas dipertahankan sebagai catatan historis pembekuan awal; nilai yang berlaku adalah nilai pada addendum ini.

1. **`agentic-security-validation-2026` (ARGUS, `S-Def-79`):** `adaptive_evaluation` dan `adaptive_adversary_raw` diubah dari `Yes` menjadi `No`. ARGUS adalah pemindai red-team ofensif; sifat "adaptif" merujuk ke generator serangannya sendiri, bukan ke serangan yang dirancang terhadap ARGUS. Evaluasi adaptif kini **2 dari 72** (2,8%; Wilson 95% CI 0,8%–9,6%) dan **2 dari 70** konservatif (2,9%; CI 0,8%–9,8%): MindGuard dan Delegation Broker. Kolom adaptif Tabel 14: A1 = 1, A2 = 0, C1 = 1, C3 = 1.
2. **Atribusi sitasi di naskah:** angka 2.846/6.137 dialihkan dari Li et al. [30] ke Y. Huang et al. (`S-Preprint-05`); angka drift registri dari Mas et al. [34] ke Bharti (`S-Preprint-07`); operator mutasi dari [34] ke MCPEvol-Bench (`S-Preprint-08`); tool cloning dari Gentyala et al. [37] ke T. Kim et al. (`S-Preprint-11`); guardrail bypass dari Polat et al. [57] ke C. Zhang et al. (`S-Preprint-10`); MCPSecBench dari Guo et al. [9] ke Yang et al. (`S-Preprint-02`); FPR/FNR McpSafetyScanner dari Abadeh et al. [49] ke VIPER-MCP (`S-Preprint-12`).
3. **Bukti kelas A3:** Liu et al. [33] adalah benchmark *tool description poisoning* (dipindah ke A1). Studi *description smell* P. Wang et al. menganalisis 10.831 server (bukan 1.180).
4. **Set validasi E4:** X. He et al. [41] mengkurasi 24 CVE MCP tervalidasi; hanya 5 yang beririsan dengan 20 CVE set E4. Keterbatasan ini dan usulan uji held-out pada 19 CVE sisanya ditambahkan ke Sec. 2.10, 8.3, dan 9.3.
5. **Tautan `S-Preprint`:** enam `Canonical Corpus ID` dikoreksi agar cocok dengan `record_id` korpus (`yixuan-2025`, `peiran-2026`, `gautam-2026`, `chenkai-2026`, `taein-2026`, `yulin-2026`).

| Berkas | Ukuran (Byte) | Checksum SHA-256 baru |
| ----- | ----- | ----- |
| `defenses_89_reconciled_frozen.csv` | 82.693 | `cde6591e9005cba7e3bf15d9fb903495e2255f769ed28244432ef273cf578634` |
| `defenses_85_reconciled_frozen.csv` | 78.849 | `21ad04c2d0effdd725c654fad41b9593b73cb3d4a1c9e4cdd914d54aa643b733` |
| `dataset_s4_frozen_defenses_89.csv` | 33.743 | `441c062290cd7b6d0b2e96ecfc39bf693d7cb5c83827ef15d8435a442922f90f` |
6. **Jang & Lee [19] (`S-Def-84`):** rentang halaman dikoreksi dari 58110–58126 menjadi **77148–77164** (Crossref; naskah, `dataset_s3_frozen_corpus_182.csv`, dan Supplementary Dataset). Deskripsi empat strategi di naskah dan S5 diselaraskan dengan teks lengkap (*MCP-Specific Defense*, *LLM Inherent Defense*, *Cyber Security Inherent*, *MCP Firewall*). Klaim "uneven protection across host orchestration, transport, and supply chain" di Sec. 6.5 dialihkan ke sumbernya, Rostamzadeh et al. (`S-Preprint-03`). Kode `classes_evaluated` (A2;C5;DNS) belum diubah dan menunggu keputusan coder, karena eksperimen hanya menguji DNS poisoning.
7. **Metadata referensi (dicek ke Crossref):** halaman [11] 341–356 → 494–517, [16] 512–525 → 474–483, [30] 1–9 → 555–560, [60] 1845–1860 → 5165–5180; volume [18] 99 → 103 (juga di Supplementary Dataset dan `dataset_s3_frozen_corpus_182.csv`); [2] dan [31] kini TOSEM vol. 35(10) dan 35(11), [9] TDSC vol. 23(5); halaman ditambahkan untuk [32], [33], [37], [41], [47], [49], [52], [53], [58], dan [59]. Teks lengkap Tamayo [16] dan Nandish [20] (folder `springer`) mengonfirmasi angka 73 studi / 93,2% / 23,3% dan 18 studi / empat defisit MIRT.
8. **Eksklusi IC3 (14 November 2026):** `survey-model-context-2026` (*Chinese Journal on Internet of Things*) dan `empirical-study-privilege-2026` (*Journal of Computer Research and Development*) dieksklusi dengan kode **IC3** karena teks utamanya tidak berbahasa Inggris (hanya judul dan abstrak yang berbahasa Inggris). Keduanya berasal dari pool Supplementary (`S-Corpus-072` dan `S-Corpus-085`; ID dipensiunkan, tidak dipakai ulang) dan bukan rekaman defense, sehingga matriks defense (89 dan 85) tidak berubah. Angka yang berlaku: korpus **180** (konservatif **171**), diekstraksi **191** (**182**), eksklusi unik **418** (**427**) dengan IC3 = 2, Tier E1 **69** (**66**), layer A/B/C/D **91 / 3 / 77 / 9** (**89 / 2 / 72 / 8**), dan Supplementary memuat **23** studi korpus. Berkas korpus diganti namanya (`..._182_...` menjadi `..._180_...`, `..._173_...` menjadi `..._171_...`); `rohit-2024` dan `upendra-2026` dipertahankan. Figure 1 dirender ulang.

| Berkas (nama baru) | Ukuran (Byte) | Checksum SHA-256 baru |
| ----- | ----- | ----- |
| `mcp_sok_corpus_180_reconciled_frozen.csv` | 63977 | `c66be30c28c4a63e677e2a8195334b8049be4bcf2def0a3891adf52b5e5ccd40` |
| `mcp_sok_corpus_171_conservative_frozen.csv` | 59963 | `9bc91d70e76b42c466478d30735355456ff026382aca960355f8a2c5d2a9c0ac` |
| `dataset_s3_frozen_corpus_180.csv` | 70590 | `32bd50191595013c452a85612a3982dfaf9f9fc2244f4c2d18015930e54dc5ef` |
| `prisma_screening_pool_reconciled_frozen.csv` | 302424 | `4209b35b03909fd8687d16020dcbbdffb75b0465e75dd19289ca0fd87d5cbb88` |
| `screening_pool_reconciled.json` | 680537 | `ba072a9070c6d59ab003ca3caf26b88a4a980955c28a6557df16b41fd0dc9a04` |
9. **Bhosle [59] / Attested Policy Brokerage (`S-Def-85`), cek ke PDF IEEE (14 November 2026):** klaim "100% block rate pada 120 percobaan adversarial", "4,8 ms fast-path", token "JWS", dan tingkat breach T1-T5 di catatan data **tidak ada** di makalah (Tabel II adalah pemetaan kualitatif cakupan ancaman; tabel latensi adalah Tabel IV). Bukti yang ada: mikrobenchmark PoC satu host, profil latensi terdistribusi (p95 1,54-6,89 ms pada 50-500k req/s), dan satu replay jejak serangan bergaya CVE-2025-68144. Pengodean: tetap `defense_primary`, L1, `author_run`; `classes_evaluated` diubah dari `C1;C2;C3;C5` menjadi **`C5`** (`classes_claimed` tetap). Dampak Tabel 14 (Skema A dan B): C1 17 menjadi **16**, C2 8 menjadi **7**, C3 14 menjadi **13**; kolom klaim, C5, L0/L1/L2, dan evaluasi adaptif tidak berubah. `verify_defense_maturity.py` kini memeriksa seluruh hitungan Tabel 14 terhadap CSV.

| Berkas | Ukuran (Byte) | Checksum SHA-256 baru |
| ----- | ----- | ----- |
| `defenses_89_reconciled_frozen.csv` | 83136 | `7e46171b9625954d1b6e416ee58c57f79f079ae9d9dcefd658a6e8241fa45e70` |
| `defenses_85_reconciled_frozen.csv` | 79292 | `efc6101cbc6c3d298b0feaef9242a7ddd8bc8636b0a179b523b75539536b140c` |
| `dataset_s4_frozen_defenses_89.csv` | 33734 | `1f09ef0137ac229badb2c25b95a3798434349bdb69c998cd7e2cf168f244858f` |
| `mcp_sok_corpus_180_reconciled_frozen.csv` | 63969 | `f20d802dc1b417f20f0ee6ab338d1d5f0af399f1783a4a7905b5e0bfa5a2922c` |
| `mcp_sok_corpus_171_conservative_frozen.csv` | 59955 | `b5b8e96f7bc6e6eed2b9efc08a6e5d8aa78e744aae27117a88899fac86f2383d` |
| `dataset_s3_frozen_corpus_180.csv` | 70581 | `84baa0b4b0fc066e43a83be55ea13b6472eaad7c80d8ce7bf49b6aa82777abb3` |
10. **Eksklusi IC2 `genreachai-agentic-generative-2026` (14 November 2026):** setelah PDF IEEE (ISDFS 2026) dibaca, makalah ini terbukti alat analisis *reachability* kerentanan perangkat lunak (SCA; Log4Shell, React2Shell; 500 layanan mikro) yang memakai MCP hanya sebagai konektor data; kelas D3 yang dikodekan tidak ada di makalah dan klaimnya bertahan bila MCP diganti konektor generik (gagal uji substitusi). Rekaman dieksklusi dengan kode **IC2** dari pool Supplementary; `S-Corpus-088` dan `S-Def-78` dipensiunkan. Angka yang berlaku: korpus **179** (konservatif **170**), diekstraksi **190** (**181**), eksklusi unik **419** (**428**) dengan IC2 = 149; defense **88** (**84**), L0/L1/L2 = **17 / 69 / 2** (**15 / 67 / 2**), dievaluasi **71** (**69**), adaptif **2/71** (**2/69**), keluarga kebijakan/konten/integritas **39 / 36 / 13** (**36 / 35 / 13**), LLM di loop **24**, Tabel 14 D3 **8 (20)**. Berkas diganti nama: korpus `..._179_...` dan `..._170_...`, `dataset_s3_frozen_corpus_179.csv`, `defenses_88_...`, `defenses_84_...`, `dataset_s4_frozen_defenses_88.csv`. Figure 1 dirender ulang.

| Berkas (nama baru) | Ukuran (Byte) | Checksum SHA-256 baru |
| ----- | ----- | ----- |
| `mcp_sok_corpus_179_reconciled_frozen.csv` | 63511 | `9a624139f8d96cd6d0828c94eaf044f2baf73621ea54c0675c4dadbba9076917` |
| `mcp_sok_corpus_170_conservative_frozen.csv` | 59497 | `b5a4c6ff56f90bc9d389874a85851cfd45f0265637857695ef26c4f7d905abce` |
| `dataset_s3_frozen_corpus_179.csv` | 70141 | `4e92d4f46da147eeb52fce755d0543f2a73c15fd3acd12b32d3dcaa1f5f61de0` |
| `defenses_88_reconciled_frozen.csv` | 82287 | `270d51b808673f48bdc9fa11ab8f44a32d92a143ce14d408df49076b2ece1a2b` |
| `defenses_84_reconciled_frozen.csv` | 78443 | `cbdfeda03b9545c8bd7f605a187be054ac01f083560e31e1ebdc869c0a990eac` |
| `dataset_s4_frozen_defenses_88.csv` | 33366 | `78bf2cbf452c0eccd0bdc4a0b162ce5644eb1285f64a67884610808b3c6fd672` |
| `prisma_screening_pool_reconciled_frozen.csv` | 302638 | `19b7c1371801f950afdeffb2f0903bc7a9656c6f0752c1d59668568e269790c8` |
| `screening_pool_reconciled.json` | 680749 | `7d91437e946d3bce8b00be0af76e9ba86b9e1a32d5efab207977e23d11e45a68` |
