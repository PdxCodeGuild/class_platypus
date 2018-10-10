from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import UrlShort
# Create your views here.


def index(request):
    return render(request, 'urlshort/index.html')


# def saveUrl(request):


# def redirect(request):
