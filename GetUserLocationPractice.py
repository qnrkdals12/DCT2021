import requests
import json

payload={}
headers = {'Authorization': 'token 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'}

keywords = ["artificial intelligence", "deep learning","machine learning", "natural language processing","neural networks"
  ,"predictive analytics","reinforcement learning","supervised learning","unsupervised learning","robotics"
  ,"image recognition", "computer vision"
  ,"computer vision", "virtual assistant", "face recognition", "facial recognition","self driving", "speech recognition"
  ,"autonomous vehicle"]

url = "https://api.github.com/search/repositories?q=robotics created:2020-01-01..2020-12-31"

response = requests.request("GET", url, headers=headers, data=payload)

json_data = response.json()

user_data = json_data["items"][0]["owner"]["url"]

user_api = requests.request("GET", user_data, headers=headers, data=payload)

user_json = user_api.json()

print(user_json)