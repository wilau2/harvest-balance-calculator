import unittest
from HarvestBalanceCalculator import WorkingTimeInterval

config = {
    "period": {
        "begin": "2016-5-2",
        "end": "2016-5-8"
    },
    "preference": {
        "hoursPerDay": 7,
        "daysOfWork": [0, 1, 2]
    }
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
