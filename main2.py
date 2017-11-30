from datetime import timedelta

from github import Github
from Config.Loader import load_configuration_file
from dateutil.parser import parse

github_config = load_configuration_file('config.json.secret')["github"]
date_config = load_configuration_file('config.json')

g = Github(github_config["token"])

organizations = [{
        "name": "aptology",
        "repos": [
            "daikoku",
            "kuebiko",
            "hanbo",
            "aptology-assessment-server",
            "assessment-client",
            "assessment-engine"
        ]
    }]
for org in organizations:
    org_repos = g.get_organization(org["name"]).get_repos()
    for repo in org_repos:
        if repo.name in org["repos"]:
            since = parse(date_config["beginDate"])
            until = parse(date_config["endDate"]) + timedelta(days=1)
            commits = repo.get_commits(author=github_config["username"],
                                       since=since,
                                       until=until
                                       ).get_page(0)
            if len(commits) > 0:
                print("================")
                print(repo.name)
                for commit in commits:
                    print(commit.commit.message)
                print("END==============")



