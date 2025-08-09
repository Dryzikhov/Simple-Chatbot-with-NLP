import os
import logging
from flask import Flask, render_template, request, jsonify, session
import chatbot

# Konfigurasi logging dasar untuk melihat output di konsol
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Memulai eksekusi app.py")

app = Flask(__name__)
logging.info("Objek Flask berhasil dibuat")

# Kunci rahasia diperlukan untuk menggunakan sesi Flask
app.secret_key = os.urandom(24)
logging.info("Kunci rahasia Flask telah diatur")

knowledge_base, orders, products = None, None, None
try:
    logging.info("Mencoba menginisialisasi chatbot dan memuat data...")
    knowledge_base, orders, products = chatbot.initialize_application()
    if not all([knowledge_base, orders, products]):
        logging.error("Inisialisasi chatbot gagal: satu atau lebih file data tidak dapat dimuat.")
        raise RuntimeError("Gagal memuat data penting untuk chatbot.")
    logging.info("Inisialisasi chatbot dan pemuatan data berhasil.")
except Exception as e:
    logging.critical(f"Terjadi kesalahan fatal saat inisialisasi: {e}", exc_info=True)
    # Keluar jika inisialisasi gagal
    exit(1)

@app.route("/")
def index():
    """Menyajikan halaman utama antarmuka chat."""
    if 'conversation_state' not in session:
        session['conversation_state'] = {}
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    """Endpoint untuk menerima pesan pengguna dan mengembalikan respons chatbot."""
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Pesan tidak boleh kosong"}), 400

    conversation_state = session.get('conversation_state', {})

    response, updated_state = chatbot.get_chatbot_response(
        user_message,
        conversation_state,
        knowledge_base,
        orders,
        products
    )

    session['conversation_state'] = updated_state
    session.modified = True # Pastikan sesi disimpan

    return jsonify({"response": response})

if __name__ == "__main__":
    logging.info("Memulai server Flask...")
    # Menggunakan use_reloader=False untuk mencegah proses ganda dalam mode debug,
    # yang terkadang dapat menyebabkan masalah di beberapa lingkungan.
    app.run(host='0.0.0.0', port=5001, debug=True, use_reloader=False)
    logging.info("Server Flask telah berhenti.")
