from infrastructure.exceptions.invalid_validation_key import InvalidValidationKey


class ValidationConfig:
    def __init__(self, data_sample: dict, ean_key: str):
        self.sample = data_sample
        self.ean_key = ean_key
        self.sample_keys = list(self.sample.keys())
        self.name_key = self.detect_used_key(["product_name", "product"], "product name")
        self.price_key = self.detect_used_key(["price", "price_credit_card", "price_pix"], "price")

    def detect_used_key(self, valid_keys: list, context: str) -> str:
        for key in valid_keys:
            if key in self.sample_keys:
                return key

        raise InvalidValidationKey(context)

    def get_platform_name(self) -> str:
        return self.sample["platform"]

    @staticmethod
    def get_client_name(file_name: str) -> str:
        return file_name.split("_")[0].split("/")[-1]