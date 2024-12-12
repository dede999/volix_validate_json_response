
class NonExistingPlatformException(Exception):
    def __init__(self, searched_platform: str, platform_class_name: str):
        message = f"There is no implemented platform for {searched_platform}"
        tip1 = f"Check if {platform_class_name} is implemented in domain/platforms/ folder"
        tip2 = f"Check if the platform is imported in infrastructure/platform_factory.py"
        super().__init__(f"{message}. {tip1}. {tip2}")
