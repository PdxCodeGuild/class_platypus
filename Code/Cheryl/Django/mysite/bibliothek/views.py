
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


import random
from datetime import datetime
from .models import Book, Author

def index(request):
    authors = Author.objects.all()
    # books = Book.objects.get()
    books = Book.objects.all()
    return render(request, 'bibliothek/index.html', {'authors': authors, 'books': books})


def check_book(request):
    book_title = request.POST['Book']
    title = Book(title=book_title)
    title.save()
    return render(request, 'bibliothek/index.html', {})

def add_book(request):
    book_title = request.POST['book']
    author_id = request.POST['author_id']
    pub_date = request.POST['pub_date']
    pub_date = datetime.strptime(pub_date, '%Y-%m-%d')

    # get the author id, add it to the book

    # author = Author.objects.get(pk=author_id)

    title = Book(title=book_title, author_id=author_id, pub_date=pub_date)
    title.save()
    return render(request, 'bibliothek/index.html', {})

def check_author(request):
    author = request.POST['Author']
    author_name = Author(name=author)
    author_name.save()
    return render(request, 'bibliothek/index.html', {})
