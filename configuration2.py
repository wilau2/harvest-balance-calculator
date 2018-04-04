from Config.Loader import load_configuration_file, retrieve_index_manually_from_list, save_json_file

configuration_json = load_configuration_file('configuration.json.secret')
organizations = configuration_json["github"]["organizations"]
clients = configuration_json["harvest"]["clients"]

links = []
for org in organizations:
    print("For organization: " + org["name"])
    for repo in org["repos"]:
        print("For repository: " + repo["name"])
        client = retrieve_index_manually_from_list(clients, "Which client do you want to select?", 'name')
        project = retrieve_index_manually_from_list(client["projects"], "Which project do you want to select?", "name")
        links.append({"repository": repo["id"], "project": project["id"]})
        print(" ")
        print(" ")


configuration_json["links"] = links
save_json_file("configuration.json.secret", configuration_json)
