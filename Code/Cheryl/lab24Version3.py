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

plt.plot([row['date'] for row in data if row['date'].year == 2015],
         [row['daily_total'] for row in data if row['date'].year == 2015])

plt.show()

