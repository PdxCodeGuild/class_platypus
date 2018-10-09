from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
# from .models import MODEL_CLASS
import string


def index(request):

    return render(request, 'library/index.html', {})