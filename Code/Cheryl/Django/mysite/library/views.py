from django.shortcuts import render

from django.http import HttpResponse

import random
from .models import Books

def index(request):
    return render(request, 'library/index.html', {})