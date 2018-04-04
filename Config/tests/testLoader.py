import unittest

from Config.Loader import load_configuration_file


class TestLoader(unittest.TestCase):
    def test_load_configuration_file(self):
        config = load_configuration_file('Config/tests/config.json')
        self.assertEqual("2016-5-2", config["period"]["begin"])
        self.assertEqual("2017-11-24", config["period"]["end"])
        self.assertEqual("7.5", config["preference"]["hoursPerDay"])
        self.assertEqual([0, 1, 2, 3, 4], config["preference"]["daysOfWork"])


if __name__ == '__main__':
    unittest.main()
