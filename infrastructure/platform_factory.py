from domain.platforms.base_platform import BasePlatform
from domain.platforms.amazon_platform import AmazonPlatform
from domain.platforms.carrefour_platform import CarrefourPlatform
from domain.platforms.mercado_livre_platform import MercadoLivrePlatform
from domain.platforms.magazine_luiza_platform import MagazineLuizaPlatform
from domain.platforms.valid_test_platform import ValidTestPlatform
from domain.platforms.andra_platform import AndraPlatform
from domain.platforms.dimensional_platform import DimensionalPlatform
from infrastructure.exceptions.non_existing_platform import NonExistingPlatformException


def platform_factory(platform: str) -> BasePlatform:
    platform_class = platform.replace(" ", "")
    platform_name = f"{platform_class}Platform"
    try:
        return globals()[platform_name]()
    except KeyError:
        raise NonExistingPlatformException(platform, platform_name)
