# Laporan Finalisasi Lembar Koding Koder 2 Blind & Analisis Kesepakatan Antar-Koder (Inter-Coder Agreement)

**Dokumen Acuan:** `Addendum_A1_Pedoman_Skrining_v3.2.md` & `Pedoman_Pengisian_Lembar_Koding_v1.1.md`  
**Berkas Sumber:**
- Koder 1 (Master Korpus 186): `Lembar_Koding_Pertahanan_v1_1_Sesi2_Recall.xlsx`
- Koder 2 (Blind Sample 38): `Lembar_Koding_KODER2_BLIND.xlsx`  
**Waktu Eksekusi Final:** September 2026  
**Status Audit Formula:** **100% Bersih (38/38 baris terisi, 0 PERIKSA / 0 Error)**

---

## 1. Ringkasan Eksekutif & Status Pengisian

Pengisian lembar koding blind oleh Koder 2 dilakukan secara independen terhadap **38 makalah sampel representatif** yang ditarik dari korpus final 186 makalah. Proses pengisian dilakukan secara bertahap dalam 4 batch terverifikasi:
- **Batch 1 (Baris 2–11, 10 baris):** `saeid-2025` s.d. `pei-2026` — Selesai & Terverifikasi
- **Batch 2 (Baris 12–21, 10 baris):** `zhiqiang-2025` s.d. `herman-2025` — Selesai & Terverifikasi
- **Batch 3 (Baris 22–30, 9 baris):** `nicola-2025` s.d. `shiqiang-2025` — Selesai & Terverifikasi
- **Batch 4 (Baris 31–39, 9 baris):** `ping-2026` s.d. `murali-2026` — Selesai & Terverifikasi

Seluruh aturan validasi logika (formula `cek_konsistensi` pada kolom 25) terpenuhi 100% tanpa inkonsistensi (`0 PERIKSA`).

---

## 2. Distribusi Peran Koder 2 Blind

| Peran Granular | Jumlah | Persentase | Klasifikasi Biner |
| :--- | :---: | :---: | :--- |
| `defense_primary` | 10 | 26.32% | **Pertahanan (21 makalah / 55.26%)** |
| `defense_secondary` | 4 | 10.53% | |
| `proposal_only` | 7 | 18.42% | |
| `benchmark_measurement` | 5 | 13.16% | **Non-Pertahanan (17 makalah / 44.74%)** |
| `survey_review` | 5 | 13.16% | |
| `attack` | 5 | 13.16% | |
| `position_other` | 1 | 2.63% | |
| `not_defense` | 1 | 2.63% | |
| **Total Sampel** | **38** | **100.0%** | **38 Makalah** |

---

## 3. Hasil Uji Statistik Kesepakatan Antar-Koder (Inter-Coder Agreement)

### A. Klasifikasi Peran Makalah ($N = 38$)

| Dimensi Pengujian | Kesepakatan Teramati (*Observed*) | Cohen's Kappa ($\kappa$) | Tingkat Kesepakatan (*Interpretation*) |
| :--- | :---: | :---: | :--- |
| **Peran Biner** (*Defense* vs *Non-Defense*) | **100.00%** (38/38) | **1.0000** | **Perfect Agreement** |
| **Peran Granular** (8 Kategori) | **92.11%** (35/38) | **0.9044** | **Almost Perfect Agreement** ($\kappa \ge 0.81$) |

### B. Dimensi Teknis Pertahanan yang Disepakati Bersama ($N = 21$)

| Dimensi Koding | Variabel | Kesepakatan Teramati | Cohen's Kappa ($\kappa$) | Kategori Kesepakatan (Landis & Koch, 1977) |
| :--- | :--- | :---: | :---: | :--- |
| **Tingkat Kematangan** | `maturitas (otomatis)` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |
| **Adaptivitas Serangan** | `adaptif` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |
| **Jenis Evaluasi** | `jenis_evaluasi` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |
| **LLM dalam Keputusan** | `llm_dlm_keputusan` | **95.24%** (20/21) | **0.9261** | **Almost Perfect Agreement** |
| **Status Deployment** | `deployment` | **90.48%** (19/21) | **0.8409** | **Almost Perfect Agreement** |
| **Asal Set Serangan** | `asal_set_serangan` | **85.71%** (18/21) | **0.7812** | **Substantial Agreement** |
| **Titik Penegakan** | `titik_penegakan` | **80.95%** (17/21) | **0.6441** | **Substantial Agreement** |
| **Paradigma Pertahanan** | `paradigma` | **71.43%** (15/21) | **0.6348** | **Substantial Agreement** |
| **Biaya Utilitas (Presensi)**| `biaya_utilitas` | **100.00%** (21/21) | **1.0000** | **Perfect Agreement** |

