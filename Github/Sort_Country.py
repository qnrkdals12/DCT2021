import pandas as pd
import glob
from tqdm import tqdm

file_names = ["deep learning total-country.xlsx", "face recognition total-country.xlsx", "facial recognition total-country.xlsx",
              "image recognition total-country.xlsx", "natural language processing-country.xlsx", "neural networks-country.xlsx",
              "predictive_analytics-country.xlsx", "reinforcement learning-country.xlsx", "speech recognition-country.xlsx",
              "supervised learning-country.xlsx"]

countries = ["中国", "United States", "日本", "Canada", "대한민국", "Deutschland", "France", "United Kingdom"]

China = []
USA = []
Japan = []
Canada = []
Korea = []
Germany = []
France = []
UK = []

result = [China, USA, Japan, Canada, Korea, Germany, France, UK]

def read_file(file_name):
    fileDF = pd.read_excel(file_name)
    return fileDF

def sort_country(data_frame):
    for row in tqdm(data_frame.itertuples()):
        if row[10] in countries:
            index = countries.index(row[10])
        else:
            index = -1

    for country in result:
        if index == result.index(country):
            country.append(row)

def make_excel(list):
    count = 0
    for country in list:
        df_coun = pd.DataFrame(country)
        df_coun.to_excel(countries[count] + ".xlsx", encoding="utf-8-sig")
        count = count + 1

file_list = glob.glob("/Users/bugangmin/PycharmProjects/Intern/Github/*.xlsx")

for file in file_names:
    df = read_file(file)
    sort_country(df)
make_excel(result)
