# Proyek Chatbot FAQ Sederhana

## Deskripsi
Proyek ini adalah sebuah chatbot berbasis teks yang dirancang untuk memberikan jawaban cepat dan akurat terhadap pertanyaan umum (Frequently Asked Questions). Chatbot ini dibangun sebagai Produk Minimum yang Layak (MVP) sesuai dengan dokumen PRD-MVP-5, dengan fokus pada penyediaan informasi yang telah dikurasi tanpa memerlukan personalisasi atau riwayat percakapan lintas sesi. Tujuannya adalah untuk memberikan fondasi yang kuat bagi pengembangan fitur chatbot yang lebih canggih di masa depan.

## Fitur Utama
- **Antarmuka Percakapan Teks:** Pengguna dapat berinteraksi dengan chatbot melalui antarmuka web yang sederhana dan responsif.
- **Basis Pengetahuan FAQ:** Menjawab lebih dari 20 pertanyaan umum yang telah ditentukan, mencakup topik seperti informasi perusahaan, layanan, kebijakan, dan dukungan teknis.
- **Penanganan Percakapan Dasar:** Mampu merespons sapaan (salam), ucapan terima kasih, dan permintaan bantuan.
- **Fallback Cerdas:** Memberikan respons yang sopan dan membantu ketika pertanyaan pengguna tidak dikenali, serta menyarankan untuk menghubungi dukungan jika diperlukan.
- **Pencatatan (Logging):** Mencatat kategori (tag) dari setiap pertanyaan yang berhasil dikenali untuk analisis konten di masa depan. Interaksi yang tidak dikenali juga dicatat untuk perbaikan.
- **Stateless:** Setiap pertanyaan diproses secara independen tanpa menyimpan riwayat percakapan, sesuai dengan prinsip privasi dan kesederhanaan MVP.

## Teknologi yang Digunakan
- **Bahasa:** Python 3
- **Kerangka Kerja/Library:**
  - **Flask:** Sebagai kerangka kerja web untuk menyediakan antarmuka API dan web.
  - **Standard Libraries:** `json` (untuk mengelola basis pengetahuan), `re` (untuk pencocokan pola), `logging` (untuk pencatatan).
- **Frontend:** HTML5, CSS3, JavaScript (untuk antarmuka chat).

## Instalasi
Untuk menjalankan proyek ini di lingkungan lokal, ikuti langkah-langkah berikut:

1.  **Clone Repositori:**
    ```bash
    git clone <URL_REPOSITORI_ANDA>
    cd <NAMA_DIREKTORI_PROYEK>
    ```

2.  **Buat dan Aktifkan Virtual Environment (Direkomendasikan):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Di Windows, gunakan `venv\Scripts\activate`
    ```

3.  **Instal Ketergantungan (Dependencies):**
    Proyek ini menggunakan Flask. Instal dengan pip:
    ```bash
    pip install Flask
    ```

## Penggunaan
Setelah instalasi selesai, Anda dapat menjalankan aplikasi chatbot dengan perintah berikut dari direktori utama proyek:

```bash
python3 app.py
```
Aplikasi akan berjalan di `http://127.0.0.1:5001`. Buka alamat ini di browser Anda untuk mulai berinteraksi dengan chatbot.

Log interaksi akan disimpan dalam file `chat_log.log` di direktori utama.

## Kontribusi
Kami menyambut baik kontribusi dari siapa saja. Jika Anda ingin berkontribusi, silakan ikuti pedoman berikut:
1.  **Fork** repositori ini.
2.  Buat **branch** baru untuk fitur atau perbaikan Anda (`git checkout -b nama-fitur-anda`).
3.  **Commit** perubahan Anda (`git commit -m 'Menambahkan fitur X'`).
4.  **Push** ke branch Anda (`git push origin nama-fitur-anda`).
5.  Buka **Pull Request**.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT.
