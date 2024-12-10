from domain.platforms.base_platform import BasePlatform
from domain.platforms.carrefour_platform import CarrefourPlatform
from infrastucture.exceptions.non_existing_platform import NonExistingPlatformException


def platform_factory(platform: str) -> BasePlatform:
    platform_class = platform.replace(" ", "")
    platform_name = f"{platform_class}Platform"
    try:
        return globals()[platform_name]()
    except KeyError:
        raise NonExistingPlatformException(platform_name)
