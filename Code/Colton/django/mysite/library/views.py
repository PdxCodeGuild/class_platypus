from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author


def index(request):
    books = Book.objects.all
    return render(request, 'library/index.html', {'books': books})


def checkout(request, book_id):
    book = Book.objects.get(pk=book_id)
    if Book.checked_out:
        return HttpResponse('That book is already checked out.')
    else:
        return render(request, 'library/detail.html', {'book': book})



