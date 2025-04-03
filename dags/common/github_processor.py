import logging

logger = logging.getLogger(__name__)
from github.Organization import Organization
from github.Commit import Commit


def print_commit(commit: Commit):
    logger.info(commit.sha)
    logger.info(commit.author)

    logger.info(commit.raw_data["commit"]["author"]["name"])
    logger.info(commit.raw_data["commit"]["author"]["email"])
    logger.info(commit.raw_data["commit"]["author"]["date"])
    logger.info(commit.raw_data["commit"]["message"])


def post_process_github_org(organization: Organization):
    repos = list(organization.get_repos())
    logger.info(f"Found {repos} repos")
    repos.sort(key=lambda repo: repo.updated_at, reverse=True)
    logger.info(f"Repos sorted by updated_at: {repos}")
    latest_repo = repos[0]
    latest_commits = list(latest_repo.get_commits())[:3]
    for commit in latest_commits:
        print_commit(commit)
    logger.info(latest_commits)
    content = open("commits.txt", "r").readlines()[0]
    # If sha in the file is the same as the one you queried, nothing new to be added
    if content == str(latest_commits[0].sha):
        logger.info("Nothing new to update here!")
    else:
        open("commits.txt", "w").write(str(latest_commits[0].sha))
        logger.info("Successfully updated the database")
