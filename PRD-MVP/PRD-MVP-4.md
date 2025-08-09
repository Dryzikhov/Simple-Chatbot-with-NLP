# PRD-MVP-4: Simple Chatbot with NLP

## Ikhtisar proyek
Simple Chatbot adalah asisten percakapan berbasis teks yang membantu pengguna menemukan jawaban cepat atas pertanyaan umum (FAQ) dan melakukan tugas sederhana. Versi MVP berfokus pada pemahaman pertanyaan dasar dan memberikan respons yang jelas, konsisten, dan mudah dipahami. Peningkatan kemampuan pemahaman bahasa alami yang lebih canggih akan direncanakan pada fase berikutnya (lihat “Rencana Masa Depan”).

## Tujuan MVP
- Menjawab pertanyaan FAQ prioritas dengan akurasi minimal 90% pada uji internal yang terukur.
- Memberikan respons pertama dalam ≤ 2 detik pada koneksi internet normal.
- Menangani minimal 80% sesi tanpa bantuan manusia melalui jawaban langsung atau panduan langkah.
- Menyediakan cara mudah untuk memperbarui konten jawaban tanpa perlu perubahan kode.
- Mengumpulkan umpan balik pengguna di akhir percakapan untuk mengukur kepuasan (target rata-rata ≥ 4/5 pada uji pilot).

## Ruang lingkup
**In-scope (MVP):**
- Menjawab daftar FAQ yang telah disepakati (mis. 20–50 topik prioritas).
- Pencarian kata kunci sederhana dan pencocokan frasa untuk memetakan pertanyaan ke jawaban.
- Tanggapan standar untuk pertanyaan di luar cakupan (“maaf, belum bisa menjawab”) dengan opsi rujukan.
- Antarmuka chat web responsif (desktop dan mobile).
- Panel sederhana untuk mengelola konten (tambah/ubah/hapus jawaban).
- Pencatatan percakapan non-pribadi untuk evaluasi kualitas (tanpa data sensitif).

**Out-of-scope (MVP; dipindahkan ke Rencana Masa Depan):**
- Pemahaman konteks percakapan multi-putaran yang kompleks.
- Menangkap nuansa bahasa, maksud tidak langsung, atau ambiguitas tingkat lanjut.
- Pembelajaran otomatis dari percakapan langsung (training otomatis).

## Persona dan kebutuhan utama
- **Pengguna umum:** Butuh jawaban cepat, jelas, dan relevan.
- **Pemilik konten/CS:** Butuh cara mudah memperbarui jawaban dan menambah topik baru.
- **Manajer operasional:** Butuh metrik sederhana: tingkat penyelesaian, kepuasan, topik teratas, dan gap konten.

## Fitur MVP
**Must-have:**
- FAQ prioritas dengan struktur tanya–jawab konsisten.
- Pencocokan kata kunci dan frasa.
- Respons fallback yang sopan.
- UI chat web ringan dan responsif.
- Pengelolaan konten jawaban (CRUD).
- Pencatatan metrik dasar.

**Should-have:**
- Saran pertanyaan terkait.
- Tombol cepat untuk topik populer.

**Nice-to-have:**
- Tema yang dapat disesuaikan.
- Ekspor data percakapan (CSV).

## Alur utama pengguna
1. Pengguna membuka widget chat di halaman web.
2. Pengguna mengetik pertanyaan singkat.
3. Chatbot mencocokkan pertanyaan dan menampilkan jawaban ringkas.
4. Chatbot menawarkan tindakan lanjutan.
5. Chatbot meminta rating singkat.

## Kisah pengguna
- Sebagai pengguna, saya ingin bertanya dengan bahasa sehari-hari agar cepat mendapatkan jawaban.
- Sebagai pengguna, saya ingin melihat pertanyaan terkait jika jawaban kurang tepat.
- Sebagai pengguna, saya ingin opsi untuk menghubungi dukungan.
- Sebagai pemilik konten, saya ingin memperbarui jawaban dengan cepat.
- Sebagai manajer operasional, saya ingin ringkasan kinerja mingguan.

## Kriteria penerimaan
- **Kualitas jawaban:** ≥ 90% akurasi, ≥ 80% penyelesaian mandiri.
- **Kinerja:** Respons ≤ 2 detik, uptime ≥ 99%.
- **Pengalaman pengguna:** Tampilan responsif, fitur pertanyaan terkait dan dukungan.
- **Konten:** Konten bisa dikelola tanpa tim teknis.
- **Privasi:** Tidak menyimpan data pribadi.
- **Definisi selesai:** Semua kriteria terpenuhi dan berhasil pada skenario uji.

## Metrik keberhasilan
- Self-serve ≥ 80%
- Fallback ≤ 15%
- CSAT ≥ 4/5
- Jawaban topik populer dalam ≤ 2 langkah
- Respons pertama ≤ 2 detik

## Batasan dan ketergantungan
- Basis pengetahuan awal disediakan tim konten.
- Bahasa utama: Indonesia.
- Platform: web saja.
- Tidak ada pelatihan otomatis.

## Rencana Masa Depan (NLP)
Tujuan: membuat chatbot berinteraksi lebih alami dan efektif.
- **Memahami pertanyaan rumit:** Maksud implisit, ambiguitas, konteks multi-putaran.
- **Respons variasi bahasa:** Sinonim, gaya tutur, singkatan, entitas spesifik.
- **Target NLP:** ≥ 85–90% akurasi, penurunan fallback ≥ 30%, peningkatan CSAT ≥ 0.3 poin.
- **Ekstensi fitur:** Pemahaman konteks, pencocokan makna, penjelasan langkah demi langkah.
- **Kontrol kualitas:** Tinjauan manusia, jawaban diawasi, pemantauan kesalahan dan bias.

## Lampiran: Daftar FAQ (Contoh)
- Jam operasional.
- Pengiriman dan kebijakan.
- Pengembalian dan penukaran.
- Akun dan kata sandi.
- Metode pembayaran.
- Kontak dukungan.
