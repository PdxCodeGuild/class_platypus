
import datetime


def rain_data(path):  # open the data file
    with open(path, 'r') as f:
        contents = f.read().split('\n')

        data = {}
        # date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
        # print(date.year)   # 2016
        # print(date.month)  # 3
        # print(date.day)    # 25
        # print(date)  # 2016-03-25 00:00:00
        # print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
    return data

data = rain_data('rain.txt')
print()


# open the file
# create a list of tuples/dictionaries
#


