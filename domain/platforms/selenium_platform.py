from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from domain.platforms.base_platform import BasePlatform


class SeleniumPlatform(BasePlatform):
    VALIDATION_INSTANCES = 20

    def __init__(self):
        super().__init__()
        self.driver_wait = None

    async def request_content(self, url: str):
        # Configurações do Firefox para evitar detecção de bot
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.set_preference("general.useragent.override", self.create_random_user_agent())

        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)

        try:
            driver.get(url)

            self.driver_wait = WebDriverWait(driver, 10)
            product_name = self.get_title()
            price = self.get_price()

            driver.quit()
            return {"title": product_name, "price": price}

        except Exception as e:
            print(f"Erro durante o scraping: {e}")
            driver.quit()
            return {"error": str(e)}