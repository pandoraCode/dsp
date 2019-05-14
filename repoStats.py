import requests
import json
import github3
import csv
from github import Github

def get_repos():
    with open('repos.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            repos.append([row[0]])
    csvFile.close()
