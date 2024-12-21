from unittest import TestCase
from infrastructure.result_tracker import ResultTracker

class TestResultTracker(TestCase):
    def test_report_is_generated_correctly(self):
        tracker = ResultTracker()
        tracker.add_to_report({"item": "A"}, True, True)
        tracker.add_to_report({"item": "B"}, False, True)
        tracker.add_to_report({"item": "C"}, True, False)
        tracker.add_to_report({"item": "D"}, False, False)
        tracker.add_error({"error": "E"})
        report = tracker.print_report()
        self.assertEqual(report["full_match_count"], 1)
        self.assertEqual(report["name_fail_count"], 1)
        self.assertEqual(report["price_fail_count"], 1)
        self.assertEqual(report["both_fail_count"], 1)
        self.assertEqual(report["error_count"], 1)
        self.assertEqual(report["total_count"], 5)

    def test_report_is_empty_initially(self):
        tracker = ResultTracker()
        report = tracker.print_report()
        self.assertEqual(report["full_match_count"], 0)
        self.assertEqual(report["name_fail_count"], 0)
        self.assertEqual(report["price_fail_count"], 0)
        self.assertEqual(report["both_fail_count"], 0)
        self.assertEqual(report["error_count"], 0)
        self.assertEqual(report["total_count"], 0)

    def test_error_is_added_correctly(self):
        tracker = ResultTracker()
        tracker.add_error({"error": "E"})
        self.assertEqual(tracker.errors, [{"error": "E"}])

    def test_report_level_is_set_correctly(self):
        self.assertEqual(ResultTracker._set_report_level(True, True), 0)
        self.assertEqual(ResultTracker._set_report_level(False, True), 1)
        self.assertEqual(ResultTracker._set_report_level(True, False), 2)
        self.assertEqual(ResultTracker._set_report_level(False, False), 3)