# Proyek Chatbot Sederhana dengan NLP

## Deskripsi
Proyek ini adalah implementasi dari sebuah chatbot sederhana yang dirancang untuk memahami dan merespons pertanyaan dasar dari pengguna. Dibuat sebagai Produk Minimum yang Layak (MVP), chatbot ini menggunakan pencocokan pola berbasis kata kunci untuk memberikan jawaban yang relevan dari basis pengetahuan yang telah ditentukan. Tujuannya adalah untuk menyediakan antarmuka percakapan yang efisien untuk menjawab pertanyaan umum, mengurangi kebutuhan akan intervensi manual, dan membangun fondasi untuk fitur yang lebih canggih di masa depan.

## Fitur Utama
- **Pemahaman Pertanyaan Dasar:** Mampu mengenali pertanyaan umum berdasarkan kata kunci.
- **Respons Berbasis Teks:** Memberikan jawaban yang jelas dan relevan dalam format teks.
- **Penanganan Salam:** Dapat merespons sapaan (misalnya, "Halo") dan ucapan perpisahan (misalnya, "Selamat tinggal").
- **Basis Pengetahuan:** Dilengkapi dengan basis pengetahuan dalam format JSON yang mudah diperluas untuk topik-topik seperti:
  - Jam operasional
  - Prosedur reset kata sandi
  - Pengecekan status pesanan
- **Antarmuka Baris Perintah (CLI):** Interaksi dengan chatbot dilakukan melalui antarmuka teks yang sederhana dan intuitif.

## Teknologi yang Digunakan
- **Bahasa:** Python 3
- **Kerangka Kerja/Library:** Tidak ada kerangka kerja eksternal, hanya menggunakan library standar Python (`json`, `random`).
- **Database:** Tidak menggunakan database eksternal. Basis pengetahuan disimpan dalam berkas `knowledge_base.json`.

## Instalasi
Untuk menjalankan proyek ini di lingkungan lokal, Anda hanya memerlukan Python 3. Tidak ada dependensi eksternal yang perlu diinstal.

1.  **Clone repositori ini (atau unduh file-filenya):**
    ```bash
    git clone https://github.com/username/repo-name.git
    cd repo-name
    ```
2.  Pastikan Anda memiliki `python3` terinstal di sistem Anda.

## Penggunaan
Untuk memulai chatbot, jalankan skrip `chatbot.py` dari terminal Anda:
```bash
python3 chatbot.py
```
Setelah chatbot berjalan, Anda akan melihat pesan sambutan. Cukup ketik pertanyaan Anda dan tekan Enter.

**Contoh Interaksi:**
```
Anda: halo
Bot: Hai, selamat datang. Apa yang bisa saya bantu untuk Anda hari ini?
Anda: jam buka toko
Bot: Toko kami buka dari jam 9 pagi hingga 9 malam, setiap hari Senin sampai Jumat.
Anda: bagaimana cara saya reset password?
Bot: Untuk mereset kata sandi Anda, silakan kunjungi halaman 'Lupa Kata Sandi' di situs web kami dan ikuti petunjuk yang diberikan.
Anda: terima kasih
Bot: Dengan senang hati!
Anda: exit
Bot: Senang bisa membantu. Selamat tinggal!
```
Untuk keluar dari program, ketik `exit`, `quit`, atau `selamat tinggal`.

## Kontribusi
Kami menyambut baik kontribusi dari siapa pun. Jika Anda ingin berkontribusi, silakan ikuti langkah-langkah berikut:
1.  Fork repositori ini.
2.  Buat branch baru (`git checkout -b fitur/NamaFiturAnda`).
3.  Commit perubahan Anda (`git commit -m 'Menambahkan beberapa fitur luar biasa'`).
4.  Push ke branch tersebut (`git push origin fitur/NamaFiturAnda`).
5.  Buka Pull Request.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT.
