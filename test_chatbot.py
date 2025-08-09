import unittest
import json
from chatbot import get_response, load_knowledge_base

class TestChatbot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load the knowledge base once for all tests."""
        cls.knowledge_base = load_knowledge_base('knowledge_base.json')
        # Ensure knowledge base is loaded correctly
        if not cls.knowledge_base or not cls.knowledge_base.get("intents"):
            raise ValueError("Failed to load or parse the knowledge base for testing.")

    def get_expected_responses_by_tag(self, tag: str) -> list[str]:
        """Helper function to find all possible responses for a given intent tag."""
        for intent in self.knowledge_base.get("intents", []):
            if intent.get("tag") == tag:
                return intent.get("responses", [])
        return []

    def test_chatbot_responses(self):
        """
        Tests the chatbot's responses against a predefined set of questions.
        This test verifies that the bot provides a correct and relevant response
        for various intents defined in the knowledge base.
        """
        test_cases = [
            # Greeting Intent
            ("halo", "greeting"),
            ("selamat pagi", "greeting"),
            # Goodbye Intent
            ("sampai jumpa", "goodbye"),
            # Thanks Intent
            ("terima kasih", "thanks"),
            # Hours Intent
            ("jam operasional berapa?", "hours"),
            ("toko buka jam berapa", "hours"),
            # Password Intent
            ("bagaimana cara reset password?", "password"),
            ("lupa kata sandi", "password"),
            # Order Status Intent
            ("cek status pesanan saya", "order_status"),
            ("lacak pesanan", "order_status"),
        ]

        successful_responses = 0

        for user_input, expected_tag in test_cases:
            response = get_response(user_input, self.knowledge_base)
            expected_responses = self.get_expected_responses_by_tag(expected_tag)

            # Check if the response is one of the expected responses for that tag
            if response in expected_responses:
                successful_responses += 1
                print(f"PASS: Input='{user_input}', Tag='{expected_tag}'")
            else:
                print(f"FAIL: Input='{user_input}', Tag='{expected_tag}', Got='{response}'")

        # Verify acceptance criteria (80% success rate)
        total_cases = len(test_cases)
        success_rate = (successful_responses / total_cases)
        print(f"\nTest Summary:")
        print(f"Total Test Cases: {total_cases}")
        print(f"Successful Responses: {successful_responses}")
        print(f"Success Rate: {success_rate:.2%}")

        self.assertGreaterEqual(success_rate, 0.80, "Chatbot failed to meet the 80% success rate criterion.")

    def test_unknown_question(self):
        """
        Tests that the chatbot returns a default message for a question
        that does not match any intent.
        """
        user_input = "apakah bumi itu datar?"
        response = get_response(user_input, self.knowledge_base)
        expected_default_response = "Maaf, saya tidak mengerti pertanyaan Anda. Bisakah Anda mencoba bertanya dengan cara lain?"
        self.assertEqual(response, expected_default_response, "Chatbot should return the default message for unknown questions.")
        print(f"PASS: Unknown question test.")


if __name__ == '__main__':
    unittest.main()
