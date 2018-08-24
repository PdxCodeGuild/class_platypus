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


def get_info(path):
    with open(path, 'r') as f:
        contents = f.read()

    date = re.findall(r'\d\d\-\D\D\D\-\d\d\d\d', contents)
    # date = ' '.join(date).split()
    daily_total = re.findall(r'\     \d    ', contents)
    daily_total = [x.strip(' ') for x in daily_total]
    k = list(zip(date, daily_total))
    get_info_dict = {}
    ########
    for (x, y) in k:
        if x in get_info_dict:
            get_info_dict[x] = d[x] + y
        else:
            get_info_dict[x] = y
    ########
    
    print(get_info_dict)
    return daily_total

get_info('rain_test.txt')







#
# date = datetime.datetime.strptime(get_date('rain_test.txt'), '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016