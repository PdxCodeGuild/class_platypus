import datetime
import re
# Calculates the mean for a tuple list of daily rain
def mean_finder(tups):
    sum_total = 0
    for j in range(len(tups)):
        sum_total += tups[j][1]
    return sum_total / len(tups)
# Finds the day/year with the most daily rain in list
def most_rain(tups):
    most = 0
    most_day = tups[0][0]
    for k in range(len(tups)):
        if tups[k][1] > most:
            most = tups[k][1]
            most_day = tups[k][0]
    return (most_day, most)
# Opens and copies the text of a book's .txt file
with open('hayden_island.rain.txt', 'r') as f:
    input_text = f.read()
# Removes all stuff up until data starts
data_list = input_text.splitlines()
data_list = data_list[11:]
daily_rain = []
# Loops through each line and removes date and daily total
for i in range(len(data_list)):
    curr_line = data_list[i]
    # Save the date with a time strip for each row
    date_string = curr_line[:11]
    date = datetime.datetime.strptime(date_string, '%d-%b-%Y').date()
    # If no data is given for the date, do not include it
    if curr_line[11:20] == '     -   ':
        continue
    # Save the daily total for each date in a list of tuples
    else:
        daily_total = float(curr_line[11:20])
        daily_rain.append((date, daily_total))
print(str(mean_finder(daily_rain)))
print(most_rain(daily_rain))