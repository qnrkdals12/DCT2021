import pandas as pd
import requests
from tqdm import tqdm
import time
from datetime import datetime, timedelta

repo_data = pd.read_csv("machine learning.csv")

headers = {'Authorization': 'token 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'}

location = []

rundata = repo_data.copy()

for user in tqdm(rundata["user_api"]):
    try:
        one_response = requests.request("GET", user, headers=headers)
        one_json = one_response.json()
        if one_json.get("location"):
            location.append(one_json["location"])
        else:
            location.append(None)

    except:
        print("Error at: " + user)
        print("Sleep until: " + str(datetime.now() + timedelta(hours=1)))
        time.sleep(3601)
        one_response = requests.request("GET", user, headers=headers)
        one_json = one_response.json()
        location.append(one_json["location"])
        continue

rundata['location'] = location
rundata.to_csv("machine learning with location.csv", encoding="utf-8-sig")