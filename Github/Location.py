import pandas as pd
import requests
from tqdm import tqdm
import pandas as pd
import time

repo_data = pd.read_csv("robotics.csv")

headers = {'Authorization': 'token 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'}

location = []

for user in tqdm(repo_data["user_api"]):
    try:
        one_response = requests.request("GET", user, headers=headers)
        one_json = one_response.json()
        location.append(one_json["location"])
    except:
        time.sleep(3601)
        one_response = requests.request("GET", user, headers=headers)
        one_json = one_response.json()
        location.append(one_json["location"])
        continue


repo_data['location'] = location
repo_data.to_csv("robotics.csv", encoding="utf-8-sig")

