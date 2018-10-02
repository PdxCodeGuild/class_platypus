from django.contrib import admin
from django.urls import include, path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('', views.index, name='index'),
    path('addcontact/', views.addcontact, name='addcontact'),
    path('deletecontact/', views.deletecontact, name='deletecontact')
]