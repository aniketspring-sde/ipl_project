import csv
import unittest
from pathlib import Path


class TestFetchData(unittest.TestCase):

    TEST_DATA_DIR = Path(__file__).parent / "test_data"

    def fetch_deliveries_test(self):
        file_path = self.TEST_DATA_DIR / "deliveries_test.csv"

        with open(file_path, "r") as file:
            dt_rows = csv.DictReader(file)
            return list(dt_rows)

    def fetch_matches_test(self):
        file_path = self.TEST_DATA_DIR / "matches_test.csv"

        with open(file_path, "r") as file:
            mt_rows = csv.DictReader(file)
            return list(mt_rows)