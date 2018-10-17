from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Author, Book
from django.contrib.auth.models import User

# Create your views here.
# @login_required
def index(request):
    # user = request.user
    paper_back = Book.objects.all()
    auth = Author.objects.all()
    return render(request, 'library/index.html', {'paper_back': paper_back, 'auth': auth})


def check_out(request):
    book_id = request.POST['book_id']
    name = request.POST['name']
    book_id.save()
    name.save()
    return HttpResponseRedirect('library/index.html')



def check_in(request):
    book_id = request.POST['book_id']
    book_id.save()
    return HttpResponseRedirect('library/index.html')
