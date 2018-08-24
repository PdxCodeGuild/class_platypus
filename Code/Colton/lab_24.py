import datetime
import re
with open('hayden_island.txt', 'r') as f:
    text = f.read()
# use regex to find the dates from the text
dates = re.findall(r'[0-9]+-[A-Z]+-[0-9]+', text)
date = [datetime.datetime.strptime(i, '%d-%b-%Y') for i in dates]
# use regex to find the total daily rain from the text then turn it into int's and take out extra spaces
totals = re.findall('(?:\d{4})( +[0-9]+)', text)
totals = [x.strip(' ') for x in totals]
totals = [int(i) for i in totals]


# take the two lists and make them a dict.
dates_totals_dict = dict(zip(date, totals))

print(dates_totals_dict[])

# find the mean of the whole thing
import statistics
numbers = [dates_totals_dict[key] for key in dates_totals_dict]
mean_ = statistics.mean(numbers)
print(mean_)


