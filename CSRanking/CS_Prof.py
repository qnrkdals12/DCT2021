from bs4 import BeautifulSoup
import pandas as pd

countries = ["Canada", "China", "France", "Germany", "Japan", "UnitedKingdom", "USA", "SouthKorea"]

def get_html(country):
    file_name = country + ".html"
    page = open(file_name, "rt", encoding="utf-8").read()
    soup = BeautifulSoup(page, "html.parser")
    return soup

def get_data(soup):
    tables = soup.find_all("table")

    names = []
    counts = []
    faculties = []

    for table in tables:
        each = table.find("tbody")

        first_prof = each.find("tr")
        professors = first_prof.find_next_siblings()

        name1 = first_prof.find("small").find("a")
        count1 = first_prof.find("td", {"align": "right"})
        facu1 = count1.find_next_sibling()

        names.append(name1.get_text())
        counts.append(count1.get_text())
        faculties.append(facu1.get_text())

        counter = 0

        for prof in professors:
            if counter % 2 == 1:
                name = prof.find("small").find("a")
                count = prof.find("td", {"align": "right"})
                facu = count.find_next_sibling()
                names.append(name.get_text())
                counts.append(count.get_text())
                faculties.append(facu.get_text())
            counter = counter + 1
    total = []
    for i in range(len(names)):
        eachtotal = [names[i], counts[i], faculties[i]]
        total.append(eachtotal)

    return total

def make_csv(total, country):
    total_df = pd.DataFrame(total, columns=['Faculty', 'Count', 'Faculty'])
    save_fname = 'Faculty_list_' + country + '.xlsx'
    total_df.to_excel(save_fname, encoding='utf-8-sig')

for each in countries:
    soup = get_html(each)
    data = get_data(soup)
    make_csv(data, each)