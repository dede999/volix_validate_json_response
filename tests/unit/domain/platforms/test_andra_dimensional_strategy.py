from unittest.mock import MagicMock

from domain.platforms.andra_dimensional_strategy import AndraDimensionalStrategy
from tests.unit.domain.platforms.bs_platform_test_helper import BsPlatformTestHelper


class TestAndraDimensionalStrategy(BsPlatformTestHelper):
    def setUp(self) -> None:
        super().setUp()
        self.platform = AndraDimensionalStrategy()
        self.platform.soup = self.soup

    def test_get_title(self):
        self.soup.find.return_value.text = 'Sample Title'
        self.assertEqual(self.platform.get_title(), 'Sample Title')

    def test_get_whole_price(self):
        self.soup.find.return_value.text = '123'
        self.assertEqual(self.platform.get_whole_price(), '123')

    def test_get_fraction_price(self):
        self.soup.find.return_value.text = '45'
        self.assertEqual(self.platform.get_fraction_price(), '45')

    def test_get_price(self):
        self.soup.find.side_effect = [MagicMock(text='123'), MagicMock(text='45')]
        self.assertEqual(self.platform.get_price(), 123.45)

        self.soup.find.side_effect = AttributeError
        self.assertEqual(self.platform.get_price(), 0.0)
