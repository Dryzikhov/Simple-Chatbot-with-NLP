import json
import random
import re
import logging

# Bagian 0: Konfigurasi Awal
def setup_logging():
    """Mengatur konfigurasi logging untuk menyimpan riwayat percakapan."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        filename='chat_log.txt',
        filemode='a' # 'a' untuk menambahkan, 'w' untuk menimpa
    )

# Bagian 1: Fungsi Inti dan Utilitas
def load_json_data(file_path: str) -> dict | list:
    """Memuat data dari file JSON dengan penanganan kesalahan yang kuat."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logging.error(f"JSON decode error in file: {file_path}")
    return None

def get_intent_and_entities(user_input: str) -> tuple[str | None, dict]:
    """
    Mengenali maksud (intent) dan mengekstrak entitas dari input pengguna
    menggunakan regular expressions yang lebih fleksibel.
    """
    user_input = user_input.lower()
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
            # Menggunakan regex untuk pencocokan yang lebih baik
            if re.search(r'\b' + re.escape(pattern.lower()) + r'\b', user_input):
                return random.choice(intent.get("responses", []))
    # Respons default jika tidak ada pola yang cocok
    return random.choice(knowledge_base.get("fallback_responses", ["Maaf, saya tidak mengerti. Bisakah Anda bertanya dengan cara lain?"]))

def is_exit_command(user_input: str) -> bool:
    """Memeriksa apakah pengguna ingin keluar."""
    exit_commands = ["exit", "quit", "selamat tinggal", "sampai jumpa", "keluar"]
    return user_input.lower() in exit_commands

# Bagian 2: Penanganan Fitur Spesifik
def handle_order_status(order_id: str, email: str, orders: list) -> str:
    """Memverifikasi dan mengembalikan status pesanan."""
    order = next((o for o in orders if o['order_id'] == order_id), None)
    if not order:
        return f"Maaf, pesanan dengan ID {order_id} tidak ditemukan."
    if order['customer_email'].lower() != email.lower():
        return "Verifikasi gagal. Email yang Anda berikan tidak cocok dengan data pesanan."
    return f"Status untuk pesanan {order_id} adalah: **{order['status']}**."

def handle_product_info(product_name: str, products: list) -> str:
    """Mencari dan mengembalikan informasi produk."""
    product = next((p for p in products if p['name'].lower() == product_name.lower()), None)
    if not product:
        return f"Maaf, produk dengan nama '{product_name}' tidak ditemukan."
    return (
        f"Berikut detail untuk **{product['name']}**:\n"
        f"- Deskripsi: {product['description']}\n"
        f"- Harga: Rp {product['price']:,}\n"
        f"- Stok: {product['stock']} unit"
    )

# Bagian 3: Logika Aplikasi Utama (Direfaktor untuk Web)
def initialize_application():
    """Menyiapkan semua komponen yang diperlukan untuk aplikasi."""
    setup_logging()
    knowledge_base = load_json_data('knowledge_base.json')
    orders = load_json_data('orders.json')
    products = load_json_data('products.json')
    if not all([knowledge_base, orders, products]):
        logging.critical("Inisialisasi Gagal: Satu atau lebih file data tidak dapat dimuat.")
        return None, None, None
    # Menambahkan respons fallback default jika tidak ada di JSON
    if "fallback_responses" not in knowledge_base:
        knowledge_base["fallback_responses"] = ["Maaf, saya tidak mengerti. Silakan coba pertanyaan lain."]
    return knowledge_base, orders, products

def get_chatbot_response(user_input: str, conversation_state: dict, kb: dict, orders: list, products: list) -> tuple[str, dict]:
    """
    Memproses input pengguna dan mengembalikan respons chatbot beserta state percakapan yang diperbarui.
    """
    logging.info(f"User: {user_input}")

    if is_exit_command(user_input):
        response = random.choice(next(i['responses'] for i in kb['intents'] if i['tag'] == 'goodbye'))
        conversation_state = {} # Reset state saat keluar
    elif conversation_state.get('awaiting_email_for_order'):
        order_id = conversation_state['awaiting_email_for_order']
        email_input = user_input
        response = handle_order_status(order_id, email_input, orders)
        conversation_state = {}  # Reset state setelah verifikasi
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

    logging.info(f"Bot: {response}")
    return response, conversation_state
