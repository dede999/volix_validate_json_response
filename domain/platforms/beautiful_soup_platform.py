from aiohttp import ClientSession
from bs4 import BeautifulSoup

from domain.platforms.base_platform import BasePlatform


class BeautifulSoupPlatform(BasePlatform):
    VALIDATION_INSTANCES = 50

    def __init__(self):
        super().__init__()
        self.soup = None

    async def request_content(self, url: str):
        async with ClientSession() as session:
            try:
                async with session.get(
                        url,
                        headers=self.get_headers(),
                        cookies=self.get_cookies(),
                        ssl=self.set_ssl_context()
                ) as response:
                    if response.status != 200:
                        return { 'error': f"Error {response.status} - {response.reason}" }

                    html = await response.text()
                    self.soup = BeautifulSoup(html, 'html.parser')
                    title = self.get_title()
                    price = self.get_price()

                    return { "title": title, "price": price }

            except Exception as e:
                return { 'error': str(e) }
