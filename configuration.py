from github import Github

from Config.Loader import load_configuration_file, save_json_file, filter_list_manually
from HarvestBalanceCalculator import WorkingTimeInterval, HarvestTimeEntries
from HarvestHttpClient.Client import HarvestHttpClient

github_config_secret = load_configuration_file('config.json.secret')["github"]
config = load_configuration_file('config.json')
period_config = config["period"]


def get_all_harvest_clients_for_current_user_and_period():
    time_interval = WorkingTimeInterval(config)
    client = HarvestHttpClient()
    user_id = client.get_me()["id"]
    time_entries = client.get_user_time_entries(
        time_interval.begin,
        time_interval.end,
        user_id
    )
    time_entries = HarvestTimeEntries(time_entries)
    return time_entries.get_clients()


def select_github_organizations_to_track():
    g = Github(github_config_secret["token"])
    repos_user_have_access = g.get_user().get_repos()
    organization_names = []
    for repo in repos_user_have_access:
        org = repo.full_name.split("/")[0]
        if org not in organization_names:
            organization_names.append(org)

    print("Selecting organizations")
    selected_organizations = filter_list_manually(organization_names, "Do you want to track this organization?")

    organization_object_list = []
    for org_name in selected_organizations:
        git_organization = g.get_organization(org_name)
        organization_object = {
            "name": org_name,
            "id": git_organization.id,
        }
        repos = []
        for repo in git_organization.get_repos():
            repo_object = {
                "name": repo.name,
                "id": repo.id
            }
            repos.append(repo_object)
        organization_object["repos"] = repos
        organization_object_list.append(organization_object)
    return organization_object_list


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
