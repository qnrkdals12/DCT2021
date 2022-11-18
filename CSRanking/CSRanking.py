from bs4 import BeautifulSoup
import pandas as pd

countries = ["Canada", "China", "France", "Germany", "Japan", "UnitedKingdom", "USA"]

def get_html(country):
    file_name = country + ".html"
    page = open(file_name, "rt", encoding="utf-8").read()
    soup = BeautifulSoup(page, "html.parser")
    return soup

def get_data(soup):
    tr = soup.find('tr')
    trs = tr.find_next_siblings()
    univs = []
    first_spans = tr.find_all("span")
    first_span = first_spans[1].get_text(strip=True)
    univs.append(first_span)

    counts = []
    score = tr.find("td", {"align": "right"})
    counts.append(score.get_text(strip=True))

    faculties = []
    fa = score.find_next_sibling()
    faculties.append(fa.get_text(strip=True))

    counter = 0
    for k in trs:
        if counter % 3 == 2:
            spans = k.find_all("span")
            name = spans[1].get_text(strip=True)
            univs.append(name)
            count = k.find("td", {"align": "right"})
            counts.append(count.get_text(strip=True))
            facu = count.find_next_sibling()
            faculties.append(facu.get_text(strip=True))
        counter = counter + 1

    total = []
    for i in range(len(univs)):
        eachtotal = [univs[i], counts[i], faculties[i]]
        total.append(eachtotal)
    return total

def make_csv(total, country):
    total_df = pd.DataFrame(total, columns=['Institution', 'Count', 'Faculty'])
    save_fname = 'Institution_list_' + country
    total_df.to_csv(save_fname, encoding='utf-8-sig')

for each in countries:
    soup = get_html(each)
    data = get_data(soup)
    make_csv(data, each)