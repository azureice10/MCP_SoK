# Pedoman Operasional Pengisian Lembar Koding Pertahanan (v1.1)

Berlaku untuk `Lembar_Koding_Pertahanan_v1.1.xlsx`, sheet `Koding`. Pedoman ini
mengikat: bila ada konflik dengan ingatan atau draf lain, pedoman ini yang dipakai.
Semua nilai berasal dari teks paper, bukan dari judul, abstrak, atau kolom agent.

---

## 0. Prinsip yang tidak boleh dilanggar

1. **Tidak ada tebakan.** Bila teks tidak cukup, pakai `tidak_jelas` atau kosongkan,
   lalu tulis alasannya di `catatan`.
2. **Kode dari bagian metode dan evaluasi**, bukan dari abstrak. Abstrak hanya
   cukup untuk peran, nama, paradigma, dan ringkasan mekanisme.
3. **Tanpa teks lengkap = tanpa kode evaluasi.** Isi `teks_lengkap_tersedia = tidak`
   dan kosongkan semua kolom dari `jenis_evaluasi` sampai `biaya_utilitas`.
4. **Tidak ada nilai default.** Jangan menyalin pola dari baris lain (misalnya
   `A1;C1`). Setiap kelas harus punya alasan dari teks paper itu.
5. **Kolom biru (maturitas, cek_konsistensi) dilarang diedit.** Maturitas selalu hasil
   rumus.
6. **Sembunyikan kolom `agent_role (referensi)`** sebelum mulai (klik kanan kolom F,
   Hide). Tentukan peran dari paket bukti dulu, baru buka kolom itu untuk
   perbandingan, dan catat perbedaan di `catatan`.

## 1. Sebelum mulai (±20 menit)

1. Buka 5 paket acak di `defense/packets/`. Untuk tiap paket, salin satu kutipan ke
   pencarian teks di `fulltext.txt` paper tersebut. Kutipan harus ada persis, dan
   lokasi (bagian atau halaman) harus benar. Jika satu saja gagal, hentikan dan
   kembalikan ke agent.
2. Pastikan tiap paket punya blok Adaptivity hits (bisa berisi `no hits`).
3. Simpan salinan lembar kosong sebagai cadangan.

## 2. Urutan kerja

| Urutan | Baris (kolom `triase`) | Yang dilakukan | Waktu/baris |
|---|---|---|---|
| 1 | `kandidat_agent` (80) | Isi lengkap sesuai Bagian 3–8 | 5–8 menit (proposal_only: 2–3) |
| 2 | `kandidat_cek_recall` (17) | Putuskan peran dulu. Bila bukan pertahanan, berhenti. Bila pertahanan, isi lengkap | 3–8 menit |
| 3 | `scan_cepat` (89) | Isi `peran` saja dari judul dan abstrak. Bila ada indikasi mitigasi yang diimplementasikan, buka paketnya dan naikkan menjadi kandidat | ±1 menit |

Simpan setiap 20 baris. Kerjakan per kelompok satu sesi agar definisi tetap segar.

## 3. Kolom `peran` (isi untuk SEMUA baris)

Jawab berurutan dan berhenti di jawaban pertama yang cocok.

1. Paper membangun atau menspesifikasikan **mekanisme** yang dimaksudkan mencegah,
   mendeteksi, atau memitigasi serangan pada sistem berbasis MCP? Pemindai,
   detektor, gateway, dan kebijakan termasuk mekanisme.
   - **Ya, dan itu kontribusi utama** → `defense_primary`
   - **Ya, tetapi kontribusi utamanya serangan, pengukuran, atau survei, dan
     mitigasi itu diimplementasikan serta dievaluasi** → `defense_secondary`
   - **Ya, tetapi hanya disarankan atau disketsa tanpa implementasi/evaluasi** →
     `proposal_only`
