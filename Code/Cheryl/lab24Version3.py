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
    date = datetime.datetime.strptime(row[0], '%d-%b-%Y')
    dt = int(row[1])
    row = {
        'date': date,
        'daily_total': dt
    }
    data.append(row)

plt.plot(date, dt)
plt.show()


import matplotlib.pyplot as plt

plt.bar(range(len(row)), list(row.values()), align='center')
plt.xticks(range(len(row)), list(row.keys()))