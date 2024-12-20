from unittest import TestCase
from unittest.mock import MagicMock

from domain.platforms.andra_platform import AndraPlatform
from tests.unit.domain.platforms.bs_platform_test_helper import BsPlatformTestHelper


class TestAndraPlatform(BsPlatformTestHelper):
    def setUp(self) -> None:
        super().setUp()
        self.platform = AndraPlatform()
        self.platform.soup = self.soup

    def test_get_title(self):
        self.soup.find.return_value.text = 'Sample Title'
        self.assertEqual(self.platform.get_title(), 'Sample Title')

    def test_get_whole_price(self):
        def test_get_title(self):
            self.soup.find.return_value.text = 'Sample Title'
            self.assertEqual(self.platform.get_title(), 'Sample Title')

    def test_get_fraction_price(self):
        self.soup.find.return_value.text = '45'
        platform = AndraPlatform()
        platform.soup = self.soup
        self.assertEqual(platform.get_fraction_price(), '45')

    def test_get_price(self):
        self.soup.find.side_effect = [MagicMock(text='123'), MagicMock(text='45')]
        self.assertEqual(self.platform.get_price(), 123.45)

        self.soup.find.side_effect = AttributeError
        self.assertEqual(self.platform.get_price(), 0.0)
