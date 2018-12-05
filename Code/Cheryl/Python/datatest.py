import csv
import numpy


data = []
headers = None
with open('oregonpopulation.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for i, row in enumerate(spamreader):
        if i == 0:
            headers = row
            print(headers)
            continue
        row_data = {}
        for i in range(len(headers)):
            row_data[headers[i]] = row[i]
        data.append(row_data)

        #print(', '.join(row))

print(data)




for row in data:
    row['Pop. 2017'] = int(row['Pop. 2017'].replace(',', ''))
    print(f'County name: ' + row['County name'])
    print(f'\tPop. 2017: ' + str(row['Pop. 2017']))



# def open_with_csv(filename, d=','):
#     data = []
#     with open(filename, encoding='utf-8') as tsvin:
#         tie_reader = csv.reader(tsvin, delimiter='d')
#         for line in tie_reader:
#             data.append(line)
#     return data
#
# data_from_csv = open_with_csv('oregonpopulation.csv')
# print(data_from_csv[0])
#
# FIELDNAMES = ['FIPS*','County name','RUC code','Pop. 1990','Pop. 2000','Pop. 2010','Pop. 2017','Change 2010-17']
#
# DATATYPES = [('FIPS*', 'i'), ('County name', 'S'), ('RUC code', 'i'), ('Pop. 1990', 'i'), ('Pop. 2000', 'i'), ('Pop. 2010', 'i'), ('Pop. 2017', 'i'), ('Change 2010-2017', 'i'),]
#
# def load_data(filename, d=','):
#     my_csv = numpy.genfromtxt(filename, delimiter=d, skip_header=1, invalid_raise=False, names=FIELDNAMES, dtype=DATATYPES)
#     return my_csv
#
# my_csv = load_data('oregonpopulation.csv')

# with open('oregonpopulation.csv', newline='') as csvfile:
#     # The reader in this is like a DICT reader
#     reader = csv.DictReader(csvfile, delimiter=',')
#     rows = list(reader)
#     for row in rows[3::]:
#         print(row['population'])
#

# with open('oregonpopulation.csv', newline='') as csvfile:
#     # The reader in this is like a LIST reader
#     reader = csv.reader(csvfile, delimiter=',')
#     rows = list(reader)
#     for row in rows[3:12]:
#         print(' HHHH '.join(row))