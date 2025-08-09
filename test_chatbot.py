import unittest
import json
from chatbot import (
    load_json_data,
    get_intent_and_entities,
    handle_order_status,
    handle_product_info,
    get_fallback_response
)

class TestChatbotFeatures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Memuat semua data yang diperlukan sekali untuk semua tes."""
        cls.knowledge_base = load_json_data('knowledge_base.json')
        cls.orders = load_json_data('orders.json')
        cls.products = load_json_data('products.json')

        if not all([cls.knowledge_base, cls.orders, cls.products]):
            raise ValueError("Gagal memuat satu atau lebih file data untuk pengujian.")

    def test_get_intent_and_entities(self):
        """Menguji pengenalan maksud (intent) dan ekstraksi entitas."""
        test_cases = {
            "status pesanan ORD759": ("check_order", {'order_id': 'ORD759'}),
            "lacak order ORD321": ("check_order", {'order_id': 'ORD321'}),
            "info produk Laptop Pro": ("find_product", {'product_name': 'laptop pro'}),
            "detail barang Mouse Gaming": ("find_product", {'product_name': 'mouse gaming'}),
            "halo, apa kabar?": (None, {}),
            "terima kasih banyak": (None, {})
        }

        for text, (expected_intent, expected_entities) in test_cases.items():
            with self.subTest(text=text):
                intent, entities = get_intent_and_entities(text)
                self.assertEqual(intent, expected_intent)
                self.assertEqual(entities, expected_entities)

    def test_handle_order_status(self):
        """Menguji logika penanganan status pesanan."""
        # Kasus sukses
        response = handle_order_status("ORD759", "john.doe@example.com", self.orders)
        self.assertIn("Status untuk pesanan ORD759 adalah: **Sedang Diproses**.", response)

        # Kasus verifikasi gagal
        response = handle_order_status("ORD321", "wrong.email@example.com", self.orders)
        self.assertIn("Verifikasi gagal.", response)

        # Kasus pesanan tidak ditemukan
        response = handle_order_status("ORD999", "any@email.com", self.orders)
        self.assertIn("tidak ditemukan", response)

    def test_handle_product_info(self):
        """Menguji logika penanganan informasi produk."""
        # Kasus sukses
        response = handle_product_info("Laptop Pro", self.products)
        self.assertIn("Berikut detail untuk **Laptop Pro**", response)
        self.assertIn("Harga: Rp 21,500,000", response)
        self.assertIn("Stok: 35 unit", response)

        # Kasus produk tidak ditemukan
        response = handle_product_info("Produk Impian", self.products)
        self.assertIn("tidak ditemukan", response)

        # Kasus sensitivitas huruf (case-insensitivity)
        response_lower = handle_product_info("keyboard mekanikal", self.products)
        self.assertIn("Berikut detail untuk **Keyboard Mekanikal**", response_lower)

    def test_get_fallback_response(self):
        """Menguji respons fallback untuk pertanyaan umum."""
        # Kasus sapaan
        response = get_fallback_response("halo", self.knowledge_base)
        self.assertIn(response, self.knowledge_base['intents'][0]['responses'])

        # Kasus tidak dikenal
        response = get_fallback_response("apakah pizza itu enak?", self.knowledge_base)
        self.assertIn("Maaf, saya tidak mengerti.", response)

if __name__ == '__main__':
    unittest.main(verbosity=2)
