import requests

github_pull = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")


complete_details = github_pull.json()

for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])

