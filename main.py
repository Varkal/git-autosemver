from git import Repo, InvalidGitRepositoryError
import re


class NoCommitSinceLastTagError(Exception):
    pass


def is_semver_tag(tag, config=None):
    pattern = re.compile(
        "^" + re.escape(config["prefix"]) +
        "(\d+)\.(\d+)\.(\d+)" +
        re.escape(config["suffix"]) + "$"
    )
    return pattern.search(tag["name"])


def is_major_commit(commit):
    pattern = re.compile(r"^.*#major.*$")
    return pattern.search(commit.message)


def is_minor_commit(commit):
    pattern = re.compile(r"^.*feat.*$")
    return pattern.search(commit.message)


def get_commits_more_recent_than(repo, ref):
    commits_list = []
    for commit in repo.iter_commits():
        if repo.is_ancestor(ref, commit) and commit != ref:
            commits_list.append(commit)
    return commits_list


def create_tag_dict(tag_ref):
    return {
        "timestamp": tag_ref.commit.authored_date,
        "name": tag_ref.name,
        "commit": tag_ref.commit
    }


def create_tag_list(tags):
    return [create_tag_dict(tag_ref) for tag_ref in tags]


def get_semver_dict(tag_name):
    splitted_name = tag_name.split(".")
    return {
        "major": int(splitted_name[0]),
        "minor": int(splitted_name[1]),
        "patch": int(splitted_name[2])
    }


def get_rev_type(commits):
    if len(commits) == 0:
        raise NoCommitSinceLastTagError

    rev_type = "patch"
    for commit in commits:
        if rev_type != "major" and is_major_commit(commit):
            rev_type = "major"
        if rev_type != "major" and is_minor_commit(commit):
            rev_type = "minor"
    return rev_type


def calc_new_version(semver_dict, rev_type):
    semver_dict[rev_type] += 1
    if rev_type == "major":
        semver_dict["minor"] = semver_dict["patch"] = 0
    if rev_type == "minor":
        semver_dict["patch"] = 0
    return semver_dict


def main():
    try:
        repo = Repo(".")
        config = {"prefix": "", "suffix": ""}
        tag_list = [tag for tag in create_tag_list(repo.tags) if is_semver_tag(tag, config)]

        if len(tag_list):
            last_tag = max(tag_list, key=lambda tag: tag["timestamp"])
            commits = get_commits_more_recent_than(repo, last_tag["commit"])
            rev_type = get_rev_type(commits)
            semver_dict = calc_new_version(get_semver_dict(last_tag["name"]), rev_type)
        else:
            semver_dict = get_semver_dict("1.0.0")

        repo.create_tag("%(major)s.%(minor)s.%(patch)s" % semver_dict)

    except InvalidGitRepositoryError:
        print("This is not a git repository")
        exit()
    except NoCommitSinceLastTagError:
        print("No commits since last tag")
        exit()


if __name__ == "__main__":
    main()
