import unittest
from datetime import datetime

from HarvestBalanceCalculator.Utils import get_number_of_weeks_between_dates


class TestTimeUtils(unittest.TestCase):
    def test_get_number_of_weeks_between_dates_when_one_week_difference(self):
        begin_date = datetime(2017, 1, 1)  # week 1
        end_date = datetime(2017, 1, 2)  # week 2
        expected_result = 1
        self.assertEqual(expected_result, get_number_of_weeks_between_dates(begin_date, end_date))

    def test_get_number_of_weeks_between_dates_when_same_dates(self):
        begin_date = datetime(2017, 1, 1)  # week 1
        end_date = datetime(2017, 1, 1)  # week 2
        expected_result = 0
        self.assertEqual(expected_result, get_number_of_weeks_between_dates(begin_date, end_date))


if __name__ == '__main__':
    unittest.main()
