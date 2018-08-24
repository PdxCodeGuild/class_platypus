#lab 24 version 1

import datetime
import re

with open('rain_data.txt', 'r') as f:
    contents = f.read()

#trying to figure out regex
matchObject = re.search(' ', contents, flags=0)
print(matchObject)

#
#
# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016