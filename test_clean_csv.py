import csv
import tempfile
import unittest
import pytest
from clean_csv import parse_date, clean_csv
from pathlib import Path

from clean_csv import clean_csv, parse_date


class TestParseDate(unittest.TestCase):
    def test_iso_date(self):
        self.assertEqual(parse_date("2026-09-01"), "2026-09-01")

    def test_european_date(self):
        self.assertEqual(parse_date("01/09/2026"), "2026-09-01")

    def test_slash_date(self):
        self.assertEqual(parse_date("2026/09/03"), "2026-09-03")

    def test_invalid_date(self):
        self.assertEqual(parse_date("invalid"), "invalid")


class TestCleanCsv(unittest.TestCase):
    def test_removes_empty_and_duplicate_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            input_path = directory / "input.csv"
            output_path = directory / "output.csv"

            input_path.write_text(
                "name,email,signup_date,city\n"
                "Anna,anna@example.com,2026-09-01,Minsk\n"
                "Anna,anna@example.com,2026-09-01,Minsk\n"
                "\n"
                "Ivan,ivan@example.com,01/09/2026,Minsk\n",
                encoding="utf-8",
            )

            clean_csv(str(input_path), str(output_path))

            with output_path.open(
                "r",
                encoding="utf-8",
                newline="",
            ) as file:
                rows = list(csv.reader(file))

            expected_rows = [
                ["name", "email", "signup_date", "city"],
                ["Anna", "anna@example.com", "2026-09-01", "Minsk"],
                ["Ivan", "ivan@example.com", "2026-09-01", "Minsk"],
            ]

            self.assertEqual(rows, expected_rows)


if __name__ == "__main__":
    unittest.main()