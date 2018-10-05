from django.conf.urls import url
from . import views

app_name = 'shorturl'
urlpatterns = [
    path('', views.index, name='index'),
]