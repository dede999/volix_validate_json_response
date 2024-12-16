from domain.platforms.beautiful_soup_platform import BeautifulSoupPlatform


class AmazonPlatform(BeautifulSoupPlatform):
    def get_title(self) -> str:
        return self.soup.find('span', id='productTitle').text.strip()

    def get_price(self) -> float:
        try:
            price_whole = self.soup.find('span', class_='a-price-whole').text.replace(',', '')
            price_fraction = self.soup.find('span', class_='a-price-fraction').text
            return float(f"{price_whole}.{price_fraction}")
        except AttributeError:
            return 0.0
