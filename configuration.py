from Config.Loader import save_json_file, filter_list_manually_boolean, retrieve_index_manually_from_list, \
    load_configuration_file
from GithubCommit.GithubCommit import GithubCommit
from HarvestBalanceCalculator import WorkingTimeInterval, HarvestTimeEntries
from HarvestHttpClient.Client import HarvestHttpClient


def get_all_harvest_clients_for_current_user_and_period():
    print("Retrieving the clients you worked for during the configured interval in Harvest")
    time_interval = WorkingTimeInterval(load_configuration_file('config.json'))
    print(" ")
    print("Configured time interval:")
    time_interval.print_interval()
    print(" ")
    client = HarvestHttpClient()
    user_id = client.get_me()["id"]
    time_entries = client.get_user_time_entries(
        time_interval.start,
        time_interval.end,
        user_id
    )
    time_entries = HarvestTimeEntries(time_entries)
    clients = time_entries.get_clients()

    print("Clients")
    for client_index, client in enumerate(clients):
        print(client["name"])
        for project_index, project in enumerate(client["projects"]):
            print("        " + project["name"])
        print("-----------------------------------------------")
    return clients


def select_github_organizations_to_track():
    print(" ")
    print("Retrieving the repositories you worked on during the configured interval in Github")
    time_interval = WorkingTimeInterval(load_configuration_file('config.json'))
    github_commit = GithubCommit()
    github_objects_with_commits = github_commit.get_github_organizations_and_repositories_with_commits_in_interval(
        time_interval.startDatetime, time_interval.endDatetime)
    print(" ")
    print(" ")
    print("Selecting organizations with commits between the configured interval...")
    organizations_with_commits = github_objects_with_commits["organizations"]
    repositories_with_commits = github_objects_with_commits["repositories"]
    selected_organizations = filter_list_manually_boolean(organizations_with_commits,
                                                          "Do you want to track this organization?", "name")
    configuration_organization = []
    for organization in selected_organizations:
        repos = organization.get_repos()
        repos_with_commit = []
        for repo in repos:
            if repo in repositories_with_commits:
                repos_with_commit.append(repo)
        print(" ")
        print("Selecting repositories with commits between the configured interval...")
        selected_repositories = filter_list_manually_boolean(repos_with_commit, "Do you want to track this repository?",
                                                             "name")
        configuration_organization.append(build_organization_configuration_object(organization, selected_repositories))

    return configuration_organization


def build_organization_configuration_object(organization, repositories):
    repos = []
    for repo in repositories:
        repos.append({
            "name": repo.name,
            "id": repo.id
        })
    return {
        "name": organization.name,
        "id": organization.id,
        "repos": repos
    }


clients = get_all_harvest_clients_for_current_user_and_period()
organizations = select_github_organizations_to_track()

configuration_json = {
    "github": {
        "organizations": organizations
    },
    "harvest": {
        "clients": clients
    }
}

save_json_file("configuration.json.secret", configuration_json)
