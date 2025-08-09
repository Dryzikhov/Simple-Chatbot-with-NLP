import json
import random

def load_knowledge_base(file_path: str) -> dict:
    """
    Memuat basis pengetahuan dari file JSON dengan penanganan kesalahan.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: Berkas '{file_path}' tidak ditemukan. Chatbot tidak dapat memulai.")
        return {"intents": []}
    except json.JSONDecodeError:
        print(f"Error: Gagal mem-parsing JSON dari '{file_path}'. Pastikan formatnya valid.")
        return {"intents": []}

def get_response(user_input: str, knowledge_base: dict) -> str:
    """
    Mencari respons dari basis pengetahuan berdasarkan input pengguna.
    Menggunakan pencocokan kata kunci sederhana dan case-insensitive.
    """
    user_input = user_input.lower()

    for intent in knowledge_base.get("intents", []):
        for pattern in intent.get("patterns", []):
            if pattern.lower() in user_input:
                # Mengembalikan salah satu respons secara acak dari intent yang cocok
                return random.choice(intent.get("responses", []))

    # Respons default jika tidak ada intent yang cocok
    return "Maaf, saya tidak mengerti pertanyaan Anda. Bisakah Anda mencoba bertanya dengan cara lain?"

def chat():
    """
    Fungsi utama untuk menjalankan loop chat di CLI.
    """
    knowledge_base = load_knowledge_base('knowledge_base.json')

    if not knowledge_base.get("intents"):
        print("Basis pengetahuan kosong atau gagal dimuat. Program berhenti.")
        return

    print("Chatbot siap! Ketik 'exit' atau 'selamat tinggal' untuk keluar.")

    while True:
        try:
            user_input = input("Anda: ")
            # Periksa apakah input adalah perintah untuk keluar
            if user_input.lower() in ["exit", "quit", "selamat tinggal", "sampai jumpa"]:
                # Cari respons perpisahan dari basis pengetahuan
                goodbye_response = "Sampai jumpa!"  # Default fallback
                for intent in knowledge_base.get("intents", []):
                    if intent.get("tag") == "goodbye":
                        goodbye_response = random.choice(intent.get("responses", []))
                        break
                print(f"Bot: {goodbye_response}")
                break

            response = get_response(user_input, knowledge_base)
            print(f"Bot: {response}")

        except (KeyboardInterrupt, EOFError):
            # Tangani Ctrl+C atau Ctrl+D dengan anggun
            print("\nBot: Sampai jumpa lagi!")
            break

if __name__ == "__main__":
    chat()
