from django.shortcuts import render, reverse
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author, Book
from django.contrib.auth.models import User

# Create your views here.
# @login_required
def index(request):
    # user = request.user
    books = Book.objects.all()
    auth = Author.objects.all()
    return render(request, 'library/index.html', {'books': books, 'auth': auth})


def check_out(request):
    book_id = request.POST['book_id']
    name = request.POST['name']
    book = Book.objects.get(pk=book_id)
    # print('book id: ' + book_id)
    # print('name: ' + name)
    # print('book title: ' + book.title)
    # print('book author: ' + book.author.full_name())
    book.checkout_name = name
    book.save()
    return HttpResponseRedirect(reverse('library:index'))



def check_in(request):
    book_id = request.POST['book_id']
    book = Book.objects.get(checkout_name=checkout_name)
    book.



    return HttpResponseRedirect(reverse('library:index'))
