from unittest.mock import MagicMock

from domain.platforms.mercado_livre_platform import MercadoLivrePlatform
from tests.unit.domain.platforms.bs_platform_test_helper import BsPlatformTestHelper


class TestMercadoLivrePlatform(BsPlatformTestHelper):
    def setUp(self) -> None:
        super().setUp()
        self.platform = MercadoLivrePlatform()
        self.platform.soup = self.soup
        self.price_container = MagicMock()

    def test_get_headers(self):
        headers = self.platform.get_headers()
        self.assertEqual(
            list(headers.keys()),
            ['accept', 'accept-language', 'dnt', 'priority', 'referer', 'sec-ch-ua',
             'sec-ch-ua-mobile', 'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode',
             'sec-fetch-site', 'sec-fetch-user', 'upgrade-insecure-requests', 'user-agent'])

    def test_title_is_extracted_correctly(self):
        self.soup.find.return_value = MagicMock(text="Product Title")
        self.assertEqual(self.platform.get_title(), "Product Title")
        self.soup.find.assert_called_once_with('h1', class_='ui-pdp-title')

    def test_price_container_is_extracted_correctly(self):
        self.assertIsNotNone(self.platform.get_price_container())
        self.soup.find.assert_called_once_with('div', class_='ui-pdp-price__second-line')

    def test_whole_price_is_extracted_correctly(self):
        self.price_container.find.return_value = MagicMock(text="1.234")
        self.platform.get_price_container = MagicMock(return_value=self.price_container)
        self.assertEqual(self.platform.get_whole_price(), "1.234")

    def test_cents_price_is_extracted_correctly(self):
        self.price_container.find.return_value = MagicMock(text="56")
        self.platform.get_price_container = MagicMock(return_value=self.price_container)
        self.assertEqual(self.platform.get_cents_price(), "56")

    def test_cents_price_is_defaulted_when_not_found(self):
        self.price_container.find.side_effect = AttributeError
        self.platform.get_price_container = MagicMock(return_value=self.price_container)
        self.assertEqual(self.platform.get_cents_price(), "00")

    def test_price_is_calculated_correctly(self):
        self.platform.get_whole_price = MagicMock(return_value="1.234")
        self.platform.get_cents_price = MagicMock(return_value="56")
        self.assertEqual(self.platform.get_price(), 1234.56)

    def price_is_calculated_correctly_without_cents(self):
        self.platform.get_whole_price = MagicMock(return_value="1.234")
        self.platform.get_cents_price = MagicMock(return_value="00")
        self.assertEqual(self.platform.get_price(), 1234.00)
