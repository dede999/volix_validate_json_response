from random import randint, uniform
from unittest import IsolatedAsyncioTestCase
from unittest.mock import patch, MagicMock, AsyncMock

from domain.platforms.beautiful_soup_platform import BeautifulSoupPlatform

class TestBeautifulSoupPlatform(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.beautiful_soup_platform = BeautifulSoupPlatform()
        self.beautiful_soup_platform.get_title = MagicMock(return_value=f"Product Title {randint(1, 100)}")
        self.beautiful_soup_platform.get_price = MagicMock(return_value=uniform(50.0, 150.0))

    @patch('domain.platforms.base_platform.ssl.create_default_context')
    @patch('domain.platforms.beautiful_soup_platform.BeautifulSoup')
    @patch('domain.platforms.beautiful_soup_platform.ClientSession')
    async def test_request_content_returns_title_and_price(
            self, mock_client_session, mock_beautiful_soup, mock_ssl_context):
        cm_session = MagicMock()
        session_mock = MagicMock()
        session_mock.get = MagicMock()
        get_session = MagicMock()
        response_mock = MagicMock()
        response_mock.status = 200
        response_mock.text = AsyncMock()
        response_mock.text\
            .return_value = "<html><head><title>Test Title</title></head><body><div class='price'>100.0</div></body></html>"

        cm_session.__aenter__.return_value = session_mock
        session_mock.get.return_value = get_session
        get_session.__aenter__.return_value = response_mock
        mock_client_session.return_value = cm_session

        result = await self.beautiful_soup_platform.request_content("http://example.com")
        self.assertEqual(result, {
            "title": self.beautiful_soup_platform.get_title.return_value,
            "price": self.beautiful_soup_platform.get_price.return_value
        })
        mock_client_session.assert_called_once()
        mock_ssl_context.assert_called_once()
        session_mock.get.assert_called_once_with(
            "http://example.com", headers={}, cookies={}, ssl=mock_ssl_context.return_value)
        response_mock.text.assert_awaited_once()
        mock_beautiful_soup.assert_called_once_with(response_mock.text.return_value, 'html.parser')

    @patch('domain.platforms.base_platform.ssl.create_default_context')
    @patch('domain.platforms.beautiful_soup_platform.ClientSession')
    async def test_request_content_handles_non_200_status(self, mock_client_session, mock_ssl_context):
        cm_session = MagicMock()
        session_mock = MagicMock()
        session_mock.get = MagicMock()
        get_session = MagicMock()
        response_mock = MagicMock()
        response_mock.text = AsyncMock()
        response_mock.status = 404
        response_mock.reason = "Not Found"

        cm_session.__aenter__.return_value = session_mock
        session_mock.get.return_value = get_session
        get_session.__aenter__.return_value = response_mock
        mock_client_session.return_value = cm_session

        result = await self.beautiful_soup_platform.request_content("http://example.com")
        self.assertEqual(result, {"error": "Error 404 - Not Found"})
        mock_client_session.assert_called_once()
        session_mock.get.assert_called_once_with(
            "http://example.com", headers={}, cookies={}, ssl=mock_ssl_context.return_value)
        response_mock.text.assert_not_awaited()

    @patch('domain.platforms.base_platform.ssl.create_default_context')
    @patch('domain.platforms.beautiful_soup_platform.ClientSession')
    async def test_request_content_handles_exceptions(self, mock_client_session, mock_ssl_context):
        cm_session = MagicMock()
        session_mock = MagicMock()
        session_mock.get.side_effect = Exception("Test Exception")

        cm_session.__aenter__.return_value = session_mock
        mock_client_session.return_value = cm_session

        result = await self.beautiful_soup_platform.request_content("http://example.com")
        self.assertEqual(result, {"error": "Test Exception"})
        mock_client_session.assert_called_once()
        session_mock.get.assert_called_once_with(
            "http://example.com", headers={}, cookies={}, ssl=mock_ssl_context.return_value)
        session_mock.get.assert_called_once()