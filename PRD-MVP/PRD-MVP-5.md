# PRD-MVP-5: Simple Chatbot with NLP

## 1. Ikhtisar Proyek
Simple Chatbot with NLP adalah chatbot berbasis teks yang dirancang untuk memberikan jawaban cepat dan jelas terhadap pertanyaan umum. MVP berfokus pada percakapan dasar tanpa fitur personalisasi lintas sesi.

## 2. Tujuan
- Menyediakan jawaban untuk 20–30 pertanyaan FAQ dengan akurasi tinggi.
- Menjamin waktu respons cepat (≤ 2 detik untuk FAQ).
- Memberikan respons sopan untuk pertanyaan di luar cakupan.
- Menyediakan nada dan gaya bahasa yang konsisten.
- Membangun fondasi yang mudah diperluas untuk fitur personalisasi di masa depan.

## 3. Lingkup MVP
### 3.1 Dalam Lingkup
- Antarmuka chat berbasis teks.
- Jawaban untuk FAQ terkurasi.
- Penanganan salam, bantuan, dan fallback.
- Log kategori pertanyaan untuk evaluasi konten.

### 3.2 Di Luar Lingkup
- Personalisasi pengguna.
- Integrasi multi-kanal.
- Handover ke agen manusia.
- Analitik lanjutan.
- Dukungan multi-bahasa.

## 4. Fitur
1. **Percakapan Dasar**
   - Menyapa pengguna.
   - Menjelaskan fungsi chatbot dan menampilkan daftar topik.

2. **FAQ Terkurasi**
   - Jawaban siap pakai untuk 20–30 pertanyaan umum.
   - Panduan langkah bila diperlukan (maks. 5 langkah).

3. **Fallback Terarah**
   - Respon untuk pertanyaan di luar cakupan:
     - Mengakui keterbatasan.
     - Menampilkan topik yang tersedia.
     - Memberikan tautan kontak atau instruksi lanjut.

4. **Nada dan Bahasa Konsisten**
   - Bahasa sopan, ringkas, ramah.
   - Tanpa jargon teknis.

5. **Pencatatan Ringan**
   - Log tipe pertanyaan.
   - Tidak menyimpan data pribadi.

6. **Kepatuhan Privasi**
   - Pemberitahuan singkat tentang penggunaan data.
   - Tidak menyimpan preferensi pengguna lintas sesi.

## 5. Kisah Pengguna
- *Sebagai pengguna baru*, saya ingin tahu topik apa yang bisa dibantu agar bisa mulai dengan cepat.
- *Sebagai pengguna yang punya pertanyaan*, saya ingin jawaban yang relevan dan mudah dipahami.
- *Sebagai pengguna dengan pertanyaan yang tidak dikenal*, saya ingin diarahkan dengan sopan ke sumber bantuan lain.
- *Sebagai pemilik konten*, saya ingin data pertanyaan yang tidak dikenali untuk perbaikan konten.

## 6. Kriteria Penerimaan
- Chatbot merespons salam dengan pengantar dan daftar topik.
- FAQ dijawab dengan jawaban ringkas dan tepat dalam ≤ 2 detik.
- Pertanyaan di luar cakupan ditangani dengan fallback sopan dan informatif.
- Minimal 80% pengguna uji menyatakan puas terhadap jawaban FAQ.
- Bahasa dan nada konsisten, bebas jargon.
- Tidak menyimpan data pribadi.
- Semua FAQ telah disetujui oleh pemangku kepentingan.

## 7. Rencana Masa Depan
- **Personalisasi**
  - Menyimpan preferensi pengguna secara eksplisit.
  - Menyesuaikan gaya dan isi respons.
  - Memberi kontrol penuh kepada pengguna untuk melihat/menghapus preferensi.
- **Ekspansi**
  - Dukungan multi-bahasa.
  - Integrasi kanal lain (WhatsApp, Email).
  - Analitik dan laporan konten.

## 8. Risiko dan Mitigasi
- *Cakupan konten terbatas*: Gunakan fallback dan tampilkan daftar topik.
- *Ekspektasi pengguna terlalu tinggi*: Jelaskan batasan chatbot di awal.
- *Kekonsistenan nada*: Uji dengan pengguna dan lakukan review konten.
- *Privasi*: Hindari penyimpanan data pribadi dan tampilkan pemberitahuan singkat.

## 9. Keputusan Tertunda
- Kanal utama (web/widget/aplikasi)?
- Bahasa utama (Indonesia saja atau multi-bahasa)?
- Nada merek (formal/semi-formal)?
- Sumber dan penanggung jawab FAQ?
- Tautan kontak fallback?
- Kalimat privasi untuk sesi awal?
- Target waktu respons final?
