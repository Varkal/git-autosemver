from git import Repo, InvalidGitRepositoryError
import re


def is_semver_tag(tag):
    pattern = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
    return pattern.search(tag[1])


def get_commits_more_recent_than(repo_ref, ref):
    print(ref)


if __name__ == "__main__":
    try:
        repo = Repo(".")
        tag_list = [(tag_ref.commit.authored_date, tag_ref.name, tag_ref.commit) for tag_ref in repo.tags]
        tag_list = [tag for tag in tag_list if is_semver_tag(tag)]
        last_tag = max(tag_list, key=lambda tag: tag[0])
        get_commits_more_recent_than(repo, last_tag[2])

    except InvalidGitRepositoryError:
        print("This is not a git repository")
        exit()
