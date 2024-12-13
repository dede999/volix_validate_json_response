import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from domain.platforms.selenium_platform import SeleniumPlatform

class MagazineLuizaPlatform(SeleniumPlatform):
    def get_price(self) -> float:
        price_element = self.driver_wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p[data-testid='price-value']")))
        price_text = price_element.text.replace("R$", "").replace(".", "").replace(",", ".")
        return float(re.sub(r"[a-zA-Z]", "", price_text))

    def get_title(self) -> str:
        title_element = self.driver_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        return title_element.text
