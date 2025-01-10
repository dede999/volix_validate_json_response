
from datetime import datetime
from infrastructure.result_tracker import ResultTracker
from infrastructure.validation_config import ValidationConfig


class DataValidator:
    def __init__(self, data: any, config: ValidationConfig):
        self.time = datetime.now()
        self.data = data
        self.config = config
        self.tracker = ResultTracker()
        print(f"DataValidator initialized at {self.time.strftime('%d_%m_%Y')} for {self.config.client} on {self.config.platform_name}")

    async def test_runner(self) -> dict:
        for product in self.data:
            ean = product[self.config.ean_key]
            expected_price = product[self.config.price_key]
            product_name = product[self.config.name_key]
            result = await self.config.platform.request_content(product["link"])
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
