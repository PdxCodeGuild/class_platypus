import csv


def open_with_csv(filename, d=','):
    data = []
    with open(filename, encoding='utf-8') as tsvin:
        tie_reader = csv.reader(tsvin, delimiter='d')
        for line in tie_reader:
            data.append(line)
    return data

data_from_csv = open_with_csv('oregonpopulation.csv')
print(data_from_csv[5])
# with open('oregonpopulation.csv', newline='') as csvfile:
#     # The reader in this is like a DICT reader
#     reader = csv.DictReader(csvfile, delimiter=',')
#     rows = list(reader)
#     for row in rows[3::]:
#         print(row['population'])


# with open('oregonpopulation.csv', newline='') as csvfile:
#     # The reader in this is like a LIST reader
#     reader = csv.reader(csvfile, delimiter=',')
#     rows = list(reader)
#     for row in rows[3:12]:
#         print(' HHHH '.join(row))