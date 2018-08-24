#lab 24 version 2

import re
import datetime


def rain_file(path):
    with open(path, 'r') as f:
        return f.read()


contents = rain_file('rain_data.txt')

text_data = re.findall(r'(\d{2}\-\w{3}\-\d{4}) +(\d+)', contents)

data = []
for row in text_data:
    date = datetime.datetime.strptime(row[0], '%d-%b-%Y')
    dt = int(row[1])
    row = {
        'date': date,
        'daily_total': dt
    }
    data.append(row)

#total rainfall of all data
total_rain = 0
for row in data:
    total_rain += row['daily_total']
print(total_rain)

#find the total num of days in data file
total_days = 0
for row in data:
    total_days += int(len(row) / 2)
print(total_days)

#divide total rainfall by num of days
rainfall_mean = 0
for row in data:
    rainfall_mean = (total_days / total_rain)
print(rainfall_mean)