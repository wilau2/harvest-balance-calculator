import unittest
from HarvestBalanceCalculator import WorkingTimeInterval

config = {
    "beginDate": "2016-5-2",
    "endDate": "2016-5-8",
    "workDaysOfTheWeek": [0, 1, 2],
    "hoursPerWorkDay": 7
}
working_time_interval = WorkingTimeInterval(config)


class TestWorkingTimeInterval(unittest.TestCase):
    def test_get_number_of_working_days(self):
        number_of_working_days = working_time_interval.get_number_of_working_days()
        self.assertEqual(3, number_of_working_days)

    def test_get_total_should_of_worked_time(self):
        total_should_of_worked_time = working_time_interval.get_total_should_of_worked_time()
        self.assertEqual(21, total_should_of_worked_time)


if __name__ == '__main__':
    unittest.main()