2. **Tidak.** Pilih satu:
   - eksploit atau serangan tanpa mitigasi yang dievaluasi → `attack`
   - survei, SLR, taksonomi, threat model → `survey_review`
   - benchmark, dataset, studi pengukuran → `benchmark_measurement`
   - makalah posisi, konseptual, indeks atau kerangka penilaian tanpa mekanisme
     penegakan → `position_other`
   - lainnya (jelaskan di `catatan`) → `not_defense`

Penegasan:
- Survei atau SLR atas pertahanan **bukan** `proposal_only`; pakai `survey_review`,
  sekalipun memuat "panduan yang diusulkan".
- Serangan dengan satu paragraf "kami sarankan" tanpa eksperimen = `attack`. Bila ada
  eksperimen yang menunjukkan mitigasi menurunkan keberhasilan serangan =
  `defense_secondary`.
- Benchmark untuk menilai pertahanan = `benchmark_measurement`.
- Contoh dari korpus (peran, bukan kode lain): Hou et al. (landscape) =
  `survey_review`; Zhou et al. (autentikasi server remote) =
  `benchmark_measurement`; MCPTox = `benchmark_measurement`; MCP-SecLint =
  `defense_primary`.

Untuk peran non-pertahanan (`attack`, `survey_review`, `benchmark_measurement`,
`position_other`, `not_defense`) **kosongkan semua kolom lain**; rumus akan mengisi
`n/a`.

## 4. Kolom identitas pertahanan (peran pertahanan saja)

| Kolom | Cara mengisi |
|---|---|
| `teks_lengkap_tersedia` | `ya` bila kamu punya teks lengkap dan bisa membuka paketnya; selain itu `tidak` |
| `nama_pertahanan` | Nama dari penulis; bila tak ada, tulis `unnamed:<3 kata kunci>` |
| `ringkasan_mekanisme` | Maks 2 kalimat dengan kata sendiri: apa yang diperiksa, di mana, dan apa yang memutuskan izin atau tolak |

**Paper dengan beberapa pertahanan.** Buat baris terpisah (salin baris, ubah
`nama_pertahanan`, `record_id` tetap) hanya bila komponen itu punya titik penegakan
berbeda **atau** dievaluasi secara terpisah. Komponen yang selalu berjalan bersama dan
dievaluasi sebagai satu sistem = satu baris. Baseline pembanding di dalam paper
tidak dibuatkan baris kecuali baseline itu sendiri adalah record korpus (baris dari
record itu sendiri).

## 5. `paradigma`, `llm_dlm_keputusan`, `titik_penegakan`

### 5.1 `llm_dlm_keputusan` (isi dulu, sebelum `paradigma`)

- `ya`: pada saat runtime, keputusan izin, tolak, atau deteksi bergantung pada
  keluaran LLM atau model ML (LLM-as-judge, klasifikator ML, LLM yang menormalkan
  masukan lalu hasilnya menentukan keputusan).
- `tidak`: keputusan murni dari aturan, kriptografi, atau mekanisme OS.
- LLM yang hanya dipakai **saat penyiapan** (misalnya menurunkan kebijakan yang
  kemudian ditegakkan tanpa LLM per request) = `tidak`; tulis fakta itu di
  ringkasan.
- Teks tidak menyatakan apakah LLM dipanggil per request = `tidak_jelas`.

### 5.2 `paradigma`: pilih **satu** yang menentukan keputusan akhir

| Nilai | Pilih bila |
|---|---|
| `content_inspection_static` | Menganalisis kode, konfigurasi, atau metadata secara offline atau sebelum publikasi |
| `content_inspection_runtime` | Memeriksa isi (deskripsi, argumen, hasil, jejak) saat berjalan, dengan aturan, heuristik, model ML, atau LLM |
| `human_approval` | Keputusan akhir ada pada persetujuan pengguna |
| `isolation_containment` | Membatasi dampak lewat sandbox, kontainer, VM, atau pembatasan path |
| `deterministic_policy` | Aturan eksplisit (mis. OPA, Cedar, ABAC) mengevaluasi permintaan **dan** `llm_dlm_keputusan = tidak` |
| `capability_or_token` | Otoritas dibawa token atau kapabilitas yang dapat diperlemah atau diverifikasi |
| `integrity_provenance` | Tanda tangan, hash, pinning, atau atestasi atas definisi atau server |
| `protocol_provision` | Ketentuan spesifikasi protokol atau perluasan protokol |
| `lainnya` | Tak ada yang cocok (jelaskan) |

