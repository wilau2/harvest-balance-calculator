from datetime import timedelta

from github import Github
from Config.Loader import load_configuration_file
from dateutil.parser import parse

start = parse("2017-10-1")
end = parse("2017-11-27")

github_config_secret = load_configuration_file('config.json.secret')["github"]
github_config = load_configuration_file('configuration.json.secret')["github"]
period_config = load_configuration_file('config.json')["period"]

g = Github(github_config_secret["token"])


def get_project_advancement(start, end):
    for organization in github_config["organizations"]:
        organization_repos = g.get_organization(organization["name"]).get_repos()
        for repo in organization_repos:
            since = start
            until = end + timedelta(days=1)
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


def get_repos_with_commits(start, end):
    for organization in github_config["organizations"]:
        organization_repos = g.get_organization(organization["name"]).get_repos()
        for repo in organization_repos:
            since = start
            until = end + timedelta(days=1)
            commits = repo.get_commits(author=github_config_secret["username"],
                                       since=since,
                                       until=until
                                       )
            has_commit = False
            for commit in commits:
                has_commit = True

            if has_commit:
                print(repo.name)


get_repos_with_commits(start, end)



