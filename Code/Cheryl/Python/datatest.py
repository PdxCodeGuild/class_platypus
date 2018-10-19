import csv

with open('oregonpopulation.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    rows = list(reader)
    for row in rows[3:12]:
        print(' HHHH '.join(row))