Aturan keras: `deterministic_policy` **dilarang** bila `llm_dlm_keputusan` = `ya`
(lembar akan menandai PERIKSA). Sistem hibrida diberi paradigma komponen yang
menentukan keputusan akhir; komponen lain disebut di ringkasan.

### 5.3 `titik_penegakan`

`H` host; `C` klien; `S` server; `gateway_proxy` komponen yang menengahi klien dan
server; `registry` saat publikasi atau admisi; `Theta` infrastruktur otorisasi; `X`
sisi sistem eksternal; `offline_analysis` di luar jalur permintaan; `lainnya`. Pilih
satu titik primer.

## 6. Crossing dan kelas taksonomi

**`kelas_diklaim`**: kelas yang paper **secara eksplisit** nyatakan diatasi (abstrak,
pendahuluan, threat model). Pisahkan dengan `;`. Jangan menyimpulkan dari kata
"security" umum. Pemetaan berdasarkan mekanisme serangan, bukan istilah:

| Kelas | Mekanisme yang dimaksud | Crossing |
|---|---|---|
| A1 | Instruksi berbahaya di deskripsi atau skema tool | R2 |
| A2 | Injeksi lewat hasil tool atau resource | R2 |
| A3 | Miscall akibat deskripsi ambigu atau bertentangan | R2 |
| B1 | Perubahan definisi setelah persetujuan (rug pull) | R7 |
| B2 | Drift metadata registri dari waktu ke waktu | R7 |
| B3 | Kegagalan planner terhadap mutasi skema | R7 |
| C1 | Confused deputy | R3 |
| C2 | Caller identity confusion (otorisasi sebagai state persisten) | R3 |
| C3 | Otorisasi transport hilang atau cacat | R4 |
| C4 | Inversi niat lewat jejak pemanggilan | R3 |
| C5 | Handler server keluar dari cakupan yang diiklankan | R5 |
| D1 | Rantai tool lintas server, eksfiltrasi terkomposisi | R6 |
| D2 | Bypass guardrail pada rencana multi-langkah | R6 |
| D3 | Propagasi kerentanan lewat kloning atau rantai pasok | `PRA` (pra-sesi) |

Kelas di luar taksonomi (mis. penyalahgunaan sumber daya atau DoS): tulis
`OUT_OF_TAXONOMY:<deskripsi>` **tanpa** memuat kode kelas di dalam deskripsi
(rumus menghitung dengan pencocokan teks).

**`crossings (R1-R7, pisah ;)`**: crossing yang propertinya ditegakkan oleh
pertahanan. Harus konsisten dengan tabel di atas; selisih perlu alasan di `catatan`.

**`kelas_dievaluasi`**: hanya kelas yang punya **eksperimen atau studi kasus dengan
hasil** di paper. Harus merupakan himpunan bagian dari `kelas_diklaim`. Klaim tanpa
eksperimen tidak masuk sini.

## 7. Evaluasi (hanya bila `teks_lengkap_tersedia = ya`)

### 7.1 `jenis_evaluasi`

| Nilai | Kapan |
|---|---|
| `none` | Tidak ada eksperimen, ukuran, atau studi kasus dengan hasil |
| `author_run` | Penulis mengevaluasi sendiri |
| `author_run+independent` | Ditambah paper LAIN di korpus yang menjalankan eksperimen terhadap pertahanan ini |
| `independent_only` | Hanya paper lain di korpus yang mengevaluasi (penulis tidak) |
| `deployment_measurement` | Studi pengukuran mengamati kontrol ini di deployment nyata. Maturitas kosong; laporkan terpisah di Section 5 |

