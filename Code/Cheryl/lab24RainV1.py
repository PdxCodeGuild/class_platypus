#lab 24 version 1

########################################

import requests
import re
import datetime
import ast

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


# def get_info(path):
#     with open(path, 'r') as f:
#         contents = f.read()
#
#     date = re.findall(r'\d\d\-\D\D\D\-\d\d\d\d', contents)
#     # date = ' '.join(date).split()
#     daily_total = re.findall(r'\     \d    ', contents)
#     daily_total = [x.strip(' ') for x in daily_total]
#     k = list(zip(date, daily_total))
#     get_info_dict = {}
#     ########
#     for (x, y) in k:
#         if x in get_info_dict:
#             get_info_dict[x] = d[x] + y
#         else:
#             get_info_dict[x] = y
#     ########
#
#     return get_info_dict
#
# get_info('rain_test.txt')


with open('rain_test.txt', 'r') as f:
    contents = f.read()

dates = re.findall(r'\d\d\-\D\D\D\-\d\d\d\d', contents)
daily_totals = re.findall(r'\     \d    ', contents)
daily_totals = [x.strip() for x in daily_totals]

# print(f"Dates: {dates}")
# print(f'Daily Totals: {daily_totals}')

data = []
for i in range(len(dates)):
    date = datetime.datetime.strptime(dates[i], '%d-%b-%Y')
    daily_total = daily_totals[i]
    row = {
        'date': date,
        'daily_total': daily_total
    }
print(row)
# print(date)
# print(date.month)



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