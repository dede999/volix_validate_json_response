from unittest import TestCase
from unittest.mock import MagicMock


class BsPlatformTestHelper(TestCase):
    def setUp(self):
        self.soup = MagicMock()
        self.soup.find = MagicMock()
        self.soup.find_all = MagicMock()
