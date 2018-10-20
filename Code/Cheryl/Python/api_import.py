import requests
var_name = requests.get(url="https://api.census.gov/data.json")
dict_name = var_name.json()
dict_name.keys()
dict_keys(['@context', '@id', '@type', 'conformsTo', 'describedBy', 'dataset'])
dict_name['describedBy']
'https://project-open-data.cio.gov/v1.1/schema/catalog.json'
