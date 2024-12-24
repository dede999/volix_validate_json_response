from domain.platforms.beautiful_soup_platform import BeautifulSoupPlatform


class AndraDimensionalStrategy(BeautifulSoupPlatform):
    def get_title(self) -> str:
        return self.soup.find('h1').text

    def get_whole_price(self) -> str:
        return self.soup.find('span', class_='vtex-product-price-1-x-currencyInteger').text

    def get_fraction_price(self) -> str:
        return self.soup.find('span', class_='vtex-product-price-1-x-currencyFraction').text

    def get_price(self) -> float:
        try:
            price_whole = self.get_whole_price()
            price_fraction = self.get_fraction_price()
            return float(f"{price_whole}.{price_fraction}")
        except AttributeError:
            return 0.0
