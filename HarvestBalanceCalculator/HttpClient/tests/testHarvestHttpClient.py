import unittest
from datetime import datetime
from unittest.mock import MagicMock

from HarvestBalanceCalculator import HarvestHttpClient


class TestTimeUtils(unittest.TestCase):
    def test_get_user_time_entries_when_error(self):
        with self.assertRaises(RuntimeError):
            self.__given_an_error()

    def test_get_user_time_entry(self):
        result = self.__given_a_single_time_entry()
        expected = [{'expected': True}]
        self.assertEqual(expected, result)

    def test_get_user_time_entries(self):
        result = self.__given_multiple_time_entries()
        expected = [{'expected': 1}, {'expected': 2}]
        self.assertEqual(expected, result)

    def test_harvest_http_client_has_good_headers(self):
        harvest_http_client = HarvestHttpClient()
        self.assertEqual("Harvest-Account-ID", harvest_http_client.HARVEST_ACCOUNT_ID_HEADER)
        self.assertEqual("Authorization", harvest_http_client.HARVEST_AUTHORIZATION_HEADER)

    def test_harvest_http_client_has_good_url(self):
        harvest_http_client = HarvestHttpClient()
        self.assertEqual("api.harvestapp.com", harvest_http_client.HARVEST_API_URL)

    def __given_a_single_time_entry(self):
        date_from = datetime(2017, 1, 1)
        date_to = datetime(2017, 1, 15)
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        harvest_http_client.conn.getresponse.return_value.read.return_value.decode.return_value = """
        {"time_entries":[{"expected":true}],"links":{"next":null}}
        """
        return harvest_http_client.get_user_time_entries(date_from, date_to)

    def __given_multiple_time_entries(self):
        date_from = datetime(2017, 1, 1)
        date_to = datetime(2017, 1, 15)
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        harvest_http_client.conn.getresponse.return_value.read.return_value.decode.side_effect = ["""
                {"time_entries":[{"expected":1}],"links":{"next":"aNextRoute"}}
                """, """
                {"time_entries":[{"expected":2}],"links":{"next":null}}
                """]
        return harvest_http_client.get_user_time_entries(date_from, date_to)

    def __given_an_error(self):
        date_from = datetime(2017, 1, 1)
        date_to = datetime(2017, 1, 15)
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        harvest_http_client.conn.getresponse.return_value.read.return_value.decode.return_value = """
        {"error":"AnError","error_description":"A description"}
        """
        return harvest_http_client.get_user_time_entries(date_from, date_to)

    @staticmethod
    def __given_http_client_with_secret_config_and_http_client():
        harvest_http_client = HarvestHttpClient(MagicMock(return_value={
            "harvest": {"accountId": "dumpAccountId", "authorization": "dumbAuthorization"}
        }), MagicMock())
        harvest_http_client.conn.request = MagicMock()
        return harvest_http_client


if __name__ == '__main__':
    unittest.main()
