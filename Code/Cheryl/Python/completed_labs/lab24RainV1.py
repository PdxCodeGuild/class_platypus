#lab 24 version 1 with user input

import re
import datetime


def rain_file(path):
    with open(path, 'r') as f:
        return f.read()


contents = rain_file('rain_data.txt')

text_data = re.findall(r'(\d{2}\-\w{3}\-\d{4}) +(\d+)', contents)
print(text_data)
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

search_value = input("Enter a date with the format 00-JAN-YEAR: ")


def row_search(text_data, search_value):
    for x in text_data:
        if x[0] == search_value:
            return x[1]


row_search(text_data, search_value)
rainfall = int(row_search(text_data, search_value)) * .01

print(f'The rain on {search_value} was: {rainfall} of an inch.  ')
