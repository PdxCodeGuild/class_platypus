import datetime
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
# Puts all included years in an ordered list
years = {drr[0].year for drr in daily_rain}
years = list(years)
years.sort()
print(years)
# Variables used for finding yearly total and average
yearly_rain = [0] * 21
days_in_year = [0] * 21
# Loop through the days & add its total to the appropriate year
for m in range(len(daily_rain)):
    for n in range(len(years)):
        # If correct year increment yearly_rain and days in year
        if daily_rain[m][0].year == years[n]:
            yearly_rain[n] = yearly_rain[n] + daily_rain[m][1]
            days_in_year[n] = days_in_year[n] + 1
print(years)
print(days_in_year)
print(yearly_rain)