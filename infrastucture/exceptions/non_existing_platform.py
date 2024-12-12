
class NonExistingPlatformException(Exception):
    def __init__(self, searched_platform: str):
        super().__init__(f"There is no implemented platform for {searched_platform}")
