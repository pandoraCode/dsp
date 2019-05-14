import requests
import json
import github3
import csv
from github import Github

repos= []
users= []
g = Github("pandoraCode", "yass_0001A")
repo = g.get_repo("primer/css")
cons = repo.get_contributors()

print(cons[0].email)
# def get_repos():
#     with open('repos.csv', 'r') as csvFile:
#         reader = csv.reader(csvFile)
#         for row in reader:
#             repos.append([row[0]])
#     csvFile.close()


# def parse_userInfo():
#     with open("contributors.csv", 'w', newline='\n') as f:
#      wr = csv.writer(f, quoting=csv.QUOTE_ALL)
#      for row in users:
#          wr.writerow(row)
#
#
# def get_contributors(repo):
#     repo = g.get_repo(repo)
#     for c in repo.get_contributors():
#         if c.email:
#             users.append([repo.name,c.name,email,c.location,c.bio])




# get_repos()
# for repo in repos:
#     get_contributors(repo[0])
#
# parse_userInfo()
