from Config.Loader import load_configuration_file, filter_list_manually

json = load_configuration_file("configuration.json.secret")

organizations = json["github"]["organizations"]
clients = json["harvest"]["clients"]

link_json_object = {}

for client in clients:
    print("Setting up harvest-github link for harvest project: " + client["name"])
    filtered_organizations = filter_list_manually(
        organizations,
        "Do you want to link a repo in this organizations?",
        "name"
    )
    for organization in filtered_organizations:
        filtered_repos = filter_list_manually(organization["repos"], "Do you want to link this repo?", "name")
