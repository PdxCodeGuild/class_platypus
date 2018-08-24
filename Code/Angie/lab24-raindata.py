
import datetime

# open the data file
with open('rain.txt', 'r') as f:
    contents = f.read().split('\n')
contents = contents[11:]

data = []

for line in contents:
    date = line[:11]
    daily_total = line[11:17].strip()
    #print(f'{date} {daily_total}')
    my_dict = {
        'date': date,
        'daily_total': daily_total
    }
    data.append(my_dict)
    sep_date = datetime.datetime.strptime(date, '%d-%b-%Y')
    # print(sep_date.year)   # 2016
    # print(sep_date.month)  # 3
    # print(sep_date.day)    # 25
    # print(sep_date)  # 2016-03-25 00:00:00
    # print(sep_date.strftime('%d-%b-%Y'))  # 25-Mar-2016
    counter = str(0)
    for num in daily_total:
        counter += num
    print(daily_total)






