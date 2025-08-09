# Chatbot Sederhana dengan NLP

## Deskripsi
Proyek ini adalah sebuah bot percakapan (chatbot) sederhana yang dirancang untuk memahami dan merespons pertanyaan umum dari pengguna. Chatbot ini dibangun sebagai Produk Minimum yang Layak (MVP) untuk memvalidasi konsep interaksi berbasis teks menggunakan Pemrosesan Bahasa Alami (NLP) tingkat dasar. Tujuannya adalah untuk memberikan respons yang cepat dan otomatis terhadap pertanyaan yang sering diajukan, sehingga meningkatkan efisiensi dan pengalaman pengguna.

## Fitur Utama
- **Pemahaman Pertanyaan Dasar**: Mampu mengidentifikasi maksud dari pertanyaan pengguna berdasarkan pola kata kunci.
- **Respons Berbasis Teks**: Memberikan jawaban yang relevan dan informatif dari basis pengetahuan yang telah ditentukan.
- **Penanganan Salam & Perpisahan**: Dapat mengenali dan merespons sapaan umum (misalnya, "Halo", "Selamat Pagi") dan ucapan perpisahan.
- **Basis Pengetahuan**: Menggunakan file JSON (`knowledge_base.json`) sebagai sumber jawaban untuk pertanyaan seputar:
    - Jam operasional
    - Cara mereset kata sandi
    - Pengecekan status pesanan

## Teknologi yang Digunakan
- **Bahasa:** Python 3
- **Kerangka Kerja/Library:** Hanya menggunakan pustaka standar Python (`json`, `random`).
- **Database:** JSON (untuk menyimpan basis pengetahuan).

## Instalasi
Tidak ada dependensi eksternal yang perlu diinstal. Anda hanya memerlukan interpreter Python 3.

1.  Clone repositori ini atau unduh file-filenya ke direktori lokal Anda.
    ```bash
    git clone <URL_REPOSITORI_ANDA>
    cd <NAMA_DIREKTORI>
    ```
2.  Pastikan Anda memiliki file `chatbot.py` dan `knowledge_base.json` di direktori yang sama.

## Penggunaan
Untuk menjalankan chatbot, buka terminal atau command prompt, navigasikan ke direktori proyek, dan jalankan perintah berikut:
```bash
python chatbot.py
```
Setelah itu, chatbot akan diinisialisasi dan Anda dapat mulai mengetik pertanyaan Anda di konsol. Untuk keluar dari program, ketik `exit`, `quit`, atau `selamat tinggal`.

**Contoh Interaksi:**
```
Anda: halo
Bot: Halo! Ada yang bisa saya bantu?
Anda: jam buka toko?
Bot: Toko kami buka dari jam 9 pagi hingga 9 malam, setiap hari Senin sampai Jumat.
Anda: terima kasih
Bot: Dengan senang hati!
Anda: sampai jumpa
Bot: Senang bisa membantu. Selamat tinggal!
```

## Kontribusi
Kontribusi untuk proyek ini sangat diharapkan. Jika Anda ingin berkontribusi, silakan ikuti langkah-langkah berikut:
1.  Fork repositori ini.
2.  Buat branch baru untuk fitur Anda (`git checkout -b fitur/NamaFitur`).
3.  Commit perubahan Anda (`git commit -m 'Menambahkan Fitur X'`).
4.  Push ke branch Anda (`git push origin fitur/NamaFitur`).
5.  Buka Pull Request.

## Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT.
