# Proyek Chatbot Asisten Virtual

## Deskripsi
Proyek ini adalah implementasi dari asisten percakapan berbasis teks (chatbot) yang dirancang untuk membantu pengguna menemukan jawaban cepat atas pertanyaan umum (FAQ) dan melakukan tugas-tugas sederhana seperti melacak status pesanan atau mencari informasi produk. Chatbot ini dibangun dengan antarmuka web yang bersih dan responsif, serta didukung oleh backend Python yang ringan.

Tujuan utamanya adalah menyediakan solusi yang efisien untuk mengurangi beban tim layanan pelanggan dengan mengotomatiskan jawaban atas pertanyaan yang sering diajukan, sekaligus memberikan pengalaman pengguna yang mulus dan cepat.

## Fitur Utama
- **Tanya Jawab Umum (FAQ):** Menjawab berbagai pertanyaan umum berdasarkan basis pengetahuan (knowledge base) yang mudah diperbarui.
- **Pelacakan Status Pesanan:** Memungkinkan pengguna untuk memeriksa status pesanan mereka dengan aman melalui verifikasi email.
- **Pencarian Informasi Produk:** Memberikan detail produk, termasuk deskripsi, harga, dan jumlah stok.
- **Antarmuka Web Responsif:** Antarmuka chat yang bersih dan dapat diakses dengan baik di perangkat desktop maupun mobile.
- **Manajemen Konten Eksternal:** Seluruh data (FAQ, produk, pesanan) disimpan dalam format JSON, sehingga pembaruan konten tidak memerlukan perubahan kode.
- **Pencatatan Percakapan:** Menyimpan riwayat percakapan ke dalam file log untuk tujuan analisis dan peningkatan kualitas.

## Teknologi yang Digunakan
- **Bahasa:** Python
- **Kerangka Kerja/Library:**
  - **Flask:** Sebagai kerangka kerja web untuk membangun server dan API.
  - **Standard Libraries:** `json` (untuk memproses data), `re` (untuk pencocokan pola), `logging` (untuk mencatat riwayat).
- **Frontend:** HTML5, CSS3 (dengan Flexbox), JavaScript (dengan Fetch API).
- **Data:** File JSON sebagai basis data sederhana.

## Instalasi
Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah berikut:

1.  **Clone Repositori:**
    ```bash
    git clone <URL_REPOSITORI_ANDA>
    cd <NAMA_DIREKTORI_PROYEK>
    ```

2.  **Buat dan Aktifkan Virtual Environment (Direkomendasikan):**
    ```bash
    python -m venv venv
    # Windows
    venv\\Scripts\\activate
    # macOS / Linux
    source venv/bin/activate
    ```

3.  **Instal Dependensi:**
    Proyek ini hanya memerlukan Flask. Instal dari file `requirements.txt` (jika ada) atau langsung menggunakan pip.
    ```bash
    pip install Flask
    ```

## Penggunaan
Setelah instalasi selesai, Anda dapat menjalankan aplikasi dengan perintah berikut:

1.  **Jalankan Server Flask:**
    ```bash
    python app.py
    ```

2.  **Akses Aplikasi:**
    Buka browser web Anda dan navigasikan ke alamat berikut:
    ```
    http://127.0.0.1:5001
    ```

3.  **Contoh Interaksi:**
    Anda dapat mulai berinteraksi dengan chatbot. Coba beberapa perintah berikut:
    - `halo`
    - `jam operasional`
    - `info produk Laptop Pro`
    - `cek pesanan ORD759` (kemudian masukkan email `john.doe@example.com` saat diminta)

## Kontribusi
Kami menyambut baik kontribusi dari siapa pun. Jika Anda ingin berkontribusi, silakan ikuti pedoman berikut:
1.  **Fork** repositori ini.
2.  Buat **branch** baru untuk fitur atau perbaikan Anda (`git checkout -b fitur/nama-fitur`).
3.  **Commit** perubahan Anda (`git commit -m 'Menambahkan fitur X'`).
4.  **Push** ke branch Anda (`git push origin fitur/nama-fitur`).
5.  Buka **Pull Request**.

## Lisensi
Proyek ini dilisensikan di bawah **Lisensi MIT**.
