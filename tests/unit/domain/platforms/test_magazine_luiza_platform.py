import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from domain.platforms.magazine_luiza_platform import MagazineLuizaPlatform

class TestMagazineLuizaPlatform(TestCase):
    def setUp(self):
        self.platform = MagazineLuizaPlatform()
        self.driver_wait = MagicMock()
        self.platform.driver_wait = self.driver_wait

    def test_price_is_extracted_correctly(self):
        self.driver_wait.until = MagicMock(return_value=MagicMock(text="R$ 1.234,56"))
        self.assertEqual(self.platform.get_price(), 1234.56)
        self.driver_wait.until.assert_called_once()

    def test_price_with_letters_is_cleaned(self):
        self.driver_wait.until = MagicMock(return_value=MagicMock(text="R$ 1.234,56abc"))
        self.assertEqual(self.platform.get_price(), 1234.56)
        self.driver_wait.until.assert_called_once()

    def test_title_is_extracted_correctly(self):
        self.driver_wait.until = MagicMock(return_value=MagicMock(text="Product Title"))
        self.assertEqual(self.platform.get_title(), "Product Title")
        self.driver_wait.until.assert_called_once()

    def test_price_element_not_found_raises_exception(self):
        self.driver_wait.until = MagicMock(side_effect=Exception("Element not found"))
        with self.assertRaises(Exception):
            self.platform.get_price()
        self.driver_wait.until.assert_called_once()

    def test_title_element_not_found_raises_exception(self):
        self.driver_wait.until = MagicMock(side_effect=Exception("Element not found"))
        with self.assertRaises(Exception):
            self.platform.get_title()
        self.driver_wait.until.assert_called_once()

if __name__ == "__main__":
    unittest.main()