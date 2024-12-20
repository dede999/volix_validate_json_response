from random import uniform, randint
from unittest import TestCase
from unittest.mock import patch, MagicMock
from domain.platforms.selenium_platform import SeleniumPlatform

class TestSeleniumPlatform(TestCase):
    @patch('domain.platforms.selenium_platform.webdriver.Firefox')
    @patch('domain.platforms.selenium_platform.WebDriverWait')
    @patch('domain.platforms.selenium_platform.GeckoDriverManager')
    async def test_request_content_returns_title_and_price(self, mock_gecko_driver_manager, mock_web_driver_wait, mock_firefox):
        mock_driver = MagicMock()
        mock_firefox.return_value = mock_driver
        mock_driver.get.return_value = None
        mock_driver.quit.return_value = None

        random_price = uniform(50.0, 150.0)
        random_product_title = f"Test Title {randint(1, 1000)}"

        platform = SeleniumPlatform()
        platform.get_title = MagicMock(return_value=random_product_title)
        platform.get_price = MagicMock(return_value=random_price)

        result = await platform.request_content("http://example.com")
        self.assertEqual(result, {"title": random_product_title, "price": random_price })

    @patch('domain.platforms.selenium_platform.webdriver.Firefox')
    @patch('domain.platforms.selenium_platform.WebDriverWait')
    @patch('domain.platforms.selenium_platform.GeckoDriverManager')
    async def test_request_content_handles_exceptions(self, mock_gecko_driver_manager, mock_web_driver_wait, mock_firefox):
        mock_driver = MagicMock()
        mock_firefox.return_value = mock_driver
        mock_driver.get.side_effect = Exception("Test Exception")
        mock_driver.quit.return_value = None

        platform = SeleniumPlatform()

        result = await platform.request_content("http://example.com")
        self.assertEqual(result, {"error": "Test Exception"})
