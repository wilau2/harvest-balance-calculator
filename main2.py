from datetime import timedelta

from github import Github
from Config.Loader import load_configuration_file
from dateutil.parser import parse

github_config_secret = load_configuration_file('config.json.secret')["github"]
period_config = load_configuration_file('config.json')["period"]

g = Github(github_config_secret["token"])

# config = [
#     {
#         "harvest": {
#             "clients": [
#                 {
#                     "id": 5283466,
#                     "name": "Aptology Inc",
#                     "projects": [
#                         {
#                             "id": 12990453,
#                             "name": "Pivotal Ground Work"
#                         }
#                     ]
#                 }
#             ],
#         }
#     }
# ]

for organization in github_config_secret["organizations"]:
    organization_repos = g.get_organization(organization["name"]).get_repos()
    for repo in organization_repos:
        if repo.name in organization["repos"]:
            since = parse(period_config["begin"])
            until = parse(period_config["end"]) + timedelta(days=1)
            commits = repo.get_commits(author=github_config_secret["username"],
                                       since=since,
                                       until=until
                                       )
            print("================")
            print(repo.name)
            for commit in commits:
                print("commit name: " + commit.commit.message)
                print("additions: +" + str(commit.stats.additions))
                print("deletions: -" + str(commit.stats.deletions))
                print("nb changed files: " + str(len(commit.files)))
            print("END==============")



