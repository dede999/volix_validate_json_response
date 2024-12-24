from unittest import TestCase

from parameterized import parameterized

from domain.platforms.dimensional_platform import DimensionalPlatform
from infrastructure.platform_factory import platform_factory
from infrastructure.exceptions.non_existing_platform import NonExistingPlatformException
from domain.platforms.amazon_platform import AmazonPlatform
from domain.platforms.carrefour_platform import CarrefourPlatform
from domain.platforms.mercado_livre_platform import MercadoLivrePlatform
from domain.platforms.magazine_luiza_platform import MagazineLuizaPlatform
from domain.platforms.valid_test_platform import ValidTestPlatform
from domain.platforms.andra_platform import AndraPlatform

class TestPlatformFactory(TestCase):
    @parameterized.expand([
        ("Andra", AndraPlatform),
        ("Amazon", AmazonPlatform),
        ("Carrefour", CarrefourPlatform),
        ("Dimensional", DimensionalPlatform),
        ("Mercado Livre", MercadoLivrePlatform),
        ("Magazine Luiza", MagazineLuizaPlatform),
        ("Valid Test", ValidTestPlatform)
    ])
    def test_platform_is_returned(self, platform_name, platform_class):
        self.assertIsInstance(platform_factory(platform_name), platform_class)

    def test_non_existing_platform_raises_exception(self):
        with self.assertRaises(NonExistingPlatformException):
            platform_factory("NonExisting")