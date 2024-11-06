from github import Github

username = "tatyanaharlamova"

g = Github()

user = g.get_user(username)
for repo in user.get_repos():
    print(repo.name, repo.description, repo.stargazers_count, repo.forks_count)
    for commit in repo.get_commits():
        print(commit.sha, commit.author, commit.commit.message)


#
# repo = g.get_repo('tatyanaharlamova/diagnostic_website')  # 'пользователь/репозиторий'
# for commit in repo.get_commits():
#     print(commit.sha, commit.author, commit.last_modified)
