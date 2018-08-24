#lab 24 version 1

########################################

import requests
import re
import datetime
import math


#
# url = 'https://or.water.usgs.gov/non-usgs/bes/'
#
#
# def get_locations():
#     r = requests.get(url)
#     locations = re.findall(r'\w+\.rain', r.text)
#     locations.sort()
#     return locations
#
#
# def get_file(location):
#     r = requests.get(url + location)
#     return r.text
#
#
# locations = get_locations()
#
# print('which location would you like to see?')
# for i in range(len(locations)):
#     print(f'\t{i} {locations[i]}')
#
# location_index = int(input('> '))
#
# print(get_file(locations[location_index]))

########################################################################


def rain_file(path):
    with open(path, 'r') as f:
        return f.read()


contents = rain_file('rain_test.txt')

text_data = re.findall(r'(\d{2}\-\w{3}\-\d{4}) +(\d+)', contents)
# print(f'printing the data: {text_data}')


data = []
for row in text_data:
    date = datetime.datetime.strptime(row[0], '%d-%b-%Y')
    dt = int(row[1])


for i in range(len(data)):
    date = datetime.datetime.strptime(date[i], '%d-%b-%Y')
    dt = dt[i]
    row = {
        'date': date,
        'daily_total': dt
    }

search_value = print(input("Enter a date: "))

def row_search(text_data, search_value):
    for x in text_data:
        if x[0] == search_value:
            return x[1]

print(row[1])
print(row_search(text_data, '22-AUG-2018'))

#
# print(type(data))
# print(row[0])
# print(date)












#
# print(f'printint row {row}')
#
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016



#
# data = []
# for i in range(len(data)):
#     date = datetime.datetime.strptime(date[i], '%d-%b-%Y')
#     dt = dt[i]
#     row = {
#         'date': date,
#         'daily_total': dt
#     }
# print(f'printing data {data}')
# print(f'printing date {date}')
# # print(f'print the motnh {date.month}')



# data = [{
#     'date': '2018-08-14',
#     'daily_total': 0
# },{
#     'date': '2018-08-14',
#     'daily_total': 0
# },{
#     'date': '2018-08-14',
#     'daily_total': 0
# },{
#     'date': '2018-08-14',
#     'daily_total': 0
# }]