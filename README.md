# Chatbot NLP Sederhana

## Deskripsi
Proyek ini adalah sebuah chatbot berbasis teks yang dirancang untuk menjawab pertanyaan-pertanyaan umum secara efisien. Dibangun sebagai Produk Minimum yang Layak (MVP), chatbot ini menggunakan pendekatan Pemrosesan Bahasa Alami (NLP) sederhana berbasis aturan untuk memahami masukan pengguna dan memberikan respons yang relevan dari basis pengetahuan yang telah ditentukan. Tujuannya adalah untuk menyediakan fondasi yang kuat bagi pengembangan asisten virtual yang lebih canggih di masa depan.

## Fitur Utama
- **Pemahaman Pertanyaan Dasar**: Mampu memahami dan merespons pertanyaan umum (misalnya, jam operasional, cara reset password).
- **Penanganan Salam**: Dapat berinteraksi dengan pengguna melalui sapaan dan salam perpisahan.
- **Basis Pengetahuan Eksternal**: Menggunakan file JSON (`knowledge_base.json`) sebagai sumber pengetahuan, sehingga mudah untuk diperbarui dan diperluas.
- **Antarmuka Baris Perintah (CLI)**: Interaksi dengan chatbot dilakukan melalui antarmuka terminal yang sederhana dan intuitif.
- **Respons Fallback**: Memberikan jawaban standar ketika tidak memahami pertanyaan pengguna.

## Teknologi yang Digunakan
- **Bahasa:** Python 3
- **Kerangka Kerja/Library:** Hanya menggunakan pustaka standar Python (`json`, `random`).
- **Penyimpanan Data:** JSON (untuk basis pengetahuan).

## Instalasi
Tidak ada proses instalasi khusus yang diperlukan. Anda hanya memerlukan Python 3 terpasang di sistem Anda.

1.  **Clone repositori ini:**
    ```bash
    git clone https://github.com/username/repo.git
    ```
2.  **Masuk ke direktori proyek:**
    ```bash
    cd nama-direktori-proyek
    ```

## Penggunaan
Untuk menjalankan chatbot, cukup eksekusi skrip Python utama dari terminal Anda:

```bash
python3 chatbot.py
```

Setelah itu, chatbot akan siap menerima masukan Anda. Ketik pertanyaan Anda dan tekan Enter. Untuk keluar, ketik `exit` atau `selamat tinggal`.

**Contoh Sesi:**
```
Chatbot siap! Ketik 'exit' atau 'selamat tinggal' untuk keluar.
Anda: halo
Bot: Hai, selamat datang. Apa yang bisa saya bantu untuk Anda hari ini?
Anda: jam buka toko kapan ya?
Bot: Toko kami buka dari jam 9 pagi hingga 9 malam, setiap hari Senin sampai Jumat.
Anda: terima kasih
Bot: Sama-sama!
Anda: exit
Bot: Sampai jumpa lagi!
```

## Kontribusi
Kontribusi untuk proyek ini sangat diharapkan! Jika Anda ingin berkontribusi, silakan ikuti langkah-langkah berikut:
1.  **Fork** repositori ini.
2.  Buat **branch** baru untuk fitur Anda (`git checkout -b fitur/NamaFitur`).
3.  **Commit** perubahan Anda (`git commit -m 'Menambahkan fitur X'`).
4.  **Push** ke branch Anda (`git push origin fitur/NamaFitur`).
5.  Buka **Pull Request**.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT.