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
print(f'the total rain of all data is: {total_rain}')

#find the total num of days in data file
total_days = 0
for row in data:
    total_days += int(len(row) / 2)
print(f'the total number of days in the data file is: {total_days}')

#mean of rainfall
rainfall_mean = 0
for row in data:
    rainfall_mean = (total_days / total_rain)
print(f'The mean rainfall is: {rainfall_mean}')

#makes a list to call the most rainfall
text_data_two = re.findall(r'(?:\d{4})( +[0-9]+)', contents)
text_data_two = [x.strip(' ') for x in text_data_two]

print(f'\nThe most rainfall in all of the data is: {max(text_data_two)}\n')

#finds the index of most rainfall day
max_rainfall_day = text_data_two.index(max(text_data_two))

#tha date for the most rainfall
text_data_three = re.findall(r'(\d{2}-\D{3}-\d{4})', contents)
print(f'date that goes with most rainfall: {text_data_three[max_rainfall_day]}')


#which year had the most rain?




######## DELETE ############
#which day had the most rain?
# most_rain_day = 0
# for row in data:
#     most_rain_day = max(max_rain)
# print(f'The most rainy day had this much rain: {most_rain_day}\n\n')
# print(f'The max data', end=' ')
# #print(max(text_data))