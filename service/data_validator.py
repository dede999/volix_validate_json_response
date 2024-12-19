
from datetime import datetime
from infrastucture.platform_factory import platform_factory
from infrastucture.result_tracker import ResultTracker
from infrastucture.validation_config import ValidationConfig


class DataValidator:
    def __init__(self, data: any, file_name: str, ean_key: str):
        self.time = datetime.now()
        self.data = data
        self.config = ValidationConfig(self.data[0], ean_key)
        self.client = self.config.get_client_name(file_name)
        self.platform_name = self.config.get_platform_name()
        self.tracker = ResultTracker()
        self.platform = platform_factory(self.platform_name)
        print(f"DataValidator initialized at {self.time.strftime('%d_%m_%Y')} for {self.client} on {self.platform_name}")

    async def test_runner(self) -> dict:
        for product in self.data:
            ean = product[self.config.ean_key]
            expected_price = product[self.config.price_key]
            product_name = product[self.config.name_key]
            result = await self.platform.request_content(product["link"])
            if "error" in result:
                self.tracker.add_error({
                    "ean": ean,
                    "product_name": product_name,
                    "price": expected_price,
                    "error": result["error"],
                    "link": product["link"]
                })
            else:
                name_match = result["title"].lower() == product_name.lower()
                price_match = result["price"] == expected_price
                data = {
                        "ean": ean,
                        "product_name": product_name,
                        "test_name": result["title"],
                        "price": expected_price,
                        "test_price": result["price"],
                        "link": product["link"]
                        }
                self.tracker.add_to_report(data, name_match, price_match)

        return self.tracker.print_report()
