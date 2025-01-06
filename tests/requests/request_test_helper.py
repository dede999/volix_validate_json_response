import os
from typing import Any
from unittest import TestCase
from fastapi.testclient import TestClient
import main  # Ensure this imports your FastAPI app correctly

class RequestTestHelper(TestCase):
    def setUp(self):
        self.client = TestClient(main.app)  # Assuming your FastAPI app is named 'app'
        self.file = None
        self.case = ""

    def open_file(self):
        file_path = os.path.join("tests", "fixtures", f"client_{self.case}_2024_12_16_09.json")
        absolute_path = os.path.abspath(file_path)
        print(f"File path: {absolute_path}")

        # Ensure the file exists
        self.assertTrue(os.path.exists(absolute_path), f"File not found: {absolute_path}")

        self.file = open(absolute_path, "rb")
        return {
            "file": (f"client_{self.case}_2024_12_16_09.json", self.file, "application/json")
        }

    def perform_request(self, lines: int = 20):
        files = self.open_file()
        return self.client.post(
            f"/validate",
            files=files, data={"ean_key": "ean"})

    def tearDown(self):
        # Ensure file is closed if it was opened
        if self.file:
            self.file.close()
            self.file = None
