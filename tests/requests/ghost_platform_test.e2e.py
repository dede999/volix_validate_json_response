import unittest
from tests.requests.request_test_helper import RequestTestHelper


class GhostPlatformE2eTest(RequestTestHelper):
    def setUp(self):
        super().setUp()
        self.case = "ghost"

    def test_ghost_platform_request(self):
        response = self.perform_request()
        self.assertEqual(response.status_code, 400)
        error_message = response.json().get("message")
        self.assertIn("There is no implemented platform for Ghost Test", error_message)
        self.assertIn("Check if GhostTestPlatform is implemented in domain/platforms/ folder", error_message)

if __name__ == '__main__':
    unittest.main()