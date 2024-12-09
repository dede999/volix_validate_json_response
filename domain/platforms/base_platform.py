
from abc import abstractmethod
from typing import Any


class BasePlatform:
    @abstractmethod
    def get_headers(self) -> dict[str, str]:
        pass
    
    @abstractmethod
    def get_cookies(self) -> dict[str, str]:
        pass
    
    @abstractmethod
    async def request_content(self, url: str):
        pass
