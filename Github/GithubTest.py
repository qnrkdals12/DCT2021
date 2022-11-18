import requests
from tqdm import tqdm

payload={}
headers = {'Authorization': 'token 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 '}

def get_data_from_repos(response):
  json_data = response.json()
  repos = []

  for project in json_data["items"]:
    repo_data = []
    repo_name = project["name"]
    repo_data.append(repo_name)
    description = project["description"]
    repo_data.append(description)
    owner = project["owner"]["login"]
    repo_data.append(owner)
    topic = project["topics"]
    repo_data.append(topic)
    url = project["html_url"]
    repo_data.append(url)
    user_api = project["owner"]["url"]
    repo_data.append(user_api)
    repo_api = project["url"]
    repo_data.append(repo_api)
    repos.append(repo_data)

  return repos



keywords = ["artificial intelligence", "deep learning","machine learning", "natural language processing","neural networks"
  ,"predictive analytics","reinforcement learning","supervised learning","unsupervised learning","robotics"
  ,"image recognition", "computer vision"
  ,"computer vision", "virtual assistant", "face recognition", "facial recognition","self driving", "speech recognition"
  ,"autonomous vehicle"]


page_num = 1
url = "https://api.github.com/search/repositories?q={" + keywords[0] + "}+created:2020-01-01..2020-12-31&per_page=100&page=" + str(page_num)
page_num = page_num + 1
res = requests.get(url, headers=headers)
repos = get_data_from_repos(res)

