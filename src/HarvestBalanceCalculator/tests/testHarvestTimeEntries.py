import unittest

from HarvestBalanceCalculator import HarvestTimeEntries


class TestHarvestTimeEntries(unittest.TestCase):
    def test_get_total_worked_time(self):
        harvest_time_entries = HarvestTimeEntries([{"hours": 10}, {"hours": 15}])
        result = harvest_time_entries.get_total_worked_time()
        self.assertEqual(25, result)


if __name__ == '__main__':
    unittest.main()
