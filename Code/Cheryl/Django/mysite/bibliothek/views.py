
# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

import random
from .models import Book, Author

def index(request):
    return render(request, 'bibliothek/index.html', {})


def check_book(request):
    book_title = request.POST['Book']
    title = Book(title=book_title)
    title.save()
    # return HttpResponseRedirect(reverse('bibliothek:index'))
    return render(request, 'bibliothek/index.html', {})

def add_book(request):
    book_title = request.POST['Book']
    title = Book(title=book_title)
    # title = Book(title=book_title, author=book_title)
    title.save()
    # return HttpResponseRedirect(reverse('bibliothek:index'))
    return render(request, 'bibliothek/index.html', {})