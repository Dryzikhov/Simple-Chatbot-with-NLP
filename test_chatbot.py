import unittest
import json
from chatbot import initialize_application, get_faq_response

class TestFaqChatbot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Memuat knowledge base sekali untuk semua tes.
        Ini memastikan bahwa data pengujian konsisten dan efisien.
        """
        print("Menyiapkan data untuk pengujian...")
        cls.knowledge_base = initialize_application()
        if cls.knowledge_base is None:
            raise ValueError("Gagal memuat knowledge_base.json untuk pengujian.")

        # Ekstrak beberapa data untuk pengujian yang lebih mudah dibaca
        cls.greeting_responses = next(i['responses'] for i in cls.knowledge_base['intents'] if i['tag'] == 'greeting')
        cls.location_responses = next(i['responses'] for i in cls.knowledge_base['intents'] if i['tag'] == 'office_location')
        cls.fallback_responses = cls.knowledge_base['fallback_responses']

    def test_initialization(self):
        """Memastikan knowledge base berhasil dimuat dan tidak kosong."""
        self.assertIsNotNone(self.knowledge_base)
        self.assertIn("intents", self.knowledge_base)
        self.assertIn("fallback_responses", self.knowledge_base)
        self.assertTrue(len(self.knowledge_base["intents"]) > 10) # Memastikan FAQ sudah banyak

    def test_greeting_intent(self):
        """Menguji apakah input sapaan dikenali dengan benar."""
        user_input = "Halo, selamat pagi!"
        response = get_faq_response(user_input, self.knowledge_base)
        self.assertIn(response, self.greeting_responses)

    def test_specific_faq_intent(self):
        """Menguji pertanyaan FAQ spesifik (misalnya, lokasi)."""
        user_input = "Di mana alamat kantor Anda?"
        response = get_faq_response(user_input, self.knowledge_base)
        self.assertIn(response, self.location_responses)

    def test_case_insensitivity(self):
        """Menguji apakah pencocokan tidak sensitif terhadap huruf besar/kecil."""
        user_input = "SAYA MAU TANYA LOKASI KANTOR"
        response = get_faq_response(user_input, self.knowledge_base)
        self.assertIn(response, self.location_responses)

    def test_keyword_in_sentence(self):
        """Menguji apakah kata kunci dikenali meskipun berada di tengah kalimat."""
        user_input = "Boleh saya tahu di mana lokasi kantor pusat?"
        response = get_faq_response(user_input, self.knowledge_base)
        self.assertIn(response, self.location_responses)

    def test_fallback_response(self):
        """Menguji apakah respons fallback diberikan untuk input yang tidak dikenali."""
        # Input ini sengaja dibuat agar tidak mengandung kata kunci dari intent manapun
        user_input = "Apakah cuaca cerah hari ini di Pluto?"
        response = get_faq_response(user_input, self.knowledge_base)
        self.assertIn(response, self.fallback_responses)

    def test_partial_match_avoidance(self):
        """
        Menguji bahwa pola tidak cocok dengan bagian dari kata lain.
        Misalnya, 'harga' tidak boleh cocok dengan 'berharga'.
        """
        # "registrasi" ada di knowledge base, tapi "konsentrasi" seharusnya tidak memicunya.
        user_input = "Saya butuh konsentrasi penuh."
        response = get_faq_response(user_input, self.knowledge_base)
        self.assertIn(response, self.fallback_responses)

    def test_help_intent(self):
        """Menguji intent 'help' untuk memberikan panduan kepada pengguna."""
        user_input = "apa saja yang bisa kamu lakukan?"
        help_responses = next(i['responses'] for i in self.knowledge_base['intents'] if i['tag'] == 'help')
        response = get_faq_response(user_input, self.knowledge_base)
        self.assertIn(response, help_responses)

if __name__ == '__main__':
    # Menjalankan tes dengan output yang lebih detail (verbosity=2)
    unittest.main(verbosity=2)
