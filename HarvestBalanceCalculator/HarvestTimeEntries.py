from funcy import pluck


class HarvestTimeEntries:
    def __init__(self, time_entries):
        self.time_entries = time_entries

    def print_all(self):
        for entry in self.time_entries:
            print(entry["notes"])

    def get_total_worked_time(self):
        total_worked_time = 0
        for time_entry in self.time_entries:
            total_worked_time += time_entry["hours"]
        return total_worked_time

    def get_clients(self):
        clients = []
        for time_entry in self.time_entries:
            client = time_entry["client"]
            client_id = client["id"]
            clients_id = pluck("id", clients)
            if client_id not in clients_id:
                clients.append(client)

            project = time_entry["project"]
            project_id = project["id"]
            client_projects = self.__get_client_projects(client)
            client_projects_id = pluck("id", client_projects)
            if project_id not in client_projects_id:
                client_projects.append(project)

        return clients

    @staticmethod
    def __get_client_projects(client):
        try:
            return client["projects"]
        except KeyError:
            client["projects"] = []
            return client["projects"]
