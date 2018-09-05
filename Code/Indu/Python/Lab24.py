import datetime
import re

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
print(raindata)
rows_2018 = [d[date] for date in d if date[0] == 2018]
print(rows_2018)

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
