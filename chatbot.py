import json
import random
import re
import logging

# Bagian 0: Konfigurasi Awal
def setup_logging():
    """Mengatur konfigurasi logging untuk menyimpan riwayat percakapan."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - User: %(message)s',
        filename='chat_log.txt',
        filemode='w' # 'w' untuk menimpa log setiap sesi baru, 'a' untuk menambahkan
    )

# Bagian 1: Fungsi Inti dan Utilitas
def load_json_data(file_path: str) -> dict | list:
    """Memuat data dari file JSON dengan penanganan kesalahan yang kuat."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Berkas '{file_path}' tidak ditemukan.")
        logging.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Gagal mem-parsing JSON dari '{file_path}'.")
        logging.error(f"JSON decode error in file: {file_path}")
    return None

def get_intent_and_entities(user_input: str) -> tuple[str | None, dict]:
    """
    Mengenali maksud (intent) dan mengekstrak entitas dari input pengguna
    menggunakan regular expressions yang lebih fleksibel.
    """
    user_input = user_input.lower()

    # Pola regex yang ditingkatkan untuk fleksibilitas
    patterns = {
        'check_order': r"(?:cek|status|lacak|track)\s(?:pesanan|order)\s(ORD\d+)",
        'find_product': r"(?:info|harga|stok|detail)\s(?:produk|barang)\s(.+)",
    }

    for intent, pattern in patterns.items():
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            if intent == 'check_order':
                return intent, {'order_id': match.group(1).upper()}
            elif intent == 'find_product':
                return intent, {'product_name': match.group(1).strip()}

    return None, {}

def get_fallback_response(user_input: str, knowledge_base: dict) -> str:
    """
    Memberikan respons dari knowledge base jika tidak ada intent spesifik yang cocok.
    """
    user_input = user_input.lower()
    for intent in knowledge_base.get("intents", []):
        for pattern in intent.get("patterns", []):
            if pattern.lower() in user_input:
                return random.choice(intent.get("responses", []))

    return "Maaf, saya tidak mengerti. Coba gunakan format seperti: 'status pesanan ORD123' atau 'info produk Laptop Pro'."

def is_exit_command(user_input: str, knowledge_base: dict) -> bool:
    """Memeriksa apakah pengguna ingin keluar."""
    exit_commands = ["exit", "quit", "selamat tinggal", "sampai jumpa", "keluar"]
    if user_input.lower() in exit_commands:
        return True
    return False

# Bagian 2: Penanganan Fitur Spesifik
def handle_order_status(order_id: str, email: str, orders: list) -> str:
    """Memverifikasi dan mengembalikan status pesanan."""
    # Cari pesanan berdasarkan ID
    order = next((o for o in orders if o['order_id'] == order_id), None)

    if not order:
        return f"Maaf, pesanan dengan ID {order_id} tidak ditemukan."

    # Verifikasi email
    if order['customer_email'].lower() != email.lower():
        return "Verifikasi gagal. Email yang Anda berikan tidak cocok dengan data pesanan."

    return f"Status untuk pesanan {order_id} adalah: **{order['status']}**."

def handle_product_info(product_name: str, products: list) -> str:
    """Mencari dan mengembalikan informasi produk."""
    # Cari produk (case-insensitive)
    product = next((p for p in products if p['name'].lower() == product_name.lower()), None)

    if not product:
        return f"Maaf, produk dengan nama '{product_name}' tidak ditemukan."

    # Format respons
    return (
        f"Berikut detail untuk **{product['name']}**:\n"
        f"- Deskripsi: {product['description']}\n"
        f"- Harga: Rp {product['price']:,}\n"
        f"- Stok: {product['stock']} unit"
    )

# Bagian 3: Logika Aplikasi Utama
def initialize_application():
    """Menyiapkan semua komponen yang diperlukan untuk aplikasi."""
    print("Menginisialisasi chatbot...")
    knowledge_base = load_json_data('knowledge_base.json')
    if not knowledge_base or "intents" not in knowledge_base:
        print("Inisialisasi gagal: Basis pengetahuan tidak valid.")
        return None, None, None

    orders = load_json_data('orders.json')
    products = load_json_data('products.json')

    if orders is None or products is None:
        print("Inisialisasi gagal: Data pesanan atau produk tidak dapat dimuat.")
        return None, None, None

    print("Chatbot berhasil diinisialisasi.")
    return knowledge_base, orders, products

def run_core_logic(kb: dict, orders: list, products: list):
    """Menjalankan loop interaksi utama dengan pengguna, dengan manajemen state."""
    print("\nChatbot siap! Ketik pertanyaan Anda atau 'exit' untuk keluar.")
    logging.info("Sesi chatbot dimulai.")

    conversation_state = {}

    while True:
        try:
            user_input = input("Anda: ")
            logging.getLogger().handlers[0].setFormatter(logging.Formatter('%(asctime)s - User: %(message)s'))
            logging.info(user_input)

            if is_exit_command(user_input, kb):
                response = get_fallback_response("selamat tinggal", kb)
                print(f"Bot: {response}")
                logging.getLogger().handlers[0].setFormatter(logging.Formatter('%(asctime)s - Bot: %(message)s'))
                logging.info(response)
                logging.info("Sesi chatbot berakhir.\n" + "="*50 + "\n")
                break

            # Logika State Machine untuk verifikasi email
            if conversation_state.get('awaiting_email_for_order'):
                order_id = conversation_state['awaiting_email_for_order']
                email_input = user_input
                response = handle_order_status(order_id, email_input, orders)
                conversation_state = {} # Reset state
            else:
                intent, entities = get_intent_and_entities(user_input)
                if intent == 'check_order':
                    order_id = entities['order_id']
                    conversation_state['awaiting_email_for_order'] = order_id
                    response = f"Tentu, untuk memverifikasi, silakan masukkan alamat email yang terkait dengan pesanan {order_id}."
                elif intent == 'find_product':
                    response = handle_product_info(entities['product_name'], products)
                else:
                    response = get_fallback_response(user_input, kb)

            print(f"Bot: {response}")
            logging.getLogger().handlers[0].setFormatter(logging.Formatter('%(asctime)s - Bot: %(message)s'))
            logging.info(response)

        except (KeyboardInterrupt, EOFError):
            print("\n\nBot: Sesi diakhiri. Sampai jumpa lagi!")
            logging.info("Sesi diakhiri oleh pengguna (Ctrl+C/D).")
            break

# Bagian 3: Titik Masuk Program
def main():
    """Fungsi utama untuk memulai eksekusi program."""
    setup_logging()
    kb, orders, products = initialize_application()

    if all((kb, orders, products)):
        run_core_logic(kb, orders, products)

if __name__ == "__main__":
    main()
