import unittest
from datetime import datetime
from unittest.mock import MagicMock

from HarvestBalanceCalculator import HarvestHttpClient

harvest_http_client = HarvestHttpClient(MagicMock(return_value={
    "harvest": {"accountId": "dumpAccountId", "authorization": "dumbAuthorization"}
}), MagicMock())

harvest_http_client.conn.request = MagicMock()

harvest_http_client.conn.getresponse.return_value.read.return_value.decode.return_value = """
{"time_entries":[{"expected":true}],"links":{"next":null}}
"""


class TestTimeUtils(unittest.TestCase):
    def test_get_user_time_entries(self):
        date_from = datetime(2017, 1, 1)
        date_to = datetime(2017, 1, 15)
        expected = [{'expected': True}]
        result = harvest_http_client.get_user_time_entries(date_from, date_to)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
