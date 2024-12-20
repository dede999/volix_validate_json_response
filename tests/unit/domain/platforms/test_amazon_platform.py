from unittest.mock import MagicMock

from domain.platforms.amazon_platform import AmazonPlatform
from tests.unit.domain.platforms.bs_platform_test_helper import BsPlatformTestHelper


class TestAmazonPlatform(BsPlatformTestHelper):
    def setUp(self) -> None:
        super().setUp()
        self.platform = AmazonPlatform()
        self.platform.soup = self.soup

    def test_get_title(self):
        self.soup.find.return_value.text = 'Title '
        self.assertEqual('Title', self.platform.get_title())
        self.soup.find.assert_called_once_with('span', id='productTitle')

    def test_get_price(self):
        self.soup.find.side_effect = [
            MagicMock(text='1,234'),
            MagicMock(text='56')
        ]
        self.assertEqual(1234.56, self.platform.get_price())
        self.soup.find.assert_any_call('span', class_='a-price-whole')
        self.soup.find.assert_any_call('span', class_='a-price-fraction')

    def test_get_price_handles_missing_whole_price(self):
        self.soup.find.side_effect = [
            None,
            MagicMock(text='56')
        ]
        result = self.platform.get_price()
        self.assertEqual(result, 0.0)

    def test_get_price_handles_missing_fraction_price(self):
        self.soup.find.side_effect = [
            MagicMock(text='1,234'),
            None
        ]
        result = self.platform.get_price()
        self.assertEqual(result, 0.0)

    def test_get_price_handles_missing_both_prices(self):
        self.soup.find.side_effect = [None, None]
        result = self.platform.get_price()
        self.assertEqual(result, 0.0)