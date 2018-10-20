
from django.http import HttpResponse
from django.shortcuts import render

from .models import MapType


def index(request):
    return render(request, 'charts/line_chart.html', {})



def line_chart(request):
    return render(request, 'charts/line_chart.html', {})