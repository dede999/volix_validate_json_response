from domain.platforms.beautiful_soup_platform import BeautifulSoupPlatform


class MercadoLivrePlatform(BeautifulSoupPlatform):
    def get_headers(self) -> dict[str, str]:
        return {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'dnt': '1',
            'priority': 'u=0, i',
            'referer': 'https://www.mercadolivre.com.br/',
            'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': self.create_random_user_agent(),
        }

    def get_title(self):
        return self.soup.find('h1', class_='ui-pdp-title').text

    def get_price_container(self):
        return self.soup.find('div', class_='ui-pdp-price__second-line')

    def get_whole_price(self):
        return (self.get_price_container()
                .find('span', class_='andes-money-amount__fraction').text)

    def get_cents_price(self):
        try:
            return (self.get_price_container()
                    .find('span', class_='andes-money-amount__cents').text)
        except AttributeError:
            return '00'

    def get_price(self):
        whole = self.get_whole_price().replace('.', '')
        cents = self.get_cents_price()
        price = (100 * int(whole) + int(cents)) / 100
        return price
