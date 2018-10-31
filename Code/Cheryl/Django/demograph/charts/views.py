
from django.http import HttpResponse
from django.shortcuts import render
import requests



# def index(request):
#     return render(request, 'charts/graphs.html', {})
#
#
#
# def line_chart(request):
#     return render(request, 'charts/graphs.html', {})




def index(request):
    county = {}
    if 'county:*' in request.GET:
        county_ext = request.GET['county:*']
        url = 'https://api.census.gov/data/2015/acs1?get=NAME,B17003_002E&for=' % county_ext
        response = requests.get(url)
        county = response.json()
    return render(request, 'charts/graphs.html', {'county': county})

