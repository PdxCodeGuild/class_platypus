

import requests
import json

#api key/token

api_url_base = 'https://api.census.gov/data.json'

def get_json(url):
    return json.loads(requests.get(url).text)

def get_data(title, datasets):
    for dataset in datasets['dataset']:
        #print(dataset['title'])
        if dataset['title'] == title:
            variables_url = dataset['c_variablesLink']
            values_url = dataset['c_valuesLink']
            variables = get_json(variables_url)
            values = get_json(values_url + '?key=' + api_key)

            print(variables)
            print()
            print()
            print()
            print()
            print()
            print(values)


datasets = get_json(api_url_base)
get_data('County Total Population and Components of Change', datasets)






