from domain.platforms.carrefour_platform import CarrefourPlatform
from unittest.mock import MagicMock
from tests.unit.domain.platforms.bs_platform_test_helper import BsPlatformTestHelper


class TestCarrefourPlatform(BsPlatformTestHelper):
    def setUp(self) -> None:
        super().setUp()
        self.platform = CarrefourPlatform()
        self.platform.soup = self.soup

    def test_get_headers(self):
        self.platform.create_random_user_agent = MagicMock(return_value="Mozilla/5.0")
        headers = self.platform.get_headers()
        self.assertEqual(headers['accept'], 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7')
        self.assertEqual(headers['user-agent'], 'Mozilla/5.0')
        self.assertEqual(
            list(headers.keys()),
            [
                'accept', 'accept-language', 'dnt', 'priority', 'referer', 'sec-ch-ua', 'sec-ch-ua-mobile',
                'sec-ch-ua-platform', 'sec-fetch-dest', 'sec-fetch-mode', 'sec-fetch-site', 'sec-fetch-user',
                'upgrade-insecure-requests', 'user-agent'])

    def test_get_cookies(self):
        cookies = self.platform.get_cookies()
        self.assertEqual(
            list(cookies.keys()),
            [
                '_gcl_au', '_ga', 'dtm_token_sc', 'dtm_token', '_cq_duid', '_fbp', '_tt_enable_cookie', '_ttp',
                '_rlid', 'analytic_id', 'AwinChannelCookie', '_clck', '__privaci_cookie_consent_uuid',
                '__privaci_cookie_consent_generated', '__rtbh.uid', 'device-id', 'session-id', '__cf_bm',
                '_cfuvid', '_gcl_gs', '__utmzz', '__utmzzses', '_ga_XSP6W5L7L1', '_gcl_aw', '_gcl_dc',
                '_cq_suid', '__rtbh.lid', '_clsk', '__privaci_cookie_no_action', '_ga_SHP4RTV3MH'])

    def test_get_title(self):
        self.platform.soup.find.return_value = MagicMock(text='Test Title')
        title = self.platform.get_title()
        self.assertEqual(title, 'Test Title')

    def test_get_price_returns_correct_price(self):
        self.soup.find_all.return_value = [MagicMock(text='"Value":1234.56')]
        price = self.platform.get_price()
        self.assertEqual(price, 1234.56)

    def test_get_price_handles_missing_price(self):
        self.soup.find_all.return_value = [MagicMock(text='')]
        price = self.platform.get_price()
        self.assertEqual(price, 0.0)