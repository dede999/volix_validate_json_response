from webdriver_manager.firefox import GeckoDriverManager

from domain.platforms.base_platform import BasePlatform
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class MagazineLuizaPlatform(BasePlatform):
    def __init__(self):
        self.soup = None
        print("MagazineLuizaPlatform initialized")

    def get_headers(self) -> dict[str, str]:
        return {}

    def get_cookies(self) -> dict[str, str]:
        return {}

    async def request_content(self, url: str):
        # Configurações do Firefox para evitar detecção de bot
        firefox_options = Options()  # Use Firefox Options
        firefox_options.add_argument("--headless")
        firefox_options.set_preference("general.useragent.override", self.create_random_user_agent())

        # Inicializar o WebDriver do Firefox
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)

        try:
            driver.get(url)

            # Resto do código permanece igual
            wait = WebDriverWait(driver, 10)
            product_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text
            price_element = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "p[data-testid='price-value']")))
            price = price_element.text

            driver.quit()
            return {"title": product_name, "price": price}

        except Exception as e:
            print(f"Erro durante o scraping: {e}")
            driver.quit()
            return {"error": str(e)}