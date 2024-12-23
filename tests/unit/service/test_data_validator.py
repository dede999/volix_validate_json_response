import unittest
from unittest.mock import MagicMock, patch, AsyncMock
from service.data_validator import DataValidator
from infrastructure.result_tracker import ResultTracker
from infrastructure.validation_config import ValidationConfig
from infrastructure.platform_factory import platform_factory


class TestDataValidator(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.data = [
            {
                "product_name": "Test Product",
                "price": 100, "link": "some_link", "ean_key": "ean",
                "client": "client", "platform": "Amazon",
            }]

    def test_data_validator_initializes_correctly(self):
        validator = DataValidator(self.data, "client_file_2023.csv", "ean_key")
        self.assertEqual(validator.client, "client")
        self.assertEqual(validator.platform_name, "Amazon")
        self.assertIsInstance(validator.tracker, ResultTracker)
        self.assertIsNotNone(validator.time)

    @patch('service.data_validator.platform_factory')
    @patch('service.data_validator.ResultTracker')
    @patch('service.data_validator.ValidationConfig')
    async def test_runner_processes_data_correctly(self, mock_validation_config, mock_result_tracker, mock_platform_factory):
        mock_config = mock_validation_config.return_value
        mock_config.ean_key = "ean_key"
        mock_config.price_key = "price"
        mock_config.name_key = "product_name"
        mock_config.get_client_name.return_value = "client"
        mock_config.get_platform_name.return_value = "Amazon"

        mock_tracker = MagicMock()
        mock_tracker.add_to_report.return_value = {}
        mock_tracker.print_report.return_value = {"full_match_count": 1}
        mock_result_tracker.return_value = mock_tracker
        mock_platform = AsyncMock()
        mock_platform_factory.return_value = mock_platform
        mock_platform.request_content.return_value = {"title": "Test Product", "price": 100}

        validator = DataValidator(self.data, "client_file_2023.csv", "ean_key")
        report = await validator.test_runner()

        mock_tracker.add_to_report.assert_called_once()
        mock_tracker.print_report.assert_called_once()
        self.assertEqual(report["full_match_count"], 1)

    @patch('service.data_validator.platform_factory')
    @patch('service.data_validator.ResultTracker')
    @patch('service.data_validator.ValidationConfig')
    async def test_runner_handles_errors_correctly(self, mock_validation_config, mock_result_tracker, mock_platform_factory):
        mock_config = mock_validation_config.return_value
        mock_config.ean_key = "ean_key"
        mock_config.price_key = "price"
        mock_config.name_key = "product_name"
        mock_config.get_client_name.return_value = "client"
        mock_config.get_platform_name.return_value = "Amazon"

        mock_tracker = MagicMock()
        mock_result_tracker.return_value = mock_tracker
        mock_tracker.print_report.return_value = {"error_count": 1}
        mock_platform = AsyncMock()
        mock_platform_factory.return_value = mock_platform
        mock_platform.request_content.return_value = {"error": "some error"}

        validator = DataValidator(self.data, "client_file_2023.csv", "ean_key")
        report = await validator.test_runner()

        mock_tracker.add_error.assert_called_once()
        self.assertEqual(report["error_count"], 1)