Evaluasi independen sah bila **semua** terpenuhi: (a) paper lain ada di korpus 186;
(b) ia **mengeksekusi** eksperimen terhadap pertahanan itu (tabel atau hasil);
(c) sekadar menyebut, mengutip, atau membahas tidak dihitung. Sumber kandidat:
`independent_eval_candidates.csv`; verifikasi konteksnya. Isi `evaluator_independen`
dengan `record_id` paper penguji (pisah `;`). Bila penguji adalah pesaing yang
membandingkan baseline, tetap dihitung dan tulis "baseline pesaing" di `catatan`.

### 7.2 `asal_set_serangan`

`authors_own` buatan penulis; `third_party_public` benchmark atau dataset publik
(tulis namanya di `catatan`); `mixed`; `none` bila `jenis_evaluasi = none`.

### 7.3 `adaptif` (ketat)

Jawab tiga pertanyaan dari paket (Adaptivity hits dan bagian evaluasi):

1. Apakah paper menyebut serangan yang **dirancang atau dioptimasi terhadap
   pertahanan ini** dengan pengetahuan cara kerjanya (white-box, defense-aware,
   iterasi terhadap keputusan pertahanan)?
2. Apakah kalimat itu berbicara tentang pertahanan **ini**, bukan baseline atau
   pertahanan lain?
3. Apakah kamu bisa menyalinnya persis (maks 25 kata)?

- Ketiganya ya → `ya`, dan salin kutipan ke `kutipan_adaptif`.
- Set serangan tetap, benchmark, variasi parafrase, atau "unseen" yang tidak disetel
  terhadap pertahanan → `tidak`.
- Setelah membaca semua hits dan bagian evaluasi, teks tetap ambigu → `tidak_jelas`
  dan tulis apa yang sudah dicek di `catatan`.
- `jenis_evaluasi = none` → wajib `n/a_tanpa_evaluasi`.

Jebakan umum: kata *adaptive* sering menunjuk kebijakan atau ambang yang adaptif,
bukan penyerang adaptif. Kata *bypass* sering menggambarkan serangan pada baseline.
*Red team* oleh penulis dengan prompt tetap bukan adaptif kecuali disetel terhadap
pertahanan.

### 7.4 `lokasi_bukti` dan `biaya_utilitas`

- `lokasi_bukti`: wajib untuk setiap entri yang dievaluasi; tulis seperti
  `Sec 5.2; Table 3; hal. 8`.
- `biaya_utilitas`: tulis metrik dan nilainya (`latensi +5 ms (Tabel 4)`); bila teks
  lengkap sudah dibaca dan tidak ada, tulis `not_reported`; biarkan kosong hanya bila
  belum dikodekan. Rumus menghitung entri berisi teks selain `not_reported`.

## 8. `deployment` dan L3

`none` bawaan. `prototype_open_source` bila ada kode publik. `produksi_bukti_publik`
hanya bila ada rilis atau dokumentasi resmi bertanggal yang menunjukkan mekanisme
dikirim di produk (tulis sumber di `catatan`). `spec_normatif` hanya untuk ketentuan
MUST atau SHOULD di revisi spesifikasi. Ketersediaan kode bukan L3.

Ketentuan spesifikasi dilaporkan di Section 5 (Tabel 14–15), **bukan** dibuatkan baris
baru di lembar ini. Baris L3 yang muncul dilaporkan terpisah, tidak sebagai persentase
literatur.

## 9. Kolom biru

`maturitas` dihitung dari `deployment` dan `jenis_evaluasi`: L3 (spec_normatif atau
produksi_bukti_publik), L2 (mengandung independent), L1 (author_run), L0 (none),
`n/a` (peran non-pertahanan). Bila kosong padahal peran pertahanan, kolom
`jenis_evaluasi` belum diisi atau berupa `deployment_measurement`.

`cek_konsistensi` harus kosong di baris selesai. Arti tiap PERIKSA:

