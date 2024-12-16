from domain.platforms.beautiful_soup_platform import BeautifulSoupPlatform


class ValidTestPlatform(BeautifulSoupPlatform):
    def get_title(self) -> str:
        return self.soup.find('h1').text

    def get_price(self) -> float:
        return float(self.soup.find('p', class_='price_color').text[1:])