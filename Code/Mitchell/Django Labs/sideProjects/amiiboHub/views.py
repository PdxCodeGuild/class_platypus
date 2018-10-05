from django.http import HttpResponse
from django.shortcuts import render, reverse


def index(request):
    #return HttpResponse("Hello, world. You're at the amiibo Hub's index.")
    return render(request, 'amiiboHub/index.html', )
