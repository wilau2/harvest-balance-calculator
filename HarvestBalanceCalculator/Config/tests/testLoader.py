import unittest

from HarvestBalanceCalculator.Config.Loader import load_configuration_file


class TestLoader(unittest.TestCase):
    def test_load_configuration_file(self):
        config = load_configuration_file('config.json')
        self.assertEqual("2016-5-2", config["beginDate"])
        self.assertEqual("2017-11-24", config["endDate"])
        self.assertEqual("37.5", config["hoursPerWorkWeek"])
        self.assertEqual("7.5", config["hoursPerWorkDay"])
        self.assertEqual([0, 1, 2, 3, 4], config["workDaysOfTheWeek"])


if __name__ == '__main__':
    unittest.main()
