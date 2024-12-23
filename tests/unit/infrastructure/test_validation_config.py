import unittest
from unittest import TestCase

from infrastructure.validation_config import ValidationConfig
from infrastructure.exceptions.invalid_validation_key import InvalidValidationKey

class TestValidationConfig(TestCase):
    def test_ean_key_is_set_correctly(self):
        config = ValidationConfig({"product_name": "Test Product", "price": 100}, "1234567890123")
        self.assertEqual(config.ean_key, "1234567890123")

    def test_name_key_is_detected_correctly(self):
        config = ValidationConfig({"product_name": "Test Product", "price": 100}, "1234567890123")
        self.assertEqual(config.name_key, "product_name")

    def test_price_key_is_detected_correctly(self):
        config = ValidationConfig({"product_name": "Test Product", "price": 100}, "1234567890123")
        self.assertEqual(config.price_key, "price")

    def test_invalid_name_key_raises_exception(self):
        with self.assertRaises(InvalidValidationKey):
            ValidationConfig({"invalid_key": "Test Product", "price": 100}, "1234567890123")

    def test_invalid_price_key_raises_exception(self):
        with self.assertRaises(InvalidValidationKey):
            ValidationConfig({"product_name": "Test Product", "invalid_key": 100}, "1234567890123")

    def test_platform_name_is_extracted_correctly(self):
        config = ValidationConfig({"platform": "Amazon", "product_name": "Test Product", "price": 100}, "1234567890123")
        self.assertEqual(config.get_platform_name(), "Amazon")

    def test_client_name_is_extracted_correctly(self):
        self.assertEqual(ValidationConfig.get_client_name("client_file_2023.csv"), "client")

if __name__ == '__main__':
    unittest.main()