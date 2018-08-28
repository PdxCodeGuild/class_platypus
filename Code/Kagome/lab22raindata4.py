import datetime
import re
import requests


url = 'http://or.water.usgs.gov/non-usgs/bes/'


def get_locations():
    r = requests.get(url)
    locations = re.findall(r'\w+\.rain', r.text)
    locations.sort()
    return locations


def get_file(location):
    r = requests.get(url + location)
    return r.text


def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%d-%b-%Y')



locations = get_locations()
location = locations[12]
print('using location: ' + location)
text = get_file(locations[12])



data = re.findall('(\d{2}-\w{3}-\d{4}) + (\d+)', text)
# data = [parse_date(data)[i](0)], int(data[i](1))
print(data)




def find_mean_and_variance(data):
    total = 0
    count = 0
    for i in range(len(data)):
        if data[i][1] is not None:
            total += int(data[i][1])
            count += 1

    mean = total / count

    variance_total = 0
    for i in range(len(data)):
        if data[i][1] is not None:
            diff = int(data[i][1]) - mean
            variance_total += diff * diff
    variance = variance_total / count

    return mean, variance
print(find_mean_and_variance(data))