| Pesan | Perbaikan |
|---|---|
| deterministic_policy tetapi LLM/ML ada dalam keputusan | Ubah paradigma atau `llm_dlm_keputusan` sesuai teks |
| adaptif=ya wajib ada kutipan | Tambah kutipan, atau ubah ke `tidak` bila tak bisa dikutip |
| tanpa evaluasi, adaptif harus n/a | Isi `n/a_tanpa_evaluasi` |
| isi kelas_dievaluasi / isi lokasi_bukti | Lengkapi dari bagian evaluasi |
| tanpa teks lengkap, kosongkan kolom evaluasi | Kosongkan atau perbaiki `teks_lengkap_tersedia` |

## 10. Contoh terkalibrasi (ilustrasi hipotetis; jawabannya baku)

| # | Deskripsi | Kode yang benar |
|---|---|---|
| 1 | Sandbox per subproses server dijalankan host; penulis menguji 20 kasus path traversal dari set buatan sendiri; tidak ada serangan yang disesuaikan | `defense_primary`; `isolation_containment`; `llm=tidak`; `H`; R5; klaim C5; evaluasi C5; `author_run`; `authors_own`; `adaptif=tidak`; `prototype_open_source`; maturitas L1 |
| 2 | LLM-as-judge memeriksa deskripsi tool, diuji di benchmark publik oleh penulis; paper lain di korpus menjalankannya pada set serangannya sendiri | `content_inspection_runtime`; `llm=ya`; `author_run+independent` (isi `evaluator_independen`); `third_party_public`; L2 |
| 3 | Mesin kebijakan OPA dengan aturan tertulis administrator, dievaluasi penulis pada 30 tugas | `deterministic_policy`; `llm=tidak`; `author_run`; L1 |
| 4 | Gateway "deterministik" di mana LLM menilai risiko tiap panggilan, lalu aturan mengizinkan atau menolak menurut level risiko | `content_inspection_runtime`, `llm=ya` (bukan deterministic_policy); sebut hibrida di ringkasan |
| 5 | Paper serangan dengan satu paragraf saran mitigasi tanpa eksperimen | `attack`; kolom lain kosong |
| 6 | Paper serangan yang memuat detektor, dievaluasi menurunkan keberhasilan serangan dari 90% ke 10% | `defense_secondary`; isi seperti pertahanan biasa |
| 7 | Penulis mengoptimasi payload terhadap detektor mereka dengan pengetahuan aturannya dan melaporkan hasilnya | `adaptif=ya`; salin kalimat yang menyatakannya ke `kutipan_adaptif` |
| 8 | Survei pertahanan dengan "panduan yang diusulkan" | `survey_review`; kolom lain kosong |

## 11. Bila ragu

1. Baca ulang bagian metode dan evaluasi di paket, bukan abstrak.
2. Pakai kode paling konservatif: `tidak_jelas`, kosong, atau `none`.
3. Tulis `DISKUSI:` di awal `catatan` beserta pertanyaannya. Baris itu dibahas saat
   rekonsiliasi dengan koder kedua.
4. Jangan menunda banyak baris sekaligus; bila lebih dari 15% baris bertanda
   `DISKUSI`, pedoman ini perlu direvisi sebelum lanjut.

## 12. Selesai: daftar cek sebelum mengirim

- [ ] Sheet `Ringkasan`: "Baris dengan PERIKSA" = 0.
- [ ] "Baris sudah diberi peran" = 186.
- [ ] Jumlah peran di bagian B menjumlah ke 186.
- [ ] Semua entri dievaluasi punya `lokasi_bukti` dan `kelas_dievaluasi`.
- [ ] Semua `adaptif = ya` punya kutipan yang kamu cek ada persis di paper.
- [ ] Baris `teks_lengkap_tersedia = tidak` terdata, untuk diprioritaskan lewat
      akses institusi lalu dikodekan ulang.
- [ ] Simpan sebagai `Lembar_Koding_KODER1_SELESAI.xlsx` dan kirim. Angka di
      Ringkasan **belum boleh dikutip di naskah** sebelum koder kedua selesai dan
      rekonsiliasi dilakukan.
