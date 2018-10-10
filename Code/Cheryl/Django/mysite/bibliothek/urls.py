from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'bibliothek'
urlpatterns = [
    path('', views.index, name='index'),
    path('check_book/', views.check_book, name='check_book'),
    path('add_book/', views.add_book, name='add_book'),
]