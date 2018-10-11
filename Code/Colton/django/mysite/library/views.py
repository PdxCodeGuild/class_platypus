from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Author
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    books = Book.objects.all
    return render(request, 'library/index.html', {'books': books})


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('library:index'))


def login_page(request):
    return render(request, 'library/login.html')


def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('library:index'))
    else:
        return HttpResponseRedirect(reverse('library:login'))


def logout_view(request):
    logout(request)
    return render(request, 'library/logout.html')


@login_required(login_url='http://localhost:8000/library/login/')
def checkout(request, book_id):
    book = Book.objects.get(pk=book_id)
    if Book.checked_out is True:
        return HttpResponse('That book is already checked out.')
    else:
        return render(request, 'library/detail.html', {'book': book})


def book_checkout(request, book_id):
    book = Book.objects.get(pk=book_id, checked_out=True)
    book.checked_out = True
    return HttpResponse('You have checked out the book.')


