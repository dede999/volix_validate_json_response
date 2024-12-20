from unittest import TestCase
from unittest.mock import patch

from domain.platforms.base_platform import BasePlatform


class TestBasePlatform(TestCase):
    def setUp(self):
        self.base_platform = BasePlatform()

    def test_get_headers(self):
        self.assertEqual(self.base_platform.get_headers(), {})

    def test_get_cookies(self):
        self.assertEqual(self.base_platform.get_cookies(), {})

    def test_get_price(self):
        self.assertEqual(self.base_platform.get_price(), 0.0)

    def test_get_title(self):
        self.assertEqual(self.base_platform.get_title(), "")

    @patch('ssl.create_default_context')
    def test_set_ssl_context(self, default_context_mock):
        self.assertEqual(self.base_platform.set_ssl_context(), default_context_mock.return_value)
        default_context_mock.assert_called_once()

    @patch('domain.platforms.base_platform.UserAgent')
    def test_create_random_user_agent(self, user_agent_mock):
        user_agent_mock.return_value.random = "random_user_agent"
        self.assertEqual(self.base_platform.create_random_user_agent(), "random_user_agent")
        user_agent_mock.assert_called_once()
