
import datetime

# open the data file
with open('rain.txt', 'r') as f:
    contents = f.read().split('\n')
contents = contents[11:]

data = []
for line in contents:
    if line == '':
        continue
    date = line[:11]
    date = datetime.datetime.strptime(date, '%d-%b-%Y')
    daily_total = line[11:17].strip()
    if daily_total == '-':
        continue
    daily_total = int(daily_total)
    my_dict = {
        'date': date,
        'daily_total': daily_total
    }
    data.append(my_dict)


# find the sum of the rain to find the average
total = 0
for row in data:
    total += row['daily_total']
    print(data)
# for i in range(len(data)):
#     total += data[i]['daily_total']
