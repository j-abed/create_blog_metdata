import unittest
from datetime import datetime
import random

class TestDateParsing(unittest.TestCase):
    def setUp(self):
        self.formats = [
            "%b %d %Y",
            "%B %d %Y",
            "%B %d, %Y",
            "%b %d, %Y",
            "%d %B %Y",
            "%m/%d/%y",
            "%m/%d/%Y",
        ]

    def generate_random_date(self):
        year = random.randint(2000, 2030)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # To avoid invalid dates
        return datetime(year, month, day)

    def test_random_dates(self):
        for _ in range(100):  # Test 100 random dates
            dt = self.generate_random_date()
            for fmt in self.formats:
                try:
                    date_str = dt.strftime(fmt)
                    parsed = None
                    for test_fmt in self.formats:
                        try:
                            parsed = datetime.strptime(date_str, test_fmt)
                            break
                        except ValueError:
                            continue
                    self.assertIsNotNone(parsed, f"Failed to parse: {date_str} with format {fmt}")
                    self.assertEqual(parsed.strftime("%b %d, %Y"), dt.strftime("%b %d, %Y"))
                    print(f"Parsed '{date_str}' using '{test_fmt}' -> '{parsed.strftime('%b %d, %Y')}'")
                except Exception as e:
                    self.fail(f"Exception for date {dt} and format {fmt}: {e}")

if __name__ == "__main__":
    #unittest.main()
    unittest.main(verbosity=2)