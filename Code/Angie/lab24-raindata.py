import re
import datetime

# open the data file
with open('rain.txt', 'r') as f:
    contents = f.read().split('\n')
contents = contents[11:]
# data = [{
#     'date': '23-AUG-2018',
#     'daily_total': 0
# },{
#     'date': '24-AUG-2018',
#     'daily_total': 0
# },{
#     'date': '25-AUG-2018',
#     'daily_total': 0
# },{
#     'date': '26-AUG-2018',
#     'daily_total': 0
# }]
data = []
for line in contents:
    data.append(line[:17])
    #date = data
    #daily_total =


    # date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
    #  print(date.year)   # 2016
     # print(date.month)  # 3
     # print(date.day)    # 25
     # print(date)  # 2016-03-25 00:00:00
     # print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016



print(data)

# open the file
# create a list of tuples/dictionaries-need date and daily total
#


