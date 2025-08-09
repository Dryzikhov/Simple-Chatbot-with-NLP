# PRD-MVP-3.md — Simple Chatbot with NLP

## Metadata
- Versi: 1.0 (MVP)
- Tanggal: 10 Agustus 2025
- Pemilik Dokumen: Manajer Produk
- Nama Proyek: Simple Chatbot with NLP

---

## Ikhtisar Proyek
Proyek ini bertujuan membangun chatbot sederhana yang mampu terhubung dengan sistem eksternal seperti sistem manajemen pesanan dan basis data produk. Tujuannya adalah memungkinkan pengguna melakukan tugas praktis seperti memeriksa status pesanan dan mendapatkan informasi produk secara langsung melalui percakapan.

---

## Tujuan
- Memberikan jawaban status pesanan yang akurat untuk ≥ 95% permintaan yang tervalidasi.
- Menyediakan informasi produk (nama, harga, stok, deskripsi) dengan akurasi ≥ 95%.
- Waktu respon rata-rata ≤ 3 detik untuk ≥ 90% permintaan.
- Tingkat penyelesaian mandiri ≥ 80% untuk dua kasus utama: cek pesanan dan info produk.
- Skor kepuasan pengguna rata-rata ≥ 4 dari 5.

---

## Fitur
1. Pengenalan maksud percakapan (cek pesanan vs info produk).
2. Cek status pesanan dengan verifikasi ringan.
3. Pencarian dan penyajian informasi produk.
4. Klarifikasi otomatis jika data tidak lengkap.
5. Eskalasi ke agen manusia bila diperlukan.
6. Pesan kesalahan yang jelas dan ramah.
7. Log percakapan dan ringkasan permintaan.
8. Privasi dan keamanan data dasar.

---

## Kisah Pengguna
- Sebagai pelanggan, saya ingin memeriksa status pesanan saya agar tahu kapan pesanan tiba.
- Sebagai pelanggan, saya ingin mencari informasi produk agar bisa memutuskan untuk membeli.
- Sebagai pelanggan, saya ingin diberi tahu jika saya salah memasukkan data dan cara memperbaikinya.
- Sebagai pelanggan, saya ingin bisa berbicara dengan agen manusia jika chatbot tidak bisa membantu.
- Sebagai staf layanan, saya ingin melihat ringkasan percakapan agar bisa melanjutkan bantuan dengan cepat.

---

## Kriteria Penerimaan
- Jawaban dalam bahasa Indonesia yang jelas dan sopan.
- Respon ≤ 3 detik untuk ≥ 90% permintaan.
- Akurasi data ≥ 95% untuk status pesanan dan info produk.
- Eskalasi tersedia kapan saja atas permintaan pengguna.
- Ringkasan percakapan tersedia untuk agen layanan.
- Tidak menampilkan data pribadi tanpa verifikasi.

---

## Rencana Masa Depan
- Integrasi dengan kanal lain (WhatsApp, Instagram).
- Dukungan bahasa Inggris.
- Fitur transaksi lanjutan (ubah alamat, pembatalan).
- Personalisasi berdasarkan riwayat pengguna.
- Analitik lanjutan untuk pemantauan kualitas.
- Pusat pengetahuan untuk pertanyaan umum.
