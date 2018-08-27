import matplotlib.pyplot as plt
import re
import datetime


def rain_file(path):
    with open(path, 'r') as f:
        return f.read()


contents = rain_file('rain_data.txt')

text_data = re.findall(r'(\d{2}\-\w{3}\-\d{4}) +(\d+)', contents)

data = []
for row in text_data:
    date = row[0]
    date = datetime.datetime.strptime(row[0], '%d-%b-%Y')
    dt = int(row[1])
    row = {
        'date': date,
        'daily_total': dt
    }
    data.append(row)

#green triangles show the same months over all of the years.
plt.plot([row['date'] for row in data if row['date'].month == 8],
         [row['daily_total'] for row in data if row['date'].month == 8], 'g^')

#red dots shows rain over a specific year
plt.plot([row['date'] for row in data if row['date'].year == 2018],
         [row['daily_total'] for row in data if row['date'].year == 2018], 'ro')

plt.show()

