import ssl
from abc import abstractmethod
from fake_useragent import UserAgent


class BasePlatform:
    def __init__(self):
        print(f"{self.__class__.__name__} initialized")

    def get_headers(self) -> dict[str, str]:
        return {}
    
    def get_cookies(self) -> dict[str, str]:
        return {}
    
    def get_price(self) -> float:
        return 0.0

    def get_title(self) -> str:
        return ""

    @abstractmethod
    async def request_content(self, url: str):
        pass

    @staticmethod
    def set_ssl_context():
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context

    @staticmethod
    def create_random_user_agent():
        return UserAgent().random