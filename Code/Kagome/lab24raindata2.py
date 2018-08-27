import requests
import re
import datetime
import matplotlib.pyplot as plt
import csv

url = 'http://or.water.usgs.gov/non-usgs/bes/'


def get_locations():
    r = requests.get(url)
    locations = re.findall(r'\w+\.rain', r.text)
    locations.sort()
    return locations


def get_file(location):
    r = requests.get(url + location)
    return r.text

locations = get_locations()
text = get_file(locations[0])

print('What location would you like to read? ')
for i in range(len(locations)):
    print(f'\t{i} {locations [i]}')

location_index = int(input('> '))
contents =get_file(locations[location_index])
print(contents)

def parse_date(date_str):
    date = datetime.datetime.strptime(date_str, '%d-%b-%Y')
    return (date.year, date.month, date.day)

date = re.findall(r'\d\d\-\D\D\D\-\d\d\d\d', contents)
date = ' '.join(date).split()
daily_total = re.findall(r'\d+', contents)
daily_total = [x.strip(' ') for x in daily_total]
if daily_total == '-':
   print('None')

print(daily_total)
print(date)



#   data = re.findall()
#   data = parse_date(date)
#   data = [(parse_date(data[i][0]), int(data[i][1]) for i in range(len(data))]


def find_mean():
    total = 0
    count = 0
    mean = total / count
    for i in range(len(data)):
        if data[i][1] is not None:
            total += data[i][1]
            count += 1
    return mean

def find_var():
    v_total = 0
    count = 0
    variance = v_total / count
    for i in range(len(data)):
        if data[i][1] is not None:
            diff = data[i][1] - mean
            v_total += diff*diff
    return variance

# total = sum([row[1]) for row in data])