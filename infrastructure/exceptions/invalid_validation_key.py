
class InvalidValidationKey(Exception):
    def __init__(self, context: str):
        self.message = f"No valid key found in the sample data for {context}"
        super().__init__(self.message)