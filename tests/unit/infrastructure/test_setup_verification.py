import unittest
from unittest.mock import MagicMock, patch
from infrastructure.setup_verification import SetupVerification

class TestSetupVerification(unittest.TestCase):
    def test_line_with_error_is_invalid(self):
        self.assertFalse(SetupVerification.line_is_valid({"error": "some error", "link": "some link"}))

    def test_line_without_error_is_valid(self):
        self.assertTrue(SetupVerification.line_is_valid({"link": "some link"}))

    def test_line_without_link_is_invalid(self):
        self.assertFalse(SetupVerification.line_is_valid({"error": "some error"}))

    def test_errors_are_filtered_out(self):
        json_content = [{"error": "some error", "link": "some link"}, {"link": "valid link"}]
        filtered = SetupVerification.filter_errors(json_content)
        self.assertEqual(filtered, [{"link": "valid link"}])

    def test_lines_are_selected_based_on_probability(self):
        json_content = [{"link": "link1"}, {"link": "link2"}, {"link": "link3"}]
        random_return = MagicMock()
        random_return.tolist.return_value = [0.1, 0.5, 0.9]
        with patch('numpy.random.rand', return_value=random_return):
            selected = SetupVerification.probabilistic_line_selection(json_content, 2)
            self.assertEqual(selected, [{"link": "link1"}, {"link": "link2"}])

if __name__ == '__main__':
    unittest.main()