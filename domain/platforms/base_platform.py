import ssl
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

    @staticmethod
    def set_ssl_context():
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context