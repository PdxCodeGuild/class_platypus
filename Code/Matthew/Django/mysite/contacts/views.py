from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect


from .models import Contact

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {'contacts': contacts})


def addcontact(request):
    name = request.POST['name']
    age = request.POST['age']
    phone = request.POST['phone']
    gender = request.POST['gender']

    contact = Contact(name=name, age=age, phone_number=phone, gender=gender)
    contact.save()

    return HttpResponseRedirect(reverse('contacts:index'))


def deletecontact(request):
    id = request.POST['id']
    contact = Contact.objects.get(pk=id)
    contact.delete()

    return HttpResponseRedirect(reverse('contacts:index'))

