import requests
import json
import github3
import csv
from github import Github

repos= []
users= []

# repo = g.get_repo("primer/css")
# cons = repo.get_contributors()
# s = repo.get_commits(author="shawnbot").totalCount
# i = repo.get_issues(creator="shawnbot").totalCount
# print(s)
# print(i)


def get_contributors_info(repo):
    repo = g.get_repo(repo)
    for c in repo.get_contributors():
        numCommits = repo.get_commits(author=c).totalCount
        numIssues= repo.get_issues(creator=c).totalCount
        if c.email:
            users.append([repo.name,c.name,c.email,numCommits,numIssues,c.company,c.location,c.bio])

def parse_userInfo():
    with open("contributors2.csv", 'w', newline='\n') as f:
     wr = csv.writer(f, quoting=csv.QUOTE_ALL)
     for row in users:
         wr.writerow(row)


def get_repos():
    with open('repos.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            repos.append([row[0]])
    csvFile.close()


# get_repos()
# for repo in repos:
#     get_contributors_info(repo[0])

get_contributors_info("audi/audi-ui")
parse_userInfo()
