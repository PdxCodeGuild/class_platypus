
import datetime
import matplotlib.pyplot as plt

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
    # print(daily_total)
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
# for i in range(len(data)):
#     total += data[i]['daily_total']

mean = total / len(data)
# print(mean)
# print(total)
# print(len(data))

# Use the mean to calculate the variance:
v = 0
for row in data:
    v += (row['daily_total'] - mean) ** 2

variance = v / len(data)
std = variance ** 0.5  # square root
# print(std)


# find the day that had the most rain
# Find the year which had the most rain on average
max_rain = 0
max_day = 0
for i in range(len(data)):
    if data[i]['daily_total'] > max_rain:
        max_rain = data[i]['daily_total']
        max_day = data[i]['date']
        value = max_rain * .01

print(f'The day with the most rain on average is {max_day.month}/{max_day.day}/{max_day.year} with {max_rain} tips or {value} in.')


# all the data, date vs daily total
days = []
daily_rain = []
for day in range(len(data)):
    days.append(data[day]['date'].year)
    daily_rain.append(data[day]['daily_total'])
    print(days)
    print(daily_rain)

    plt.plot('daily_total', 'days')
    plt.ylabel('Date')
    plt.xlabel('Total Rain')
    plt.show()

