import datetime
import re
from datetime import date
from datetime import time
from datetime import datetime



def rain_file(path):
    with open(path, 'r') as f:
        return f.read()


contents = rain_file('rain_test.txt')

year = re.findall(r'(?:\d\d-\D{3}-)+(\d{4})', contents)
year = [s.strip('-') for s in year] # remove the 8 from the string borders

rain = re.findall(r'(?:\d\d-\D{3}-\d{4}) +(\d+)', contents)


# text_data_dictionary = dict(zip(year, rain))

# to find indexes
to_find_i_year = [i for i, x in enumerate(year) if x == "2018"]
to_find_i_rain = [i for i, x in enumerate(rain) if x == '0']

# to find the average rain per year

T = ''

for years in year:
    print(T)
    T += years

# average = sum(nums) / len(nums)
average = T / len(year)
print(f'The floor division average is: {average}')


# test = year.index('2018')
# print(year)
print(to_find_i_year)
for i in to_find_i_year:
    print(rain[to_find_i_year])
# print(to_find_i_rain)



# data = []
# for row in text_data:
#     date = row[0]
#     dt = row[1]
#     row = {
#         'date': date,
#         'daily_total': dt
#     }
#     data.append(row)
# print(row)

#
# def main():
#     #get today's date
#     today = date.today()
#     print('Today is: ', today)
#
# today = date.today()
# print("Date Components:", today.day, today.month, today.year)
#
# wd = date.weekday(today)
# days = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
#
# print("Today is day number %d" % wd)
# print('Which is a ' + days[wd])
#
# if __name__ == '__main__':
#     main()
#

