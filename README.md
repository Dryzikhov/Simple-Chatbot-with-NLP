# Chatbot Cerdas dengan NLP

## Deskripsi
Proyek ini adalah sebuah chatbot cerdas yang dirancang untuk melayani permintaan pengguna secara dinamis. Berbeda dari chatbot berbasis kata kunci sederhana, program ini menggunakan teknik Pemrosesan Bahasa Alami (NLP) dasar melalui _regular expressions_ untuk mengenali maksud (intent) pengguna dan mengekstrak informasi penting (entitas) dari percakapan.

Chatbot ini mampu terhubung dengan sistem data (disimulasikan melalui JSON) untuk melakukan tugas-tugas praktis seperti memeriksa status pesanan dan mencari informasi produk, serta menyertakan lapisan verifikasi untuk keamanan data.

## Fitur Utama
- **Pengenalan Maksud & Entitas:** Mampu memahami permintaan spesifik seperti "cek status pesanan ORD123" atau "info produk Laptop Pro" dan mengekstrak data relevan (ID pesanan, nama produk).
- **Pengecekan Status Pesanan:** Memungkinkan pengguna melacak status pesanan mereka. Fitur ini diamankan dengan **verifikasi email** untuk memastikan hanya pemilik pesanan yang dapat melihat statusnya.
- **Pencarian Informasi Produk:** Memberikan detail produk (deskripsi, harga, stok) secara dinamis berdasarkan permintaan pengguna.
- **Manajemen Konteks Percakapan:** Mampu menangani dialog multi-langkah, seperti saat meminta email untuk proses verifikasi pesanan.
- **Logging Percakapan:** Semua interaksi dicatat ke dalam file `chat_log.txt` untuk tujuan audit dan analisis di masa depan.
- **Respons Fallback Cerdas:** Jika permintaan tidak dikenali, chatbot akan memberikan petunjuk tentang cara bertanya yang benar.

## Teknologi yang Digunakan
- **Bahasa:** Python 3
- **Kerangka Kerja/Library:** Hanya menggunakan pustaka standar Python (`json`, `re`, `logging`). Tidak ada dependensi eksternal.
- **Database:** File JSON (`orders.json`, `products.json`) digunakan untuk mensimulasikan database pesanan dan produk.

## Instalasi
Proyek ini tidak memerlukan instalasi dependensi eksternal.

1.  Clone repositori ini ke mesin lokal Anda:
    ```bash
    git clone <URL_REPOSITORI_PROYEK_INI>
    ```
2.  Navigasikan ke direktori proyek:
    ```bash
    cd <NAMA_DIREKTORI_PROYEK>
    ```

## Penggunaan
Untuk menjalankan chatbot, jalankan skrip utama dari terminal Anda:
```bash
python3 chatbot.py
```
Chatbot akan diinisialisasi dan siap menerima input Anda.

**Contoh Sesi 1: Pengecekan Status Pesanan**
```
Menginisialisasi chatbot...
Chatbot berhasil diinisialisasi.

Chatbot siap! Ketik pertanyaan Anda atau 'exit' untuk keluar.
Anda: status pesanan ORD759
Bot: Tentu, untuk memverifikasi, silakan masukkan alamat email yang terkait dengan pesanan ORD759.
Anda: john.doe@example.com
Bot: Status untuk pesanan ORD759 adalah: **Sedang Diproses**.
```

**Contoh Sesi 2: Pencarian Info Produk**
```
Anda: info produk Mouse Gaming
Bot: Berikut detail untuk **Mouse Gaming**:
- Deskripsi: Mouse dengan presisi tinggi untuk pengalaman gaming terbaik.
- Harga: Rp 850,000
- Stok: 150 unit
```

**Contoh Sesi 3: Pertanyaan Tidak Dikenali**
```
Anda: cuaca hari ini
Bot: Maaf, saya tidak mengerti. Coba gunakan format seperti: 'status pesanan ORD123' atau 'info produk Laptop Pro'.
```

## Kontribusi
Kami menyambut baik kontribusi dari siapa saja. Jika Anda ingin berkontribusi, silakan ikuti langkah-langkah berikut:
1.  **Fork** repositori ini.
2.  Buat **branch** baru untuk fitur Anda (`git checkout -b fitur/NamaFiturAnda`).
3.  **Commit** perubahan Anda (`git commit -m 'Menambahkan fitur X'`).
4.  **Push** ke branch Anda (`git push origin fitur/NamaFiturAnda`).
5.  Buka **Pull Request**.

## Lisensi
Proyek ini dilisensikan di bawah **Lisensi MIT**. Lihat file `LICENSE` untuk detail lebih lanjut.
