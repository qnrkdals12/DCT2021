import requests
from tqdm import tqdm
import pandas as pd

repo_data = pd.read_csv("robotics.csv")

headers = {'Authorization': 'token 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'}

location = []

for user in tqdm(repo_data["user_api"]):
    one_response = requests.request("GET", user, headers = headers)
    one_json = one_response.json()
    location.append(one_json["location"])

repo_data['location'] = location

repo_data.to_csv("Autonomous Vehicle.csv", encoding="utf-8-sig")