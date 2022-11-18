import csv

f = open('StackOverflow_2021_Question.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
counter = 0
for line in rdr:
    if counter < 962:
        print(line[5])
    counter = counter + 1