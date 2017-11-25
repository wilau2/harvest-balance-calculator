import http.client
import json

from config.loader import load_configuration_file


class HarvestApi:

    def __init__(self):
        self.conn = http.client.HTTPSConnection("api.harvestapp.com")
        self.secret_config = load_configuration_file('config.json.secret')

    def get_user_time_entries(self, date_from, date_to):
        headers = {
            "Harvest-Account-ID": self.secret_config["harvest"]["accountId"],
            "Authorization": self.secret_config["harvest"]["authorization"],
            "User-Agent": "Harvest API Example"
        }
        routes = ["/v2/time_entries?from=" + date_from.isoformat() + "&to=" + date_to.isoformat()]
        return self.__get_paginated_results("time_entries", routes, headers)

    def __get_paginated_results(self, array_name, routes, headers):
        results = []
        while len(routes) > 0:
            self.conn.request("GET", routes.pop(), None, headers)
            response = json.loads(self.conn.getresponse().read())
            results += response[array_name]

            next_route = response["links"]["next"]
            if next_route:
                routes.append(next_route)

        return results
