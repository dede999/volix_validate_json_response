import unittest
from unittest.mock import MagicMock, patch, AsyncMock
from service.data_validator import DataValidator
from infrastructure.result_tracker import ResultTracker
from infrastructure.validation_config import ValidationConfig


class TestDataValidator(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.sample = {
            "product_name": "Test Product",
            "price": 100,
            "link": "some_link.com.br", "ean_key": "ean",
            "platform": "Amazon",
        }
        self.data = [self.sample]
        self.config = ValidationConfig(self.sample, "ean_key", "client_file_2023.csv")

    def test_data_validator_initializes_correctly(self):
        validator = DataValidator(self.data, self.config)
        self.assertEqual(validator.config.client, "client")
        self.assertEqual(validator.config.platform_name, "Amazon")
        self.assertIsInstance(validator.tracker, ResultTracker)
        self.assertIsNotNone(validator.time)

    @patch('service.data_validator.ResultTracker')
    async def test_runner_processes_data_correctly(self, mock_result_tracker):
        mock_tracker = MagicMock()
        mock_tracker.add_to_report.return_value = {}
        mock_tracker.print_report.return_value = {"full_match_count": 1}
        mock_result_tracker.return_value = mock_tracker
        mock_request_content = AsyncMock()
        self.config.platform.request_content = mock_request_content
        mock_request_content.return_value = {"title": "Test Product", "price": 100}

        validator = DataValidator(self.data, self.config)
        report = await validator.test_runner()

        mock_tracker.add_to_report.assert_called_once()
        mock_tracker.print_report.assert_called_once()
        mock_request_content.assert_awaited_once_with(self.sample.get("link"))
        self.assertEqual(report["full_match_count"], 1)

    @patch('service.data_validator.ResultTracker')
    async def test_runner_handles_errors_correctly(self, mock_result_tracker):
        mock_tracker = MagicMock()
        mock_result_tracker.return_value = mock_tracker
        mock_tracker.print_report.return_value = {"error_count": 1}
        mock_request_content = AsyncMock()
        self.config.platform.request_content = mock_request_content
        mock_request_content.return_value = {"error": "some error"}

        validator = DataValidator(self.data, self.config)
        report = await validator.test_runner()

        mock_tracker.add_error.assert_called_once()
        mock_request_content.assert_awaited_once_with(self.sample.get("link"))
        self.assertEqual(report["error_count"], 1)