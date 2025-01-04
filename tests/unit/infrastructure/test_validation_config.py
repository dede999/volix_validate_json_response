import unittest
from unittest import TestCase

from random import randrange, uniform, randint
from unittest.mock import patch

from domain.platforms.amazon_platform import AmazonPlatform
from infrastructure.validation_config import ValidationConfig
from infrastructure.exceptions.invalid_validation_key import InvalidValidationKey

class TestValidationConfig(TestCase):
    def setUp(self):
        self.sample = {
            "product_name": f"Test Product{randint(1, 10)}",
            "price": uniform(50.0, 150.0),
            "platform": "Amazon"
        }
        self.ean_key = str(randrange(10 ** 12, 10 ** 13)) # It has 13 chars
        self.file_name = "client_file_2023.json"

    def test_ean_key_is_set_correctly(self):
        config = ValidationConfig(self.sample, self.ean_key, self.file_name)
        self.assertEqual(config.ean_key, self.ean_key)

    def test_name_key_is_detected_correctly(self):
        config = ValidationConfig(self.sample, self.ean_key, self.file_name)
        self.assertEqual(config.name_key, "product_name")

    def test_price_key_is_detected_correctly(self):
        config = ValidationConfig(self.sample, self.ean_key, self.file_name)
        self.assertEqual(config.price_key, "price")

    def test_client_name_is_set_correctly(self):
        config = ValidationConfig(self.sample, self.ean_key, self.file_name)
        self.assertEqual(config.client, self.file_name.split("_")[0])

    def test_platform_name_is_set_correctly(self):
        config = ValidationConfig(self.sample, self.ean_key, self.file_name)
        self.assertEqual(config.platform_name, "Amazon")

    def test_platform_is_set_correctly(self):
        config = ValidationConfig(self.sample, self.ean_key, self.file_name)
        self.assertIsInstance(config.platform, AmazonPlatform)

    @patch("infrastructure.validation_config.ValidationConfig.get_platform_name")
    def test_invalid_name_key_raises_exception(self, mock_get_platform_name):
        mock_get_platform_name.return_value = "Amazon"
        with self.assertRaises(InvalidValidationKey):
            ValidationConfig({"invalid_key": "Test Product", "price": 100}, "1234567890123", self.file_name)

    @patch("infrastructure.validation_config.ValidationConfig.get_platform_name")
    def test_invalid_price_key_raises_exception(self, mock_get_platform_name):
        mock_get_platform_name.return_value = "Amazon"
        with self.assertRaises(InvalidValidationKey):
            ValidationConfig({"product_name": "Test Product", "invalid_key": 100}, "1234567890123", self.file_name)

    def test_platform_name_is_extracted_correctly(self):
        config = ValidationConfig(self.sample, self.ean_key, self.file_name)
        self.assertEqual(config.get_platform_name(), "Amazon")

    def test_client_name_is_extracted_correctly(self):
        self.assertEqual(ValidationConfig.get_client_name("client_file_2023.csv"), "client")

if __name__ == '__main__':
    unittest.main()