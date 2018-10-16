from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author, Book

# Create your views here.
def index(request):
    paper_back = Book.objects.all()
    return render(request, 'library/index.html', {'paper_back': paper_back})


def check_out(request):
    book_id = request.POST['book_id']
    name = request.POST['name']


def check_in(request):
    book_id = request.POST['book_id']
