import unittest
from datetime import datetime
from unittest.mock import MagicMock, Mock

from HarvestHttpClient import Client


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
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        self.assertEqual("Harvest-Account-ID", harvest_http_client.HARVEST_ACCOUNT_ID_HEADER)
        self.assertEqual("Authorization", harvest_http_client.HARVEST_AUTHORIZATION_HEADER)

    def test_harvest_http_client_has_good_url(self):
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        self.assertEqual("api.harvestapp.com", harvest_http_client.HARVEST_API_URL)

    def test_given_harvest_api_404(self):
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        mock = Mock()
        mock.status = 404
        harvest_http_client.conn.getresponse.return_value = mock
        with self.assertRaises(RuntimeError):
            harvest_http_client.get_me()

    def __given_a_single_time_entry(self):
        a_date_from = datetime(2017, 1, 1)
        a_date_to = datetime(2017, 1, 1)
        a_user_id = "aUserId"
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        harvest_http_client.conn.getresponse.return_value.read.return_value.decode.return_value = """
        {"time_entries":[{"expected":true}],"links":{"next":null}}
        """
        return harvest_http_client.get_user_time_entries(a_date_from, a_date_to, a_user_id)

    def __given_multiple_time_entries(self):
        a_date_from = datetime(2017, 1, 1)
        a_date_to = datetime(2017, 1, 1)
        a_user_id = "aUserId"
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        harvest_http_client.conn.getresponse.return_value.read.return_value.decode.side_effect = ["""
                {"time_entries":[{"expected":1}],"links":{"next":"aNextRoute"}}
                """, """
                {"time_entries":[{"expected":2}],"links":{"next":null}}
                """]
        return harvest_http_client.get_user_time_entries(a_date_from, a_date_to, a_user_id)

    def __given_an_error(self):
        a_date_from = datetime(2017, 1, 1)
        a_date_to = datetime(2017, 1, 1)
        a_user_id = "aUserId"
        harvest_http_client = self.__given_http_client_with_secret_config_and_http_client()
        harvest_http_client.conn.getresponse.return_value.read.return_value.decode.return_value = """
        {"error":"AnError","error_description":"A description"}
        """
        return harvest_http_client.get_user_time_entries(a_date_from, a_date_to, a_user_id)

    @staticmethod
    def __given_http_client_with_secret_config_and_http_client():
        harvest_http_client = Client.HarvestHttpClient(MagicMock(return_value={
            "harvest": {"accountId": "dumpAccountId", "authorization": "dumbAuthorization"}
        }), MagicMock())
        mock = Mock()
        mock.status = 200
        harvest_http_client.conn.getresponse.return_value = mock
        harvest_http_client.conn.request = MagicMock()
        harvest_http_client.headers = MagicMock()
        return harvest_http_client




if __name__ == '__main__':
    unittest.main()
