import datetime
import re


with open('raindata.txt', 'r', encoding='utf-8') as f:
    contents = f.read()  # read the contents
    my_data = re.findall(r'(\d\d\-...\-\d\d\d\d) *(\d+)',contents)
    #print(my_data)
     #date = re.findall(r'\d\d\-\D\D\D\-\d\d\d\d', contents)
    #print(len(date))
    raindata = {}
    for tup in my_data:
        raindata[tup[0]] =tup[1]
    #print(raindata)
    dates=list(raindata.keys())
    print(dates)
    print(type(dates))
    date_new =[]
    for date in dates:
        date_new.append(datetime.datetime.strptime(dates(date), '%d-%b-%Y'))
        print(date.year)  # 2016
        print(date.month)  # 3
        print(date.day)  # 25
        print(date)  # 2016-03-25 00:00:00
        print (date.strftime('%d-%b-%Y'))  # 25-Mar-2016