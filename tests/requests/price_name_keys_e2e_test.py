import json
import unittest
from io import BytesIO

from tests.requests.request_test_helper import RequestTestHelper


class PriceNameKeysTest(RequestTestHelper):
    def setUp(self):
        super().setUp()
        self.file = None
        self.price_ok_name_ok = [
            {
                "date": "2024-12-05 14:45:57",
                "searched_term": "A Light in the Attic",
                "sku": "SA0812",
                "ean": "7891112005969",
                "custom_terms": {},
                "product": "A Light in the Attic",
                "link": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
                "platform": "Valid Test",
                "seller": "Olist",
                "price": 51.77
            }
        ]
        self.price_ok_name_not_ok = [
            {
                "date": "2024-12-05 14:45:57",
                "searched_term": "A Light in the Attic",
                "sku": "SA0812",
                "ean": "7891112005969",
                "custom_terms": {},
                "name_product": "A Light in the Attic",
                "link": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
                "platform": "Valid Test",
                "seller": "Olist",
                "price_pix": 51.77
            }
        ]
        self.price_not_ok_name_not_ok = [
            {
                "date": "2024-12-05 14:45:57",
                "searched_term": "A Light in the Attic",
                "sku": "SA0812",
                "ean": "7891112005969",
                "custom_terms": {},
                "name_product": "A Light in the Attic",
                "link": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
                "platform": "Valid Test",
                "seller": "Olist",
                "price_debit": 51.77
            }
        ]
        self.price_not_ok_name_ok = [
            {
                "date": "2024-12-05 14:45:57",
                "searched_term": "A Light in the Attic",
                "sku": "SA0812",
                "ean": "7891112005969",
                "custom_terms": {},
                "product_name": "A Light in the Attic",
                "link": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
                "platform": "Valid Test",
                "seller": "Olist",
                "price_debit": 51.77
            }
        ]

    def write_json_content(self, content: list):
        file_content = json.dumps(content).encode('utf-8')  # Convert to bytes
        self.file = ("file", ("file.json", BytesIO(file_content), "application/json"))

    def perform_request_with_mocked_file(self, case: list, lines: int = 20):
        self.write_json_content(case)
        return self.client.post(
            "/validate",
            files={"file": self.file[1]},
            data={
                "lines": str(lines),  # Form data needs to be string
                "ean_key": "ean"
            }
        )

    def test_when_price_and_name_keys_are_ok(self):
        response = self.perform_request_with_mocked_file(self.price_ok_name_ok)
        self.assertEqual(200, response.status_code)
        self.assertNotIn("message", response.json())

    def test_when_price_key_is_ok_and_name_key_is_not_ok(self):
        response = self.perform_request_with_mocked_file(self.price_ok_name_not_ok)
        self.assertEqual(422, response.status_code)
        self.assertIn("message", response.json())
        self.assertEqual(
            response.json()["message"],
            "No valid key found in the sample data for product name")

    def test_when_price_key_is_not_ok_and_name_key_is_not_ok(self):
        response = self.perform_request_with_mocked_file(self.price_not_ok_name_not_ok)
        self.assertEqual(422, response.status_code)
        self.assertIn("message", response.json())
        self.assertEqual(
            response.json()["message"],
            "No valid key found in the sample data for product name")
        self.assertNotIn("price", response.json())

    def test_when_price_key_is_not_ok_and_name_key_is_ok(self):
        response = self.perform_request_with_mocked_file(self.price_not_ok_name_ok)
        self.assertEqual(422, response.status_code)
        self.assertIn("message", response.json())
        self.assertEqual(
            response.json()["message"],
            "No valid key found in the sample data for price")
        self.assertNotIn("product name", response.json())

    def tearDown(self):
        if self.file:
            self.file = None

if __name__ == '__main__':
    unittest.main()
