import datetime
import re
# data = [{
#     'date': '2018-08-24',
#     'daily_total': 5
# },{
#     'date': '2018-08-24',
#     'daily_total': 5
# },{
#     'date': '2018-08-24',
#     'daily_total': 5
# },{
#     'date': '2018-08-24',
#     'daily_total': 5
# },{
#     'date': '2018-08-24',
#     'daily_total': 5
# }]

with open('raindata.txt', 'r', encoding='utf-8') as f:
    contents = f.read()  # read the contents
    my_data = re.findall(r'(\d\d\-...\-\d\d\d\d) *(\d+)',contents)
    #print(my_data)
    raindata = []
for row in my_data:
    date = row[0]
    # convert it to a datetime
    date_parse = datetime.datetime.strptime(date,'%d-%b-%Y')
    daily_total = int(row[1])
    d = {
        'date': date_parse,
        'daily_total': daily_total
    }
    raindata.append(d)
#print(raindata)
rainfall = []
for row in raindata:
    rainfall.append(row['daily_total'])
mean_rainfall = sum(rainfall)/len(rainfall)
variance_rainfall = []
for i in range(len(rainfall)):
    var = (rainfall[i]-mean_rainfall)**2
    variance_rainfall.append(var)
variance = sum(variance_rainfall)/len(variance_rainfall)
print(f"The data is available for {len(rainfall)} days")
print(f"The maximum rain fall in this list is {max(rainfall)} \nThe minimun rainfall is {min(rainfall)}")
print(f"The mean rain fall for 7291 days is {mean_rainfall}")
print(f"The variance of rain fall is {variance}")
# for row in raindata:
#     print(row['date'].year)
# # for tup in my_data:
# #     raindata[tup[0]] =tup[1]
# #print(raindata)
# # dates=list(raindata.keys())
# # print(dates)
# # print(type(dates))
# # date_new =[]
# # for date in dates:
# #     date_new.append(datetime.datetime.strptime(dates(date), '%d-%b-%Y'))
# #     print(date.year)  # 2016
# #     print(date.month)  # 3
# #     print(date.day)  # 25
# #     print(date)  # 2016-03-25 00:00:00
# #     print (date.strftime('%d-%b-%Y'))  # 25-Mar-2016