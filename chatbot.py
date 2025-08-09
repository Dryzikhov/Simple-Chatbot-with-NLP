import json
import random

# Bagian 1: Fungsi Inti dan Utilitas

def load_knowledge_base(file_path: str) -> dict:
    """
    Memuat basis pengetahuan dari file JSON.
    Fungsi ini menangani kasus di mana file tidak ditemukan atau format JSON tidak valid,
    untuk mencegah program berhenti secara tak terduga.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        # Validasi dasar untuk memastikan 'intents' ada
        if "intents" not in data:
            print(f"Error: Kunci 'intents' tidak ditemukan dalam '{file_path}'.")
            return {"intents": []}
        return data
    except FileNotFoundError:
        print(f"Error: Berkas basis pengetahuan '{file_path}' tidak ditemukan.")
        return {"intents": []}
    except json.JSONDecodeError:
        print(f"Error: Gagal mem-parsing JSON dari '{file_path}'. Pastikan formatnya valid.")
        return {"intents": []}

def get_response(user_input: str, knowledge_base: dict) -> str:
    """
    Mencari respons yang paling sesuai dari basis pengetahuan berdasarkan input pengguna.
    Logika pencocokan ini bersifat case-insensitive untuk fleksibilitas.
    """
    # Normalisasi input pengguna ke huruf kecil untuk pencocokan yang konsisten
    user_input = user_input.lower()

    # Iterasi melalui setiap 'intent' dalam basis pengetahuan
    for intent in knowledge_base.get("intents", []):
        # Periksa apakah salah satu 'pattern' cocok dengan input pengguna
        for pattern in intent.get("patterns", []):
            if pattern.lower() in user_input:
                # Jika cocok, kembalikan salah satu respons secara acak
                return random.choice(intent.get("responses", []))

    # Jika tidak ada pola yang cocok, kembalikan respons default
    return "Maaf, saya tidak mengerti pertanyaan Anda. Bisakah Anda mencoba bertanya dengan cara lain?"

def is_exit_command(user_input: str, knowledge_base: dict) -> bool:
    """
    Memeriksa apakah input pengguna merupakan perintah untuk mengakhiri percakapan.
    """
    exit_commands = ["exit", "quit", "selamat tinggal", "sampai jumpa"]
    # Periksa apakah input ada dalam daftar perintah keluar umum
    if user_input.lower() in exit_commands:
        return True

    # Periksa juga pola dalam intent 'goodbye'
    for intent in knowledge_base.get("intents", []):
        if intent.get("tag") == "goodbye":
            if user_input.lower() in [p.lower() for p in intent.get("patterns", [])]:
                return True
    return False

# Bagian 2: Logika Aplikasi Utama

def initialize_application():
    """
    Menyiapkan semua komponen yang diperlukan untuk aplikasi,
    terutama memuat basis pengetahuan.
    """
    print("Menginisialisasi chatbot...")
    knowledge_base = load_knowledge_base('knowledge_base.json')
    if not knowledge_base.get("intents"):
        print("Inisialisasi gagal: Basis pengetahuan kosong atau tidak valid.")
        return None
    print("Chatbot berhasil diinisialisasi.")
    return knowledge_base

def run_core_logic(knowledge_base: dict):
    """
    Menjalankan loop interaksi utama dengan pengguna.
    """
    print("\nChatbot siap! Ketik pertanyaan Anda atau 'exit' untuk keluar.")

    while True:
        try:
            # Menerima input dari pengguna
            user_input = input("Anda: ")

            # Memeriksa apakah pengguna ingin keluar
            if is_exit_command(user_input, knowledge_base):
                response = get_response("selamat tinggal", knowledge_base)
                print(f"Bot: {response}")
                break

            # Mendapatkan dan menampilkan respons dari chatbot
            response = get_response(user_input, knowledge_base)
            print(f"Bot: {response}")

        except (KeyboardInterrupt, EOFError):
            # Menangani interupsi (Ctrl+C atau Ctrl+D) dengan anggun
            print("\n\nBot: Sesi diakhiri. Sampai jumpa lagi!")
            break

# Bagian 3: Titik Masuk Program

def main():
    """
    Fungsi utama untuk memulai eksekusi program.
    """
    # Langkah 1: Inisialisasi aplikasi
    knowledge_base = initialize_application()

    # Langkah 2: Jalankan logika inti jika inisialisasi berhasil
    if knowledge_base:
        run_core_logic(knowledge_base)

if __name__ == "__main__":
    main()
