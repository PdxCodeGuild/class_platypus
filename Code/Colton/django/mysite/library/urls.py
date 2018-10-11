
from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<int:book_id>', views.checkout, name='checkout'),
    # path('checkin/<book>', views.checkin, name='checkin'),
    ]