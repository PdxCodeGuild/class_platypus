from django.shortcuts import render

from .models import Book, Author, BookCheckout

def index(request):
    return render(request, 'library/index.html', {})