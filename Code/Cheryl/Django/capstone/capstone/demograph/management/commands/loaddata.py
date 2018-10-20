

from django.core.management.base import BaseCommand
import requests
import json

api_key = '35cfed388d369e78f29d2be64e38f5365b7c92c9'


def get_json(url):
    return json.loads(requests.get(url).text)

def get_data(title, datasets):
    for dataset in datasets['dataset']:
        #print(dataset['title'])
        if dataset['title'] == title:
            variables_url = dataset['c_variablesLink']
            values_url = dataset['c_valuesLink']
            print(variables_url)
            print(values_url)



datasets = get_json('https://api.census.gov/data.json')
get_data('Vintage 2014 Population Estimates: County Total Population and Components of Change', datasets)










