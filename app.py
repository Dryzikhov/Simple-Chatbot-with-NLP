import logging
from flask import Flask, render_template, request, jsonify
import chatbot

# Mengatur logging dasar untuk output konsol.
# Ini akan membantu dalam proses debug selama pengembangan.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Memulai aplikasi Flask...")

app = Flask(__name__)
logging.info("Objek Flask berhasil dibuat.")

# Inisialisasi chatbot saat aplikasi dimulai.
# Ini adalah pendekatan yang lebih bersih dan lebih aman.
knowledge_base = None
try:
    logging.info("Menginisialisasi chatbot...")
    # Memuat knowledge base yang akan digunakan oleh semua permintaan.
    knowledge_base = chatbot.initialize_application()
    if knowledge_base is None:
        # Jika knowledge base gagal dimuat, hentikan aplikasi.
        logging.critical("Aplikasi berhenti karena inisialisasi chatbot gagal.")
        raise RuntimeError("Gagal memuat knowledge base. Aplikasi tidak dapat berjalan.")
    logging.info("Inisialisasi chatbot berhasil.")
except Exception as e:
    logging.critical(f"Terjadi kesalahan fatal saat inisialisasi: {e}", exc_info=True)
    # Menghentikan server jika terjadi kesalahan kritis saat setup.
    exit(1)

@app.route("/")
def index():
    """Menyajikan halaman utama antarmuka chat yang statis."""
    # Tidak perlu lagi manajemen sesi, halaman cukup dirender.
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    """
    Endpoint untuk menerima pesan pengguna dan mengembalikan respons dari chatbot.
    Versi yang disederhanakan dan stateless.
    """
    user_message = request.json.get("message")
    if not user_message:
        # Validasi input dasar.
        return jsonify({"error": "Pesan tidak boleh kosong."}), 400

    # Memanggil fungsi chatbot yang telah direfaktor.
    # Tidak ada lagi status percakapan (conversation_state) atau data tambahan.
    response = chatbot.get_chatbot_response(user_message, knowledge_base)

    # Mengembalikan respons dalam format JSON.
    return jsonify({"response": response})

if __name__ == "__main__":
    # Menjalankan server Flask.
    # 'debug=True' berguna untuk pengembangan, tetapi harus dimatikan di produksi.
    # 'use_reloader=False' dapat membantu menghindari masalah inisialisasi ganda.
    logging.info("Memulai server Flask untuk pengembangan...")
    app.run(host='0.0.0.0', port=5001, debug=True, use_reloader=False)
    logging.info("Server Flask telah berhenti.")
