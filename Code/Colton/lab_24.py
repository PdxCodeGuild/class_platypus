import datetime
import re
with open('hayden_island.txt', 'r') as f:
    text = f.read()
# use regex to find the dates from the text
dates = re.findall(r'[0-9]+-[A-Z]+-[0-9]+', text)
dates = [datetime.datetime.strptime(i, '%d-%b-%Y') for i in dates]


# use regex to find the total daily rain from the text then turn it into int's and take out extra spaces
totals = re.findall('(?:\d{4})( +[0-9]+)', text)
totals = [x.strip(' ') for x in totals]
totals = [int(i) for i in totals]


# take the two lists and make them a dict.
dates_totals_dict = []
for i in range(len(totals)):
    dates_totals_dict.append({
        'date': dates[i],
        'daily_total': totals[i]
    })


import statistics

# # find the mean of the whole thing in tips
numbers = [dates_totals_dict[i]['daily_total'] for i in range(len(dates_totals_dict))]
avg = statistics.mean(numbers)

#avg rainfall for 2018
dt_2018 = 0
count_2018 = 0
for row in dates_totals_dict:
    if row['date'].year == 2018:
        dt_2018 += row['daily_total']
        count_2018 += 1
print(dt_2018/count_2018)

# plot of all data over the years
import matplotlib.pyplot as plt
x_values = [dates_totals_dict[i]['date'] for i in range(len(dates_totals_dict))]
y_values = [dates_totals_dict[i]['daily_total'] for i in range(len(dates_totals_dict))]
plt.plot(x_values, y_values)
plt.show()




