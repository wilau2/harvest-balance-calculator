import unittest
from datetime import datetime
from HarvestBalanceCalculator import WorkingPreference

config = {
    "workDaysOfTheWeek": [0, 1, 2],
    "hoursPerWorkDay": 7
}
working_preference = WorkingPreference(config)
a_monday = datetime(2016, 5, 2)
a_tuesday = datetime(2016, 5, 3)
a_wednesday = datetime(2016, 5, 4)
a_thursday = datetime(2016, 5, 5)
a_friday = datetime(2016, 5, 6)
a_saturday = datetime(2016, 5, 7)
a_sunday = datetime(2016, 5, 8)


class TestWorkingPreference(unittest.TestCase):
    def test_is_a_working_day_should_return_true(self):
        self.assertEqual(True, working_preference.is_a_working_day(a_monday))
        self.assertEqual(True, working_preference.is_a_working_day(a_tuesday))
        self.assertEqual(True, working_preference.is_a_working_day(a_wednesday))

    def test_is_a_working_day_should_return_false(self):
        self.assertEqual(False, working_preference.is_a_working_day(a_thursday))
        self.assertEqual(False, working_preference.is_a_working_day(a_friday))
        self.assertEqual(False, working_preference.is_a_working_day(a_saturday))
        self.assertEqual(False, working_preference.is_a_working_day(a_sunday))

    def test_get_hours_per_day(self):
        self.assertEqual(7, working_preference.hours_per_day)


if __name__ == '__main__':
    unittest.main()