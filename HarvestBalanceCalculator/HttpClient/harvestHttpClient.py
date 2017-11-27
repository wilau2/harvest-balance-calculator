import http.client
import json

from config.loader import load_configuration_file


class HarvestHttpClient:
    def __init__(self,
                 config_loader=load_configuration_file,
                 https_connection=http.client.HTTPSConnection):
        self.HARVEST_API_URL = "api.harvestapp.com"
        self.HARVEST_ACCOUNT_ID_HEADER = "Harvest-Account-ID"
        self.HARVEST_AUTHORIZATION_HEADER = "Authorization"
        self.HARVEST_USER_AGENT = "User-Agent"
        self.conn = https_connection(self.HARVEST_API_URL)
        self.secret_config = config_loader('config.json.secret')

    def get_user_time_entries(self, date_from, date_to):
        headers = {
            self.HARVEST_ACCOUNT_ID_HEADER: self.secret_config["harvest"]["accountId"],
            self.HARVEST_AUTHORIZATION_HEADER: self.secret_config["harvest"]["authorization"],
            self.HARVEST_USER_AGENT: "HarvestBalanceCalculator API Example"
        }
        routes = ["/v2/time_entries?from=" + date_from.isoformat() + "&to=" + date_to.isoformat()]
        return self.__get_paginated_results("time_entries", routes, headers)

    def __get_paginated_results(self, array_name, routes, headers):
        results = []
        while len(routes) > 0:
            self.conn.request("GET", routes.pop(), None, headers)
            str_response = self.conn.getresponse().read().decode('utf-8')
            response = json.loads(str_response)
            self.__validate_errors(response)
            results += response[array_name]

            next_route = response["links"]["next"]
            if next_route:
                routes.append(next_route)

        return results

    @staticmethod
    def __validate_errors(json_response):
        try:
            error = json_response["error"]
            raise RuntimeError(error + " " + json_response["error_description"])
        except KeyError:
            return






