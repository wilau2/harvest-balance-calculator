import unittest
import os
from HarvestBalanceCalculator import WorkingTimeInterval

os.environ['BEGIN_DATE'] = '2016-5-2'
os.environ['END_DATE'] = '2016-5-8'
working_time_interval = WorkingTimeInterval()

os.environ['WORKED_HOURS_CORRECTION'] = '-5.5'
working_time_interval_with_hour_correction = WorkingTimeInterval()


class TestWorkingTimeInterval(unittest.TestCase):
    def test_get_number_of_working_days(self):
        number_of_working_days = working_time_interval.get_number_of_working_days()
        self.assertEqual(3, number_of_working_days)

    def test_get_total_should_have_worked_time(self):
        total_should_have_worked_time = working_time_interval.get_total_should_have_worked_time()
        self.assertEqual(21, total_should_have_worked_time)

    def test_get_worked_hours_correction_when_not_specified(self):
        worked_hours_correction = working_time_interval.get_worked_hours_correction()
        self.assertEqual(0, worked_hours_correction)

    def test_get_worked_hours_correction_when_specified(self):
        worked_hours_correction = working_time_interval_with_hour_correction.get_worked_hours_correction()
        self.assertEqual(-5.5, worked_hours_correction)


if __name__ == '__main__':
    unittest.main()
