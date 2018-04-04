from dateutil.parser import parse

from GithubCommit.GithubCommit import GithubCommit

start = parse("2017-10-1")
end = parse("2017-11-27")


github_commit = GithubCommit()

# print(github_commit.get_all_organizations())

print(github_commit.get_github_organizations_and_repositories_with_commits_in_interval(start, end))



