def add_data_to_list(json):
    for project in json["items"]:
        repo_name = project["name"]
        description = project["description"]
        owner = project["owner"]["login"]
        topic = project["topics"]
        url = project["html_url"]
        user_api = project["owner"]["url"]
        repo_api = project["url"]
        repo_data = [repo_name, description, owner, topic, url, user_api, repo_api]
        repos.append(repo_data)

import requests
import pandas as pd
from datetime import datetime, timedelta

payload = {}
headers = {'Authorization': 'token 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'}
repos = []

start = "2020-01-01"
last = "2020-12-31"

start_date = datetime.strptime(start, "%Y-%m-%d")
last_date = datetime.strptime(last, "%Y-%m-%d")

counter = 0

while start_date <= last_date:
    dates = start_date.strftime("%Y-%m-%d")
    print(dates)
    url = "https://api.github.com/search/repositories?q={robotics}+created:"+ str(dates) +"&per_page=100"
    print(url)
    response = requests.request("GET", url, headers=headers)
    json_data = response.json()
    total_count = json_data["total_count"]

    if total_count > 1000:
        total_page = 10
    else:
        total_page = int(total_count / 100) + 1

    print("Count: " + str(total_count))
    print("Page: " + str(total_page))

    for page in range(2, total_page + 1):
        one_page = url + "&page=" + str(page)
        print(one_page)
        one_response = requests.request("GET", one_page, headers=headers)
        one_json = one_response.json()
        add_data_to_list(one_json)

    start_date += timedelta(days=1)

repos_df = pd.DataFrame(repos, columns=['repo_name', 'description', 'owner', 'topic', 'urls', 'user_api', 'repo_api'])
save_fname = 'robotics.csv'
repos_df.to_csv(save_fname, encoding='utf-8-sig')