from git import Repo, InvalidGitRepositoryError

if __name__ == "__main__":
    try:
        repo = Repo(".")
        print(repo.tags)
    except InvalidGitRepositoryError:
        print("This is not a git repository")
        exit()
