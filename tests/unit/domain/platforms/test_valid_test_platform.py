from domain.platforms.valid_test_platform import ValidTestPlatform
from tests.unit.domain.platforms.bs_platform_test_helper import BsPlatformTestHelper


class TestValidTestPlatform(BsPlatformTestHelper):
    def setUp(self) -> None:
        super().setUp()
        self.platform = ValidTestPlatform()
        self.platform.soup = self.soup

    def test_get_title(self):
        self.soup.find.return_value.text = 'Title'
        self.assertEqual('Title', self.platform.get_title())
        self.soup.find.assert_called_once_with('h1')

    def test_get_price(self):
        self.soup.find.return_value.text = '£134.56'
        self.assertEqual(134.56, self.platform.get_price())
        self.soup.find.assert_called_once_with('p', class_='price_color')
