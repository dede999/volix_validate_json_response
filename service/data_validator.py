
from datetime import datetime

from infrastucture.platform_factory import platform_factory


class DataValidator:
    def __init__(self, data, file_name):
        self.time = datetime.now()
        self.data = data
        self.client = file_name.split("_")[0].split("/")[-1]
        self.platform_name = ""
        self.get_platform()
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