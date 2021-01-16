import csv
import json

use = open('state_to_region.json')
checker = json.load(use)

csvfile = open('people.csv', newline='')
reader = csv.reader(csvfile, delimiter=',')

list_csv = list(reader)

for i in range(len(list_csv)):
    for c in checker:
        if list_csv[i][3] == c:
            list_csv[i][4] = checker[c]
            print(list_csv[i][4])

with open('people.csv', 'w', newline='') as csvfile2:
    writer = csv.writer(csvfile2)
    writer.writerows(list_csv)
