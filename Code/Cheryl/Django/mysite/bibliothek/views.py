
# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

import random
from .models import Books, Circulation, Author

def index(request):
    return render(request, 'bibliothek/index.html', {})