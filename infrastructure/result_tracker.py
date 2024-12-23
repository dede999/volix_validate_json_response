NAME_MATCH_BIT = 1
PRICE_MATCH_BIT = 2

class ResultTracker:
    def __init__(self):
        self._full_match = []
        self._name_fail = []
        self._price_fail = []
        self._both_fail = []
        self.errors = []
        self._reports = [
            self._full_match, self._name_fail, self._price_fail, self._both_fail
        ]

    def print_report(self):
        report = {}
        total = 0
        report_keys = ["full_match", "name_fail", "price_fail", "both_fail"]
        for i, key in enumerate(report_keys):
            report[key] = self._reports[i]
            report_count = len(self._reports[i])
            report[f"{key}_count"] = report_count
            total += report_count

        report["errors"] = self.errors
        report["error_count"] = len(self.errors)
        report["total_count"] = total + len(self.errors)
        return report

    def add_to_report(self, result: dict, name_match: bool, price_match: bool):
        report_type = self._set_report_level(name_match, price_match)
        self._reports[report_type].append(result)

    def add_error(self, error: dict):
        self.errors.append(error)

    @staticmethod
    def _set_report_level(name_match: bool, price_match: bool):
        level = 0
        if not name_match:
            level ^= NAME_MATCH_BIT

        if not price_match:
            level ^= PRICE_MATCH_BIT

        return level
