
from datetime import datetime

from infrastucture.platform_factory import platform_factory
from infrastucture.result_tracker import ResultTracker


class DataValidator:
    def __init__(self, data, file_name):
        self.time = datetime.now()
        self.data = data
        self.client = file_name.split("_")[0].split("/")[-1]
        self.platform_name = ""
        self.get_platform()
        self.tracker = ResultTracker()
        self.platform = platform_factory(self.platform_name)
        print(f"DataValidator initialized at {self.time.strftime('%d_%m_%Y')} for {self.client} on {self.platform_name}")

    def get_platform(self):
        if len(self.data) > 0:
            self.platform_name = self.data[0]["platform"]
            
    def snake_case_platform(self):
        return self.platform_name.lower().replace(" ", "_")

    def print_file_content(self, line):
        with open(f"output/{self.time.strftime('%d_%m_%Y_%H_%M')}_{self.client}_{self.snake_case_platform()}.csv", 'a', encoding='utf-8') as file:
            file.write(line)
            
    async def test_runner(self) -> dict:
        self.print_file_content(
            "Ean\tProdName\tTestProdName\tNameMatch\tPrice\tTestPrice\tPriceMatch\tBothMatch\tLinkUrl\n")
        for product in self.data:
            result = await self.platform.request_content(product["link"])
            if "error" not in result:
                ean = product["ean"]
                expected_price = product["price_credit_card"]
                product_name = product["product_name"]
                name_match = result["title"] == product_name
                price_match = result["price"] == expected_price
                both_match = name_match and price_match
                data = {
                        "ean": ean,
                        "product_name": product_name,
                        "test_name": result["title"],
                        "price": expected_price,
                        "test_price": result["price"],
                        "link": product["link"]
                        }
                self.tracker.add_to_report(data, name_match, price_match)
                line = f"{ean}\t{product_name}\t{result['title']}\t{name_match}\t{expected_price}\t{result['price']}\t{price_match}\t{both_match}\t{product['link']}\n"
                self.print_file_content(line)
        
        return self.tracker.print_report()