### C. Kesamaan Himpunan Multi-Label (*Mean Jaccard Similarity*, $N = 21$)

- **Boundary Crossings (`crossings`, R1–R7):** **0.6786** (*Substantial Overlap*)
- **Kelas Serangan Diklaim (`kelas_diklaim`, A1–D3):** **0.5825** (*Moderate-to-Substantial Overlap*)
- **Kelas Serangan Dievaluasi (`kelas_dievaluasi`):** **0.7667** (*High Overlap*)

---

## 4. Analisis Diskrepansi & Rekonsiliasi Metodologis

Terdapat 3 makalah dengan perbedaan klasifikasi peran granular, di mana Koder 1 mengklasifikasikan sebagai `defense_primary` sementara Koder 2 mengklasifikasikan sebagai `proposal_only`. Seluruh diskrepansi ini berada dalam domain biner pertahanan (*100% sepakat biner*):

1. **`om-2026-chainwatch-kill-chain-aligned-sequential`**
   - *Koder 1:* `defense_primary`
   - *Koder 2:* `proposal_only`
   - *Rasional Rekonsiliasi:* Makalah menyajikan arsitektur mitigasi sekuensial yang sangat spesifik, namun tidak menyertakan eksperimen pengujian empiris kuantitatif (`jenis_evaluasi=none`). Koder 2 secara konservatif mengelompokkannya sebagai proposal konseptual. Keduanya sepakat tingkat maturitasnya adalah **L0**.
2. **`gamini-2026-mcp-secure-runtime-access-control`**
   - *Koder 1:* `defense_primary`
   - *Koder 2:* `proposal_only`
   - *Rasional Rekonsiliasi:* Dokumen teks lengkap berada di balik perlindungan portal/anti-bot. Koder 1 melabeli peran dari ringkasan teknis awal, sedangkan Koder 2 menahan status evaluasi hingga berkas terbuka. Keduanya sepakat makalah mengusulkan mekanisme kontrol akses pertahanan.
3. **`shiqiang-2025-secure-model-context-protocol-large`**
   - *Koder 1:* `defense_primary`
   - *Koder 2:* `proposal_only`
   - *Rasional Rekonsiliasi:* Serupa dengan Gamini-2026, status teks lengkap berbayar/paywalled mendorong Koder 2 menandai proposal murni tanpa evaluasi.

---

## 5. Temuan Ilmiah Utama yang Dikonfirmasi Secara Independen

1. **Ketiadaan Evaluasi Penyerang Adaptif (*Adaptive Attack Blindness*):**
   - Kedua koder secara independen menemukan bahwa **0 dari 21 sistem pertahanan** dievaluasi terhadap penyerang adaptif ($\kappa = 1.0000$). Ini memvalidasi klaim kritis di Bab 6 bahwa literatur pertahanan agen MCP saat ini rentan terhadap *adaptive attacker bypass*.
2. **Ketiadaan Validasi Pihak Ketiga Independen (*Independence Gap*):**
   - Tidak ada satu pun makalah dalam sampel yang dievaluasi oleh entitas independen atau menggunakan kerangka evaluasi pihak ketiga murni (0 makalah L2, $\kappa = 1.0000$).
3. **Konfirmasi Bukti Adopsi Produksi (Maturitas L3):**
   - Kedua koder secara serempak mengonfirmasi makalah `chenning-2026-adr-agentic-detection-system-enterprise` sebagai satu-satunya sistem yang memenuhi kriteria **L3**, didukung bukti adopsi skala produksi publik pada infrastruktur Uber.
