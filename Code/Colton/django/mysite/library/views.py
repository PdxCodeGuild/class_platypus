from django.shortcuts import render
from .models import Book, Author

def index(request):
    checkout = Book.objects.get('title')
    return render(request, 'library/index.html', {'checkout': checkout})

