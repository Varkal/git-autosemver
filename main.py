from git import Repo, InvalidGitRepositoryError

if __name__ == "__main__":
    try:
        repo = Repo(".")
        tag_list = [(tag_ref.commit.authored_date, tag_ref.name) for tag_ref in repo.tags]
        print(max(tag_list, key=lambda tag: tag[0]))
    except InvalidGitRepositoryError:
        print("This is not a git repository")
        exit()
