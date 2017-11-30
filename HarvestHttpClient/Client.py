import http.client
import json

from Config.Loader import load_configuration_file


class HarvestHttpClient:
    def __init__(self,
                 config_loader=load_configuration_file,
                 https_connection=http.client.HTTPSConnection):
        self.HARVEST_API_URL = "api.harvestapp.com"
        self.HARVEST_ACCOUNT_ID_HEADER = "Harvest-Account-ID"
        self.HARVEST_AUTHORIZATION_HEADER = "Authorization"
        self.HARVEST_USER_AGENT = "User-Agent"
        self.conn = https_connection(self.HARVEST_API_URL)
        secret_config = config_loader('config.json.secret')
        self.headers = {
            self.HARVEST_ACCOUNT_ID_HEADER: secret_config["harvest"]["accountId"],
            self.HARVEST_AUTHORIZATION_HEADER: secret_config["harvest"]["authorization"],
            self.HARVEST_USER_AGENT: "HarvestBalanceCalculator API Example"
        }

    def get_me(self):
        route = "/v2/users/me"
        return self.__get_single_result(route, self.headers)

    def get_user_time_entries(self, date_from, date_to, user_id):
        routes = ["/v2/time_entries?from=" +
                  date_from.isoformat() +
                  "&to=" +
                  date_to.isoformat() +
                  "&user_id=" +
                  str(user_id)]
        return self.__get_all_paginated_results("time_entries", routes, self.headers)

    def __get_single_result(self, route, headers):
        self.conn.request("GET", route, None, headers)
        response = self.conn.getresponse()
        status = response.status
        if status != 200:
            raise RuntimeError(
                'Something bad happened. Http code: {0} returned by harvest api. '
                'Check the doc and validate the Authorization token format, '
                'it should start with Bearer'.format(status))
        response = json.loads(response.read().decode('utf-8'))
        self.__validate_errors(response)
        return response

    def __get_all_paginated_results(self, array_name, routes, headers):
        results = []
        while len(routes) > 0:
            response = self.__get_single_result(routes.pop(), headers)
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
