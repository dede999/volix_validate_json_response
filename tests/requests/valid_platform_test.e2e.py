import unittest

from tests.requests.request_test_helper import RequestTestHelper


class ValidTest(RequestTestHelper):
    def setUp(self):
        super().setUp()
        self.case = "valid"

    def test_valid_platform_request(self):
        response = self.perform_request()
        self.assertEqual(response.status_code, 200)
        result = response.json().get("result")
        self.assertEqual(len(result.get("full_match")), 1)
        self.assertEqual(len(result.get("name_fail")), 1)
        self.assertEqual(len(result.get("price_fail")), 1)
        self.assertEqual(len(result.get("both_fail")), 1)
        self.assertEqual(len(result.get("errors")), 1)
        self.assertEqual(result.get("full_match")[0].get("ean"), "7891112005969")
        self.assertEqual(result.get("name_fail")[0].get("ean"), "7891112005980")
        self.assertEqual(result.get("price_fail")[0].get("ean"), "7891112009101")
        self.assertEqual(result.get("both_fail")[0].get("ean"), "7891112005678")
        self.assertEqual(result.get("errors")[0].get("ean"), "7891112001234")

if __name__ == '__main__':
    unittest.main()
