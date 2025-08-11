import json
import random
import re
import logging

def setup_logging():
    """Mengatur konfigurasi logging untuk menyimpan riwayat percakapan."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='chat_log.log',
        filemode='a'
    )

def load_json_data(file_path: str) -> dict:
    """Memuat data dari file JSON dengan penanganan kesalahan yang kuat."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Kesalahan: File tidak ditemukan di '{file_path}'")
    except json.JSONDecodeError:
        logging.error(f"Kesalahan: Gagal mendekode JSON dari '{file_path}'")
    return None

def get_faq_response(user_input: str, knowledge_base: dict) -> str:
    """
    Mencari respons yang cocok dari knowledge base berdasarkan input pengguna.
    Pencocokan ini memeriksa apakah semua kata dalam sebuah pola ada di input pengguna.
    """
    user_input_lower = user_input.lower()

    # Mencari kecocokan intent berdasarkan pola
    for intent_data in knowledge_base.get("intents", []):
        for pattern in intent_data.get("patterns", []):
            pattern_words = pattern.lower().split()
            # Memeriksa apakah semua kata dari pola ada di dalam input pengguna
            all_words_found = all(re.search(r'\b' + re.escape(word) + r'\b', user_input_lower) for word in pattern_words)

            if all_words_found:
                # Mencatat kategori (tag) yang cocok untuk tujuan logging
                logging.info(f"Input '{user_input}' cocok dengan kategori: {intent_data.get('tag')}")
                return random.choice(intent_data.get("responses", []))

    # Jika tidak ada pola yang cocok, catat sebagai 'unrecognized'
    logging.info(f"Input '{user_input}' tidak dikenali (fallback).")

    # Memberikan respons fallback default
    fallback_responses = knowledge_base.get("fallback_responses",
                                            ["Maaf, saya tidak mengerti. Bisakah Anda bertanya dengan cara lain?"])
    return random.choice(fallback_responses)

def initialize_application():
    """
    Menyiapkan semua komponen yang diperlukan untuk aplikasi chatbot.
    Hanya memuat knowledge base.
    """
    setup_logging()
    knowledge_base = load_json_data('knowledge_base.json')

    if not knowledge_base:
        logging.critical("Inisialisasi Gagal: File 'knowledge_base.json' tidak dapat dimuat.")
        return None

    # Memastikan ada respons fallback default
    if "fallback_responses" not in knowledge_base:
        knowledge_base["fallback_responses"] = ["Maaf, saya tidak mengerti. Silakan coba pertanyaan lain."]

    logging.info("Aplikasi chatbot berhasil diinisialisasi.")
    return knowledge_base

def get_chatbot_response(user_input: str, kb: dict) -> str:
    """
    Memproses input pengguna dan mengembalikan respons chatbot.
    Versi yang disederhanakan tanpa status percakapan.
    """
    # Langsung memanggil fungsi pencarian FAQ
    response = get_faq_response(user_input, kb)

    # Mencatat interaksi untuk tujuan debug
    logging.info(f"User: \"{user_input}\" | Bot: \"{response}\"")

    return response
