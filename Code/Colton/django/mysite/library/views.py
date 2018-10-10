from django.shortcuts import render
from .models import Book, Author

def index(request):
    books = Book.objects.all
    return render(request, 'library/index.html', {'books': books})

