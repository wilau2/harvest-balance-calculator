from datetime import timedelta

from github import Github, GithubException

from Config.Loader import load_configuration_file


class GithubCommit:
    def __init__(self, config_loader=load_configuration_file):
        self.github_config_secret = config_loader('config.json.secret')["github"]
        self.github_config = config_loader('configuration.json.secret')["github"]
        self.period_config = config_loader('config.json')["period"]
        self.g = Github(self.github_config_secret["token"])
        self.github_organizations = []

    def get_project_advancement(self, start, end):
        for organization in self.github_config["organizations"]:
            organization_repos = g.get_organization(organization["name"]).get_repos()
            for repo in organization_repos:
                since = start
                until = end + timedelta(days=1)
                commits = repo.get_commits(author=self.github_config_secret["username"],
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

    def get_all_github_organizations(self):
        if not self.github_organizations:
            self.__fetch_all_github_organizations()
        return self.github_organizations

    def __fetch_all_github_organizations(self):
        repos_user_have_access = self.g.get_user().get_repos()
        organizations = []
        for repo in repos_user_have_access:
            organization_name = repo.full_name.split("/")[0]
            organization = self.__safely_fetch_org_by_name(organization_name)
            if organization and organization not in organizations:
                organizations.append(organization)

        self.github_organizations = organizations

    def __safely_fetch_org_by_name(self, organization_name):
        try:
            return self.g.get_organization(organization_name)
        except GithubException:
            # not an organization
            return False

    def get_github_organizations_and_repositories_with_commits_in_interval(self, start, end):
        repos_with_commits = []
        orgs_with_commits = []
        for organization in self.get_all_github_organizations():
            org_has_commit = False
            for repo in organization.get_repos():
                repo_has_commit = False
                commits = repo.get_commits(
                    author=self.github_config_secret["username"],
                    since=start,
                    until=(end + timedelta(days=1)))

                for commit in commits:
                    repo_has_commit = True
                    org_has_commit = True

                if repo_has_commit:
                    repos_with_commits.append(repo)

            if org_has_commit:
                orgs_with_commits.append(organization)

        return {"repositories": repos_with_commits, "organizations": orgs_with_commits}



