from django.urls import path
from . import views

app_name = 'amiiboHub'
urlpatterns = [
    path('', views.index, name='index'),
]