#!/usr/bin/python3
"""
Retrieves information about a GitHub repository using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repository}"

    response = requests.get(url)

    if response.status_code == 200:
        repo_info = response.json()
        print("Repository Name:", repo_info['name'])
        print("Owner:", repo_info['owner']['login'])
        print("Description:", repo_info['description'])
        print("Number of Stars:", repo_info['stargazers_count'])
        print("Number of Forks:", repo_info['forks_count'])
    else:
        print("Failed to retrieve repository information. Status code:", response.status_code)

