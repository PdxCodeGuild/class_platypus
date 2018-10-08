from django.urls import path
from . import views

urlshort = 'urlshort'
urlpatterns = [
    path('', views.index, name='index'),
]