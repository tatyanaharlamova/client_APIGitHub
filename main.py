from github import Github

username = "tatyanaharlamova"

g = Github()
for repo in g.search_repositories("tatyanaharlamova/mailing_service"):
    # распечатать сведения о репозитории
    print(repo)

# user = g.get_user(username)
# for repo in user.get_repos():
#     print(repo.name, repo.description, repo.stargazers_count, repo.forks_count)
#     for commit in repo.get_commits():
#         print(commit.sha, commit.author, commit.commit.message)


#
# repo = g.get_repo('tatyanaharlamova/diagnostic_website')  # 'пользователь/репозиторий'
# for commit in repo.get_commits():
#     # print(commit.sha, commit.author, commit.last_modified, commit.url)
#     # print(dir(commit))
#     print(commit.sha, commit.author.email, commit.commit.message, commit.commit.committer.date, commit.commit.url)
