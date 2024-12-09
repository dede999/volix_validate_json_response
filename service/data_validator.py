
from datetime import datetime


class DataValidator:
    def __init__(self, data, file_name):
        self.time = datetime.now()
        self.data = data
        self.client = file_name.split("_")[0].split("/")[-1]
        self.platform = ""
        self.get_platform()
        print(f"DataValidator initialized at {self.time} for {self.client} on {self.platform}")

    def get_platform(self):
        if len(self.data) > 0:
            self.platform = self.data[0]["platform"].replace(" ", "")
